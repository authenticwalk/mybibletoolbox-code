# TBTA Aspect Prediction Experiment 001

## Overview

This experiment tests TBTA aspect predictions to establish patterns for identifying aspect values from context. The goal is to create a method for distinguishing between:
- **Completed vs ongoing actions** (Perfective vs Imperfective)
- **Habitual vs single occurrence** (Habitual vs other aspects)
- **Beginning actions** (Inceptive)
- **Ending actions** (Cessative)
- **Fully completed** (Completive)

This is critical because aspect marking is obligatory in ~40% of world languages (all Slavic languages, Mandarin, Arabic, many African languages).

## Aspect Values in TBTA

From FEATURE-SUMMARY.md, TBTA supports these aspect values:

- **Unmarked**: No specific aspect (neutral/unspecified)
- **Perfective**: Completed action viewed as whole
- **Imperfective**: Ongoing/habitual action
- **Progressive**: Currently in progress
- **Iterative**: Repeated action
- **Habitual**: Regular occurrence
- **Inceptive**: Beginning of action
- **Cessative**: End of action
- **Completive**: Fully completed

## Key Distinctions

### Perfective vs Imperfective
- **Perfective**: "He walked to the store" (completed, viewed as whole)
- **Imperfective**: "He was walking to the store" (ongoing, partial view)

### Habitual vs Single
- **Habitual**: "He used to walk every day" (regular pattern)
- **Single occurrence**: "He walked to the store" (one-time event)

### Inceptive vs Cessative
- **Inceptive**: "He began to sing" (starting point)
- **Cessative**: "He stopped singing" (ending point)

### Progressive vs Imperfective
- **Progressive**: "He is walking" (actively in progress now)
- **Imperfective**: "He was walking" (ongoing but completed past action)

---

## Test Category 1: Inceptive Aspect

### Test 1.1: MAT.024.049 - Inceptive ("begin")

**Verse**: Matthew 24:49
**Text**: "The evil servant will begin to beat his fellow servants..."
**Context**: Narrative of servants' actions, teaching parable

**Sample Verb**: "beat"
- **Aspect**: Inceptive
- **Mood**: 'might' Potential
- **Time**: Later Today
- **Polarity**: Affirmative
- **Discourse Genre**: Climactic Narrative Story
- **IlLocutionary Force**: Declarative

**Analysis**:
- The action "beat" is marked as INCEPTIVE, showing the beginning point
- The servant hasn't been beating yet - only starting to
- Combined with "might" (potential), suggests hypothetical beginning
- Time "Later Today" shows near-future inception

**Context Clues for Inceptive**:
- Verb suggests initiation of action (beat, hit, strike)
- Potential mood indicates beginning is not yet certain
- Parable context (teaching via hypothetical)
- Servant's evil action is just beginning in the narrative

**Test Prediction**:
When a verb marks the START of a new action in narrative/teaching context, especially with potential mood and near-future time, it should be INCEPTIVE.

---

## Test Category 2: Imperfective Aspect

### Test 2.1: MAT.024.015 - Imperfective (Ongoing)

**Verse**: Matthew 24:15 (estimated)
**Pattern**: Imperfective marked multiple times
**Context**: Narrative passage, apocalyptic vision

**Analysis**:
- Imperfective appears in ongoing narrative descriptions
- Typically in narrative (Climactic Narrative Story) genre
- Often with past or present time markers
- Represents actions that are/were ongoing

**Context Clues for Imperfective**:
- Narrative contexts showing ongoing states
- Actions that are continuous rather than point-like
- Often in "being" or state verbs
- Multiple characters experiencing ongoing situations

**Test Prediction**:
When describing ongoing states or continuous actions in narrative, especially with state verbs ("be", "sit", "stay"), use IMPERFECTIVE.

### Test 2.2: MAT.024.037 - Imperfective Pattern

**Verse**: Matthew 24:37
**Pattern**: Teaching passage with imperfective
**Context**: Jesus teaching about the future

**Analysis**:
- Imperfective appears in descriptive teaching
- Describes conditions/states that continue
- Part of comparison: "as it was... so it will be"
- Habitual or continuing situations

---

## Test Category 3: Cessative Aspect

### Test 3.1: MAT.024.029 - Cessative ("stop")

**Verse**: Matthew 24:29 (estimated)
**Pattern**: Cessative marked
**Context**: Apocalyptic events ending

**Analysis**:
- Cessative marks the END of action/state
- In apocalyptic context: cosmic events stop
- Opposite of inceptive
- Marks transition point in narrative

**Context Clues for Cessative**:
- Verbs of ending: stop, cease, end, finish
- Apocalyptic/climactic events ending
- Transition markers in narrative
- Change from one state to another (ending the first state)

**Test Prediction**:
When describing the END of an action or state in apocalyptic/narrative context, use CESSATIVE.

---

## Test Category 4: Habitual Aspect

### Test 4.1: Habitual Pattern

**Verse**: Matthew 24:49 (clause with "other servants")
**Pattern**: Habitual in conditional/descriptive context
**Context**: Teaching through habituality

**Analysis**:
- Habitual marks regular, repeated actions
- Often in teaching contexts
- Can combine with other aspects
- Shows customary or repeated behavior

**Context Clues for Habitual**:
- Teaching about customary practice
- Repeated actions in past or general time
- Characterization of normal behavior
- "Used to" or "would repeatedly" meaning

---

## Test Category 5: Unmarked Aspect (Default)

