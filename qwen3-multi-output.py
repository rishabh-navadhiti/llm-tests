import json
import time
import subprocess
import logging
from pathlib import Path
import re
from typing import Optional, List, Dict
import requests
import os
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load environment variables
load_dotenv()

# ==================== CONFIGURATION ====================
# Model and API settings - UPDATED FOR QWEN3
MODEL_NAME = "Qwen/Qwen3-30B-A3B-Instruct-2507"  # Using the latest Instruct variant
VLLM_API_URL = "http://localhost:8000/v1/chat/completions"

# Path settings
INPUT_DIR = Path("/workspace/llm-tests/evaluation/testiing/trans")
OUTPUT_DIR = Path("/workspace/llm-tests/newTest/test")  # Updated output directory
TEMPLATE_PATH = Path("/workspace/llm-tests/templates/doctor-template-specialized-v2.json")
PROMPT_PATH = Path("/workspace/llm-tests/prompt-v2.txt")

# Generation parameters - OPTIMIZED FOR QWEN3
MAX_TOKENS = 4000  # Increased for potential thinking tokens
TEMPERATURE = 0.2  # Lower for medical accuracy :cite[2]
TOP_P = 0.3
TOP_K = 40
FREQUENCY_PENALTY = 0.1
PRESENCE_PENALTY = 0.1

# Request settings
REQUEST_TIMEOUT = 900  # Increased timeout for thinking mode
MAX_CONCURRENT_REQUESTS = 12  # Adjusted for MoE architecture :cite[7]


# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Qwen3-specific settings
ENABLE_THINKING = False  # Set to True for complex reasoning tasks :cite[1]:cite[7]
# =======================================================

def show_gpu_memory(note: str = "") -> None:
    """Display GPU memory usage"""
    try:
        output = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.used,memory.total", "--format=csv,nounits,noheader"],
            timeout=10,
        )
        for i, line in enumerate(output.decode().strip().split("\n")):
            used, total = map(int, line.split(","))
            usage_pct = used / total * 100
            logger.info(f"📊 GPU {i} Memory {note}: {used} MiB / {total} MiB ({usage_pct:.1f}%)")
    except Exception as e:
        logger.warning(f"⚠️ Could not read GPU memory: {e}")

def load_core_instructions() -> str:
    """Load the core instructions from the prompt file"""
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read().strip()

def load_json_template() -> str:
    """Load and return the JSON template as a formatted string"""
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template_data = json.load(f)
    return json.dumps(template_data, indent=2)

def build_full_prompt(transcript_text: str) -> str:
    """
    Construct the complete prompt by combining:
    1. Core instructions
    2. JSON template
    3. Formatted transcript
    
    Updated for Qwen3's instruction format :cite[6]
    """
    core_instructions = load_core_instructions()
    json_template = load_json_template()
    
    # Qwen3 responds well to structured instructions
    full_prompt = (
        f"<|im_start|>system\n{core_instructions}\n\n"
        "### TEMPLATE TO POPULATE:\n"
        f"{json_template}<|im_end|>\n\n"
        "<|im_start|>user\n"
        "### MEDICAL TRANSCRIPT:\n"
        f"{transcript_text}\n\n"
        "Please generate a structured medical note in JSON format that exactly follows the provided template."
        "Extract information faithfully from the transcript without adding any information not present.<|im_end|>\n\n"
        "<|im_start|>assistant\n"
    )
    
    return full_prompt

def load_transcript(file_path: Path) -> str:
    """Load a transcript file and format it with speaker labels"""
    with open(file_path, "r", encoding="utf-8") as f:
        transcript_data = json.load(f)
    
    # Format the transcript into a readable string with speaker labels
    formatted_transcript = ""
    for entry in transcript_data:
        speaker = entry.get("speaker", "unknown").capitalize()
        conversation = entry.get("conversation", "")
        formatted_transcript += f"{speaker}: {conversation}\n"
    
    return formatted_transcript.strip()

