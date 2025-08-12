# First, you need to ensure you have a modern version of Python (3.8 or higher)
# and a recent version of pip. This script assumes you are running a compatible
# version of both.

# Step 1: Install or upgrade the required libraries.
# The `openai/gpt-oss-20b` model requires recent versions of `transformers`
# and `accelerate` for compatibility with `bitsandbytes` quantization.
# `bitsandbytes` is also required for the quantization itself.
# The `--upgrade` flag ensures you get the latest, compatible versions.
# The `pip install` command is wrapped in a try/except block to catch any
# potential installation errors.
try:
    import subprocess
    import sys

    print("Upgrading `bitsandbytes`, `transformers`, and `accelerate`...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "--upgrade",
        "bitsandbytes", "transformers", "accelerate"
    ])
    print("Installation complete.")

except subprocess.CalledProcessError as e:
    print(f"An error occurred during installation: {e}")
    sys.exit(1)

# Step 2: Import the necessary classes from the updated libraries.
# `BitsAndBytesConfig` is now compatible with `AutoModelForCausalLM` and
# `AutoTokenizer`.
try:
    from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
    import torch

    print("\nLibraries imported successfully.")

except ImportError as e:
    print(f"Error importing libraries after installation: {e}")
    print("Please ensure your Python environment is clean and try again.")
    sys.exit(1)

# Step 3: Define the quantization configuration.
# The `bnb_4bit_compute_dtype` and `bnb_4bit_quant_type` are crucial for
# a successful load.
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

# Step 4: Specify the model name.
model_id = "openai/gpt-oss-20b"
print(f"Attempting to load model: {model_id}")

try:
    # Step 5: Load the model and tokenizer with the new configuration.
    # The `device_map="auto"` argument automatically handles placing the model
    # parts on your available hardware (CPU and GPU).
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=quantization_config,
        device_map="auto",
    )

    print(f"\nModel '{model_id}' loaded successfully!")
    print(f"Model on device: {model.device}")

    # Optional: A simple test to verify the model is working.
    print("\nRunning a quick test...")
    prompt = "Explain why the sky is blue."
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=50)

    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Generated Text:")
    print(decoded_output)

except Exception as e:
    print(f"An error occurred while loading the model: {e}")

