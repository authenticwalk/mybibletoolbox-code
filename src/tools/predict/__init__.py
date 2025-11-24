"""Prediction Tools

Generic reusable tools for TBTA feature prediction and validation.
These tools are feature-agnostic and can be used across all TBTA features.
"""

__version__ = "1.0.0"

from .score_predictions import (
    load_data,
    match_prediction,
    calculate_accuracy,
    score_predictions
)

from .validate_format import (
    validate_prediction_format,
    check_verse_reference,
    ValidationError
)

__all__ = [
    # Scoring tools
    'load_data',
    'match_prediction',
    'calculate_accuracy',
    'score_predictions',
    # Format validation
    'validate_prediction_format',
    'check_verse_reference',
    'ValidationError',
]
