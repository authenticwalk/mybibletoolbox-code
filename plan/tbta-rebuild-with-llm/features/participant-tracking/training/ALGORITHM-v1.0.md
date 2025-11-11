# Participant Tracking: Algorithm v1.0

**Date created**: 2025-11-11
**Based on**: PATTERNS-LEARNED.md (3,067 TBTA annotations analyzed)
**Training accuracy target**: 90%+ on 4 validated verses
**Purpose**: Predict TBTA participant tracking states for Bible translation guidance
**Status**: LOCKED (commit pending)

---

## Overview

This algorithm predicts which of 5 active participant tracking states applies to each noun phrase referent in Biblical text:
- **D** (Routine): Ongoing presence, continuous activation
- **G** (Generic): Type/class reference, not specific individual
- **F** (Frame Inferable): Inferable from scene/frame
- **I** (First Mention): New participant introduction
- **Q** (Interrogative): In question context

**Rare states** (R, i, E, O) are not predicted by v1.0 (0% frequency in training corpus, require adversarial search).

---

## Algorithm Structure

**Decision Method**: Hierarchical rule cascade (check rules in priority order)

**Priority Sequence**:
1. Rule 1: **Interrogative** (highest priority - question context)
2. Rule 2: **Generic** (semantic class/type reference)
3. Rule 3: **Frame Inferable** (contextual inference)
4. Rule 4: **First Mention vs. Routine** (default decision)

**Once a rule matches, STOP and return that state. Do not check lower-priority rules.**

---

## Rule 1: Interrogative (Q) - HIGHEST PRIORITY

**Check First**: Is the participant in a question context?

### Conditions (any ONE triggers Interrogative):

#### 1.1 Direct questioned referent
```
IF participant occurs with interrogative word (who, what, which, whom, whose)
AND clause illocutionary force = Interrogative
THEN → Interrogative (Q)
```

**Example**: "**which** command is greatest?" → "command" = Interrogative

#### 1.2 Identity question subject
```
IF participant is subject/object of identity question
AND question word refers to participant
THEN → Interrogative (Q)
```

**Example**: "**Who** are you?" → "who" = Interrogative, "you" = Interrogative

#### 1.3 Interrogative pronoun direct reference
```
IF participant IS an interrogative pronoun (who, what, which, whom)
THEN → Interrogative (Q)
```

**Example**: "**Whom** do you seek?" → "whom" = Interrogative

### Implementation Notes:
- **Surface forms**: who, what, which, whom, whose, what kind, how many
- **Clause type**: Interrogative illocutionary force required (not rhetorical questions in declarative clauses)
- **Transition rule**: Same participant OUTSIDE question context → proceed to Rule 2 (not Interrogative)

### Frequency: 0.2% (7/3,067 annotations)

**If Interrogative conditions NOT met → Proceed to Rule 2**

---

## Rule 2: Generic (G) - HIGH PRIORITY

**Check Second**: Is the participant a class/type reference (not specific individual)?

### Conditions (any ONE triggers Generic):

#### 2.1 Universal quantifiers
```
IF participant includes universal quantifier
   (whosoever, whoever, anyone, everyone, all, every, any)
THEN → Generic (G)
```

**Example**: "**whosoever** believeth" → Generic (class of believers)

**Quantifier list**:
- English: whosoever, whoever, anyone, everyone, all, every, any, no one, none, nothing
- Greek: πᾶς (pas - all), τις (tis - any), οὐδείς (oudeis - no one)
- Hebrew: כֹּל (kol - all), אִישׁ (ish - man/anyone in generic context)

#### 2.2 Negative existentials
```
IF participant has negative polarity
AND refers to absence of class (no one, no person, none, nothing)
THEN → Generic (G)
```

**Example**: "**no person** was there" → Generic (universal negation)

#### 2.3 Abstract concepts as types
```
IF participant is abstract noun
AND refers to concept/type (not specific instance)
AND NOT possessive or definite instance reference
THEN → Generic (G)
```

