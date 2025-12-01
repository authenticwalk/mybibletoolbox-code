#!/usr/bin/env python3
"""
Baseline Scorer for Simple Label Files
======================================

Scores a simple list of labels (one per line) against a ground truth JSONL file.
Assumes exact line-by-line alignment between the prediction file and ground truth.

Usage:
    python score_baseline.py \
        --predictions predictions.txt \
        --ground-truth validate.jsonl \
        --output report.md
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Dict, Any

def load_labels(filepath: str) -> List[str]:
    """Load labels from a text file (one per line)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def load_ground_truth(filepath: str) -> List[Dict[str, Any]]:
    """Load ground truth from JSONL."""
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    return data

def score(predictions: List[str], ground_truth: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Score predictions against ground truth."""
    if len(predictions) != len(ground_truth):
        print(f"WARNING: Count mismatch! Predictions: {len(predictions)}, Truth: {len(ground_truth)}", file=sys.stderr)
        # Truncate to the shorter length for scoring
        min_len = min(len(predictions), len(ground_truth))
        predictions = predictions[:min_len]
        ground_truth = ground_truth[:min_len]

    correct = 0
    total = len(predictions)
    errors = []

    for i, (pred, truth) in enumerate(zip(predictions, ground_truth)):
        # Try different field names for the value
        actual = truth.get('label') or truth.get('value') or truth.get('tbta_value')
        
        # Normalize for comparison (case-insensitive)
        pred_norm = pred.lower()
        actual_norm = str(actual).lower() if actual else ""

        is_correct = pred_norm == actual_norm
        if is_correct:
            correct += 1
        else:
            errors.append({
                "line": i + 1,
                "verse": truth.get('verse', 'UNKNOWN'),
                "predicted": pred,
                "actual": actual
            })

    accuracy = correct / total if total > 0 else 0

    return {
        "accuracy": accuracy,
        "correct": correct,
        "total": total,
        "errors": errors
    }

def generate_markdown_report(metrics: Dict[str, Any]) -> str:
    """Generate a readable Markdown report."""
    report = []
    report.append(f"# Baseline Analysis Report")
    report.append(f"")
    report.append(f"- **Accuracy**: {metrics['accuracy']:.1%}")
    report.append(f"- **Correct**: {metrics['correct']}/{metrics['total']}")
    report.append(f"")
    report.append(f"## Errors")
    report.append(f"| Line | Verse | Predicted | Actual |")
    report.append(f"|------|-------|-----------|--------|")
    
    for err in metrics['errors']:
        report.append(f"| {err['line']} | {err['verse']} | {err['predicted']} | {err['actual']} |")
    
    return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description="Score baseline predictions")
    parser.add_argument("--predictions", required=True, help="Text file with one label per line")
    parser.add_argument("--ground-truth", required=True, help="JSONL file with ground truth")
    parser.add_argument("--output", required=True, help="Output markdown report file")
    
    args = parser.parse_args()
    
    try:
        predictions = load_labels(args.predictions)
        ground_truth = load_ground_truth(args.ground_truth)
        
        metrics = score(predictions, ground_truth)
        report = generate_markdown_report(metrics)
        
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
            
        print(f"Scoring complete. Accuracy: {metrics['accuracy']:.1%}")
        print(f"Report written to {args.output}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()



