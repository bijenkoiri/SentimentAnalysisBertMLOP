#!/bin/bash

# Install gdown (only if needed at runtime)
pip install gdown

# Download checkpoint folder using gdown
echo "Downloading checkpoint folder from Google Drive..."
gdown --folder https://drive.google.com/drive/folders/1_g6NKcUfkpUOKgbq1vBio1Pm5DmIeHAA?usp=sharing -O checkpoints2

# Start the FastAPI app
echo "Starting FastAPI server..."
uvicorn main:app --host 0.0.0.0 --port 8000
