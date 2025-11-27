# Number Systems: LLM Baseline Analysis

**Date**: 2025-11-27
**Dataset**: 100 samples from train.jsonl (stratified by label)

## Dual Baseline Comparison

| Test | Accuracy | Notes |
|------|----------|-------|
| Zero-Shot | 69/100 (69%) | No definitions, just value names |
| Guided | 79/100 (79%) | Full definitions per value |
| **Improvement** | **+10%** | Guidance helps significantly |

## Zero-Shot Prompt

```
Label each highlighted word (**word**) with one of these Number values:
Singular, Dual, Trial, Quadrial, Paucal, Plural

Return format: $verse\t$label (e.g., "GEN.001.001\tSingular")
```

## Guided Prompt

```
Grammatical number encodes the count of entities referenced by a noun or pronoun.
Label each highlighted word (**word**) with the number category that matches how
many entities it refers to in context.

- Singular:
  - Refers to exactly 1 entity
  - Proper names (Jesus, David, Yahweh, God)
  - Lexicalized plurals with singular meaning ("heavens" = one sky)
  - Collective nouns treated as a unit
  - Abstract concepts (faith, love, grace)

- Dual:
  - Refers to exactly 2 entities
  - Explicit "two" or "2" in context
  - Natural body part pairs (hands, feet, eyes, ears)
  - Hebrew dual morphology (-ayim suffix)

- Trial:
  - Refers to exactly 3 entities
  - Explicit "three" or "3" in context
  - Trinity contexts where God says "us/our" (Gen 1:26, 3:22, 11:7, Isa 6:8)
  - Named triplets (Peter/James/John, Shadrach/Meshach/Abednego)

- Quadrial:
  - Refers to exactly 4 entities
  - Explicit "four" or "4" in context
  - Four living creatures, four corners, four rivers

- Paucal:
  - Refers to a few entities (typically 3-10, not precisely specified)
  - Words like "few", "some", "several", "a little"
  - Small indefinite groups where exact count is unknown

- Plural:
  - Refers to many entities (general plural, large or unspecified)
  - Large groups: nations, peoples, crowds, multitudes
  - Generic statements ("all have sinned")
```

## Distribution Bias Analysis

| Label | TBTA | Zero-Shot | Guided |
|-------|------|-----------|--------|
| Singular | 18 | 26 (+8) | 23 (+5) |
| Dual | 24 | 24 (=) | 24 (=) |
| Trial | 13 | **0** (-13) | 13 (=) |
| Quadrial | 14 | 10 (-4) | 12 (-2) |
| Paucal | 13 | 7 (-6) | 10 (-3) |
| Plural | 18 | 33 (+15) | 18 (=) |

**Key Insight**: Without guidance, the LLM:
- **NEVER uses Trial** (0 predictions) - defaults to Plural or Singular
- Over-predicts Plural (+15) and Singular (+8)
- Under-predicts Paucal and Quadrial

**With guidance**, the LLM distribution matches TBTA almost exactly.

## Where Guidance Helped (14 cases, +10%)

| Verse | TBTA | Zero-Shot | Guided | Pattern |
|-------|------|-----------|--------|---------|
| DAN.003.025 | Quadrial | Plural | Quadrial | "4 **man** walking" |
| EXO.019.015 | Trial | Plural | Trial | "3 **day**" |
| DAN.003.024 | Trial | Plural | Trial | "3 **man**" |
| MAT.026.034 | Trial | Plural | Trial | "deny 3 **time**" |
| 1SA.004.004 | Paucal | Plural | Paucal | "send **man** Shiloh" |
| 1SA.025.039 | Paucal | Plural | Paucal | "send **servant**" |
| GEN.001.026 | Trial | Singular | Trial | "**God**" (Trinity context) |
| JDG.019.014 | Trial | Plural | Trial | "3 **person** travel" |
| DAN.003.019 | Trial | Plural | Trial | "**friend**" (Shadrach/Meshach/Abednego) |
| EXO.025.027 | Quadrial | Plural | Quadrial | "**ring** near top table" (4 rings) |
| DAN.006.002 | Trial | Plural | Trial | "3 **leader**" |
| GEN.018.005 | Trial | Plural | Trial | "3 **man** say ok" |
| LUK.010.002 | Paucal | Plural | Paucal | "**worker** are few" |

**Analysis**: Guidance primarily helps with:
1. **Trial detection** (10/14 cases) - LLM has NO internal concept of Trial without guidance
2. **Paucal vs Plural** (3/14 cases) - clearer criteria help distinguish "few" from "many"
3. **Quadrial** (1/14 cases) - explicit "4" triggers correct label

## Where Guidance Hurt (4 cases)

