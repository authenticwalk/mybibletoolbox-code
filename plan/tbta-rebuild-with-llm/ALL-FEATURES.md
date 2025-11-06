# TBTA All Features - Complete List

This document catalogs ALL features from the official TBTA README at https://github.com/AllTheWord/tbta_db_export

## Source: Official TBTA Documentation

Retrieved: 2025-11-05
Source: https://raw.githubusercontent.com/AllTheWord/tbta_db_export/main/README.md

---

## Feature Categories Overview

TBTA provides 15 major categories of linguistic annotation:

### Word-Level Categories (1-8)
1. **Nouns** - Category 1
2. **Verbs** - Category 2
3. **Adjectives** - Category 3
4. **Adverbs** - Category 4
5. **Adpositions** - Category 5
6. **Conjunctions** - Category 6
7. **Phrasal Elements** - Category 7
8. **Particles** - Category 8

### Phrase-Level Categories (101-104)
9. **Noun Phrases** - Category 101
10. **Verb Phrases** - Category 102
11. **Adjective Phrases** - Category 103
12. **Adverb Phrases** - Category 104

### Clause/Discourse Categories (105-120)
13. **Clauses** - Category 105
14. **Paragraph Markers** - Category 110
15. **Episode Markers** - Category 120

---

## 1. NOUNS (Category 1)

**Structure**: `N-[complexity]-[sense]-[noun index]-[features]`

### Features

#### Position 1-3: Category, Complexity, Sense
- Category: N (Noun)
- Complexity: Semantic complexity level
- Sense: Lexical sense identifier

#### Position 4: Noun List Index
- **Values**: 1-9, A-Z, a-z (62 possible entities per verse)
- **Purpose**: Tracks coreference - identical indices = same entity
- **Use Case**: Disambiguates "which 'he' is which" in narratives

#### Position 5: Number
- **S** - Singular
- **D** - Dual (exactly 2)
- **T** - Trial (exactly 3) ✨
- **Q** - Quadrial (exactly 4)
- **p** - Paucal (a few, small number)
- **P** - Plural

**Translation Impact**: Critical for languages with number systems beyond singular/plural (Polynesian, Austronesian languages)

#### Position 6: Participant Tracking
- **I** - First Mention (new entity introduced)
- **D** - Routine (established participant)
- **i** - Integration
- **E** - Exiting (leaving the narrative)
- **R** - Restaging (reintroduced after absence)
- **O** - Offstage
- **G** - Generic
- **Q** - Interrogative
- **F** - Frame Inferable (can be inferred from context)

**Translation Impact**: Essential for switch-reference languages (Native American, Papua New Guinea)

#### Position 7: Polarity
- **A** - Affirmative
- **N** - Negative

#### Position 8: Proximity
- **n** - Near (general)
- **N** - Near Speaker and Listener
- **S** - Near Speaker
- **L** - Near Listener
- **R** - Remote within Sight
- **r** - Remote out of Sight
- **T** - Temporally Near
- **t** - Temporally Remote
- **C** - Contextually Near with Focus
- **c** - Contextually Near

**Translation Impact**: Critical for 3-way, 4-way, 5-way demonstrative systems (Japanese, Korean, Spanish, many Native American languages)

#### Position 9: Person (reserved)

#### Position 10: Person
- **1** - First
- **2** - Second
- **3** - Third
- **A** - First Inclusive ✨ ("we" including listener)
- **B** - First Exclusive ("we" excluding listener)
- **F** - First as Third
- **S** - Second as Third
- **I** - First Inclusive as Third
- **E** - First Exclusive as Third

**Translation Impact**: Essential for inclusive/exclusive distinction (Tagalog, Malay, Fijian, hundreds of languages)

#### Position 11: Surface Realization
- **N** - Not Applicable
- **A** - Argument of Verb
- **p** - Predicate Referent (singular)
- **P** - Predicate Referent (plural)

