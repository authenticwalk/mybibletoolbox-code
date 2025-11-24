"""Shared pytest fixtures for TBTA tools tests."""

import json
import pytest
from pathlib import Path
from typing import Dict, List, Any


@pytest.fixture
def tmp_data_dir(tmp_path):
    """Create temporary data directory structure."""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    return data_dir


@pytest.fixture
def sample_tbta_json() -> List[Dict[str, Any]]:
    """Sample TBTA JSON structure with multiple features."""
    return [
        {
            "Part": "Clause",
            "Constituent": "God created the heavens",
            "Number": "S",
            "Person": "3",
            "Gender": "M",
            "Tense": "Past",
            "Children": [
                {
                    "Part": "Subject",
                    "Constituent": "God",
                    "Number": "S",
                    "Person": "3",
                    "Gender": "M",
                    "Children": []
                },
                {
                    "Part": "Predicate",
                    "Constituent": "created",
                    "Tense": "Past",
                    "Children": []
                },
                {
                    "Part": "Object",
                    "Constituent": "the heavens",
                    "Number": "P",
                    "Children": []
                }
            ]
        },
        {
            "Part": "Clause",
            "Constituent": "and the earth",
            "Number": "S",
            "Children": [
                {
                    "Part": "Object",
                    "Constituent": "the earth",
                    "Number": "S",
                    "Children": []
                }
            ]
        }
    ]


@pytest.fixture
def sample_tbta_json_with_unspecified() -> List[Dict[str, Any]]:
    """Sample TBTA JSON with 'Unspecified' values."""
    return [
        {
            "Part": "Clause",
            "Constituent": "In the beginning",
            "Number": "Unspecified",
            "Person": "Unspecified",
            "Children": []
        }
    ]


@pytest.fixture
def sample_tbta_file(tmp_data_dir, sample_tbta_json):
    """Create a sample TBTA JSON file."""
    file_path = tmp_data_dir / "GEN-001-001.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(sample_tbta_json, f, ensure_ascii=False, indent=2)
    return file_path


@pytest.fixture
def sample_tbta_files(tmp_data_dir, sample_tbta_json):
    """Create multiple sample TBTA JSON files."""
    files = []
    for book, chapter, verse in [("GEN", 1, 1), ("GEN", 1, 2), ("MAT", 1, 1)]:
        file_path = tmp_data_dir / f"{book}-{chapter:03d}-{verse:03d}.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(sample_tbta_json, f, ensure_ascii=False, indent=2)
        files.append(file_path)
    return files


@pytest.fixture
def sample_predictions() -> List[Dict[str, Any]]:
    """Sample prediction data."""
    return [
        {
            "verse": "GEN.001.001",
            "predicted_value": "S",
            "confidence": "high"
        },
        {
            "verse": "GEN.001.002",
            "predicted_value": "P",
            "confidence": "medium"
        },
        {
            "verse": "MAT.001.001",
            "predicted_value": "S",
            "confidence": "low"
        }
    ]


@pytest.fixture
def sample_answers() -> List[Dict[str, Any]]:
    """Sample answer key data."""
    return [
        {
            "verse": "GEN.001.001",
            "tbta_value": "S",
            "genre": "narrative"
        },
        {
            "verse": "GEN.001.002",
            "tbta_value": "S",  # Intentionally different from prediction
            "genre": "narrative"
        },
        {
            "verse": "MAT.001.001",
            "tbta_value": "S",
            "genre": "genealogy"
        }
    ]


@pytest.fixture
def sample_predictions_file(tmp_data_dir, sample_predictions):
    """Create a sample predictions JSONL file."""
    file_path = tmp_data_dir / "predictions.jsonl"
    with open(file_path, 'w', encoding='utf-8') as f:
        for record in sample_predictions:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')
    return file_path


@pytest.fixture
def sample_answers_file(tmp_data_dir, sample_answers):
    """Create a sample answers JSONL file."""
    file_path = tmp_data_dir / "answers.jsonl"
    with open(file_path, 'w', encoding='utf-8') as f:
        for record in sample_answers:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')
    return file_path


