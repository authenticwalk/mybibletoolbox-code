# Participant Tracking: TBTA Training Annotations

**Purpose**: Document actual TBTA annotations for training set analysis
**Date extracted**: 2025-11-11
**Verses analyzed**: 4 of 15 (limited by TBTA data availability)
**Total TBTA corpus analyzed**: 215 verses with participant tracking annotations

---

## Overall Statistics (TBTA Corpus)

**Total Participant Annotations**: 3,067 (across 215 verses)

| State | Count | Percentage | Training Set Expectation |
|-------|-------|------------|--------------------------|
| **Routine (D)** | 2,196 | 71.6% | 73% ✅ |
| **Generic (G)** | 485 | 15.8% | 13.9% ✅ |
| **Frame Inferable (F)** | 194 | 6.3% | 7.5% ✅ |
| **First Mention (I)** | 185 | 6.0% | 5.4% ✅ |
| **Interrogative (Q)** | 7 | 0.2% | 0.2% ✅ |
| **Restaging (R)** | 0 | 0.0% | Rare (1-4/100) ⚠️ |
| **Integration (i)** | 0 | 0.0% | Rare (1-4/100) ⚠️ |
| **Exiting (E)** | 0 | 0.0% | Rare (1-4/100) ⚠️ |
| **Offstage (O)** | 0 | 0.0% | <0.001% (extremely rare) |

**Key Finding**: Training set frequency predictions closely match actual TBTA distribution. Rare states (R, i, E) confirmed absent in current 215-verse sample, validating need for adversarial search in Phase 5.

---

## Data Availability

**Successfully extracted** (4 verses from training set):
1. ✅ **JHN 3:16** - Generic (universal "whosoever", "world", "life")
2. ✅ **MRK 1:35** - Routine (Jesus continuous), First Mention (new place), Generic (no one)
3. ✅ **GEN 1:1** - Frame Inferable (sky, earth, beginning in creation context)
4. ✅ **MAT 22:36** - Interrogative (questioned "command")

**Not available in TBTA export** (11 verses):
- Matthew 24:46-47 (chapter 24 not in export)
- Matthew 6:24 (verse not in export)
- Matthew 26:57 (chapter 26 not in export)
- Matthew 16:13 (chapter 16 not in export)
- John 4:7-8 (only John 3 available)
- John 1:19 (chapter 1 not in export)
- Luke 10:29-30, 10:34-35 (Luke 10 not in export)
- Genesis 3:6, 6:9 (only Genesis 1 available)
- Mark 1:29 (verse 29 not in export, only verse 35)
- Proverbs 14:12 (Proverbs not in export)

**Note**: TBTA export contains only 18 of 66 Bible books. Training proceeds with 4 accessible verses + linguistic theory for remaining 11.

---

## Verse 1: John 3:16 - Generic + Routine + Frame Inferable

**Reference**: JHN 3:16
**English**: "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life."

### TBTA Participant Tracking Annotations

```yaml
# Line 20 (first clause)
- Constituent: God
  Participant Tracking: Routine

# Line 50
- Constituent: person  # "world" = people of earth
  Participant Tracking: Routine

# Line 65
- Constituent: earth
  Participant Tracking: Routine

# Line 100 (embedded clause "so that God gave...")
- Constituent: God
  Participant Tracking: Routine

# Line 141 ⭐
- Constituent: son
  Participant Tracking: Frame Inferable  # Inferable from "God" context

# Line 156
- Constituent: God  # (third mention)
  Participant Tracking: Routine

# Line 197 ⭐
- Constituent: person  # "whosoever believes"
  Participant Tracking: Generic  # Universal quantifier

# Line 209 (relative clause)
- Constituent: person  # "person who believe"
  Participant Tracking: Generic

# Line 239
- Constituent: son  # (continued reference)
  Participant Tracking: Routine

# Line 295
- Constituent: person  # (continued from "whosoever")
  Participant Tracking: Routine

# Line 326 ⭐
- Constituent: life  # "everlasting life"
  Participant Tracking: Generic  # Abstract concept, type not token

# Line 338 (relative clause)
- Constituent: life  # "life which does not end"
  Participant Tracking: Generic
```

### Analysis

**Generic State Patterns**:
1. **Universal quantifiers**: "person who believes" (whosoever) → Generic
2. **Abstract concepts**: "life" (eternal life) → Generic (type, not specific instance)
3. **Transition to Routine**: First mention Generic ("whosoever") → later Routine when continued

**Frame Inferable Pattern**:
1. **Relational inference**: "son" marked Frame Inferable in context of "God" (son inferable from father)

**Routine Dominance**:
1. "God" marked Routine throughout (3 mentions), even in theological discourse
2. "person" (world) marked Routine initially (established in prior discourse?)

