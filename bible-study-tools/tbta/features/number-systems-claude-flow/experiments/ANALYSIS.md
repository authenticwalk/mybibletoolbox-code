# Stage 5A: Pattern Analysis for Number Systems Prediction

**Feature**: Number Systems (Singular, Dual, Trial, Quadrial, Paucal, Plural)
**Dataset**: train.yaml (236 verses)
**Date**: 2025-11-17
**Agent**: Coder (Number Systems)

---

## Training Data Overview

**Total Verses**: 236

**Value Distribution**:
- Dual: 48 verses (20.3%)
- Paucal: 20 verses (8.5%)
- **Plural: 60 verses (25.4%)** ← Baseline candidate
- Quadrial: 8 verses (3.4%)
- **Singular: 60 verses (25.4%)** ← Baseline candidate
- Trial: 40 verses (16.9%)

**Testament Distribution**:
- OT: 69 verses (29.2%) - Heavy in Dual (30), Trial (28)
- NT: 167 verses (70.8%) - Dominated by Singular/Plural epistles

**Genre Patterns**:
- **Epistles**: Almost entirely Singular (55) + Plural (56) - very regular
- **Narrative**: Mixed across all values, highest diversity
- **Prophecy**: Small sample, includes Trial (6), Singular (5), Plural (4)
- **Law**: Small sample, includes Trial (4), Dual (3)
- **Wisdom**: Minimal (2 Dual)

**Arbitrarity Classification**:
- Arbitrary: 228 verses (96.6%)
- **Non-arbitrary: 8 verses (3.4%)** - Includes:
  - GEN.001.026 (Trial, Trinity reference)
  - MAT.018.020 (Trial, "two or three gathered")
  - LUK.010.001 (Dual, sending disciples)
  - LUK.024.013 (Dual, Emmaus road)
  - MRK.006.007 (Dual x2, sending by twos)

---

## Key Insights from Research Materials

### From STAGE3-RESEARCH.md

1. **Greenberg's Universal 34**: Number hierarchy: Singular < Dual < Trial < Quadrial < Paucal < Plural
2. **Austronesian Languages**: Fijian, Tok Pisin, Hawaiian encode trial (3 persons)
3. **Semantic vs Morphological**: Hebrew plural forms don't always mean semantic plurality
4. **Trinity Theology**: Trial number in Gen 1:26 may encode Father/Son/Spirit

### From ARBITRARITY-CLASSIFICATION.md

**Non-arbitrary contexts (HIGH stakes)**:
- **Trinity References** (GEN.001.026, ISA.006.008): Trial vs Plural - doctrinal implications
- **Dual Sending** (MRK.006.007, LUK.010.001): Jesus sends disciples "two by two"
- **Small Group Theology** (MAT.018.020): "Two or three gathered in my name"

**Arbitrary contexts (96.6% of data)**:
- Crowd sizes, group descriptions, narrative participants
- Default: Just describe what's there without theological weight

### From TRANSLATION-DATABASE.md

**Trial-marking languages**: Fijian, Tok Pisin, Hawaiian
**Dual-marking languages**: Samoan, Slovenian
**Paucal-marking languages**: Warlpiri, Bislama

---

## Pattern Analysis: What Predicts Number Values?

### Pattern 1: Explicit Number Words in Text

**Observation**: Many verses likely contain explicit number markers
- "Two" → Dual
- "Three" → Trial
- "Four" → Quadrial
- "A few" → Paucal
- Unmarked groups → Singular or Plural

**Expected Accuracy**: 70-80% (strong when present)
**Limitations**: Not all verses have explicit markers

---

### Pattern 2: Paired Entities (Natural Duals)

**Observation**: Certain entities come in pairs
- Body parts: Eyes, hands, feet, ears → Dual
- Narrative pairs: Two disciples, two witnesses → Dual
- Cultural pairs: Day/night, heaven/earth → Dual (sometimes)

**Expected Accuracy**: 80-90% for body parts, 60-70% for narrative
**Limitations**: Context-dependent, needs semantic understanding

---

### Pattern 3: Trinity Contexts (Theological)

**Observation**: References to Godhead → Trial
- GEN.001.026 "Let US make" → Trial (Father, Son, Spirit)
- ISA.006.008 "Who will go for US?" → Trial
- MAT.028.019 "Father, Son, Holy Spirit" → Trial

