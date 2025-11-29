# Stage 2.1 Analysis Dataset - Time Granularity

**Feature**: Time Granularity (Temporal Remoteness)
**TBTA Field**: Time (Position 1 in Verb codes)
**Completed**: 2025-11-29

## Overview

This directory contains the complete Stage 2.1 analysis dataset for the time-granularity feature, following the standardized TBTA feature development methodology.

## Dataset Statistics

### Extraction (Step 1A)

- **Total TBTA annotations**: 72,087 entries
- **Unique values**: 24 distinct time granularity labels
- **Source**: TBTA macula dataset (all books, all verses with Time annotations)

**Top values** (see [distribution.yaml](distribution.yaml)):
- Discourse: 29,102 (40.4%)
- Present: 25,659 (35.6%)
- Immediate Future: 11,669 (16.2%)
- Later Today: 1,295 (1.8%)
- Others: ~16%

### Balanced Dataset (Step 1B)

- **Selected entries**: 1,000 (from 72,087)
- **Selection criteria**:
  - Balanced by genre (OT/NT proportional)
  - One per verse (no duplicate verses)
  - Sampled by constituent diversity
  - Capped at 150 per major label

**Enrichment**:
- ✅ **strongs_number**: 92.3% coverage (923/1000)
- ✅ **reason_group**: 100% coverage (1000/1000)
- ✅ **difficulty**: Assigned for non-arbitrary cases

**Reason groups**:
- GENERIC_FUTURE: 248
- DIALOGUE: 204
- GENERIC_PAST: 165
- GOSPEL_NARRATIVE: 153
- GENERIC_PRESENT: 90
- PATRIARCHAL: 42
- CONQUEST_JUDGES: 29
- PROPHETIC_NARRATIVE: 25
- TIMELESS_TEACHING: 18
- Others: ~26

### Translations (Step 1C)

**11 translation codes** included (see [LANGUAGE-SELECTION.md](LANGUAGE-SELECTION.md)):

**Core languages**:
- eng-YLT (99.5%)
- grc (90.2% combined - BRENT for OT, SR for NT)
- hbo (67.5% - OT only)
- heb-heb (99.5%)
- lat-VUC (99.5%)

**Time-marking languages**:
- swh-ONEN (Swahili - Bantu, 2-3 past distinctions): 99.5%
- tgl-ULB (Tagalog - Austronesian, aspect-based): 99.5%
- ind (Indonesian - control, no time granularity): 99.5%

**Additional major languages**:
- spa-BES (Spanish): 99.5%
- fra-LSG (French): 99.5%
- deu-1912 (German): 99.5%

### Final Split (Step 1E)

| Split | Entries | File |
|-------|---------|------|
| **Train** | 789 | [data/train.jsonl](data/train.jsonl) |
| **Validate** | 104 | [data/validate.jsonl](data/validate.jsonl) |
| **Validate (secret)** | 104 | [data/validate.secret.jsonl](data/validate.secret.jsonl) |
| **Test** | 107 | [data/test.jsonl](data/test.jsonl) |
| **Test (secret)** | 107 | [data/test.secret.jsonl](data/test.secret.jsonl) |
| **Leftovers** | 70,643 | [data/leftovers.jsonl](data/leftovers.jsonl) |

**Note**: Secret files contain answers (TBTA labels). Regular files exclude labels for blind testing.

## Audit Results

Full audit report: [audit-data.md](audit-data.md)

### ✅ All Requirements Met

- [x] Strongs list present: 92.3%
- [x] Strongs_number assigned: 92.3%
- [x] Reason_group assigned: 100%
- [x] Translations present: 99.5%
- [x] Core translations: >99%
- [x] Time-marking languages: Swahili at 99.5%
- [x] Additional languages: 8+ at >88% coverage

### Known Issues

1. **Missing strongs_number (7.7%)**: 77 entries could not infer strongs_number from constituent mapping. ACCEPTABLE - full strongs list still present.
2. **Missing translations (0.5%)**: 5 verses not in sparse checkout. ACCEPTABLE - can add if needed.

## File Structure

