import json
import time
import subprocess
import logging
from pathlib import Path
import re
from typing import Optional
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env file and loads variables

OLLAMA_MODEL_NAME = "gpt-oss:120b"
OLLAMA_API_URL = "http://localhost:11434/api/generate"  # local server

TRANSCRIPT_PATH = "/workspace/llm-tests/transcripts/Spencer/REC-6604.json"
TEMPLATE_PATH = "/workspace/llm-tests/templates/doctor-template-specialized-v2.json"
PROMPT_PATH = "/workspace/llm-tests/prompt-v1.txt"
OUTPUT_PATH = "/workspace/llm-tests/Output/testing/REC-6604-gpt120b.json"

MAX_TOKENS = 6000
TEMPERATURE = 0.7
REQUEST_TIMEOUT = 600  # seconds

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


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


def load_files() -> tuple[str, str, str]:
    """Load system prompt, JSON template, and transcript from disk."""
    for p in (PROMPT_PATH, TEMPLATE_PATH, TRANSCRIPT_PATH):
        if not Path(p).exists():
            raise FileNotFoundError(f"Required file not found: {p}")

    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        system_prompt = f.read().strip()

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template_data = json.load(f)
    template_json = json.dumps(template_data, indent=2, ensure_ascii=False)

    with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
        transcript = f.read().strip()

    logger.info("✅ All files loaded successfully")
    return system_prompt, template_json, transcript


def generate_response_ollama(system_prompt: str, template: str, transcript: str) -> str:
    """Send prompt to Ollama GPT-OSS 120B API and return extracted response."""
    logger.info("🚀 Sending request to Ollama GPT-OSS API...")
    show_gpu_memory("before request")
    start_time = time.time()

    prompt_text = (
        system_prompt
        + "\n\nTEMPLATE_JSON (use exactly this structure; return only JSON matching the template):\n"
        + template
        + "\n\nINSTRUCTION: Fill this JSON template with data extracted from the transcript."
        + "\n⚠️ CRITICAL: Return ONLY valid JSON and nothing else"
        + " Do NOT include explanations, commentary, thoughts, or markdown/code fences."
        + "\n\nMedical Transcript to Process:\n\n"
        + transcript
    )

    payload = {
        "model": OLLAMA_MODEL_NAME,
        "prompt": prompt_text,
        "temperature": TEMPERATURE,  # Use the defined constant
        "max_tokens": MAX_TOKENS,
        "stream": False,  # Disable streaming to get complete response
    }

    headers = {"Content-Type": "application/json"}

    try:
        resp = requests.post(
            OLLAMA_API_URL,
            json=payload,
            headers=headers,
            timeout=REQUEST_TIMEOUT,
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Request to Ollama API failed: {e}")
        raise

    # Dump raw response immediately for debugging
    raw_dump_path = Path(OUTPUT_PATH).with_suffix(".raw.txt")
    with open(raw_dump_path, "w", encoding="utf-8") as f:
        f.write(resp.text)
    logger.info(f"✅ Raw Ollama response dumped to {raw_dump_path}")

    # Parse the response
    try:
        response_data = resp.json()
        
        # Handle streaming response format (multiple JSON objects)
        if isinstance(response_data, str):
            # If response is a string, try to parse multiple JSON objects
            response_parts = []
            for line in response_data.strip().split('\n'):
                line = line.strip()
                if line:
                    try:
                        part = json.loads(line)
                        if 'response' in part:
                            response_parts.append(part['response'])
                    except json.JSONDecodeError:
                        continue
            output_text = ''.join(response_parts)
        else:
            # Single response object
            output_text = response_data.get("response", "")
            
        # If output_text is still empty, try alternative parsing
        if not output_text:
            # Try to parse line by line from raw text
            response_parts = []
            for line in resp.text.strip().split('\n'):
                line = line.strip()
                if line:
                    try:
                        part = json.loads(line)
                        if 'response' in part and part['response']:
                            response_parts.append(part['response'])
                    except json.JSONDecodeError:
                        continue
            output_text = ''.join(response_parts)
            
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse response JSON: {e}")
        # Fallback: return raw text
        output_text = resp.text

    gen_time = time.time() - start_time
    logger.info(f"✅ Received response in {gen_time:.2f}s")
    show_gpu_memory("after request")
    
    return output_text.strip()


def extract_json(response: str) -> Optional[any]:
    """Extract first valid JSON object/array from Ollama output."""
    if not response or not response.strip():
        return None

    # Clean up the response - remove any non-JSON text
    response = response.strip()
    
    # Look for JSON object or array patterns
    json_patterns = [
        r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}',  # Simple object pattern
        r'\[[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*\]',  # Simple array pattern
    ]
    
    for pattern in json_patterns:
        matches = re.findall(pattern, response, re.DOTALL)
        for match in matches:
            try:
                return json.loads(match)
            except json.JSONDecodeError:
                continue
    
    # Try to find JSON between braces more aggressively
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
    
    # Try to find JSON array
    bracket_level = 0
    start_idx = -1
    
    for i, char in enumerate(response):
        if char == '[':
            if bracket_level == 0:
                start_idx = i
            bracket_level += 1
        elif char == ']':
            bracket_level -= 1
            if bracket_level == 0 and start_idx >= 0:
                candidate = response[start_idx:i+1]
                try:
                    return json.loads(candidate)
                except json.JSONDecodeError:
                    continue

    # Final fallback: try to parse entire response as JSON
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        logger.warning("⚠️ Could not parse JSON from response.")
        logger.debug(f"Response content: {response[:500]}...")
        return None


def save_outputs(raw_response: str, json_data: Optional[any] = None) -> None:
    out_path = Path(OUTPUT_PATH)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(raw_response)
    logger.info(f"✅ Raw output saved: {out_path}")

    if json_data is not None:
        json_path = out_path.with_suffix(".processed.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        logger.info(f"✅ JSON output saved: {json_path}")
    else:
        logger.warning("⚠️ No valid JSON data to save")


def main():
    total_start = time.time()

    logger.info(f"🚀 Processing with chat model {OLLAMA_MODEL_NAME} @ {OLLAMA_API_URL}")
    system_prompt, template, transcript = load_files()
    
    try:
        response = generate_response_ollama(system_prompt, template, transcript)
        logger.info(f"📝 Response length: {len(response)} characters")
        logger.info(f"📝 Response preview: {response[:200]}...")
        
    except Exception as e:
        logger.error(f"Generation failed: {e}")
        return

    # Extract JSON
    json_data = extract_json(response)
    
    if json_data:
        logger.info("✅ Successfully extracted JSON data")
    else:
        logger.error("❌ Failed to extract valid JSON from response")
    
    save_outputs(response, json_data)

    total_time = time.time() - total_start
    logger.info(f"🎉 Completed in {total_time:.2f}s ({total_time/60:.2f} mins)")


if __name__ == "__main__":
    main()