# Prediction Tools

Generic reusable tools for TBTA feature prediction and validation. These tools are feature-agnostic and can be used across all TBTA features.

## Tools

### 1. `score_predictions.py`

Compare predictions against ground truth and calculate accuracy metrics.

**Usage:**
```bash
python src/tools/predict/score_predictions.py \
  --predictions test_predictions.yaml \
  --ground-truth test.yaml \
  --output scoring_report.yaml
```

**Input formats:** YAML, JSON, or JSONL (auto-detected)

**Prediction file format:**
```yaml
- verse: "GEN.001.026"
  predicted_value: "inclusive"
  confidence: "high"
- verse: "GEN.011.007"
  predicted_value: "trial"
  confidence: "medium"
```

**Ground truth file format:**
```yaml
- verse: "GEN.001.026"
  actual_value: "inclusive"
  genre: "narrative"
- verse: "GEN.011.007"
  actual_value: "trial"
  genre: "narrative"
```

**Output report:**
```yaml
overall:
  accuracy: 0.95
  percentage: 95.0
  correct: 142
  total: 150
by_confidence:
  high:
    accuracy: 0.98
    correct: 98
    total: 100
  medium:
    accuracy: 0.88
    correct: 44
    total: 50
by_genre:
  narrative:
    accuracy: 0.96
    correct: 96
    total: 100
errors:
  - verse: "MAT.028.019"
    predicted: "exclusive"
    actual: "inclusive"
    confidence: "medium"
    genre: "narrative"
```

**Matcher configuration** (optional):
```json
{
  "normalize": true,
  "fuzzy_match": false,
  "ignore_case": true
}
```

### 2. `validate_format.py`

Validate prediction file format and structure.

**Usage:**
```bash
python src/tools/predict/validate_format.py \
  --predictions test_pred.jsonl \
  --answers answers.jsonl \
  --mode test \
  --show-errors
```

**Validation modes:**
- `train` - Validation for training set
- `test` - Validation for test set (show errors)
- `validate` - Validation for final validation (hide errors by default)

**Features:**
- Check required fields (`verse`, `predicted_value`)
- Validate verse references (USFM format)
- Check value enumerations
- Detect duplicate verses
- Compare against answer key

## Integration with LLM Workflows

These tools are designed to be called by LLM agents during TBTA feature development (STAGES.md):

**Stage 5: Develop Algorithm**
```bash
# LLM generates predictions, then scores them
python src/tools/predict/score_predictions.py \
  --predictions features/clusivity/experiments/test_predictions.yaml \
  --ground-truth features/clusivity/data/test.yaml \
  --output features/clusivity/experiments/scoring_report.yaml
```

**Stage 6: Validate & Peer Review**
```bash
# Validate format before submission
python src/tools/predict/validate_format.py \
  --predictions final_predictions.jsonl \
  --answers validation_set.jsonl \
  --mode validate
```

## Python API

```python
from tools.predict import score_predictions, load_data

# Load data
predictions = load_data('predictions.yaml')
ground_truth = load_data('ground_truth.yaml')

# Score predictions
report = score_predictions(predictions, ground_truth)

print(f"Accuracy: {report['overall']['percentage']:.2f}%")
print(f"Errors: {len(report['errors'])}")
```

## Design Principles

1. **Feature-agnostic** - Works for any TBTA feature (clusivity, degree, discourse-genre, etc.)
2. **Multiple formats** - Supports YAML, JSON, JSONL
3. **Flexible matching** - Configurable normalization and matching rules
4. **Clear output** - Human-readable reports with detailed error analysis
5. **CLI + API** - Can be used from command line or imported as library
