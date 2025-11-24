#!/usr/bin/env python3
"""
Predictions Validation Tool

Compares predicted answers against answer keys and calculates accuracy metrics.
Supports train/test/validate modes with configurable error reporting.
"""

import json
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple


def load_jsonl(filepath: str) -> List[Dict[str, Any]]:
    """
    Load JSONL file and return list of records.

    Args:
        filepath: Path to JSONL file

    Returns:
        List of dictionaries from JSONL file

    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file contains invalid JSON
    """
    records = []
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(
                    f"Invalid JSON on line {line_num}: {e.msg}",
                    e.doc,
                    e.pos
                )

    return records


def validate_predictions(
    predictions: List[Dict[str, Any]],
    answers: List[Dict[str, Any]],
    mode: str,
    show_errors: bool
) -> Dict[str, Any]:
    """
    Validate predictions against answer key.

    Args:
        predictions: List of prediction records with verse, predicted_value, confidence
        answers: List of answer key records with verse, tbta_value, genre
        mode: Validation mode (train|test|validate)
        show_errors: Whether to include error details in output

    Returns:
        Dictionary with validation results including accuracy metrics and errors
    """
    # Create lookup dictionary for answers by verse
    answer_lookup = {record['verse']: record for record in answers}

    # Track results
    results = []
    correct_count = 0
    incorrect_count = 0
    errors = []

    for pred in predictions:
        verse = pred.get('verse')
        predicted_value = pred.get('predicted_value')
        confidence = pred.get('confidence', 'unknown')

        # Validation checks
        if not verse:
            error = {
                'verse': None,
                'error': 'Missing verse field in prediction',
                'prediction': pred
            }
            errors.append(error)
            incorrect_count += 1
            continue

        if not predicted_value:
            error = {
                'verse': verse,
                'error': 'Missing predicted_value field',
                'prediction': pred
            }
            errors.append(error)
            incorrect_count += 1
            continue

        # Check if verse exists in answer key
        if verse not in answer_lookup:
            error = {
                'verse': verse,
                'error': 'Verse not found in answer key',
                'predicted_value': predicted_value,
                'confidence': confidence
            }
            errors.append(error)
            incorrect_count += 1
            continue

        # Compare prediction with answer
        answer = answer_lookup[verse]
        tbta_value = answer.get('tbta_value')

        if predicted_value == tbta_value:
            correct_count += 1
            results.append({
                'verse': verse,
                'correct': True,
                'predicted': predicted_value,
                'actual': tbta_value
            })
        else:
            incorrect_count += 1
            error_detail = {
                'verse': verse,
                'error': 'Incorrect prediction',
                'predicted_value': predicted_value,
                'actual_value': tbta_value,
                'confidence': confidence,
                'genre': answer.get('genre', 'unknown')
            }
            errors.append(error_detail)
            results.append({
                'verse': verse,
                'correct': False,
                'predicted': predicted_value,
                'actual': tbta_value
            })

    # Calculate metrics
    total = correct_count + incorrect_count
    accuracy = correct_count / total if total > 0 else 0.0

    # Build output
    output = {
        'mode': mode,
        'accuracy': round(accuracy, 4),
        'total': total,
        'correct': correct_count,
        'incorrect': incorrect_count
    }

    # Include errors based on mode and show_errors flag
    # Never show errors for validate mode unless explicitly requested
    if show_errors and (mode != 'validate' or show_errors):
        output['errors'] = errors

    return output


def calculate_metrics(results: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate detailed accuracy metrics from validation results.

    Args:
        results: Validation results dictionary

    Returns:
        Dictionary with calculated metrics
    """
    total = results['total']
    correct = results['correct']
    incorrect = results['incorrect']

    metrics = {
        'accuracy': results['accuracy'],
        'accuracy_percentage': round(results['accuracy'] * 100, 2),
        'total_predictions': total,
        'correct_predictions': correct,
        'incorrect_predictions': incorrect,
        'error_rate': round(incorrect / total, 4) if total > 0 else 0.0
    }

    return metrics


def main():
    """CLI entry point for predictions validation tool."""
    parser = argparse.ArgumentParser(
        description='Validate predictions against answer keys',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate test predictions with errors
  python validate_predictions.py --predictions test_pred.jsonl --answers answers.jsonl --mode test --show-errors

  # Validate without showing errors
  python validate_predictions.py --predictions val_pred.jsonl --answers answers.jsonl --mode validate

  # Save output to file
  python validate_predictions.py --predictions train_pred.jsonl --answers answers.jsonl --mode train --output results.json
        """
    )

    parser.add_argument(
        '--questions',
        type=str,
        help='Questions JSONL file (optional, not used in validation)'
    )

    parser.add_argument(
        '--predictions',
        type=str,
        required=True,
        help='Predictions JSONL file (required)'
    )

    parser.add_argument(
        '--answers',
        type=str,
        required=True,
        help='Answer key JSONL file (required)'
    )

    parser.add_argument(
        '--mode',
        type=str,
        required=True,
        choices=['train', 'test', 'validate'],
        help='Validation mode: train|test|validate'
    )

    parser.add_argument(
        '--show-errors',
        action='store_true',
        default=False,
        help='Include error details in output (default: false for validate mode)'
    )

    parser.add_argument(
        '--output',
        type=str,
        help='Output JSON file (optional, prints to stdout if not provided)'
    )

    args = parser.parse_args()

    try:
        # Load input files
        predictions = load_jsonl(args.predictions)
        answers = load_jsonl(args.answers)

        # Validate predictions
        results = validate_predictions(
            predictions=predictions,
            answers=answers,
            mode=args.mode,
            show_errors=args.show_errors
        )

        # Calculate detailed metrics
        metrics = calculate_metrics(results)

        # Merge metrics into results
        final_output = {**results, 'metrics': metrics}

        # Output results
        output_json = json.dumps(final_output, indent=2, ensure_ascii=False)

        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output_json)
            print(f"Validation results written to: {args.output}", file=sys.stderr)
        else:
            print(output_json)

        # Exit with appropriate code
        sys.exit(0 if results['accuracy'] > 0 else 1)

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
