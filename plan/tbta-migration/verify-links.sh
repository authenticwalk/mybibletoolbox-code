#!/bin/bash
# Verify all markdown links point to existing files
cd /workspaces/mybibletoolbox-code/bible-study-tools/tbta
errors=0

echo "🔍 Checking markdown links..."

while IFS= read -r file; do
  while IFS= read -r link; do
    # Extract path from [text](path) format
    path=$(echo "$link" | sed 's/.*(\(.*\)).*/\1/')

    # Skip URLs and anchors
    [[ "$path" =~ ^http ]] && continue
    [[ "$path" =~ ^# ]] && continue

    # Check if file exists (relative to current file's directory)
    dir=$(dirname "$file")
    if [[ ! -f "$dir/$path" && ! -f "$path" && ! -f "/workspaces/mybibletoolbox-code/$path" ]]; then
      echo "❌ Broken link in $file: $path"
      ((errors++))
    fi
  done < <(grep -o '\[.*\](.*[^)])' "$file" 2>/dev/null || true)
done < <(find . -name "*.md")

if [ $errors -eq 0 ]; then
  echo "✅ All links valid"
  exit 0
else
  echo "❌ Found $errors broken links"
  exit 1
fi
