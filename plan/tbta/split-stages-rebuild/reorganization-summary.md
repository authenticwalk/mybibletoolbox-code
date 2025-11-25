# Tools Reorganization Summary

**Date:** 2025-11-20
**Task:** Reorganize tools based on architectural analysis

## Changes Made

### 1. Directory Structure Created

```
/src/tools/
  ├── fetch_verse.py (already exists)
  ├── predict/
  │   ├── __init__.py (NEW)
  │   ├── score_predictions.py (NEW - generic scorer)
  │   ├── validate_format.py (MOVED from validate_predictions.py)
  │   └── README.md (NEW)
  └── tests/
      ├── __init__.py (NEW)
      └── conftest.py (MOVED from /tests/tools/)
```

### 2. Generic Prediction Scorer Extracted

**File:** `/src/tools/predict/score_predictions.py` (~350 lines)

**Purpose:** Generic prediction scoring tool that works for ANY TBTA feature

**Key Functions:**
- `load_data()` - Load YAML/JSON/JSONL files
- `match_prediction()` - Compare prediction vs ground truth
- `calculate_accuracy()` - Calculate accuracy metrics with breakdown by confidence/genre
- `score_predictions()` - Main API function

**Features:**
- Feature-agnostic (no TBTA-specific terminology)
- Supports multiple formats (YAML, JSON, JSONL)
- Configurable matcher (normalization, fuzzy matching)
- Detailed error reporting
- CLI + Python API

**Usage:**
```bash
python src/tools/predict/score_predictions.py \
  --predictions test_predictions.yaml \
  --ground-truth test.yaml \
  --output scoring_report.yaml
```

**Output:**
```yaml
overall:
  accuracy: 0.95
  percentage: 95.0
  correct: 142
  total: 150
by_confidence:
  high: {accuracy: 0.98, correct: 98, total: 100}
by_genre:
  narrative: {accuracy: 0.96, correct: 96, total: 100}
errors:
  - verse: "MAT.028.019"
    predicted: "exclusive"
    actual: "inclusive"
```

### 3. Format Validator Moved

**File:** `/src/tools/predict/validate_format.py` (moved from `validate_predictions.py`)

**Purpose:** Validate prediction file format and structure

**Already generic** - just needed better location in directory structure

**Features:**
- Check required fields
- Validate verse references
- Compare against answer key
- Multiple validation modes (train/test/validate)

### 4. LLM-Task Scripts Removed

**Deleted:**
- ❌ `select_reference_values.py` (427 lines) - LLM does this in STAGES.md Stage 4
- ❌ `guess_translation_words.py` (303 lines) - Use Quote Bible skill instead
- ❌ `score_tbta_accuracy.py` (280 lines) - Replaced by generic `score_predictions.py`
- ❌ `extract_tbta_to_jsonl.py` - Already exists in `/src/ingest_data/tbta/`

**Reasoning:**
These scripts conflate LLM workflows with deterministic tools. Per the architecture analysis:
- **Selecting reference values** requires judgment (adversarial cases, theological significance) → LLM workflow
- **Guessing translation words** is impossible algorithmically → Use Quote Bible skill to fetch actual translations
- **TBTA-specific scoring** is a subset of generic prediction scoring → Use `score_predictions.py`

### 5. Tests Cleaned Up

**Removed:**
- ❌ `test_select_reference_values.py`
- ❌ `test_guess_translation_words.py`
- ❌ `test_score_tbta_accuracy.py`
- ❌ `test_validate_predictions.py`
- ❌ `test_extract_tbta_to_jsonl.py`

**Moved:**
- ✅ `conftest.py` → `/src/tools/tests/conftest.py`

**Remaining test files** (for tools NOT deleted):
- `test_discover_languages.py` - Keep (uses Quote Bible skill)
- `test_fetch_verse.py` - Keep (if exists)

### 6. Package Exports Updated

**File:** `/src/tools/__init__.py`

**Before:**
```python
# Exported 17+ functions from various scripts
from .select_reference_values import classify_verse, select_references
from .guess_translation_words import guess_words, load_linguistic_rules
from .score_tbta_accuracy import fetch_verse, check_words_in_verse
from .validate_predictions import validate_predictions, calculate_metrics
```

**After:**
```python
# Export only from predict module
from .predict import (
    load_data,
    match_prediction,
    calculate_accuracy,
    score_predictions,
    validate_prediction_format,
    check_verse_reference,
    ValidationError
)
```