**Example**: "everlasting **life**" → Generic (life as type, not specific person's life)

**Abstract noun list**: life, death, love, wisdom, truth, sin, salvation, grace, judgment, mercy, faith, hope

**Contrast**: "his life" (specific instance) → Routine, NOT Generic

#### 2.4 Vocative/role titles
```
IF participant is vocative (address term)
OR role title used generically
THEN → Generic (G)
```

**Example**: "**Teacher**, which command...?" → Generic (role address, not referential)

**Vocative/role list**: Teacher, Master, Lord, Sir, Rabbi, Father, Mother, King, Prophet

**Note**: Context-dependent. "the Teacher" (referential) may be Routine if established.

#### 2.5 Proverbial/wisdom generic
```
IF genre = Wisdom literature (Proverbs, Ecclesiastes, Job wisdom sections)
AND participant = generic human reference ("a man", "the fool", "the wise")
THEN → Generic (G)
```

**Example**: "There is a way that seemeth right unto **a man**" (Proverbs) → Generic

**Genre detection**: Book codes PRO, ECC, JOB (wisdom sections), some Psalms (wisdom psalms)

#### 2.6 Hypothetical/conditional participants
```
IF participant occurs in hypothetical/conditional context
AND refers to class (not specific individual)
THEN → Generic (G)
```

**Example**: "If **anyone** comes to me..." → Generic

**Conditional markers**: if, suppose, were (subjunctive), should, would

### Implementation Notes:
- **Surface forms**: Bare nouns, quantifiers, negatives, abstract nouns, vocatives
- **Polarity check**: Negative polarity often signals Generic (no X, none, nothing)
- **Genre matters**: Wisdom literature has higher Generic frequency

### Frequency: 15.8% (485/3,067 annotations)

**If Generic conditions NOT met → Proceed to Rule 3**

---

## Rule 3: Frame Inferable (F) - MEDIUM PRIORITY

**Check Third**: Is the participant inferable from contextual frame/scene?

### Conditions (any ONE triggers Frame Inferable):

#### 3.1 Relational inference (kinship/social roles)
```
IF participant is relational noun (son, father, wife, husband, servant, master, disciple)
AND relationship to established participant is inferable
THEN → Frame Inferable (F)
```

**Example**: "God gave his only **son**" → "son" = Frame Inferable (inferable from "God" as father)

**Relational noun list**:
- Kinship: son, daughter, father, mother, brother, sister, child, parent, ancestor, descendant
- Social: master, servant, slave, lord, subject, king, citizen
- Religious: disciple, teacher, prophet, priest, follower

#### 3.2 Frame-based inference (scene-expected participants)
```
IF scene/frame established by verb or setting
AND participant is expected element of that frame
THEN → Frame Inferable (F)
```

**Common frames and expected participants**:

**Creation frame**:
- Trigger verbs: create, make, form
- Expected participants: sky, earth, creatures, light, darkness
- **Example**: "God created **the sky** and **the earth**" → Frame Inferable

**Inn/hospitality frame**:
- Trigger nouns: inn, lodging
- Expected participants: innkeeper, host, guests
- **Example**: "brought him to an inn... gave them to **the host**" → Frame Inferable

**Household frame**:
- Trigger nouns: house, home
- Expected participants: family members, residents
- **Example**: "entered house of Simon... **Simon's wife's mother**" → Frame Inferable

**Legal/trial frame**:
- Trigger nouns: court, trial, judgment
- Trigger verbs: judge, accuse, condemn
- Expected participants: judge, scribes, elders, officials, witnesses
- **Example**: "led to Caiaphas... **the scribes and elders** were assembled" → Frame Inferable

**Travel frame**:
- Trigger verbs: journey, travel, depart
- Expected participants: travelers, road, destination
- **Example**: "went down from Jerusalem to Jericho... fell among **thieves**" (if inferable from travel danger frame)

**Meal frame**:
- Trigger nouns: table, feast, supper
- Expected participants: food, guests, host, servants

**Temple/worship frame**:
- Trigger nouns: temple, synagogue, altar
- Expected participants: priests, worshippers, offerings

#### 3.3 Temporal frames
```
IF participant is temporal reference
AND establishes or is inferable from temporal frame
THEN → Frame Inferable (F)
```

**Example**: "In **the beginning**..." → "beginning" = Frame Inferable (temporal frame setter)

**Temporal frame markers**: beginning, end, day, night, morning, evening, time

#### 3.4 Definite on first mention (frame diagnostic)
```
IF participant has definite article ("the X")
AND participant is first mention in discourse
AND frame context makes it inferable
THEN → Frame Inferable (F)
```

**Key diagnostic**: Definite article on first mention signals frame inference (speaker assumes hearer can identify referent via frame)

**Example**: "the sky and the earth" (Genesis 1:1) → definite despite first mention because creation frame

### Implementation Notes:
- **Surface forms**: Definite NP on first mention is strongest signal
- **Relational nouns**: Check for possessive or relationship markers
- **Frame detection**: Identify frame-setting verbs/nouns, then check if participant is expected element

### Frequency: 6.3% (194/3,067 annotations)

**If Frame Inferable conditions NOT met → Proceed to Rule 4**

---

## Rule 4: First Mention (I) vs. Routine (D) - DEFAULT DECISION

**Check Fourth**: Is the participant new (First Mention) or established (Routine)?

### Rule 4A: First Mention (I)

#### 4A.1 Indefinite article on introduction
```
IF participant has indefinite article ("a", "an", "some")
AND participant is NEW to discourse
THEN → First Mention (I)
```

**Example**: "**a woman** of Samaria" → First Mention (indefinite signals new participant)

**Exception**: Indefinite in Generic context ("a man" in Proverbs) → Generic (caught by Rule 2)

#### 4A.2 Proper name (first occurrence in narrative)
```
IF participant is proper name
AND first mention in current narrative unit
THEN → First Mention (I)
```

**Example**: "These are the generations of **Noah**" → First Mention (genealogical introduction)

**Note**: Check discourse scope - "Moses" may be First Mention in one book, Routine in another (if previously established)

#### 4A.3 Demonstrative + new referent
```
IF participant uses demonstrative ("this X", "that X")
AND X is new information (not previously mentioned)
THEN → First Mention (I)
```

**Example**: "**This** tax collector" (if not mentioned before) → First Mention

#### 4A.4 Truly novel participant
```
IF participant NOT mentioned previously in discourse
AND NOT inferable from frame (checked in Rule 3)
AND NOT generic (checked in Rule 2)
THEN → First Mention (I)
```

**Default**: New participant = First Mention (unless other rules applied)

### Rule 4B: Routine (D)

#### 4B.1 Repeated mentions (2nd, 3rd+ occurrences)
```
IF participant mentioned previously in discourse
AND NOT in question context (Rule 1 would catch)
THEN → Routine (D)
```

**Example**: "Jesus...Jesus...Jesus...Jesus" (Mark 1:35) → all Routine (continuous presence)

**Implementation**: Maintain participant list/tracker per discourse unit

#### 4B.2 Pronouns (anaphoric reference)
```
IF participant is pronoun (he, she, it, they, him, her, them)
THEN → Routine (D)
```

**Rationale**: Pronouns refer to established participants (otherwise uninterpretable)

**Pronoun list**: he, she, it, they, him, her, them, his, her, its, their, himself, herself, itself, themselves

**Exception**: Interrogative pronouns (who, what, which) → Interrogative (caught by Rule 1)

#### 4B.3 Zero anaphora (pro-drop)
```
IF verb has no overt subject (pro-drop language)
AND subject is inferable from context
THEN → (implied subject) Routine (D)
```

**Languages**: Greek, Hebrew, Latin (pro-drop)

**Example**: Greek "ἐξῆλθεν" (went-out) → implied subject "he" = Routine

#### 4B.4 Definite NPs for established referents
```
IF participant has definite article ("the X")
AND X mentioned previously in discourse
THEN → Routine (D)
```

**Example**: "**the house**" (after house mentioned earlier) → Routine

**Contrast**: "the house" on first mention in household frame → Frame Inferable (Rule 3)

#### 4B.5 Main narrative participants (protagonist tracking)
```
IF participant is central figure throughout narrative
AND continuous presence (not absent then returning)
THEN → Routine (D)
```

**Example**: Jesus in Gospel narratives, God in Genesis creation → Routine throughout

**Implementation**: Identify protagonist(s) at discourse level

#### 4B.6 Theologically presupposed entities ⭐
```
IF participant = "God" (or variants: LORD, Yahweh, Elohim, Theos, Adonai)
THEN → Routine (D)
```

**Rationale**: TBTA marks "God" as Routine even in Genesis 1:1 (first verse of Bible)

**Theological presupposition**: God's existence/presence is presupposed in Biblical discourse, not introduced

**Special case**: Core theological concepts treated as always-accessible

**Other potential presuppositions** (tentative, needs validation):
- Heaven, Satan (in New Testament)
- The Law (in legal contexts)
- Sin, salvation (in theological discourse)

#### 4B.7 Established context from prior discourse
```
IF participant mentioned in prior verses/chapters
AND still in narrative scope
THEN → Routine (D)
```

**Example**: "his disciples" (after disciples introduced earlier) → Routine

**Scope**: Typically chapter-level or narrative unit (not across entire book unless main character)

#### 4B.8 Continued reference after question
```
IF participant was Interrogative in question
AND now occurs outside question context
THEN → Routine (D)
```

**Example**: "which **command**?" (Interrogative) → "the **command** is..." (Routine)

### Frequency:
- **Routine**: 71.6% (2,196/3,067 annotations) - DOMINANT state
- **First Mention**: 6.0% (185/3,067 annotations)

**Implementation Note**: Default to Routine if uncertain (most common state)

---

## Special Cases and Disambiguation

### Special Case 1: God as Routine (Theological Presupposition)

```
IF participant IN ["God", "LORD", "Yahweh", "YHWH", "Elohim", "Theos", "Adonai", "Most High"]
THEN → Routine (D)  # Override Rule 4A (First Mention)
```

**Rationale**: Marked Routine even in Genesis 1:1 (first verse of Bible)

**Apply**: Across all contexts (unless Interrogative per Rule 1: "Who is God?")

---

### Special Case 2: Definite Article Disambiguation

**Problem**: "the X" can signal three states:
1. Routine (the house - established)
2. Frame Inferable (the sky - creation frame, first mention)
3. First Mention (the Noah - proper names)

**Resolution**:
```
IF "the X" AND X = proper name
   THEN → First Mention (I) if first occurrence, Routine (D) if repeated

ELSE IF "the X" AND first mention AND frame-expected (Rule 3)
   THEN → Frame Inferable (F)

ELSE IF "the X" AND mentioned before
   THEN → Routine (D)

ELSE → Routine (D)  # Default (most common)
```

---

### Special Case 3: Generic vs. Routine Disambiguation (Abstract Nouns)

**Problem**: "life" can be Generic (type) or Routine (specific instance)

**Resolution**:
```
IF abstract noun AND possessive ("his life", "their love")
   THEN → Routine (D) if possessor established

ELSE IF abstract noun AND universal context ("everlasting life", "eternal love")
   THEN → Generic (G)

ELSE IF abstract noun AND specific instance ("the life of Moses")
   THEN → Routine (D)
```

---

### Special Case 4: Vocative vs. Referential

**Problem**: "Teacher" can be Generic (vocative address) or Routine (referential)

**Resolution**:
```
IF role title AND vocative comma context ("Teacher, which...")
   THEN → Generic (G)  # Rule 2.4

ELSE IF role title AND referential ("the Teacher said", "Jesus the Teacher")
   THEN → Routine (D)  # Established participant
```

---

### Special Case 5: Interrogative Transition

**Pattern**: Participant state changes after question

```
IN QUESTION CLAUSE:
   IF questioned referent → Interrogative (Q)

AFTER QUESTION (same participant):
   Re-evaluate with Rules 2-4 (typically → Routine)
```

**Example**:
- "Which **command** is greatest?" → "command" = Interrogative
- "The **command** is..." → "command" = Routine

---

## Rare States (Not Predicted by v1.0)

### Restaging (R) - 0% in training corpus

**Expected context**: Participant returns after extended absence

**Not predicted**: Requires extended narrative tracking (not in current algorithm)

**Phase 5 strategy**: Design adversarial test to find Restaging examples (long narratives, character returns)

---

### Integration (i) - 0% in training corpus

**Expected context**: Peripheral participant moves to central role

**Not predicted**: Requires discourse role shift tracking (not in current algorithm)

**Phase 5 strategy**: Target verses where minor characters suddenly become focal

---

### Exiting (E) - 0% in training corpus

**Expected context**: Participant explicitly departs narrative

**Not predicted**: May overlap with Routine (departures described but participant still "active")

**Phase 5 strategy**: Target explicit departure statements

---

### Offstage (O) - <0.001% frequency

**Expected context**: Background modifiers only (ethnic/locational attributes)

**Not predicted**: Extremely rare, not encountered in 3,067 annotations

**Phase 5 strategy**: May not be worth targeting (accept as edge case if found)

---

## Validation Protocol

### Training Validation (Phase 4)

**Test verses** (4 TBTA-validated):
1. JHN 3:16 - Multiple states (Generic, Frame Inferable, Routine)
2. MRK 1:35 - Routine dominance (Jesus 4x), First Mention, Generic
3. GEN 1:1 - Frame Inferable (sky, earth), Routine (God)
4. MAT 22:36 - Interrogative, Generic, Routine

**Target accuracy**: 90%+ on individual participant annotations

**Method**:
1. Apply algorithm to each participant in verse
2. Compare prediction to TBTA annotation
3. Calculate accuracy = (correct predictions) / (total participants)

---

### Test Validation (Phase 7)

**Test verses** (to be designed in Phase 5):
- Adversarial test: 10-15 challenging verses (target 60-70% accuracy)
- Random test: 10-15 random verses (target 85-90% accuracy)

**Method**:
1. Make blind predictions (Phase 6 - NO TBTA ACCESS)
2. Lock predictions via git commit
3. Access TBTA for validation (Phase 7)
4. Calculate accuracy, perform error analysis

---

## Implementation Pseudocode

```python
def predict_participant_tracking(participant, context):
    """
    Predict TBTA participant tracking state for a participant.

    Args:
        participant: Noun phrase referent
        context: Discourse context (clause, genre, prior mentions, frame)

    Returns:
        State: One of ['Interrogative', 'Generic', 'Frame Inferable',
                       'First Mention', 'Routine']
    """

    # Rule 1: Interrogative (highest priority)
    if is_question_context(context):
        if is_interrogative_pronoun(participant):
            return 'Interrogative'
        if is_questioned_referent(participant, context):
            return 'Interrogative'

    # Rule 2: Generic
    if has_universal_quantifier(participant):
        return 'Generic'
    if is_negative_existential(participant):
        return 'Generic'
    if is_abstract_type_reference(participant, context):
        return 'Generic'
    if is_vocative(participant, context):
        return 'Generic'
    if is_wisdom_generic(participant, context):
        return 'Generic'
    if is_hypothetical(participant, context):
        return 'Generic'

    # Rule 3: Frame Inferable
    if is_relational_inference(participant, context):
        return 'Frame Inferable'
    if is_frame_expected_participant(participant, context):
        return 'Frame Inferable'
    if is_temporal_frame(participant, context):
        return 'Frame Inferable'
    if is_definite_on_first_mention(participant, context) and has_frame(context):
        return 'Frame Inferable'

    # Special Case: God presupposition
    if participant in ["God", "LORD", "Yahweh", "Elohim", "Theos", "Adonai"]:
        return 'Routine'

    # Rule 4A: First Mention
    if has_indefinite_article(participant):
        return 'First Mention'
    if is_proper_name_first_occurrence(participant, context):
        return 'First Mention'
    if is_novel_participant(participant, context):
        return 'First Mention'

    # Rule 4B: Routine (default)
    return 'Routine'


# Helper function examples

def is_question_context(context):
    return context.illocutionary_force == 'Interrogative'

def has_universal_quantifier(participant):
    quantifiers = ['whosoever', 'whoever', 'anyone', 'everyone', 'all', 'any',
                   'no one', 'none', 'nothing', 'every']
    return any(q in participant.lower() for q in quantifiers)

def is_frame_expected_participant(participant, context):
    frames = {
        'creation': ['sky', 'earth', 'light', 'darkness', 'creatures'],
        'inn': ['innkeeper', 'host', 'guests'],
        'household': ['family', 'wife', 'mother', 'father', 'son', 'daughter'],
        'legal': ['judge', 'scribes', 'elders', 'officials', 'witnesses'],
        'travel': ['travelers', 'road', 'thieves'],
        'meal': ['food', 'guests', 'host', 'servants'],
        'temple': ['priests', 'worshippers', 'offerings']
    }

    active_frame = detect_frame(context)
    if active_frame in frames:
        return participant in frames[active_frame]
    return False

def is_novel_participant(participant, context):
    # Check if participant mentioned before in discourse
    return participant not in context.prior_mentions
```

---

## Expected Performance

### Training Set (4 verses, multiple participants)
- **Target**: 90%+ accuracy on individual participants
- **Rationale**: Algorithm directly derived from TBTA patterns

### Adversarial Test Set (Phase 5)
- **Target**: 60-70% accuracy
- **Rationale**: Challenging edge cases, ambiguous contexts

### Random Test Set (Phase 5)
- **Target**: 85-90% accuracy
- **Rationale**: Reflects natural distribution (71.6% Routine)

### Known Limitations
- ❌ Cannot predict rare states (R, i, E, O) - not in training
- ❌ Frame detection requires manual vocabulary (not fully automated)
- ❌ Proper name first occurrence requires discourse tracking
- ❌ Relational inference requires relationship detection
- ⚠️ Definite article disambiguation context-dependent (potential errors)

---

## Algorithm Versioning

**v1.0** (current):
- Based on 4 TBTA-validated verses + 3,067 corpus annotations
- Hierarchical rule cascade
- 5 active states predicted (D, G, F, I, Q)
- Rare states (R, i, E, O) not predicted
- Training accuracy TBD (Phase 4 validation)

**v2.0** (future - post-error analysis):
- Will incorporate error patterns from test validation
- May refine frame detection rules
- May add discourse-level tracking for Restaging/Integration/Exiting
- Target: 80%+ adversarial, 90%+ random

---

## Commit and Lock

**Status**: Algorithm v1.0 complete, ready for git-lock

**Next steps** (Phase 4 completion):
1. Validate algorithm on 4 training verses
2. Calculate training accuracy
3. Git commit with SHA lock
4. Document commit SHA in this file
5. Proceed to Phase 5 (test set design)

**Locked commit SHA**: [PENDING - will be added after validation]

---

**Created**: 2025-11-11
**Author**: Extracted from TBTA patterns (TBTA-ANNOTATIONS.md, PATTERNS-LEARNED.md)
**Training corpus**: 3,067 participant annotations across 215 verses
**Validation target**: 90%+ on 4 training verses
**Production target**: 80%+ adversarial, 85%+ random (to be tested Phase 5-7)
