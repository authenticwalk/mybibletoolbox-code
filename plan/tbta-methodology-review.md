# TBTA LLM Reproduction - Methodology Review

**Date**: 2025-11-06
**Reviewer**: Claude (Sonnet 4.5)
**Status**: In Progress

## Critical Issue Identified

The TBTA LLM reproduction plan contains a **fundamental methodology error**: Some feature documentation describes extracting/reading TBTA labels directly rather than predicting them independently.

### The Problem

**What we're trying to do**: Build a system that can PREDICT TBTA-style linguistic annotations for any Bible verse WITHOUT looking at existing TBTA labels.

**What some files are doing**: Describing how to EXTRACT features that are already labeled in TBTA data structures.

### Examples of the Problem

#### PROBLEM: Direct Extraction (Cheating)

File: `features/verb-tam/mood-mood_identification_method.md`

**Line 1-5**: "This document describes the proven method for identifying mood values from TBTA data structures. Based on testing with Matthew 24 (316 verbs, 100% accuracy on test cases)."

**What this does**:
```python
# This is just reading the answer key!
for clause in verse_data['clauses']:
    for element in clause['children']:
        if element['Part'] == 'VP':
            mood = child['Mood']  # <-- READING TBTA's LABEL
```

**Why this is wrong**: Of course you get 100% accuracy when you're just copying TBTA's existing labels! This doesn't prove we can predict these features independently.

#### PROBLEM: Claiming 100% accuracy on features that are just extracted

Multiple files claim "100% accuracy" on features that are directly extracted from TBTA:
- `mood-mood_identification_method.md`: "100% accuracy on test cases" - but it's just reading the Mood field
- `features/07-phrasal-elements/README.md`: "Explicit in TBTA data (direct extraction, 100% accuracy)"
- Multiple participant-tracking claims of 100% accuracy

### Correct Methodology

#### CORRECT: Independent Prediction + Validation

File: `features/number-systems/experiment-001.md`

**Line 28**: "MY PREDICTIONS (BEFORE CHECKING TBTA):"

**What this does**:
1. Analyzes the verse semantically and morphologically
2. Makes a prediction about number (Singular/Dual/Plural/etc.)
3. THEN compares with TBTA to validate accuracy
4. Documents mismatches and learns from them

**Why this is correct**: We're actually predicting the feature, not just reading it. TBTA data is used ONLY for validation.

## Correct Use of TBTA Data

### Allowed Uses

1. **Training/Learning**: Examine TBTA examples to understand feature patterns
2. **Validation**: Compare predictions against TBTA labels to measure accuracy
3. **Error Analysis**: When predictions differ from TBTA, analyze why
4. **Test Set Creation**: Select verses that have TBTA labels for testing

### Forbidden Uses

1. **Direct Extraction**: Reading TBTA feature labels and claiming this as "reproduction"
2. **Feature Completion**: Using TBTA labels to fill in predictions
3. **Accuracy Inflation**: Claiming high accuracy by extracting rather than predicting
4. **Answer Peeking**: Looking at TBTA labels before making predictions

## Data Sources We CAN Use for Prediction

### Allowed Inputs (Not Cheating)

1. **Source Text**: Hebrew, Aramaic, Greek biblical texts with morphology
2. **Translations**: 900+ translations in translations-ebible.yaml
3. **Dictionaries**: Strong's, lexicons, semantic databases
4. **Grammars**: Language family grammars, typological patterns
5. **Linguistic Theory**: Semantic frameworks, discourse patterns
6. **Context**: Surrounding verses, discourse structure, genre
7. **Theological Knowledge**: Doctrinal patterns (Trinity, divine speech, etc.)

### Workflow

```
1. READ: Source text (Hebrew/Greek) + translations + context
2. ANALYZE: Apply linguistic/semantic/theological reasoning
3. PREDICT: Generate feature label (e.g., "Mood: Indicative")
4. VALIDATE: Compare with TBTA label
5. LEARN: If mismatch, improve prediction method
6. ITERATE: Refine prompts and context
```

## Files Requiring Correction

### Files with Direct Extraction Problems

1. **features/verb-tam/mood-mood_identification_method.md**
   - Problem: Describes extracting Mood from TBTA VP nodes
   - Fix: Rewrite to describe predicting mood from Greek morphology + semantics
   - Keep: Validation section comparing predictions to TBTA

2. **features/verb-tam/aspect-aspect_identification_method.md**
   - Problem: Similar extraction approach
   - Fix: Describe prediction from Greek tense-aspect patterns

3. **features/07-phrasal-elements/README.md**
   - Problem: Claims "direct extraction, 100% accuracy"
   - Fix: If these are actually predictable, describe the prediction method
   - Alternative: If they're truly just in TBTA structure, note this as metadata, not features to reproduce

