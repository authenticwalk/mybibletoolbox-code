# PROMPT1: Hierarchical Number Systems Prediction Algorithm

**Version**: 1.0
**Created**: 2025-11-17
**Feature**: Number Systems (Singular, Dual, Trial, Quadrial, Paucal, Plural)
**Expected Accuracy**: 75-85% (first iteration)

---

## Algorithm Overview

This algorithm uses a **hierarchical decision tree** to predict TBTA number system values based on textual, theological, and contextual cues. It prioritizes explicit evidence over inference, and handles both arbitrary and non-arbitrary contexts.

---

## Decision Hierarchy

Process each verse through these levels in order. **Stop at the first matching rule.**

---

### LEVEL 1: Non-Arbitrary Detection (Theological Significance)

**Purpose**: Identify verses with doctrinal/theological implications

**Rule 1.1: Trinity References**
```
IF verse is:
  - GEN.001.026 ("Let US make mankind in OUR image")
  - ISA.006.008 ("Whom shall I send, and who will go for US?")
  - MAT.028.019 ("baptizing in the name of Father, Son, Holy Spirit")
  - Any verse explicitly mentioning all three persons of Trinity

THEN:
  Predicted value: **Trial**
  Confidence: High
  Rationale: Trinitarian theology - Father, Son, Holy Spirit (three persons, one God)
  Arbitrarity: non-arbitrary
  Theological stakes: HIGH (doctrine of Trinity)
```

**Rule 1.2: "Two or Three Gathered" Theology**
```
IF verse is:
  - MAT.018.020 ("where two or three are gathered in my name")

THEN:
  Predicted value: **Trial** (or possibly Paucal - "two or three" is small group)
  Confidence: Medium-High
  Rationale: Small group theology - Jesus emphasizing minimal gathering size
  Arbitrarity: non-arbitrary
  Theological stakes: MEDIUM (church gathering, corporate worship)

  Note: Context suggests "two or three" as minimum viable church, likely Trial
```

**Rule 1.3: Disciples Sent in Pairs**
```
IF verse describes:
  - Jesus sending disciples "two by two" or "in pairs"
  - MRK.006.007, LUK.010.001 patterns

THEN:
  Predicted value: **Dual**
  Confidence: High
  Rationale: Explicit pairing for mission work (mutual support, witness principle)
  Arbitrarity: non-arbitrary (mission theology pattern)
  Theological stakes: MEDIUM (discipleship practice)
```

**If none of Level 1 rules match, proceed to Level 2.**

---

### LEVEL 2: Explicit Number Detection (Textual Evidence)

**Purpose**: Use explicit number words/phrases in the text

**Rule 2.1: Singular Markers**
```
IF text contains (based on biblical knowledge):
  - "one" (person, thing, etc.)
  - "a" or "an" (singular article context)
  - "himself", "herself", "itself"
  - Singular proper names (Abraham, Moses, Jesus - when alone)

THEN:
  Predicted value: **Singular**
  Confidence: Very High
  Rationale: Explicit singular linguistic marking
```

**Rule 2.2: Dual Markers**
```
IF text contains:
  - "two" (explicitly)
  - "both" (referring to exactly two)
  - "pair" or "couple"
  - "the two" (definite dual reference)

THEN:
  Predicted value: **Dual**
  Confidence: Very High
  Rationale: Explicit dual number marking
```

**Rule 2.3: Trial Markers**
```
IF text contains:
  - "three" (explicitly)
  - "the three" (definite trial reference)
  - "trio" or "triad"

THEN:
  Predicted value: **Trial**
  Confidence: Very High
  Rationale: Explicit trial number marking
```

**Rule 2.4: Quadrial Markers**
```
IF text contains:
  - "four" (explicitly)
  - "the four" (definite reference)
  - "quartet"

THEN:
  Predicted value: **Quadrial**
  Confidence: Very High
  Rationale: Explicit quadrial number marking
```

**Rule 2.5: Paucal Markers**
```
IF text contains:
  - "a few" (explicitly small number >4)
  - "several" (implying small, countable group)
  - "some" (when context suggests small group, not mass)
  - Numbers 5-10 approximately (if mentioned)

THEN:
  Predicted value: **Paucal**
  Confidence: High
  Rationale: Explicit small group marking (more than quadrial, less than plural mass)
```

**Rule 2.6: Plural Markers**
```
IF text contains:
  - "many", "all", "every", "numerous"
  - "multitude", "crowd", "people" (large groups)
  - "they", "them" (when referring to large/indefinite group)
  - Collective nouns: "church", "nations", "believers" (large groups)

THEN:
  Predicted value: **Plural**
  Confidence: High-Very High
  Rationale: Explicit plural/mass marking
```

**If none of Level 2 rules match, proceed to Level 3.**

---

### LEVEL 3: Genre-Specific Patterns

**Purpose**: Epistles have very regular patterns; use genre to constrain

**Rule 3.1: Epistle + Abstract Nouns**
```
IF genre = epistle AND referent is:
  - Abstract theological concept: faith, love, grace, peace, hope, wisdom
  - Spiritual quality: holiness, righteousness, sanctification
  - Doctrinal term: gospel, truth, word

THEN:
  Predicted value: **Singular**
  Confidence: Very High (90%+ for epistles)
  Rationale: Epistles treat abstract concepts as singular entities

Examples: "the faith", "the love of God", "the grace of our Lord"
```

