import os
import json
import requests

# Paths
benchmark_dir = "/Users/rish/Development/runpod dev/llm-tests/newTest/benchmark-gemini"
candidate_dir = "/Users/rish/Development/runpod dev/llm-tests/newTest/GPT-OSS-120b"
output_dir = "/Users/rish/Development/runpod dev/llm-tests/newTest/GPT-OSS-120b/Framework-eval"

# API details
API_URL = "https://pa.aieval.ndproject.dev/compare"
HEADERS = {
    "auth": "dCEjL31sgX",
    "content-type": "application/json"
}

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def evaluate_pair(record_id, benchmark_file, candidate_file):
    """Send benchmark + candidate JSONs to API and save response."""
    try:
        benchmark_data = load_json(benchmark_file)
        candidate_data = load_json(candidate_file)

        payload = {
            "original-notes": benchmark_data,
            "note-to-evaluate": candidate_data
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()

        result = response.json()

        # Save result
        out_path = os.path.join(output_dir, f"{record_id}.json")
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2)

        print(f"✅ Saved evaluation for {record_id}")
    except Exception as e:
        print(f"❌ Error evaluating {record_id}: {e}")

def main():
    benchmark_files = [f for f in os.listdir(benchmark_dir) if f.startswith("REC-") and f.endswith(".json")]

    for bench_file in benchmark_files:
        record_id = bench_file.replace(".json", "")
        candidate_file = os.path.join(candidate_dir, f"{record_id}-output.processed.json")
        benchmark_file = os.path.join(benchmark_dir, bench_file)

        if os.path.exists(candidate_file):
            evaluate_pair(record_id, benchmark_file, candidate_file)
        else:
            print(f"⚠️ Candidate file not found for {record_id}")

if __name__ == "__main__":
    main()