### Files with Inflated Accuracy Claims

Search for claims like:
- "100% accuracy" when it's extraction, not prediction
- "TBTA has covered this 80% of the time" - implies using TBTA coverage as input
- "This feature is in TBTA data so can be completed with 100% accuracy" - wrong approach

### Files That Are Correct

1. **features/number-systems/experiment-001.md**
   - ✅ Makes predictions before checking TBTA
   - ✅ Uses semantic + morphological analysis
   - ✅ Documents uncertainties
   - ✅ Validates against TBTA afterward

2. **features/person-systems/clusivity/\*.md**
   - ✅ Analyzes translations to determine clusivity
   - ✅ Uses TBTA only for final validation
   - ✅ Shows reasoning process

## Action Plan

### Step 1: Audit All Feature Files

- [ ] Review each feature README and experiment file
- [ ] Flag files that describe extraction vs prediction
- [ ] Document which files are correct

### Step 2: Rewrite Extraction Files

For each file describing extraction:

1. **Add "Prediction Methodology" section**:
   - How to determine this feature from source text
   - What linguistic/semantic/contextual cues to use
   - Decision trees for ambiguous cases

2. **Rename "Extraction Method" to "Validation Method"**:
   - Keep the TBTA structure knowledge for validation
   - But clarify this is for checking predictions, not generating them

3. **Add "Prediction Workflow" examples**:
   - Show worked examples of making predictions
   - Before/after comparisons
   - Error analysis when predictions differ from TBTA

### Step 3: Correct Accuracy Claims

1. **Remove inflated accuracy claims**:
   - "100% accuracy" from extraction → Remove or clarify as "validation accuracy"
   - Add honest accuracy from actual prediction experiments

2. **Add confidence levels**:
   - High confidence (80-95%): Features with clear linguistic patterns
   - Medium confidence (60-80%): Features requiring semantic interpretation
   - Low confidence (<60%): Features with high ambiguity

3. **Genre-specific accuracy**:
   - Don't claim "100% overall" - specify by genre
   - Note where prediction methods work better or worse

### Step 4: Clarify Proper Goal

Update README.md and PLAN.md to emphasize:

**GOAL**: Build prediction methods that can:
1. Take Hebrew/Greek/English text + translations
2. Apply linguistic/semantic/theological reasoning
3. Generate TBTA-style annotations
4. WITHOUT looking at existing TBTA labels (except for training/validation)

**SUCCESS METRIC**: Accuracy when predicting labels on verses we haven't seen before, compared to TBTA's human-annotated labels.

## Updated Methodology Statement

### What We're Building

**NOT**: A parser that extracts features already labeled in TBTA data
**YES**: A prediction system that can label any Bible verse using:
- Prompt engineering (detailed linguistic instructions)
- Context engineering (translations showing how features are realized)
- Semantic reasoning (understanding meaning, not just morphology)
- Theological reasoning (understanding divine vs human patterns)

### Resources We Use

**For Prediction**:
- Source language morphology (Greek/Hebrew parsing)
- 900+ translations (showing feature realization across languages)
- Linguistic theory (semantic patterns, discourse rules)
- Genre patterns (narrative vs poetry vs prophecy)
- Theological context (divine speech, prayer, doctrinal implications)

**For Validation Only**:
- TBTA human-labeled data (compare our predictions to verify accuracy)
- Error analysis (learn from mismatches to improve prompts)
- Coverage analysis (which verses/features TBTA has labeled)

## Skepticism Checklist

When reviewing any accuracy claim, ask:

1. **Is this actually predicting or just extracting?**
   - If it reads a TBTA field, it's extraction, not prediction

2. **Can I see the prediction methodology?**
   - What inputs are used (excluding TBTA labels)?
   - What reasoning process generates the prediction?
   - Are there worked examples?

3. **Is the accuracy claim validated?**
   - Tested on held-out verses not used in development?
   - Accuracy reported by genre, not just overall?
   - Sample size sufficient for the claim?

4. **Are failure cases documented?**
   - What patterns cause errors?
   - Are edge cases identified?
   - Is there honest uncertainty quantification?

## Next Steps

1. ✅ Create this review document
2. [ ] Audit all feature files systematically
3. [ ] Rewrite problematic "extraction" files
4. [ ] Remove/correct inflated accuracy claims
5. [ ] Add clear prediction methodologies
6. [ ] Update README with corrected goals
7. [ ] Commit changes with clear explanation

---

**Key Takeaway**: We're trying to PREDICT features using linguistic reasoning and translations, with TBTA as the answer key for validation. We're NOT just reading TBTA's existing labels and calling that "reproduction."
