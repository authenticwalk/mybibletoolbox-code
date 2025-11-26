# Number Systems: Analysis Summary

**Feature**: Grammatical Number (Singular, Dual, Trial, Quadrial, Paucal, Plural)
**Stage**: 2 - Analysis & Hypothesis Validation
**Date**: 2025-11-26
**Status**: Complete

## Distribution

| Value | Count | Percentage |
|-------|-------|------------|
| Singular | 113,745 | 66.2% |
| Plural | 55,654 | 32.4% |
| Dual | 1,744 | 1.0% |
| Trial | 496 | 0.3% |
| Quadrial | 185 | 0.1% |
| Paucal | 52 | 0.03% |
| **Total** | **171,876** | **100%** |

## Dataset Sizes

| Split | Count | Purpose |
|-------|-------|---------|
| Train | 331 | LLM training with labels visible |
| Validate | 100 | Prompt tuning (labels hidden) |
| Test | 96 | Final evaluation (DO NOT TOUCH) |
| Leftovers | 171,260 | Remaining data for edge case analysis |

## Key Findings

### 1. LLM Baseline: 76% Accuracy

**Major Error Patterns**:
1. **Paucal → Plural** (41.7% of errors): LLM doesn't know when to use "few" vs "many"
2. **Quadrial → Plural** (12.5%): No natural language has grammatical quadrial
3. **Trinity inconsistency**: LLM correctly uses Trial for "us" passages, but TBTA sometimes uses Plural

See: [HIGH-LEVEL-REVIEW.md](HIGH-LEVEL-REVIEW.md)

### 2. TBTA Data Quality Issues

**Trinity Passage Inconsistency** (HIGH Priority):
- GEN.1.26 → Trial (correct)
- GEN.11.7 → Plural (should be Trial?)
- ISA.6.8 → Plural (should be Trial?)

**Quadrial Category** (MEDIUM Priority):
- 185 uses but no attested language has grammatical quadrial
- TBTA uses semantically (exactly 4 entities)
- Recommend: Document as semantic category or merge to Paucal

**Paucal Boundary** (HIGH Priority):
- Only 52 natural occurrences (0.03%)
- Unclear criteria for when to use vs Plural
- Causes 41.7% of LLM errors

See: [TBTA-QUALITY.md](TBTA-QUALITY.md)

### 3. Edge Case Patterns

**When NOT Singular/Plural**:
- **Dual (1%)**: Explicit pairs ("two men"), body parts (hands, feet, eyes)
- **Trial (0.3%)**: Groups of 3, Trinity references
- **Quadrial (0.1%)**: Groups of 4 (Daniel's friends, four creatures)
- **Paucal (0.03%)**: "few/little", small indefinite quantities

See: [EDGE-CASES.md](EDGE-CASES.md)

### 4. Strong's Word Patterns

**No Strong's number reliably predicts number category** with ≥95% confidence.
- H376 (אִישׁ "man"): Variable across all categories
- Body parts show Dual tendency but not exclusive

See: [STRONGS.md](STRONGS.md)

### 5. Word Patterns

**Discriminative Words**:
- "two/dos/duo" → Dual (high confidence)
- "four/cuatro" → Quadrial (moderate)
- "few/pocos" → Paucal (moderate)
- "hands/feet/eyes" → Dual (body parts)

See: [WORD-ANALYSIS.md](WORD-ANALYSIS.md)

## Suspicious Data

| Issue | Priority | Impact |
|-------|----------|--------|
| Trinity passages inconsistent | HIGH | Theological precision |
| Quadrial linguistically invalid | MEDIUM | ML confusion |
| Paucal criteria unclear | HIGH | 41.7% LLM errors |
| EXO.28.21 "12 stones" labeled Dual | LOW | Data error |

## Recommended Approach

### For ML Training:
- [ ] **4-category system first**: Start with Singular/Dual/Trial/Plural (skip Quadrial/Paucal)
- [ ] **Explicit number features**: Count "two", "three", "four", "few" in context
- [ ] **Body part detection**: Dual for hands/feet/eyes unless overridden
- [ ] **Trinity context hints**: Use reason-groupings-with-hints.jsonl

### Before Scaling:
- [ ] **Resolve TBTA issues**: Get clarity on Trinity labeling policy
- [ ] **Document Paucal criteria**: When is "few" few enough?
- [ ] **Decide on Quadrial**: Keep as semantic or merge to Paucal

### Hybrid Approach (Recommended):
1. **Simple rules** for explicit counts (2 → Dual, 3 → Trial, 4+ → Plural)
2. **LLM with hints** for theological/contextual cases
3. **Default to morphology** when source language available

## Analysis Files

| File | Purpose |
|------|---------|
| [HIGH-LEVEL-REVIEW.md](HIGH-LEVEL-REVIEW.md) | LLM baseline analysis (76% accuracy) |
| [EDGE-CASES.md](EDGE-CASES.md) | When NOT Singular/Plural |
| [TBTA-QUALITY.md](TBTA-QUALITY.md) | Data quality issues, TBTA questions |
| [STRONGS.md](STRONGS.md) | Strong's word pattern analysis |
| [WORD-ANALYSIS.md](WORD-ANALYSIS.md) | Translation word patterns |
| [reason-groupings-with-hints.jsonl](reason-groupings-with-hints.jsonl) | Theological hints for verses |

## Data Files

| File | Count | Purpose |
|------|-------|---------|
| data/train.jsonl | 331 | Training data with labels |
| data/validate.jsonl | 100 | Validation (no labels) |
| data/validate.secret.jsonl | 100 | Validation answers |
| data/test.jsonl | 96 | Test (no labels) |
| data/test.secret.jsonl | 96 | Test answers |
| data/leftovers.jsonl | 171,260 | Remaining TBTA data |
| enriched.secret.jsonl | 527 | Enriched with 17 translations |
| tbta-extract.secret.jsonl | 171,876 | Full TBTA extraction |

## Next Steps (Stage 3)

1. **Resolve TBTA issues** before prompt engineering
2. **Build hybrid classifier**: Rules + LLM
3. **Test on validate set**: Target >90% accuracy
4. **Final test**: Only after prompt optimization complete
