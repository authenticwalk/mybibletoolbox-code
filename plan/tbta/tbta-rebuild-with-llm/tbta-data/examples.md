# TBTA Annotation Examples

This document provides concrete examples of TBTA annotations extracted from actual data files, showing the range of linguistic features encoded in the system.

---

## Example 1: Simple Sentence (Genesis 1:3b)

**Text**: "then light be"

**Clause-level Features**:
```json
{
  "Part": "Clause",
  "Type": "Independent",
  "Illocutionary Force": "Declarative",
  "Discourse Genre": "Climactic Narrative Story",
  "Topic NP": "Most Agent-like",
  "Location": "Not Applicable"
}
```

**Noun Annotation**:
```json
{
  "Constituent": "light",
  "Part": "Noun",
  "LexicalSense": "A",
  "NounListIndex": "3",
  "SemanticComplexityLevel": "1",
  "Number": "Singular",
  "Person": "Third",
  "Participant Tracking": "Generic",
  "Polarity": "Affirmative",
  "Surface Realization": "Noun"
}
```

**Verb Annotation**:
```json
{
  "Constituent": "be",
  "Part": "Verb",
  "LexicalSense": "E",
  "SemanticComplexityLevel": "1",
  "Time": "Discourse",
  "Aspect": "Unmarked",
  "Mood": "Indicative",
  "Polarity": "Affirmative",
  "Reflexivity": "Not Applicable"
}
```

**Insight**: Simple declarative sentence with generic noun and unmarked verb aspect.

---

## Example 2: Creation Verb with Aspect (Genesis 1:1)

**Text**: "God create sky and earth in beginning"

**Verb - Historic Past with Inceptive Aspect**:
```json
{
  "Constituent": "create",
  "Part": "Verb",
  "LexicalSense": "A",
  "Time": "Historic Past",
  "Aspect": "Inceptive",
  "Mood": "Indicative",
  "Polarity": "Affirmative"
}
```

**Noun Phrase with Semantic Role**:
```json
{
  "Part": "NP",
  "Semantic Role": "Most Agent-like",
  "Sequence": "Not in a Sequence",
  "Relativized": "No",
  "Children": [
    {
      "Constituent": "God",
      "NounListIndex": "1",
      "Participant Tracking": "Routine"
    }
  ]
}
```

**Insight**: The verb "create" is marked as **Inceptive Aspect**, indicating the beginning of an action. The "Historic Past" timeframe situates it in deep history.

---

## Example 3: Coordinated Noun Phrases (Genesis 1:1)

**Noun Phrase 1 (First Coordinate)**:
```json
{
  "Part": "NP",
  "Semantic Role": "Most Patient-like",
  "Sequence": "First Coordinate",
  "Children": [
    {
      "Constituent": "sky",
      "NounListIndex": "2",
      "Participant Tracking": "Frame Inferable"
    }
  ]
}
```

**Noun Phrase 2 (Last Coordinate)**:
```json
{
  "Part": "NP",
  "Semantic Role": "Most Patient-like",
  "Sequence": "Last Coordinate",
  "Children": [
    {
      "Constituent": "and",
      "Part": "Conjunction",
      "LexicalSense": "B"
    },
    {
      "Constituent": "earth",
      "NounListIndex": "3"
    }
  ]
}
```

**Insight**: Coordinated noun phrases are marked with **Sequence** field ("First Coordinate", "Last Coordinate"). Both share the same semantic role (Patient).

---

## Example 4: Negative Polarity (Genesis 1:2)

**Text**: "earth have form"

**Verb with Negative Polarity**:
```json
{
  "Constituent": "have",
  "Part": "Verb",
  "LexicalSense": "D",
  "Polarity": "Negative",
  "Time": "Discourse",
  "Aspect": "Unmarked",
  "Mood": "Indicative"
}
```

**Noun with Negative Polarity**:
```json
{
  "Constituent": "thing",
  "Part": "Noun",
  "Polarity": "Negative",
  "Participant Tracking": "Generic",
  "Number": "Singular"
}
```