**Surface Form Correlation**:
- Generic: Bare noun "person", quantifier "whosoever", abstract "life"
- Frame Inferable: Relational noun "son" (son-of-God relationship)
- Routine: Proper noun "God", continued reference "person" (later clauses)

---

## Verse 2: Mark 1:35 - Routine + First Mention + Generic

**Reference**: MRK 1:35
**English**: "And in the morning, rising up a great while before day, he went out, and departed into a solitary place, and there prayed. Very early in the morning, while it was still dark, Jesus got up, left the house and went off to a solitary place, where he prayed."

### TBTA Participant Tracking Annotations

```yaml
# Line 13 (first clause - title)
- Constituent: Jesus
  Participant Tracking: Routine

# Line 70
- Constituent: sky
  Participant Tracking: Routine

# Line 128 ⭐
- Constituent: Jesus  # (second mention)
  Participant Tracking: Routine

# Line 163
- Constituent: morning
  Participant Tracking: Routine
  Participant Status: Significant Time

# Line 200 ⭐
- Constituent: Jesus  # (third mention)
  Participant Tracking: Routine

# Line 230
- Constituent: house
  Participant Tracking: Routine  # (mentioned in prior verses)

# Line 254
- Constituent: town
  Participant Tracking: Routine  # (established context)

# Line 282 ⭐
- Constituent: Jesus  # (fourth mention)
  Participant Tracking: Routine

# Line 312 ⭐
- Constituent: place  # "a solitary place"
  Participant Tracking: First Mention  # NEW location introduced

# Line 336 ⭐
- Constituent: person  # "no other person"
  Participant Tracking: Generic  # Negative existential (no one)

# Line 369 ❌
- Constituent: place  # (second mention of "place")
  Participant Tracking: First Mention  # ERROR: should be Routine?

# Line 449 ⭐
- Constituent: place  # (third mention)
  Participant Tracking: Routine  # Correct on third mention
```

### Analysis

**Routine State Patterns**:
1. **Continuous protagonist**: "Jesus" mentioned 4 times, all Routine (main narrative participant)
2. **Established context**: "house", "town" marked Routine (from prior narrative)
3. **Temporal reference**: "morning" marked Routine (established time frame)

**First Mention Pattern**:
1. **New location**: "place" (solitary place) marked First Mention on introduction
2. **Indefinite article**: "a solitary place" (indefinite signals newness)

**Generic Pattern**:
1. **Negative existential**: "person" in context of "no other person" / "no one" → Generic (refers to class, not individual)

**Potential TBTA Error**:
1. Line 369: "place" marked First Mention on SECOND occurrence (should be Routine?)
2. Line 449: "place" marked Routine on THIRD occurrence (correct pattern)
3. **Implication**: TBTA may have annotation inconsistency, or complex discourse tracking rule

**Surface Form Correlation**:
- Routine: Proper noun "Jesus" (4x), definite "the house", "the town"
- First Mention: Indefinite article "a place"
- Generic: Negative polarity "no person" / "other person"

---

## Verse 3: Genesis 1:1 - Routine + Frame Inferable

**Reference**: GEN 1:1
**English**: "In the beginning God created the heavens and the earth."

### TBTA Participant Tracking Annotations

```yaml
# Line 13 ⭐
- Constituent: God
  Participant Tracking: Routine  # FIRST verse of Bible, still Routine!

# Line 43 ⭐
- Constituent: sky  # "heavens"
  Participant Tracking: Frame Inferable  # Inferable from creation context

# Line 64 ⭐
- Constituent: earth
  Participant Tracking: Frame Inferable  # Inferable from creation context

# Line 85 ⭐
- Constituent: beginning
  Participant Tracking: Frame Inferable  # Temporal frame
  Participant Status: Significant Time

# Line 111 (second clause)
- Constituent: God
  Participant Tracking: Routine  # Continued reference
```

### Analysis

**Routine State - Theological Special Case**:
1. **"God" as Routine in Genesis 1:1**: Even at the FIRST verse of the Bible, "God" is marked Routine, not First Mention
2. **Theological significance**: TBTA treats "God" as always-accessible in Biblical discourse
3. **Presupposed existence**: God's presence is presupposed, not introduced

**Frame Inferable Patterns**:
1. **Creation frame**: "sky" and "earth" inferable from "create" verb frame
2. **Frame elements**: Participants expected in "creation" scenario (creator → created things)
3. **Temporal frame**: "beginning" inferable as temporal setting for creation narrative
4. **Definite on first mention**: "the heavens and the earth" (definite article despite first mention)

**Surface Form Correlation**:
- Routine: Proper noun "God" (theologically presupposed)
- Frame Inferable: Definite NP on first mention ("the sky", "the earth") - definite because inferable from frame

---

## Verse 4: Matthew 22:36 - Interrogative + Generic + Routine

