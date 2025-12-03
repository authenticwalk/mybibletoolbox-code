# TBTA Documentation Review: Semantic Role

## 1. Concept Definition

**Source**: `/workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md` (line 46)

Semantic Role is a **Noun Phrase feature** (Category 101) that indicates the thematic role or semantic relationship of a noun phrase to its governing verb. It belongs to **Tier A: Essential Features** (priority: highest), affecting 1000+ languages and cannot be easily inferred from context alone.

**Citation**: {tbta-features-2025}

### Linguistic Foundation

Semantic roles (also called thematic roles or theta roles) represent the semantic relationship between a verb and its arguments. They answer questions like:
- Who performs the action? (Agent)
- Who/what is affected? (Patient)
- What is the origin? (Source)
- What is the destination/goal? (Destination)
- What is used to perform the action? (Instrument)
- Who benefits? (Beneficiary)
- Who is addressed? (Addressee)

**Citation**: {tbta-features-2025}

## 2. TBTA Values

**Source**: `/workspace/plan/tbta/tbta-rebuild-with-llm/tbta-data/SCHEMA.md` (lines 364-387)

### Primary Values (Single-Letter Codes)

| Code | Full Value | Description |
|------|------------|-------------|
| A | Agent-like | Doer of the action (volitional, controlling) |
| P | Patient-like | Undergoer of the action (affected entity) |
| S | State | Experiencer, possessor, or entity in a state |
| s | Source | Origin or starting point |
| d | Destination | Goal or endpoint |
| I | Instrument | Means or tool by which action is performed |
| D | Addressee | Recipient of communication |
| B | Beneficiary | Entity for whose benefit the action is performed |
| N | Not Applicable | Adjunct roles (not core arguments) |

**Citation**: {tbta-schema-2025}

### Special Extended Values

| Value | Description |
|-------|-------------|
| Most Agent-like | Prototypical agent (highest degree of agency) |
| Most Patient-like | Prototypical patient (most affected participant) |

**Source**: `/workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md` (lines 114, 151, 166)

Examples from Genesis 1:1:
- "God" → Semantic Role: "Most Agent-like" (creator, volitional actor)
- "sky" → Semantic Role: "Most Patient-like" (created entity)
- "earth" → Semantic Role: "Most Patient-like" (created entity)

**Citation**: {tbta-data-structure-2025}

## 3. Gateway Features (Constraints)

**Source**: Direct inspection of TBTA schema

### Part of Speech Constraint

Semantic Role is **ONLY applicable to Noun Phrases (NP)**, not individual nouns.

**Evidence**:
- Field appears under "Noun Phrase (NP)" section in schema (line 364)
- Individual nouns (Part: "Noun") do not have Semantic Role field
- Only phrasal NP constituents carry this annotation

**Citation**: {tbta-schema-2025}

### Argument vs Adjunct Distinction

**Code "N" (Not Applicable)** marks adjuncts - elements that are not required by the verb's argument structure:
- Time adjuncts: "yesterday", "in the morning"
- Location adjuncts (when not required): "in the house" (if not a required destination)
- Manner adjuncts: "with great care"

**Core arguments** receive specific role codes (A, P, S, s, d, I, D, B).

**Citation**: {tbta-schema-2025}

### Clause Type Interaction

Not explicitly documented, but inferred: Semantic roles interact with:
- **Voice**: Passive voice may suppress Agent or promote Patient to subject
- **Clause Type**: Different clause types (main, subordinate, relative) may have different argument structures
- **Illocutionary Force**: Imperatives often have implicit agents (second person)

**Status**: Not listed in documentation (inference from linguistic theory)

## 4. TBTA Policy

### Semantic vs Morphological

**Finding**: TBTA appears to prioritize **SEMANTIC** interpretation over pure morphological case marking.

**Evidence**:
1. Greek nominative case can mark both Agent-like subjects AND Patient-like subjects in passive constructions
2. The same morphological case (e.g., accusative) can correspond to multiple semantic roles depending on the verb
3. Values like "Most Agent-like" and "Most Patient-like" refer to semantic prototypicality, not morphological form

**Source**: Inference from TBTA-FEATURES.md which notes "Ergative languages, Filipino" as example languages (line 46), suggesting TBTA handles both nominative-accusative and ergative-absolutive systems semantically.

