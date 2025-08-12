#!/bin/bash
set -e

echo "🔹 Updating system packages..."
apt update
apt install -y python3.12 python3.12-venv python3.12-dev git build-essential

echo "🐍 Creating virtual environment..."
python3.12 -m venv llm-venv
source llm-venv/bin/activate

echo "Upgrading pip, setuptools, wheel..."
pip install --upgrade pip setuptools wheel

echo "📦 Installing uv..."
pip install uv

echo "Installing PyTorch nightly with CUDA 12.8 (required by GPT-OSS vLLM)..."
pip install --pre torch==2.9.0.dev20250804+cu128 torchvision torchaudio \
  --extra-index-url https://download.pytorch.org/whl/nightly/cu128

echo "Installing triton compatible with PyTorch 2.9 and CUDA 12.8..."
pip install --pre triton --extra-index-url https://download.pytorch.org/whl/nightly/cu128

pip install --upgrade kernels
# pip install flash-attn --upgrade


echo "Installing GPT-OSS special vLLM build..."
pip install --pre vllm==0.10.1+gptoss \
  --extra-index-url https://wheels.vllm.ai/gpt-oss/ \
  --extra-index-url https://download.pytorch.org/whl/nightly/cu128

echo "Installing extras: huggingface_hub, transformers..."
pip install huggingface_hub transformers

echo "✅ Setup complete! Activate environment with:"
echo "source llm-venv/bin/activate"