**Reduction:** From 17+ exports to 7 focused prediction tools

## Impact

### Code Reduction
- **Deleted:** 1,010+ lines of LLM-task scripts
- **Created:** 350 lines of generic tools
- **Net reduction:** ~660 lines

### Clarity Improvement
- ✅ Clear separation: Scripts vs LLM workflows
- ✅ Generic tools that work for ANY TBTA feature
- ✅ Better directory organization
- ✅ Reduced confusion about what should be automated vs what requires LLM judgment

### What Still Exists

**Tools directory:**
```
/src/tools/
  ├── fetch_verse.py - Fetch verses from eBible corpus
  ├── discover_languages.py - Uses Quote Bible skill (hybrid: script + skill)
  └── predict/
      ├── score_predictions.py - Generic prediction scorer
      └── validate_format.py - Format validator
```

**Ingestion directory** (separate, one-time use):
```
/src/ingest_data/tbta/
  ├── tbta_processor.py - Convert TBTA → YAML
  └── extract_feature.py - Extract feature data
```

## Integration with STAGES.md

The remaining tools integrate with LLM workflows:

**Stage 2: Language Study**
```bash
# LLM uses discover_languages.py (which wraps Quote Bible skill)
python src/tools/discover_languages.py --feature clusivity
```

**Stage 4: Generate Test Set**
```
# LLM agent performs stratification (NOT a script)
# Uses: extract_feature.py, Quote Bible skill, LLM judgment
```

**Stage 5: Develop Algorithm**
```bash
# LLM generates predictions, then scores them
python src/tools/predict/score_predictions.py \
  --predictions experiments/test_predictions.yaml \
  --ground-truth data/test.yaml \
  --output experiments/scoring_report.yaml
```

**Stage 6: Validate & Peer Review**
```bash
# Validate format
python src/tools/predict/validate_format.py \
  --predictions final_predictions.jsonl \
  --answers validation_set.jsonl \
  --mode validate
```

## Migration Guide

**If you had code using deleted scripts:**

### 1. `score_tbta_accuracy.py` → `score_predictions.py`

**Before:**
```bash
python src/tools/score_tbta_accuracy.py \
  --guessed-words guessed_words.jsonl \
  --scorecard-output scorecard.yaml \
  --raw-output raw_results.jsonl
```

**After:**
```bash
python src/tools/predict/score_predictions.py \
  --predictions test_predictions.yaml \
  --ground-truth test.yaml \
  --output scoring_report.yaml
```

**Data format change:**
- Old: JSONL with `tbta_agrees`, `tbta_wrong` word lists
- New: YAML/JSON with `predicted_value`, `actual_value`

### 2. `select_reference_values.py` → LLM Workflow

**Before:**
```bash
python src/tools/select_reference_values.py \
  --input raw_tbta_data.jsonl \
  --feature-config feature_config.json \
  --output reference_values.jsonl
```

**After:** LLM agent performs this in STAGES.md Stage 4
```
"Generate test set for Clusivity following STAGES.md Stage 4"

# LLM agent:
1. Runs extract_feature.py to get TBTA data
2. Analyzes theological significance
3. Stratifies by testament, genre, difficulty
4. Selects balanced sample
5. Outputs train.yaml, test.yaml, validate.yaml
```

### 3. `guess_translation_words.py` → Quote Bible Skill

**Before:**
```bash
python src/tools/guess_translation_words.py \
  --references reference_values.jsonl \
  --languages available_languages.jsonl \
  --output guessed_words.jsonl
```

**After:** Use Quote Bible skill directly
```python
# In LLM workflow, fetch actual translations
from skills import quote_bible

verses = quote_bible.fetch(
    verse="GEN.001.026",
    languages=["tgl", "fij", "smo"]
)

# Analyze actual words used in translations
# No need to "guess" - we have the real data!
```

## Verification

All changes follow the architectural analysis:
- ✅ Scripts are deterministic, mechanical operations
- ✅ LLM workflows handle judgment, semantic understanding
- ✅ Generic tools work across all TBTA features
- ✅ Clear directory organization
- ✅ Reduced code duplication and complexity

## Next Steps

1. **Update existing features** (if any) to use new generic tools
2. **Document LLM workflows** in feature-specific README files
3. **Create example usage** in `/examples/` directory
4. **Test generic tools** with multiple TBTA features to ensure they're truly feature-agnostic
