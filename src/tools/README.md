# TBTA Analysis Tools

This directory contains tools for developing and validating TBTA feature predictions. These tools support the 6-stage workflow defined in `/bible-study-tools/tbta/features/STAGES.md`.

## Architecture Overview

### Tool Classification

**LLM-Driven Workflows** (follow STAGES.md):
- Stage 1: Research TBTA Documentation
- Stage 2: Language Study → Uses `discover_languages.py`
- Stage 3: Scholarly Research
- Stage 4: Generate Test Set → Uses `select_reference_values.py`
- Stage 5: Develop Algorithm → Uses `score_tbta_accuracy.py`, `guess_translation_words.py`
- Stage 6: Validate & Peer Review → Uses `validate_predictions.py`

**Standalone Scripts** (mechanical operations):
- Data extraction (ingestion, not prediction)
- Accuracy scoring (deterministic calculation)
- Format validation (structural checking)

See `/plan/tbta/split-stages-rebuild/architecture-reorganization.md` for detailed classification reasoning.

### Recent Architecture Changes

**Removed Tools** (migrated to LLM workflows):
- ~~`select_reference_values.py`~~ → Now part of Stage 4 LLM workflow
- ~~`guess_translation_words.py`~~ → Now part of Stage 5 LLM workflow
- ~~`score_tbta_accuracy.py`~~ → Replaced by generic `predict/score_predictions.py`

**Why?** These tasks require semantic judgment (adversarial case selection, linguistic analysis) that LLMs handle better than scripts. The new architecture separates:
- **Prediction-focused tools** (`/src/tools/predict/`) - Generic helpers
- **Feature-specific work** - LLM-driven in `/plan/tbta-rebuild-with-llm/features/{feature}/`
- **TBTA ingestion** - One-time import in `/src/ingest_data/tbta/`

---

## Current Tools

### extract_tbta_to_jsonl.py

Extract TBTA annotations to JSONL format for analysis and processing.

**Status**: ⚠️ **Ingestion Tool** (not prediction-focused)
**Location**: Should migrate to `/src/ingest_data/tbta/`

### Features

- **Feature-agnostic**: Works with ANY TBTA feature field (Number, Person, Gender, Tense, etc.)
- **Recursive extraction**: Handles nested TBTA tree structures
- **Progress indicators**: Shows progress for large datasets
- **Error handling**: Continues processing on individual file errors
- **Statistics**: Provides label distribution and summary
- **Validation**: Validates input directory and file formats
- **Type hints**: Full type annotations for maintainability

### Usage

```bash
python extract_tbta_to_jsonl.py \
  --source-dir tbta-source/data/ \
  --feature-field Number \
  --output number_data.jsonl
```

### Arguments

- `--source-dir`: Directory containing TBTA JSON files (required)
- `--feature-field`: TBTA field name to extract (e.g., Number, Person, Gender, Tense) (required)
- `--output`: Output JSONL file path (required)
- `--verbose`: Enable verbose logging (optional)

### Input Format

TBTA JSON files with standard structure:
- Filename: `{BOOK}-{chapter:03d}-{verse:03d}.json`
- Content: List of clause elements with nested Children

Example:
```json
[
  {
    "Constituent": "God created",
    "Part": "Clause",
    "Number": "",
    "Children": [
      {
        "Constituent": "God",
        "Part": "Subject",
        "Number": "Singular",
        "Children": []
      }
    ]
  }
]
```

### Output Format

JSONL (JSON Lines) with one annotation per line:

```jsonl
{"verse": "GEN.001.001", "label": "Singular", "constituent": "God", "part": "Subject", "path": "Clause[0]/Predicate[0]"}
{"verse": "GEN.001.001", "label": "Plural", "constituent": "heavens", "part": "Object", "path": "Clause[0]/Predicate[1]"}
```

Fields:
- `verse`: Bible reference in format `BOOK.CCC.VVV`
- `label`: The feature value extracted
- `constituent`: The text constituent being annotated
- `part`: Grammatical part (Predicate, Subject, Object, etc.)
- `path`: Hierarchical path showing location in tree

### Examples

Extract Number features:
```bash
python extract_tbta_to_jsonl.py \
  --source-dir tbta-source/data/ \
  --feature-field Number \
  --output features/number/raw_tbta_data.jsonl
```

Extract Person features with verbose output:
```bash
python extract_tbta_to_jsonl.py \
  --source-dir tbta-source/data/ \
  --feature-field Person \
  --output features/person/raw_tbta_data.jsonl \
  --verbose
```

Extract Gender features:
```bash
python extract_tbta_to_jsonl.py \
  --source-dir tbta-source/data/ \
  --feature-field Gender \
  --output features/gender/raw_tbta_data.jsonl
```

### Error Handling

The tool handles various error conditions gracefully:

