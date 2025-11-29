# TBTA Documentation Review: Discourse Genre

## What is Discourse Genre?

**Discourse Genre** identifies the type of discourse or literary form being used in a biblical text. It is a clause-level feature that helps translators understand the functional and structural characteristics of a passage to render it appropriately in the target language.

**Source**: {tbta-features-2025}

## TBTA Classification

**Tier**: A - Essential (Feature #14)
**Category**: Clause Features (Category 105)
**Status**: ✅ Complete
**Scope**: All languages
**Coverage**: 11,649 verses across 34 books (~37% of Bible)

**Source**: {tbta-features-2025}, {tbta-readme-2025}

## Documented Values

Based on TBTA source documentation, the following values are documented:

1. **Narrative** (including subtypes like "Climactic Narrative Story")
2. **Expository**
3. **Poetic**
4. **Legal**
5. **Prophetic**
6. **Epistolary**

**Source**: {tbta-features-2025}, {tbta-data-structure-2025}

### Example from TBTA Data

Genesis 1:1 is annotated with:
```json
{
  "Discourse Genre": "Climactic Narrative Story"
}
```

**Source**: {tbta-data-structure-2025}

## Conceptual Definition

### What Discourse Genre Represents

Discourse genre classification determines:
- **Functional purpose** of the text (telling a story vs. giving instructions vs. presenting arguments)
- **Structural patterns** expected (chronological events vs. logical development vs. poetic parallelism)
- **Translation strategies** needed (maintaining narrative flow vs. preserving logical connections vs. honoring poetic form)

**Source**: Internal analysis based on TBTA documentation

## Gateway Features & Constraints

### Controlling Features

**No explicit gateway features documented** in TBTA for Discourse Genre. The feature appears to be:
- **Clause-level**: Applied to clauses regardless of other grammatical features
- **Independent**: Not contingent on other features like Part of Speech, Mood, or Sentence Type
- **Discourse-scoped**: May apply to pericopes (OT) or individual verses (NT)

**Source**: {tbta-data-structure-2025}

### Data Structure Constraints

**Old Testament vs. New Testament Organization**:
- **Old Testament**: Organized by **pericopes** (thematic units spanning multiple verses)
- **New Testament**: Organized by **individual verses**

**Implication**: Discourse genre annotations in the OT may span multiple verses as a single unit, while NT annotations are verse-specific.

**Source**: {tbta-data-structure-2025}

## TBTA Policy & Methodology

### Semantic vs. Morphological Approach

**Not explicitly documented** for Discourse Genre. However, discourse genre is inherently:
- **Semantic/Functional**: Based on the communicative function of the text
- **Contextual**: Determined by analyzing multiple sentences/clauses together
- **Not morphologically encoded**: No specific morphemes mark genre in Hebrew/Greek

**Source**: Internal analysis

### Level of Annotation

**Clause-level feature**: Annotated at the clause level in TBTA's hierarchical structure:

```
Clause (root)
├── Discourse Genre: "Climactic Narrative Story"
├── Illocutionary Force: "Declarative"
├── Type: "Independent"
└── [Phrases and Words...]
```

**Source**: {tbta-data-structure-2025}

## Past Learnings

### TBTA's Strategic Coverage

TBTA deliberately prioritizes **narrative and discourse-heavy books** where cross-linguistic features (participant tracking, discourse genre, speaker demographics) matter most for translation.

**Books with less coverage**:
- Leviticus (legal/ritual genre is more uniform)
- Psalms (poetic genre with less discourse variation)

**Coverage by genre**:
- **Narrative**: ~8,500 verses (73% of TBTA coverage)
- **Other genres**: ~3,149 verses (27%)

**Source**: {tbta-coverage-2025}

### Integration with Other Features

Discourse Genre works in conjunction with:
- **Salience Band**: Foreground/Background/Setting/Pivotal distinctions within genres
- **Illocutionary Force**: Speech act type (Declarative, Interrogative, Imperative, etc.)
- **Participant Tracking**: How entities are introduced and tracked through narrative
- **Speaker/Listener**: Who is communicating (relevant for epistolary and direct speech)

**Source**: {tbta-features-2025}

## Edge Cases

### Genre Mixing

**Challenge**: Biblical texts often mix genres (e.g., narrative with embedded poetry, prophecy with legal commands).

**TBTA Handling**: Not explicitly documented. Likely handled by:
1. **Clause-level annotation**: Each clause receives its own genre marking
2. **Pericope boundaries** (OT): Genre shifts may align with pericope divisions
3. **Embedded structures**: Different genres for outer vs. embedded clauses

**Example potential cases**:
- Genesis 1:3 - Narrative frame ("God said") + Jussive speech ("Let there be light")
- Exodus 20 - Legal commands embedded in narrative context
- Psalms in narrative (e.g., Hannah's song in 1 Samuel 2)

**Source**: Internal analysis; specific TBTA handling not documented

### Genre Ambiguity

**Challenge**: Some texts blur genre boundaries:
- Wisdom literature that uses narrative examples
- Prophetic oracles that include legal material
- Epistles that contain hymnic poetry

**TBTA Handling**: Not explicitly documented

**Source**: Internal analysis

### Subgenres and Specificity

**Observed**: TBTA uses specific subtypes like "**Climactic Narrative Story**" rather than just "Narrative"

**Questions not answered in documentation**:
- How many subgenre values exist?
- What is the full taxonomy (e.g., "Climactic" vs. "Routine" vs. "Expository" narrative)?
- Are there specific values for wisdom literature, parables, genealogies, etc.?

**Source**: {tbta-data-structure-2025}; specific taxonomy not documented

## Value Inventory

### Documented Values (Confirmed)

| Value | Source | Context |
|-------|--------|---------|
| Climactic Narrative Story | {tbta-data-structure-2025} | Genesis 1:1 example |
| Narrative | {tbta-features-2025} | Listed as general category |
| Expository | {tbta-features-2025} | Listed as general category |
| Poetic | {tbta-features-2025} | Listed as general category |
| Legal | {tbta-features-2025} | Listed as general category |
| Prophetic | {tbta-features-2025} | Listed as general category |
| Epistolary | {tbta-features-2025} | Listed as general category |

### Potential Values (Theoretically Possible, Not Yet Confirmed)

Based on biblical literature and discourse analysis frameworks:

| Potential Value | Rationale | Likelihood |
|----------------|-----------|------------|
| Wisdom | Distinct genre in OT (Proverbs, Job, Ecclesiastes) | High |
| Apocalyptic | Distinct form of prophecy (Daniel, Revelation) | High |
| Genealogy | Distinct structural pattern in Genesis, Chronicles | Medium |
| Parable | Distinct narrative subtype in Gospels | Medium |
| Hymnic/Lyric Poetry | Distinct from didactic poetry | Medium |
| Procedural | "How to" instructions (Longacre taxonomy) | Medium |
| Hortatory/Behavioral | Exhortation (Longacre taxonomy) | Medium |

**Source**: Internal analysis based on biblical literature

### Theoretical vs. Productive Values

**Cannot determine from documentation**:
- Which values are **frequently used** vs. **rarely used**
- Whether all 6 documented values appear in the actual TBTA data
- Whether additional undocumented values exist in the database

**Note**: Frequency analysis belongs to Stage 2 (Analysis), not Stage 1 (Research).

**Source**: Per methodology instructions

## Mixed Annotations

**Not documented** for Discourse Genre.

**Hypothesis**: Discourse Genre is likely **single-valued** per clause, not multi-valued like Degree (which allows "Intensified" + "'too'").

**Rationale**: A clause functions as one primary genre type at a time, though genres can nest or transition at clause boundaries.

**Source**: Internal analysis; TBTA documentation does not address this

## Relationship to Source Languages

### Hebrew and Greek Encoding

**Discourse genre is NOT explicitly encoded in Hebrew or Greek morphology**.

Unlike features like Number (morphological suffixes) or Tense (verb conjugations), discourse genre is:
- **Inferred from context**: Determined by analyzing sentence structure, vocabulary, connectives, and broader discourse patterns
- **Suprasegmental**: Operates above the word and clause level
- **Functional**: Based on communicative purpose, not grammatical form

**Source**: Internal linguistic analysis

### Source Language Indicators

While not morphologically marked, certain **discourse markers and patterns** in Hebrew and Greek signal genre:

**Hebrew**:
- **Narrative**: Wayyiqtol verb chains, sequential action
- **Poetry**: Parallelism, terseness, metaphor
- **Legal**: Apodictic (commands) vs. casuistic (if-then) formulations
- **Prophecy**: Messenger formula ("Thus says the LORD")

**Greek**:
- **Narrative**: Historical present, aorist verb sequences
- **Epistolary**: Formulaic openings (χάρις καὶ εἰρήνη), closings
- **Expository**: Logical connectives (γάρ, οὖν, ἀλλά)
- **Apocalyptic**: Vision reports, symbolic imagery

**Source**: Standard biblical linguistic analysis (not TBTA-specific)

## Implications for Target Languages

### Universal Relevance

Discourse genre affects **all languages** because:
1. **Translation strategy varies by genre**: Narrative requires maintaining temporal flow; poetry requires preserving parallelism; legal requires precision; epistolary requires appropriate register
2. **Discourse markers differ by genre**: Connectives, participant reference, tense/aspect usage
3. **Cultural adaptation needed**: Some genres (apocalyptic, legal) may be unfamiliar in target culture

**Source**: {tbta-features-2025} lists "All languages"

### Language-Specific Challenges

Different languages may have:
- **Different genre systems**: Some cultures lack written legal codes, epistles, or apocalyptic literature
- **Different genre markers**: Narrative marked by tone (African languages), particles (Asian languages), or verb forms (most languages)
- **Genre-specific grammar**: Some languages use distinct grammatical features for narrative vs. non-narrative (e.g., switch-reference in Papua New Guinea languages)

**Source**: General translation theory

## Integration with myBibleToolbox

### Schema Mapping

Per TBTA source documentation:

| TBTA Field | myBibleToolbox Schema Section |
|------------|-------------------------------|
| Discourse Genre | `themes.genre` |

**Source**: {tbta-data-structure-2025}

### Data Transformation Requirements

1. **Pericope splitting**: OT data organized by pericopes must be split to verse-level for consistency
2. **File naming**: Convert to `/commentary/{BOOK}/{chapter:03d}/{BOOK}-{chapter:03d}-{verse:03d}-tbta.yaml`
3. **Format conversion**: JSON → YAML
4. **Citation addition**: Add inline citations for all TBTA-sourced data

**Source**: {tbta-data-structure-2025}

## Gaps in Documentation

The following aspects are **not documented** in TBTA source materials:

1. **Complete value taxonomy**: Full list of all possible genre values and subgenres
2. **Value definitions**: Precise criteria for assigning each genre value
3. **Genre mixing policy**: How embedded genres, transitions, or ambiguous cases are handled
4. **Frequency distribution**: Which values are common vs. rare (belongs to Stage 2)
5. **Inter-annotator reliability**: How consistently this feature is annotated
6. **Relationship to book-level genre**: How clause-level annotations relate to book-level classifications

**Source**: Comprehensive review of TBTA documentation

## Research Questions for Stage 2+

These questions **cannot be answered** from TBTA documentation alone:

1. What is the **complete list of all values** used in the TBTA database?
2. How frequently does each value appear?
3. How does TBTA handle **genre transitions** within a single verse?
4. Are there **book-level or chapter-level** patterns in genre annotation?
5. What **linguistic features** (vocabulary, syntax, connectives) correlate with each genre?
6. How do translators in marking languages handle different genres?

**Source**: Internal analysis

## Summary

### What We Know

- **Definition**: Discourse genre is the type of discourse/literary form (narrative, expository, poetic, legal, prophetic, epistolary)
- **Scope**: Clause-level feature, applicable to all languages
- **Values**: At least 6 documented categories, with evidence of subtypes (e.g., "Climactic Narrative Story")
- **Status**: Tier A Essential feature, marked as Complete in TBTA
- **Coverage**: ~11,649 verses with 73% narrative

### What We Don't Know (From TBTA Docs)

- **Complete taxonomy**: Full list of all genre values and subgenres
- **Annotation guidelines**: Specific criteria for assigning values
- **Edge case handling**: How genre mixing, ambiguity, and transitions are resolved
- **Frequency data**: Distribution of values across the corpus (Stage 2 task)

### Key Discrepancy to Investigate

**TBTA lists vs. Linguistic frameworks**:
- TBTA documentation lists 6 values: Narrative, Expository, Poetic, Legal, Prophetic, Epistolary
- Longacre linguistic framework uses 4 values: Narrative, Procedural, Behavioral/Hortatory, Expository
- Traditional biblical genres: Law, Narrative, Poetry, Wisdom, Prophecy, Gospels/Acts, Epistles, Apocalyptic

**Question for Stage 2**: How does TBTA's taxonomy map to established frameworks?

## Citation Codes

- `{tbta-features-2025}`: /workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md
- `{tbta-readme-2025}`: /workspace/bible-study-tools/tbta/tbta-source/README.md
- `{tbta-data-structure-2025}`: /workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md
- `{tbta-coverage-2025}`: /workspace/bible-study-tools/tbta/tbta-source/COVERAGE.md

---

**Completed**: 2025-11-29
**Next Step**: Language Family & Typology Analysis (LANGUAGES.md)
