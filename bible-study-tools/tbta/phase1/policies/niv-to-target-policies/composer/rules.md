# Master Rule Set: NIV to Tabitha Target Format

**Purpose:** Convert NIV Bible text into Tabitha's intermediary format for translation to any language.

**Analysis Base:** Ruth 1:1-22 (complete chapter)

---

## Rule Categories

### A. Structure & Organization

#### R1: Title Addition

- **Pattern**: Add title to first verse of narrative sections
- **Format**: "Title: [Summary of main event]"
- **Example**: "Title: Elimelech and Naomi move from Bethlehem to Moab."
- **Reference**: notation.md §50
- **Pros**: Provides context for translators
- **Cons**: Requires understanding of narrative structure
- **Priority**: High

#### R2: Sentence Splitting

- **Pattern**: Split compound sentences into separate sentences
- **Example**: "X, and Y" → "X. So Y"
- **Reference**: notation.md §113 (one verb per clause)
- **Pros**: Simpler parsing, clearer event boundaries
- **Cons**: May create choppy text
- **Priority**: High

---

### B. Temporal & Connectors

#### R3: Temporal Simplification

- **Pattern**: Simplify temporal phrases
- **Examples**:
  - "In the days when X" → "When X"
  - "Now" → "Later" (when indicating sequence)
- **Reference**: clauses.md (temporal clauses)
- **Pros**: Clearer temporal structure
- **Cons**: May lose nuance
- **Priority**: High

#### R4: Temporal Clause Restructuring

- **Pattern**: Convert temporal subordinate clauses to main clauses
- **Example**: "After they had lived" → "That family continued living"
- **Reference**: R3
- **Pros**: Simpler structure
- **Cons**: May change emphasis
- **Priority**: Medium

#### R5: Connector Selection

- **Pattern**: Choose connector based on semantic relationship
- **Examples**:
  - "And" → "But" (contrastive)
  - "and" → "or" (in negative contexts)
- **Reference**: notation.md §32
- **Pros**: Accurate relationship marking
- **Cons**: Requires semantic analysis
- **Priority**: High

---

### C. Determiners & Reference

#### R6: Referential Determiner

- **Pattern**: Use "that" for referential back-reference
- **Example**: "The man" → "That man" (after first mention)
- **Reference**: determiners.md
- **Pros**: Clear referent tracking
- **Cons**: May sound repetitive
- **Priority**: High

#### R7: Character Introduction Determiner

- **Pattern**: Use "a certain [noun]" for first introduction
- **Example**: "a man" → "a certain man" (first mention)
- **Reference**: determiners.md
- **Pros**: Signals new character
- **Cons**: May be unnecessary if context clear
- **Priority**: Medium

#### R8: Established Number Removal

- **Pattern**: Remove numbers when already established
- **Example**: "her two sons" → "her sons" (when "two" already mentioned)
- **Pros**: Avoid redundancy
- **Cons**: May lose precision
- **Priority**: Low

---

### D. Pronouns & Reference Resolution

#### R9: Pronoun Resolution

- **Pattern**: Resolve all third-person pronouns to nouns
- **Examples**:
  - "she" → "Naomi"
  - "they" → "Those sons" / "That family"
  - "his wife" → "Elimelech's wife"
- **Reference**: pronouns.md
- **Pros**: Explicit referents for translation
- **Cons**: May be verbose
- **Priority**: Critical

#### R10: Pronoun Resolution in Lists

- **Pattern**: Resolve pronouns when listing participants
- **Example**: "a man... together with his" → "That man, his"
- **Reference**: pronouns.md
- **Pros**: Clear referent tracking
- **Cons**: Verbose
- **Priority**: High

---

### E. Clauses & Relationships

#### R11: Apposition to Relative Clause

- **Pattern**: Convert apposition to explicit relative clause
- **Examples**:
  - "X in Y" → "X, which was in Y"
  - "X, Y's Z" → "X, who was Y's Z"
- **Reference**: clauses.md §4
- **Pros**: Explicit relationship marker
- **Cons**: More verbose
- **Priority**: High

#### R12: Adjective to Relative Clause

- **Pattern**: Convert ethnic/nationality adjectives to relative clauses
- **Example**: "Moabite women" → "women who were from Moab"
- **Pros**: Explicit relationship structure
- **Cons**: More verbose
- **Priority**: Medium

---

### F. Verbs & Voice

#### R13: Verb Simplification

- **Pattern**: Use simple verbs, avoid compound verb phrases
- **Example**: "went to live" → "moved... to live"
- **Reference**: notation.md §113
- **Pros**: One action per verb phrase
- **Cons**: May require restructuring
- **Priority**: High

#### R14: Passive to Active

- **Pattern**: Convert passive to active voice
- **Examples**:
  - "was left with" → "lived with"
  - "was left without" → "didn't have"
- **Reference**: notation.md §13, §24
- **Pros**: Simpler structure
- **Cons**: May change emphasis
- **Priority**: High

---

### G. Geographic & Location

#### R15: Geographic Specificity

- **Pattern**: Replace generic terms with specific names when contextually clear
- **Example**: "the land" → "Israel" (when Israel is meant)
- **Pros**: Explicit reference aids translation
- **Cons**: Requires contextual knowledge
- **Priority**: Medium

#### R16: Geographic Expansion

- **Pattern**: Expand geographic references with explicit structure
- **Example**: "from X, Y" → "living in a town named X, which was in Y"
- **Combines**: R11, R17
- **Pros**: Explicit location structure
- **Cons**: Very verbose
- **Priority**: Medium

#### R17: Named Construction

- **Pattern**: Use explicit "named" for proper nouns
- **Examples**:
  - "country of X" → "country named X"
  - "town X" → "town named X"