- **Invalid JSON**: Logs error and skips file
- **Missing directory**: Exits with clear error message
- **No JSON files**: Exits with helpful message
- **Malformed filenames**: Logs warning and skips file
- **Missing feature fields**: Silently skips (normal for sparse data)

### Output

The tool provides summary statistics:

```
============================================================
EXTRACTION COMPLETE
============================================================
Files processed successfully: 1234/1235
Files with errors: 1
Total annotations extracted: 45678
Output written to: number_data.jsonl

Label distribution:
  Singular: 28456
  Plural: 17222
```

### Testing

Run unit tests:
```bash
python test_extract_tbta_to_jsonl.py -v
```

Test with example data:
```bash
python extract_tbta_to_jsonl.py \
  --source-dir example_data \
  --feature-field Number \
  --output /tmp/test.jsonl \
  --verbose
```

### Implementation Details

**Core Functions:**

- `extract_feature()`: Recursively walks TBTA tree extracting annotations
- `process_file()`: Processes single JSON file and adds verse references
- `validate_source_dir()`: Validates input directory exists and contains JSON
- `main()`: CLI entry point with argparse

**Design Principles:**

- Filters out "Unspecified" and empty values automatically
- Builds hierarchical paths for annotation provenance
- Uses generators where possible for memory efficiency
- Continues on errors to process as much data as possible
- Provides clear progress feedback for long-running operations

### See Also

- `/workspace/plan/tbta/split-stages-rebuild/analysis-workflow.md` - Full analysis workflow
- TBTA source data specification
- Feature-specific analysis scripts

---

## Prediction Tools (/src/tools/predict/)

**New Architecture**: Generic prediction helpers moved to dedicated directory.

See `/src/tools/predict/README.md` for:
- `score_predictions.py` - Generic accuracy scoring (replaces `score_tbta_accuracy.py`)
- `validate_format.py` - Prediction file format validation
- Usage examples and integration patterns

### Migration Benefits

**Before** (feature-specific scripts):
- `score_tbta_accuracy.py` - Hardcoded TBTA-specific logic
- `guess_translation_words.py` - Required linguistic rules database
- `select_reference_values.py` - Mixed LLM workflow with scripting

**After** (generic tools):
- `predict/score_predictions.py` - Works for ANY TBTA feature
- `predict/validate_format.py` - Generic format validation
- LLM workflows handle semantic judgment (STAGES.md Stage 4-5)

**Why?** Separates deterministic operations (scripts) from semantic judgment (LLM). The new architecture is:
- **More reusable**: One script serves all features
- **More maintainable**: Clear separation of concerns
- **More flexible**: LLMs handle context-dependent tasks better

---

## discover_languages.py

Discover available language translations for Bible verses using eBible corpus and quote-bible skill.

### Purpose

Identifies which languages have translations available for testing:
1. Queries eBible corpus for verse availability
2. Uses quote-bible skill for comprehensive language coverage
3. Generates language list with metadata for downstream analysis

### Input

Uses Bible verse references to query available translations. No input file required.

### Output Format

**available_languages.jsonl** - Languages with translation coverage:
```jsonl
{"lang": "eng", "name": "English", "count": 31102}
{"lang": "tgl", "name": "Tagalog", "count": 7957}
{"lang": "fij", "name": "Fijian", "count": 27789}
```

Fields:
- `lang`: ISO-639-3 language code
- `name`: Language name
- `count`: Number of verses available

### Usage

```bash
python3 src/tools/discover_languages.py \
  --output features/number-systems/analysis/available_languages.jsonl \
  --sample-verses GEN.001.001 JHN.003.016 MAT.005.001 \
  --verbose
```

### Arguments

- `--output`: Path to output JSONL file (required)
- `--sample-verses`: Sample verses to test (default: popular verses across OT/NT)
- `--min-coverage`: Minimum verse count to include language (default: 1000)
- `--verbose`: Show discovery progress (optional)

### Discovery Process

1. **Sample verse selection**: Uses diverse verses (Genesis, John, Matthew, etc.)
2. **Language querying**: Queries each sample verse for available translations
3. **Coverage calculation**: Counts verses per language across corpus
4. **Filtering**: Removes languages below minimum coverage threshold
5. **Metadata enrichment**: Adds language names and statistics

### Data Sources

- **eBible corpus**: Primary source for verse translations
- **quote-bible skill**: Fallback for additional language coverage
- **ISO-639-3 codes**: Standard language identification

### Example Output

```
Discovering languages from eBible corpus...
Testing sample verses: GEN.001.001, JHN.003.016, MAT.005.001

Found languages:
  eng (English): 31,102 verses
  spa (Spanish): 28,437 verses
  fra (French): 27,891 verses
  tgl (Tagalog): 7,957 verses
  fij (Fijian): 27,789 verses
  ...

Filtered to 50 languages with ≥1000 verses

✓ Wrote 50 languages to available_languages.jsonl
```

### Integration

The language list is used by `guess_translation_words.py` to determine which languages to generate predictions for.

### See Also

