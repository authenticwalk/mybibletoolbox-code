<<<<<<< HEAD
# Discourse Genre Feature

**Discourse genre** identifies the functional type of discourse (narrative, teaching, law, poetry, etc.) at the clause level. It determines grammatical choices for tense, aspect, word order, vocabulary, and discourse markers in target languages.
=======
# Discourse Genre

**TBTA Feature #14** | Tier A - Essential | Clause-Level | All Languages
>>>>>>> origin/feat/self-learning-tbta

## Quick Facts

| Property | Value |
<<<<<<< HEAD
|---|---|
| **TBTA ID** | #14 (Tier A, Clause-level) |
| **Source Encoding** | NOT morphological (Hebrew/Greek) |
| **Documented Values** | 9 (Climactic Narrative, Background, Procedural, Expository, Poetic, Hortatory, Prophetic, Legal, Epistolary) |
| **Data Reality** | 1 value observed in TBTA (11% coverage) |
| **Target Languages Affected** | 300-500+ languages require genre-aware translation |
| **Theological Stakes** | **CRITICAL** (35% non-arbitrary, 20% theological) |

## High-Stakes Examples

| Verse | Genre | **WRONG CHOICE** | **RIGHT CHOICE** |
|---|---|---|---|
| Genesis 1:1-2:3 | Narrative (elevated prose) | ❌ **Myth/allegory** → Denies creation doctrine | ✅ Historical narrative |
| Matthew 5-7 | Teaching (expository) | ❌ Narrative tense → Flattens theological discourse | ✅ Timeless present |
| Exodus 20:13 | Legal (apodictic law) | ❌ Narrative forms → Weakens commands | ✅ Imperative/conditional |
| Psalm 23:1 | Poetry (not narrative) | ❌ Narrative wayyiqtol → Grammatically impossible | ✅ Poetic forms |
| Revelation 1-22 | Apocalyptic (symbolic prophecy) | ❌ Purely literal → False date-setting, absurd interpretation | ✅ Apocalyptic with symbolic conventions |

## Target Audience & Languages

**Mandatory marking**: French, Spanish, Portuguese, Italian, German, Bantu languages (89+), Mandarin, Japanese, most Austronesian (176 languages). Genre-tense mismatch produces ungrammatical sentences.

**Details**: See `research/LANGUAGES.md` for 8 Stage 2 candidate languages and typological classification.

## TBTA Encoding

Clause-level annotation in hierarchical structure: `Discourse Genre: "Climactic Narrative Story"` (context-dependent semantics, NOT part-of-speech rules).

**Data Status**: Only 1 of 9 values observed across 12,091 annotations. Algorithm must rely on linguistic theory + book-type classification; TBTA data currently insufficient for validation except Climactic Narrative.

**Details & Research**: See `research/README.md` (synthesis) and `research/SCHOLARLY.md` (30+ scholarly sources).
=======
|----------|-------|
| **Feature Type** | Discourse/Literary Form Classification |
| **TBTA Tier** | A - Essential (affects 1000+ languages, cannot be easily inferred) |
| **Scope** | Clause-level annotation |
| **Values** | 6+ documented: Narrative, Expository, Poetic, Legal, Prophetic, Epistolary (+ subtypes) |
| **Source Encoding** | NOT morphological - inferred from discourse patterns |
| **Universal?** | YES - all languages require genre awareness for appropriate translation |
| **Theological Stakes** | HIGH (~15% of contexts theologically critical) |
| **Coverage** | 11,649 verses (~37% of Bible), 73% narrative |

## Feature Description

Discourse genre identifies the **functional type of discourse** used to accomplish communicative purposes in biblical text. Genre affects translation strategy, grammatical choices, information structure, and register/style.

**Examples**:
- **Narrative**: Genesis 1, Acts, Gospels (tells story with temporal sequence, agent focus)
- **Poetry**: Psalms, Song of Solomon (parallelism, metaphor, elevated language)
- **Legal**: Exodus 20, Leviticus (commands, prohibitions, case law)
- **Prophecy**: Isaiah, Jeremiah (divine message through prophet)
- **Wisdom**: Proverbs, Ecclesiastes (practical guidance, general principles)
- **Epistolary**: Romans, Ephesians (letter with sender-recipient, expository + hortatory)
- **Apocalyptic**: Revelation, Daniel (symbolic-visionary divine revelation)

## Target Audiences

### All Languages Affected

Genre awareness required for ALL languages, though manifestation differs:

**Morphological Marking** (~40% of languages):
- **Swahili** (Niger-Congo): Narrative tense ka- obligatory for sequential narrative
- **Spanish** (Indo-European): Preterite/imperfect distinction correlates with narrative vs. background
- **Russian** (Indo-European): Perfective/imperfective aspect distribution varies by genre

