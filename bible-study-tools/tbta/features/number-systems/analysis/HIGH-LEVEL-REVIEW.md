# Number Systems: LLM Baseline Analysis

**Date**: 2025-11-26
**Dataset**: 100 samples from train.jsonl (stratified by label)
**Accuracy**: 76/100 (76.0%)

## Baseline Prompt Used

```
Classify each highlighted word into: Singular, Dual, Trial, Quadrial, Paucal, Plural

Key Guidelines:
1. Count matters: If text explicitly states a count (2, 3, 4), use that number category
2. Trinity references: God saying "us/our" → Trial
3. Pairs: Eyes, ears, two people → Dual
4. Small groups explicitly named: 3 disciples → Trial
5. Large/unspecified groups: nations, peoples → Plural
6. Single entities even if morphologically plural: "heavens" → Singular
```

## Key Findings

### 1. Major Error Pattern: Paucal → Plural (10 errors, 41.7% of all errors)

The LLM consistently fails to use "Paucal" (few items, 3-10) when TBTA does.

**Examples**:
- LUK.005.019: "man could not enter house" → TBTA: Paucal, LLM: Plural
- MAT.025.021: "master entrust thing" → TBTA: Paucal, LLM: Plural
- LUK.008.013: "believe for month" → TBTA: Paucal, LLM: Plural

**Analysis**: TBTA uses Paucal semantically for "a few" even when the exact number isn't specified. The LLM defaults to Plural for unspecified plurals.

**Recommendation**: Paucal requires clearer guidance on when to use it vs Plural. TBTA seems to use Paucal when context implies "not many" without giving a specific count.

### 2. Quadrial → Plural (3 errors)

**Examples**:
- EXO.025.027: "Moses put ring near top table" → TBTA: Quadrial, LLM: Plural
- 1SA.016.010: "Samuel say Yahweh choose man" → TBTA: Quadrial, LLM: Plural
- LUK.009.028: "man go-up mountain to pray" → TBTA: Quadrial, LLM: Plural

**Analysis**: These cases where TBTA uses Quadrial (4) may be counting from broader context not visible in the snippet. LUK.009.028 is the Transfiguration with Peter, James, John + Jesus = 4 people.

**Issue**: Quadrial has no linguistic attestation (Corbett 2000). TBTA uses it semantically but the LLM correctly questions whether a true grammatical quadrial exists.

### 3. Trinity Passages: Mixed Results

**Correct**:
- GEN.011.007 "let us go down" → LLM: Trial (but TBTA says Plural!)
- ISA.006.008 "who will go for us" → LLM: Trial (but TBTA says Plural!)

**TBTA Inconsistency Discovered**:
- GEN.001.026: TBTA marks different constituents differently (some Trial, some Plural, some Singular)
- The LLM consistently uses Trial for Trinity "us" passages, but TBTA sometimes uses Plural

**Key Question for TBTA Team**: Why is GEN.011.007 "us" marked as Plural rather than Trial? Is this a data quality issue or intentional?

### 4. Dual Confusion

**Examples**:
- MAT.26.037: "Peter and 2 sons Zebedee disciple" → TBTA: Trial, LLM: Dual
  - Issue: "2 sons" + Peter = 3 people (Trial), but LLM focused on "2 sons"
- EXO.28.21: "12 stone according 12 tribes" → TBTA: Dual (!), LLM: Plural
  - Issue: 12 is definitely not Dual. TBTA labeling seems wrong here.

### 5. Do TBTA Labels Seem Correct?

**Potentially Incorrect TBTA Labels**:

| Verse | Constituent | TBTA Label | Expected | Issue |
|-------|-------------|------------|----------|-------|
| EXO.28.21 | stone | Dual | Plural | 12 stones = not dual |
| GEN.011.007 | we | Plural | Trial | Trinity context |
| ISA.006.008 | us | Plural | Trial | Trinity context |
| PSA.019.001 | heavens | Plural | Singular | Lexicalized dual should be Singular per TBTA policy |

**Possibly Correct but Needs Clarification**:

| Verse | Constituent | TBTA Label | LLM | Analysis |
|-------|-------------|------------|-----|----------|
| MAT.18.020 | person | Dual | Paucal | "2 or 3" - TBTA chose minimum |
| LUK.005.019 | man | Paucal | Plural | "Men" carrying paralytic - ~4 people |

### 6. Confusion Matrix Summary

| Actual → Predicted | Count | Analysis |
|--------------------|-------|----------|
| Paucal → Plural | 10 | LLM doesn't know when to use Paucal |
| Quadrial → Plural | 3 | No natural language has Quadrial |
| Plural → Singular | 2 | Collective nouns confusion |
| Plural → Trial | 2 | LLM over-applies Trinity rule |
| Trial → Plural | 2 | Context not clear in snippet |
| Other | 5 | Various edge cases |

## Recommendations

### For Improving LLM Accuracy:

1. **Paucal Training**: Add explicit rules for when Paucal applies (numbers 3-10, words like "few", "some")
2. **Quadrial Handling**: Either train on TBTA's semantic use OR document that Quadrial is non-linguistic
3. **Trinity Consistency**: Clarify whether Trinity passages should be Trial or Plural

### TBTA Data Quality Issues:

1. **Verify EXO.28.21**: 12 stones marked as Dual seems incorrect
2. **Review Genesis Trinity passages**: Inconsistent labeling (some Trial, some Plural)
3. **Document Paucal usage policy**: When is "few" few enough for Paucal?

## Should We Continue?

**No** - We cannot achieve high accuracy without:
1. Resolving TBTA data quality issues
2. Getting clearer Paucal/Quadrial guidelines
3. Consistent Trinity passage labeling

**Recommendation**: Proceed to Step 3 analyses to identify patterns and data quality issues before optimizing prompts.

## Files Generated

- `baseline_test_input.jsonl` - 100 test samples (without labels)
- `baseline_test_answers.secret.jsonl` - TBTA labels for comparison
- `baseline_predictions.tsv` - LLM predictions
