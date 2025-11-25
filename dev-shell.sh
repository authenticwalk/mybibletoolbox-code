#!/bin/bash
# Enter isolated development environment

cd "$(dirname "$0")"

CONTAINER_NAME="mybibletoolbox-dev"

# Make sure Colima is running
if ! docker info &>/dev/null; then
    echo "Starting Colima..."
    colima start --cpu 4 --memory 20
fi

# Check if container is already running
if docker ps --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo "✅ Container '$CONTAINER_NAME' is already running."
    echo "   Opening a new shell in the existing instance..."
    echo ""
    docker exec -it "$CONTAINER_NAME" bash -c "stty sane; bash"
    exit 0
fi

# Cleanup stopped container if it exists (from a crash/non-clean exit)
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo "🧹 Removing stale container instance..."
    docker rm -f "$CONTAINER_NAME" > /dev/null
fi

# Calculate hash of Dockerfile to ensure image is up-to-date
DOCKERFILE_HASH=$(shasum .devcontainer/Dockerfile | awk '{print $1}')
IMAGE_NAME="mybibletoolbox-dev:${DOCKERFILE_HASH}"

# Build custom image if it doesn't exist
if ! docker image inspect "$IMAGE_NAME" &>/dev/null; then
    echo "🏗️  Building development image (Docker file changed)..."
    docker build -f .devcontainer/Dockerfile -t "$IMAGE_NAME" .devcontainer/
    # Tag as latest for convenience
    docker tag "$IMAGE_NAME" "mybibletoolbox-dev:latest"
fi

# Setup environment variables for the container
WORKSPACE_DIR="/workspace"
DATA_DIR="${WORKSPACE_DIR}/.data"

# Check if eBible corpus exists on host
EBIBLE_HOST_DIR="${HOME}/projects/ebible"
EBIBLE_MOUNT_OPTS=""
EBIBLE_CONTAINER_DIR="/ebible"

if [ -d "$EBIBLE_HOST_DIR" ]; then
    echo "📚 Mounting eBible corpus from: $EBIBLE_HOST_DIR"
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

# Pass ANTHROPIC_API_KEY if set in host environment
API_KEY_OPTS=""
if [ -n "$ANTHROPIC_API_KEY" ]; then
    echo "🔑 Passing ANTHROPIC_API_KEY from host environment"
    API_KEY_OPTS="-e ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}"
fi

# Start the isolated container
echo "🚀 Starting new isolated development environment..."
echo "   Container: $CONTAINER_NAME"
echo "   Environment:"
echo "     DATA_DIR=${DATA_DIR}"
echo "     EBIBLE_DIR=${EBIBLE_DIR}"
echo ""
echo "🛡️  Your Mac is protected - commands run only inside the container."
echo "   Type 'exit' to leave the container."
echo ""

# Create persistence directories
mkdir -p .dev-persistence/config .dev-persistence/claude .dev-persistence/npm-global

# Note: stty handling fixes Ctrl+C behavior
docker run --rm -it \
  --name "$CONTAINER_NAME" \
  -v "$(pwd):/workspace" \
  -v "$(pwd)/.dev-persistence/config:/home/devuser/.config" \
  -v "$(pwd)/.dev-persistence/claude:/home/devuser/.claude" \
  ${EBIBLE_MOUNT_OPTS} \
  -w /workspace \
  -e DATA_DIR="${DATA_DIR}" \
  -e EBIBLE_DIR="${EBIBLE_DIR}" \
  ${API_KEY_OPTS} \
  --memory=12g \
  --cpus=4 \
  --security-opt=no-new-privileges:true \
  --cap-drop=ALL \
  --cap-add=CHOWN \
  --cap-add=SETGID \
  --cap-add=SETUID \
  "$IMAGE_NAME" \
  bash -c "stty sane; claude --dangerously-skip-permissions; bash"
