# TBTA Data Schema

Complete schema documentation for the Bible Translator's Assistant (TBTA) annotation format.

---

## Overview

TBTA uses a hierarchical JSON structure with:
- **Clauses** as top-level containers
- **Phrases** (NP, VP, AdjP, AdvP) as intermediate nodes
- **Words** (Noun, Verb, Adjective, Adverb, Adposition, Conjunction, Particle) as leaf nodes
- **Punctuation markers** (Space, Period, etc.)

Every element has a **Part** field indicating its type, and type-specific fields for grammatical/semantic features.

---

## Syntactic Categories

### Primary Categories

| Code | Part | Description |
|------|------|-------------|
| 1 | Noun | Nominal elements |
| 2 | Verb | Verbal elements |
| 3 | Adjective | Adjectival elements |
| 4 | Adverb | Adverbial elements |
| 5 | Adposition | Prepositions, postpositions, case markers |
| 6 | Conjunction | Coordinating and subordinating conjunctions |
| 7 | Phrasal | Multi-word idiomatic units |
| 8 | Particle | Discourse particles, markers |

### Phrase-Level Categories

| Code | Part | Description |
|------|------|-------------|
| 101 | NP | Noun Phrase |
| 102 | VP | Verb Phrase |
| 103 | AdjP | Adjective Phrase |
| 104 | AdvP | Adverb Phrase |
| 105 | Clause | Clause (sentence or subclause) |
| 110 | Paragraph | Paragraph marker |
| 120 | Episode | Episode marker |

---

## Universal Fields

### All Elements

| Field | Type | Description |
|-------|------|-------------|
| Part | string | Element type (see Syntactic Categories) |
| Children | array | Child elements (for non-terminals) |

### All Lexical Elements (Words)

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| Constituent | string | - | The actual word/morpheme |
| LexicalSense | string | A-Z, a-z, 1-9 | Distinguishes different senses of the same word |
| SemanticComplexityLevel | string | "1", "2", etc. | Complexity indicator (hardcoded in TBTA) |

---

## Noun Fields

### Core Noun Fields

| Field | Type | Description |
|-------|------|-------------|
| Part | string | "Noun" |
| Constituent | string | The noun word |
| LexicalSense | string | Sense identifier (A-Z, a-z, 1-9) |
| SemanticComplexityLevel | string | Complexity level |
| NounListIndex | string | Coreference index (1-9, A-Z, a-z) |
| Number | string | Grammatical number |
| Person | string | Grammatical person |
| Participant Tracking | string | Discourse status |
| Polarity | string | Affirmative/Negative |
| Proximity | string | Spatial/temporal deixis |
| Participant Status | string | Narrative role |
| Surface Realization | string | Syntactic realization |
| Future Expansion | string | "Unspecified" (reserved) |

### Number Values

| Value | Description |
|-------|-------------|
| S | Singular |
| D | Dual (two) |
| T | Trial (three) |
| Q | Quadrial (four) |
| p | Paucal (few) |
| P | Plural (many) |

**Note**: "Trial" is used for Trinity references in Biblical text.

### Person Values

| Value | Description |
|-------|-------------|
| 1 | First person |
| 2 | Second person |
| 3 | Third person |
| A | First person inclusive ("we" including listener) |
| B | First person exclusive ("we" excluding listener) |
| F | First person derived |
| S | Second person derived |
| I | Third person derived (impersonal) |
| E | Third person derived (existential) |

### Participant Tracking Values

| Value | Description |
|-------|-------------|
| I | First Mention - New participant introduced |
| i | Integration - Participant being integrated into discourse |
| D | Routine - Active, previously mentioned participant |
| E | Exiting - Participant leaving the discourse |
| R | Restaging - Participant reintroduced after absence |
| O | Offstage - Participant mentioned but not present |
| G | Generic - Generic/indefinite reference |
| Q | Interrogative - Question word |
| F | Frame Inferable - Expected from context/frame |

### Polarity Values

| Value | Description |
|-------|-------------|
| A | Affirmative |
| N | Negative |

### Proximity Values

| Value | Description |
|-------|-------------|
| n | Not Applicable |
| N | Near Both (speaker and listener) |
| S | Near Speaker |
| L | Near Listener |
| R | Remote Visible |
| r | Remote Hidden |
| T | Temporal Near |
| t | Temporal Remote |
| C | Contextual Near |
| c | Contextual Remote |

### Participant Status Values

| Value | Description |
|-------|-------------|
| N | Not Applicable |
| P | Protagonist |
| A | Antagonist |
| M | Major Participant |
| (special) | Significant Time - For temporal nouns |

