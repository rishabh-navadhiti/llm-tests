import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import time
import subprocess
import logging
from pathlib import Path
import re

# === SIMPLE CONFIG ===
MODEL_NAME = "Qwen/Qwen3-30B-A3B-Instruct-2507"
# MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"  # Alternative for testing
# MODEL_NAME = "meta-llama/Llama-3.1-8B-Instruct"  # Alternative for testing

TRANSCRIPT_PATH = "/workspace/llm-tests/transcripts/eric-baker.json"
TEMPLATE_PATH = "/workspace/llm-tests/doctor-template.json"
PROMPT_PATH = "/workspace/llm-tests/prompt.txt"
OUTPUT_PATH = "/workspace/llm-tests/output.json"

# Generation settings
MAX_NEW_TOKENS = 4096
TEMPERATURE = 0.1  # Low for structured output
USE_8BIT = True
USE_4BIT = False

# === SETUP LOGGING ===
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def show_gpu_memory(note=""):
    """Monitor GPU memory usage."""
    try:
        output = subprocess.check_output([
            "nvidia-smi", "--query-gpu=memory.used,memory.total", 
            "--format=csv,nounits,noheader"
        ], timeout=10)
        
        for i, line in enumerate(output.decode().strip().split('\n')):
            used, total = map(int, line.split(","))
            usage_pct = used/total*100
            logger.info(f"📊 GPU {i} Memory {note}: {used} MiB / {total} MiB ({usage_pct:.1f}%)")
            
    except Exception as e:
        logger.warning(f"⚠️ Could not read GPU memory: {e}")

def load_files():
    """Load all required files with error handling."""
    try:
        # Load prompt
        with open(PROMPT_PATH, "r", encoding='utf-8') as f:
            prompt = f.read().strip()
        
        # Load template
        with open(TEMPLATE_PATH, "r", encoding='utf-8') as f:
            template_data = json.load(f)
        template_json = json.dumps(template_data, indent=2)
        
        # Load transcript
        with open(TRANSCRIPT_PATH, "r", encoding='utf-8') as f:
            transcript = f.read().strip()
        
        logger.info("✅ All files loaded successfully")
        return prompt, template_json, transcript
        
    except FileNotFoundError as e:
        logger.error(f"❌ File not found: {e}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"❌ JSON parsing error: {e}")
        raise

def setup_quantization():
    """Setup quantization config."""
    if USE_4BIT:
        return BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
        )
    elif USE_8BIT:
        return BitsAndBytesConfig(load_in_8bit=True)
    else:
        return None

def load_model_and_tokenizer():
    """Load model and tokenizer."""
    logger.info(f"🔧 Loading tokenizer for {MODEL_NAME}...")
    
    # Load tokenizer with fallback
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
    except Exception as e:
        logger.warning(f"Retrying tokenizer load: {e}")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True, use_fast=False)
    
    # Handle pad token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token or tokenizer.unk_token
    
    logger.info(f"🔧 Loading model {MODEL_NAME}...")
    quant_config = setup_quantization()
    
    model_kwargs = {
        "device_map": "auto",
        "torch_dtype": torch.float16,
        "trust_remote_code": True,
    }
    
    if quant_config:
        model_kwargs["quantization_config"] = quant_config
    
    # Try flash attention, fallback if not supported
    try:
        model_kwargs["attn_implementation"] = "flash_attention_2"
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, **model_kwargs)
        logger.info("✅ Using Flash Attention 2")
    except Exception:
        logger.info("Using default attention")
        model_kwargs.pop("attn_implementation", None)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, **model_kwargs)
    
    logger.info(f"✅ Model loaded: ~{model.num_parameters() / 1e9:.1f}B parameters")
    show_gpu_memory("after model load")
    
    return model, tokenizer

def prepare_messages(prompt, template, transcript):
    """Prepare chat messages with model compatibility."""
    system_msg = f"""{prompt}

OUTPUT TEMPLATE:
{template}

INSTRUCTIONS:
1. Return ONLY valid JSON matching the template
2. No explanatory text before/after JSON
3. Use "N/A" for missing information
4. Ensure valid JSON syntax"""
    
    user_msg = f"Process this medical transcript:\n\n{transcript}"
    
    return [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg}
    ]

