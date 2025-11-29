# Polarity Feature - Stage 2.1 Analysis Dataset

**Status**: COMPLETE
**Date Completed**: 2025-11-29
**Feature**: Polarity (Affirmative, Negative, Emphatic Affirmative, Emphatic Negative)

## Overview

This directory contains the complete Stage 2.1 analysis dataset for the polarity feature. All steps have been successfully completed following the process defined in `.instructions-to-build-feature/STAGE-2-1-ANALYSIS-DATASET.md`.

## Dataset Statistics

### Source Data
- **Total TBTA annotations**: 243,965 polarity annotations
- **Unique verses**: 11,646
- **Distribution**:
  - Affirmative: 238,971 (97.95%)
  - Negative: 4,798 (1.97%)
  - Emphatic Affirmative: 164 (0.07%)
  - Emphatic Negative: 32 (0.01%)

### Balanced Dataset
- **Total selected entries**: 2,170
- **Target distribution**:
  - Affirmative: 1,000 (balanced)
  - Negative: 1,000 (balanced)
  - Emphatic Affirmative: 143 (all available)
  - Emphatic Negative: 27 (all available)

### Final Splits
- **train.jsonl**: 1,736 entries (80%)
- **validate.jsonl**: 217 entries (10%)
- **test.jsonl**: 217 entries (10%)
- **leftovers.jsonl**: 239,277 entries (remaining from original extract)

## Data Enrichment

### Strong's Numbers
- **strongs field**: List of Strong's codes for entire verse (93.2% coverage)
- **strongs_number**: Specific Strong's code for the constituent (61.0% coverage)

### Reason Groups
All entries tagged with semantic/linguistic reason_group (30 categories):
- VERB-GENERAL, ACTION-COMMAND, COGNITION, COMMUNICATION
- DEITY, HUMAN-INDIVIDUAL, STATE, POSSESSION
- VIOLENCE, JUDGMENT, TREAT, RITUAL, MOVEMENT
- Plus emphatic variants: *-EMPHATIC

### Translation Coverage
**Core languages** (>90% coverage):
- eng-YLT (99.6%)
- heb-heb (99.6%)
- lat-VUC (99.5%)
- arb-NAV (99.6%)
- grc (89.2% - NT only, expected)
- hbo (65.0% - OT only, expected)

**Additional languages** (>99% coverage):
- deu-1912, fra-LSG, spa-BES, ind-AYT, rus-SYN
- Plus: jpn-JAP, kor, swa-ONEN, tha

**Total**: 18 languages representing multiple language families and polarity-marking strategies

## Files in This Directory

### Data Files
- `data/train.jsonl` - Training dataset (1,736 entries)
- `data/validate.jsonl` - Validation dataset (217 entries)
- `data/test.jsonl` - Test dataset (217 entries) - DO NOT USE until final eval
- `data/test.secret.jsonl` - Test answers (hidden for blind testing)
- `data/validate.secret.jsonl` - Validation answers (hidden for blind testing)
- `data/leftovers.jsonl` - Remaining entries not in train/validate/test

### Documentation Files
- `README.md` - This file
- `distribution.yaml` - Feature value distribution statistics
- `LANGUAGE-SELECTION.md` - Language selection rationale and validation
- `audit-data.md` - Complete data audit results

### Secret Files (for reference, not for training)
- `tbta-extract.secret.jsonl` - Full extraction with answers
- `enriched.secret.jsonl` - Enriched dataset with answers

## Data Quality

See `audit-data.md` for complete audit results. Summary:
- ✓ All entries have reason_group assigned
- ✓ Core translations present (accounting for OT/NT split)
- ✓ 12+ languages with >99% coverage
- ✓ Proper 80/10/10 dataset split
- ⚠️ strongs_number incomplete (61%) but not critical for polarity

## Next Steps (Stage 2.2+)

This dataset is ready for:
1. **Stage 2.2**: Manual analysis of polarity patterns in translations
2. **Stage 2.3**: Hypothesis development about polarity marking
3. **Stage 2.4**: Algorithm development
4. **Stage 2.5**: Validation against validate.jsonl
5. **Stage 2.6**: Final testing against test.jsonl

## Notes

- Polarity is a universal feature - all languages mark negation
- The heavily imbalanced source distribution (98% affirmative) required careful balancing
- Emphatic cases are extremely rare and all included as adversarial test cases
- Testament-specific coverage (grc=NT, hbo=OT) is expected and normal

---

**Generated**: 2025-11-29
**Process**: STAGE-2-1-ANALYSIS-DATASET.md
**Feature**: polarity
