# Discourse Genre: Research Summary

**Stage**: 1 - Research & Definition
**Status**: Complete
**Date**: 2025-11-29

## Executive Summary

**Discourse Genre** identifies the type of discourse or literary form being used in biblical text (narrative, poetry, prophecy, legal, wisdom, epistolary, apocalyptic). It is a **clause-level feature** in TBTA, marked as **Tier A Essential** (affects all languages, cannot be easily inferred).

**Key Finding**: Genre is **NOT encoded morphologically** in Hebrew/Greek but is **inferred from discourse patterns** (verb sequences, particles, formulas, parallelism). This affects algorithm development - cannot rely on single morpheme, requires **holistic discourse analysis**.

**Universal Relevance**: ALL ~1,008 languages in our dataset require genre awareness, though marking strategies differ dramatically (morphological, syntactic, lexical, prosodic).

**Theological Significance**: Genre recognition affects **interpretation and application** (~15% theologically critical contexts where wrong genre leads to heresy or serious misinterpretation).

## Feature Definition

### What is Discourse Genre?

**Conceptual**: The functional type of discourse used to accomplish communicative purposes:
- **Narrative**: Tells a story with temporal sequence and agent focus
- **Poetry**: Uses parallelism, metaphor, elevated language
- **Prophecy**: Divine message through appointed spokesperson
- **Legal**: Commands, prohibitions, case law
- **Wisdom**: Practical guidance and general life principles
- **Epistolary**: Letter format with sender-recipient relationship
- **Apocalyptic**: Symbolic-visionary revelation of divine plans
- **Expository**: Logical explanation and argumentation
- **Hortatory**: Exhortation and ethical instruction

### TBTA Implementation

**Values Documented** (6 main categories):
1. Narrative (including subtypes like "Climactic Narrative Story")
2. Expository
3. Poetic
4. Legal
5. Prophetic
6. Epistolary

**Note**: Full taxonomy not documented. Evidence of subtypes (e.g., "Climactic Narrative Story" in Gen 1:1).

**Coverage**: 11,649 verses (~37% of Bible), focusing on narrative-heavy books (73% narrative).

**Scope**: Clause-level annotation, all languages affected.

**Source**: [research/TBTA.md](TBTA.md) - Complete TBTA documentation review

## Linguistic Frameworks

### Longacre's Functional Taxonomy (4 main types)

Distinguished by **agent focus**, **temporal succession**, **projection**:

| Type | Agent Focus | Temporal Succession | Examples |
|------|-------------|---------------------|----------|
| **Narrative** | + | + (contingent) | Stories, accounts, historical narrative |
| **Procedural** | - | + (contingent) | Instructions, "how to" |
| **Behavioral/Hortatory** | + | - (non-contingent) | Exhortation, commands, advice |
| **Expository** | - | - (non-contingent) | Explanation, description, argument |

Each type has 2 subtypes (e.g., Narrative: story, future events).

**Source**: Longacre (1996) *The Grammar of Discourse*; Longacre & Hwang (2012) *Holistic Discourse Analysis*

### Traditional Biblical Genres (7-8 types)

Form-based classification:

1. **Law/Legal**: Exodus-Deuteronomy legal codes
2. **Narrative**: Genesis-Esther, Gospels, Acts (43% of Bible)
3. **Poetry**: Psalms, Song of Solomon (33% of Bible)
4. **Wisdom**: Proverbs, Job, Ecclesiastes
5. **Prophecy**: Isaiah-Malachi
6. **Epistles**: Romans-Jude (24% as "discourse")
7. **Apocalyptic**: Daniel, Revelation
8. **(Gospels)**: Sometimes treated as unique genre (biographical-theological narrative)

**Source**: Core Christianity, GotQuestions, American Bible Society, Bible Project

### Proposed Additions

**Descriptive** (MacSaveny): Static, non-temporal, non-agentive (tabernacle descriptions, genealogies, visions). May be 5th major genre type beyond Longacre's 4.