- `/plan/tbta/split-stages-rebuild/analysis-workflow.md` - Full analysis workflow
- `guess_translation_words.py` - Uses language list for predictions
- `src/ingest_data/ebible/` - eBible corpus integration

---

## validate_predictions.py

Validate TBTA feature predictions and calculate accuracy metrics.

### Purpose

Final validation step that:
1. Compares TBTA predictions against actual Bible translations
2. Calculates precision, recall, and F1 scores
3. Generates comprehensive accuracy reports
4. Identifies error patterns for improvement

### Input Format

**raw_results.jsonl** - From `score_tbta_accuracy.py`:
```jsonl
{"verse": "GEN.001.026", "label": "trial", "lang": "tgl", "verse_text": "...", "tbta_matches": ["tayo"], "wrong_matches": []}
{"verse": "JHN.003.016", "label": "singular", "lang": "eng", "verse_text": "...", "tbta_matches": ["God"], "wrong_matches": []}
```

### Output Formats

**validation_report.yaml** - Comprehensive metrics:
```yaml
overall:
  accuracy: 0.874
  precision: 0.891
  recall: 0.867
  f1_score: 0.879
  total_predictions: 522
  correct: 456
  false_positives: 28
  false_negatives: 38

by_label:
  trial:
    accuracy: 0.92
    precision: 0.95
    recall: 0.89
    count: 45
  dual:
    accuracy: 0.85
    precision: 0.88
    recall: 0.82
    count: 67

by_language:
  tgl:
    accuracy: 0.92
    count: 50
  eng:
    accuracy: 0.85
    count: 141

error_analysis:
  common_errors:
    - pattern: "collective nouns misclassified"
      count: 15
      examples: ["GEN.001.026", "GEN.011.004"]
```

**error_cases.jsonl** - Detailed error analysis:
```jsonl
{"verse": "GEN.001.026", "label": "trial", "lang": "tgl", "error_type": "false_negative", "expected": ["tayo"], "found": []}
```

### Usage

```bash
python3 src/tools/validate_predictions.py \
  --raw-results features/number-systems/analysis/raw_results.jsonl \
  --validation-report features/number-systems/analysis/validation_report.yaml \
  --error-cases features/number-systems/analysis/error_cases.jsonl \
  --verbose
```

### Arguments

- `--raw-results`: Path to raw results JSONL (required)
- `--validation-report`: Path to output validation report YAML (required)
- `--error-cases`: Path to output error cases JSONL (optional)
- `--min-confidence`: Minimum confidence threshold (default: 0.0)
- `--verbose`: Show detailed validation progress (optional)

### Validation Metrics

**Accuracy**: (TP + TN) / Total
- Measures overall correctness

**Precision**: TP / (TP + FP)
- Measures reliability of positive predictions
- High precision = few false alarms

**Recall**: TP / (TP + FN)
- Measures coverage of actual positives
- High recall = few missed cases

**F1 Score**: 2 × (Precision × Recall) / (Precision + Recall)
- Harmonic mean balancing precision and recall

### Error Classification

- **False Positive**: TBTA predicted word appears, but shouldn't
- **False Negative**: Expected word missing from translation
- **True Positive**: TBTA prediction confirmed in translation
- **True Negative**: Correct absence of word

### Example Output

```
Loading raw results from raw_results.jsonl...
Loaded 522 predictions

Validating predictions...
[522/522] Processing... ✓

============================================================
VALIDATION REPORT
============================================================
Overall Metrics:
  Accuracy: 87.40%
  Precision: 89.10%
  Recall: 86.70%
  F1 Score: 87.90%

Predictions: 522 total (456 correct, 66 errors)
  False Positives: 28
  False Negatives: 38

By Label:
  trial: 92.00% accuracy (45 cases)
  dual: 85.00% accuracy (67 cases)
  quadrial: 78.00% accuracy (23 cases)

By Language:
  tgl: 92.00% (50 cases)
  eng: 85.00% (141 cases)
  fra: 88.50% (90 cases)

Error Analysis:
  15 cases: collective nouns misclassified
  8 cases: ambiguous pronoun reference
  5 cases: poetic/archaic language forms

✓ Validation report saved to validation_report.yaml
✓ Error cases saved to error_cases.jsonl
```

### Integration with Workflow

This is the final validation step in the TBTA analysis pipeline:
1. `extract_tbta_to_jsonl.py` → Extract TBTA annotations
2. `select_reference_values.py` → Select test cases
3. `discover_languages.py` → Find available translations
4. `guess_translation_words.py` → Generate predictions
5. `score_tbta_accuracy.py` → Score against translations
6. **`validate_predictions.py`** → Final validation and metrics

### See Also

- `/plan/tbta/split-stages-rebuild/analysis-workflow.md` - Full analysis workflow
- `score_tbta_accuracy.py` - Generates raw results input
- REVIEW-GUIDELINES.md - Validation standards and thresholds