#### Position 12: Participant Status
- **N** - Not Applicable
- **P** - Primary Participant
- **A** - Associated Participant
- **M** - Minimal Participant

---

## 2. VERBS (Category 2)

**Structure**: `V-[complexity]-[sense]-[features]`

### Features

#### Position 4: Time
**Immediate/Recent Past**:
- **D** - Immediate Past
- **A** - Earlier Today
- **a** - Yesterday
- **b** - 2 Days Ago
- **c** - 3 Days Ago
- **d** - A Week Ago
- **e** - A Month Ago
- **f** - A Year Ago
- **g** - A Few Years Ago
- **h** - Historic Past

**Present**:
- **P** - Present

**Future**:
- **1** - Immediate Future
- **2** - Later Today
- **3** - Tomorrow
- **4** - 2 Days from Now
- **5** - 3 Days from Now
- **6** - A Week from Now
- **7** - A Month from Now
- **8** - A Year from Now
- **9** - A Few Years from Now
- **F** - Distant Future

**Other**:
- **T** - Timeless
- **s** - Discourse (timeless in discourse)
- **E** - Eternity Past
- **e** - Eternity Future

**Translation Impact**: Languages requiring temporal distance marking (Tagalog, many others)

#### Position 5: Aspect
- **I** - Inceptive (beginning)
- **C** - Completive (completed)
- **c** - Cessative (ending)
- **o** - Continuative (ongoing)
- **i** - Imperfective
- **R** - Routinely
- **H** - Habitual
- **G** - Gnomic (general truth)
- **U** - Unmarked

#### Position 6: Mood
- **I** - Indicative

**Potential**:
- **P** - Potential (general)
- **p** - Potential (remote possibility)
- **L** - Potential (likely)

**Obligation**:
- **O** - Obligation (general)
- **o** - Obligation (strong)
- **b** - Obligation (weak)

**Permissive**:
- **A** - Permissive (allowed)

#### Position 7: Reflexivity
- **N** - Not Reflexive
- **R** - Reflexive (intransitive)
- **r** - Reflexive (transitive)

#### Position 8: Polarity
- **A** - Affirmative
- **N** - Negative
- **E** - Emphatic Affirmative
- **e** - Emphatic Negative

#### Position 9: Adjective Degree
- **N** - No Degree
- **C** - Comparative
- **S** - Superlative
- **I** - Intensified
- **E** - Extremely Intensified
- **T** - 'too'
- **L** - 'less'
- **l** - 'least'

#### Positions 10-12: Target Tense, Aspect, Mood
Forward-looking features for target language requirements

---

## 3. ADJECTIVES (Category 3)

**Structure**: `A-[complexity]-[sense]-[degree]-[spares]`

### Features

#### Position 4: Degree
- **N** - No Degree
- **C** - Comparative
- **S** - Superlative
- **I** - Intensified
- **E** - Extremely Intensified
- **T** - 'too'
- **L** - 'less'
- **l** - 'least'
- **=** - Equality
- **+** - Intensified Comparative
- **2** - Superlative of 2 items

**Translation Impact**: Languages with complex comparison systems

---

## 4. ADVERBS (Category 4)

**Structure**: `a-[complexity]-[sense]-[degree]-[spares]`

### Features

#### Position 4: Degree
- **N** - No Degree
- **C** - Comparative
- **S** - Superlative
- **I** - Intensified
- **E** - Extremely Intensified
- **T** - 'too'
- **L** - 'less'
- **l** - 'least'

Similar intensity/comparison system to adjectives

---

## 5. ADPOSITIONS (Category 5)

**Structure**: `P-[complexity]-[sense]-[spares]`

### Purpose
Mark relationships like:
- Kinship relationships
- Quantity relationships
- Spatial relationships

**Position**: Typically precede related nouns

---

## 6. CONJUNCTIONS (Category 6)

**Structure**: `C-[complexity]-[sense]-[implicit flag]-[spares]`

