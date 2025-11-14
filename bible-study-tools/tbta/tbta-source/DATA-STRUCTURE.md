# TBTA Data Structure

Overview of The Bible Translator's Assistant (TBTA) data format and organization.

---

## File Organization

### Old Testament vs New Testament

**Critical Difference**:

- **Old Testament**: Organized by **pericopes** (thematic units spanning multiple verses)
- **New Testament**: Organized by **individual verses**

**Implication for myBibleToolbox**: We use verse-based structure throughout our project. When integrating TBTA OT data, pericopes must be split to individual verses for consistency with our data standards.

### Data Access

**Source**: https://github.com/AllTheWord/tbta_db_export

**Format**: JSON export from TBTA's internal database (originally Access .mdb format)

**Files Available**:
- Bible.mdb: Main grammar database
- Sample.mdb: Sample annotations with field definitions

---

## Data Format: Hierarchical JSON

TBTA uses a tree structure with three levels:

```
Clause (root)
├── Phrases (NP, VP, AdjP, AdvP)
│   └── Words (Noun, Verb, Adjective, Adverb, etc.)
└── Punctuation (Space, Period)
```

**Universal Field**: Every element has a `Part` field indicating its type (e.g., "Clause", "NP", "Noun").

---

## Character-Based Encoding

TBTA encodes linguistic features using **single-character codes** at specific positions.

### Example: Noun Codes (10 positions)

| Position | Feature | Example Values |
|----------|---------|----------------|
| 1 | Gender | M (masculine), F (feminine), N (neuter), C (common) |
| 2 | Number | S (singular), D (dual), T (trial), P (plural) |
| 3 | Case | N (nominative), A (accusative), G (genitive), D (dative) |
| 4 | NounListIndex | 1-9, A-Z, a-z (coreference tracking) |
| 5 | Participant Tracking | I (first mention), D (routine), R (restaging) |
| 6 | Proximity | S (near speaker), L (near listener), R (remote) |
| 7 | Polarity | A (affirmative), N (negative) |
| 8 | Participant Status | P (protagonist), A (antagonist), M (major) |
| 9 | Surface Realization | N (noun), p (pronoun), P (personal pronoun) |
| 10 | Person | 1, 2, 3, A (first inclusive), B (first exclusive) |

### Example: Verb Codes (9 positions)

| Position | Feature | Example Values |
|----------|---------|----------------|
| 1 | Time | P (present), D (immediate past), h (historic past), E (immediate future) |
| 2 | Aspect | I (imperfective), C (completive), H (habitual), G (gnomic) |
| 3 | Mood | I (indicative), a-e (potential levels), f-i (obligation levels) |
| 4 | Polarity | A (affirmative), N (negative), E (emphatic affirmative) |
| 5 | Reflexivity | N (not applicable), R (reciprocal), r (reflexive) |
| 6 | Degree | N (no degree), C (comparative), S (superlative), I (intensified) |
| 7-9 | Target Features | Aspect/Mood/Tense for auxiliary/modal verbs |

**Note**: The JSON export expands these character codes into readable field names with descriptive values.

---

## Parsing Example: Old Testament

**Genesis 1:1** - "In the beginning, God created the heavens and the earth"

### Clause-Level Features

```json
{
  "Part": "Clause",
  "Type": "Independent",
  "Illocutionary Force": "Declarative",
  "Discourse Genre": "Climactic Narrative Story",
  "Location": "First in Book",
  "Salience Band": "Not Applicable"
}
```

**Interpretation**:
- Independent clause (not embedded)
- Statement (declarative)
- Part of narrative genre
- First clause of Genesis
- Foreground event (not background)

### Noun: "God" (Agent)

```json
{
  "Constituent": "God",
  "Part": "Noun",
  "Number": "Singular",
  "Person": "Third",
  "Participant Tracking": "Routine",
  "NounListIndex": "1",
  "Semantic Role": "Most Agent-like"
}
```

**Interpretation**:
- Singular noun
- Third person
- Already-introduced participant (Routine, not First Mention)
- Coreference index "1" (all references to God in this verse)
- Agent (doer of action)

### Verb: "create"

