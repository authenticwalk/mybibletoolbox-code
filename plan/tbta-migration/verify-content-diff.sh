#!/bin/bash
# Verify migrated content matches source (95%+ similarity)
source_file="$1"
target_file="$2"
threshold=${3:-95}

if [[ ! -f "$source_file" ]]; then
  echo "❌ Source file not found: $source_file"
  exit 1
fi

if [[ ! -f "$target_file" ]]; then
  echo "❌ Target file not found: $target_file"
  exit 1
fi

echo "🔍 Comparing content similarity..."

# Calculate similarity using diff
total_lines=$(wc -l < "$source_file")
if [ $total_lines -eq 0 ]; then
  echo "⚠️ Source file is empty"
  exit 1
fi

diff_lines=$(diff -u "$source_file" "$target_file" | grep -c "^[-+]" || echo "0")
similarity=$((100 - (diff_lines * 100 / total_lines)))

if [ $similarity -ge $threshold ]; then
  echo "✅ Content verified: ${similarity}% similarity (threshold: ${threshold}%)"
  exit 0
else
  echo "❌ Content mismatch: ${similarity}% similarity (need ${threshold}%)"
  echo ""
  echo "Run 'diff -u $source_file $target_file' to see differences"
  exit 1
fi