### Surface Realization Values

| Value | Description |
|-------|-------------|
| N | Noun (full noun) |
| A | Always Noun |
| p | PRO (pronoun) |
| P | Personal Pronoun |

---

## Verb Fields

### Core Verb Fields

| Field | Type | Description |
|-------|------|-------------|
| Part | string | "Verb" |
| Constituent | string | The verb word |
| LexicalSense | string | Sense identifier |
| SemanticComplexityLevel | string | Complexity level |
| Time | string | Tense/time reference |
| Aspect | string | Aspectual value |
| Mood | string | Mood/modality |
| Polarity | string | Affirmative/Negative/Emphatic |
| Reflexivity | string | Reflexive/Reciprocal |
| Adjective Degree | string | Degree (for stative verbs) |
| Target Aspect | string | Target aspect (for auxiliary/modal) |
| Target Mood | string | Target mood (for auxiliary/modal) |
| Target Tense & Form | string | Target tense (for auxiliary/modal) |

### Time Values

| Value | Description |
|-------|-------------|
| P | Present |
| D | Immediate Past (today before now) |
| A | Earlier Today |
| a | Yesterday |
| b | Day Before Yesterday |
| c | 2-7 days ago |
| d | Last Week |
| e | Last Month |
| f | Last Year |
| g | Within 10 years |
| h | Remote Past (within living memory) |
| i | Historic Past (beyond living memory) |
| q | Unknown Past |
| r | Discourse (narrative timeframe) |
| E | Immediate Future |
| F | Later Today |
| G | Tomorrow |
| H | Day After Tomorrow |
| I | 2-7 days future |
| J | Next Week |
| K | Next Month |
| L | Next Year |
| M | Within 10 years future |
| N | Remote Future (within lifetime) |
| o | Far Future (beyond lifetime) |
| p | Unknown Future |
| T | Timeless (gnomic, generic) |

### Aspect Values

| Value | Description |
|-------|-------------|
| U | Unmarked |
| N | Inceptive (beginning) |
| C | Completive (finished) |
| c | Cessative (stopping) |
| o | Continuative (ongoing) |
| I | Imperfective (progressive) |
| R | Routinely (habitual-repetitive) |
| H | Habitual (characteristic) |
| G | Gnomic (universal truth) |

### Mood Values

| Value | Description |
|-------|-------------|
| I | Indicative (statement) |
| a | Potential (possible) |
| b | Potential Moderate |
| c | Potential Strong |
| d | Potential Very Strong |
| e | Potential Certain |
| f | Obligation Weak |
| g | Obligation Moderate |
| h | Obligation Strong |
| i | Obligation Very Strong |
| l | Permissive (allowed) |

### Polarity Values (Verb)

| Value | Description |
|-------|-------------|
| A | Affirmative |
| N | Negative |
| E | Emphatic Affirmative |
| e | Emphatic Negative |

### Reflexivity Values

| Value | Description |
|-------|-------------|
| N | Not Applicable |
| R | Reciprocal ("each other") |
| r | Reflexive ("oneself") |

---

## Adjective Fields

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| Part | string | "Adjective" | - |
| Constituent | string | - | The adjective word |
| LexicalSense | string | A-Z, a-z, 1-9 | Sense identifier |
| SemanticComplexityLevel | string | "1", etc. | Complexity level |
| Degree | string | See below | Degree of comparison |

### Degree Values

| Value | Description |
|-------|-------------|
| N | No Degree (positive) |
| C | Comparative ("more", "better") |
| S | Superlative ("most", "best") |
| I | Intensified ("very") |
| E | Extremely Intensified ("extremely") |
| T | Totality ("completely") |
| L | Large Degree ("greatly") |
| l | Small Degree ("slightly") |
| q | Equality ("as...as") |
| i | Intensified Comparative |
| s | Superlative of 2 items |

---

## Adverb Fields

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| Part | string | "Adverb" | - |
| Constituent | string | - | The adverb word |
| LexicalSense | string | A-Z, a-z, 1-9 | Sense identifier |
| SemanticComplexityLevel | string | "1", etc. | Complexity level |
| Degree | string | See Degree | Same as Adjective Degree |

---

## Adposition Fields

| Field | Type | Description |
|-------|------|-------------|
| Part | string | "Adposition" |
| Constituent | string | The preposition/postposition word |
| LexicalSense | string | Sense identifier |
| SemanticComplexityLevel | string | Complexity level |

