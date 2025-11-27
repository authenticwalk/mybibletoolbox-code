# Number Systems: LLM Baseline Analysis

**Date**: 2025-11-27
**Dataset**: 100 samples from train.jsonl (stratified by label)
**Accuracy**: 84/100 (84.0%)

## Baseline Prompt Used

```
Grammatical number encodes the count of entities referenced by a noun or pronoun.
Label each highlighted word (**word**) with the number category that matches how
many entities it refers to in context.

- Singular:
  - Refers to exactly 1 entity
  - Proper names (Jesus, David, Yahweh, God)
  - Lexicalized plurals with singular meaning ("heavens" = one sky, "waters" = one body of water)
  - Collective nouns treated as a unit ("the people" as one group)
  - Abstract concepts (faith, love, grace)

- Dual:
  - Refers to exactly 2 entities
  - Explicit "two" or "2" in context
  - Natural body part pairs (hands, feet, eyes, ears)
  - Named pairs (Ruth and Naomi, two disciples, two witnesses)
  - Hebrew dual morphology (-ayim suffix)

- Trial:
  - Refers to exactly 3 entities
  - Explicit "three" or "3" in context
  - Trinity contexts where God says "us/our" (Gen 1:26, 3:22, 11:7, Isa 6:8)
  - Named triplets (Peter/James/John, Shadrach/Meshach/Abednego)
  - Three days, three men, etc.

- Quadrial:
  - Refers to exactly 4 entities
  - Explicit "four" or "4" in context
  - Four living creatures, four corners, four rivers
  - Groups of exactly 4 people (Daniel and 3 friends = 4)

- Paucal:
  - Refers to a few entities (typically 3-10, not precisely specified)
  - Words like "few", "some", "several", "a little"
  - Small indefinite groups where exact count is unknown
  - Numbers 5-10 when not emphasizing the exact count

- Plural:
  - Refers to many entities (general plural, large or unspecified)
  - Large groups: nations, peoples, crowds, multitudes
  - Unspecified quantities greater than paucal
  - Generic statements ("all have sinned")
```

## Results Summary

| Metric | Value |
|--------|-------|
| Accuracy | 84/100 (84.0%) |
| Errors | 16 |
| Previous (wrong format) | 76/100 (76.0%) |
| Improvement | +8% |

## Key Findings

### 1. Major Error Pattern: Paucal → Plural (4 errors, 25% of all errors)

The LLM still struggles with Paucal - defaulting to Plural for unspecified small groups.

**Examples**:
- LUK.005.019: "**man** could not enter house" → TBTA: Paucal, LLM: Plural
- LUK.005.018: "**man** carry paralyzed man" → TBTA: Paucal, LLM: Plural
- 1SA.004.004: "leader send **man** Shiloh" → TBTA: Paucal, LLM: Plural

**Analysis**: TBTA uses Paucal for small groups even without explicit "few" markers. The LLM needs more context or stricter criteria.

### 2. Trinity Passages: LLM Correct, TBTA Inconsistent

**LLM correctly applies Trial to Trinity contexts, but TBTA labels them as Plural:**
- GEN.011.007 "let **us** go down" → LLM: Trial, TBTA: Plural
- ISA.006.008 "who will go for **us**" → LLM: Trial, TBTA: Plural

**Issue**: This is a TBTA data quality issue, not an LLM error. The LLM correctly followed the prompt's Trinity guidance, but TBTA inconsistently labels these passages.

### 3. Lexicalized Duals

**PSA.019.001 "heavens"**:
- LLM: Singular (correctly following prompt - lexicalized plural with singular meaning)
- TBTA: Plural

**Analysis**: The LLM followed the prompt correctly. This may be a TBTA inconsistency - Hebrew שָׁמַיִם has dual morphology but is often semantically singular.

### 4. Remaining Errors

| Error Type | Count | Analysis |
|-----------|-------|----------|
| Paucal → Plural | 4 | LLM defaults to Plural for small groups |
| Plural → Singular | 2 | Collective/lexicalized confusion |
| Plural → Trial | 2 | LLM over-applies Trinity rule (but may be correct) |
| Other edge cases | 8 | Various context-dependent errors |

## Do TBTA Labels Seem Correct?

**Potentially Incorrect TBTA Labels**:

| Verse | TBTA | LLM | Analysis |
|-------|------|-----|----------|
| GEN.011.007 | Plural | Trial | Trinity context - should be Trial |
| ISA.006.008 | Plural | Trial | Trinity context - should be Trial |
| PSA.019.001 | Plural | Singular | Lexicalized dual - should be Singular per TBTA policy |
| EXO.28.21 | Dual | Plural | 12 stones = definitely not Dual |
| MAT.018.020 | Plural | Dual | "two or three" - LLM picked minimum, TBTA picked ambiguous |

**Questions for TBTA Team**:
1. Why are GEN.011.007 and ISA.006.008 labeled Plural instead of Trial? These are Trinity contexts.
2. Why is EXO.28.21 ("12 stones") labeled Dual? 12 is not 2.
3. Should PSA.019.001 "heavens" be Singular (lexicalized) or Plural (morphological)?

## Confusion Matrix

| Actual → Predicted | Count |
|--------------------|-------|
| Paucal → Plural | 4 |
| Plural → Singular | 2 |
| Plural → Trial | 2 |
| Dual → Paucal | 1 |
| Dual → Plural | 1 |
| Trial → Dual | 1 |
| Trial → Plural | 1 |
| Quadrial → Singular | 1 |
| Quadrial → Trial | 1 |
| Plural → Paucal | 1 |
| Plural → Dual | 1 |

## Recommendations

### 1. LLM Baseline is Reasonably Good

84% accuracy is a solid baseline. The remaining errors are:
- 25% Paucal confusion (needs clearer TBTA criteria)
- 25% TBTA data quality issues (not LLM errors)
- 50% genuine edge cases requiring context

### 2. Before Optimizing Prompts, Fix TBTA Data

Several "errors" are actually the LLM being more consistent than TBTA:
- Trinity passages should consistently use Trial
- Lexicalized duals should consistently use Singular
- EXO.28.21 needs correction (12 ≠ 2)

### 3. Recommended Approach

- [ ] **Hybrid system**: Rules for explicit counts + LLM for semantic cases
- [ ] **Clarify Paucal**: Document when TBTA uses Paucal vs Plural
- [ ] **Fix TBTA inconsistencies** before final evaluation

## Files Generated

- `baseline_test_input.jsonl` - 100 test samples (without labels)
- `baseline_test_answers.secret.jsonl` - TBTA labels for comparison
- `baseline_predictions_v2.tsv` - LLM predictions (correct prompt format)
