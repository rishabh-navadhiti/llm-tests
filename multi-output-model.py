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

VLLM_API_URL = "http://localhost:8000/v1/chat/completions"  # Changed to chat completions endpoint

# CONFIG — change as needed
INPUT_DIR = Path("/workspace/llm-tests/transcripts/Spencer")
OUTPUT_DIR = Path("/workspace/llm-tests/Output/Spencer-Deepseek-Qwen32b-FP8")
TEMPLATE_PATH = Path("/workspace/llm-tests/templates/doctor-template-specialized.json")
PROMPT_PATH = Path("/workspace/llm-tests/prompt-v1.txt")

MAX_TOKENS = 10000
TEMPERATURE = 0.1
REQUEST_TIMEOUT = 600  # seconds

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


def generate_response_vllm(system_prompt: str, template: str, transcript: str) -> str:
    """Send chat prompt to vLLM chat API and return the raw text content."""
    logger.info("🚀 Sending request to chat API...")
    show_gpu_memory("before request")
    start_time = time.time()

    # Put the template and strict instructions into the system message, transcript into user message.
    system_content = (
        system_prompt
        + "\n\nTEMPLATE_JSON (use exactly this structure; return only JSON matching the template):\n"
        + template
        + "\n\nINSTRUCTION: Return only valid JSON (array/object) that exactly matches the template. "
        + "Do NOT include any extra commentary, explanation, or surrounding markdown/code fences."
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
        "top_p": 0.9 if TEMPERATURE > 0 else 1.0,
    }

    headers = {"Content-Type": "application/json"}

    try:
        resp = requests.post(VLLM_API_URL, json=payload, headers=headers, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Request to chat API failed: {e}")
        raise

    data = resp.json()
    # standard chat response shape: choices[0].message.content
    try:
        output_text = data["choices"][0]["message"]["content"]
    except Exception:
        # fallback for other servers: choices[0].text
        output_text = data.get("choices", [{}])[0].get("text", "")
    gen_time = time.time() - start_time
    logger.info(f"✅ Received response in {gen_time:.2f}s")
    show_gpu_memory("after request")
    return output_text.strip()


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

        try:
            response = generate_response_vllm(prompt, template, transcript)
        except Exception as e:
            logger.error(f"Generation failed for {transcript_file.name}: {e}")
            continue

        json_data = extract_json(response)

        base_filename = transcript_file.stem
        save_outputs(OUTPUT_DIR, base_filename, response, json_data)

    total_time = time.time() - total_start
    logger.info(f"🎉 All files completed in {total_time:.2f}s ({total_time/60:.2f} mins)")


if __name__ == "__main__":
    main()