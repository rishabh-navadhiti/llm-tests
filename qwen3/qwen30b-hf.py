import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import time
import subprocess


# === CONFIG ===
MODEL_NAME = "Qwen/Qwen3-30B-A3B-Instruct-2507"
TRANSCRIPT_PATH = "/workspace/llm-tests/transcripts/eric-baker.json"
TEMPLATE_PATH = "/workspace/llm-tests/doctor-template.json"
PROMPT_PATH = "/workspace/llm-tests/prompt.txt"
OUTPUT_PATH = "/workspace/llm-tests/output.json"

# === MONITORING GPU ===
def show_gpu_memory(note=""):
    try:
        output = subprocess.check_output(["nvidia-smi", "--query-gpu=memory.used,memory.total", "--format=csv,nounits,noheader"])
        used, total = map(int, output.decode().strip().split(","))
        print(f"📊 GPU Memory {note}: {used} MiB / {total} MiB")
    except Exception as e:
        print("⚠️ Could not read GPU memory usage:", str(e))

# === LOAD PROMPT ===
with open(PROMPT_PATH, "r") as f:
    raw_prompt = f.read().strip()

# === LOAD TEMPLATE ===
with open(TEMPLATE_PATH, "r") as f:
    template_data = json.load(f)
template_json_str = json.dumps(template_data, indent=2)

# === LOAD TRANSCRIPT ===
with open(TRANSCRIPT_PATH, "r") as f:
    formatted_transcript = f.read()

# === PREPARE MESSAGES ===
system_message = raw_prompt + "\n\nTEMPLATE:\n" + template_json_str
user_message = formatted_transcript

messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_message}
]

# === LOAD MODEL AND TOKENIZER ===
print("🔧 Loading model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


quant_config = BitsAndBytesConfig(load_in_8bit=True)


# quant_config = BitsAndBytesConfig(
#     load_in_4bit=True,
#     bnb_4bit_compute_dtype=torch.float16,
#     bnb_4bit_use_double_quant=True,
#     bnb_4bit_quant_type="nf4",  # or "fp4"
# )


model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=quant_config,
    device_map="auto",
    torch_dtype=torch.float16,
    attn_implementation="flash_attention_2",
)

print("✅ Model loaded.")
show_gpu_memory("after model load")

# === TOKENIZE INPUT ===
print("\n📝 Tokenizing input...")
tokenize_start = time.time()

chat_text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

# Optional: try batching
# chat_text = [chat_text] * 2  # batch of 2

inputs = tokenizer([chat_text], return_tensors="pt").to(model.device)

input_token_count = inputs["input_ids"].shape[-1]
print(f"🔢 Input tokens: {input_token_count}")
show_gpu_memory("after tokenization")

tokenize_end = time.time()
print(f"⏱️ Tokenization time: {tokenize_end - tokenize_start:.2f}s")

# === GENERATE OUTPUT ===
print("\n🚀 Starting generation...")
generate_start = time.time()

with torch.no_grad():
    generated_ids = model.generate(
        **inputs,
        max_new_tokens=4096,
        do_sample=False,
        eos_token_id=tokenizer.eos_token_id,
    )

generate_end = time.time()

# === DECODE OUTPUT ===
output_ids = generated_ids[0][inputs["input_ids"].shape[-1]:]
content = tokenizer.decode(output_ids, skip_special_tokens=True)

output_token_count = len(output_ids)
print(f"🧾 Output tokens: {output_token_count}")
print(f"⏱️ Generation time: {generate_end - generate_start:.2f}s ({(generate_end - generate_start)/60:.2f} mins)")
show_gpu_memory("after generation")

# === SAVE TO FILE ===
with open(OUTPUT_PATH, "w") as f:
    f.write(content)

print(f"\n✅ Output saved to: {OUTPUT_PATH}")