**Special Constituents**:
- "-Generic Genitive" - Marks genitive/possessive constructions
- "-Benefactive" - Marks benefactive constructions
- Other case markers with "-" prefix

---

## Conjunction Fields

| Field | Type | Description |
|-------|------|-------------|
| Part | string | "Conjunction" |
| Constituent | string | The conjunction word (e.g., "and", "then", "but") |
| LexicalSense | string | Sense identifier |
| SemanticComplexityLevel | string | Complexity level |
| Implicit | string | "Yes" or "No" - Whether conjunction is implicit |

---

## Particle Fields

| Field | Type | Description |
|-------|------|-------------|
| Part | string | "Particle" |
| Constituent | string | Particle or marker |
| LexicalSense | string | Sense identifier |
| SemanticComplexityLevel | string | Complexity level |

**Special Constituents**:
- "-QuoteBegin" - Marks beginning of quoted speech
- "-QuoteEnd" - Marks end of quoted speech
- Other discourse markers

---

## Phrase Fields

### Noun Phrase (NP)

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| Part | string | "NP" | - |
| Children | array | - | Child elements (Nouns, Adjectives, Adpositions, other NPs) |
| Semantic Role | string | See below | Thematic role |
| Sequence | string | See below | Coordination status |
| Relativized | string | "Yes", "No" | Whether NP is head of relative clause |
| Implicit | string | Various | Implicit argument status |
| Thing-Thing Relationship | string | "Unspecified", etc. | Semantic relationship |

#### Semantic Role Values

| Value | Description |
|-------|-------------|
| A | Agent-like (doer) |
| P | Patient-like (undergoer) |
| S | State (experiencer, possessor) |
| s | Source (origin) |
| d | Destination (goal) |
| I | Instrument (means) |
| D | Addressee (recipient) |
| B | Beneficiary (benefactive) |
| N | Not Applicable (adjunct) |

**Special Values**:
- "Most Agent-like" - Prototypical agent
- "Most Patient-like" - Prototypical patient

#### Sequence Values

| Value | Description |
|-------|-------------|
| S | Not in a Sequence |
| F | First Coordinate |
| L | Last Coordinate |
| C | Coordinate (middle of series) |

#### Implicit Values

| Value | Description |
|-------|-------------|
| N | Not Applicable |
| G | Name Explanation |
| A | Optional Passive Agent |
| I | Implicit Argument |
| P | Implicit Phrase |
| M | Metonymy |
| i | Implicit Necessary |

### Verb Phrase (VP)

| Field | Type | Description |
|-------|------|-------------|
| Part | string | "VP" |
| Children | array | Child elements (Verbs, Adverbs, etc.) |
| Sequence | string | Coordination status |
| Implicit | string | "Yes", "No", etc. |

### Adjective Phrase (AdjP)

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| Part | string | "AdjP" | - |
| Children | array | - | Child elements (Adjectives, Adverbs) |
| Sequence | string | See Sequence | Coordination status |
| Usage | string | See below | Syntactic function |
| Implicit | string | See NP Implicit | Implicit status |

#### Usage Values

| Value | Description |
|-------|-------------|
| A | Attributive (modifies noun: "red car") |
| P | Predicative (predicate: "car is red") |

### Adverb Phrase (AdvP)

| Field | Type | Description |
|-------|------|-------------|
| Part | string | "AdvP" |
| Children | array | Child elements (Adverbs) |
| Sequence | string | Coordination status |
| Implicit | string | Implicit status |

---

## Clause Fields

Clauses are the most feature-rich elements, with 20+ fields covering discourse and pragmatic features.

### Core Clause Fields

| Field | Type | Description |
|-------|------|-------------|
| Part | string | "Clause" |
| Children | array | Child elements (Phrases, Particles, Conjunctions) |
| Type | string | Clause type |
| Illocutionary Force | string | Speech act type |
| Topic NP | string | Topicalization |

### Type Values

| Value | Description |
|-------|-------------|
| I | Independent (main clause) |
| C | Coordinate (coordinated main clause) |
| T | Restrictive Relative (defining) |
| t | Descriptive Relative (non-defining) |
| E | Event Modifier (temporal, conditional, etc.) |
| A | Agent Complement |
| P | Patient Complement |
| p | Attributive Patient |
| Q | Closing Quotation |

**Special Value**:
- "Patient (Object Complement)" - Embedded clause as object

### Illocutionary Force Values

| Value | Description |
|-------|-------------|
| D | Declarative (statement) |
| I | Imperative (command) |
| C | Content Interrogative ("wh"-question) |
| Y | Yes-No Interrogative |
| S | Suggestive ("let's...") |
| L | Jussive ("may...", "let...") |
| i | Emphasized Imperative |