**Insight**: Both verbs and nouns can carry **Polarity** marking for negation.

---

## Example 5: Adjective Phrases (Genesis 1:2)

**Predicative Adjectives (Coordinated)**:

**First Adjective**:
```json
{
  "Part": "AdjP",
  "Usage": "Predicative",
  "Sequence": "First Coordinate",
  "Children": [
    {
      "Constituent": "formless",
      "Part": "Adjective",
      "LexicalSense": "A",
      "Degree": "No Degree"
    }
  ]
}
```

**Second Adjective**:
```json
{
  "Part": "AdjP",
  "Usage": "Predicative",
  "Sequence": "Last Coordinate",
  "Children": [
    {
      "Constituent": "and",
      "Part": "Conjunction"
    },
    {
      "Constituent": "empty",
      "Part": "Adjective",
      "Degree": "No Degree"
    }
  ]
}
```

**Insight**: Adjective phrases distinguish between **Predicative** and **Attributive** usage.

---

## Example 6: Attributive Adjective (Genesis 1:2)

**Noun Phrase with Attributive Adjective**:
```json
{
  "Part": "NP",
  "Semantic Role": "Most Patient-like",
  "Children": [
    {
      "Part": "AdjP",
      "Usage": "Attributive",
      "Children": [
        {
          "Constituent": "deep",
          "Part": "Adjective",
          "Degree": "No Degree"
        }
      ]
    },
    {
      "Constituent": "water",
      "Part": "Noun",
      "NounListIndex": "5"
    }
  ]
}
```

**Insight**: Attributive adjectives appear **within** noun phrases, modifying the head noun.

---

## Example 7: Salience Band (Genesis 1:2)

**Backgrounded Action**:
```json
{
  "Part": "Clause",
  "Type": "Independent",
  "Illocutionary Force": "Declarative",
  "Discourse Genre": "Climactic Narrative Story",
  "Salience Band": "Backgrounded Actions"
}
```

**Contrast with Main Event**:
```json
{
  "Part": "Clause",
  "Salience Band": "Not Applicable"
}
```

**Insight**: **Salience Band** distinguishes narrative prominence. "Backgrounded Actions" mark descriptive or setting information, while main events have "Not Applicable" (foreground).

---

## Example 8: Embedded Clause with Quote (Genesis 1:3)

**Outer Clause Structure**:
```json
{
  "Part": "Clause",
  "Type": "Independent",
  "Speaker": "Not Applicable",
  "Children": [
    { "Constituent": "God", "Part": "Noun" },
    { "Constituent": "say", "Part": "Verb" },
    {
      "Part": "Clause",
      "Type": "Patient (Object Complement)",
      "Illocutionary Force": "Jussive",
      "Speaker": "God",
      "Listener": "God",
      "Children": [
        { "Constituent": "-QuoteBegin", "Part": "Particle" },
        { "Constituent": "light", "Part": "Noun" },
        { "Constituent": "be", "Part": "Verb" },
        { "Constituent": "-QuoteEnd", "Part": "Particle" }
      ]
    }
  ]
}
```

**Insight**:
- Embedded clauses marked with **Type** = "Patient (Object Complement)"
- **Particles** mark discourse boundaries ("-QuoteBegin", "-QuoteEnd")
- **Speaker** and **Listener** track dialogue participants
- **Illocutionary Force** = "Jussive" for commands ("let there be light")

---

## Example 9: Participant Tracking Across Nouns (Genesis 1:2)

**First Mention**:
```json
{
  "Constituent": "form",
  "Part": "Noun",
  "NounListIndex": "2",
  "Participant Tracking": "First Mention"
}
```

**Routine Mention**:
```json
{
  "Constituent": "God",
  "NounListIndex": "1",
  "Participant Tracking": "Routine"
}
```

**Frame Inferable**:
```json
{
  "Constituent": "earth",
  "NounListIndex": "1",
  "Participant Tracking": "Frame Inferable"
}
```

