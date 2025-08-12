#!/bin/bash

# install dependencies
sudo apt update && sudo apt install -y curl lshw

# install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# start Ollama server in background
nohup ollama serve > /workspace/ollama.log 2>&1 &

# Wait for server to be ready
sleep 5

# Pull the model
ollama pull qwen3:14b-fp16
ollama pull qwen3:30b-a3b-instruct-2507-q8_0