### Features

#### Position 4: Implicit Flag
- **N** - No (explicit conjunction stated)
- **Y** - Yes (implicit conjunction, not stated in text)

**Translation Impact**: Languages that require explicit conjunctions vs. those that allow implicit connections

---

## 7. PHRASAL ELEMENTS (Category 7)

**Structure**: `p-[complexity]-[sense]-[spares]`

### Purpose
Encode multi-word expressions as single linguistic units

Examples: idioms, fixed phrases, compound expressions

---

## 8. PARTICLES (Category 8)

**Structure**: `r-[complexity]-[sense]-[spares]`

### Types
- Quote markers
- Discourse particles
- Other functional particles

---

## 9. NOUN PHRASES (Category 101)

**Structure**: `n-[sequence]-[semantic role]-[implicit]-[thing-relationship]-[relativized]-[spares]`

**Boundaries**: `(` and `)`

### Features

#### Position 2: Sequence
- **N** - Not in a Sequence
- **F** - First Coordinate
- **L** - Last Coordinate
- **C** - Coordinate (middle)

#### Position 3: Semantic Role
- **A** - Most Agent-like
- **a** - Less Agent-like
- **P** - Most Patient-like
- **p** - Less Patient-like
- **S** - State
- **s** - Source
- **d** - Destination
- **I** - Instrument
- **D** - Addressee
- **B** - Beneficiary
- **N** - Not Applicable

**Translation Impact**: Critical for languages with case marking or word order based on semantic role

#### Position 4: Implicit
- **E** - Explanation of Name
- **O** - Optional Passive Agent
- **A** - Implicit Argument
- **P** - Implicit Phrase
- **M** - Metonymy Explanation
- **N** - Necessary Implicit

#### Position 5: Thing Relationship
(Reserved for semantic relationships)

#### Position 6: Relativized
- **N** - No (not relativized)
- **Y** - Yes (relativized)

---

## 10. VERB PHRASES (Category 102)

**Structure**: `v-[sequence]-[implicit]-[spares]`

**Boundaries**: `(` and `)`

### Features

#### Position 2: Sequence
- **N** - Not in a Sequence
- **F** - First Coordinate
- **L** - Last Coordinate
- **C** - Coordinate (middle)

#### Position 3: Implicit
- **N** - No (explicit)
- **Y** - Yes (implicit)

---

## 11. ADJECTIVE PHRASES (Category 103)

**Structure**: `j-[sequence]-[usage]-[implicit]-[spares]`

**Boundaries**: `(` and `)`

### Features

#### Position 2: Sequence
- **N** - Not in a Sequence
- **F** - First Coordinate
- **L** - Last Coordinate
- **C** - Coordinate (middle)

#### Position 3: Usage
- **A** - Attributive
- **P** - Predicative

#### Position 4: Implicit
- **N** - No (explicit)
- **Y** - Yes (implicit)

---

## 12. ADVERB PHRASES (Category 104)

**Structure**: `d-[sequence]-[implicit]-[spares]`

**Boundaries**: `(` and `)`

### Features

#### Position 2: Sequence
- **N** - Not in a Sequence
- **F** - First Coordinate
- **L** - Last Coordinate
- **C** - Coordinate (middle)

#### Position 3: Implicit
- **N** - No (explicit)
- **Y** - Yes (implicit)

---

## 13. CLAUSES (Category 105)

**Structure**: `c-[type]-[illocutionary force]-[topic NP]-[speaker]-[listener]-[attitude]-[speaker age]-[age relationship]-[style]-[genre]-[structure]-[salience]-[sequence]-[location]-[implicit info]-[alternative analysis]-[vocabulary]-[rhetorical question]-[spares]`

**Boundaries**: Main clauses `{` and `}`, Subclauses `[` and `]`

### Features (18+ positions)