### Test 5.1: MAT.024.046 - Unmarked

**Verse**: Matthew 24:46
**Sample Verbs**: "do", "return", "order", "be"
- **Aspect**: Unmarked (all verbs)
- **Mood**: Indicative (various)
- **Time**: Varies (Present, Immediate Future, Discourse)
- **Discourse Genre**: Climactic Narrative Story

**Analysis**:
- Most verbs in narrative are UNMARKED
- Unmarked is the default when aspect is not semantically relevant
- Narrative action verbs (do, return) are unmarked
- Telic verbs in climactic narrative tend to be unmarked

**Context Clues for Unmarked**:
- Simple narrative progression
- No special aspect semantics needed
- Focus on event occurrence, not how it unfolds
- Not habitual, inceptive, or cessative

---

## Hypothesis Development Process

### Hypothesis 1: Genre + Semantics
**Initial Hypothesis**: Aspect is determined by:
1. Narrative genre → mostly Unmarked or Inceptive/Cessative
2. Teaching genre → Habitual or Imperfective
3. Verb semantics → some verbs predispose aspect

**Test**: Compare aspect distribution across genres in Matthew 24

### Hypothesis 2: Temporal Semantics
**Initial Hypothesis**: Aspect relates to time:
- Inceptive = beginning → Immediate Future or Later Today
- Cessative = ending → same time frames
- Habitual = repeated → Present or general time
- Imperfective = ongoing → various times but duration-marked

**Test**: Check if time markers correlate with aspect

### Hypothesis 3: Mood Interaction
**Initial Hypothesis**: Mood influences aspect:
- Potential/Subjunctive → Inceptive (hypothetical beginning)
- Indicative → Unmarked or Habitual
- Conditional → specific aspect patterns

**Test**: MAT.024.049 ("beat" = Inceptive + Potential) supports this

---

## Experimental Method

### Phase 1: Aspect Distribution Analysis (Initial)

1. **Collect data** from Matthew 24 TBTA annotations
2. **Count aspect values** by:
   - Genre (Narrative vs Teaching)
   - Mood (Indicative vs others)
   - Verb class (action vs state)
   - Time value
3. **Create frequency table** showing patterns

### Phase 2: Test Case Validation

For each test case:
1. **State hypothesis** about when this aspect should appear
2. **Predict aspect** before seeing TBTA data
3. **Compare prediction** to actual TBTA value
4. **Analyze mismatch** if prediction failed
5. **Refine hypothesis** based on error

### Phase 3: Cross-Genre Testing

1. **Narrative passages**: Matthew 24:1-35 (eschatological signs)
2. **Teaching passages**: Matthew 24:36-51 (parables and exhortations)
3. **Mixed passages**: Transition sections

### Phase 4: Error Analysis

Record each error with:
- Verse reference
- Predicted vs actual aspect
- Why prediction failed
- What additional context is needed
- Refined understanding

---

## Success Metrics

- **Accuracy**: % of aspects correctly predicted (target: >70%)
- **Precision by aspect**: For each aspect type, how often we're correct when we predict it
- **Recall by aspect**: When an aspect appears in data, how often we catch it
- **Genre-specific accuracy**: Narrative vs teaching genre differences

---

## Preliminary Results Framework

### Aspect Frequency (from data search)

From grep results, Matthew 24 has:
- **Unmarked**: Most common (default)
- **Imperfective**: Common in narrative/teaching
- **Inceptive**: Appears in action descriptions (beat, begin)
- **Cessative**: Appears with ending verbs
- **Habitual**: Conditional contexts
- **Potential moods often paired with Inceptive**

### Initial Pattern Recognition

1. **Inceptive** appears with:
   - Action verbs (beat, hit, strike)
   - Potential mood ('might')
   - Later Today / Immediate Future time
   - Narrative contexts (parable)

2. **Imperfective** appears with:
   - State verbs (be, stay)
   - Indicative mood
   - Narrative contexts
   - Ongoing situations

3. **Cessative** appears with:
   - Verbs of ending
   - Apocalyptic events
   - Transition points

4. **Unmarked** (default) appears with:
   - Simple narrative progression
   - Most verbs when aspect is not semantically loaded
   - Various moods and times

---

## Next Steps

1. **Phase 1 Data Collection**: Extract all MAT 24 verbs with aspects
2. **Create detailed table**: verse, verb, aspect, mood, time, genre
3. **Test each hypothesis**: Measure accuracy
4. **Refine and validate**: Improve predictions
5. **Test other passages**: GEN, Mark, Luke (different genres)

## Notes on Language Relevance

This is critical for:
- **All Slavic languages** (Czech, Polish, Russian, Serbian, Ukrainian) - aspect is OBLIGATORY
- **Mandarin Chinese** - requires aspect marking
- **Perfective/Imperfective pairs** in target languages
- **Biblical translation accuracy** - getting aspect wrong changes meaning fundamentally

Example:
- Russian "Я читал книгу" (imperfective, was reading) = ongoing/habitual
- Russian "Я прочитал книгу" (perfective, read) = completed

Same English sentence needs different Russian verb aspect depending on TBTA aspect marking.

---

## Document History

- **2025-11-04**: Created experiment-001.md - Aspect prediction testing framework
- Tests: Inceptive (MAT.024.049), Imperfective (MAT.024.015, MAT.024.037), Cessative (MAT.024.029), Unmarked (MAT.024.046)
- Framework: Hypothesis-driven testing with error analysis
