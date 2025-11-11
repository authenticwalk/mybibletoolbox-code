# Participant Tracking: Training Set

**Feature**: Participant Tracking (Referent Tracking / Topic Continuity)
**Phase**: 2 (Training Set Design)
**Date**: 2025-11-11
**Design Principle**: Equal value coverage with diverse genres and contexts

---

## Training Set Overview

**Total Verses**: 15 (Phase 2 - initial training)
**Active States**: 5 (Routine, Generic, Frame Inferable, First Mention, Interrogative)
**Verses per State**: 3 (equal coverage)
**Coverage**: 3 common values × 3 verses each = 15 total

**IMPORTANT LEARNING FROM DEGREE FEATURE**:
> After 7-12 verses, degree feature concluded rare values (i, E, L, T, s) were "non-existent"
> After 100 verses: ALL 5 rare values found at rates of 1-4 per 100 verses
> **Lesson**: Small samples incorrectly conclude rare values don't exist

**Status of "Unused" States**:
- **Restaging (R)**: 0% in 171,875 TBTA annotations, BUT may exist at rare rates (1-4 per 100)
- **Integration (i)**: 0% documented, BUT may exist (degree feature lesson applies)
- **Exiting (E)**: 0% documented, BUT may exist (degree feature lesson applies)
- **Offstage (O)**: <0.001% (extremely rare, confirmed background modifiers only)

**Training Set Approach**:
- Phase 2: Train on 5 common states (15 verses) to learn baseline patterns
- Phase 5: Design 100+ verse adversarial test to FIND rare states (Restaging, Integration, Exiting)
- Phase 10: Comprehensive validation with complete value inventory

**Rationale**: Start with common patterns, then systematically search for rare values using adversarial testing. DO NOT conclude rare values don't exist until 100+ verses tested.

---

## State 1: Routine (D) - 3 verses

**Definition**: Ongoing presence; continuous activation; participant already established and continues in narrative

**Training Verses**:

### 1. Matthew 24:46-47 (Parable narrative continuation)
**English**: "Blessed is that servant whom his lord when he cometh shall find so doing. Verily I say unto you, That he shall make him ruler over all his goods."

**Expected Entities**:
- "servant" → Routine (continues from v45)
- "lord" → Routine (established in parable)
- "he" (2x) → Routine (continuous reference)

**Why this verse**: Clear continuous reference with pronouns, established parable context

### 2. John 4:7-8 (Narrative with continuous actors)
**English**: "There cometh a woman of Samaria to draw water: Jesus saith unto her, Give me to drink. (For his disciples were gone away unto the city to buy meat.)"

**Expected Entities**:
- "woman" (after v7) → Routine (continues in v8)
- "Jesus" → Routine (main narrative participant)
- "disciples" → Routine (mentioned earlier in chapter)

**Why this verse**: Mix of pronouns and full NPs in continuous narrative

### 3. Genesis 3:6 (Sequential action, same participant)
**English**: "And when the woman saw that the tree was good for food...she took of the fruit thereof, and did eat, and gave also unto her husband"

**Expected Entities**:
- "woman" → Routine (subject throughout verse)
- "she" → Routine (same participant, continuous action)
- "husband" → Routine (established in prior verses)

**Why this verse**: Sequential verbs with same subject, established relationships

---

## State 2: Generic (G) - 3 verses

**Definition**: Type/class reference, not specific individual; generic or hypothetical

**Training Verses**:

### 4. John 3:16 (Generic referent "whosoever")
**English**: "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life."

**Expected Entities**:
- "whosoever" → Generic (any person who believes, not specific)
- "world" → Generic (humanity in general)

**Why this verse**: Classic generic reference, universal scope

### 5. Matthew 6:24 (Generic "man" / "no one")
**English**: "No man can serve two masters: for either he will hate the one, and love the other; or else he will hold to the one, and despise the other."

**Expected Entities**:
- "No man" → Generic (universal negative, not specific person)
- "he" → Generic (refers to generic "man", not specific referent)

**Why this verse**: Universal principle, generic human subject

### 6. Proverbs 14:12 (Wisdom literature generic "man")
**English**: "There is a way which seemeth right unto a man, but the end thereof are the ways of death."

