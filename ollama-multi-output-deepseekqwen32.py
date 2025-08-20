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

# DeepSeek-R1:32B configuration
OLLAMA_MODEL_NAME = "deepseek-r1:32b"  # DeepSeek-R1 32B reasoning model
OLLAMA_API_URL = "http://localhost:11434/api/generate"  # local server

# CONFIG — change as needed
INPUT_DIR = Path("/workspace/llm-tests/transcripts/Spencer")
OUTPUT_DIR = Path("/workspace/llm-tests/Output/DeepSeek-R1-32b-reasoning")
TEMPLATE_PATH = Path("/workspace/llm-tests/templates/doctor-template-specialized-v2.json")
PROMPT_PATH = Path("/workspace/llm-tests/prompt-v1.txt")

# Optimized settings for DeepSeek-R1 based on research
MAX_TOKENS = 8192   # Conservative for structured output
TEMPERATURE = 0.6   # Optimized for reasoning and consistency
TOP_P = 0.95        # Recommended for DeepSeek-R1
TOP_K = 40          # Balanced creativity/consistency
REPEAT_PENALTY = 1.05  # Light penalty for reasoning models
REQUEST_TIMEOUT = 1200  # Extended timeout for reasoning processes
CONTEXT_LENGTH = 32768  # Extended context window for R1 models
FREQUENCY_PENALTY = 0.1  # Reduce repetitive patterns

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
        resp = requests.get("http://localhost:11434/api/tags", timeout=15)
        if resp.status_code != 200:
            logger.error("❌ Ollama server not responding")
            return False
            
        models = resp.json().get("models", [])
        available_models = [model["name"] for model in models]
        
        if OLLAMA_MODEL_NAME not in available_models:
            logger.error(f"❌ Model {OLLAMA_MODEL_NAME} not found. Available: {available_models}")
            logger.info(f"💡 To install the model, run: ollama pull {OLLAMA_MODEL_NAME}")
            logger.info(f"💡 Alternative distilled models: deepseek-r1:32b-qwen-distill-q4_K_M")
            return False
            
        logger.info(f"✅ Ollama connection OK, DeepSeek-R1 model {OLLAMA_MODEL_NAME} available")
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
    """Send prompt to DeepSeek-R1 and return JSON-only response."""
    logger.info(f"🧠 Sending request to DeepSeek-R1 for {filename}...")
    show_gpu_memory("before request")
    start_time = time.time()

    # Simplified prompt: instruct to fill all fields and return JSON only
    full_prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}

TEMPLATE_JSON (use exactly this structure; return only JSON matching the template):
{template}

INSTRUCTION:
- Carefully read the entire transcript
- Fill all fields in the JSON template
- Use "N/A" for missing or unavailable information
- Return ONLY valid JSON
- Do NOT include explanations, reasoning steps, or markdown/code fences

<|eot_id|><|start_header_id|>user<|end_header_id|>

Medical Transcript to Process:

{transcript}