## Cross-Linguistic Findings

### Source Language Encoding: Not Morphological

**Hebrew Genre Indicators** (contextual, not morphological):

| Genre | Primary Markers |
|-------|-----------------|
| Narrative | Wayyiqtol verb chains (ויקטל), temporal sequences |
| Poetry | Parallelism, terseness, metaphor, asyndeton |
| Legal | Apodictic imperatives (לא), casuistic conditionals (כי...ו) |
| Prophecy | Messenger formula (כה אמר יהוה), woe formulas (הוי) |
| Wisdom | Instructional imperatives (שמע בני), comparisons |

**Greek Genre Indicators** (contextual, not morphological):

| Genre | Primary Markers |
|-------|-----------------|
| Narrative | Aorist sequences, historical present, καί connections |
| Epistolary | Opening formula (χάρις καὶ εἰρήνη), closing (ἀσπάζομαι) |
| Expository | Logical connectives (γάρ, διό, ὅτι) |
| Hortatory | Imperatives, subjunctives, οὖν (therefore) |
| Apocalyptic | Vision formulas (εἶδον), symbolic imagery |

**Implication**: Algorithm must analyze **discourse patterns**, not single morphemes.

### Typological Variation in Genre Marking

Languages mark genre through different strategies:

**1. Morphological** (verb forms, aspect, mood):
- **Swahili**: Narrative tense ka- (obligatory for sequential narrative)
- **Spanish**: Preterite/imperfect distinction correlates with narrative vs. background
- **Russian**: Perfective/imperfective aspect distribution varies by genre

**2. Syntactic** (word order, clause chaining):
- **Trans-New Guinea languages** (Enga, Kewa): Switch-reference density high in narrative
- **Arabic**: VSO for narrative foreground, SVO for background/topicalized
- **Japanese**: Sentence-final particles signal genre-relevant speech acts

**3. Lexical** (particles, connectives, formulas):
- **Greek**: γάρ (expository), οὖν (hortatory), δέ (narrative continuity)
- **Hebrew**: Wayyiqtol (narrative), weqatal (non-narrative)
- **English**: Connectives differ by genre ("then" narrative, "therefore" expository)

**4. Register/Style** (honorifics, formality):
- **Japanese**: Keigo system (honorifics) interacts with epistolary genre
- **Javanese**: Speech levels correlate with genre and social context

**Source**: [research/LANGUAGES.md](LANGUAGES.md) - Complete language family analysis

### Language-Specific Challenges

**Missing Genre Traditions**:
- **Epistolary**: Oral cultures lack written letter conventions (PNG languages)
- **Legal codes**: Customary oral law vs. codified written law (minority languages)
- **Apocalyptic**: Symbolic-visionary genre unfamiliar (many cultures)

**Solution**: Adapt to oral conventions OR create written traditions (often happens through Bible translation itself).

**Narrative-Focused Languages**: Trans-New Guinea (~250 languages) have specialized narrative grammar (switch-reference, medial verbs) but emerging conventions for other genres.

**Topic-Prominent Languages**: Austronesian, Sino-Tibetan (~180 languages) - genre affects what is topicalized (participants in narrative, concepts in expository).

**Honorific Languages**: Japanese, Javanese, Korean - genre interacts with social register (epistolary requires appropriate politeness level).

## Theological Analysis

### Theological Significance: ~15% Critical Contexts

**High Stakes** (wrong genre → heresy):
1. **Genesis 1-2**: Narrative vs. poetry debate affects creation theology
2. **Revelation**: Apocalyptic vs. literal narrative confusion leads to bizarre interpretations
3. **Parables**: Parable vs. historical narrative confusion creates false history

