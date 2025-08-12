import json
import logging
import time
import requests
from pathlib import Path
import re

# **** config ********
OLLAMA_MODEL = "gpt-oss:20b"
OLLAMA_API_URL = "http://localhost:11434/api/generate"

TRANSCRIPT_PATH = "/workspace/llm-tests/transcripts/milo.json"
TEMPLATE_PATH = "/workspace/llm-tests/doctor-template-v1.json"
PROMPT_PATH = "/workspace/llm-tests/prompt-v1.txt"
OUTPUT_PATH = "/workspace/llm-tests/gpt-oss-20b/evaluate-output/milo-soap.json"

# **** logging ********
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def load_files():
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        prompt = f.read().strip()
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template_json = json.dumps(json.load(f), indent=2)
    with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
        transcript = f.read().strip()
    return prompt, template_json, transcript

def prepare_prompt(prompt: str, template: str, transcript: str) -> str:
    return f"""{prompt}

OUTPUT TEMPLATE:
{template}

Medical Transcript to Process:
{transcript}

Return ONLY valid JSON matching the template format. No explanatory text before or after the JSON."""

def send_request_ollama(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    headers = {"Content-Type": "application/json"}

    logger.info(" Sending request to Ollama API...")
    start = time.time()
    response = requests.post(OLLAMA_API_URL, headers=headers, json=payload)
    elapsed = time.time() - start

    if response.status_code != 200:
        raise RuntimeError(f" Ollama API Error: {response.status_code}: {response.text}")

    logger.info(f" Response received in {elapsed:.2f} seconds")
    return response.json().get("response", "")

def extract_json(response: str):
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        pass

    patterns = [
        r"\{.*\}",
        r"```json\s*(\{.*?\})\s*```",
        r"```\s*(\{.*?\})\s*```",
    ]
    for pattern in patterns:
        matches = re.findall(pattern, response, re.DOTALL)
        for match in matches:
            try:
                return json.loads(match)
            except json.JSONDecodeError:
                continue
    return None

def save_outputs(raw: str, extracted: dict):
    Path(OUTPUT_PATH).parent.mkdir(exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(raw)
    logger.info(f"Raw response saved: {OUTPUT_PATH}")
    if extracted:
        json_path = str(Path(OUTPUT_PATH).with_suffix(".processed.json"))
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(extracted, f, indent=2)
        logger.info(f" Extracted JSON saved: {json_path}")

def main():
    logger.info("Starting Ollama Inference Pipeline")
    try:
        prompt, template, transcript = load_files()
        full_prompt = prepare_prompt(prompt, template, transcript)
        response = send_request_ollama(full_prompt)
        json_data = extract_json(response)
        if json_data:
            logger.info(" JSON extraction successful")
        else:
            logger.warning("⚠️ Could not extract structured JSON")
        save_outputs(response, json_data)
    except Exception as e:
        logger.error(f" Pipeline failed: {e}")

if __name__ == "__main__":
    main()