**Rule 3.2: Epistle + Collective Nouns**
```
IF genre = epistle AND referent is:
  - Collective group: church, churches, believers, saints, brothers
  - All-inclusive: "all", "everyone"

THEN:
  Predicted value: **Plural**
  Confidence: Very High (90%+ for epistles)
  Rationale: Epistles address plural communities

Examples: "to the saints", "to all the churches", "the believers"
```

**If genre ≠ epistle OR no match, proceed to Level 4.**

---

### LEVEL 4: Paired Entities (Natural Duals)

**Purpose**: Certain entities naturally come in pairs

**Rule 4.1: Body Parts (Paired)**
```
IF referent is paired body part:
  - eyes, ears, hands, feet, arms, legs, shoulders, kidneys

THEN:
  Predicted value: **Dual**
  Confidence: High (80-90%)
  Rationale: Natural paired anatomy

Note: Check context - "all the eyes of the people" = Plural (many pairs)
      Only mark Dual if specifically "his eyes" or "the two eyes"
```

**Rule 4.2: Narrative Pairs**
```
IF narrative describes:
  - Two specific characters traveling/acting together
  - "The two" as definite reference
  - Paired witnesses (legal contexts)

THEN:
  Predicted value: **Dual**
  Confidence: Medium-High (70-80%)
  Rationale: Narrative pairing pattern

Examples: "the two men", "the two disciples", "the two angels"
```

**If no paired entity detected, proceed to Level 5.**

---

### LEVEL 5: Small Group vs Large Group

**Purpose**: Distinguish paucal (few) from plural (many)

**Rule 5.1: Small Group Indicators**
```
IF context suggests small, countable group:
  - "few" (without explicit number)
  - "some people" (small subset)
  - Specific small group: "the leaders", "the elders" (if <10 implied)

THEN:
  Predicted value: **Paucal**
  Confidence: Medium (65-75%)
  Rationale: Small group semantics
```

**Rule 5.2: Large Group/Crowd Indicators**
```
IF context suggests large, uncountable group:
  - "the multitude", "the crowd"
  - "all the people", "everyone"
  - "many came", "a great number"

THEN:
  Predicted value: **Plural**
  Confidence: High (80-90%)
  Rationale: Mass/crowd semantics
```

**If still unclear, proceed to Level 6 (fallback).**

---

### LEVEL 6: Default Fallback (Genre-Based)

**Purpose**: When all else fails, use most likely default based on genre

**Rule 6.1: Narrative Default**
```
IF genre = narrative:
  Default: **Plural**
  Confidence: Low (baseline)
  Rationale: Narrative often involves groups/participants; plural more common than singular in uncertain contexts
```

**Rule 6.2: Epistle Default**
```
IF genre = epistle:
  Default: **Singular** (if abstract/theological topic)
  Default: **Plural** (if addressing audience)
  Confidence: Low (baseline)
  Rationale: Epistles alternate between singular concepts and plural audiences
```

**Rule 6.3: Prophecy/Wisdom Default**
```
IF genre = prophecy OR wisdom:
  Default: **Singular** (if symbolic/abstract)
  Default: **Plural** (if addressing nations/people)
  Confidence: Very Low (baseline)
  Rationale: Mixed patterns in these genres
```

---

## Application Instructions

For each verse in train_questions.yaml:

1. **Read the verse reference** (e.g., GEN.001.026)
2. **Use biblical knowledge** to recall the verse content and context
3. **Apply the decision tree** from Level 1 → Level 6 in order
4. **Stop at first matching rule** and record:
   - Predicted value
   - Confidence level
   - Rationale
   - Which rule/level was applied
5. **Mark non-arbitrary** if Level 1 rule matched
6. **Never look at train.yaml answers** until predictions are locked

---

## Output Format

For each verse, record:

```yaml
reference: "GEN.001.026"
predicted_value: "Trial"
confidence: "High"
rule_applied: "Level 1, Rule 1.1 (Trinity Reference)"
rationale: "Let us make mankind - Trinitarian theology (Father, Son, Spirit)"
arbitrarity: "non-arbitrary"
theological_stakes: "HIGH"
```

---

## Known Limitations

1. **No translation data**: Cannot use Fijian/Samoan/Hawaiian evidence (would be 95%+ if available)
2. **No source language morphology**: Cannot check Hebrew dual endings, Greek plural forms
3. **Single verse context**: Cannot track participants across verses (discourse analysis)
4. **Biblical knowledge dependency**: Relies on LLM's training data about Bible content
5. **First iteration**: Expected 75-85% accuracy; will need refinement

---

## Confidence Calibration

- **Very High**: Explicit textual markers (Level 2), 90%+ expected accuracy
- **High**: Theological/genre patterns (Level 1, 3, 4), 80-90% expected accuracy
- **Medium**: Contextual inference (Level 5), 65-75% expected accuracy
- **Low**: Fallback defaults (Level 6), 30-50% expected accuracy

---

## Next Steps After Prediction

1. Apply this prompt to all 236 verses in train_questions.yaml
2. Generate predictions file: `train_predictions_v1.yaml`
3. **Git commit predictions BEFORE checking answers**
4. Score against train.yaml
5. Analyze errors using 6-step methodology
6. Refine prompt based on error patterns

---

**Status**: ✅ Ready for Application
**Expected Completion**: 2-3 hours to manually apply to 236 verses
**Next File**: `train_predictions_v1.yaml`
