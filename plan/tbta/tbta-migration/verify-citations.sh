#!/bin/bash
# Verify all {citations} exist in ATTRIBUTION.md
cd /workspaces/mybibletoolbox-code/bible-study-tools/tbta
attribution_file="../../ATTRIBUTION.md"
errors=0

echo "🔍 Checking citations..."

if [[ ! -f "$attribution_file" ]]; then
  echo "⚠️ ATTRIBUTION.md not found at $attribution_file"
  exit 1
fi

# Extract all citations from markdown files
while IFS= read -r file; do
  while IFS= read -r citation; do
    # Extract citation code from {code} format
    code=$(echo "$citation" | sed 's/.*{\(.*\)}.*/\1/')

    # Skip empty or malformed citations
    [[ -z "$code" ]] && continue

    # Check if citation exists in ATTRIBUTION.md
    if ! grep -q "$code" "$attribution_file"; then
      echo "❌ Unknown citation in $file: {$code}"
      ((errors++))
    fi
  done < <(grep -o '{[a-zA-Z0-9_-]*}' "$file" 2>/dev/null || true)
done < <(find . -name "*.md")

if [ $errors -eq 0 ]; then
  echo "✅ All citations valid"
  exit 0
else
  echo "❌ Found $errors unknown citations"
  exit 1
fi