**Syntactic Marking** (~30% of languages):
- **Enga, Kewa** (Trans-New Guinea, ~250 languages): Switch-reference density high in narrative
- **Arabic** (Afro-Asiatic): VSO for narrative foreground, SVO for background
- **Japanese** (Japonic): Sentence-final particles signal genre-relevant speech acts

**Lexical Marking** (~25% of languages):
- **English, Malay** (various): Connectives differ by genre (narrative "then", expository "therefore")
- **Greek NT**: γάρ (expository), οὖν (hortatory), δέ (narrative continuity)
- **Hebrew OT**: Wayyiqtol (narrative), weqatal (non-narrative)

**Register/Style** (~5% of languages, overlaps with others):
- **Japanese, Korean, Javanese**: Honorifics interact with epistolary genre
- **Thai, Khmer**: Speech levels correlate with genre and social context

**See** [research/LANGUAGES.md](research/LANGUAGES.md) for complete typological analysis of ~1,008 languages.

### Special Challenges

**Missing Genre Traditions**:
- **Epistolary**: Oral cultures lack written letter conventions (PNG languages, ~250)
- **Legal Codes**: Customary oral law vs. codified written law (minority languages)
- **Apocalyptic**: Symbolic-visionary genre unfamiliar in many cultures

**Emerging Written Genres**: Bible translation often creates written genre conventions for languages with strong oral traditions.

## Critical Translation Examples

### Genesis 1-2: Narrative vs. Poetry Debate

| Approach | Genre | Interpretation | Orthodox Status |
|----------|-------|----------------|-----------------|
| ✅ Conservative | **Narrative** | Historical, sequential 6-day creation | **Preferred** (majority view) |
| ⚠️ Framework | Poetry/Elevated | Theological framework, non-sequential | **Acceptable** (Reformed minority) |
| ❌ Liberal | Mythology | Non-historical, symbolic only | **FORBIDDEN** (rejects authority) |

**Why It Matters**: Genre determines whether Genesis 1 describes historical events or theological framework. Affects creation theology, biblical inerrancy debates.

### Revelation: Apocalyptic vs. Literal Narrative

| Approach | Genre | Interpretation | Result |
|----------|-------|----------------|--------|
| ✅ Orthodox | **Apocalyptic-Prophecy** | Symbolic imagery with theological truth | Correct interpretation |
| ❌ Hyper-literal | Plain Narrative | Literal seven-headed beasts, dragons | Bizarre, cult-prone errors |
| ❌ Allegory-only | Pure Allegory | Arbitrary symbols, no future reference | Denies prophetic content |

**Why It Matters**: Apocalyptic uses culturally-coded symbols (from Daniel, Ezekiel). Literalizing leads to absurd interpretations; allegorizing removes prophetic force.

**CRITICAL**: Distinguish apocalyptic (coded symbols) from mythology (false) and plain narrative (wrong genre).

### Parables: Teaching Stories vs. Historical Events

| Text | Genre | Truth Claim |
|------|-------|-------------|
| ✅ Luke 15:11-32 (Prodigal Son) | **Parable** | Theological truth via fictional narrative |
| ❌ Treating as history | Narrative | **FALSE** - creates non-existent historical event |

**Why It Matters**: Parables are explicitly fictional ("He spoke to them in parables"). Treating as history falsely claims events happened.

### Proverbs: Wisdom vs. Legal Promises

| Approach | Genre | Interpretation | Problem |
|----------|-------|----------------|---------|
| ✅ Orthodox | **Wisdom** | General principles, "usually true" | Correct understanding |
| ❌ Prosperity Gospel | Legal/Prophetic | Absolute promises, "always true" | **Heretical** - creates false expectations |

**Example**: Proverbs 22:6 "Train up a child..." is **general wisdom**, not absolute guarantee. Treating as legal promise creates prosperity gospel errors.

## TBTA Encoding

### Clause-Level Feature

```
Clause (root)
├── Discourse Genre: "Climactic Narrative Story"  # <-- This feature
├── Illocutionary Force: "Declarative"
├── Type: "Independent"
└── [Phrases and Words...]
```

### Data Structure

**Old Testament**: Organized by pericopes (multi-verse units) - must split to verse-level for myBibleToolbox
**New Testament**: Organized by individual verses

**Integration**: Maps to `themes.genre` in myBibleToolbox commentary schema

### Known Values (From TBTA Docs)

1. Narrative (+ subtypes: "Climactic Narrative Story")
2. Expository
3. Poetic
4. Legal
5. Prophetic
6. Epistolary

**Potential additional values** (from research): Wisdom, Apocalyptic, Procedural, Hortatory, Descriptive, Parable, Genealogy (requires Stage 2 analysis to confirm).

## Scholarly Frameworks

### Longacre's Functional Taxonomy (4 main types)