**Expected Entities**:
- "man" → Generic (any person, universal principle)
- "way" → Generic (abstract concept, type not token)

**Why this verse**: Proverbial generic, wisdom literature context

---

## State 3: Frame Inferable (F) - 3 verses

**Definition**: Inferable from scene/frame; participant expected in this type of situation even if not previously mentioned

**Training Verses**:

### 7. Luke 10:34-35 (Parable scene: inn → innkeeper)
**English**: "And went to him, and bound up his wounds...and brought him to an inn, and took care of him. And on the morrow when he departed, he took out two pence, and gave them to the host..."

**Expected Entities**:
- "inn" → Frame setter (establishes scene)
- "host" / "innkeeper" → Frame Inferable (expected in inn scene, definite despite first mention)

**Why this verse**: Classic frame inference (inn → innkeeper is inferable)

### 8. Matthew 26:57 (Arrest scene: officers/guards)
**English**: "And they that had laid hold on Jesus led him away to Caiaphas the high priest, where the scribes and the elders were assembled."

**Expected Entities**:
- "they that had laid hold" → Frame Inferable (arrest scene → guards/officers expected)
- "scribes and elders" → Frame Inferable (trial scene → officials expected)

**Why this verse**: Legal scene frames infer participants

### 9. Mark 1:29 (Home scene: household members)
**English**: "And forthwith, when they were come out of the synagogue, they entered into the house of Simon and Andrew...But Simon's wife's mother lay sick of a fever"

**Expected Entities**:
- "house" → Frame setter
- "Simon's wife's mother" → Frame Inferable (home scene → family members expected)

**Why this verse**: Household frame infers family members

---

## State 4: First Mention (I) - 3 verses

**Definition**: New referent introduction; not previously mentioned or inferable

**Training Verses**:

### 10. John 4:7 (Woman at well introduction)
**English**: "There cometh a woman of Samaria to draw water"

**Expected Entities**:
- "a woman" → First Mention (new participant, indefinite article, not previously mentioned)

**Why this verse**: Classic first mention with indefinite article, narrative introduction

### 11. Luke 10:30 (Good Samaritan parable - initial participants)
**English**: "A certain man went down from Jerusalem to Jericho, and fell among thieves"

**Expected Entities**:
- "A certain man" → First Mention (indefinite, parable opening)
- "thieves" → First Mention (new antagonists, not inferable from "traveling" frame)

**Why this verse**: Parable opening, multiple first mentions

### 12. Genesis 6:9 (Noah introduction)
**English**: "These are the generations of Noah: Noah was a just man and perfect in his generations"

**Expected Entities**:
- "Noah" (first occurrence) → First Mention (genealogical introduction, new narrative focus)

**Why this verse**: Genealogical introduction pattern, shifts narrative focus

---

## State 5: Interrogative (Q) - 3 verses

**Definition**: In question context; participant introduced via question

**Training Verses**:

### 13. John 1:19 (Who are you? question)
**English**: "And this is the record of John, when the Jews sent priests and Levites from Jerusalem to ask him, Who art thou?"

**Expected Entities**:
- "Who" → Interrogative (question word)
- "thou" → Interrogative (questioned identity, even if referent known)

**Why this verse**: Direct identity question, interrogative pronoun

### 14. Luke 10:29 (And who is my neighbor? question)
**English**: "But he, willing to justify himself, said unto Jesus, And who is my neighbour?"

**Expected Entities**:
- "who" → Interrogative (question word)
- "neighbour" → Interrogative (questioned referent)

**Why this verse**: Definitional question, leads to parable

### 15. Matthew 16:13 (Who do men say that I am?)
**English**: "When Jesus came into the coasts of Caesarea Philippi, he asked his disciples, saying, Whom do men say that I the Son of man am?"

**Expected Entities**:
- "Whom" → Interrogative (question word)
- "I" (questioned identity) → Interrogative (identity question context)

**Why this verse**: Identity question, theological significance

---

## Training Set Statistics

**Total verses**: 15
**Testament distribution**:
- Old Testament: 4 verses (Genesis, Proverbs)
- New Testament: 11 verses (Gospels focus)

