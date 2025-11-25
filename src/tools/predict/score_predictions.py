#!/usr/bin/env python3
"""
Generic Prediction Scorer

Compares predictions against ground truth and calculates accuracy metrics.
Feature-agnostic - works for any TBTA feature by comparing predicted vs actual values.

Usage:
    python score_predictions.py \\
        --predictions test_predictions.yaml \\
        --ground-truth test.yaml \\
        --output scoring_report.yaml \\
        --matcher-config config.json
"""

import json
import yaml
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import defaultdict


def load_data(filepath: str, format: str = 'auto') -> List[Dict[str, Any]]:
    """
    Load data from YAML or JSON file.

    Args:
        filepath: Path to data file
        format: File format ('yaml', 'json', 'jsonl', or 'auto' to detect)

    Returns:
        List of dictionaries

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file format is invalid
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    # Auto-detect format
    if format == 'auto':
        suffix = path.suffix.lower()
        if suffix in ['.yaml', '.yml']:
            format = 'yaml'
        elif suffix == '.json':
            format = 'json'
        elif suffix == '.jsonl':
            format = 'jsonl'
        else:
            raise ValueError(f"Cannot auto-detect format for: {filepath}")

    # Load based on format
    if format == 'yaml':
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            # Ensure it's a list
            if isinstance(data, dict):
                data = [data]
            elif not isinstance(data, list):
                raise ValueError(f"YAML file must contain a list or dict: {filepath}")
            return data

    elif format == 'json':
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict):
                data = [data]
            elif not isinstance(data, list):
                raise ValueError(f"JSON file must contain a list or dict: {filepath}")
            return data

    elif format == 'jsonl':
        data = []
        with open(path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError as e:
                    raise ValueError(f"Invalid JSON on line {line_num} of {filepath}: {e}")
        return data

    else:
        raise ValueError(f"Unsupported format: {format}")


def match_prediction(
    prediction: Dict[str, Any],
    ground_truth: Dict[str, Any],
    matcher_config: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Match a prediction against ground truth.

    Args:
        prediction: Prediction entry with 'verse' and 'predicted_value'
        ground_truth: Ground truth entry with 'verse' and 'actual_value'
        matcher_config: Optional configuration for matching (e.g., fuzzy matching, normalization)

    Returns:
        Dictionary with:
        - verse: Verse reference
        - predicted: Predicted value
        - actual: Actual value
        - correct: Boolean indicating if prediction matches
        - confidence: Confidence level (if provided)
        - metadata: Any additional metadata
    """
    matcher_config = matcher_config or {}

    verse = prediction.get('verse')
    predicted_value = prediction.get('predicted_value', prediction.get('value'))
    actual_value = ground_truth.get('actual_value', ground_truth.get('tbta_value', ground_truth.get('value')))
    confidence = prediction.get('confidence', 'unknown')

    # Normalization if configured
    if matcher_config.get('normalize', False):
        if predicted_value:
            predicted_value = str(predicted_value).lower().strip()
        if actual_value:
            actual_value = str(actual_value).lower().strip()

    # Compare
    correct = predicted_value == actual_value

    return {
        'verse': verse,
        'predicted': predicted_value,
        'actual': actual_value,
        'correct': correct,
        'confidence': confidence,
        'genre': ground_truth.get('genre', 'unknown')
    }


