# Illocutionary Force - Stage 2.1 Analysis Dataset

**Feature**: Illocutionary Force
**Stage**: 2.1 - Analysis Dataset Creation
**Date Completed**: 2025-11-29
**Status**: ✓ COMPLETE

---

## Overview

This directory contains the completed Stage 2.1 analysis dataset for the Illocutionary Force feature. The dataset has been extracted from TBTA annotations, balanced, enriched with multilingual translations, audited, and split for model training and evaluation.

---

## Directory Structure

```
analysis/
├── data/
│   ├── train.jsonl              # 80 entries for training
│   ├── validate.jsonl           # 10 entries for validation (without answers)
│   ├── validate.secret.jsonl    # 10 entries for validation (with answers)
│   ├── test.jsonl               # 10 entries for testing (without answers)
│   ├── test.secret.jsonl        # 10 entries for testing (with answers)
│   └── leftovers.jsonl          # 71,714 entries not used in train/validate/test
├── distribution.yaml            # Distribution of illocutionary force values in full TBTA
├── LANGUAGE-SELECTION.md        # Rationale for selected translation languages
├── audit-data.md                # Data quality audit report
└── README.md                    # This file
```

---

## Dataset Statistics

### Full TBTA Extraction
- **Total annotations**: 72,505
- **Unique verses**: 11,647
- **Source**: TBTA field "Illocutionary Force"

### Balanced Dataset (train/validate/test)
- **Total entries**: 100
- **Train**: 80 entries
- **Validate**: 10 entries
- **Test**: 10 entries
- **Leftovers**: 71,714 entries (remainder from full extraction)

### Distribution of Illocutionary Force Values

From full TBTA extraction (72,505 annotations):

| Value | Count | Percentage |
|-------|-------|------------|
| Declarative | 67,037 | 92.46% |
| Imperative | 3,955 | 5.45% |
| Content Interrogative | 838 | 1.16% |
| Yes-No Interrogative | 552 | 0.76% |
| Suggestive 'let's' | 71 | 0.10% |
| Jussive | 34 | 0.05% |
| Imperative with emphasized Agent | 18 | 0.02% |

**Note**: The highly imbalanced distribution (92.46% Declarative) required careful balancing in the dataset creation process.

---

## Balancing Strategy

The balanced dataset (100 entries) was created using `draft_dataset.py` with:
- **One entry per verse** (avoid duplicate verses)
- **Genre interleaving** (balanced OT/NT distribution)
- **Equal representation** across all 7 illocutionary force values
- **Constituent sampling** (field='constituent' to ensure variety)

### Balanced Dataset Distribution

| Illocutionary Force | Train | Validate | Test | Total |
|---------------------|-------|----------|------|-------|
| Declarative | 13 | 2 | 1 | 16 |
| Content Interrogative | 13 | 2 | 1 | 16 |
| Imperative with emphasized Agent | 12 | 2 | 1 | 15 |
| Yes-No Interrogative | 12 | 2 | 1 | 15 |
| Imperative | 11 | 2 | 1 | 14 |
| Jussive | 10 | 1 | 1 | 12 |
| Suggestive 'let's' | 9 | 2 | 1 | 12 |

---

## Reason Groups

Each entry was manually assigned a `reason_group` field indicating the logical/theological grouping:

| Reason Group | Count | Description |
|--------------|-------|-------------|
| ROUTINE-QUESTION | 25 | Information-seeking interrogatives |
| NARRATIVE-STATEMENT | 15 | Historical declaratives |
| COHORTATIVE | 10 | Hortative "let's" suggestions |
| ROUTINE-DIRECTIVE | 7 | Mundane commands |
| DIVINE-EMPHASIS | 7 | Emphatic directives from God |
| EMPHATIC-DIRECTIVE | 7 | Human emphatic directives |
| JUSSIVE | 6 | Third-person commands |
| DIVINE-DIRECTIVE | 6 | Divine commands |
| THEOLOGICAL-QUESTION | 6 | Questions with theological content |
| DIVINE-FIAT | 4 | Creation commands (Gen 1) - **ADVERSARIAL** |
| DIVINE-LAW | 2 | Ten Commandments - **ADVERSARIAL** |
| MALICIOUS-COHORTATIVE | 2 | Evil "let's" suggestions |
| DIVINE-BLESSING | 1 | "Be fruitful and multiply" type |
| RITUAL-INSTRUCTION | 1 | Tabernacle/ritual commands |
| PETITION-JUSSIVE | 1 | Petitionary jussives |

