# NounListIndex Coreference Resolution Experiment 001
## Matthew 24:46-47 Analysis

### Purpose
Test and understand TBTA's NounListIndex feature for tracking entity coreference, which is crucial for languages with switch-reference and complex pronoun systems.

### Test Verses
**Matthew 24:46 (ESV):** "Blessed is that servant whom his master will find doing so when he comes."
**Matthew 24:47 (ESV):** "Truly, I say to you, he will set him over all his possessions."

---

## Phase 1: Initial Entity Identification

### Verse 46 - Manual Analysis
Looking at the English text, I identify these noun phrases:
1. **"that servant"** - the main subject, a specific servant being discussed
2. **"his master"** - the servant's master/lord
3. **"he"** (implicit in "when he comes") - refers back to the master

### Verse 47 - Manual Analysis
1. **"I"** - the speaker (Jesus)
2. **"you"** - the audience (disciples)
3. **"he"** - refers to the master from v46
4. **"him"** - refers to the servant from v46
5. **"his possessions"** - the master's belongings

### Initial Coreference Hypothesis
Based on semantic understanding:
- Entity 1: The servant (v46: "that servant"; v47: "him")
- Entity 2: The master (v46: "his master", "he"; v47: "he", "his")
- Entity 3: Jesus/Speaker (v47: "I")
- Entity 4: Disciples/Audience (v47: "you")
- Entity 5: Possessions (v47: "possessions")

---

## Phase 2: TBTA Data Analysis

### Verse 46 - TBTA NounListIndex Assignments

From the TBTA data:
- **Index 1 (master)**: Appears 3 times
  - Line 13-14: "master" (first mention in temporal clause)
  - Line 58-60: "master" (as owner of house)
  - Line 130-132: "master" (as one who orders)

- **Index 2 (house)**: Appears 1 time
  - Line 43-45: "house" (destination)

- **Index 3 (servant)**: Appears 4 times
  - Line 87-89: "servant" (main clause subject)
  - Line 160-162: "servant" (recipient of orders)
  - Line 178-180: "servant" (subject in relative clause)
  - (Implicit references as subject of "do")

- **Index 4 (thing/tasks)**: Appears 2 times
  - Line 119-120: "thing" (what servant is doing)
  - Line 210-211: "thing" (what was ordered to be done)

### Verse 47 - TBTA NounListIndex Assignments

From the TBTA data:
- **Index 1 (Jesus)**: Line 7-9
- **Index 2 (follower/disciples)**: Line 37-39
- **Index 3 (truth)**: Line 48-50
- **Index 4 (servant)**: Appears 3 times
  - Line 113-115: "servant" (direct object of appoint)
  - Line 135-137: "servant" (subject of care)
  - (Continued from v46)
- **Index 5 (master)**: Appears 2 times
  - Line 82-84: "master" (subject of appoint)
  - Line 193-195: "master" (owner of things)
  - (Continued from v46)
- **Index 6 (things/possessions)**: Appears 2 times
  - Line 182-184: "thing" (all things)
  - Line 223-225: "thing" (possessed things)

---

## Phase 3: Key Observations & Mismatches

### Important Finding: Index Numbering Resets Between Verses!

The TBTA system appears to **restart numbering for each verse**, not maintaining indices across verses. This is critical for understanding the system:

- **Verse 46**: Uses indices 1-4
- **Verse 47**: Uses indices 1-6 (completely new set)

### Cross-Verse Coreference Challenge

The entities that span verses are:
- **Master**: Index 1 in v46 → Index 5 in v47
- **Servant**: Index 3 in v46 → Index 4 in v47
- **Things/Tasks**: Index 4 in v46 → Index 6 in v47

This means the NounListIndex system is **verse-scoped**, not passage-scoped.

---

## Phase 4: Refined Coreference Resolution Method

### Algorithm for Within-Verse Coreference:

1. **First Pass - Identify All Noun Phrases**
   - Extract all nouns, pronouns, and noun phrases
   - Include both explicit and implicit references

2. **Second Pass - Group by Semantic Identity**
   - Same lexical item usually = same entity
   - Pronouns matched to nearest compatible antecedent
   - Consider grammatical role and semantic compatibility

3. **Third Pass - Assign Indices**
   - Number entities in order of first appearance
   - Maintain consistency throughout the verse
   - Use digits first (1-9), then uppercase (A-Z), then lowercase (a-z)

### Special Considerations:

1. **Participant Tracking Field**: TBTA includes this field which helps:
   - "Routine" = previously mentioned entity
   - "Frame Inferable" = inferrable from context

2. **Semantic Roles**: Help distinguish entities:
   - "Most Agent-like" = typically subject/actor
   - "Most Patient-like" = typically object/recipient

3. **Nested References**: An entity can appear in multiple syntactic positions:
   - As main clause subject
   - Within relative clauses
   - As possessor in genitive constructions

---

## Phase 5: Validation Rules

### Critical Requirements:
1. Each distinct entity gets a unique index within the verse
2. All references to the same entity share the same index
3. Indices restart at 1 for each new verse

### Quality Checks:
1. Pronouns must resolve to an appropriate antecedent
2. Repeated lexical items should typically share indices (unless context indicates different entities)
3. Possessive constructions maintain entity identity

---

## Phase 6: Application to Switch-Reference Languages

### Why This Matters:

In languages with switch-reference systems:
- Verbs mark whether their subject is same or different from previous clause
- Accurate coreference tracking is essential for proper marking
- Misidentification could change meaning dramatically

### Example Application:
If translating to a switch-reference language:
- v46: "servant does X" → "master orders [SAME-SUBJECT] servant do"
- v47: "master appoints" → [DIFFERENT-SUBJECT from v46 final clause]

The NounListIndex provides the necessary tracking to make these determinations programmatically.

---

## Conclusions

1. **Verse-Scoped System**: NounListIndex resets for each verse, not maintained across passages
2. **Comprehensive Tracking**: Includes all noun mentions, even within embedded clauses
3. **Multiple Occurrences**: Same entity can have many index appearances within a verse
4. **Semantic Grouping**: Based on referential identity, not just lexical similarity
5. **Critical for Translation**: Provides essential data for morphologically complex languages

### Next Steps:
- Test with more complex passages (multiple speakers, quoted speech)
- Analyze passages with ambiguous pronoun reference
- Compare with other coreference resolution systems
- Develop automated validation for new TBTA data