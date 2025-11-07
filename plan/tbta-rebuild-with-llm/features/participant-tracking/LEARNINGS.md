# Participant Tracking: Implementation Guide

**Date**: 2025-11-05
**Feature**: Noun Participant Tracking
**TBTA States**: 9 defined, 5 actively used
**Data Analyzed**: 171,875 annotations from TBTA database export

---

## Executive Summary

Participant tracking can be reproduced with **high accuracy (estimated 85-90%)** using:
1. Coreference resolution
2. Referential distance calculation
3. Frame semantics / FrameNet integration
4. Generic reference detection
5. Interrogative clause identification

**Key Insight**: Only 5 states are actively needed for Biblical text (Routine, Generic, Frame Inferable, First Mention, Interrogative). The other 4 states are theoretical or extremely rare.

---

## 5-State Simplified System

### State 1: ROUTINE (73% of cases)
**When to use**: Referent mentioned in last 1-3 clauses with low competing referents

**LLM Detection Prompt**:
```
For this referent, ask yourself:
1. "Was this referent mentioned recently (within last 1-3 clauses)?"
2. "Are there few competing referents between mentions?"
3. "Is this referent maintaining continuous presence in the discourse?"

If YES to all three → Label as ROUTINE

Reasoning: Apply Givón's continuity principle - continuous topics require
minimal linguistic marking. This referent is "in focus" per Gundel's
hierarchy, maintaining high accessibility per Ariel's scale.
```

**Surface forms**: Pronouns (he, she, it, they), zero anaphora in pro-drop languages

---

### State 2: GENERIC (14% of cases)
**When to use**: Reference to types/classes, not specific individuals; timeless statements

**Indicators**:
- Timeless present tense ("Lions are dangerous")
- Habitual aspect ("A man goes to work daily")
- Definitions ("Water is H₂O")
- Bare plurals in English ("Dogs bark")
- Proverbs/wisdom statements

**Common in**: Wisdom literature, teaching passages, parables

---

### State 3: FRAME INFERABLE (7.5% of cases)
**When to use**: First occurrence BUT inferable from established scene/frame

**Key test**: Definite article on first mention
- "John went to a restaurant. **The waiter** was rude."
- "In the beginning God created **the heavens** and **the earth**."

**Requires**: Frame/scene database
- Restaurant → waiter, menu, food, bill
- Market → vendors, goods, prices
- Well → water, bucket, rope
- Creation → heaven, earth, light, darkness
- Temple → altar, priest, sacrifice

---

### State 4: FIRST MENTION (5.4% of cases)
**When to use**: Truly new referent, not inferable from frame

**Surface forms**:
- Indefinite article in English ("a woman")
- Existential constructions ("there was a man")
- Full noun phrases with no prior context

---

### State 5: INTERROGATIVE (0.2% of cases)
**When to use**: Referent in interrogative clause querying identity/properties

**Indicators**:
- Wh-words: who, what, which, whom, whose
- Question context
- Only for the questioned referent, not all referents in a question

---

## Rare/Theoretical States (Not Needed for Initial Implementation)

**RESTAGING** (0% in data): Participant returns after 4+ clause absence with high interference
**OFFSTAGE** (1 instance total): "Samaritan" in John 4:7 modifying "woman"
**INTEGRATION** (0% in data): Theoretical only
**EXITING** (0% in data): Theoretical only

---

## LLM Prediction Workflow

### Phase 1: Minimum Viable System (3 States - 92.4% coverage)
Focus on: Routine (73%), Generic (14%), First Mention (5.4%)

**LLM Prompting**:
```
For each nominal constituent in this passage, determine its
participant tracking state using these steps:

STEP 1: Check if GENERIC
Ask: Is this a timeless statement about types/classes?
Look for: bare plurals, habitual aspect, definitional contexts
If YES → Label: GENERIC

STEP 2: Check if FIRST MENTION (for non-generic referents)
Ask: Is this the first occurrence in the discourse?
Look for: indefinite article, new participant introduction
If YES → Label: FIRST MENTION

STEP 3: Default to ROUTINE (for previously mentioned)
Ask: Has this referent appeared before?
Look for: pronouns, repeated nouns, continued reference
If YES → Label: ROUTINE
```

