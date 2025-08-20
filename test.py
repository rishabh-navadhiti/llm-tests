import requests
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env file and loads variables

MODEL_NAME = os.getenv("VLLM_MODEL_NAME")
if MODEL_NAME is None:
    raise ValueError("VLLM_MODEL_NAME is not set")

VLLM_API_URL = "http://localhost:8000/v1/chat/completions"

def test_vllm_api():
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": "Hello world"}
        ],
        "max_tokens": 20,
        "temperature": 0,
    }
    
    response = requests.post(VLLM_API_URL, json=payload)
    
    print("=== RAW RESPONSE ===")
    print(response.text)
    
    try:
        data = response.json()
        print("\n=== Parsed assistant message ===")
        print(data["choices"][0]["message"]["content"])
    except Exception as e:
        print("\n⚠️ Could not parse JSON:")
        print(e)

if __name__ == "__main__":
    test_vllm_api()