**Expected Accuracy**: 90%+ when identifiable
**Limitations**: Requires theological knowledge, rare (only a few verses)

---

### Pattern 4: Small Groups vs Large Crowds

**Observation**: Distinction between paucal (few) and plural (many)
- "A few loaves" → Paucal
- "The multitude" → Plural
- "Several men" → Paucal
- "All the people" → Plural

**Expected Accuracy**: 65-75%
**Limitations**: Fuzzy boundary, context-dependent

---

### Pattern 5: Genre-Based Baseline

**Observation**: Epistles heavily favor Singular + Plural
- Epistle + abstract noun → Singular (95%)
- Epistle + collective noun (church, believers) → Plural (95%)
- Narrative → Requires analysis (mixed)
- Prophecy → Mixed (requires analysis)

**Expected Accuracy**: 90%+ for epistles, 40% for narrative
**Limitations**: Only works for certain genres

---

### Pattern 6: Grammatical Number Markers

**Observation**: Source language morphology (if accessible)
- Hebrew dual ending (-ayim) → Dual
- Greek plural endings → Plural
- Singular morphology → Singular

**Expected Accuracy**: 85-95% if accessible
**Limitations**: Requires source language access (not in our data)

---

### Pattern 7: Participant Tracking (Discourse)

**Observation**: Number depends on referent identity
- Same entity mentioned before → Check first mention number
- "The two" referring back → Dual
- "They" (3 people) → Trial

**Expected Accuracy**: 75-85% with context
**Limitations**: Requires multi-verse context, discourse memory

---

### Pattern 8: Cultural/Idiomatic Patterns

**Observation**: Certain phrases have conventional numbers
- "Two or three" (small gathering) → Trial or Paucal
- "The twelve" (apostles) → Plural
- "The three" (Peter/James/John) → Trial
- "Both" → Dual

**Expected Accuracy**: 80-90% for idioms
**Limitations**: Requires cultural knowledge

---

### Pattern 9: Rarity Principle (Baseline Fallback)

**Observation**: Most common values are Singular (25.4%) and Plural (25.4%)
- When uncertain, predict based on most frequent value
- Genre modifies: Epistles → Singular/Plural; Narrative → All values possible

**Expected Accuracy**: 25-30% (baseline)
**Limitations**: Low accuracy, only use as last resort

---

### Pattern 10: Hierarchical Decision Tree

**Observation**: Combine multiple patterns in priority order
1. Check for Trinity context → Trial
2. Check for explicit number word → Match to value
3. Check for paired entities → Dual
4. Check genre (Epistle) + noun type → Singular/Plural
5. Check for small group markers ("few") → Paucal
6. Default to Plural (more common than Singular in uncertain narrative contexts)

**Expected Accuracy**: 80-90% (combined strength)
**Limitations**: Requires careful rule ordering

---

### Pattern 11: Translation Consensus Discovery

**Observation**: Languages that mark trial/dual/paucal have already solved this
- If Fijian uses trial pronoun → Trial
- If Samoan uses dual → Dual
- If multiple trial-marking languages agree → High confidence

**Expected Accuracy**: 95%+ when translations available
**Limitations**: NO TRANSLATION DATA in our dataset (TO_BE_FETCHED was never fetched)

---

### Pattern 12: Adversarial Pattern (Non-Arbitrary Detection)

**Observation**: 8 verses are non-arbitrary (theological significance)
- First, classify: Arbitrary vs Non-arbitrary
- If Non-arbitrary: Apply theological analysis
- If Arbitrary: Use standard algorithm

**Expected Accuracy**: 95%+ with proper branching
**Limitations**: Requires two-stage prompting

---

## Approach Evaluation & Selection

### Top Tier Approaches (Strong Evidence)

**✅ Approach A: Explicit Number Detection** (Pattern 1)
- **Pros**: Direct textual evidence, high confidence when present
- **Cons**: Not all verses have explicit numbers
- **Use**: Primary detection layer

**✅ Approach B: Trinity Theological Analysis** (Pattern 3)
- **Pros**: Handles non-arbitrary cases with high accuracy
- **Cons**: Very rare (only ~8 verses)
- **Use**: First-priority check for non-arbitrary contexts

**✅ Approach C: Genre + Epistles Pattern** (Pattern 5)
- **Pros**: 90%+ accuracy for epistles (50% of NT data)
- **Cons**: Doesn't help with narrative/prophecy
- **Use**: Strong for epistles, skip for other genres

