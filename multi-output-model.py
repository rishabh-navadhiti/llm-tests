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
# Model and API settings
# MODEL_NAME = os.getenv("VLLM_MODEL_NAME", "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B")
MODEL_NAME = "openai/gpt-oss-120b"
VLLM_API_URL = "http://localhost:8000/v1/chat/completions"

# Path settings
INPUT_DIR = Path("/workspace/llm-tests/newTest/transcripts")
OUTPUT_DIR = Path("/workspace/llm-tests/newTest/Deepseek-distill32b")
TEMPLATE_PATH = Path("/workspace/llm-tests/templates/doctor-template-specialized-v2.json")
PROMPT_PATH = Path("/workspace/llm-tests/prompt-v1.txt")

# Generation parameters - TUNE THESE
MAX_TOKENS = 2000  # Output JSON should be concise; reduce from 6000
TEMPERATURE = 0.2  # Lower for more deterministic output (recommended for structured data)
TOP_P = 0.3        # Lower for more focused sampling (recommended for structured data)
TOP_K = 40         # Moderate value for diversity control
FREQUENCY_PENALTY = 0.1  # Reduce repetition
PRESENCE_PENALTY = 0.1   # Encourage new content

# Request settings
REQUEST_TIMEOUT = 1200  # seconds
MAX_CONCURRENT_REQUESTS = 3  # Start with 16, can increase to 32 if GPU memory allows

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
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

def load_template_and_prompt() -> tuple[str, str]:
    """Load the prompt template and JSON template"""
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        prompt = f.read().strip()

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template_data = json.load(f)

    return prompt, json.dumps(template_data, indent=2)

def load_transcript(file_path: Path) -> str:
    """Load a transcript file"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def generate_single_request(system_prompt: str, template: str, transcript: str, transcript_name: str) -> dict:
    """Generate a response for a single transcript"""
    logger.info(f"🚀 Preparing request for: {transcript_name}")
    
    # Construct the system message with template
    system_content = (
        system_prompt
        + "\n\nTEMPLATE_JSON (use exactly this structure; return only JSON matching the template):\n"
        + template
        + "\n\nINSTRUCTION: Fill this JSON template with data extracted from the transcript."
        + "\n⚠️ CRITICAL: Return ONLY valid JSON that exactly matches the template."
        + " Do NOT include explanations, commentary, thoughts, or markdown/code fences."
    )

    messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": f"Medical Transcript to Process:\n\n{transcript}"},
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
    }

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
    """
    if not response or not response.strip():
        return None

    # direct attempt
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        pass

    # try to locate JSON-like substrings
    for start_char in ("[", "{"):
        starts = [m.start() for m in re.finditer(re.escape(start_char), response)]
        for start in starts:
            for end in range(len(response) - 1, start, -1):
                if response[end] not in ("}", "]"):
                    continue
                candidate = response[start : end + 1]
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
        matches = re.findall(p, response, re.DOTALL)
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
    prompt, template = load_template_and_prompt()
    
    logger.info(f"🚀 Processing all transcripts in {INPUT_DIR}")
    logger.info(f"📊 Using parameters: temperature={TEMPERATURE}, top_p={TOP_P}, top_k={TOP_K}")
    
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
                prompt, 
                template, 
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