def generate_single_request(transcript: str, transcript_name: str) -> dict:
    """Generate a response for a single transcript"""
    logger.info(f"🚀 Preparing request for: {transcript_name}")
    
    # Build the complete prompt with instructions, template, and transcript
    full_prompt = build_full_prompt(transcript)
    
    # For Qwen3, we use the chat format with explicit role tags :cite[6]
    messages = [
        {"role": "user", "content": full_prompt}
    ]

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "top_k": TOP_K,
        "frequency_penalty": FREQUENCY_PENALTY,
        "presence_penalty": PRESENCE_PENALTY,
        "stop": ["<|im_end|>", "</think>"]  # Qwen3-specific stop tokens :cite[6]
    }

    # Add thinking mode parameter if enabled
    if ENABLE_THINKING:
        payload["reasoning"] = True
        logger.info(f"🤔 Thinking mode enabled for {transcript_name}")

    try:
        start_time = time.time()
        resp = requests.post(VLLM_API_URL, json=payload, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        gen_time = time.time() - start_time
        
        data = resp.json()
        output_text = data["choices"][0]["message"]["content"].strip()
        
        logger.info(f"✅ Received response for {transcript_name} in {gen_time:.2f}s")
        return {"success": True, "text": output_text, "name": transcript_name}
    
    except requests.RequestException as e:
        logger.error(f"Request failed for {transcript_name}: {e}")
        return {"success": False, "error": str(e), "name": transcript_name}
    except Exception as e:
        logger.error(f"Unexpected error processing {transcript_name}: {e}")
        return {"success": False, "error": str(e), "name": transcript_name}

def extract_json(response: str) -> Optional[dict]:
    """
    Robustly try to find & parse the first valid JSON object/array in `response`.
    Enhanced for Qwen3's output format which may include thinking tokens :cite[7]
    """
    if not response or not response.strip():
        return None

    # Remove thinking tags if present
    cleaned_response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL)
    
    # direct attempt
    try:
        return json.loads(cleaned_response)
    except json.JSONDecodeError:
        pass

    # try to locate JSON-like substrings
    for start_char in ("[", "{"):
        starts = [m.start() for m in re.finditer(re.escape(start_char), cleaned_response)]
        for start in starts:
            for end in range(len(cleaned_response) - 1, start, -1):
                if cleaned_response[end] not in ("}", "]"):
                    continue
                candidate = cleaned_response[start : end + 1]
                try:
                    return json.loads(candidate)
                except json.JSONDecodeError:
                    continue

    # fallback patterns
    patterns = [
        r"```json\s*(\{.*?\}|\[.*?\])\s*```",
        r"```\s*(\{.*?\}|\[.*?\])\s*```",
        r"(\{.*\})",
        r"(\[.*\])",
    ]
    for p in patterns:
        matches = re.findall(p, cleaned_response, re.DOTALL)
        for m in matches:
            try:
                return json.loads(m)
            except json.JSONDecodeError:
                continue

    logger.warning("⚠️ Could not extract valid JSON from the response.")
    return None

def save_outputs(output_dir: Path, base_filename: str, raw_response: str, json_data: Optional[dict]) -> None:
    """Save both raw response and processed JSON"""
    output_dir.mkdir(parents=True, exist_ok=True)

    raw_path = output_dir / f"{base_filename}-output.json"
    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(raw_response)
    logger.info(f"✅ Raw output saved: {raw_path}")

    if json_data:
        processed_path = output_dir / f"{base_filename}-output.processed.json"
        with open(processed_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        logger.info(f"✅ JSON output saved: {processed_path}")

def main():
    total_start = time.time()
    
    logger.info(f"🚀 Processing all transcripts in {INPUT_DIR}")
    logger.info(f"📊 Using parameters: temperature={TEMPERATURE}, top_p={TOP_P}, top_k={TOP_K}")
    logger.info(f"🤔 Thinking mode: {'ENABLED' if ENABLE_THINKING else 'DISABLED'}")
    
    # Get all transcript files
    transcript_files = list(INPUT_DIR.glob("*.json"))
    logger.info(f"📄 Found {len(transcript_files)} transcript files")
    
    # Show initial GPU memory
    show_gpu_memory("before processing")
    
    # Process all transcripts concurrently
    results = []
    with ThreadPoolExecutor(max_workers=MAX_CONCURRENT_REQUESTS) as executor:
        # Submit all tasks
        future_to_transcript = {
            executor.submit(
                generate_single_request, 
                load_transcript(file), 
                file.name
            ): file for file in transcript_files
        }
        
        # Process results as they complete
        for future in as_completed(future_to_transcript):
            transcript_file = future_to_transcript[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                logger.error(f"Error processing {transcript_file.name}: {e}")
                results.append({
                    "success": False, 
                    "error": str(e), 
                    "name": transcript_file.name
                })
    
    # Save all results
    success_count = 0
    for result in results:
        if result["success"]:
            success_count += 1
            json_data = extract_json(result["text"])
            save_outputs(OUTPUT_DIR, Path(result["name"]).stem, result["text"], json_data)
        else:
            logger.error(f"Failed to process {result['name']}: {result.get('error', 'Unknown error')}")
    
    # Show final statistics
    total_time = time.time() - total_start
    logger.info(f"🎉 Processing completed in {total_time:.2f}s ({total_time/60:.2f} mins)")
    logger.info(f"📈 Success rate: {success_count}/{len(transcript_files)} ({success_count/len(transcript_files)*100:.1f}%)")
    show_gpu_memory("after processing")

if __name__ == "__main__":
    main()