# Degree Feature - Stage 2.1 Analysis & Dataset

**Status:** COMPLETE
**Date Completed:** 2025-11-29
**Total Dataset Size:** 2,354 entries (from 30,879 TBTA annotations)

## Overview

This directory contains the dataset and analysis for the **Degree** feature (Stage 2.1: Analysis & Hypothesis Validation). The dataset has been extracted from TBTA annotations, balanced by genre, enriched with 10 translations, and split into train/validate/test sets.

## Directory Structure

```
analysis/
├── data/
│   ├── train.jsonl           # 1,883 entries (80%) - Training data
│   ├── validate.jsonl         # 235 entries (10%) - Validation without labels
│   ├── validate.secret.jsonl  # 235 entries (10%) - Validation with labels (DO NOT TOUCH)
│   ├── test.jsonl             # 236 entries (10%) - Test without labels (LOCKED)
│   ├── test.secret.jsonl      # 236 entries (10%) - Test with labels (DO NOT TOUCH UNTIL FINAL EVAL)
│   └── leftovers.jsonl        # 27,446 entries - Remaining TBTA data not in train/validate/test
├── distribution.yaml          # Feature value distribution from full extraction
├── LANGUAGE-SELECTION.md      # Documentation of translation selection rationale
├── audit-data.md              # Data quality audit report
├── enriched.secret.jsonl      # Full enriched dataset (archived)
└── tbta-extract.secret.jsonl  # Full TBTA extraction (archived)
```

## Dataset Composition

### Feature Value Distribution (Train Set)

| Value | Count | Percentage |
|-------|-------|------------|
| No Degree | ~1,500 | 80% |
| Intensified | ~160 | 8.5% |
| Comparative | ~90 | 4.8% |
| Superlative | ~70 | 3.7% |
| Extremely Intensified | ~43 | 2.3% |
| 'too' | ~16 | 0.8% |
| Others | ~4 | <0.2% |

### Reason Group Coverage

20 semantic reason groups including:
- **INTENSIFIED-GENERAL** (608 entries, 25.8%)
- **OTHER-QUALITY** (387 entries, 16.4%)
- **COMPARISON-DEGREE** (228 entries, 9.7%)
- **SUPERLATIVE-DEGREE** (183 entries, 7.8%)
- **EXTREME-INTENSIFICATION** (179 entries, 7.6%)
- **MORAL-QUALITY** (148 entries, 6.3%)
- Plus 14 more specialized groups

### Translation Coverage

**10 languages across major families:**

#### Core Languages (Required)
- `eng-YLT` - English (Young's Literal Translation)
- `grc` - Greek (LXX for OT, Byzantine/SR for NT)
- `hbo` - Hebrew (Westminster Leningrad Codex, OT only)
- `heb-heb` - Modern Hebrew
- `lat-VUC` - Latin (Vulgate Clementine)
- `arb-NAV` - Arabic (Van Dyke)

#### Additional Languages (For Pattern Discovery)
- `deu-1912` - German (Luther 1912)
- `fra-LSG` - French (Louis Segond)
- `spa-BES` - Spanish (Reina Valera)
- `rus-SYN` - Russian (Synodal)

## Data Fields

Each entry in the dataset contains:

```jsonl
{
  "verse": "GEN-001-002",                    # Verse reference
  "label": "Intensified",                     # TBTA degree annotation
  "constituent": "formless",                  # Target word/phrase
  "part": "Adjective",                        # Part of speech
  "path": "Clause[0]/Clause[2]/AdjP[0]",     # Syntax tree path
  "text": "earth be **formless** and empty",  # Reconstructed text with highlight
  "strongs": "H2050b H1886a H0776...",       # Strong's codes for verse
  "strongs_number": "H8414",                  # Strong's code for constituent (heuristic)
  "reconstructed_verse": "earth be formless...", # Simplified NIV-like text
  "genre": "History",                         # Literary genre
  "dataset": {
    "split": "train",                         # Split assignment
    "section": "OT",                          # Testament
    "literary_type": "history",               # Literary type
    "reason_group": "INTENSIFIED-AGE",       # Semantic grouping
    "difficulty": "tricky"                    # Optional: tricky/adversarial
  },
  "translations": {                           # 10 translations
    "eng-YLT": "...",
    "grc-BRENT": "...",
    "hbo-hbo": "...",
    ...
  }
}
```

## Known Limitations

1. **strongs_number accuracy:** Generated heuristically, needs manual review for production use
2. **Translation gaps:** Expected OT/NT split (Hebrew missing from NT, Greek missing from OT)
3. **Imbalanced reason_groups:** Reflects natural distribution in biblical text
4. **14 entries missing data:** Source files not available in dataset

See [audit-data.md](audit-data.md) for complete audit report.

## Next Steps (Stage 2.2)

1. **Translation Discovery Analysis** - Analyze how translators handled each degree value
2. **Pattern Identification** - Discover common strategies across languages
3. **Algorithm Development** - Build prediction logic based on discovered patterns
4. **Validation** - Test against validate set (blind evaluation)

## Usage Notes

- **DO NOT LOOK AT** `test.secret.jsonl` or `validate.secret.jsonl` until directed
- Use `train.jsonl` for developing algorithms
- Use `validate.jsonl` (without labels) for blind validation
- Use `test.jsonl` (without labels) only for final evaluation
- Refer to `leftovers.jsonl` for additional examples if needed

---

*Stage 2.1 completed: 2025-11-29*
*Ready for Stage 2.2: Analysis & Hypothesis Development*