- **Reference**: notation.md §201
- **Pros**: Explicit naming relationship
- **Cons**: Repetitive
- **Priority**: High

---

### H. Ethnicity & Relationships

#### R18: Ethnicity Expansion

- **Pattern**: Expand ethnic terms to explicit relationships
- **Example**: "Ephrathites" → "in Ephrah's clan"
- **Pros**: Explicit relationship structure
- **Cons**: May lose cultural nuance
- **Priority**: Medium

---

### I. Lists & Enumeration

#### R19: List Decomposition

- **Pattern**: Split compound lists into separate sentences
- **Example**: "X and Y were A and B" → "X was A. And Y was B."
- **Pros**: Simpler parsing for translation
- **Cons**: Verbose
- **Priority**: Medium

---

### J. Time & Duration

#### R20: Time Specificity

- **Pattern**: Replace vague time with specific when possible
- **Example**: "for a while" → "for a few years"
- **Note**: Only when source supports specificity
- **Pros**: Concrete time reference
- **Cons**: May add information not in source
- **Priority**: Low

---

### K. Implicit Information

#### R21: Implicit Information Addition

- **Pattern**: Add implicit cultural/situational info with markers
- **Example**: "<<Naomi's sons grew up and became men.>>" (for unchurched)
- **Reference**: implicit.md
- **Pros**: Cultural context for translation
- **Cons**: Requires cultural knowledge
- **Priority**: Medium (audience-dependent)

---

### L. Redundancy & Simplicity

#### R22: Redundant Word Removal

- **Pattern**: Remove redundant words when meaning clear
- **Example**: "both X and Y" → "X and Y"
- **Pros**: Simplicity
- **Cons**: May lose emphasis
- **Priority**: Low

#### R23: Idiom Simplification

- **Pattern**: Simplify idioms to direct verbs
- **Examples**:
  - "come to the aid of" → "helped"
  - "show kindness" → "be kind to"
- **Reason**: Direct action clearer for translation
- **Priority**: High

#### R28: First/Second Person Referent Marking

- **Pattern**: Mark first/second person referents in quotes
- **Examples**:
  - "to me" → "to me(Naomi)"
  - "you" → "you(daughters)"
  - "We" → "We(those women)"
- **Reference**: pronouns.md (first/second person)
- **Reason**: Explicit referent in dialogue
- **Priority**: High

#### R30: Metaphor Handling

- **Pattern**: Keep metaphors if understandable, expand if not
- **Example**: "the LORD's hand has turned" - keep if clear
- **Reference**: notation.md §143-149 (metaphor)
- **Reason**: Balance clarity with naturalness
- **Priority**: Medium

#### R31: Contraction Expansion

- **Pattern**: Expand contractions to full forms
- **Examples**:
  - "Don't" → "Do not"
  - "I'll" → "I will"
  - "can't" → "cannot"
- **Reason**: Clearer for translation
- **Priority**: Medium

#### R33: Implicit Subject Addition

- **Pattern**: Add implicit subjects in questions/commands
- **Examples**:
  - "Why call me" → "Why do you call me"
  - "Go home" → "You (imp) go home" (if needed)
- **Reason**: Explicit subject for translation
- **Priority**: Medium

---

## Rule Application Priority

### Critical (Always Apply)

- R9: Pronoun Resolution

### High Priority (Apply Consistently)

- R1: Title Addition
- R2: Sentence Splitting
- R3: Temporal Simplification
- R5: Connector Selection
- R6: Referential Determiner
- R9: Pronoun Resolution (Critical, also listed here for workflow)
- R11: Apposition to Relative Clause
- R13: Verb Simplification
- R14: Passive to Active
- R17: Named Construction
- R23: Idiom Simplification
- R28: First/Second Person Referent Marking

### Medium Priority (Apply When Appropriate)

- R4: Temporal Clause Restructuring
- R7: Character Introduction Determiner
- R10: Pronoun Resolution in Lists
- R12: Adjective to Relative Clause
- R15: Geographic Specificity
- R16: Geographic Expansion
- R18: Ethnicity Expansion
- R19: List Decomposition
- R21: Implicit Information Addition
- R30: Metaphor Handling
- R31: Contraction Expansion
- R33: Implicit Subject Addition

### Low Priority (Apply Sparingly)

- R8: Established Number Removal
- R20: Time Specificity
- R22: Redundant Word Removal

---

## Compression Techniques

Reference existing policies/techniques rather than explaining:

- **pronouns.md** - Pronoun resolution patterns
- **clauses.md** - Clause structure rules
- **determiners.md** - Determiner usage
- **implicit.md** - Implicit information marking
- **notation.md** - TBTA notation standards
- **vocabulary.md** - Word level guidelines

---

## Rule Conflicts & Resolution

### Conflict: Verbosity vs. Clarity

- **Resolution**: Prioritize clarity for translation, accept verbosity
- **Example**: R11 (apposition → relative clause) increases verbosity but improves clarity

### Conflict: Specificity vs. Source Fidelity

- **Resolution**: Only add specificity when source supports it
- **Example**: R20 (time specificity) only applies when source allows

### Conflict: Simplicity vs. Completeness

- **Resolution**: Prioritize completeness for intermediary layer
- **Example**: R21 (implicit addition) adds completeness even if verbose

---

## Process Document

See **PROCESS.md** for step-by-step application of these rules.

## Rule Summary by Priority

**Critical (1 rule):**

- R9: Pronoun Resolution

**High Priority (12 rules):**

- R1, R2, R3, R5, R6, R9, R11, R13, R14, R17, R23, R28

**Medium Priority (12 rules):**

- R4, R7, R10, R12, R15, R16, R18, R19, R21, R30, R31, R33

**Low Priority (3 rules):**

- R8, R20, R22

**Total: 28 rules** (consolidated from initial 34+ patterns)
