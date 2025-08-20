import json
import time
import subprocess
import logging
from pathlib import Path
import re
from typing import Optional, Dict, Any
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env file and loads variables

OLLAMA_MODEL_NAME = "gemma3:27b-it-fp16"  # Correct Gemma 3 model name
OLLAMA_API_URL = "http://localhost:11434/api/generate"  # local server

# CONFIG — change as needed
INPUT_DIR = Path("/workspace/llm-tests/transcripts/Spencer")
OUTPUT_DIR = Path("/workspace/llm-tests/Output/Gemma-27b-full-updatedTemp")
TEMPLATE_PATH = Path("/workspace/llm-tests/templates/doctor-template-specialized-v2.json")
PROMPT_PATH = Path("/workspace/llm-tests/prompt-v1.txt")

MAX_TOKENS = 8192  # Conservative limit for stability
TEMPERATURE = 0.7  # Lower for more consistent JSON output
REQUEST_TIMEOUT = 600  # Reduced timeout

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def show_gpu_memory(note: str = "") -> None:
    """Monitor GPU memory usage (best-effort)."""
    try:
        output = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.used,memory.total", "--format=csv,nounits,noheader"],
            timeout=5,
        )
        for i, line in enumerate(output.decode().strip().split("\n")):
            used, total = map(int, line.split(","))
            usage_pct = used / total * 100 if total else 0.0
            logger.info(f"📊 GPU {i} Memory {note}: {used} MiB / {total} MiB ({usage_pct:.1f}%)")
    except Exception as e:
        logger.debug(f"Could not read GPU memory: {e}")


def test_ollama_connection() -> bool:
    """Test if Ollama is running and model is available."""
    try:
        # Test basic connection
        resp = requests.get("http://localhost:11434/api/tags", timeout=10)
        if resp.status_code != 200:
            logger.error("❌ Ollama server not responding")
            return False
            
        models = resp.json().get("models", [])
        available_models = [model["name"] for model in models]
        
        if OLLAMA_MODEL_NAME not in available_models:
            logger.error(f"❌ Model {OLLAMA_MODEL_NAME} not found. Available: {available_models}")
            return False
            
        logger.info(f"✅ Ollama connection OK, model {OLLAMA_MODEL_NAME} available")
        return True
        
    except Exception as e:
        logger.error(f"❌ Failed to connect to Ollama: {e}")
        return False


def load_template_and_prompt() -> tuple[str, str]:
    """Load system prompt and JSON template from disk."""
    for p in (PROMPT_PATH, TEMPLATE_PATH):
        if not p.exists():
            raise FileNotFoundError(f"Required file not found: {p}")

    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        system_prompt = f.read().strip()

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template_data = json.load(f)
    template_json = json.dumps(template_data, indent=2, ensure_ascii=False)

    logger.info("✅ Template and prompt loaded successfully")
    return system_prompt, template_json


def load_transcript(file_path: Path) -> str:
    """Load transcript from a specific file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    
    # If it's a JSON file, try to extract transcript content
    if file_path.suffix.lower() == '.json':
        try:
            data = json.loads(content)
            # Try common transcript fields
            for field in ['transcript', 'text', 'content', 'body']:
                if field in data:
                    return str(data[field])
            # If no specific field, return the whole JSON as string
            return json.dumps(data, indent=2)
        except json.JSONDecodeError:
            # If not valid JSON, return as-is
            pass
    
    return content


def generate_response_ollama(system_prompt: str, template: str, transcript: str, filename: str) -> str:
    """Send prompt to Ollama API and return extracted response."""
    logger.info(f"🚀 Sending request to Ollama for {filename}...")
    show_gpu_memory("before request")
    start_time = time.time()

    # Old-style prompt instructions
    full_prompt = (
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
        "prompt": full_prompt,
        "options": {
            "temperature": TEMPERATURE,
            "top_p": 0.9,
            "top_k": 40,
            "num_predict": MAX_TOKENS,
        },
        "stream": False
    }

    headers = {"Content-Type": "application/json"}

    try:
        logger.info(f"📤 Sending request (prompt length: {len(full_prompt)} chars)...")
        resp = requests.post(
            OLLAMA_API_URL,
            json=payload,
            headers=headers,
            timeout=REQUEST_TIMEOUT,
        )
        resp.raise_for_status()
        logger.info(f"📥 Received response (status: {resp.status_code})")
    except requests.Timeout:
        logger.error(f"❌ Request timeout after {REQUEST_TIMEOUT}s for {filename}")
        raise
    except requests.RequestException as e:
        logger.error(f"❌ Request failed for {filename}: {e}")
        raise

    # Parse response
    try:
        response_data = resp.json()
        output_text = response_data.get("response", "").strip()
        if not output_text:
            logger.error("❌ Empty response from Ollama")
            return ""
    except json.JSONDecodeError as e:
        logger.error(f"❌ Failed to parse Ollama response JSON: {e}")
        return resp.text

    gen_time = time.time() - start_time
    logger.info(f"✅ Generated response in {gen_time:.2f}s (length: {len(output_text)} chars)")
    show_gpu_memory("after request")
    
    return output_text


def extract_json_from_response(response: str) -> Optional[Dict[Any, Any]]:
    """Extract JSON from model response with multiple strategies."""
    if not response or not response.strip():
        logger.warning("⚠️ Empty response")
        return None

    response = response.strip()
    
    # Strategy 1: Clean up markdown and try direct parse first
    cleaned = response
    # Remove markdown code blocks
    cleaned = re.sub(r'```json\s*|\s*```', '', cleaned)
    cleaned = cleaned.strip()
    
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # Strategy 2: Find complete JSON arrays first (priority for your use case)
    bracket_count = 0
    start_pos = -1
    
    for i, char in enumerate(response):
        if char == '[':
            if bracket_count == 0:
                start_pos = i
            bracket_count += 1
        elif char == ']':
            bracket_count -= 1
            if bracket_count == 0 and start_pos >= 0:
                try:
                    json_str = response[start_pos:i+1]
                    parsed = json.loads(json_str)
                    # Make sure we got a full array, not just partial
                    if isinstance(parsed, list) and len(parsed) > 0:
                        return parsed
                except json.JSONDecodeError:
                    continue

    # Strategy 3: Find JSON objects (fallback)
    brace_count = 0
    start_pos = -1
    
    for i, char in enumerate(response):
        if char == '{':
            if brace_count == 0:
                start_pos = i
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0 and start_pos >= 0:
                try:
                    json_str = response[start_pos:i+1]
                    return json.loads(json_str)
                except json.JSONDecodeError:
                    continue

    # Strategy 4: More aggressive regex approach for arrays
    # Look for arrays with nested objects
    array_pattern = r'\[[\s\S]*?\]'
    matches = re.findall(array_pattern, response)
    
    # Try the longest match first (most likely to be complete)
    matches.sort(key=len, reverse=True)
    
    for match in matches:
        try:
            parsed = json.loads(match)
            if isinstance(parsed, list) and len(parsed) > 0:
                return parsed
        except json.JSONDecodeError:
            continue

    # Strategy 5: Try to find and extract from cleaned response
    json_match = re.search(r'(\[[\s\S]*\]|\{[\s\S]*\})', cleaned)
    if json_match:
        try:
            return json.loads(json_match.group(1))
        except json.JSONDecodeError:
            pass

    logger.warning(f"⚠️ Could not extract JSON. Response preview: {response[:200]}...")
    return None


def save_outputs(output_dir: Path, base_filename: str, raw_response: str, json_data: Optional[Dict[Any, Any]] = None) -> None:
    """Save raw response and processed JSON to output directory."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save raw response
    raw_path = output_dir / f"{base_filename}-raw.txt"
    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(raw_response)
    logger.info(f"💾 Raw output saved: {raw_path}")

    # Save processed JSON
    if json_data is not None:
        json_path = output_dir / f"{base_filename}-output.processed.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        logger.info(f"💾 JSON output saved: {json_path}")
    else:
        logger.warning(f"⚠️ No valid JSON extracted for {base_filename}")