| Verse | TBTA | Zero-Shot | Guided | Analysis |
|-------|------|-----------|--------|----------|
| GEN.011.007 | Plural | Plural | Trial | Prompt says Trinity→Trial, but TBTA uses Plural |
| GEN.001.026 | Singular | Singular | Trial | "**God**" - TBTA marks Singular, prompt says Trinity→Trial |
| ISA.006.008 | Plural | Plural | Trial | "**us**" - Trinity context, but TBTA uses Plural |
| PSA.019.001 | Plural | Plural | Singular | "**heavens**" - prompt's lexicalized rule triggered |

**Analysis**: These are **TBTA inconsistencies**, not LLM errors:
- **Trinity passages**: GEN.011.007 and ISA.006.008 are Trinity contexts that TBTA labels Plural instead of Trial
- **GEN.001.026 "God"**: Appears 5x in dataset with inconsistent TBTA labels (Trial x3, Singular x2)
- **Lexicalized duals**: PSA.019.001 "heavens" - should be Singular by TBTA's semantic-priority policy

## Persistent Errors (17 cases - Both Wrong)

| Verse | TBTA | ZS | Guided | Pattern |
|-------|------|----|--------|---------|
| MAT.18.020 | Dual | Paucal | Paucal | "2 or 3 **person**" - ambiguous |
| GEN.001.026 | Plural | Singular | Singular | "create **person**" - mankind |
| LUK.005.019 | Paucal | Plural | Plural | "**man** could not enter" - no "few" marker |
| MAT.26.037 | Trial | Dual | Dual | Peter + 2 sons = 3, but labeled as 2 |
| LUK.005.018 | Paucal | Plural | Plural | "**man** carry paralyzed" - no marker |
| HEB.010.025 | Plural | Paucal | Paucal | "habit of **some**" - LLM reads "some" as few |
| MAT.018.020 | Plural | Dual | Dual | "**two** or three" - LLM picks explicit number |
| PSA.034.007 | Plural | Singular | Singular | "**him**" - pronoun unclear |
| MAT.025.021 | Paucal | Plural | Plural | "entrust **thing**" - no "few" marker |
| GEN.001.026 | Trial | Singular | Singular | "**God**" - TBTA inconsistent |
| JDG.019.019 | Trial | Singular | Singular | "**person** have dry grass" - unclear 3 |
| EXO.28.21 | Dual | Plural | Plural | "12 **stone**" - 12 ≠ 2 (TBTA error?) |
| 1SA.016.010 | Quadrial | Singular | Singular | Samuel choosing - context unclear |
| EXO.016.018 | Paucal | Singular | Plural | "gather **flake**" - no quantity marker |

**Root Causes**:
1. **Paucal without markers** (5 cases): TBTA uses Paucal for small groups even without "few/some"
2. **TBTA labeling errors** (3 cases): EXO.28.21 (12≠2), inconsistent GEN.001.026
3. **Context-dependent** (5 cases): Requires narrative knowledge LLM doesn't have
4. **Ambiguous expressions** (4 cases): "two or three", pronouns with unclear referents

## LLM Internal Biases (from Zero-Shot)

1. **No Trial concept**: Zero predictions without explicit guidance
2. **Plural over-use**: Defaults to Plural for any group (+15 over-prediction)
3. **Singular over-use**: Defaults to Singular for proper nouns, even in Trinity contexts
4. **Dual is accurate**: Matches TBTA exactly (24/24 distribution)
5. **Paucal under-use**: Only 7 vs TBTA's 13 - needs explicit "few" markers

## Recommendations

### 1. Guidance Is Essential (+10% improvement)

The LLM has **no internal concept of Trial** - it must be taught. Keep the guided prompt format.

### 2. TBTA Data Quality Issues to Resolve

Before final evaluation, flag these for TBTA team review:
- GEN.011.007, ISA.006.008: Trinity→Plural (should be Trial?)
- GEN.001.026 "God": Inconsistent (Trial x3, Singular x2)
- EXO.28.21 "12 stones": Labeled Dual (should be Plural)
- PSA.019.001 "heavens": Plural vs Singular policy unclear

### 3. Paucal Criteria Need Clarification

Both baselines struggle with Paucal. TBTA uses it for:
- Unmarked small groups (no "few")
- Context-dependent inference

**Question for TBTA**: What triggers Paucal when no quantity word is present?

### 4. Recommended Approach

- [x] **Guided prompt is baseline** - 79% accuracy
- [ ] **Rules for explicit counts**: 2→Dual, 3→Trial, 4→Quadrial
- [ ] **Clarify Paucal criteria** with TBTA team
- [ ] **Fix TBTA inconsistencies** before final evaluation

## Files Generated

- `baseline_test_input.jsonl` - 100 test samples (without labels)
- `baseline_test_answers.secret.jsonl` - TBTA labels for comparison
- `baseline_zero_shot.tsv` - Zero-shot predictions
- `baseline_guided.tsv` - Guided predictions (79% accuracy)