def calculate_accuracy(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate accuracy metrics from match results.

    Args:
        results: List of match result dictionaries

    Returns:
        Dictionary with overall and by-category metrics
    """
    overall = {'correct': 0, 'total': 0}
    by_confidence = defaultdict(lambda: {'correct': 0, 'total': 0})
    by_genre = defaultdict(lambda: {'correct': 0, 'total': 0})
    errors = []

    for result in results:
        # Overall
        overall['total'] += 1
        if result['correct']:
            overall['correct'] += 1
        else:
            errors.append({
                'verse': result['verse'],
                'predicted': result['predicted'],
                'actual': result['actual'],
                'confidence': result['confidence'],
                'genre': result['genre']
            })

        # By confidence
        confidence = result['confidence']
        by_confidence[confidence]['total'] += 1
        if result['correct']:
            by_confidence[confidence]['correct'] += 1

        # By genre
        genre = result['genre']
        by_genre[genre]['total'] += 1
        if result['correct']:
            by_genre[genre]['correct'] += 1

    # Calculate percentages
    metrics = {
        'overall': {
            'accuracy': overall['correct'] / overall['total'] if overall['total'] > 0 else 0.0,
            'correct': overall['correct'],
            'total': overall['total'],
            'percentage': round((overall['correct'] / overall['total']) * 100, 2) if overall['total'] > 0 else 0.0
        },
        'by_confidence': {},
        'by_genre': {},
        'errors': errors
    }

    for confidence, counts in by_confidence.items():
        metrics['by_confidence'][confidence] = {
            'accuracy': counts['correct'] / counts['total'] if counts['total'] > 0 else 0.0,
            'correct': counts['correct'],
            'total': counts['total'],
            'percentage': round((counts['correct'] / counts['total']) * 100, 2) if counts['total'] > 0 else 0.0
        }

    for genre, counts in by_genre.items():
        metrics['by_genre'][genre] = {
            'accuracy': counts['correct'] / counts['total'] if counts['total'] > 0 else 0.0,
            'correct': counts['correct'],
            'total': counts['total'],
            'percentage': round((counts['correct'] / counts['total']) * 100, 2) if counts['total'] > 0 else 0.0
        }

    return metrics


def score_predictions(
    predictions: List[Dict[str, Any]],
    ground_truth: List[Dict[str, Any]],
    matcher_config: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Score predictions against ground truth.

    Args:
        predictions: List of prediction dictionaries
        ground_truth: List of ground truth dictionaries
        matcher_config: Optional matcher configuration

    Returns:
        Scoring report with accuracy metrics
    """
    # Create lookup for ground truth by verse
    truth_lookup = {entry['verse']: entry for entry in ground_truth}

    # Match predictions
    results = []
    unmatched = []

    for pred in predictions:
        verse = pred.get('verse')
        if not verse:
            unmatched.append({'error': 'Missing verse field', 'prediction': pred})
            continue

        if verse not in truth_lookup:
            unmatched.append({'error': 'Verse not in ground truth', 'verse': verse, 'prediction': pred})
            continue

        result = match_prediction(pred, truth_lookup[verse], matcher_config)
        results.append(result)

    # Calculate metrics
    metrics = calculate_accuracy(results)

    # Add unmatched entries
    metrics['unmatched'] = unmatched

    return metrics


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Score predictions against ground truth',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Score test predictions
  python score_predictions.py \\
      --predictions test_predictions.yaml \\
      --ground-truth test.yaml \\
      --output scoring_report.yaml

  # Use custom matcher config
  python score_predictions.py \\
      --predictions predictions.jsonl \\
      --ground-truth answers.jsonl \\
      --matcher-config matcher.json \\
      --output report.json
        """
    )

    parser.add_argument(
        '--predictions',
        required=True,
        help='Predictions file (YAML, JSON, or JSONL)'
    )

    parser.add_argument(
        '--ground-truth',
        required=True,
        help='Ground truth file (YAML, JSON, or JSONL)'
    )

    parser.add_argument(
        '--output',
        required=True,
        help='Output report file (YAML or JSON)'
    )

    parser.add_argument(
        '--matcher-config',
        help='Optional matcher configuration JSON file'
    )

    parser.add_argument(
        '--format',
        choices=['auto', 'yaml', 'json', 'jsonl'],
        default='auto',
        help='Input file format (default: auto-detect)'
    )

    args = parser.parse_args()

    try:
        # Load data
        print(f"Loading predictions from {args.predictions}...", file=sys.stderr)
        predictions = load_data(args.predictions, args.format)
        print(f"Loaded {len(predictions)} predictions", file=sys.stderr)

        print(f"Loading ground truth from {args.ground_truth}...", file=sys.stderr)
        ground_truth = load_data(args.ground_truth, args.format)
        print(f"Loaded {len(ground_truth)} ground truth entries", file=sys.stderr)

        # Load matcher config if provided
        matcher_config = None
        if args.matcher_config:
            print(f"Loading matcher config from {args.matcher_config}...", file=sys.stderr)
            with open(args.matcher_config, 'r', encoding='utf-8') as f:
                matcher_config = json.load(f)

        # Score predictions
        print("Scoring predictions...", file=sys.stderr)
        report = score_predictions(predictions, ground_truth, matcher_config)

        # Save report
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if output_path.suffix.lower() in ['.yaml', '.yml']:
            with open(output_path, 'w', encoding='utf-8') as f:
                yaml.dump(report, f, default_flow_style=False, allow_unicode=True)
        else:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)

        # Print summary
        print("\n" + "="*60, file=sys.stderr)
        print("PREDICTION SCORING REPORT", file=sys.stderr)
        print("="*60, file=sys.stderr)
        print(f"Overall accuracy: {report['overall']['percentage']:.2f}%", file=sys.stderr)
        print(f"Correct: {report['overall']['correct']}/{report['overall']['total']}", file=sys.stderr)
        print(f"Errors: {len(report['errors'])}", file=sys.stderr)
        print(f"Unmatched: {len(report['unmatched'])}", file=sys.stderr)
        print("="*60, file=sys.stderr)
        print(f"\n✓ Report saved to {args.output}", file=sys.stderr)

        sys.exit(0)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