| Type | Agent Focus | Temporal Succession | Biblical Examples |
|------|-------------|---------------------|-------------------|
| **Narrative** | + | + (contingent) | Genesis, Acts, Gospels |
| **Procedural** | - | + (contingent) | Leviticus (sacrificial instructions) |
| **Hortatory/Behavioral** | + | - (non-contingent) | Exhortations in Epistles, Deuteronomy |
| **Expository** | - | - (non-contingent) | Romans 1-11, theological arguments |

**Source**: Longacre (1996) *The Grammar of Discourse*

### Traditional Biblical Genres (7-8 types)

1. **Law/Legal** - Exodus-Deuteronomy
2. **Narrative** - Genesis-Esther, Gospels, Acts (43% of Bible)
3. **Poetry** - Psalms, Song of Solomon (33%)
4. **Wisdom** - Proverbs, Job, Ecclesiastes
5. **Prophecy** - Isaiah-Malachi
6. **Epistles** - Romans-Jude (24% as "discourse")
7. **Apocalyptic** - Daniel, Revelation
8. **Gospels** - Unique biographical-theological narrative

**See** [research/SCHOLARLY.md](research/SCHOLARLY.md) for 25+ scholarly sources with full bibliography.

## TBTA Data Distribution

**Extraction Date**: 2025-11-29
**Total Annotations**: 72,505 clause-level annotations

| Value | Count | Percentage |
|-------|-------|-----------|
| Climactic Narrative Story | 72,440 | 99.9% |
| Genealogy | 62 | 0.1% |
| Expository | 3 | 0.0% |

**Key Findings**:
- Only **3 unique values** found in TBTA data (vs. 6+ documented)
- Extreme imbalance: 99.9% Narrative, with minimal Genealogy/Expository
- Missing expected values: Poetry, Legal, Prophetic, Epistolary, Parabolic
- **Implication**: TBTA only annotated narrative portions; other genres require inference or additional sources

See [analysis/distribution.yaml](analysis/distribution.yaml) for detailed distribution analysis.

## Development Status

✅ **Stage 1: Research & Definition** - COMPLETE (2025-11-29)

**Completed**:
- TBTA documentation review ([research/TBTA.md](research/TBTA.md))
- Language family & typology analysis ([research/LANGUAGES.md](research/LANGUAGES.md))
- Scholarly research with 25+ sources ([research/SCHOLARLY.md](research/SCHOLARLY.md))
- Theological classification ([research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml))
- Research summary ([research/README.md](research/README.md))

🔄 **Stage 2: Analysis & Hypothesis Validation** - IN PROGRESS (2025-11-29)

**Step 1A Complete**:
- TBTA data extracted: 72,505 annotations from 11,649 verses
- Distribution analysis: 3 unique values (Climactic Narrative Story, Genealogy, Expository)
- See [analysis/distribution.yaml](analysis/distribution.yaml)

**Next**: Step 1B - Create balanced dataset with strongs_number and reason_group

## Key Learnings

### Universal but Not Morphological

- **All languages** require genre awareness for natural translation
- **Source languages** (Hebrew, Greek) do NOT morphologically encode genre
- Genre inferred from **discourse patterns**: verb sequences, particles, formulas, parallelism, vocabulary
- **Implication**: Algorithm requires multi-level discourse analysis, not single-morpheme lookup

### Typological Diversity

- **~1,008 languages** in dataset across all major families
- **Diverse marking strategies**: morphological, syntactic, lexical, prosodic, register
- **Some languages** have specialized narrative grammar (switch-reference, narrative tenses)
- **Some genres** missing in target cultures (epistolary, legal codes) - emerging through Bible translation

### Theological Significance

- **~15% theologically critical**: Wrong genre → heresy or serious misinterpretation
- **High stakes**: Genesis 1-2, Revelation, Parables (3 contexts)
- **Medium stakes**: Psalms, Proverbs, Job, Jonah, Legal codes, Epistles, Gospels (9 contexts)
- **~85% arbitrary**: Subtype distinctions (narrative vs. historical-narrative) that don't affect theology

## Resources

### Research Files (Stage 1)

- **[research/README.md](research/README.md)** - Executive summary (200 lines max)
- **[research/TBTA.md](research/TBTA.md)** - Complete TBTA documentation analysis
- **[research/LANGUAGES.md](research/LANGUAGES.md)** - Language families, typology, 10 control languages
- **[research/SCHOLARLY.md](research/SCHOLARLY.md)** - 25+ scholarly sources with bibliography
- **[research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)** - Theological classification

### Methodology

- **[STAGES.md](../.instructions-to-build-feature/STAGES.md)** - 6-stage development process
- **[STAGE-1-RESEARCH.md](../.instructions-to-build-feature/STAGE-1-RESEARCH.md)** - Research instructions (followed for this work)

---

**Last Updated**: 2025-11-29
**Status**: Stage 1 Complete
**Next Step**: Stage 2 - Translation Database (10 languages, 100+ verses per genre value)
>>>>>>> origin/feat/self-learning-tbta