**Citation**: {tbta-features-2025}

### Part-of-Speech Rules

**Documented**: Semantic Role is assigned at the **Noun Phrase level**, not word level.

**Implications**:
- Pronouns within NPs inherit the NP's semantic role
- Coordination: Each coordinated NP can have its own semantic role (e.g., "God created [the sky]_Patient and [the earth]_Patient")
- Genitive constructions: Possessor NPs embedded within larger NPs may have different roles than their container

**Citation**: {tbta-schema-2025}

## 5. Past Learnings

**Source**: `/workspace/bible-study-tools/tbta/tbta-source/CRITIQUE.md`

### Morphological vs Semantic Encoding

**Issue identified** (line 142-168):
> "Morphological vs. Semantic Number Confusion"
> - TBTA correctly chooses semantic interpretation (lexicalized duals treated as singular if semantically one entity)
> - Need explicit "morphological vs. semantic" distinction

**Implication for Semantic Role**: TBTA's approach is **semantically-driven**, not purely morphologically-driven. This explains why they use descriptive labels like "Most Agent-like" rather than purely syntactic labels like "Subject" or morphological labels like "Nominative".

**Citation**: {tbta-critique-2025}

### Encoding Level Decisions

**Finding** (CRITIQUE.md, line 356):
> "Single annotation level (no morphological vs. semantic distinction)"

TBTA does **not** provide dual layers (morphological case + semantic role). Only semantic roles are annotated. This means:
- Greek nominative case → inferred as Agent-like or Patient-like based on semantics
- Greek accusative case → could be Patient, Destination, or other roles
- Hebrew prepositional phrases → analyzed for their semantic contribution

**Citation**: {tbta-critique-2025}

## 6. Edge Cases

### Case 1: Coordination of Unlike Roles

**Example**: "God created [the sky]_Patient and spoke to [Adam]_Addressee"

**Handling**: Each coordinated NP receives independent Semantic Role annotation.

**Evidence**: DATA-STRUCTURE.md shows coordinated NPs (lines 146-171) with:
- First Coordinate: Semantic Role "Most Patient-like"
- Last Coordinate: Semantic Role "Most Patient-like"

Both receive the **same** role in this example, but the schema allows different roles for each coordinate.

**Citation**: {tbta-data-structure-2025}

### Case 2: Embedded/Subordinate Clauses

**Finding**: Not explicitly documented how semantic roles are assigned in:
- Relative clauses
- Complement clauses
- Infinitival clauses

**Status**: Not listed in available documentation

### Case 3: Implicit Arguments

**Related field**: NP "Implicit" values (SCHEMA.md, lines 397-407) include:
- "A" - Optional Passive Agent
- "I" - Implicit Argument

**Implication**: Implicit NPs still receive Semantic Role annotations even when not overtly expressed.

**Example**: "The bread was eaten [by someone]_Agent" - the agent is implicit but could be annotated.

**Citation**: {tbta-schema-2025}

### Case 4: Ambiguous/Dual Roles

**Finding**: No documentation of how TBTA handles arguments with dual semantic properties.

**Linguistic Example**:
- "John loaded the truck with hay" - is "truck" a Patient (undergoes change) or Destination?
- "The key opened the door" - is "key" an Instrument (used to open) or Agent-like (caused opening)?

**Status**: Not listed in available documentation

## 7. Value Inventory

### Documented Values (9 total)

**Source**: SCHEMA.md (lines 370-387)

| Value | Linguistic Label | Frequency Status |
|-------|------------------|------------------|
| A | Agent-like | **Productive** (common) |
| P | Patient-like | **Productive** (common) |
| S | State (Experiencer/Possessor) | **Productive** (common) |
| s | Source | Productive |
| d | Destination | Productive |
| I | Instrument | Productive |
| D | Addressee | Productive |
| B | Beneficiary | Productive |
| N | Not Applicable (Adjunct) | **Productive** (common) |

**Extended forms**:
- "Most Agent-like" - highest prototypicality
- "Most Patient-like" - highest prototypicality

**Citation**: {tbta-schema-2025}

### Theoretical Values (Mentioned in Linguistic Literature but Not in TBTA Schema)

