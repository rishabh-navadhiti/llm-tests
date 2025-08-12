#!/bin/bash

# Create virtual environment
python3 -m venv qwen-venv

# Activate it
source qwen-venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Required packages
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# FlashAttention v2 (latest with PyTorch 2.3+ and CUDA 12.1+)
pip install flash-attn --no-build-isolation
# pip install "flash-attn<2"  # For example: 1.0.9


# Transformers and dependencies
pip install transformers accelerate einops xformers bitsandbytes

# Optional: if your system needs to forcefully recompile xformers
# pip install --no-binary xformers xformers

# Done
echo "Environment setup complete. Activate with:"
echo "source qwen-venv/bin/activate"
