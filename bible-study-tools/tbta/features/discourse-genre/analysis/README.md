# Analysis Results: Discourse Genre Feature

**Stage 2.1 Complete**: 2025-11-29

## Overview

This directory contains the balanced dataset and analysis results for the **Discourse Genre** feature. The dataset was created following the Stage 2.1 process from `.instructions-to-build-feature/STAGE-2-1-ANALYSIS-DATASET.md`.

## Files in This Directory

### Analysis Documentation
- **[distribution.yaml](distribution.yaml)** - Distribution of genre values in TBTA data
- **[LANGUAGE-SELECTION.md](LANGUAGE-SELECTION.md)** - Rationale for translation language selection
- **[audit-data.md](audit-data.md)** - Complete data audit report
- **[README.md](README.md)** - This file

### Dataset Directory: `data/`
- **train.jsonl** (80 entries) - Training dataset with translations
- **validate.jsonl** (10 entries) - Validation dataset (public version)
- **validate.secret.jsonl** (10 entries) - Validation dataset (with labels)
- **test.jsonl** (10 entries) - Test dataset (public version)
- **test.secret.jsonl** (10 entries) - Test dataset (with labels)
- **leftovers.jsonl** (71,797 entries) - Remaining TBTA entries not used in train/validate/test

## Dataset Summary

### Extraction Results
- **Total TBTA annotations**: 72,505 clause-level annotations
- **Verses covered**: 11,649 verses (~37% of Bible)
- **Unique genre values**: 3
  - Climactic Narrative Story: 72,440 (99.9%)
  - Genealogy: 62 (0.1%)
  - Expository: 3 (0.0%)

### Balanced Dataset
- **Total selected**: 100 verses
- **Training set**: 80 verses
- **Validation set**: 10 verses
- **Test set**: 10 verses

### Reason Groups (Theological Significance)
Based on [research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](../research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml):

| Reason Group | Count | Stakes | Description |
|--------------|-------|--------|-------------|
| HISTORICAL-NARRATIVE | 37 | Arbitrary | General OT/NT narrative |
| GOSPEL-NARRATIVE | 27 | Medium | Gospel biographical-theological narrative |
| GENEALOGY-LIST | 22 | Arbitrary | Biblical genealogies |
| WISDOM-INSTRUCTION | 7 | Medium | Proverbs, wisdom literature |
| EPISTOLARY-DISCOURSE | 5 | Medium | NT epistles |
| APOCALYPTIC-VISION | 1 | High | Revelation apocalyptic |
| CREATION-NARRATIVE | 1 | High | Genesis 1-2 creation account |

**Theological distribution**:
- High stakes: 2 entries (2%)
- Medium stakes: 39 entries (39%)
- Arbitrary: 59 entries (59%)

### Translation Coverage
Dataset enriched with **8 translations** across diverse language families:

| Language | Code | Family | Coverage |
|----------|------|--------|----------|
| English | eng-YLT | Indo-European | 99/100 |
| Greek (NT) | grc-SR | Indo-European | 48/100 |
| Greek (OT/LXX) | grc-BRENT | Indo-European | 45/100 |
| Hebrew (OT) | hbo-hbo | Afro-Asiatic | 51/100 |
| Modern Hebrew | heb-heb | Afro-Asiatic | 99/100 |
| Arabic | arb-NAV | Afro-Asiatic | 99/100 |
| German | deu-1912 | Indo-European | 99/100 |
| French | fra-LSG | Indo-European | 99/100 |
| Spanish | spa-BES | Indo-European | 99/100 |
| Indonesian | ind-AYT | Austronesian | 99/100 |

**Note**: Latin Vulgate (lat-VUL) and Chinese (zho-CUV) were requested but not available in eBible corpus.

## Key Findings

### 1. Extreme TBTA Imbalance
- TBTA data shows 99.9% "Climactic Narrative Story"
- Only 3 unique values found (vs. 6+ documented in TBTA guidelines)
- **Implication**: TBTA primarily annotated narrative portions
- Missing genres: Poetry, Legal, Prophetic, Epistolary, Parabolic

### 2. Dataset Balanced by Reason Groups
Instead of balancing by TBTA labels (which are imbalanced), we balanced by **theological reason groups**:
- Oversampled rare values (Genealogy, Expository)
- Included high-stakes contexts (CREATION-NARRATIVE, APOCALYPTIC-VISION)
- Included medium-stakes contexts (GOSPEL, WISDOM, EPISTOLARY)
- Representative sample of arbitrary contexts (HISTORICAL, GENEALOGY)

### 3. Strong's Number Assignment
- All 100 entries have `strongs_number` field
- 81/100 have full Strong's codes list from macula data
- 19/100 missing macula data (Matthew genealogies, Daniel verses) - manually assigned appropriate codes

## Next Steps (Stage 2.2+)

1. **Step 2A**: Create baseline prediction rules using `logical.py`
2. **Step 2B**: Test baseline rules against validate set
3. **Step 2C**: Create LLM-based prediction system
4. **Step 2D**: Iterative improvement based on validate set performance
5. **Step 2E**: Final evaluation on test set (locked until Stage 5)

## Related Files

- **Feature Definition**: [../README.md](../README.md)
- **Research**: [../research/](../research/)
  - TBTA analysis: [TBTA.md](../research/TBTA.md)
  - Language analysis: [LANGUAGES.md](../research/LANGUAGES.md)
  - Scholarly sources: [SCHOLARLY.md](../research/SCHOLARLY.md)
  - Theological groups: [THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](../research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)
- **Methodology**: [../.instructions-to-build-feature/](../.instructions-to-build-feature/)

## Notes

### Why Only 3 TBTA Values?
The TBTA dataset we have access to is incomplete or focused primarily on narrative analysis. The documentation mentions 6+ genre types (Narrative, Expository, Poetic, Legal, Prophetic, Epistolary), but the actual data only contains 3 values.

This is not a problem for our methodology because:
1. We're not trying to reproduce TBTA labels exactly
2. We're using TBTA as one source of truth alongside real translations
3. Our reason_groups provide finer-grained theological classification
4. Stage 3+ will validate against translation consensus, not just TBTA

### Dataset Size
The 100-entry dataset is intentionally small:
- Follows Stage 2.1 guidelines: max 800 train, 100 validate, 100 test
- Keeps manual enrichment workload manageable
- Provides sufficient statistical power for initial hypothesis testing
- Can be expanded in later stages if needed

### Translation Selection Rationale
Selected languages represent diverse genre-marking strategies:
- **Morphological**: Spanish (preterite/imperfect aspect)
- **Syntactic**: Arabic (VSO word order), Hebrew (wayyiqtol chains)
- **Lexical**: English (connectives), German (particles), French (register)
- **Source languages**: Greek, Hebrew (preserve original discourse patterns)

See [LANGUAGE-SELECTION.md](LANGUAGE-SELECTION.md) for complete rationale.

---

**Last Updated**: 2025-11-29
**Status**: Stage 2.1 Complete
**Next**: Stage 2.2 - Create baseline prediction rules
