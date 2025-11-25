# TBTA Master Prediction Prompt

## Purpose
This prompt enables accurate prediction of TBTA linguistic features for Bible translation. It combines methods proven through experimentation to achieve 80-100% accuracy across different feature types.

## Input Requirements
- Bible verse reference and text
- Target language family (if known)
- Translation context (narrative, teaching, prophetic, etc.)

## Core Prediction Process

### Step 1: Entity Identification and Indexing

For each verse, identify ALL entities (nouns and pronouns):
1. Assign unique index (1, 2, 3...) to each distinct entity
2. Track all mentions of same entity within the verse
3. Reset indices for each new verse

Example:
"The servant saw his master" → servant=1, master=2

### Step 2: Number System Analysis

For each noun/pronoun, determine number:

**Rules**:
- Count explicit quantities → Singular(1), Dual(2), Trial(3), Paucal(3-15), Plural(>15)
- Generic substances (water, food) → Singular
- Specific groups (servants, people) → Plural
- Collectives (household, congregation) → Plural if referring to members
- Add implicit concepts:
  - Actions mentioned → add "things" (Plural)
  - Locations implied → add "house/place" (Singular)
  - Communication → add "words/truth" (Singular)

### Step 3: Person/Clusivity Determination

For first person plural (we/us/our):

**Hierarchy** (check in order):
1. **Ontological**: Divine speaker → EXCLUSIVE
2. **Capability**: Can addressee participate? No → EXCLUSIVE
3. **Group Identity**: Different groups → EXCLUSIVE
4. **Discourse Function**: Authority → EXCLUSIVE, Solidarity → INCLUSIVE
5. **Default**: When uncertain → EXCLUSIVE

**Quick Rules**:
- God speaking → EXCLUSIVE
- Prayer to God → EXCLUSIVE (God not in "we")
- Apostolic testimony → EXCLUSIVE
- Shared believer experience → INCLUSIVE
- Cross-cultural/ethnic → EXCLUSIVE

### Step 4: Participant Tracking

For each entity reference:

**Categories**:
- **First Mention**: New entity introduced → "I"
- **Routine**: Previously established entity → "D"
- **Frame Inferable**: Implied by context (possessives, locations) → "F"
- **Exiting**: Entity leaves narrative (death, departure) → "E"
- **Restaging**: Reintroduced after absence → "R"
- **Generic**: Universal category → "G"

**Quick Rules**:
- All pronouns → Routine
- Possessive constructions ("his X") → X is Frame Inferable
- First noun appearance → First Mention
- Repeated references → Routine

### Step 5: Mood Identification

For each verb:

**Primary Categories**:
1. **Indicative**: Statements of fact (94% of cases)
2. **Imperative**: Direct commands
3. **Obligation**: must/should/ought
4. **Potential**: might/may/could
5. **Subjunctive**: Hypothetical/conditional

**Correlation Rules**:
- Obligation + Immediate Future time → 'must'
- Obligation + Later Today → 'should'
- Questions → Usually Indicative
- Prophecy → Often Potential

### Step 6: Aspect Marking

For each verb:

**Categories** (90% are Unmarked):
- **Unmarked**: Default, no special aspect
- **Inceptive**: Beginning of action
- **Imperfective**: Ongoing state/process
- **Habitual**: Repeated/customary action
- **Perfective**: Completed action

**Detection Rules**:
- Potential mood → Inceptive (100% correlation)
- State verbs + ongoing → Imperfective
- Present tense + customs → Habitual
- "Begin to X" → Inceptive
- Default → Unmarked

### Step 7: Time/Tense Classification

For each verb:

**Narrative Context**:
- Creation/ancient history → Historic Past
- Recent narrative → Immediate/Recent Past
- Same-day events → Earlier Today

**Discourse Context**:
- Universal truths → Discourse (timeless)
- Prophecy near → Immediate Future
- Prophecy far → Remote Future
- Eschatological → Eternity Future

**Teaching Context**:
- General principles → Present/Discourse
- Examples → Past
- Applications → Future

### Step 8: Proximity/Demonstrative Marking

For demonstratives (this/that/these/those):

**Physical Context**:
- Speaker holding/touching → Near Speaker
- Addressee's possession → Near Listener
- Visible but distant → Remote within Sight
- Not present → Remote out of Sight

**Discourse Context**:
- Just mentioned → Contextually Near
- Earlier in discourse → Contextually Remote
- Current topic → Near with Focus

### Step 9: Language-Specific Adjustments

Based on target language family:

**Austronesian**:
- Apply clusivity (inclusive/exclusive)
- Check for dual/trial number
- Mark focus/voice distinctions

**Trans-New Guinea**:
- Track switch-reference
- Mark evidentiality
- Note elevation (up/down)

**East Asian (Japanese/Korean)**:
- Apply honorific levels
- Mark age relationships
- Encode formality

**Bantu**:
- Grade past tense (immediate/recent/remote)
- Mark noun classes
- Track agreement

## Output Format

For each verse, produce:

```yaml
verse: [BOOK.CHAPTER.VERSE]
entities:
  1: [entity_name]
  2: [entity_name]
features:
  nouns:
    - constituent: [word]
      index: [1-9]
      number: [Singular|Dual|Trial|Paucal|Plural]
      person: [First|Second|Third|Inclusive|Exclusive]
      tracking: [FirstMention|Routine|FrameInferable|etc]
      proximity: [NearSpeaker|NearListener|etc]
  verbs:
    - constituent: [word]
      mood: [Indicative|Imperative|etc]
      aspect: [Unmarked|Inceptive|etc]
      time: [Present|Past|Future|Discourse|etc]
confidence:
  overall: [high|medium|low]
  notes: [any ambiguities or uncertainties]
```

## Validation Checks

Before finalizing:
1. All entities indexed consecutively (1, 2, 3...)
2. Pronouns marked as Routine (unless first mention)
3. Mood matches clause type (questions, commands)
4. Aspect correlates with mood (Potential→Inceptive)
5. Number matches quantity (2→Dual, 3→Trial)

## Error Recovery

When uncertain:
1. Default number → Singular (nouns), Plural (groups)
2. Default person → Third
3. Default tracking → Routine (if mentioned before) or First Mention
4. Default mood → Indicative
5. Default aspect → Unmarked
6. Flag for human review with uncertainty reason

## Success Metrics

Expected accuracy by feature:
- Person/Clusivity: 95-100%
- Mood: 95-100%
- Aspect: 95-98%
- NounListIndex: 95-100%
- Number: 80-85%
- Participant Tracking: 85-90%
- Time/Tense: 80-90%
- Proximity: 75-85%

Overall target: >85% accuracy across all features