### Mid Tier Approaches (Moderate Evidence)

**⚠️ Approach D: Paired Entities** (Pattern 2)
- **Pros**: Good for body parts and common pairs
- **Cons**: Context-dependent, unclear boundaries
- **Use**: Secondary check after explicit numbers

**⚠️ Approach E: Small Group vs Crowd** (Pattern 4)
- **Pros**: Helps distinguish paucal from plural
- **Cons**: Fuzzy boundary, subjective
- **Use**: Tertiary check for size contexts

**⚠️ Approach F: Participant Tracking** (Pattern 7)
- **Pros**: High accuracy with discourse context
- **Cons**: Requires multi-verse analysis (complex)
- **Use**: Advanced feature, defer to later iterations

### Low Tier Approaches (Weak/Unavailable)

**❌ Approach G: Translation Consensus** (Pattern 11)
- **Pros**: Would be 95%+ if available
- **Cons**: NO TRANSLATION DATA in our dataset
- **Use**: Cannot use (data unavailable)

**❌ Approach H: Source Language Morphology** (Pattern 6)
- **Pros**: Direct grammatical evidence
- **Cons**: Not in our dataset
- **Use**: Cannot use (data unavailable)

**❌ Approach I: Rarity Baseline** (Pattern 9)
- **Pros**: Always applicable
- **Cons**: Very low accuracy (25-30%)
- **Use**: Last resort fallback only

---

## Recommended Combined Approach for PROMPT1

**Hierarchical Detection Strategy** (combining top patterns):

### Level 1: Non-Arbitrary Detection (Pattern 12 + 3)
```
IF verse is theologically significant:
  - Trinity reference (Gen 1:26, Isa 6:8, Matt 28:19) → Trial
  - "Two or three gathered" (Matt 18:20) → Trial or Paucal
  - Disciples sent "by twos" → Dual
  - Document ramifications
```

### Level 2: Explicit Number Detection (Pattern 1)
```
IF text contains explicit number word:
  - "one" → Singular
  - "two", "both" → Dual
  - "three" → Trial
  - "four" → Quadrial
  - "a few", "several" → Paucal
  - "many", "all", "multitude" → Plural
```

### Level 3: Genre-Specific Rules (Pattern 5)
```
IF genre = epistle:
  IF abstract/singular noun (faith, love, grace) → Singular
  IF collective noun (church, believers, saints) → Plural

IF genre = prophecy:
  Analyze context (mixed patterns)
```

### Level 4: Paired Entities (Pattern 2)
```
IF entity is naturally paired:
  - Body parts (eyes, hands, feet) → Dual
  - Narrative pairs (two disciples, two witnesses) → Dual
  - Cultural pairs (day/night) → Dual
```

### Level 5: Small Group Analysis (Pattern 4)
```
IF group size indicated:
  - "a few", "some" → Paucal
  - "the crowd", "everyone", "all" → Plural
```

### Level 6: Default Fallback
```
IF narrative:
  - Default → Plural (general groups)

IF epistle and uncertain:
  - Default → Singular (abstract concepts)
```

---

## Expected Accuracy Estimate

**Optimistic**: 85-90% (if hierarchical rules work well)
**Realistic**: 75-85% (first iteration, likely refinement needed)
**Pessimistic**: 65-75% (if patterns less reliable than expected)

**Rationale**:
- Epistles (50% of data): 90%+ accuracy (genre pattern very strong)
- Narrative (40% of data): 70-80% accuracy (more complex, varied)
- Non-arbitrary (3% of data): 90%+ accuracy (theological analysis)
- Other genres (7% of data): 60-70% accuracy (mixed patterns)

**Weighted Average**: ~80% accuracy expected for PROMPT1

---

## Next Steps

1. Create `experiments/PROMPT1.md` with the hierarchical approach above
2. Apply PROMPT1 to train_questions.yaml (blind analysis)
3. Generate predictions file
4. **Git commit predictions BEFORE checking answers**
5. Score against train.yaml
6. Analyze errors using 6-step methodology
7. Refine with PROMPT2 if <95% accuracy

---

**Completion Status**: ✅ Analysis Complete
**Created**: 2025-11-17 23:46 UTC
**Next Stage**: Create PROMPT1.md
