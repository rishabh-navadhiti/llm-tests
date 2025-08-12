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

load_dotenv()

MODEL_NAME = os.getenv("VLLM_MODEL_NAME")
if MODEL_NAME is None:
    raise ValueError("VLLM_MODEL_NAME is not set")

VLLM_API_URL = "http://localhost:8000/v1/completions"

# CONFIG — change as needed
INPUT_DIR = Path("/workspace/llm-tests/transcripts/Spencer")
OUTPUT_DIR = Path("/workspace/llm-tests/Output/testing")
TEMPLATE_PATH = Path("/workspace/llm-tests/templates/doctor-template-specialized.json")
PROMPT_PATH = Path("/workspace/llm-tests/prompt-v1.txt")

MAX_NEW_TOKENS = 10000
TEMPERATURE = 0.1

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def show_gpu_memory(note: str = "") -> None:
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
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        prompt = f.read().strip()

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template_data = json.load(f)

    return prompt, json.dumps(template_data, indent=2)


def load_transcript(file_path: Path) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()


def prepare_prompt_string(prompt: str, template: str, transcript: str) -> str:
    return f"""{prompt}

OUTPUT TEMPLATE:
{template}

Medical Transcript to Process:
{transcript}

Return ONLY valid JSON matching the template format. No explanatory text before or after the JSON."""


def generate_response_vllm(prompt_string: str) -> str:
    logger.info("🚀 Sending request to vLLM API...")
    start_time = time.time()

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt_string,
        "max_tokens": MAX_NEW_TOKENS,
        "temperature": TEMPERATURE,
        "top_p": 0.9 if TEMPERATURE > 0 else 1.0,
    }

    response = requests.post(VLLM_API_URL, json=payload)
    response.raise_for_status()
    data = response.json()

    output_text = data["choices"][0]["text"]
    gen_time = time.time() - start_time
    logger.info(f"✅ Received response in {gen_time:.2f}s")

    return output_text.strip()


def extract_json(response: str) -> Optional[dict]:
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

    logger.warning("⚠️ Could not extract valid JSON from the response.")
    return None


def save_outputs(output_dir: Path, base_filename: str, raw_response: str, json_data: Optional[dict]) -> None:
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

    for transcript_file in INPUT_DIR.glob("*.json"):
        logger.info(f"📄 Processing: {transcript_file.name}")
        transcript = load_transcript(transcript_file)
        prompt_string = prepare_prompt_string(prompt, template, transcript)

        response = generate_response_vllm(prompt_string)
        json_data = extract_json(response)

        base_filename = transcript_file.stem
        save_outputs(OUTPUT_DIR, base_filename, response, json_data)

    total_time = time.time() - total_start
    logger.info(f"🎉 All files completed in {total_time:.2f}s ({total_time/60:.2f} mins)")


if __name__ == "__main__":
    main()
