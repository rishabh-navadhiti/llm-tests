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

MODEL_NAME = os.getenv("VLLM_MODEL_NAME")
if MODEL_NAME is None:
    raise ValueError("VLLM_MODEL_NAME is not set")


VLLM_API_URL = "http://localhost:8000/v1/chat/completions"   # vLLM OpenAI-style API endpoint


TRANSCRIPT_PATH = "/workspace/llm-tests/transcripts/Spencer/REC-6604.json"
TEMPLATE_PATH = "/workspace/llm-tests/templates/doctor-template-specialized-v2.json"
PROMPT_PATH = "/workspace/llm-tests/prompt-v1.txt"
OUTPUT_PATH = "/workspace/llm-tests/Output/testing/REC-6604-gemma.json"

MAX_TOKENS = 6000
TEMPERATURE = 0
REQUEST_TIMEOUT = 600  # seconds (adjust if you expect very long responses)

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
    """Load system prompt, JSON template and transcript from disk."""
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

def generate_response_vllm(system_prompt: str, template: str, transcript: str) -> str:
    """Send chat prompt to vLLM chat API and return raw JSON content."""
    logger.info("🚀 Sending request to chat API...")
    show_gpu_memory("before request")
    start_time = time.time()

    # Put the template and strict instructions into the system message, transcript into user message.
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
        "temperature": 0.7,   # keep deterministic for structured output
        "top_p": 0.95,
        "top_k": 64, 

        # "stop": ["```", "</s>"],  # safety cutoff to avoid commentary/markdown
    }

    headers = {"Content-Type": "application/json"}

    try:
        resp = requests.post(
            f"{VLLM_API_URL}",  # ensure endpoint correct
            json=payload,
            headers=headers,
            timeout=REQUEST_TIMEOUT,
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Request to chat API failed: {e}")
        raise

    data = resp.json()
    # standard OpenAI-style chat response shape
    try:
        output_text = data["choices"][0]["message"]["content"]
    except Exception:
        output_text = data.get("choices", [{}])[0].get("text", "")

    gen_time = time.time() - start_time
    logger.info(f"✅ Received response in {gen_time:.2f}s")
    show_gpu_memory("after request")
    return output_text.strip()



# def generate_response_vllm(system_prompt: str, template: str, transcript: str) -> str:
#     """Send prompt to vLLM /completions API and return raw text content."""
#     logger.info("🚀 Sending request to completions API (/v1/completions)...")
#     show_gpu_memory("before request")
#     start_time = time.time()

#     # Flatten into one raw prompt string (no roles, just text)
#     prompt = (
#         system_prompt
#         + "\n\nTEMPLATE_JSON (use exactly this structure; return only JSON matching the template):\n"
#         + template
#         + "\n\nINSTRUCTION: Fill this JSON template with data extracted from the transcript. "
#         + "\nReturn ONLY valid JSON matching the template above."
#         + "Do NOT include any extra commentary, explanation, or surrounding markdown/code fences.\n\n"
#         + "Medical Transcript to Process:\n\n"
#         + transcript
#     )

#     payload = {
#         "model": MODEL_NAME,
#         "prompt": prompt,
#         "max_tokens": MAX_TOKENS,
#         "temperature": TEMPERATURE,
#         "top_p": 0.9 if TEMPERATURE > 0 else 1.0,
#     }

#     headers = {"Content-Type": "application/json"}

#     try:
#         resp = requests.post(
#             VLLM_API_URL.replace("/chat/completions", "/completions"),
#             json=payload,
#             headers=headers,
#             timeout=REQUEST_TIMEOUT,
#         )
#         resp.raise_for_status()
#     except requests.RequestException as e:
#         logger.error(f"Request to completions API failed: {e}")
#         raise

#     data = resp.json()
#     # /completions returns choices[0].text
#     output_text = data.get("choices", [{}])[0].get("text", "")

#     gen_time = time.time() - start_time
#     logger.info(f"✅ Received response in {gen_time:.2f}s")
#     show_gpu_memory("after request")
#     return output_text.strip()



def extract_json(response: str) -> Optional[any]:
    """
    Robustly try to find & parse the first valid JSON object/array in `response`.
    Tries direct json.loads first then attempts substrings starting at first '{' or '['.
    """
    if not response or not response.strip():
        return None

    # direct attempt
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        pass

    # try to locate JSON-like substrings (search for first '{' or '[' and try to parse up to different closing positions)
    for start_char in ("[", "{"):
        starts = [m.start() for m in re.finditer(re.escape(start_char), response)]
        for start in starts:
            # scan for possible ends (work backwards to find nearest closing bracket)
            for end in range(len(response) - 1, start, -1):
                if response[end] not in ("}", "]"):
                    continue
                candidate = response[start : end + 1]
                try:
                    return json.loads(candidate)
                except json.JSONDecodeError:
                    continue

    # fallback: try regex capture of codeblock JSON or simple braces (less reliable)
    patterns = [
        r"```json\s*(\{.*?\}|\[.*?\])\s*```",
        r"```\s*(\{.*?\}|\[.*?\])\s*```",
        r"(\{.*\})",  # last resort (greedy)
        r"(\[.*\])",
    ]
    for p in patterns:
        matches = re.findall(p, response, re.DOTALL)
        for m in matches:
            try:
                return json.loads(m)
            except json.JSONDecodeError:
                continue

    logger.warning("⚠️ Could not extract valid JSON from response.")
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


def main():
    total_start = time.time()

    logger.info(f"🚀 Processing with chat model {MODEL_NAME} @ {VLLM_API_URL}")
    system_prompt, template, transcript = load_files()
    try:
        response = generate_response_vllm(system_prompt, template, transcript)
    except Exception as e:
        logger.error(f"Generation failed: {e}")
        return

    json_data = extract_json(response)
    save_outputs(response, json_data)

    total_time = time.time() - total_start
    logger.info(f"🎉 Completed in {total_time:.2f}s ({total_time/60:.2f} mins)")


if __name__ == "__main__":
    main()