The following roles are **NOT** documented in TBTA but exist in semantic role literature:

| Role | Description | Why potentially absent |
|------|-------------|------------------------|
| Theme | Moving entity | May be subsumed under Patient-like |
| Experiencer | Entity experiencing mental/emotional state | May be subsumed under "S" (State) |
| Goal | Endpoint of motion | May be identical to "d" (Destination) |
| Recipient | Receiver of transfer | May be subsumed under Addressee or Beneficiary |
| Location | Place where event occurs | Marked as "N" (Not Applicable/Adjunct)? |
| Time | Temporal setting | Marked as "N" (Not Applicable/Adjunct) |
| Comitative | Accompaniment ("with X") | Not documented |
| Cause | Non-volitional causer | Not documented |
| Stimulus | Trigger of perception/emotion | Not documented |

**Note**: TBTA uses a **simplified 9-value system** rather than the 20+ roles found in some linguistic frameworks. This reflects practical translation needs rather than exhaustive theoretical categorization.

### Rare Value Discovery

**Source**: TBTA-FEATURES.md (line 46) mentions "Ergative languages, Filipino" as key example languages.

**Implication**: Values like:
- **Instrument** ("I") - may be rare in English but common in languages with instrumental case or specific instrumental voice (Filipino -ipang-)
- **Beneficiary** ("B") - may be rare in basic narratives but common in languages with benefactive applicatives (Bantu languages, Austronesian)

**Status**: Frequency analysis deferred to Stage 2 (not part of this research phase)

## 8. Mixed Annotations

**Finding**: TBTA does **NOT** allow multiple Semantic Role values for a single NP.

**Evidence**: Schema shows Semantic Role as a single string field, not an array.

**Contrast with Other Features**:
- **Degree** (adjectives/adverbs) allows mixed annotations like "Intensified" + "'too'" (TBTA-FEATURES.md notes some features have 20+ instances per 100 verses)
- **Semantic Role** appears to be mutually exclusive - an NP is either Agent-like OR Patient-like, not both

**Citation**: {tbta-schema-2025}

### Potential Exception: State Role

The **"S" (State)** role may cover multiple sub-types:
- Experiencer: "John felt happy" (John = Experiencer)
- Possessor: "John has a book" (John = Possessor)
- Location: "The book is on the table" (book = Theme/located entity)

These are **not** mixed annotations, but rather a single broad category encompassing related semantic types.

**Citation**: {tbta-schema-2025}

## 9. Mapping to Source Languages

### Greek (Koine)

**Morphological Encoding**: Greek has a **4-case system** (nominative, genitive, dative, accusative) + vocative.

**Semantic Role Mapping**:
| Greek Case | Typical Semantic Roles |
|------------|------------------------|
| Nominative | Agent-like (subject), Patient-like (passive subject) |
| Accusative | Patient-like (direct object), Destination (motion verbs), State (some verbs) |
| Genitive | Possessor (embedded in NP), Source, Partitive |
| Dative | Addressee (indirect object), Beneficiary, Location, Instrument |

**Key Point**: Greek morphological cases **do not map 1:1** to TBTA semantic roles. Context and verb semantics determine the semantic role.

**Source**: Inference from linguistic knowledge (not explicitly documented in TBTA)

### Hebrew (Biblical)

**Morphological Encoding**: Hebrew has **limited overt case marking**. Roles are expressed through:
- Prepositions: לְ (to/for), מִן (from), בְּ (in/with), אֶת (direct object marker)
- Word order: VSO typically
- Construct state for possession

**Semantic Role Marking**:
| Hebrew Marker | Typical Semantic Roles |
|---------------|------------------------|
| (no marker, pre-verbal) | Agent-like (subject) |
| אֶת + noun | Patient-like (definite direct object) |
| לְ + noun | Addressee, Beneficiary, Destination |
| מִן + noun | Source, Cause |
| בְּ + noun | Instrument, Location, State |
| עִם + noun | Comitative (accompaniment) |

**Source**: Inference from linguistic knowledge (not explicitly documented in TBTA)

## 10. TBTA Example Analysis

**Source**: DATA-STRUCTURE.md, Genesis 1:1 example (lines 100-175)