def generate_response(model, tokenizer, messages):
    """Generate response from model."""
    logger.info("📝 Tokenizing input...")
    start_time = time.time()
    
    try:
        # Try chat template, fallback to simple concatenation
        try:
            chat_text = tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        except Exception:
            logger.info("Chat template not supported, using simple format")
            chat_text = f"{messages[0]['content']}\n\n{messages[1]['content']}"
        
        inputs = tokenizer(
            chat_text, 
            return_tensors="pt", 
            truncation=True,
            max_length=tokenizer.model_max_length - MAX_NEW_TOKENS
        ).to(model.device)
        
        input_tokens = inputs["input_ids"].shape[-1]
        logger.info(f"🔢 Input tokens: {input_tokens:,}")
        
        if input_tokens > tokenizer.model_max_length - MAX_NEW_TOKENS:
            logger.warning("⚠️ Input may be truncated")
        
        show_gpu_memory("after tokenization")
        tokenize_time = time.time() - start_time
        logger.info(f"⏱️ Tokenization: {tokenize_time:.2f}s")
        
        # Generate
        logger.info("🚀 Generating response...")
        gen_start = time.time()
        
        with torch.no_grad():
            generated_ids = model.generate(
                **inputs,
                max_new_tokens=MAX_NEW_TOKENS,
                temperature=TEMPERATURE,
                top_p=0.9,
                do_sample=TEMPERATURE > 0,
                eos_token_id=tokenizer.eos_token_id,
                pad_token_id=tokenizer.pad_token_id,
                repetition_penalty=1.1,
            )
        
        gen_time = time.time() - gen_start
        
        # Decode
        output_ids = generated_ids[0][inputs["input_ids"].shape[-1]:]
        response = tokenizer.decode(output_ids, skip_special_tokens=True).strip()
        
        output_tokens = len(output_ids)
        tokens_per_sec = output_tokens / gen_time if gen_time > 0 else 0
        
        logger.info(f"🧾 Output tokens: {output_tokens:,}")
        logger.info(f"⏱️ Generation: {gen_time:.2f}s ({gen_time/60:.2f} mins)")
        logger.info(f"🚄 Speed: {tokens_per_sec:.2f} tokens/sec")
        
        show_gpu_memory("after generation")
        return response
        
    except torch.cuda.OutOfMemoryError:
        logger.error("❌ GPU OOM! Try 4-bit quantization or reduce max_new_tokens")
        raise
    except Exception as e:
        logger.error(f"❌ Generation failed: {e}")
        raise

def extract_json(response):
    """Extract JSON from model response."""
    # Try parsing entire response first
    try:
        return json.loads(response)
    except:
        pass
    
    # Try regex patterns
    patterns = [
        r'\{.*\}',  # Simple brace matching
        r'```json\s*(\{.*?\})\s*```',  # JSON code blocks
        r'```\s*(\{.*?\})\s*```',  # Generic code blocks
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, response, re.DOTALL)
        for match in matches:
            try:
                return json.loads(match)
            except:
                continue
    
    logger.warning("⚠️ Could not extract valid JSON")
    return None

def save_outputs(raw_response, json_data=None):
    """Save both raw and processed outputs."""
    # Create output directory
    Path(OUTPUT_PATH).parent.mkdir(exist_ok=True)
    
    # Save raw response
    with open(OUTPUT_PATH, "w", encoding='utf-8') as f:
        f.write(raw_response)
    logger.info(f"✅ Raw output saved: {OUTPUT_PATH}")
    
    # Save extracted JSON if available
    if json_data:
        json_path = str(Path(OUTPUT_PATH).with_suffix('.processed.json'))
        with open(json_path, "w", encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        logger.info(f"✅ JSON output saved: {json_path}")

def main():
    """Main execution pipeline."""
    total_start = time.time()
    
    try:
        logger.info(f"🚀 Starting processing with {MODEL_NAME}")
        
        # Load files
        prompt, template, transcript = load_files()
        
        # Load model
        model, tokenizer = load_model_and_tokenizer()
        
        # Prepare messages
        messages = prepare_messages(prompt, template, transcript)
        
        # Generate response
        response = generate_response(model, tokenizer, messages)
        
        # Extract JSON
        json_data = extract_json(response)
        
        # Save outputs
        save_outputs(response, json_data)
        
        total_time = time.time() - total_start
        logger.info(f"🎉 Completed in {total_time:.2f}s ({total_time/60:.2f} mins)")
        
    except Exception as e:
        logger.error(f"❌ Pipeline failed: {e}")
        raise
    finally:
        # Cleanup
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            logger.info("🧹 GPU cache cleared")

if __name__ == "__main__":
    main()