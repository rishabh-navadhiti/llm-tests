import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import time
import subprocess
import logging
from pathlib import Path
import re
from typing import Optional

# === SIMPLE CONFIG ===
MODEL_NAME = "openai/gpt-oss-20b"

TRANSCRIPT_PATH = "/workspace/llm-tests/transcripts/eric-guefen.json"
TEMPLATE_PATH = "/workspace/llm-tests/doctor-template-v3.json"
PROMPT_PATH = "/workspace/llm-tests/prompt-v2.txt"
OUTPUT_PATH = "/workspace/llm-tests/gpt-oss-20b/output/eric-guefen-v3.json"

# Generation settings
MAX_NEW_TOKENS = 10000
TEMPERATURE = 0.1 
USE_8BIT = True
USE_4BIT = False

# === SETUP LOGGING ===
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def show_gpu_memory(note: str = "") -> None:
    """Monitor GPU memory usage."""
    try:
        output = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=memory.used,memory.total",
                "--format=csv,nounits,noheader",
            ],
            timeout=10,
        )

        for i, line in enumerate(output.decode().strip().split("\n")):
            used, total = map(int, line.split(","))
            usage_pct = used / total * 100
            logger.info(
                f"📊 GPU {i} Memory {note}: {used} MiB / {total} MiB ({usage_pct:.1f}%)"
            )

    except (subprocess.CalledProcessError, FileNotFoundError, TimeoutError) as e:
        logger.warning(f"⚠️ Could not read GPU memory: {e}")


def load_files() -> tuple[str, str, str]:
    """Load all required files with error handling."""
    try:
        # Load prompt
        with open(PROMPT_PATH, "r", encoding="utf-8") as f:
            prompt = f.read().strip()

        # Load template
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            template_data = json.load(f)
        template_json = json.dumps(template_data, indent=2)

        # Load transcript
        with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
            transcript = f.read().strip()

        logger.info("✅ All files loaded successfully")
        return prompt, template_json, transcript

    except FileNotFoundError as e:
        logger.error(f"❌ File not found: {e}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"❌ JSON parsing error: {e}")
        raise


def setup_quantization() -> Optional[BitsAndBytesConfig]:
    """Setup quantization config if needed."""
    if USE_4BIT:
        return BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
        )
    elif USE_8BIT:
        return BitsAndBytesConfig(load_in_8bit=True)
    else:
        return None


def load_model_and_tokenizer() -> tuple[AutoModelForCausalLM, AutoTokenizer]:
    """Load the model and tokenizer."""
    logger.info(f"🔧 Loading tokenizer for {MODEL_NAME}...")
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        logger.info("✅ Tokenizer loaded successfully")
    except Exception as e:
        logger.error(f"❌ Failed to load tokenizer: {e}")
        raise

    logger.info(f"🔧 Loading model {MODEL_NAME}...")
    quant_config = setup_quantization()

    model_kwargs = {
        "device_map": "auto",
        "torch_dtype": torch.bfloat16,  
        "trust_remote_code": True,
    }

    if quant_config:
        model_kwargs["quantization_config"] = quant_config

    try:
        model_kwargs["attn_implementation"] = "flash_attention_2"
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, **model_kwargs)
        logger.info("✅ Using Flash Attention 2")
    except Exception as e:
        logger.warning(f"Flash attention failed, using default: {e}")
        model_kwargs.pop("attn_implementation", None)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, **model_kwargs)

    logger.info(f"✅ Model loaded: ~{model.num_parameters() / 1e9:.1f}B parameters")
    show_gpu_memory("after model load")

    return model, tokenizer


def prepare_prompt_string(prompt: str, template: str, transcript: str) -> str:
    """
    Prepare the full prompt string for a causal language model.
    Unlike vision-language models, most text-only models work best with a single
    formatted string.
    """
    full_prompt = f"""{prompt}

OUTPUT TEMPLATE:
{template}

Medical Transcript to Process:
{transcript}

Return ONLY valid JSON matching the template format. No explanatory text before or after the JSON."""

    return full_prompt