### Example: "In the beginning God created the sky and the earth"

**Clause Structure**:
```json
{
  "Part": "Clause",
  "Type": "Independent",
  "Children": [
    {
      "Part": "AdvP",
      "Children": [{"Constituent": "In the beginning"}]
    },
    {
      "Part": "NP",
      "Semantic Role": "Most Agent-like",
      "Children": [{"Constituent": "God", "NounListIndex": "1"}]
    },
    {
      "Part": "VP",
      "Children": [{"Constituent": "created"}]
    },
    {
      "Part": "NP",
      "Sequence": "First Coordinate",
      "Semantic Role": "Most Patient-like",
      "Children": [{"Constituent": "sky", "NounListIndex": "2"}]
    },
    {
      "Part": "NP",
      "Sequence": "Last Coordinate",
      "Semantic Role": "Most Patient-like",
      "Children": [{"Constituent": "and", "Part": "Conjunction"}, {"Constituent": "earth", "NounListIndex": "3"}]
    }
  ]
}
```

**Semantic Role Assignments**:
- "God" → **Most Agent-like** (volitional creator, controller)
- "the sky" → **Most Patient-like** (created entity, affected)
- "the earth" → **Most Patient-like** (created entity, affected)
- "In the beginning" → **No Semantic Role** (it's an AdvP, not an NP)

**Key Observations**:
1. Only NPs receive Semantic Role annotations
2. Both coordinated Patients receive identical role assignment
3. "Most Agent-like" and "Most Patient-like" used for prototypical cases
4. Temporal/manner adjuncts (AdvPs) are not assigned semantic roles

**Citation**: {tbta-data-structure-2025}

## 11. Schema Mapping

**Source**: DATA-STRUCTURE.md (line 401)

**TBTA field**: `Semantic Role` (on NP elements)

**Maps to our commentary schema**: `grammar.syntax`

This indicates that semantic roles are treated as **syntactic-level information** in the TBTA-to-commentary pipeline, distinct from:
- `grammar.morphology` (Number, Person, Case)
- `context.discourse` (Participant Tracking)
- `context.pragmatics` (Illocutionary Force)

**Citation**: {tbta-data-structure-2025}

## 12. Summary

### What We Know (Documented)

1. **Concept**: Thematic relationship between NP and governing verb
2. **Values**: 9 values (A, P, S, s, d, I, D, B, N) + extended forms ("Most Agent-like", "Most Patient-like")
3. **Scope**: Noun Phrase level only
4. **Tier**: Tier A (Essential) - affects 1000+ languages
5. **Example languages**: Ergative languages, Filipino
6. **Policy**: Semantically-driven (not purely morphological)
7. **Coordination**: Each coordinated NP gets independent role
8. **Implicit arguments**: Can be annotated even when not overt

### What We Don't Know (Not Documented)

1. **Frequency**: How common is each value? (deferred to Stage 2)
2. **Ambiguous cases**: How are dual-role arguments handled?
3. **Subordinate clauses**: How are roles assigned in embedded clauses?
4. **Language-specific handling**: How does TBTA adapt roles for ergative vs nominative-accusative languages?
5. **Theoretical motivation**: Why these 9 values and not others?
6. **Inter-annotator agreement**: How reliable are human annotations?
7. **Diachronic changes**: Do roles change across Biblical Hebrew vs Koine Greek periods?

### Discrepancies and Questions

1. **Name variation**: Source documentation lists "Agent, Patient, Source..." (TBTA-FEATURES.md) but schema uses "Agent-like, Patient-like, State, Source..." (SCHEMA.md). The "-like" suffix appears to be the actual implementation.

2. **Prototypicality**: Why use "Most Agent-like" vs just "A" in some contexts? Hypothesis: "Most" is used for prototypical, unambiguous cases, while bare codes (A, P) allow for less prototypical instances. **Needs verification in Stage 2**.

## References

- {tbta-features-2025}: `/workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`
- {tbta-schema-2025}: `/workspace/plan/tbta/tbta-rebuild-with-llm/tbta-data/SCHEMA.md`
- {tbta-data-structure-2025}: `/workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md`
- {tbta-critique-2025}: `/workspace/bible-study-tools/tbta/tbta-source/CRITIQUE.md`
