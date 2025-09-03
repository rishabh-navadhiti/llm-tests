import json
import time
import subprocess
import logging
from pathlib import Path
import re
from typing import Optional, Dict, Any
import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# ==================== CONFIGURATION ====================
# Model and API settings
VLLM_MODEL_NAME = "Qwen/Qwen3-30B-A3B-Instruct-2507"
VLLM_API_URL = "http://localhost:8000/v1/chat/completions"

OLLAMA_MODEL_NAME = "gpt-oss:120b"
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Path settings
INPUT_DIR = Path("/workspace/llm-tests/newTest/transcripts")
OUTPUT_DIR = Path("/workspace/llm-tests/newTest/Dual-Model-Output")
TEMPLATE_PATH = Path("/workspace/llm-tests/templates/doctor-template-specialized-v2.json")
PROMPT_PATH = Path("/workspace/llm-tests/prompt-v2.txt")

# Generation parameters
MAX_TOKENS = 4000
TEMPERATURE = 0.1  # Lower temperature for medical accuracy
TOP_P = 0.3
TOP_K = 40
FREQUENCY_PENALTY = 0.1
PRESENCE_PENALTY = 0.1

# Request settings
REQUEST_TIMEOUT = 900  # Increased timeout for complex models
MAX_CONCURRENT_REQUESTS = 4  # Conservative for 120B model

# Field assignments
QWEN_FIELDS = ["PATIENT_NAME", "CHIEF_COMPLAINT", "MUSCULOSKELETAL", "IMAGING RESULTS"]
GPT_OSS_FIELDS = ["HPI_SPENCER", "ASSESSMENT", "PLAN_SPENCER"]

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
# =======================================================

def show_gpu_memory(note: str = "") -> None:
    """Monitor GPU memory usage (best-effort)."""
    try:
        output = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.used,memory.total", "--format=csv,nounits,noheader"],
            timeout=10,
        )
        for i, line in enumerate(output.decode().strip().split("\n")):
            used, total = map(int, line.split(","))
            usage_pct = used / total * 100 if total else 0.0
            logger.info(f"📊 GPU {i} Memory {note}: {used} MiB / {total} MiB ({usage_pct:.1f}%)")
    except Exception as e:
        logger.debug(f"Could not read GPU memory: {e}")

def load_template_and_prompt() -> tuple[str, Dict[str, Any]]:
    """Load system prompt and JSON template from disk."""
    for p in (PROMPT_PATH, TEMPLATE_PATH):
        if not p.exists():
            raise FileNotFoundError(f"Required file not found: {p}")

    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        system_prompt = f.read().strip()

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template_data = json.load(f)

    logger.info("✅ Template and prompt loaded successfully")
    return system_prompt, template_data

def load_transcript(file_path: Path) -> str:
    """Load a transcript file and format it with speaker labels."""
    with open(file_path, "r", encoding="utf-8") as f:
        transcript_data = json.load(f)
    
    # Format the transcript into a readable string with speaker labels
    formatted_transcript = ""
    for entry in transcript_data:
        speaker = entry.get("speaker", "unknown").capitalize()
        conversation = entry.get("conversation", "")
        formatted_transcript += f"{speaker}: {conversation}\n"
    
    return formatted_transcript.strip()

def build_qwen_prompt(system_prompt: str, template: Dict[str, Any], transcript: str) -> str:
    """Build prompt for Qwen model to extract specific fields."""
    # Create a minimal template with only Qwen's fields
    qwen_template = {field: template.get(field, "") for field in QWEN_FIELDS}
    template_json = json.dumps(qwen_template, indent=2, ensure_ascii=False)
    
    prompt_text = (
        f"{system_prompt}\n\n"
        "### INSTRUCTION:\n"
        "Extract ONLY the following fields from the medical transcript: "
        f"{', '.join(QWEN_FIELDS)}.\n\n"
        "### TEMPLATE TO POPULATE:\n"
        f"{template_json}\n\n"
        "### MEDICAL TRANSCRIPT:\n"
        f"{transcript}\n\n"
        "### OUTPUT:\n"
        "Return ONLY valid JSON that matches the template structure above. "
        "Do not include any explanations, commentary, or additional text."
    )
    
    return prompt_text