**Insight**: **Participant Tracking** encodes discourse status:
- **First Mention**: New participant introduced
- **Routine**: Active, previously mentioned participant
- **Frame Inferable**: Contextually expected participant

---

## Example 10: Genitive Construction (Genesis 1:2)

**Noun Phrase with Embedded Genitive NP**:
```json
{
  "Part": "NP",
  "Semantic Role": "Most Agent-like",
  "Children": [
    {
      "Constituent": "Spirit",
      "Part": "Noun",
      "NounListIndex": "6"
    },
    {
      "Part": "NP",
      "Semantic Role": "Not Applicable",
      "Children": [
        {
          "Constituent": "-Generic Genitive",
          "Part": "Adposition"
        },
        {
          "Constituent": "God",
          "Part": "Noun",
          "NounListIndex": "7"
        }
      ]
    }
  ]
}
```

**Text**: "Spirit of God"

**Insight**: Genitive relationships use an **Adposition** ("-Generic Genitive") with an embedded NP. The embedded NP has **Semantic Role** = "Not Applicable".

---

## Example 11: Trial Number and Inclusive Person (Genesis 1:26)

**Noun with Trinity Reference**:
```json
{
  "Constituent": "God",
  "Part": "Noun",
  "NounListIndex": "1",
  "Number": "Trial",
  "Person": "First Inclusive",
  "Participant Tracking": "Routine"
}
```

**Insight**:
- **Number** = "Trial" (for groups of three, e.g., Trinity)
- **Person** = "First Inclusive" ("we" including the listener)
- Used in "Let **us** make man in **our** image"

---

## Example 12: Future Tense (Genesis 1:26)

**Verb with Immediate Future**:
```json
{
  "Constituent": "create",
  "Part": "Verb",
  "LexicalSense": "A",
  "Time": "Immediate Future",
  "Aspect": "Unmarked",
  "Mood": "Indicative",
  "Polarity": "Affirmative"
}
```

**Insight**: **Time** field encodes temporal reference. "Immediate Future" contrasts with "Historic Past", "Discourse", etc.

---

## Example 13: Adverb Phrase (Genesis 1:26)

**Temporal Adverb**:
```json
{
  "Part": "AdvP",
  "Sequence": "Not in a Sequence",
  "Children": [
    {
      "Constituent": "now",
      "Part": "Adverb",
      "LexicalSense": "A",
      "Degree": "No Degree"
    }
  ]
}
```

**Insight**: Adverbs are wrapped in **AdvP** (Adverb Phrase) for consistency with phrase-level annotation.

---

## Example 14: Vocabulary Alternates (Genesis 1:1)

TBTA provides multiple translation alternatives for the same verse:

**Complex Vocabulary**:
```json
{
  "Part": "Clause",
  "Vocabulary Alternate": "Single Sentence - Complex Vocabulary Alternate"
}
```

**Simple Vocabulary**:
```json
{
  "Part": "Clause",
  "Vocabulary Alternate": "Single Sentence - Simple Vocabulary Alternate"
}
```

**Insight**: The same verse appears **multiple times** with different vocabulary levels to support translation at various complexity levels.

---

## Example 15: Significant Time Participant Status (Genesis 1:1)

**Temporal Noun with Special Status**:
```json
{
  "Constituent": "beginning",
  "Part": "Noun",
  "NounListIndex": "4",
  "Participant Status": "Significant Time",
  "Participant Tracking": "Frame Inferable"
}
```

**Insight**: **Participant Status** can mark temporal nouns as "Significant Time" (e.g., "beginning", critical time references).

---

## Example 16: Thing-Thing Relationship Field

**Most Noun Phrases**:
```json
{
  "Part": "NP",
  "Thing-Thing Relationship": "Unspecified"
}
```

**Insight**: **Thing-Thing Relationship** field is present on all NPs but typically "Unspecified". May encode semantic relationships in more complex constructions.

