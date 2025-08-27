import os
import json

INPUT_DIR = "/Users/rish/Development/runpod dev/llm-tests/newTest/GPT-OSS-120b/LLM-eval"

EXPECTED_FIELDS = {
    "PATIENT_NAME",
    "CHIEF_COMPLAINT",
    "HPI_SPENCER",
    "MUSCULOSKELETAL_VERBATIM",
    "IMAGING_RESULTS",
    "ASSESSMENT_SPENCER",
    "PLAN_SPENCER_"
}

def check_fields(input_dir):
    for filename in sorted(os.listdir(input_dir)):
        if filename.endswith("-eval.json"):
            file_path = os.path.join(input_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            fields = set(data.get("field_scores", {}).keys())
            extra = fields - EXPECTED_FIELDS
            missing = EXPECTED_FIELDS - fields

            if extra or missing:
                print(f"⚠️ {filename}")
                if extra:
                    print(f"   Extra fields: {extra}")
                if missing:
                    print(f"   Missing fields: {missing}")

if __name__ == "__main__":
    check_fields(INPUT_DIR)