```json
{
  "Constituent": "create",
  "Part": "Verb",
  "Time": "Historic Past",
  "Aspect": "Inceptive",
  "Mood": "Indicative",
  "Polarity": "Affirmative"
}
```

**Interpretation**:
- Historic past tense (beyond living memory)
- Inceptive aspect (action beginning)
- Indicative mood (statement of fact)
- Affirmative (not negated)

### Coordinated Nouns: "heavens and earth" (Patients)

**First Coordinate**:
```json
{
  "Part": "NP",
  "Sequence": "First Coordinate",
  "Semantic Role": "Most Patient-like",
  "Children": [
    {
      "Constituent": "sky",
      "NounListIndex": "2"
    }
  ]
}
```

**Last Coordinate**:
```json
{
  "Part": "NP",
  "Sequence": "Last Coordinate",
  "Semantic Role": "Most Patient-like",
  "Children": [
    {"Constituent": "and", "Part": "Conjunction"},
    {"Constituent": "earth", "NounListIndex": "3"}
  ]
}
```

**Interpretation**:
- Two coordinated noun phrases
- Both are Patients (undergoers of action)
- Different coreference indices (2 vs 3) = different entities

---

## Parsing Example: New Testament

**John 1:1** - "In the beginning was the Word, and the Word was with God"

### Embedded Quote Structure (Genesis 1:3 example)

```json
{
  "Part": "Clause",
  "Type": "Independent",
  "Speaker": "God",
  "Listener": "God",
  "Children": [
    {"Constituent": "God", "Part": "Noun"},
    {"Constituent": "say", "Part": "Verb"},
    {
      "Part": "Clause",
      "Type": "Patient (Object Complement)",
      "Illocutionary Force": "Jussive",
      "Children": [
        {"Constituent": "-QuoteBegin", "Part": "Particle"},
        {"Constituent": "light", "Part": "Noun"},
        {"Constituent": "be", "Part": "Verb"},
        {"Constituent": "-QuoteEnd", "Part": "Particle"}
      ]
    }
  ]
}
```

**Interpretation**:
- Outer clause: "God said"
- Embedded clause: "Let there be light"
- Jussive illocutionary force (command/request)
- Quote markers show speech boundaries
- Speaker/Listener track dialogue participants

### Trinity Reference (Genesis 1:26)

```json
{
  "Constituent": "God",
  "Number": "Trial",
  "Person": "First Inclusive",
  "Participant Tracking": "Routine"
}
```

**Interpretation**:
- Trial number (exactly 3 persons) = Trinity
- First Inclusive person ("we" including listener)
- Used in "Let us make man in our image"

### Time Granularity

TBTA distinguishes **20+ temporal categories**:

| Code | Time Reference |
|------|----------------|
| P | Present |
| D | Immediate Past (today) |
| A | Earlier Today |
| a | Yesterday |
| b | Day Before Yesterday |
| c | 2-7 days ago |
| h | Remote Past (living memory) |
| i | Historic Past (beyond living memory) |
| E | Immediate Future |
| T | Timeless (gnomic) |

---

## Key Features for Translation

### 1. Participant Tracking

Tracks discourse status of entities:

| Value | Meaning | Translation Impact |
|-------|---------|-------------------|
| I | First Mention | May need "a/an" article, full noun |
| D | Routine | Can use pronoun or shortened reference |
| R | Restaging | Reintroduce with full noun after absence |
| E | Exiting | Participant leaving narrative |
| F | Frame Inferable | Expected from context, can be implicit |

### 2. Clusivity (Person Systems)

Many languages distinguish inclusive/exclusive "we":

| Value | Meaning | Languages |
|-------|---------|-----------|
| A | First Inclusive | Malay *kita*, Tagalog *tayo* |
| B | First Exclusive | Malay *kami*, Tagalog *kami* |
| 1 | First (ambiguous) | English "we" |

**Example**: Acts 15:25 - "It seemed good to us" uses First Exclusive (apostles only, not congregation).

### 3. Number Systems

Beyond singular/plural:

| Value | Meaning | Languages |
|-------|---------|-----------|
| S | Singular | All languages |
| D | Dual (2) | Hebrew, some Austronesian |
| T | Trial (3) | Some Polynesian, Melanesian |
| P | Plural (many) | All languages |
| p | Paucal (few) | Some Austronesian |

### 4. Proximity (Demonstratives)

Fine-grained spatial/temporal distinctions:

| Value | Meaning | Example Languages |
|-------|---------|-------------------|
| N | Near Both | Spanish *este* |
| S | Near Speaker | Japanese これ *kore* |
| L | Near Listener | Japanese それ *sore* |
| R | Remote Visible | Japanese あれ *are* |
| r | Remote Hidden | Some Native American |
| T | Temporal Near | "this week" |
| t | Temporal Remote | "that ancient time" |

### 5. Speaker Demographics

For languages with honorifics/register:

| Field | Values | Languages |
|-------|--------|-----------|
| Speaker's Age | Child, Young Adult, Adult, Elder | Japanese, Korean |
| Speaker-Listener Age | Older, Same, Younger | Javanese, Balinese |
| Speaker's Attitude | Neutral, Familiar, Polite, Honorable | All with register systems |

**Example**: Genesis 19:31 - Sisters of same age speaking informally.

---

## Data Structure Hierarchy

### Complete Nesting Example

```
Clause (Declarative, Independent)
├── NP (Agent)
│   ├── Noun "God"
│   └── Space
├── VP
│   ├── Verb "create"
│   └── Space
├── NP (Patient, First Coordinate)
│   ├── Noun "heavens"
│   └── Space
├── NP (Patient, Last Coordinate)
│   ├── Conjunction "and"
│   ├── Space
│   └── Noun "earth"
└── Period
```

### Phrase Types

| Code | Part | Contains |
|------|------|----------|
| 101 | NP | Nouns, Adjectives, Adpositions, nested NPs |
| 102 | VP | Verbs, Adverbs |
| 103 | AdjP | Adjectives, Adverbs |
| 104 | AdvP | Adverbs |
| 105 | Clause | All phrases, embedded clauses |

---

## Working with TBTA Data

### Accessing the Data

1. **Clone repository**: `git clone https://github.com/AllTheWord/tbta_db_export`
2. **Navigate samples**: `samples/` directory contains JSON exports
3. **File naming**: `{book}_{chapter}_{verse}.json` (e.g., `genesis_001_001.json`)

### Vocabulary Alternates

The same verse may appear multiple times with different complexity levels:

```json
{"Vocabulary Alternate": "Single Sentence - Complex Vocabulary Alternate"}
{"Vocabulary Alternate": "Single Sentence - Simple Vocabulary Alternate"}
```

**Filter by desired complexity level** when processing data.

### Missing/Optional Fields

Fields may be:
- Present with value `"Not Applicable"`
- Present with value `"Unspecified"`
- Omitted entirely

Always check field existence before accessing.

---

## Integration with myBibleToolbox

### Data Transformation Requirements

1. **Pericope Splitting**: OT data must be split from pericope-level to verse-level
2. **File Naming**: Convert to our standard: `/commentary/{BOOK}/{chapter:03d}/{BOOK}-{chapter:03d}-{verse:03d}-tbta.yaml`
3. **Format Conversion**: JSON → YAML with our schema
4. **Citation Addition**: Add inline citations for all TBTA-sourced data

### Schema Mapping

Map TBTA fields to our commentary schema:

| TBTA Field | Our Schema Section |
|------------|-------------------|
| Part, Constituent | `words` |
| Number, Person, Case | `grammar.morphology` |
| Participant Tracking | `context.discourse` |
| Semantic Role | `grammar.syntax` |
| Illocutionary Force | `context.pragmatics` |
| Discourse Genre | `themes.genre` |

See `/bible-study-tools/tbta/SCHEMA.md` for full mapping details.

---

## References

- **TBTA Repository**: https://github.com/AllTheWord/tbta_db_export
- **Full Schema**: `/plan/tbta-rebuild-with-llm/tbta-data/SCHEMA.md`
- **Worked Examples**: `/plan/tbta-rebuild-with-llm/tbta-data/examples.md`
- **Feature Analysis**: `/plan/tbta-analysis.md`