**Medium Stakes** (wrong genre → serious misinterpretation):
1. **Psalms**: Poetry vs. prose - over-literalizes metaphors ("God has wings")
2. **Proverbs**: Wisdom vs. legal - prosperity gospel errors (treating general principles as absolute promises)
3. **Job 3-41**: Dialogue vs. authoritative narration - friends' errors as divine truth
4. **Song of Solomon**: Love poetry vs. allegory - affects application
5. **Jonah**: Narrative vs. parable - biblical authority debates
6. **Legal codes**: Legal vs. narrative - affects Christian application
7. **Epistles**: Expository vs. hortatory - affects understanding vs. obedience
8. **Gospels**: Biographical-theological vs. mythology - historicity debates
9. **Prophecy**: Various subtypes affect interpretation

**Arbitrary** (~85% of contexts): Genre subtype distinctions (narrative vs. historical-narrative, hymnic vs. lament poetry) that don't affect theological interpretation.

**Source**: [research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml) - Complete theological classification

### Orthodox Position Examples

**Genesis 1-2**: Conservative Protestant orthodoxy affirms **narrative** (historical, sequential), though acknowledging elevated/liturgical style. Framework hypothesis (poetry) is minority Reformed view. **Forbidden**: Mythology, legend.

**Revelation**: **Apocalyptic-prophecy** (symbolic imagery with theological/prophetic truth). **Forbidden**: Plain narrative (bizarre literalization) OR pure allegory (arbitrary symbols).

**Parables**: **Parable** (fictional teaching narratives). **Forbidden**: Historical reports (creates false history).

## Key Scholarly Sources (25+ sources)

### Foundational Works

1. **Longacre, Robert E. (1996)**. *The Grammar of Discourse*. [4-way functional taxonomy]
2. **Longacre & Hwang (2012)**. *Holistic Discourse Analysis* (2nd ed.). [Field manual]
3. **Patton, Putnam, & Van Pelt (2019)**. *Basics of Hebrew Discourse*. [Hebrew genre markers]
4. **Levinsohn, Stephen H. (1992/2000)**. *Discourse Features of New Testament Greek*. [Greek particles]

### SIL Resources

5. **Wendland & Aubrey (2023)**. *Discourse Analysis and Bible Translation* (SIL coursebook). [Practical translation application]
6. **Dooley & Levinsohn**. *Analyzing Discourse: A Manual of Basic Concepts*. [Training materials]
7. **Hoyle, Michael**. "Scenarios, Discourse, and Translation." [Case frames and genre]

### Biblical Genre Resources

8. **Core Christianity, GotQuestions, American Bible Society**. Biblical genre overviews
9. **Bible Project**. "Poetry, Narrative & Prose Discourse" podcast
10. **Wendland (ed.)**. *Discourse Analysis of Biblical Hebrew Narratives* (Fontes Press)

### Typological Database

11. **WALS** (World Atlas of Language Structures). 2,650 languages, 142 structural features [No specific genre feature, but tense/aspect/word order correlate]

**Full Bibliography**: [research/SCHOLARLY.md](SCHOLARLY.md) - Complete 25+ source review with citations

## Gaps in Knowledge

### What We Know

- **Genre affects all languages**: Universal relevance confirmed
- **Not morphologically encoded**: Requires discourse-level analysis
- **Two major frameworks**: Longacre (functional) vs. traditional biblical (form-based)
- **TBTA has 6+ values**: Narrative, Expository, Poetic, Legal, Prophetic, Epistolary (+ subtypes)
- **Theological significance exists**: ~15% of contexts theologically critical

### What We Don't Know (from documentation)

1. **Complete TBTA taxonomy**: Full list of all genre values and subtypes
2. **Annotation guidelines**: Specific criteria for assigning each value
3. **Edge case handling**: Genre mixing, transitions, ambiguous boundaries
4. **Frequency distribution**: Which values are common vs. rare (Stage 2 task)
5. **Source language correlation**: Do Hebrew/Greek markers directly predict TBTA values?

### Discrepancies to Investigate (Stage 2)