def build_gpt_oss_prompt(system_prompt: str, template: Dict[str, Any], transcript: str, qwen_output: Dict[str, Any]) -> str:
    """Build prompt for GPT-OSS model to extract specific fields using Qwen's output as context."""
    # Create a minimal template with only GPT-OSS's fields
    gpt_oss_template = {field: template.get(field, "") for field in GPT_OSS_FIELDS}
    template_json = json.dumps(gpt_oss_template, indent=2, ensure_ascii=False)
    
    # Format Qwen output for context
    extracted_info = json.dumps(qwen_output, indent=2, ensure_ascii=False)
    
    prompt_text = (
        f"{system_prompt}\n\n"
        "### INSTRUCTION:\n"
        "Based on the medical transcript and the already extracted information, "
        f"generate ONLY the following fields: {', '.join(GPT_OSS_FIELDS)}.\n\n"
        "### EXTRACTED INFORMATION (from previous analysis):\n"
        f"{extracted_info}\n\n"
        "### TEMPLATE TO POPULATE:\n"
        f"{template_json}\n\n"
        "### MEDICAL TRANSCRIPT:\n"
        f"{transcript}\n\n"
        "### OUTPUT:\n"
        "Return ONLY valid JSON that matches the template structure above. "
        "Do not include any explanations, commentary, or additional text."
    )
    
    return prompt_text