#### Position 2: Clause Type
- **I** - Independent
- **C** - Coordinate Independent
- **T** - Restrictive Relative
- **t** - Descriptive Relative
- **E** - Event Modifier (adverbial)
- **A** - Agent Complement
- **P** - Patient Complement
- **p** - Attributive Patient
- **Q** - Closing Quotation

#### Position 3: Illocutionary Force
- **D** - Declarative
- **I** - Imperative
- **C** - Content Interrogative (who, what, when, etc.)
- **Y** - Yes-No Interrogative
- **S** - Suggestive 'let's'
- **J** - Jussive
- **E** - Imperative with Emphasis

#### Position 4: Topic NP
- **A** - Most Agent-like
- **P** - Most Patient-like

#### Position 5: Speaker
Extensive coded categories including:
- Adult Daughter
- Son
- Angel
- Animal
- Boy
- Brother
- Crowd
- Daughter
- Demon
- Disciple
- Employee
- Employer
- Father
- Girl
- God
- Government Leader
- Government Official
- Group of Friends
- Holy Spirit
- King
- Man
- Men
- Military Leader
- Mother
- Prophet
- Queen
- Religious Leader
- Satan
- Servant
- Sister
- Slave
- Soldier
- Wife
- Woman
- Women
- Written Material
- Young Man

#### Position 6: Listener
(Same categories as Speaker)

#### Position 7: Speaker's Attitude
- **N** - Neutral
- **F** - Familiar
- **E** - Endearing
- **P** - Polite
- **H** - Honorable
- **f** - Friendly
- **C** - Complimentary
- **D** - Derogatory
- **A** - Antagonistic-Hostile
- **a** - Angry
- **R** - Rebuking
- **I** - Imploring

**Translation Impact**: Critical for honorific/register languages (Japanese, Korean, Javanese)

#### Position 8: Speaker's Age
- **C** - Child (0-17)
- **Y** - Young Adult (18-24)
- **A** - Adult (25-49)
- **M** - Middle Aged (50-64)
- **O** - Old (65+)
- **E** - Elder

#### Position 9: Speaker-Listener Age Relationship
- **O** - Older (different generation)
- **o** - Older (same generation)
- **S** - Essentially the Same Age
- **y** - Younger (same generation)
- **Y** - Younger (different generation)

**Translation Impact**: Essential for age-based register systems

#### Position 10: Speech Style
- **F** - Formal
- **I** - Informal

#### Position 11: Discourse Genre
- **C** - Climactic Narrative Story
- **E** - Episodic Narrative Story
- **P** - Narrative Prophecy
- **X** - Expository
- **B** - Behavioral Hortatory
- **b** - Behavioral Eulogy
- **R** - Procedural
- **S** - Persuasive
- **x** - Expressive
- **D** - Descriptive
- **L** - Epistolary (letter)
- **r** - Dramatic Narrative
- **d** - Dialog
- **G** - Genealogy

#### Position 12: Notional Structure
**Narrative**:
- **O** - Narrative-Orientation
- **I** - Narrative-Inciting Incident
- **D** - Narrative-Developing Conflict
- **C** - Narrative-Climax
- **R** - Narrative-Resolution
- **E** - Narrative-Exposition
- **c** - Narrative-Conclusion

**Hortatory**:
- **H** - Hortatory-Exhortation
- **M** - Hortatory-Motivation

**Procedural**:
- **G** - Procedural-Goal
- **S** - Procedural-Steps
- **s** - Procedural-Summary

**Persuasive**:
- **A** - Persuasive-Assertion
- **a** - Persuasive-Argument

**Expository**:
- **T** - Expository-Topic
- **i** - Expository-Information
- **t** - Expository-Topic Shift

#### Position 13: Salience Band
- **P** - Pivotal Storyline
- **1** - Primary Storyline
- **2** - Secondary Storyline
- **S** - Script Predictable Actions
- **B** - Backgrounded Actions
- **F** - Flashback
- **s** - Setting
- **I** - Irrealis (hypothetical)
- **A** - Author Intrusion
- **C** - Cohesive Material