**TBTA vs. Longacre**:
- TBTA: Narrative, Expository, Poetic, Legal, Prophetic, Epistolary (6 types)
- Longacre: Narrative, Procedural, Behavioral/Hortatory, Expository (4 types)
- **Question**: How do they map? Is TBTA "Legal" = Longacre "Procedural"? Is TBTA "Prophetic" = Longacre "Hortatory"?

**Procedural genre**: Longacre has "Procedural" (how-to instructions). Does TBTA? Leviticus sacrificial procedures may be "Procedural" not just "Legal."

**Descriptive genre**: MacSaveny proposes 5th type. Do tabernacle descriptions, genealogies, visions get special handling in TBTA?

## Implications for Algorithm Development

### Stage 2 (Translation Database)

**Recommended Languages** (10 for maximum typological diversity):
1. English (root language, lexical marking)
2. Spanish (root language, aspect marking)
3. Arabic (root language, classical genre traditions, VSO)
4. Malay (root language, topic-prominent, Austronesian)
5. Swahili (narrative tense ka-, Niger-Congo)
6. Russian (aspect varies by genre, flexible word order)
7. Enga (switch-reference narrative focus, Trans-New Guinea, oral traditions)
8. Tok Pisin (emerging genres, creole, simplified systems)
9. Japanese (honorific-genre interaction, SOV, complex register)
10. Mandarin (ancient genre traditions, topic-prominent, particles)

**Note**: Some may need substitution based on availability in dataset.

### Stage 3 (Analysis)

**Analyze**:
- What translation choices correlate with each TBTA genre value?
- Do translators in marking languages (Swahili, Enga, Japanese) make consistent genre-appropriate grammatical choices?
- Can we predict TBTA genre from source text features alone OR need broader context (book-level, chapter-level)?

### Stage 4 (Algorithm)

**Approach**:
- **Multi-level analysis required**: Word-level markers + clause-level patterns + discourse-level context
- **Cannot use single morpheme**: Hebrew wayyiqtol suggests narrative, but need broader context to confirm
- **Contextual features**: Book identity (Psalms = poetry, Acts = narrative), chapter structure, verse sequences
- **Linguistic features**: Vocabulary clusters (legal terminology, prophetic formulas), syntactic patterns, connectives

**Likely Strategy**: Combine multiple signals - no single feature determinative.

### Stage 5 (Validation)

**Test with**:
- Languages requiring mandatory genre marking (Swahili ka-tense, Enga switch-reference)
- Translation practitioner review: Does predicted genre align with translators' natural choices?
- Theologically critical passages (Genesis 1, Revelation, parables): Does algorithm correctly identify high-stakes genres?

## Files in This Research Directory

1. **[TBTA.md](TBTA.md)** - Complete TBTA documentation review (values, policy, constraints, examples)
2. **[LANGUAGES.md](LANGUAGES.md)** - Language family & typology analysis (source encoding, 10 control languages, genre marking strategies)
3. **[SCHOLARLY.md](SCHOLARLY.md)** - 25+ scholarly sources with detailed findings and bibliography
4. **[THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)** - Theological classification (high/medium stakes contexts, orthodox positions, translator guidance)
5. **[README.md](README.md)** - This summary (max 200 lines per progressive disclosure)

## Next Steps

**Stage 2**: Generate Test Set with Translation Data
- Create translation database for 10 selected languages
- Sample 100+ verses per genre value
- Discover what translators actually chose (answer sheets from TBTA, question sheets from translations)

**Stage 3**: Analyze Translations & Develop Algorithm
- Identify which translation choices correlate with genre
- Determine if genre is predictable from source text features
- Document patterns and edge cases

**Stage 4-6**: Algorithm development, testing, peer review per STAGES.md methodology.

---

**Research Completed**: 2025-11-29
**Total Sources**: 25+ scholarly and web resources
**Total Languages Analyzed**: ~1,008 (10 control languages in detail)
**Theological Contexts Classified**: 12 high/medium stakes, 9 arbitrary categories

**See individual research files for full details.**