**Reference**: MAT 22:36
**English**: "Teacher, which is the great commandment in the Law?"

### TBTA Participant Tracking Annotations

```yaml
# Line 13
- Constituent: Pharisee  # (speaker)
  Participant Tracking: Routine

# Line 49 ⭐
- Constituent: master  # "Teacher" (vocative)
  Participant Tracking: Generic  # Generic address term

# Line 65 ⭐
- Constituent: command  # "which command" (questioned)
  Participant Tracking: Interrogative  # Referent of question

# Line 77 (relative clause)
- Constituent: command  # (same referent, non-questioned context)
  Participant Tracking: Routine
```

### Analysis

**Interrogative State Pattern**:
1. **Questioned referent**: "command" in "which command is greatest?" → Interrogative
2. **Question word context**: Occurs with interrogative "which" (selection question)
3. **Transition after question**: Same referent "command" later → Routine (no longer questioned)

**Generic - Vocative Pattern**:
1. **Address term**: "master" / "Teacher" → Generic (role title, not specific individual reference)
2. **Vocative function**: Used to address, not to refer

**Interrogative vs. Routine**:
1. First mention in question → Interrogative
2. Same participant later in non-question clause → Routine
3. **Pattern**: Interrogative is CONTEXTUAL (question frame), not permanent participant status

**Surface Form Correlation**:
- Interrogative: Occurs with "which" (interrogative determiner)
- Generic: Vocative/title "Teacher"
- Routine: Speaker "Pharisee", continued referent "command" (post-question)

---

## Cross-Verse Patterns

### 1. Routine (D) - Continuous Presence

**When TBTA marks Routine**:
- ✅ Repeated mentions of same participant ("Jesus" 4x in Mark 1:35)
- ✅ Main protagonist throughout narrative ("God" in Genesis 1)
- ✅ Established participants from prior discourse ("house", "town")
- ✅ Theologically presupposed entities ("God" even in Gen 1:1)
- ✅ Continued reference after initial introduction ("place" third mention)

**Surface forms**:
- Proper nouns (Jesus, God)
- Definite NPs for established referents (the house, the town)
- Pronouns (he, it - in continuous narrative)

**Frequency**: 71.6% of all annotations (dominant state)

---

### 2. Generic (G) - Type/Class Reference

**When TBTA marks Generic**:
- ✅ Universal quantifiers ("whosoever", "person who believes")
- ✅ Negative existentials ("no person", "other person")
- ✅ Abstract concepts as types ("life" = eternal life, not specific instance)
- ✅ Vocative titles ("Teacher", "master" as role, not individual)

**Surface forms**:
- Bare nouns ("person", "life")
- Universal quantifiers ("whosoever", "all")
- Negative polarity ("no", "any")
- Generic/role titles ("Teacher", "master")

**Frequency**: 15.8% of all annotations

---

### 3. Frame Inferable (F) - Scenario-Expected Participants

**When TBTA marks Frame Inferable**:
- ✅ Relational inference ("son" inferable from "God")
- ✅ Frame elements ("sky and earth" inferable from "create" frame)
- ✅ Temporal frames ("beginning" inferable as temporal setting)
- ✅ Scene-expected participants (creation → created things)

**Surface forms**:
- Definite NP on first mention ("the sky", "the earth")
- Relational nouns ("son", kinship/relationship terms)
- Frame-specific vocabulary ("beginning" in creation narrative)

**Frequency**: 6.3% of all annotations

**Key diagnostic**: Definite article on first mention signals frame inference

---

### 4. First Mention (I) - New Participant Introduction

**When TBTA marks First Mention**:
- ✅ New location introduced ("a solitary place")
- ✅ Not inferable from prior context or frame
- ✅ Truly novel participant in discourse

**Surface forms**:
- Indefinite article ("a place")
- New proper names at genealogical introductions (not in current sample)

**Frequency**: 6.0% of all annotations

**Potential error observed**: Mark 1:35 line 369 - "place" marked First Mention on SECOND occurrence (inconsistency?)

---

### 5. Interrogative (Q) - Question Context

**When TBTA marks Interrogative**:
- ✅ Referent of identity/selection question ("which command")
- ✅ Occurs with interrogative words (who, what, which, whom)
- ✅ Questioned participant becomes Routine after question resolved

**Surface forms**:
- Interrogative pronouns (who, what, which)
- Referents in question clauses

**Frequency**: 0.2% of all annotations (7 occurrences in 215 verses)

**Pattern**: Interrogative is TEMPORARY - same referent transitions to Routine in subsequent discourse

---

## Rare States (Not Found in Current Sample)

### Restaging (R) - 0 occurrences

**Expected context** (per TBTA schema):
- Participant returns after absence
- Reintroduction after focus shift

**Why not found**: Requires extended narrative with character absences. Current 215-verse sample may lack narrative scope.

