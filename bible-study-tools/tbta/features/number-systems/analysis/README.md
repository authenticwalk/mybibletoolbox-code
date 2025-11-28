# Number Systems Analysis Dataset

**Created**: 2025-11-28
**Stage**: 2.1 - Analysis Dataset

## Dataset Summary

| Split | Count | Purpose |
|-------|-------|---------|
| train.jsonl | 301 | Model development |
| validate.jsonl | 101 | Hyperparameter tuning |
| test.jsonl | 110 | Final evaluation (DO NOT TOUCH) |
| leftovers.jsonl | 170,182 | Remaining TBTA data |

**Total TBTA annotations**: 171,876

## Distribution

From `distribution.yaml`:
- Singular: 113,745 (66.2%)
- Plural: 55,654 (32.4%)
- Dual: 1,744 (1.0%)
- Trial: 496 (0.3%)
- Quadrial: 185 (0.1%)
- Paucal: 52 (0.03%)

## Dataset Balance

The train/validate/test sets are balanced to include:
- All rare values (Paucal, Quadrial, Trial) over-sampled
- Mix of OT/NT
- Mix of literary types
- Theological groups (TRINITY, BODY_PARTS, PAIR_NARRATIVE, etc.)
- Easy and adversarial cases

## Translations Included

Enriched with 10 translations (47% coverage due to sparse checkout):
- grc-BYZ, grc-LXX (Greek)
- lat-VUC (Latin Vulgate)
- eng-YLT (English - Young's Literal)
- heb-WLC (Hebrew)
- ara, arb-NAV (Arabic - has dual morphology)
- rus-SYN (Russian)
- jpn-1965 (Japanese)
- ind (Indonesian)

## File Structure

```
analysis/
├── data/
│   ├── train.jsonl          # Training set (labels visible)
│   ├── validate.jsonl       # Validation set (labels removed)
│   ├── validate.secret.jsonl # Validation answers (DO NOT PEEK)
│   ├── test.jsonl           # Test set (labels removed)
│   ├── test.secret.jsonl    # Test answers (DO NOT PEEK)
│   └── leftovers.jsonl      # Remaining data
├── distribution.yaml        # Feature value distribution
├── datasets.jsonl           # Intermediate file (pre-split)
├── enriched.secret.jsonl    # Full enriched data (hidden)
├── tbta-extract.secret.jsonl # Full extraction (hidden)
└── README.md               # This file
```

## Next Steps

Proceed to Stage 3: Experimentation
- Develop prediction algorithms
- Test against validate set
- Iterate until accuracy target met