**Genre distribution**:
- Narrative: 9 verses (continuous stories)
- Teaching/Wisdom: 3 verses (generic principles)
- Parable: 2 verses (fictional narratives)
- Question/Dialog: 3 verses (interrogative contexts)

**State coverage**:
- Routine (D): 3 verses (73% frequency → most common)
- Generic (G): 3 verses (13.9% frequency)
- Frame Inferable (F): 3 verses (7.5% frequency)
- First Mention (I): 3 verses (5.4% frequency)
- Interrogative (Q): 3 verses (0.2% frequency → rare but important)

**Rationale for equal coverage**: Even though Routine is 73% in corpus, equal training ensures algorithm learns ALL patterns, not just common ones. Test sets will reflect natural distribution.

---

## Rare States (0% in Training, Will Search in 100+ Verse Test)

**CRITICAL LESSON FROM DEGREE FEATURE**: Do not conclude rare values don't exist based on statistics alone.

**Restaging (R)**: Returning after absence - 0% in 171,875 annotations
- **Status**: May exist at rare rates (1-4 per 100 verses)
- **Search Strategy**: 100+ verse adversarial test targeting narrative breaks, scene changes
- **Example contexts to test**: Character returns after long absence, reintroduction after focus shift

**Integration (i)**: Peripheral to central - 0% in documented samples
- **Status**: May exist at rare rates
- **Search Strategy**: Look for participants moving from background to foreground
- **Example contexts**: Minor character suddenly becomes focal, peripheral → central shift

**Exiting (E)**: Departing narrative - 0% in documented samples
- **Status**: May exist at rare rates
- **Search Strategy**: Character explicitly leaves scene, departures marked linguistically
- **Example contexts**: "He departed," "They went away," explicit exits

**Offstage (O)**: <0.001% (extremely rare, background modifiers only)
- **Status**: Confirmed rare but exists (ethnic modifiers, background attributes)
- **Not a primary tracking state** for active participants

**Training Approach**: Phase 2 focuses on 5 common states. Phase 5 will design 100+ verse test specifically to FIND rare states (R, i, E). Degree feature proved this approach essential.

---

## Surface Form Correlations (for validation)

Expected surface forms by state (use for cross-checking):

- **Routine** → Pronouns (he/she/it), zero (pro-drop)
- **Generic** → Bare nouns, "any", "whosoever", universal quantifiers
- **Frame Inferable** → Definite NP on first mention ("the waiter" in restaurant scene)
- **First Mention** → Indefinite article ("a woman"), proper names (genealogy)
- **Interrogative** → Wh-words (who/what/whom), questioned referents

---

## Cross-Feature Patterns (Learned from person-systems, degree)

1. **Equal value coverage**: Training with 3 examples per state ensures algorithm learns rare values (Interrogative 0.2%) not just common ones (Routine 73%)

2. **Surface form != Semantic state**: Definite article can be First Mention (names), Frame Inferable (scene participants), or Routine (continued reference) - context determines state

3. **Genre affects distribution**: Wisdom literature has higher Generic (principles), narrative has higher Routine (continuous tracking), dialog has higher Interrogative

4. **Theological significance**: Identity questions (Matt 16:13 "Who am I?") may have different tracking than casual questions

---

## Methodology Notes

**Prediction Method**: LLM prompting with linguistic reasoning (per README: 90%+ accuracy)
**No algorithmic rules**: Unlike person-systems/degree, this feature uses interpretive analysis
**Validation**: 3 complementary methods (surface form, discourse context, cross-linguistic translation)

**Training approach**:
1. Analyze each verse for participant entities
2. Determine discourse status (new/given/inferable)
3. Map to TBTA state
4. Validate against surface form predictions
5. Build pattern library for common cases

---

## Next Steps (Phase 3)

1. Access TBTA annotations for these 15 training verses
2. Analyze patterns in state assignments
3. Document decision rules (if patterns emerge)
4. Build prediction framework
5. Lock as Algorithm v1.0
6. Proceed to Phase 5 (test set design)

---

**Created**: 2025-11-11
**Status**: Training set designed, awaiting Phase 3 (training analysis)
**Commit**: Lock training set before accessing TBTA data