**Theological significance**: DIVINE-FIAT and DIVINE-LAW are theologically critical passages marked as "adversarial" difficulty.

---

## Translation Languages

The dataset includes 15 translation languages across 8+ language families:

### Core Languages (6)
- **eng-YLT**: Young's Literal Translation (baseline)
- **grc**: Koine Greek (NT source, 4-mood system)
- **hbo**: Biblical Hebrew (OT source, volitional forms)
- **heb-heb**: Modern Hebrew
- **lat-VUC**: Latin Vulgate (historical base)
- **arb-NAV**: Arabic Van Dyck (Semitic, jussive mood)

### Mandatory-Marking Languages (5)
- **tha-KJV**: Thai (Tai-Kadai, sentence-final particles)
- **tur-YTC**: Turkish (Turkic, interrogative suffix -mI)
- **tgl-ULB**: Tagalog (Austronesian, sentence-final particles)
- **ind-ind**: Indonesian (Austronesian, optional -kah)

### Optional-Marking Languages (4)
- **deu-1912**: German (Germanic, word order + particles)
- **fra-LSG**: French (Romance, multiple interrogative strategies)
- **spa-BES**: Spanish (Romance, subjunctive for jussive)
- **swh-ONEN**: Swahili (Bantu, optional particle je)

See `LANGUAGE-SELECTION.md` for detailed rationale.

---

## Data Quality

All entries include:
- ✓ **verse**: Biblical reference (e.g., "GEN-001-003")
- ✓ **label**: Illocutionary force value
- ✓ **strongs**: Space-separated Strong's numbers for full verse (95/100)
- ✓ **strongs_number**: Strong's number of target constituent (100/100)
- ✓ **dataset.reason_group**: Logical/theological grouping (100/100)
- ✓ **dataset.difficulty**: "adversarial" or "hard" for challenging cases
- ✓ **translations**: Dictionary of 13-15 translations per entry

See `audit-data.md` for complete quality audit.

---

## Usage

### Training
Use `data/train.jsonl` (80 entries) for model training.

### Validation
- During development: Use `data/validate.jsonl` (no answers)
- Post-validation: Check against `data/validate.secret.jsonl` (with answers)

### Testing
- **DO NOT TOUCH** `data/test.jsonl` until final evaluation
- After final eval: Check against `data/test.secret.jsonl`

### Leftovers
`data/leftovers.jsonl` contains 71,714 TBTA annotations not used in train/validate/test. These can be used for:
- Additional training data (if needed)
- Adversarial testing
- Cross-validation

---

## Next Steps (Stage 2.2+)

1. **Stage 2.2**: Hypothesis Testing
   - Test specific hypotheses about illocutionary force patterns
   - Analyze translation consensus in mandatory-marking languages

2. **Stage 2.3**: Scorecard Development
   - Create evaluation metrics
   - Define success criteria

3. **Stage 3**: Prompt Engineering
   - Use this dataset to develop and test prompts
   - Iteratively improve based on validation set

---

## Files Generated

- ✓ `distribution.yaml`: Value distribution from full TBTA
- ✓ `LANGUAGE-SELECTION.md`: Translation language rationale
- ✓ `audit-data.md`: Data quality audit
- ✓ `data/train.jsonl`: 80 training entries
- ✓ `data/validate.jsonl` + `.secret.jsonl`: 10 validation entries
- ✓ `data/test.jsonl` + `.secret.jsonl`: 10 test entries
- ✓ `data/leftovers.jsonl`: 71,714 unused entries

---

**Completed by**: Claude (Sonnet 4.5)
**Date**: 2025-11-29
