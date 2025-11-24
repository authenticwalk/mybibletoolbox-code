"""TBTA Analysis Tools

Reusable tools for TBTA feature development and validation.
"""

__version__ = "1.0.0"

# Verse fetching
from .fetch_verse import fetch_verse as fetch_verse_tool
from .fetch_verse import filter_by_languages, VerseFetchError

# Prediction tools
try:
    from .predict import (
        load_data,
        match_prediction,
        calculate_accuracy,
        score_predictions,
        validate_prediction_format,
        check_verse_reference,
        ValidationError
    )

    __all__ = [
        # Fetch verse tool
        'fetch_verse_tool',
        'filter_by_languages',
        'VerseFetchError',
        # Prediction tools
        'load_data',
        'match_prediction',
        'calculate_accuracy',
        'score_predictions',
        'validate_prediction_format',
        'check_verse_reference',
        'ValidationError',
    ]
except ImportError as e:
    # Minimal exports if prediction tools have missing dependencies
    __all__ = [
        'fetch_verse_tool',
        'filter_by_languages',
        'VerseFetchError',
    ]
