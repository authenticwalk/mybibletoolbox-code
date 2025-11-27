#!/bin/bash
# batch-claude.sh - Run Claude with a prompt template for each item in a list
#
# Usage:
#   ./batch-claude.sh --list "item1,item2,item3" --prompt "Do something with \${value}"
#   ./batch-claude.sh --list-file items.txt --prompt "Process \${value}"
#   ./batch-claude.sh --list-dir ./path/to/dir --prompt "Analyze \${value}"
#
# Options:
#   --list        Comma-separated list of values
#   --list-file   File with one value per line
#   --list-dir    Directory (uses subdirectory names as values)
#   --prompt      Prompt template with ${value} placeholder
#   --dry-run     Echo commands instead of running them
#   --parallel    Number of parallel Claude instances (default: 1)

set -e

# Parse arguments
LIST=""
LIST_FILE=""
LIST_DIR=""
PROMPT=""
DRY_RUN=false
PARALLEL=1

while [[ $# -gt 0 ]]; do
    case $1 in
        --list)
            LIST="$2"
            shift 2
            ;;
        --list-file)
            LIST_FILE="$2"
            shift 2
            ;;
        --list-dir)
            LIST_DIR="$2"
            shift 2
            ;;
        --prompt)
            PROMPT="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --parallel)
            PARALLEL="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 [--list CSV | --list-file FILE | --list-dir DIR] --prompt TEMPLATE [--dry-run] [--parallel N]"
            echo ""
            echo "Options:"
            echo "  --list        Comma-separated list of values"
            echo "  --list-file   File with one value per line"
            echo "  --list-dir    Directory (uses subdirectory names as values)"
            echo "  --prompt      Prompt template with \${value} placeholder"
            echo "  --dry-run     Echo commands instead of running them"
            echo "  --parallel    Number of parallel Claude instances (default: 1)"
            echo ""
            echo "Example:"
            echo "  $0 --list-dir ./bible-study-tools/tbta/features --prompt 'Analyze feature \${value}' --dry-run"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Validate arguments
if [[ -z "$PROMPT" ]]; then
    echo "Error: --prompt is required"
    exit 1
fi

if [[ -z "$LIST" && -z "$LIST_FILE" && -z "$LIST_DIR" ]]; then
    echo "Error: One of --list, --list-file, or --list-dir is required"
    exit 1
fi

# Build the list of values
VALUES=()

if [[ -n "$LIST" ]]; then
    IFS=',' read -ra VALUES <<< "$LIST"
elif [[ -n "$LIST_FILE" ]]; then
    if [[ ! -f "$LIST_FILE" ]]; then
        echo "Error: List file not found: $LIST_FILE"
        exit 1
    fi
    while IFS= read -r line; do
        [[ -n "$line" ]] && VALUES+=("$line")
    done < "$LIST_FILE"
elif [[ -n "$LIST_DIR" ]]; then
    if [[ ! -d "$LIST_DIR" ]]; then
        echo "Error: Directory not found: $LIST_DIR"
        exit 1
    fi
    for dir in "$LIST_DIR"/*/; do
        if [[ -d "$dir" ]]; then
            name=$(basename "$dir")
            # Skip hidden directories and common non-feature dirs
            [[ "$name" != .* && "$name" != "features-archive" ]] && VALUES+=("$name")
        fi
    done
fi

if [[ ${#VALUES[@]} -eq 0 ]]; then
    echo "Error: No values found"
    exit 1
fi

echo "=== Batch Claude Runner ==="
echo "Items: ${#VALUES[@]}"
echo "Prompt template: $PROMPT"
echo "Parallel: $PARALLEL"
echo "Dry run: $DRY_RUN"
echo ""

# Function to run claude for a single value
run_claude() {
    local value="$1"
    # Handle both ${value} and \${value} (backslash-escaped from shell)
    local expanded_prompt="${PROMPT//\$\{value\}/$value}"
    expanded_prompt="${expanded_prompt//\\\$\{value\}/$value}"
    
    echo "--- Running for: $value ---"
    echo "Prompt: $expanded_prompt"
    echo ""
    
    if [[ "$DRY_RUN" == "true" ]]; then
        echo "[DRY RUN] Would execute: claude --print \"$expanded_prompt\""
        echo ""
    else
        claude --print "$expanded_prompt"
    fi
}

export -f run_claude
export PROMPT
export DRY_RUN

# Run with or without parallelism
if [[ "$PARALLEL" -gt 1 ]]; then
    printf '%s\n' "${VALUES[@]}" | xargs -I {} -P "$PARALLEL" bash -c 'run_claude "$@"' _ {}
else
    for value in "${VALUES[@]}"; do
        run_claude "$value"
    done
fi

echo "=== Completed ${#VALUES[@]} items ==="

