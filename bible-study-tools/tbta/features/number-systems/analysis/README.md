# Number Systems Analysis

Stage 2 analysis results for the TBTA Number Systems feature.

## Data Summary

| Dataset | Entries | Distribution |
|---------|---------|--------------|
| Full TBTA | 171,876 | Singular 66%, Plural 32%, Dual 1%, Trial 0.3%, Quadrial 0.1%, Paucal 0.03% |
| Balanced Sample | 2,233 | ~500 each (Singular, Plural, Dual, Trial), 185 Quadrial, 52 Paucal |
| Train | 1,339 | 60% split |
| Validate | 446 | 20% split |
| Test | 448 | 20% split (reserved) |

## Key Findings

### 1. Data Quality Issue: Quadrial
**SUSPICIOUS**: 185 entries labeled "Quadrial" but no attested language has true quadrial number.
- Action needed: Verify TBTA source data or reclassify as Paucal/Plural

### 2. Pattern Analysis
Strong constituent-label correlations found:
- **Dual**: Body parts (hand, foot, eye, ear) - 100% predictive
- **Singular**: Proper names/divine (Jesus, Yahweh, David) - 93%+ predictive
- **Plural**: Collective nouns (disciples, nations, people)
- **Trial/Quadrial**: Less clear patterns - context-dependent

### 3. Classification Results

| Approach | Validation Accuracy | Notes |
|----------|---------------------|-------|
| Majority Baseline | 22.4% | Always predict Singular |
| Rule-based (logical.py) | 26.0% | Word-matching rules |
| TF-IDF + Logistic Regression | 36.5% | ML baseline |

### 4. Top Predictive Features (TF-IDF)
- Singular: jesus, david, yahweh
- Dual: hand, in_law, ruth
- Plural: person, you
- Trial: night, woman, year
- Quadrial: king, town
- Paucal: fish, day

## Files in This Directory

```
analysis/
├── README.md                          # This file
├── tbta-extract.jsonl                 # Full TBTA extraction (171K entries)
├── tbta-extract-sample.jsonl          # Balanced sample (2.2K entries)
├── tbta-extract-with-verses.jsonl     # Sample enriched with translations
├── data/
│   ├── train.jsonl                    # Training set (DO train on this)
│   ├── validate.jsonl                 # Validation set (tune hyperparams)
│   └── test.jsonl                     # Test set (FINAL eval only)
├── strongs-analysis.jsonl             # Word frequency analysis
├── reason-groupings.jsonl             # Theological context groupings
├── logical.py                         # Rule-based classifier
└── ml_exploration.py                  # ML baseline exploration
```

## Theological Context Groups

From reason-groupings.jsonl:
- TRINITY: 43 entries - Divine plurality contexts
- POETRY: 39 entries - Psalms, Job, Proverbs
- DIVINE_SPEECH: 16 entries - God speaking
- CORPORATE_SOLIDARITY: 12 entries - Israel/Church as collective
- PRAYER: 2 entries
- IMPERATIVE: 2 entries
- UNSET: 200 entries (unclassified)

## Next Steps

1. **Fix Quadrial data** - Investigate source or reclassify
2. **Expand translation cache** - Clone full eBible corpus for richer features
3. **Embedding classifier** - Use AgentDB vector search for semantic similarity
4. **Context window** - Include surrounding verse context for better predictions
5. **Strong's integration** - Link to source language word data

## Usage

```bash
# Run rule-based classifier
python logical.py

# Run ML exploration
python ml_exploration.py

# Note: Set MYBIBLE_DATA_DIR before running analysis scripts
export MYBIBLE_DATA_DIR=/workspace/.data
```