def process_single_file(transcript_file: Path, system_prompt: str, template: str) -> bool:
    """Process a single transcript file. Returns True if successful."""
    filename = transcript_file.stem
    logger.info(f"📄 Processing: {transcript_file.name}")
    
    try:
        # Load transcript
        transcript = load_transcript(transcript_file)
        logger.info(f"📝 Loaded transcript: {len(transcript)} characters")
        
        # Skip if transcript is too short
        if len(transcript) < 50:
            logger.warning(f"⚠️ Transcript too short, skipping: {transcript_file.name}")
            return False
        
        # Generate response
        response = generate_response_ollama(system_prompt, template, transcript, filename)
        
        if not response:
            logger.error(f"❌ Empty response for {transcript_file.name}")
            return False
            
        # Extract JSON
        json_data = extract_json_from_response(response)
        
        # Save outputs
        save_outputs(OUTPUT_DIR, filename, response, json_data)
        
        if json_data:
            logger.info(f"✅ Successfully processed {transcript_file.name}")
            return True
        else:
            logger.error(f"❌ Failed to extract JSON from {transcript_file.name}")
            return False
            
    except Exception as e:
        logger.error(f"❌ Error processing {transcript_file.name}: {e}")
        return False


def main():
    """Main processing function."""
    total_start = time.time()
    
    logger.info(f"🚀 Starting Ollama Gemma processing")
    logger.info(f"📋 Model: {OLLAMA_MODEL_NAME}")
    logger.info(f"🌐 API: {OLLAMA_API_URL}")
    logger.info(f"📁 Input: {INPUT_DIR}")
    logger.info(f"📁 Output: {OUTPUT_DIR}")

    # Test connection first
    if not test_ollama_connection():
        logger.error("❌ Cannot proceed without Ollama connection")
        return

    # Load template and prompt
    try:
        system_prompt, template = load_template_and_prompt()
    except Exception as e:
        logger.error(f"❌ Failed to load template/prompt: {e}")
        return

    # Find transcript files
    transcript_files = list(INPUT_DIR.glob("*.json")) + list(INPUT_DIR.glob("*.txt"))
    if not transcript_files:
        logger.error(f"❌ No transcript files found in {INPUT_DIR}")
        return

    logger.info(f"📄 Found {len(transcript_files)} files to process")

    # Process files
    successful = 0
    failed = 0
    
    for i, transcript_file in enumerate(transcript_files, 1):
        logger.info(f"🔄 Processing file {i}/{len(transcript_files)}")
        
        if process_single_file(transcript_file, system_prompt, template):
            successful += 1
        else:
            failed += 1
            
        # Add small delay between requests
        if i < len(transcript_files):
            time.sleep(2)

    # Summary
    total_time = time.time() - total_start
    logger.info(f"🎉 Processing complete!")
    logger.info(f"✅ Successful: {successful}")
    logger.info(f"❌ Failed: {failed}")
    logger.info(f"⏱️  Total time: {total_time:.2f}s ({total_time/60:.2f} mins)")


if __name__ == "__main__":
    main()