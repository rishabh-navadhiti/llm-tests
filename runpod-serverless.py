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
env_path = "/Users/rish/Development/runpod dev/llm-tests/.env-local"
load_dotenv(dotenv_path=env_path)
# ==================== CONFIGURATION ====================
# RunPod OpenAI-compatible API settings
RUNPOD_ENDPOINT_ID = "87tthuuosy3dlb"
RUNPOD_API_KEY = os.getenv("RUNPOD_API_KEY")  # Should be in your .env file
RUNPOD_API_URL = f"https://api.runpod.ai/v2/{RUNPOD_ENDPOINT_ID}/openai/v1/chat/completions"

# Model name (as recognized by your RunPod endpoint)
MODEL_NAME = "Qwen/Qwen3-30B-A3B-Instruct-2507"

# Path settings
INPUT_DIR = Path("/Users/rish/Development/runpod dev/llm-tests/newTest/runpod-serverless/test-trans")
OUTPUT_DIR = Path("/Users/rish/Development/runpod dev/llm-tests/newTest/runpod-serverless/test-output")
TEMPLATE_PATH = Path("/Users/rish/Development/runpod dev/llm-tests/templates/doctor-template-specialized-v2.json")
PROMPT_PATH = Path("/Users/rish/Development/runpod dev/llm-tests/prompt-v2.txt")

# Generation parameters
MAX_TOKENS = 4000
TEMPERATURE = 0.2
TOP_P = 0.3
TOP_K = 40
FREQUENCY_PENALTY = 0.1
PRESENCE_PENALTY = 0.1

# Request settings
REQUEST_TIMEOUT = 900
MAX_CONCURRENT_REQUESTS = 4  # Reduced for API rate limits

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

def load_core_instructions() -> str:
    """Load the core instructions from the prompt file"""
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read().strip()

def load_json_template() -> str:
    """Load and return the JSON template as a formatted string"""
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template_data = json.load(f)
    return json.dumps(template_data, indent=2)

def build_messages(transcript_text: str) -> List[Dict[str, str]]:
    """
    Construct the messages array for OpenAI-compatible API
    """
    core_instructions = load_core_instructions()
    json_template = load_json_template()
    
    # Build the system message with instructions and template
    system_content = (
        f"{core_instructions}\n\n"
        "### TEMPLATE TO POPULATE:\n"
        f"{json_template}\n\n"
        "INSTRUCTION: Extract information from the medical transcript and populate the JSON template. "
        "Return ONLY valid JSON that matches the template structure."
    )
    
    # Build the user message with the transcript
    user_content = (
        "### MEDICAL TRANSCRIPT:\n"
        f"{transcript_text}\n\n"
        "Please generate a structured medical note in JSON format that exactly follows the provided template."
    )
    
    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content}
    ]

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
    """Generate a response for a single transcript using RunPod's OpenAI-compatible API"""
    logger.info(f"🚀 Preparing request for: {transcript_name}")
    
    # Build the messages array
    messages = build_messages(transcript)
    
    # Prepare the request payload for OpenAI-compatible API
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "frequency_penalty": FREQUENCY_PENALTY,
        "presence_penalty": PRESENCE_PENALTY,
        "stop": ["<|im_end|>", "###"]  # Common stop tokens
    }

    headers = {
        "Authorization": f"Bearer {RUNPOD_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        start_time = time.time()
        
        # Debug: Log the request details
        logger.debug(f"Request URL: {RUNPOD_API_URL}")
        logger.debug(f"Authorization header: Bearer {RUNPOD_API_KEY[:10]}...")
        
        # Make the request to RunPod's OpenAI-compatible API
        response = requests.post(
            RUNPOD_API_URL,
            headers=headers,
            json=payload,
            timeout=REQUEST_TIMEOUT
        )

        print(f"RAW RESPONSE: {response.text}")
        
        # Debug: Log the response status and headers
        logger.debug(f"Response status: {response.status_code}")
        logger.debug(f"Response headers: {dict(response.headers)}")
        
        response.raise_for_status()
        
        # Parse the response (standard OpenAI format)
        response_data = response.json()
        
        # Extract the generated text
        output_text = response_data["choices"][0]["message"]["content"].strip()
        
        gen_time = time.time() - start_time
        logger.info(f"✅ Received response for {transcript_name} in {gen_time:.2f}s")
        return {"success": True, "text": output_text, "name": transcript_name}
    
    except requests.RequestException as e:
        logger.error(f"Request failed for {transcript_name}: {e}")
        if hasattr(e, 'response') and e.response is not None:
            logger.error(f"Response text: {e.response.text}")
        return {"success": False, "error": str(e), "name": transcript_name}
    except Exception as e:
        logger.error(f"Unexpected error processing {transcript_name}: {e}")
        return {"success": False, "error": str(e), "name": transcript_name}

def extract_json(response: str) -> Optional[dict]:
   
    if not response or not response.strip():
        return None

    cleaned_response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL)
    
    # direct attempt
    try:
        return json.loads(cleaned_response)
    except json.JSONDecodeError:
        pass

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
    # logger.info(f"🤔 Thinking mode: {'ENABLED' if ENABLE_THINKING else 'DISABLED'}")
    
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