#!/bin/bash
# Setup environment variables for myBibleToolbox development
# Source this file to set up your shell environment:
#   source setup-env.sh

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Data directory for commentary, strongs, and cached data
export DATA_DIR="${DATA_DIR:-${SCRIPT_DIR}/.data}"

# eBible corpus directory (1000+ Bible translations)
export EBIBLE_DIR="${EBIBLE_DIR:-${HOME}/projects/ebible}"

echo "Environment variables set:"
echo "  DATA_DIR=${DATA_DIR}"
echo "  EBIBLE_DIR=${EBIBLE_DIR}"
echo ""

# Check if directories exist and provide guidance
if [ ! -d "$DATA_DIR" ]; then
    echo "⚠️  DATA_DIR not found: $DATA_DIR"
    echo "   Run: ./setup-minimal-data.sh"
    echo ""
fi

if [ ! -d "$EBIBLE_DIR" ]; then
    echo "⚠️  EBIBLE_DIR not found: $EBIBLE_DIR"
    echo "   To set up eBible corpus:"
    echo "   1. Create directory: mkdir -p ~/projects"
    echo "   2. Clone repo: git clone --depth 1 https://github.com/BibleNLP/ebible ~/projects/ebible"
    echo "   3. This is a large repo (~500MB), so --depth 1 recommended"
    echo ""
    echo "   Alternative: Set EBIBLE_DIR to different location before sourcing this script"
    echo ""
fi

# Validate eBible directory structure
if [ -d "$EBIBLE_DIR" ]; then
    if [ ! -d "$EBIBLE_DIR/corpus" ] || [ ! -f "$EBIBLE_DIR/metadata/vref.txt" ]; then
        echo "⚠️  EBIBLE_DIR exists but appears incomplete"
        echo "   Expected structure:"
        echo "     $EBIBLE_DIR/corpus/*.txt"
        echo "     $EBIBLE_DIR/metadata/vref.txt"
        echo ""
    else
        echo "✓ eBible corpus found and validated"
        echo ""
    fi
fi