### Phase 2: Add Frame Inferability (4 States - 99.9% coverage)
Add Frame Inferable (7.5%)

**Enhanced Prompting**:
```
STEP 2: For first occurrences, check FRAME INFERABILITY
Ask yourself:
- 'What frame/scene has been established in prior context?'
- 'Is this referent a typical participant in that frame?'
- 'Does the text use definite marking despite first mention?'

Common Biblical frames:
- Temple frame (altar, priest, sacrifice, incense)
- Well frame (water, bucket, rope)
- Market frame (vendor, goods, prices)
- Creation frame (heaven, earth, light, darkness)
- Household frame (master, servant, goods, authority)

If frame is active AND referent belongs to it → FRAME INFERABLE
If no frame connection → FIRST MENTION
```

### Phase 3: Add Interrogatives (5 States - 100% coverage)
Add Interrogative (0.2%)

**Complete Prompting**:
```
STEP 0: Check if INTERROGATIVE
Ask: Is this referent in a question querying identity/properties?
Look for: wh-words (who, what, which, whom, whose)
→ If YES: INTERROGATIVE (only for the queried referent itself)
```

---

## Key Dependencies

### 1. Coreference Resolution
Identify when different mentions refer to same entity
- Pronouns → antecedents
- Synonyms ("the woman" = "the Samaritan")
- Name variants ("Jesus" = "He" = "the Nazarene")

**Tools**: SpaCy, CoreNLP, or build referent chains

---

### 2. Referential Distance (RD)
Count clauses between mentions of same referent

**Formula**: RD = current_clause_number - last_mention_clause_number

**Usage**:
- RD = 1-2 → Routine
- RD = 3+ → Consider Restaging (rarely needed)

---

### 3. Frame Semantics Database
Map frame-evoking words to expected participants

**Example frames**:
```yaml
restaurant:
  evoking_words: [restaurant, cafe, diner, eatery]
  participants: [waiter, waitress, server, menu, food, table, bill, cook, chef]

well:
  evoking_words: [well, spring, cistern]
  participants: [water, bucket, rope, draw]

temple:
  evoking_words: [temple, sanctuary, tabernacle, altar]
  participants: [priest, sacrifice, offering, altar, incense, holy]

creation:
  evoking_words: [beginning, create, creation]
  participants: [heaven, earth, sky, light, darkness, land, sea]
```

**Sources**: FrameNet, manual curation for Biblical frames

---

### 4. Generic Reference Detection
Identify non-specific, type-level reference

**Syntactic indicators**:
- Bare plurals in English
- Generic singular with definite article
- Timeless present tense

**Semantic indicators**:
- Habitual aspect
- Definitional statements
- Universal quantifiers (all, every, any)
- Proverbs

**Challenge**: Context-dependent ("The water is essential" vs "The water is cold")

---

## Validation Approach

### Test 1: Frequency Distribution
**TBTA Baseline**:
- Routine: 73.0%
- Generic: 13.9%
- Frame Inferable: 7.5%
- First Mention: 5.4%
- Interrogative: 0.2%

**Acceptable ranges** (based on narrative text):
- Routine: 60-80%
- Generic: 5-20% (genre-dependent)
- Frame Inferable: 5-10%
- First Mention: 3-8%
- Interrogative: 0-2%

---

### Test 2: Surface Form Consistency

| State | Expected Surface | Problem if... |
|-------|-----------------|---------------|
| First Mention | Indefinite NP ("a woman") | Pronoun ("she") |
| Routine | Pronoun, zero, or repeated NP | Indefinite NP |
| Frame Inferable | **Definite** NP on first mention | Indefinite article |
| Generic | Bare plural, generic singular | Specific demonstrative |

---

### Test 3: Referent Chain Continuity