**Search strategy for Phase 5**: Target long narratives (Genesis, Samuel, Kings) with scene changes and character departures/returns.

---

### Integration (i) - 0 occurrences

**Expected context** (per TBTA schema):
- Peripheral participant moves to central role
- Background → foreground shift

**Why not found**: May be extremely rare (similar to degree feature lesson - exists but <1%)

**Search strategy for Phase 5**: Target verses where minor characters suddenly take central role (e.g., Judas in betrayal narrative, centurion in crucifixion).

---

### Exiting (E) - 0 occurrences

**Expected context** (per TBTA schema):
- Participant explicitly leaves narrative
- Departure marked linguistically ("he departed", "went away")

**Why not found**: May overlap with Routine (departures described but participant still "active" in discourse)

**Search strategy for Phase 5**: Target explicit departure statements, especially where participant does not return.

---

### Offstage (O) - 0 occurrences

**Expected context** (per TBTA schema):
- Background modifiers (ethnic, locational attributes)
- Not active participants in narrative

**Why not found**: Confirmed <0.001% in literature. Extremely rare, background-only references.

**Search strategy**: May not be worth targeting. If found, document as edge case.

---

## Key Insights for Algorithm Development

### 1. Surface Form is NOT Sufficient

**Problem**: Definite article can mark:
- Routine (the house - established)
- Frame Inferable (the sky - creation frame)
- First Mention (proper names like "Noah")

**Solution**: Must consider discourse context, not just morphology.

---

### 2. God as Routine (Theological Presupposition)

**Pattern**: "God" marked Routine even in Genesis 1:1 (first verse of Bible)

**Implication**: Some entities are presupposed as always-accessible in discourse, not introduced.

**Generalization**: Core theological concepts (God, sin, salvation?) may always be Routine in Biblical texts.

---

### 3. Frame Inference is Active Process

**Pattern**: "Sky and earth" in Genesis 1:1 marked Frame Inferable from "create" verb

**Implication**: TBTA assumes readers actively construct frames and infer expected participants.

**Challenge**: Algorithm must identify frame-setting elements (verbs, scenes) and their expected participants.

---

### 4. Interrogative is Transient State

**Pattern**: "Command" is Interrogative in question, then Routine afterward

**Implication**: Interrogative is CONTEXTUAL, not permanent participant property.

**Algorithm rule**: Mark Interrogative only within question clause, revert to other state after question.

---

### 5. Generic Covers Multiple Patterns

**Observed Generic types**:
1. Universal quantifiers ("whosoever")
2. Negative existentials ("no one")
3. Abstract concepts as types ("life")
4. Vocative/role titles ("Teacher")

**Implication**: Generic is a diverse category, requires multiple sub-rules.

---

### 6. Rare States Require Adversarial Search

**Finding**: 0 occurrences of Restaging, Integration, Exiting, Offstage in 215 verses

**Degree feature lesson**: Rare values exist at 1-4 per 100 rates even when statistics show 0%

**Phase 5 strategy**: Design 100+ verse test specifically targeting:
- Long narratives (Restaging)
- Character focus shifts (Integration)
- Explicit departures (Exiting)

---

## Validation Against Training Set Expectations

**Training set predicted** (TRAINING-SET.md):
- Routine: 73% (actual: 71.6% ✅)
- Generic: 13.9% (actual: 15.8% ✅)
- Frame Inferable: 7.5% (actual: 6.3% ✅)
- First Mention: 5.4% (actual: 6.0% ✅)
- Interrogative: 0.2% (actual: 0.2% ✅)

**Conclusion**: Training set expectations closely match TBTA corpus distribution. Equal-coverage training approach (3 verses per state) is appropriate for rare value learning.

---

## Next Steps (Phase 4: Algorithm Development)

1. **Develop hierarchical decision framework**:
   - Rule 1: Interrogative (check question context FIRST)
   - Rule 2: Generic (universal quantifiers, negatives, abstracts)
   - Rule 3: Frame Inferable (definite on first mention, relational inference)
   - Rule 4: First Mention vs. Routine (indefinite vs. established)

2. **Handle theological presuppositions**:
   - Special rule for "God" and core theological concepts

3. **Frame detection**:
   - Identify frame-setting verbs (create, build, travel, eat)
   - List expected participants per frame

4. **Surface form + context integration**:
   - Surface form as initial signal
   - Discourse context as decisional override

5. **Git-lock Algorithm v1.0**:
   - Commit locked version before test set design

---

**Created**: 2025-11-11
**Status**: Training analysis complete, ready for Algorithm v1.0 development
**Verses accessed**: 4 of 15 (JHN 3:16, MRK 1:35, GEN 1:1, MAT 22:36)
**Total corpus**: 3,067 annotations across 215 verses