def generate_with_vllm(prompt: str, model_name: str) -> str:
    """Generate response using vLLM API."""
    messages = [{"role": "user", "content": prompt}]
    
    payload = {
        "model": model_name,
        "messages": messages,
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "top_k": TOP_K,
        "frequency_penalty": FREQUENCY_PENALTY,
        "presence_penalty": PRESENCE_PENALTY,
        "stop": ["<|im_end|>", "</think>"]
    }
    
    try:
        start_time = time.time()
        resp = requests.post(VLLM_API_URL, json=payload, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        
        data = resp.json()
        output_text = data["choices"][0]["message"]["content"].strip()
        
        gen_time = time.time() - start_time
        logger.info(f"✅ vLLM response received in {gen_time:.2f}s")
        return output_text
    except Exception as e:
        logger.error(f"vLLM request failed: {e}")
        raise

def generate_with_ollama(prompt: str, model_name: str) -> str:
    """Generate response using Ollama API."""
    payload = {
        "model": model_name,
        "prompt": prompt,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
        "stream": False,
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        start_time = time.time()
        resp = requests.post(OLLAMA_API_URL, json=payload, headers=headers, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        
        response_data = resp.json()
        output_text = response_data.get("response", "").strip()
        
        gen_time = time.time() - start_time
        logger.info(f"✅ Ollama response received in {gen_time:.2f}s")
        return output_text
    except Exception as e:
        logger.error(f"Ollama request failed: {e}")
        raise

def extract_json(response: str) -> Optional[Any]:
    """Extract first valid JSON object/array from model output."""
    if not response or not response.strip():
        return None
    
    # Try direct parsing first
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        pass
    
    # Try to find JSON in the response using various patterns
    patterns = [
        r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}',  # JSON object
        r'\[[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*\]',  # JSON array
        r'```json\s*(\{.*?\}|\[.*?\])\s*```',  # JSON in code block
        r'```\s*(\{.*?\}|\[.*?\])\s*```',  # JSON in code block without language
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, response, re.DOTALL)
        for match in matches:
            try:
                return json.loads(match)
            except json.JSONDecodeError:
                continue
    
    # Try to find the outermost JSON structure
    brace_level = 0
    start_idx = -1
    
    for i, char in enumerate(response):
        if char == '{':
            if brace_level == 0:
                start_idx = i
            brace_level += 1
        elif char == '}':
            brace_level -= 1
            if brace_level == 0 and start_idx >= 0:
                candidate = response[start_idx:i+1]
                try:
                    return json.loads(candidate)
                except json.JSONDecodeError:
                    continue
    
    logger.warning("⚠️ Could not parse JSON from response")
    return None

def save_outputs(output_dir: Path, base_filename: str, raw_response: str, json_data: Optional[Any] = None) -> None:
    """Save raw response and processed JSON to output directory."""
    output_dir.mkdir(parents=True, exist_ok=True)

    raw_path = output_dir / f"{base_filename}-output.json"
    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(raw_response)
    logger.info(f"✅ Raw output saved: {raw_path}")

    if json_data is not None:
        processed_path = output_dir / f"{base_filename}-output.processed.json"
        with open(processed_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        logger.info(f"✅ JSON output saved: {processed_path}")
    else:
        logger.warning("⚠️ No valid JSON data to save")

def process_single_transcript(transcript_file: Path, system_prompt: str, full_template: Dict[str, Any]) -> Dict[str, Any]:
    """Process a single transcript with both models."""
    transcript_name = transcript_file.name
    logger.info(f"📄 Processing: {transcript_name}")
    
    try:
        transcript = load_transcript(transcript_file)
        logger.info(f"📝 Transcript length: {len(transcript)} characters")
    except Exception as e:
        logger.error(f"Failed to load transcript {transcript_name}: {e}")
        return {"success": False, "error": f"Load failed: {e}", "name": transcript_name}
    
    # Step 1: Generate with Qwen
    try:
        qwen_prompt = build_qwen_prompt(system_prompt, full_template, transcript)
        qwen_response = generate_with_vllm(qwen_prompt, VLLM_MODEL_NAME)
        qwen_json = extract_json(qwen_response)
        
        if not qwen_json:
            logger.error(f"Failed to extract JSON from Qwen for {transcript_name}")
            return {"success": False, "error": "Qwen JSON extraction failed", "name": transcript_name}
            
        logger.info("✅ Qwen processing completed successfully")
    except Exception as e:
        logger.error(f"Qwen processing failed for {transcript_name}: {e}")
        return {"success": False, "error": f"Qwen failed: {e}", "name": transcript_name}
    
    # Step 2: Generate with GPT-OSS
    try:
        gpt_oss_prompt = build_gpt_oss_prompt(system_prompt, full_template, transcript, qwen_json)
        gpt_oss_response = generate_with_ollama(gpt_oss_prompt, OLLAMA_MODEL_NAME)
        gpt_oss_json = extract_json(gpt_oss_response)
        
        if not gpt_oss_json:
            logger.error(f"Failed to extract JSON from GPT-OSS for {transcript_name}")
            return {"success": False, "error": "GPT-OSS JSON extraction failed", "name": transcript_name}
            
        logger.info("✅ GPT-OSS processing completed successfully")
    except Exception as e:
        logger.error(f"GPT-OSS processing failed for {transcript_name}: {e}")
        return {"success": False, "error": f"GPT-OSS failed: {e}", "name": transcript_name}
    
    # Combine results from both models
    combined_json = {**qwen_json, **gpt_oss_json}
    
    # Save outputs
    base_filename = transcript_file.stem
    save_outputs(OUTPUT_DIR, base_filename, f"Qwen Response:\n{qwen_response}\n\nGPT-OSS Response:\n{gpt_oss_response}", combined_json)
    
    return {"success": True, "name": transcript_name, "data": combined_json}

def main():
    total_start = time.time()
    
    logger.info(f"🚀 Starting dual-model processing")
    logger.info(f"📊 Qwen 30B will handle: {', '.join(QWEN_FIELDS)}")
    logger.info(f"📊 GPT-OSS 120B will handle: {', '.join(GPT_OSS_FIELDS)}")
    
    # Load system prompt and template
    try:
        system_prompt, full_template = load_template_and_prompt()
    except Exception as e:
        logger.error(f"Failed to load template or prompt: {e}")
        return
    
    # Get all transcript files
    transcript_files = list(INPUT_DIR.glob("*.json"))
    if not transcript_files:
        logger.error(f"❌ No JSON files found in {INPUT_DIR}")
        return
    
    logger.info(f"📄 Found {len(transcript_files)} transcript files to process")
    show_gpu_memory("before processing")
    
    # Process transcripts with limited concurrency due to GPU memory constraints
    results = []
    with ThreadPoolExecutor(max_workers=MAX_CONCURRENT_REQUESTS) as executor:
        # Submit all tasks
        future_to_file = {
            executor.submit(process_single_transcript, file, system_prompt, full_template): file 
            for file in transcript_files
        }
        
        # Process results as they complete
        for future in as_completed(future_to_file):
            transcript_file = future_to_file[future]
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
    
    # Calculate success rate
    success_count = sum(1 for r in results if r.get("success", False))
    total_count = len(results)
    
    total_time = time.time() - total_start
    logger.info(f"🎉 All files completed in {total_time:.2f}s ({total_time/60:.2f} mins)")
    logger.info(f"📈 Success rate: {success_count}/{total_count} ({success_count/total_count*100:.1f}%)")
    show_gpu_memory("after processing")

if __name__ == "__main__":
    main()