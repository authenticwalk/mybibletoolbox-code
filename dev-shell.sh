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

# Setup environment variables for the container
WORKSPACE_DIR="/workspace"
DATA_DIR="${WORKSPACE_DIR}/.data"

# Check if eBible corpus exists on host
EBIBLE_HOST_DIR="${HOME}/projects/ebible"
EBIBLE_MOUNT_OPTS=""
EBIBLE_CONTAINER_DIR="/ebible"

if [ -d "$EBIBLE_HOST_DIR" ]; then
    echo "Mounting eBible corpus from: $EBIBLE_HOST_DIR"
    EBIBLE_MOUNT_OPTS="-v ${EBIBLE_HOST_DIR}:${EBIBLE_CONTAINER_DIR}:ro"
    EBIBLE_DIR="${EBIBLE_CONTAINER_DIR}"
else
    echo "⚠️  eBible corpus not found at: $EBIBLE_HOST_DIR"
    echo "   The container will clone to /tmp/ebible if needed"
    echo "   To use a local copy, clone it first:"
    echo "   git clone --depth 1 https://github.com/BibleNLP/ebible ~/projects/ebible"
    echo ""
    EBIBLE_DIR="/tmp/ebible"
fi

# Start the isolated container
echo "Starting isolated development environment..."
echo "Environment:"
echo "  DATA_DIR=${DATA_DIR}"
echo "  EBIBLE_DIR=${EBIBLE_DIR}"
echo ""
echo "Your Mac is protected - commands run only inside the container."
echo "Type 'exit' to leave the container."
echo ""

docker run --rm -it \
  -v "$(pwd):/workspace" \
  ${EBIBLE_MOUNT_OPTS} \
  -w /workspace \
  -e DATA_DIR="${DATA_DIR}" \
  -e EBIBLE_DIR="${EBIBLE_DIR}" \
  --memory=12g \
  --cpus=4 \
  --security-opt=no-new-privileges:true \
  --cap-drop=ALL \
  --cap-add=CHOWN \
  --cap-add=SETGID \
  --cap-add=SETUID \
  "$IMAGE_NAME" \
  bash