**Valid patterns**:
1. First Mention → Routine → Routine → Routine
2. Frame Inferable → Routine → Routine
3. First Mention → Routine → [gap] → Restaging → Routine

**Invalid patterns**:
1. Routine → First Mention (can't be routine if never mentioned!)
2. Generic → Routine (generic refs don't become specific tracked participants)

---

### Test 4: Frame Consistency

**For each Frame Inferable**:
1. Look back in context for frame-evoking word
2. Check if current referent is expected participant of that frame
3. If no frame found → Should be First Mention

**Example**:
✅ "John went to the **restaurant**. The **waiter** approached."
❌ "John walked down the street. The **waiter** approached." (no frame context)

---

## Expected Accuracy Rates

| State | Expected Accuracy | Main Error Sources |
|-------|------------------|-------------------|
| Routine | 90-95% | Coreference failures |
| Generic | 75-85% | Generic vs specific ambiguity |
| First Mention | 85-90% | Frame database incompleteness |
| Frame Inferable | 70-80% | Frame database incompleteness |
| Interrogative | 95-99% | Syntactic parsing errors |

**Overall System Accuracy**: 85-90%

---

## Common Challenges

**Pronouns in Biblical Hebrew**: Pro-drop language, subjects implicit in verb morphology. Parse verb for person/number/gender, track as Routine with "Implicit" surface realization.

**Generic vs Specific**: "Water is essential" (Generic) vs "The water was in well" (Frame Inferable) vs "She drew the water" (Routine). Check verb type, context, and tracking history.

**Collective References**: "The disciples" treated as single tracked participant with Plural number.

**Quoted Speech**: "I" in quote refers to speaker. Track as Routine, coreferent with main clause subject. Person shifts within quote.

**Titles and Epithets**: "Jesus" = "He" = "the Teacher" = "the Nazarene". Build epithet database, map to primary referents, all Routine once established.

---

## Success Metrics

### Metric 1: State-level Precision/Recall
For each state, calculate:
```
Precision = True Positives / (True Positives + False Positives)
Recall = True Positives / (True Positives + False Negatives)
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

**Target**: F1 > 0.85 for each state

---

### Metric 2: Overall Accuracy
```
Accuracy = Correct Annotations / Total Annotations
```

**Target**: > 85%

---

### Metric 3: Referent Chain Coherence
- Manual review of logical progression
- Check for state transition violations
- Validate surface form consistency

**Target**: > 90% coherent chains

---

## Implementation Phases

**Week 1-2**: Foundation (3-State System) - Routine, Generic, First Mention on Genesis 1, John 4
**Week 3**: Frame Semantics - Add Frame Inferable detection, test on Ruth/Jonah
**Week 4**: Complete System - Add Interrogative, multi-pass validation, test on Mark
**Week 5**: Scale - Process New Testament, calculate precision/recall, build QA workflow

---

## Conclusion

Participant tracking is **highly reproducible** using:
1. Coreference resolution (80%+ accuracy with modern NLP)
2. Simple heuristics (referential distance, generic detection)
3. Frame semantics database (manual curation + FrameNet)
4. Syntactic parsing (interrogative detection)

**5-state simplified system** covers 100% of TBTA's active annotations.

**Expected accuracy**: 85-90% matching TBTA annotations

**Primary challenges**:
- Generic vs. specific ambiguity (context-dependent)
- Frame database completeness
- Coreference resolution in complex passages

**Risk mitigation**:
- Start with high-precision rules, expand coverage iteratively
- Use confidence scores to flag uncertain cases
- Build genre-specific models (narrative vs. wisdom vs. epistle)

This feature is **ready for implementation**.

---

## See Also

- **README.md**: Overview, TIER 1-2 elements, quick reference
- **PREDICTION-METHODS.md**: Three complementary LLM prompting strategies
- **THEORY.md**: Detailed linguistic foundations
- **CROSS-LINGUISTIC.md**: Language family patterns, translation examples
- **experiment-001.md**: MAT 24:46-47 testing methodology