@pytest.fixture
def sample_questions() -> List[Dict[str, Any]]:
    """Sample question data."""
    return [
        {
            "verse": "GEN.001.001",
            "question": "What is the grammatical number?",
            "context": "Genesis 1:1"
        },
        {
            "verse": "GEN.001.002",
            "question": "What is the grammatical number?",
            "context": "Genesis 1:2"
        }
    ]


@pytest.fixture
def sample_jsonl_file(tmp_data_dir):
    """Create a sample JSONL file with test data."""
    file_path = tmp_data_dir / "test.jsonl"
    data = [
        {"verse": "GEN.001.001", "label": "S", "constituent": "God"},
        {"verse": "GEN.001.002", "label": "P", "constituent": "heavens"}
    ]
    with open(file_path, 'w', encoding='utf-8') as f:
        for record in data:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')
    return file_path


@pytest.fixture
def sample_translation_results() -> Dict[str, str]:
    """Sample translation results from Quote Bible."""
    return {
        "eng-NIV": "For God so loved the world...",
        "eng-KJV": "For God so loved the world...",
        "spa-RV": "Porque de tal manera amó Dios al mundo...",
        "spa-RV-1960": "Porque de tal manera amó Dios al mundo...",
        "fra-LSG": "Car Dieu a tant aimé le monde..."
    }


@pytest.fixture
def malformed_json_file(tmp_data_dir):
    """Create a file with malformed JSON."""
    file_path = tmp_data_dir / "malformed.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('{"invalid": json syntax}')
    return file_path


@pytest.fixture
def empty_jsonl_file(tmp_data_dir):
    """Create an empty JSONL file."""
    file_path = tmp_data_dir / "empty.jsonl"
    file_path.touch()
    return file_path


@pytest.fixture
def invalid_filename_file(tmp_data_dir, sample_tbta_json):
    """Create a TBTA file with invalid filename format."""
    file_path = tmp_data_dir / "invalid_name.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(sample_tbta_json, f)
    return file_path


# ============================================================================
# Fixtures for select_reference_values.py tests
# ============================================================================

@pytest.fixture
def sample_feature_config() -> Dict[str, Any]:
    """Sample feature configuration with non-arbitrary contexts."""
    return {
        'feature_name': 'Number Systems',
        'tbta_field': 'Number',
        'values': ['singular', 'dual', 'trial', 'plural'],
        'non_arbitrary_contexts': [
            {
                'pattern': 'Trinity reference (plural of majesty)',
                'examples': ['GEN.001.026', 'GEN.011.007'],
                'preferred_value': 'trial',
                'theological_significance': 'Trinity'
            },
            {
                'pattern': 'Divine speech (cohortative)',
                'examples': ['GEN.001.026'],
                'preferred_value': 'plural',
                'theological_significance': 'divine speech'
            }
        ],
        'value_statistics': {
            'singular': 5000,
            'dual': 50,
            'trial': 30,
            'plural': 1000
        }
    }


@pytest.fixture
def sample_feature_config_file(tmp_data_dir, sample_feature_config):
    """Create a sample feature config JSON file."""
    file_path = tmp_data_dir / "feature_config.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(sample_feature_config, f, ensure_ascii=False, indent=2)
    return file_path


@pytest.fixture
def sample_reference_data() -> List[Dict[str, Any]]:
    """Sample reference data for select_reference_values tests."""
    return [
        {
            'verse': 'GEN.001.001',
            'label': 'singular',
            'constituent': 'God',
            'part': 'Noun',
            'path': 'clause > subject'
        },
        {
            'verse': 'GEN.001.026',
            'label': 'trial',
            'constituent': 'us',
            'part': 'Pronoun',
            'path': 'clause > object > said'
        },
        {
            'verse': 'GEN.002.001',
            'label': 'dual',
            'constituent': 'two',
            'part': 'Noun',
            'path': 'clause'
        },
        {
            'verse': 'GEN.025.010',
            'label': 'plural',
            'constituent': 'they',
            'part': 'Pronoun',
            'path': 'clause > subject'
        },
        {
            'verse': 'GEN.050.001',
            'label': 'singular',
            'constituent': 'he',
            'part': 'Pronoun',
            'path': 'clause'
        }
    ]


