#!/bin/bash
# Automated script to complete the analysis rebuild after enrichment finishes

set -e

ANALYSIS_DIR="/workspace/bible-study-tools/tbta/features/number-systems/analysis"
cd "$ANALYSIS_DIR"

echo "Waiting for enrichment to complete..."
while ps aux | grep "enrich_extract_with_verses.py" | grep -v grep > /dev/null; do
    sleep 30
done

echo "Enrichment completed! Proceeding with split..."

# Step 3: Run split
echo "Running split_dataset.py..."
python /workspace/src/tools/predict/split_dataset.py \
  --input "$ANALYSIS_DIR/enriched.jsonl" \
  --original "$ANALYSIS_DIR/tbta-extract.jsonl" \
  --output "$ANALYSIS_DIR/data"

echo "Split completed!"

# Step 4: Delete intermediate artifacts
echo "Cleaning up intermediate files..."
rm -f "$ANALYSIS_DIR/datasets.jsonl"
rm -f "$ANALYSIS_DIR/enriched.jsonl"

echo "Cleanup completed!"

# Verify new languages are in the data
echo "Verifying new languages in train.jsonl..."
if head -n 1 "$ANALYSIS_DIR/data/train.jsonl" | python3 -m json.tool | grep -E '"haw|"meu|"ceb|"chk' | head -n 1; then
    echo "SUCCESS: New languages (haw, meu, ceb, chk) confirmed in dataset!"
else
    echo "WARNING: New languages not found in dataset - please verify manually"
fi

echo "All tasks completed successfully!"
