#!/bin/bash
set -e

# --- Config ---
HF_CACHE="$HOME/.cache/huggingface"
VENV_PATH="/workspace/llm-tests/llm-venv"

declare -A MODELS=(
  ["gptoss-20b"]="openai/gpt-oss-20b"
  ["gptoss-120b"]="openai/gpt-oss-120b"
  ["qwen3-30b"]="Qwen/Qwen3-30B-A3B-Instruct-2507-FP8"
  ["qwen3-4b"]="Qwen/Qwen3-4B-Instruct-2507"
  ["magistral-small"]="mistralai/Magistral-Small-2507"
  ["magistral-redhat"]="RedHatAI/Magistral-Small-2506-FP8"
  ["mistral-7b"]="mistralai/Mistral-7B-Instruct-v0.3"
  ["mistral-nemo"]="mistralai/Mistral-Nemo-Instruct-2407"
  ["deepseek-qwen14b"]="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
  ["deepseek-redhat-30B"]="RedHatAI/DeepSeek-R1-Distill-Qwen-32B-FP8-dynamic"
  ["gemma-redhat-27b"]="RedHatAI/gemma-3-27b-it-FP8-dynamic"
  ["medgemma-27b"]="google/medgemma-27b-text-it"
  

)

if [ -z "$1" ]; then
  echo "Usage: $0 <short-model-name>"
  echo "Options: ${!MODELS[@]}"
  exit 1
fi

SHORT="$1"
MODEL="${MODELS[$SHORT]}"
if [ -z "$MODEL" ]; then
  echo "Unknown model: $SHORT"
  echo "Options: ${!MODELS[@]}"
  exit 1
fi

echo "🔹 Selected model: $MODEL"
export VLLM_MODEL_NAME="$MODEL"

# Clear HF cache if needed
if [ -d "$HF_CACHE/hub/models--${MODEL//\//--}" ]; then
  echo "✔ Model already cached"
else
  echo "🗑 Clearing HF cache"
  rm -rf "$HF_CACHE"
fi

# Activate venv
echo "🐍 Activating virtual environment..."
source "$VENV_PATH/bin/activate"

# No pip installs here — your setup script handles that!

echo "⚡ Launching vLLM server with model: $MODEL"
vllm serve --max_model_len=32000 --gpu_memory_utilization=0.95 "$MODEL"