def generate_response(
    model: AutoModelForCausalLM, tokenizer: AutoTokenizer, prompt_string: str
) -> str:
    """Generate response from the model."""
    logger.info("📝 Processing input...")
    start_time = time.time()

    try:
        inputs = tokenizer(
            prompt_string, return_tensors="pt", padding=True, truncation=True
        )
        inputs = inputs.to(model.device)

        input_tokens = inputs["input_ids"].shape[-1]
        logger.info(f"🔢 Input tokens: {input_tokens:,}")

        show_gpu_memory("after tokenization")
        tokenize_time = time.time() - start_time
        logger.info(f"⏱️ Input processing: {tokenize_time:.2f}s")

        # Generate
        logger.info("🚀 Generating response...")
        gen_start = time.time()

        generation_kwargs = {
            **inputs,
            "max_new_tokens": MAX_NEW_TOKENS,
            "do_sample": TEMPERATURE > 0,
            "temperature": TEMPERATURE if TEMPERATURE > 0 else None,
            "top_p": 0.9 if TEMPERATURE > 0 else None,
            "repetition_penalty": 1.1,
            "eos_token_id": tokenizer.eos_token_id,
            "pad_token_id": tokenizer.pad_token_id,
        }

        # Remove None values
        generation_kwargs = {
            k: v for k, v in generation_kwargs.items() if v is not None
        }

        with torch.no_grad():
            generated_ids = model.generate(**generation_kwargs)

        gen_time = time.time() - gen_start

        # Decode output
        output_ids_trimmed = generated_ids[0][len(inputs.input_ids[0]) :]

        output_text = tokenizer.decode(
            output_ids_trimmed,
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False,
        )

        output_tokens = len(output_ids_trimmed)
        tokens_per_sec = output_tokens / gen_time if gen_time > 0 else 0

        logger.info(f"🧾 Output tokens: {output_tokens:,}")
        logger.info(f"⏱️ Generation: {gen_time:.2f}s ({gen_time/60:.2f} mins)")
        logger.info(f"🚄 Speed: {tokens_per_sec:.2f} tokens/sec")

        show_gpu_memory("after generation")
        return output_text.strip()

    except torch.cuda.OutOfMemoryError:
        logger.error("❌ GPU OOM! Try 4-bit quantization or reduce max_new_tokens")
        raise
    except Exception as e:
        logger.error(f"❌ Generation failed: {e}")
        raise


def extract_json(response: str) -> Optional[dict]:
    """Extract JSON from model response."""
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        pass

    patterns = [
        r"\{.*\}",  # Simple brace matching
        r"```json\s*(\{.*?\})\s*```",  # JSON code blocks
        r"```\s*(\{.*?\})\s*```",  # Generic code blocks
    ]

    for pattern in patterns:
        matches = re.findall(pattern, response, re.DOTALL)
        # Iterate through matches and try to parse each one
        for match in matches:
            try:
                return json.loads(match)
            except json.JSONDecodeError:
                continue

    logger.warning("⚠️ Could not extract valid JSON from the response.")
    return None


def save_outputs(raw_response: str, json_data: Optional[dict] = None) -> None:
    """Save both raw and processed outputs."""
    # Create output directory
    Path(OUTPUT_PATH).parent.mkdir(exist_ok=True)

    # Save raw response
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(raw_response)
    logger.info(f"✅ Raw output saved: {OUTPUT_PATH}")

    # Save extracted JSON if available
    if json_data:
        json_path = str(Path(OUTPUT_PATH).with_suffix(".processed.json"))
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        logger.info(f"✅ JSON output saved: {json_path}")


def main():
    """Main execution pipeline for text-only medical transcript processing."""
    total_start = time.time()

    try:
        logger.info(f"🚀 Starting medical transcript processing with {MODEL_NAME}")
        logger.info("📝 Processing text-only medical transcripts")

        # Load files
        prompt, template, transcript = load_files()

        # Load model and tokenizer
        model, tokenizer = load_model_and_tokenizer()

        # Prepare the full prompt string
        prompt_string = prepare_prompt_string(prompt, template, transcript)

        # Generate response
        response = generate_response(model, tokenizer, prompt_string)

        # Extract JSON
        json_data = extract_json(response)

        if json_data:
            logger.info("✅ Successfully extracted structured medical data")
        else:
            logger.warning("⚠️ Could not extract JSON, check raw output")

        # Save outputs
        save_outputs(response, json_data)

        total_time = time.time() - total_start
        logger.info(
            f"🎉 Medical analysis completed in {total_time:.2f}s ({total_time/60:.2f} mins)"
        )

    except Exception as e:
        logger.error(f"❌ Pipeline failed: {e}")
        # Reraise the exception for main to terminate with an error code
        raise
    finally:
        # Cleanup
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            logger.info("🧹 GPU cache cleared")


if __name__ == "__main__":
    main()