---

## Example 17: Clause Location Marker (Genesis 1:1)

**First Clause in Book**:
```json
{
  "Part": "Clause",
  "Location": "First in Book"
}
```

**Other Clauses**:
```json
{
  "Part": "Clause",
  "Location": "Not Applicable"
}
```

**Insight**: **Location** field marks structurally significant positions (e.g., "First in Book", "Last in Book", footnotes).

---

## Example 18: Multiple Semantic Roles in One Clause (Genesis 1:1)

**Agent NP**:
```json
{
  "Part": "NP",
  "Semantic Role": "Most Agent-like"
}
```

**Patient NPs (Coordinated)**:
```json
{
  "Part": "NP",
  "Semantic Role": "Most Patient-like",
  "Sequence": "First Coordinate"
}
```
```json
{
  "Part": "NP",
  "Semantic Role": "Most Patient-like",
  "Sequence": "Last Coordinate"
}
```

**Temporal/Locative NP**:
```json
{
  "Part": "NP",
  "Semantic Role": "Not Applicable"
}
```

**Insight**: Each NP receives a **Semantic Role** based on its function. Core arguments (Agent/Patient) are distinguished from adjuncts (Temporal, Locative = "Not Applicable").

---

## Example 19: Implicit Information Field

Most clauses show:
```json
{
  "Part": "Clause",
  "Implicit Information": "Not Applicable"
}
```

**Potential Values** (from schema):
- Cultural
- Situational
- Historical
- Background
- Subactions
- Argument

**Insight**: This field flags when cultural, historical, or situational knowledge is required for interpretation.

---

## Example 20: Complete Clause Metadata (Genesis 1:1)

**Full Clause-Level Annotation**:
```json
{
  "Part": "Clause",
  "Type": "Independent",
  "Illocutionary Force": "Declarative",
  "Discourse Genre": "Climactic Narrative Story",
  "Topic NP": "Most Agent-like",
  "Speaker": "Not Applicable",
  "Listener": "Not Applicable",
  "Speaker's Attitude": "Not Applicable",
  "Speaker`s Age": "Not Applicable",
  "Speaker-Listener Age": "Not Applicable",
  "Speech Style": "Not Applicable",
  "Salience Band": "Not Applicable",
  "Sequence": "Not in a Sequence",
  "Location": "First in Book",
  "Notional Structure Schema": "Not Applicable",
  "Implicit Information": "Not Applicable",
  "Alternative Analysis": "Not Applicable",
  "Rhetorical Question": "Not Applicable",
  "Vocabulary Alternate": "Single Sentence - Complex Vocabulary Alternate"
}
```

**Insight**: Clauses carry **20+ metadata fields** covering discourse, pragmatic, and structural features. Most are "Not Applicable" for simple declarative sentences but activate for dialogue, questions, complex narrative structures.

---

## Summary of Key Patterns

### 1. Hierarchical Nesting
- Clauses → Phrases → Words
- Phrases can contain other phrases (e.g., AdjP within NP)

### 2. Consistent Field Structure
- Every element has **Part**
- Lexical elements have **Constituent**, **LexicalSense**, **SemanticComplexityLevel**
- Phrase-level elements have **Sequence**, **Implicit**
- Clauses have extensive discourse metadata

### 3. Coreference via NounListIndex
- Enables tracking participants across clauses
- Combined with Participant Tracking for discourse status

### 4. Controlled Vocabularies
- Fields like "Participant Tracking", "Time", "Aspect" use fixed value sets
- See SCHEMA.md for complete enumerations

### 5. Multiple Representations
- Same verse can appear multiple times with different vocabulary levels
- Marked by "Vocabulary Alternate" field

### 6. Discourse-Rich Encoding
- Speaker/Listener tracking
- Salience bands
- Illocutionary force
- Notional structure schemas

These examples demonstrate TBTA's comprehensive linguistic annotation system, suitable for translation assistance, linguistic analysis, and natural language understanding tasks.
