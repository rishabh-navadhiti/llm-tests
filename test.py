import requests

VLLM_API_URL = "http://localhost:8000/v1/completions"  # Change if needed
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.3"            # Replace with your model name

def test_vllm_api():
    payload = {
        "model": MODEL_NAME,
        "prompt": "Hello world",
        "max_tokens": 20,
        "temperature": 0,
    }
    
    response = requests.post(VLLM_API_URL, json=payload)
    
    # Print full raw response text
    print("=== RAW RESPONSE ===")
    print(response.text)
    
    # Optionally parse JSON safely
    try:
        data = response.json()
        print("\n=== Parsed 'text' field ===")
        print(data["choices"][0]["text"])
    except Exception as e:
        print("\n⚠️ Could not parse JSON:")
        print(e)

if __name__ == "__main__":
    test_vllm_api()