<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""

    payload = {
        "model": OLLAMA_MODEL_NAME,
        "prompt": full_prompt,
        "options": {
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "top_k": TOP_K,
            "repeat_penalty": REPEAT_PENALTY,
            "frequency_penalty": FREQUENCY_PENALTY,
            "num_predict": MAX_TOKENS,
            "num_ctx": CONTEXT_LENGTH,
            "stop": ["<|eot_id|>", "<|end_of_text|>"],
            "seed": -1,
            "num_thread": -1,
            "num_gpu": -1,
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

    # Extract response
    try:
        response_data = resp.json()
        output_text = response_data.get("response", "").strip()
        if not output_text:
            logger.error("❌ Empty response from DeepSeek-R1")
            return ""
        
        # Clean reasoning traces and extra tokens
        cleaned = re.sub(r'<\|.*?\|>', '', output_text, flags=re.DOTALL)
        cleaned = re.sub(r'```json\s*|\s*```', '', cleaned)
        cleaned = cleaned.strip()
        return cleaned
    except json.JSONDecodeError as e:
        logger.error(f"❌ Failed to parse Ollama response JSON: {e}")
        return resp.text
    finally:
        gen_time = time.time() - start_time
        logger.info(f"✅ DeepSeek-R1 generated response in {gen_time:.2f}s (length: {len(output_text)} chars)")
        show_gpu_memory("after request")



def extract_json_from_response(response: str) -> Optional[Dict[Any, Any]]:
    """Extract JSON from DeepSeek-R1 response with reasoning-aware parsing."""
    if not response or not response.strip():
        logger.warning("⚠️ Empty response")
        return None

    response = response.strip()
    
    # Strategy 1: Remove DeepSeek-R1 reasoning tokens and clean
    cleaned = response
    # Remove thinking tags and content (reasoning traces)
    cleaned = re.sub(r'<thinking>.*?</thinking>', '', cleaned, flags=re.DOTALL)
    # Remove any chat template tokens that might leak through
    cleaned = re.sub(r'<\|.*?\|>', '', cleaned)
    cleaned = re.sub(r'<\|begin_of_text\|>.*?<\|start_header_id\|>', '', cleaned, flags=re.DOTALL)
    cleaned = re.sub(r'<\|eot_id\|>.*?$', '', cleaned, flags=re.DOTALL)
    # Remove markdown code blocks
    cleaned = re.sub(r'```json\s*|\s*```', '', cleaned)
    cleaned = cleaned.strip()
    
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # Strategy 2: Look for JSON after reasoning completion
    # DeepSeek-R1 often provides reasoning then JSON
    json_start_patterns = [
        r'(?:Here\'s the extracted information:|Final JSON output:|JSON result:)?\s*(\[.*\]|\{.*\})',
        r'(?:```json\s*)?(\[.*\]|\{.*\})(?:\s*```)?',
        r'(\[[\s\S]*\])',  # Array pattern
        r'(\{[\s\S]*\})',  # Object pattern
    ]
    
    for pattern in json_start_patterns:
        match = re.search(pattern, response, re.DOTALL)
        if match:
            try:
                json_str = match.group(1).strip()
                parsed = json.loads(json_str)
                if isinstance(parsed, (dict, list)) and parsed:
                    return parsed
            except json.JSONDecodeError:
                continue

    # Strategy 3: Find complete JSON arrays (priority for medical data)
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
                    if isinstance(parsed, list) and len(parsed) > 0:
                        return parsed
                except json.JSONDecodeError:
                    continue

    # Strategy 4: Find JSON objects
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
                    parsed = json.loads(json_str)
                    if isinstance(parsed, dict) and parsed:
                        return parsed
                except json.JSONDecodeError:
                    continue

    # Strategy 5: Try to extract from last part of response (after reasoning)
    lines = response.split('\n')
    for i in range(len(lines) - 1, max(0, len(lines) - 10), -1):
        line = lines[i].strip()
        if line.startswith('{') or line.startswith('['):
            try:
                # Try to parse from this line to end
                remaining_text = '\n'.join(lines[i:])
                return json.loads(remaining_text)
            except json.JSONDecodeError:
                continue

    logger.warning(f"⚠️ Could not extract JSON from DeepSeek-R1 response. Response preview: {response[:300]}...")
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
        
        # Log some statistics about the extracted data
        if isinstance(json_data, list):
            logger.info(f"📊 Extracted {len(json_data)} items from {base_filename}")
        elif isinstance(json_data, dict):
            logger.info(f"📊 Extracted data with {len(json_data)} fields from {base_filename}")
    else:
        logger.warning(f"⚠️ No valid JSON extracted for {base_filename}")


def process_single_file(transcript_file: Path, system_prompt: str, template: str) -> bool:
    """Process a single transcript file with DeepSeek-R1 reasoning. Returns True if successful."""
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
        
        # Check if transcript is too long for context window
        if len(transcript) > CONTEXT_LENGTH * 2:  # Conservative estimate
            logger.warning(f"⚠️ Transcript very long ({len(transcript)} chars), may hit context limits")
            # Consider truncating or splitting for very long transcripts
            if len(transcript) > CONTEXT_LENGTH * 3:
                logger.info(f"🔧 Truncating transcript to fit context window")
                transcript = transcript[:CONTEXT_LENGTH * 2]
        
        # Generate response using DeepSeek-R1's reasoning capabilities
        response = generate_response_ollama(system_prompt, template, transcript, filename)
        
        if not response:
            logger.error(f"❌ Empty response for {transcript_file.name}")
            return False
            
        # Extract JSON from reasoned response
        json_data = extract_json_from_response(response)
        
        # Save outputs
        save_outputs(OUTPUT_DIR, filename, response, json_data)
        
        if json_data:
            logger.info(f"✅ Successfully processed {transcript_file.name} with DeepSeek-R1 reasoning")
            return True
        else:
            logger.error(f"❌ Failed to extract JSON from {transcript_file.name}")
            return False
            
    except Exception as e:
        logger.error(f"❌ Error processing {transcript_file.name}: {e}")
        return False


def main():
    """Main processing function for DeepSeek-R1:32B."""
    total_start = time.time()
    
    logger.info(f"🧠 Starting DeepSeek-R1:32B reasoning-enhanced processing")
    logger.info(f"📋 Model: {OLLAMA_MODEL_NAME}")
    logger.info(f"🌐 API: {OLLAMA_API_URL}")
    logger.info(f"🎛️  Settings: temp={TEMPERATURE}, top_p={TOP_P}, top_k={TOP_K}")
    logger.info(f"🔬 Features: Advanced reasoning, 32K context, medical data extraction")
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

    logger.info(f"📄 Found {len(transcript_files)} files to process with DeepSeek-R1 reasoning")

    # Process files
    successful = 0
    failed = 0
    
    for i, transcript_file in enumerate(transcript_files, 1):
        logger.info(f"🔄 Processing file {i}/{len(transcript_files)}")
        
        if process_single_file(transcript_file, system_prompt, template):
            successful += 1
        else:
            failed += 1
            
        # Add delay between requests (longer for reasoning models)
        if i < len(transcript_files):
            time.sleep(4)  # Extended delay for reasoning models

    # Summary
    total_time = time.time() - total_start
    logger.info(f"🎉 DeepSeek-R1 processing complete!")
    logger.info(f"✅ Successful: {successful}")
    logger.info(f"❌ Failed: {failed}")
    logger.info(f"⏱️  Total time: {total_time:.2f}s ({total_time/60:.2f} mins)")
    if successful > 0:
        avg_time = total_time / successful
        logger.info(f"📊 Average processing time per file: {avg_time:.2f}s")


if __name__ == "__main__":
    main()