#### Position 14: Sequence
- **N** - Not in a Sequence
- **F** - First Coordinate
- **L** - Last Coordinate
- **C** - Coordinate (middle)

#### Position 15: Location in Discourse
**Book/Paragraph**:
- **B** - First in Book
- **b** - Last in Book
- **P** - First in Paragraph
- **p** - Last in Paragraph

**Special Markers**:
- **T** - Discourse Title
- **C** - Parenthetical Comment
- **F** - Footnote (general)
- **H** - Footnote (Hebrew Name meaning)
- **M** - Footnote (Measurement equivalents)
- **X** - Footnote (Cross Reference)
- **S** - Footnote (Study note)
- **D** - Footnote (Devotional)
- **Q** - Questionable Text
- **R** - Prepose Short Sentence
- **r** - Postpose Short Sentence

#### Position 16: Implicit Information
- **C** - Cultural
- **S** - Situational
- **H** - Historical
- **B** - Background
- **A** - Subactions (steps)
- **I** - Implicit Arguments

#### Position 17: Alternative Analysis
- **P** - Primary
- **1** - First Alternative
- **2** - Second Alternative
- **3** - Third Alternative
- **4** - Fourth Alternative
- **5** - Fifth Alternative
- **L** - Literal
- **D** - Dynamic
- **B** - Biblical Units
- **C** - Contemporary Units

#### Position 18: Vocabulary Alternate
- **C** - Complex (single)
- **c** - Complex (first coordinate)
- **S** - Simple (single)
- **s** - Simple (first coordinate)
- **L** - Complex (last coordinate)
- **l** - Simple (last coordinate)
- **O** - Complex (middle coordinate)
- **o** - Simple (middle coordinate)

#### Position 19: Rhetorical Question
- **C** - Content Question
- **Y** - Yes-No Question (expects Yes)
- **N** - Yes-No Question (expects No)
- **E** - Equivalent Statement

---

## 14. PARAGRAPH MARKERS (Category 110)

**Structure**: `R-` (with empty semantic data)

### Purpose
- Marks paragraph beginnings
- Appears immediately before clauses
- Aids discourse structure tracking

---

## 15. EPISODE MARKERS (Category 120)

**Structure**: `E-` (hypothetical format)

### Purpose
- Parallel to paragraph markers
- Higher-level discourse segmentation
- Marks episode boundaries in narrative

---

## Summary Statistics

- **Total Feature Categories**: 15
- **Word-Level Categories**: 8
- **Phrase-Level Categories**: 4
- **Clause/Discourse Categories**: 3
- **Clause Feature Positions**: 18+
- **Speaker/Listener Types**: 35+
- **Temporal Distinctions**: 20+
- **Mood Options**: 7+
- **Participant Tracking States**: 9

## Key Innovation Areas

1. **Number Systems** - Goes beyond binary singular/plural
2. **Person Systems** - Inclusive/exclusive distinctions
3. **Participant Tracking** - Full discourse entity tracking
4. **Proximity Systems** - Multi-way demonstrative distinctions
5. **Temporal Granularity** - 20+ time distance markers
6. **Social Register** - Age, attitude, formality encoding
7. **Discourse Structure** - Genre, notional structure, salience
8. **Implicit Information** - Marks what's culturally assumed
9. **Alternative Analyses** - Supports multiple valid interpretations

---

## Translation Impact Summary

These features are essential for translating into:
- **1000+ languages** with grammatical categories differing from English/Greek/Hebrew
- **Polynesian/Austronesian** languages (number systems)
- **Southeast Asian** languages (inclusive/exclusive, temporal distance)
- **East Asian** languages (demonstratives, honorifics)
- **Papua New Guinea** languages (switch-reference)
- **Native American** languages (evidentiality, proximity)
- **South Asian** languages (register systems)

TBTA fills the gap between source text linguistics (Macula) and target language requirements.