@pytest.fixture
def sample_reference_data_balanced() -> List[Dict[str, Any]]:
    """Balanced sample data across all values."""
    data = []
    values = ['singular', 'dual', 'trial', 'plural']
    for i, value in enumerate(values):
        for j in range(10):
            data.append({
                'verse': f'GEN.{i+1:03d}.{j+1:03d}',
                'label': value,
                'constituent': f'word_{i}_{j}',
                'part': 'Noun',
                'path': 'clause'
            })
    return data


# ============================================================================
# Fixtures for guess_translation_words.py tests
# ============================================================================

@pytest.fixture
def sample_linguistic_rules() -> Dict[str, Dict[str, List[str]]]:
    """Sample linguistic rules for multiple languages."""
    return {
        'tgl': {  # Tagalog
            'dual': ['dalawa'],
            'trial': ['tatlo', 'tayo'],
            'plural': ['mga', 'natin'],
            'inclusive': ['tayo', 'natin'],
            'exclusive': ['kami', 'namin'],
            'singular': ['ako', 'siya']
        },
        'fij': {  # Fijian
            'dual': ['rua'],
            'trial': ['tolu', 'kedatou'],
            'plural': ['ira'],
            'singular': ['dua']
        },
        'haw': {  # Hawaiian
            'dual': ['lua'],
            'trial': ['kolu'],
            'plural': ['mau'],
            'singular': ['kahi']
        }
    }


@pytest.fixture
def sample_references_file(tmp_data_dir) -> Path:
    """Create sample reference_values.jsonl file."""
    file_path = tmp_data_dir / "reference_values.jsonl"
    references = [
        {
            'verse': 'GEN.001.026',
            'label': 'trial',
            'constituent': 'us',
            'category': 'non-arbitrary',
            'reason': 'Trinity reference',
            'strongs': 'H0000',
            'strongs_word': None,
            'part': 'Pronoun',
            'path': 'clause > object'
        },
        {
            'verse': 'GEN.001.001',
            'label': 'singular',
            'constituent': 'God',
            'category': 'adversarial',
            'reason': 'genre boundary',
            'strongs': 'H0430',
            'strongs_word': 'elohim',
            'part': 'Noun',
            'path': 'clause > subject'
        },
        {
            'verse': 'GEN.002.001',
            'label': 'dual',
            'constituent': 'two',
            'category': 'arbitrary',
            'reason': 'balanced sampling',
            'strongs': None,
            'strongs_word': None,
            'part': 'Noun',
            'path': 'clause'
        }
    ]
    with open(file_path, 'w', encoding='utf-8') as f:
        for ref in references:
            f.write(json.dumps(ref, ensure_ascii=False) + '\n')
    return file_path


@pytest.fixture
def sample_languages_file(tmp_data_dir) -> Path:
    """Create sample available_languages.jsonl file."""
    file_path = tmp_data_dir / "available_languages.jsonl"
    languages = [
        {'lang': 'tgl', 'version': 'ABTAG', 'name': 'Tagalog'},
        {'lang': 'fij', 'version': 'FIJBIB', 'name': 'Fijian'},
        {'lang': 'haw', 'version': 'HWC', 'name': 'Hawaiian'},
        {'lang': 'eng', 'version': 'NIV', 'name': 'English'},
        {'lang': 'spa', 'version': 'RV', 'name': 'Spanish'}
    ]
    with open(file_path, 'w', encoding='utf-8') as f:
        for lang in languages:
            f.write(json.dumps(lang, ensure_ascii=False) + '\n')
    return file_path
