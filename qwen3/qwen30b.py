import json
import requests

    # === CONFIG ===
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen3:30b-a3b-instruct-2507-q8_0"


TRANSCRIPT_PATH = "/workspace/llm-tests/transcripts/transcript1.json"
TEMPLATE_PATH = "/workspace/llm-tests/doctor-template.json"
PROMPT_PATH = "/workspace/llm-tests/prompt.txt"

    # === LOAD RAW PROMPT ===
with open(PROMPT_PATH, "r") as f:
    raw_prompt = f.read().strip()

    # === LOAD TEMPLATE JSON AND STRINGIFY ===
with open(TEMPLATE_PATH, "r") as f:
    template_data = json.load(f)
template_json_str = json.dumps(template_data, indent=2)

    # === LOAD RAW TRANSCRIPT AS STRING ===
with open(TRANSCRIPT_PATH, "r") as f:
    formatted_transcript = f.read()

    # === COMBINE INTO SYSTEM & USER PROMPTS ===
system_message = raw_prompt + "\n\nTEMPLATE:\n" + template_json_str
user_message = formatted_transcript 

# system_message = raw_prompt
# user_message = formatted_transcript + "\n\nTEMPLATE:\n" + template_json_str

    # === SEND TO OLLAMA ===
payload = {
    "model": MODEL_NAME,
    "messages": [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ],
    "stream": False
}

response = requests.post(OLLAMA_URL, json=payload)

    # === HANDLE RESPONSE ===
try:
    output = response.json()
    content = output.get("message", {}).get("content", "[No content returned]")

    # Save the output to a file
    OUTPUT_PATH = "/workspace/llm-tests/output.json"
    with open(OUTPUT_PATH, "w") as out_file:
        out_file.write(content)

    print(f"\n✅ Output saved to: {OUTPUT_PATH}")
except Exception as e:
    print("❌ Failed to parse response:")
    print(response.text)
