# Person System - Stage 2.1 Analysis Dataset

**Status**: Complete
**Date**: 2025-11-29
**Feature**: person-system
**TBTA Field**: "Person"

## Contents

```
analysis/
├── data/
│   ├── train.jsonl           # 3,068 entries - training dataset
│   ├── validate.jsonl         # 383 entries - validation dataset (no answers)
│   ├── validate.secret.jsonl  # 383 entries - validation with answers
│   ├── test.jsonl             # 385 entries - test dataset (no answers)
│   ├── test.secret.jsonl      # 385 entries - test with answers
│   └── leftovers.jsonl        # 154,692 entries - remaining TBTA data
├── LANGUAGE-SELECTION.md      # Language choices and rationale
├── audit-data.md              # Comprehensive audit report
├── distribution.yaml          # Feature value distribution
└── README.md                  # This file
```

## Dataset Summary

### Extraction (Step 1A)
- **Source**: TBTA Person field annotations
- **Total TBTA entries**: 171,876 annotations across ~12,000 verses
- **Tool**: `src/ingest_data/tbta/extract_feature.py`

### Distribution of Person Values

| Value | Count | Percentage |
|-------|-------|------------|
| Third | 141,890 | 82.5% |
| Second | 16,732 | 9.7% |
| First | 10,207 | 5.9% |
| First Inclusive | 1,386 | 0.8% |
| First Exclusive | 1,272 | 0.7% |
| First as Third | 330 | 0.2% |
| Second as Third | 47 | <0.1% |
| First Exclusive as Third | 12 | <0.1% |

### Balanced Dataset (Step 1B)
- **Tool**: `src/tools/predict/draft_dataset.py`
- **Manual enrichment**: Added `strongs_number` and `reason_group` fields
- **Total selected**: 3,836 entries (balanced by genre, one per verse, sampled by constituent)

### Enrichment (Step 1C)
- **Tool**: `src/ingest_data/tbta/enrich_extract_with_verses.py`
- **Languages requested**: 14 (eng-YLT, grc, hbo, heb-heb, lat-VUC, arb-NAV, tgl, ind, deu-1912, fra-LSG, spa-BES, vie, zho-CUV-SIMP, kor)
- **Translation coverage**: 9.2% (limited by cache availability)

### Final Splits (Step 1E)
- **Train**: 3,068 entries (exceeds target of 800 - manageable)
- **Validate**: 383 entries (exceeds target of 100 - manageable)
- **Test**: 385 entries (exceeds target of 100 - manageable)
- **Leftovers**: 154,692 entries (remaining TBTA data for future use)

## Key Findings

### Label Distribution
Balanced across major person values:
- First: 1,000 entries
- Second: 1,000 entries  
- Third: 1,000 entries
- First Inclusive: 328 entries
- First Exclusive: 306 entries
- Edge cases: 202 entries (First as Third, etc.)

### Reason Group Classification

| Reason Group | Count | Purpose |
|-------------|-------|---------|
| COMMON_NOUN | 1,418 | Generic nouns (person, king, servant) |
| PROPER_NAME | 1,001 | Named individuals (David, Paul, Moses) |
| ROUTINE_SPEECH | 981 | Standard first/second person usage |
| DEITY_REFERENCE | 250 | God, Yahweh, Lord references |
| HUMAN_GROUP | 104 | Groups (Israelites, people) |
| PERSON_AS_THIRD | 76 | Edge cases (semantic vs morphological mismatch) |
| TRINITY | 2 | Trinity references (Gen 1:26, etc.) |
| NARRATIVE_TRAVEL | 2 | Travel companion contexts |
| PRAYER_EXCLUDE_GOD | 2 | Prayers confessing sin |

**Note**: Rare theological cases (TRINITY, PRAYER_EXCLUDE_GOD) are inherently infrequent in Scripture but theologically critical.

### Strong's Number Coverage
- **Valid codes**: 927/3,836 (24.2%)
- **UNKNOWN**: 2,909/3,836 (75.8%)
- **Reason**: Macula Hebrew/Greek source data only available for subset of verses
- **Impact**: Acceptable - strongs_number field present for all entries, UNKNOWN where source data unavailable

## Data Quality

✓ All required fields present
✓ Reason groups assigned to 100% of entries
✓ Strong's numbers extracted where source data available
✓ Balanced representation of person values
✓ Genre-balanced sampling

⚠ Translation enrichment limited by cache availability (9.2%)
⚠ Dataset sizes exceed suggested targets (train=3068 vs 800, but manageable)

## Next Steps (Stage 2.2+)

1. **Stage 2.2**: Develop prediction logic/rules
2. **Stage 2.3**: Test against validation dataset
3. **Stage 2.4**: Iterate based on errors
4. **Stage 2.5**: Final evaluation on test set

## Files Not to Touch

- `test.secret.jsonl` - Reserved for final evaluation
- `validate.secret.jsonl` - Answer key for validation

## Usage

```python
import json

# Load training data
with open('data/train.jsonl', 'r') as f:
    train_data = [json.loads(line) for line in f]

# Each entry contains:
# - verse: e.g., "GEN-001-026"
# - label: e.g., "First Inclusive"
# - constituent: e.g., "us"
# - strongs_number: e.g., "H0430" or "UNKNOWN"
# - dataset.reason_group: e.g., "TRINITY"
# - reconstructed_verse: simplified text with **constituent** marked
```

## References

- **Methodology**: `/workspace/bible-study-tools/tbta/features/.instructions-to-build-feature/STAGE-2-1-ANALYSIS-DATASET.md`
- **Theological Research**: `../research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml`
- **Language Typology**: `../research/LANGUAGES.md`
- **Audit Report**: `./audit-data.md`