### Topic NP Values

| Value | Description |
|-------|-------------|
| p | Most Agent-like (topic is agent) |
| P | Most Patient-like (topic is patient) |

### Discourse Participant Fields

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| Speaker | string | See below | Who is speaking |
| Listener | string | See below | Who is being addressed |
| Speaker's Attitude | string | See below | Social register |
| Speaker`s Age | string | See below | Age category of speaker |
| Speaker-Listener Age | string | See below | Relative age |
| Speech Style | string | Various | Formal/informal, etc. |

#### Speaker/Listener Values

| Value | Description |
|-------|-------------|
| 0 | Not Applicable (narrative, no dialogue) |
| M | God |
| R | Jesus |
| T | Man (generic) |
| (30+ codes) | Specific characters in Biblical narrative |

#### Speaker's Attitude Values

| Value | Description |
|-------|-------------|
| N | Not Applicable |
| n | Neutral |
| F | Familiar |
| E | Endearing |
| P | Polite |
| H | Honorable |
| (others) | Various social registers |

#### Speaker's Age Values

| Value | Description |
|-------|-------------|
| N | Not Applicable |
| A | Child |
| B | Young Adult |
| C | Adult |
| D | Elder |

#### Speaker-Listener Age Values

| Value | Description |
|-------|-------------|
| N | Not Applicable |
| O | Speaker Older (significant) |
| o | Speaker Older (slight) |
| S | Same Age |
| Y | Speaker Younger (significant) |
| y | Speaker Younger (slight) |

### Discourse Structure Fields

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| Discourse Genre | string | See below | Text type |
| Salience Band | string | See below | Narrative prominence |
| Notional Structure Schema | string | See below | Discourse structure position |
| Sequence | string | See Sequence | Coordination status |
| Location | string | See below | Structural position |

#### Discourse Genre Values

| Value | Description |
|-------|-------------|
| N | Climactic Narrative Story |
| n | Episodic Narrative |
| r | Narrative Prophecy |
| E | Expository |
| H | Behavioral Hortatory |
| (others) | Various discourse types |

#### Salience Band Values

| Value | Description |
|-------|-------------|
| N | Not Applicable (foreground) |
| 1 | Pivotal (climax) |
| P | Primary (main events) |
| 2 | Secondary (supporting events) |
| S | Script Predictable (routine) |
| B | Backgrounded Actions |
| F | Flashback |
| (others) | Various prominence levels |

#### Notional Structure Schema Values

Encodes position in discourse schemas (e.g., narrative: Setting → Inciting Incident → Rising Action → Climax → Resolution).

| Value | Description |
|-------|-------------|
| N | Not Applicable |
| (complex codes) | Position in narrative/hortatory/procedural/persuasive/expository structure |

#### Location Values

| Value | Description |
|-------|-------------|
| N | Not Applicable |
| F | First in Book |
| L | Last in Book |
| (others) | Footnotes, special positions |

### Metalinguistic Fields

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| Implicit Information | string | See below | Type of implicit knowledge needed |
| Alternative Analysis | string | See below | Alternative interpretation available |
| Vocabulary Alternate | string | See below | Translation complexity level |
| Rhetorical Question | string | See below | Rhetorical question type |

#### Implicit Information Values

| Value | Description |
|-------|-------------|
| N | Not Applicable |
| C | Cultural |
| S | Situational |
| H | Historical |
| B | Background |
| s | Subactions |
| A | Argument |

#### Alternative Analysis Values

| Value | Description |
|-------|-------------|
| N | Not Applicable |
| P | Primary (this is primary analysis) |
| A | Alternative 1 |
| B | Alternative 2 |
| C | Alternative 3 |
| D | Alternative 4 |
| E | Alternative 5 |
| L | Last alternative |
| d | Doubt |
| b | Better alternative exists |
| c | Conditional alternative |

#### Vocabulary Alternate Values

| Value | Description |
|-------|-------------|
| Not Applicable | Single representation |
| Single Sentence - Simple Vocabulary Alternate | Simple vocabulary version |
| Single Sentence - Complex Vocabulary Alternate | Complex vocabulary version |
| First Sentence - Simple Vocabulary Alternate | First of multi-sentence simple |
| Last Sentence - Simple Vocabulary Alternate | Last of multi-sentence simple |
| (others) | Various complexity/sentence split options |

#### Rhetorical Question Values

| Value | Description |
|-------|-------------|
| N | Not Applicable |
| Q | Content Rhetorical Question |
| Y | Expects "Yes" answer |
| n | Expects "No" answer |
| S | Equivalent Statement (not really a question) |

---

## Punctuation Markers

| Part | Description |
|------|-------------|
| Space | Whitespace separator |
| Period | Sentence-ending punctuation |
| Comma | (if present) |
| QuestionMark | (if present) |
| ExclamationMark | (if present) |

---

## Data Type Summary

### JSON Types Used

- **string**: All field values are strings (including numbers like "1", "3")
- **array**: Used for Children field
- **object**: Each element is a JSON object

### Controlled Vocabularies

All enumerated fields (Number, Person, Time, Aspect, Mood, etc.) use **controlled vocabularies** with fixed value sets. Do not expect free text—values are always from predefined sets.

### Missing/Optional Fields

- If a field is not applicable, it may be:
  - Present with value "Not Applicable"
  - Present with value "Unspecified"
  - Omitted entirely (for some optional fields)

---

## Encoding Patterns

### Hierarchical Structure

```
Clause
├── Conjunction (optional)
├── NP (Agent)
│   └── Noun
├── VP
│   └── Verb
├── NP (Patient)
│   ├── AdjP (optional)
│   │   └── Adjective
│   └── Noun
├── AdvP (optional)
│   └── Adverb
└── Period
```

### Coordination Pattern

```
NP (Sequence: First Coordinate)
├── Noun