```
analysis/
├── README.md                  # This file
├── distribution.yaml          # Full value distribution statistics
├── LANGUAGE-SELECTION.md      # Language selection rationale
├── audit-data.md              # Data quality audit report
└── data/
    ├── train.jsonl            # Training set (789)
    ├── validate.jsonl         # Validation set (104, no labels)
    ├── validate.secret.jsonl  # Validation set (104, with labels)
    ├── test.jsonl             # Test set (107, no labels)
    ├── test.secret.jsonl      # Test set (107, with labels)
    └── leftovers.jsonl        # Remaining data (70,643)
```

## Data Fields

Each entry contains:

```jsonl
{
  "verse": "GEN-001-026",
  "label": "Historic Past",           // TBTA annotation
  "constituent": "make",
  "part": "Verb",
  "path": "Clause[0]/VP[0]",
  "text": "God said, let **us** make mankind...",
  "strongs": "H7200 H0430 ...",       // Full verse Strong's codes
  "strongs_number": "H6213",          // Target constituent Strong's
  "reconstructed_verse": "God said, let us make mankind in our image...",
  "dataset": {
    "split": "train",                  // train/validate/test
    "section": "OT",                   // OT or NT
    "literary_type": "history",        // Genre
    "reason_group": "CREATION_PRIMEVAL", // Logical grouping
    "difficulty": "adversarial"        // Optional: hard/adversarial
  },
  "translations": {
    "eng-YLT": "And God saith, `Let Us make man...",
    "swh-ONEN": "Ndipo Mungu akasema, \"Tufanye mtu...",
    "grc-BRENT": "καὶ εἶπεν ὁ θεός...",
    ...
  }
}
```

## Methodology Notes

### Strongs Number Inference

Strongs_number was inferred by:
1. Matching constituent to glosses in strongs list
2. Looking for ** markers in reconstructed text
3. Fallback to position-based mapping

92.3% success rate is acceptable for an inferential feature where source languages (Hebrew/Greek) don't encode time granularity.

### Reason Group Taxonomy

Based on [research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](../research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml):

**Non-arbitrary (contextual)**:
- TIMELESS_TEACHING: Eternal principles (e.g., Sermon on Mount)
- CHARACTER_PERSPECTIVE: Direct discourse from speaker's viewpoint
- PROPHETIC_FULFILLMENT: Prophecy (original or fulfilled perspective)
- NARRATIVE_FRAME: Historical framing

**Arbitrary (stylistic - majority)**:
- CREATION_PRIMEVAL, PATRIARCHAL, EXODUS_WILDERNESS, etc.
- GOSPEL_NARRATIVE, ACTS_NARRATIVE, EPISTLE_NARRATIVE
- GENERIC_PAST, GENERIC_PRESENT, GENERIC_FUTURE

### Language Selection Rationale

**Why Swahili?** Bantu language family shows 80% require time granularity marking with 2-4 past distinctions. Swahili is major translation language with good Bible coverage.

**Why Tagalog?** Tests edge of feature - Austronesian aspect-based system where time granularity is variable/optional.

**Why Indonesian?** Control language - Austronesian but no grammatical time granularity (aspect-only system).

**Why core languages?** Hebrew and Greek do NOT encode time granularity, confirming TBTA is 100% inferential. English, Latin, Spanish, French, German also lack feature - serve as controls.

## Next Steps

**Stage 2.2**: Analysis & Hypothesis Testing
- Validate reason_group taxonomy against translations
- Test whether time-marking languages (Swahili) show different patterns
- Identify adversarial cases where AI would likely fail

**Stage 3**: Logical Rules Development
- Extract deterministic rules where possible
- Document edge cases requiring contextual inference

**Stage 4-6**: Prompt development, testing, peer review

## References

- **Stage 1 Research**: [../research/](../research/)
- **TBTA Documentation**: [../research/TBTA.md](../research/TBTA.md)
- **Language Typology**: [../research/LANGUAGES.md](../research/LANGUAGES.md)
- **Theological Groups**: [../research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](../research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)

---

**Generated**: 2025-11-29 | **Stage**: 2.1 Complete
