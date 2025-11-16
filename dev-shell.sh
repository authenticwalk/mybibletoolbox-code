#!/bin/bash
# Enter isolated development environment

cd "$(dirname "$0")"

# Make sure Colima is running
if ! docker info &>/dev/null; then
    echo "Starting Colima..."
    colima start --cpu 4 --memory 20
fi

# Build custom image if it doesn't exist
IMAGE_NAME="mybibletoolbox-dev:latest"
if ! docker image inspect "$IMAGE_NAME" &>/dev/null; then
    echo "Building development image (first time only)..."
    docker build -f .devcontainer/Dockerfile -t "$IMAGE_NAME" .devcontainer/
fi

# Start the isolated container
echo "Starting isolated development environment..."
echo "Your Mac is protected - commands run only inside the container."
echo "Type 'exit' to leave the container."
echo ""

docker run --rm -it \
  -v "$(pwd):/workspace" \
  -w /workspace \
  --memory=12g \
  --cpus=4 \
  --security-opt=no-new-privileges:true \
  --cap-drop=ALL \
  --cap-add=CHOWN \
  --cap-add=SETGID \
  --cap-add=SETUID \
  "$IMAGE_NAME" \
  bash