NP (Sequence: Last Coordinate)
├── Conjunction "and"
└── Noun
```

### Genitive Pattern

```
NP
├── Noun (head)
└── NP (possessor)
    ├── Adposition "-Generic Genitive"
    └── Noun
```

### Embedded Clause Pattern

```
Clause (Type: Independent)
├── NP (Agent)
│   └── Noun "God"
├── VP
│   └── Verb "say"
└── Clause (Type: Patient Complement)
    ├── Particle "-QuoteBegin"
    ├── NP
    │   └── Noun
    ├── VP
    │   └── Verb
    └── Particle "-QuoteEnd"
```

---

## Version and Provenance

- **Source**: TBTA (Bible Translator's Assistant) system
- **Export Format**: JSON (via Elixir Livebook processing)
- **Original Format**: Access database (.mdb)
- **Database Files**: Bible.mdb (main grammar) and Sample.mdb (samples)
- **Processing Tools**: mdbtools (extraction) + Elixir (transformation)

---

## Notes and Caveats

### 1. Not All Fields Always Present

Some fields appear only when relevant:
- **NounListIndex**: Only on nouns
- **Speaker/Listener**: Only on dialogue clauses
- **Usage**: Only on AdjP
- **Target Aspect/Mood/Tense**: Only on auxiliary/modal verbs

### 2. Vocabulary Alternates Create Duplication

The same verse appears multiple times in the data:
- Each clause in the verse array may represent a different translation level
- Filter by "Vocabulary Alternate" field to select desired complexity

### 3. Sparse Values

Many fields default to:
- "Not Applicable"
- "Unspecified"
- "Unmarked"

This is normal—not every feature is active in every sentence.

### 4. Deep Nesting

Phrase structures can nest deeply:
- NP containing NP (genitive)
- Clause containing Clause (embedding)
- AdjP within NP

Use recursive traversal for full processing.

### 5. Discourse Fields for Advanced Use

Fields like:
- Notional Structure Schema
- Salience Band
- Implicit Information

Require expertise in discourse analysis to interpret correctly.

---

## Example Minimal Schema

**Minimal annotated word**:
```json
{
  "Part": "Noun",
  "Constituent": "light",
  "LexicalSense": "A",
  "SemanticComplexityLevel": "1",
  "NounListIndex": "2",
  "Number": "Singular",
  "Person": "Third",
  "Participant Tracking": "Generic",
  "Polarity": "Affirmative",
  "Proximity": "Not Applicable",
  "Participant Status": "Not Applicable",
  "Surface Realization": "Noun",
  "Future Expansion": "Unspecified"
}
```

**Minimal clause**:
```json
{
  "Part": "Clause",
  "Type": "Independent",
  "Illocutionary Force": "Declarative",
  "Children": [...]
}
```

---

## References

- **TBTA Documentation**: Embedded in GitHub repository README
- **Semantic String Format**: Character-by-character encoding (original TBTA format, not used in JSON export)
- **Grammar Database**: Sample.mdb contains field definitions and controlled vocabularies

For working examples, see **examples.md**.

For data access instructions, see **README.md**.
