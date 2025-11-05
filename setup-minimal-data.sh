#!/bin/bash
# Setup minimal bible data for tool testing and development
#
# This script clones only the essential data needed for bible tool development:
# - Test verses (Matthew 5, John 3, Genesis 1, Mark)
# - Strong's dictionary entries
# - Minimal footprint for fast development
#
# Reduces data clone from 2.6GB to ~100MB
#
# Usage:
#   ./setup-minimal-data.sh [--data-dir PATH] [--force]
#
# Options:
#   --data-dir PATH    Specify data directory (default: .data or $DATA_DIR)
#   --force, -f        Remove existing directory without confirmation
#   --help, -h         Show this help message

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Parse command-line arguments
FORCE=false
CUSTOM_DATA_DIR=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --data-dir)
            CUSTOM_DATA_DIR="$2"
            shift 2
            ;;
        --force|-f)
            FORCE=true
            shift
            ;;
        --help|-h)
            echo "Usage: $0 [--data-dir PATH] [--force]"
            echo ""
            echo "Options:"
            echo "  --data-dir PATH    Specify data directory (default: .data or \$DATA_DIR)"
            echo "  --force, -f        Remove existing directory without confirmation"
            echo "  --help, -h         Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Minimal Bible Data Setup${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Determine data directory with priority: CLI arg > env var > default
if [ -n "$CUSTOM_DATA_DIR" ]; then
    DATA_DIR="$CUSTOM_DATA_DIR"
else
    DATA_DIR="${DATA_DIR:-.data}"
fi
export DATA_DIR

echo -e "${GREEN}Using data directory: $DATA_DIR${NC}"
echo ""

DATA_REPO="https://github.com/authenticwalk/mybibletoolbox-data"

# Check if data directory already exists
if [ -d "$DATA_DIR" ]; then
    echo -e "${YELLOW}Data directory already exists at: $DATA_DIR${NC}"
    if [ "$FORCE" = true ]; then
        echo "  Force flag set, removing existing directory..."
        rm -rf "$DATA_DIR"
        echo "  Removed existing data directory"
    else
        read -p "Do you want to remove it and start fresh? (yes/no): " confirm
        if [ "$confirm" = "yes" ]; then
            rm -rf "$DATA_DIR"
            echo "  Removed existing data directory"
        else
            echo "  Keeping existing data directory"
            exit 0
        fi
    fi
fi

echo -e "${GREEN}Cloning mybibletoolbox-data with sparse checkout...${NC}"
echo ""

# Clone without checking out any files yet
git clone --filter=blob:none --no-checkout "$DATA_REPO" "$DATA_DIR"

cd "$DATA_DIR"

echo ""
echo -e "${GREEN}Setting up sparse checkout patterns...${NC}"
echo ""

# Enable sparse checkout and configure directories to include
git sparse-checkout init --cone
git sparse-checkout set strongs commentary/MAT/005 commentary/JHN/003 commentary/GEN/001

echo ""
echo -e "${GREEN}Checking out specified files...${NC}"
# Now checkout - this will only fetch blobs for the sparse patterns
git checkout main

echo ""
echo -e "${GREEN}✓ Minimal bible data setup complete!${NC}"
echo ""
echo -e "${BLUE}Files installed:${NC}"
find . -type f -not -path './.git/*' | sed 's|^\./||' | cut -d'/' -f1 | sort | uniq -c | sort -rn | awk '{printf "  %s - %s files\n", $2, $1}'
echo ""
echo -e "${YELLOW}To add more books later:${NC}"
echo "  cd $DATA_DIR"
echo "  git sparse-checkout add commentary/MRK"
echo "  git sparse-checkout add commentary/ROM"
echo ""
echo -e "${YELLOW}Usage examples:${NC}"
echo "  # Use custom directory"
echo "  ./setup-minimal-data.sh --data-dir /path/to/data"
echo ""
echo "  # Force reinstall without confirmation"
echo "  ./setup-minimal-data.sh --force"
echo ""
echo "  # Set via environment variable"
echo "  export DATA_DIR=/path/to/data && ./setup-minimal-data.sh"
echo ""
echo -e "${BLUE}========================================${NC}"
