<<<<<<< HEAD
# Mood Feature Research Summary

**Feature**: Mood (Grammatical Modality)
**TBTA Tier**: A (Essential - affects 1000+ languages)
**Research Completed**: 2025-11-26
**Status**: Stage 1 Complete

---

## Quick Overview

**Mood** expresses the speaker's stance toward the reality, necessity, or desirability of an action or state. TBTA encodes **11 distinct mood values** spanning factual (Indicative), obligation (deontic modality), and possibility (epistemic modality).

**Translation Impact**: ⭐⭐⭐⭐⭐ VERY HIGH (5/5)
- Affects 1000+ languages worldwide
- Cannot be easily inferred from context
- Misidentifying mood can alter divine commands to suggestions, or facts to possibilities

**Key Finding**: **94.62% of verbs are Indicative** (factual), but the **5.38% modal verbs carry critical semantic and theological weight**.

---

## 1. TBTA Documentation Summary

**Source**: `research/TBTA.md` (comprehensive review of TBTA archived documentation)

### 1.1 Core Findings

**Value Inventory**: 11 distinct mood types
- **Factual**: Indicative (94.62%)
- **Obligation** (Deontic): 'must', 'should', Forbidden, 'should not', 'may' permissive (2.85%)
- **Potential** (Epistemic): Definite, Probable, 'might', Unlikely, Impossible, 'might not' (2.53%)
- **Traditional moods**: Subjunctive, Optative, Imperative (mapped to semantic values)

**TBTA Policy**:
- **Semantic priority over morphology**: Greek subjunctive maps to multiple TBTA values depending on context
- **Multi-level analysis**: Morphology + lexical auxiliaries + syntax + discourse + context
- **Default to Indicative**: 94.62% frequency = safe baseline
- **Gateway features**: δεῖ (dei), χρή (chre), ἔξεστι (exesti), δύναμαι (dunamai) trigger high-confidence modal annotations

**Source Language Encoding**:
- ✅ **Greek**: Explicitly morphological (4 moods: indicative, subjunctive, optative, imperative) + modal auxiliaries
- ⚠️ **Hebrew**: Partially morphological (imperative, jussive, cohortative) + context-dependent (YIQTOL = 80%+ modal)

**Test Data**: Matthew 24 (316 verbs, 51 verses)

**See**: `research/TBTA.md` for full details on:
- Complete value enumeration
- Gateway features and constraints
- Edge case handling (embedded moods, rhetorical questions, indirect commands)
- Common annotation errors and solutions

---

## 2. Scholarly Research Summary

**Source**: `research/SCHOLARLY.md` (31 scholarly sources)

### 2.1 Foundational Frameworks

**Three Primary Dimensions** (Palmer 2001; Nuyts 2005):
1. **Epistemic modality**: Degree of certainty (fact, possibility, probability)
2. **Deontic modality**: Obligation, permission, prohibition
3. **Dynamic modality**: Capability, volition

**Realis vs. Irrealis** (Mithun 1995):
- **Realis**: Actualized events, knowable through direct perception (→ Indicative)
- **Irrealis**: Events within realm of thought, knowable through imagination (→ all other moods)

**Semantic Map** (Van der Auwera & Plungian 1998):
- Four modality domains: participant-internal, participant-external, deontic, epistemic
- ~50% of languages show form overlap for possibility or necessity
- Justifies TBTA's semantic priority over morphological form

### 2.2 Typological Databases

**WALS Online**:
- **Feature 72**: Imperative-Hortative Systems (cross-linguistic universals)
  - Imperative 2nd singular most pervasive
  - Hortative 1st singular least grammaticalized
- **Feature 73**: The Optative (rare, often overlaps with 3rd person imperative)

**Grambank**:
- 2,467 languages, 195 features
- **GB312**: Morphological mood marking
- **GB519**: Mood via auxiliary particles
- **GB119**: Mood via auxiliary verbs
- Confirms mood is globally distributed but encoding varies enormously

### 2.3 Cross-Linguistic Case Studies

**Turkish** (Şener 2011):
- Evidential system (direct -DI vs. indirect -mIş) interacts with mood
- Indirect evidential often has inferential meaning (epistemic potential)

**Japanese** (Masuoka 2002):
- No dedicated subjunctive or irrealis morphology
- Uses conditional constructions (ba/nara/tara/to) + tense
- Desiderative -tai (speaker's desire)

**Romance Languages** (Spanish, French, Italian):
- Spanish: Subjunctive used more than any other Romance language
- French: Reduced subjunctive (present + perfect only)
- Italian: Similar to Spanish

**Arabic**:
- 3 basic moods (indicative, subjunctive, jussive); Classical Arabic has 6
- Syntactically controlled
- Modal verbs supplement morphology

**Bantu Languages** (Nurse & Devos 2019):
- Highly developed TAM systems
- Productive subjunctive -e suffix
- Aspect more fundamental than tense

**Conditional Syntax** (Greek/Latin grammars):
- Protasis mood determines conditional type
- εἰ + indicative = factual; ἐάν + subjunctive = hypothetical

**Imperatives and Politeness** (Aikhenvald 2010):
- Politeness in imperatives is grammaticalized (not just pragmatic)
- Cross-linguistic variation in what counts as polite
- Face-threatening act theory (Brown & Levinson)

**See**: `research/SCHOLARLY.md` for:
- 31 scholarly sources with full citations
- Translation case studies (Fijian, Turkish, Spanish)
- Verses where mood is critical (Gen 1:26, Mat 5:48, Rom 6:1)

---

## 3. Language Family Analysis Summary

**Source**: `research/LANGUAGES.md` (1,008 languages analyzed)

### 3.1 Major Families in Corpus

| Family | Languages | Mood Encoding | Classification |
|--------|-----------|---------------|----------------|
| **Indo-European: Romance** | Spanish (31k verses), French, Italian, Portuguese | Morphological subjunctive | **Mandatory** |
| **Indo-European: Germanic** | English, German, Dutch, Norwegian | Modal auxiliaries | **Optional** morphology |
| **Afro-Asiatic: Arabic** | MSA, Egyptian, Gulf | 3-6 morphological moods | **Mandatory** |
| **Afro-Asiatic: Hebrew** | Biblical, Modern | Imperative + context | **Mixed** |
| **Austronesian: Philippine** | Tagalog, Cebuano, Ilokano | TAM + Afactual | **Mandatory** (afactual) |
| **Austronesian: Oceanic** | Fijian, Samoan, Tongan | Realis/Irrealis (12+ moods) | **Mandatory** |
| **Austronesian: Indonesian/Malay** | Indonesian (31k verses), Malay | Modal particles | **Optional** |
| **Niger-Congo: Bantu** | Swahili, Kinyarwanda, Zulu | Subjunctive -e suffix | **Mandatory** |
| **Sino-Tibetan: Chinese** | Mandarin, Cantonese | Modal verbs + particles | **Optional** |
| **Turkic** | Turkish, Kazakh | Evidential + mood | **Mandatory** |
| **Japonic** | Japanese | Conditional + tense | **Optional** |

### 3.2 Encoding Distribution (Estimated)

- **Mandatory morphological mood**: ~30% (Romance, Arabic, Bantu, Turkic, Austronesian)
- **Optional morphology, mandatory auxiliaries/particles**: ~30% (Germanic, Chinese, Indonesian)
- **Context-dependent or minimal marking**: ~40% (Trans-New Guinea, isolating languages)

### 3.3 Root Languages (All 10 have mood features)

1. Hebrew (source), 2. Greek (source), 3. Latin, 4. English, 5. Spanish, 6. French, 7. German, 8. Arabic, 9. Indonesian, 10. Swahili

### 3.4 Recommended Translation Database (10 languages)

**Criteria**: Mix of morphological vs. non-marking, diverse families, root languages

1. **Spanish** (Romance, mandatory subjunctive)
2. **English** (Germanic, modal auxiliaries)
3. **French** (Romance, reduced subjunctive)
4. **Greek** (source language, 4 moods)
5. **Arabic** (Afro-Asiatic, 3-6 moods)
6. **Swahili** (Bantu, subjunctive -e)
7. **Indonesian** (Austronesian, particles)
8. **Tagalog** (Philippine, TAM + afactual)
9. **Turkish** (Turkic, evidential + mood)
10. **Japanese** (Japonic, conditional-based)

**See**: `research/LANGUAGES.md` for:
- Detailed family-by-family analysis
- Cultural nuances (honorifics, evidentiality, voice-mood interaction)
- Language-specific grammatical details

---

## 4. Theological Significance Summary

**Source**: `research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml`

### 4.1 Non-Arbitrary Contexts (15% of verbs, VERY HIGH stakes)

**10 theologically critical groups** identified:

1. **Ten Commandments** (Exo 20; Deu 5) - Forbidden Obligation vs. 'should not'
   - Stakes: **HIGH** - Divine authority, moral law
   - Orthodox: Forbidden Obligation (absolute prohibition)
   - Heresy: Weakening to 'should not' (advisory)

2. **Great Commission** (Mat 28:19-20) - Imperative vs. 'should'
   - Stakes: **HIGH** - Missiology, Church's mandate
   - Orthodox: Imperative/'must' Obligation
   - Heresy: 'should' (makes evangelism optional)

3. **Conditional Salvation** (John 3:16) - Indicative vs. 'might' Potential
   - Stakes: **VERY HIGH** - Assurance of salvation
   - Orthodox: Indicative (certain promise)
   - Heresy: 'might not perish' (uncertain salvation)

4. **Passion Predictions** (Mat 16:21) - 'must' Obligation vs. Indicative
   - Stakes: **VERY HIGH** - Atonement theology, divine necessity
   - Orthodox: 'must' Obligation (Cross necessary for atonement)
   - Heresy: Mere prediction (Cross contingent)

5. **Second Coming** (Acts 1:11; Rev 22:20) - Indicative vs. 'might'
   - Stakes: **HIGH** - Eschatological certainty
   - Orthodox: Indicative ("will come")
   - Heresy: 'might' (undermines certainty)

6. **Lord's Prayer** (Mat 6:9-13) - Imperative/Jussive vs. Optative
   - Stakes: **MEDIUM** - Prayer theology
   - Orthodox: Jussive ("Let Your kingdom come") or Optative ("May...")
   - Acceptable: Both (overlap in function)

7. **Sexual Immorality Prohibitions** (1 Cor 6:18) - Imperative vs. 'should'
   - Stakes: **HIGH** - Christian ethics, sanctification
   - Orthodox: Imperative ("Flee...")
   - Heresy: 'should' (weakens to advice)

8. **Covenant Blessings/Curses** (Deu 28-30) - Indicative vs. Subjunctive
   - Stakes: **MEDIUM** - Covenant theology, conditional certainty
   - Orthodox: Indicative (certain given condition)
   - Heresy: 'might' (uncertain even with obedience)

9. **Jesus's "I AM" Statements** (John 8:58) - Indicative vs. Potential
   - Stakes: **VERY HIGH** - Christology, Trinity
   - Orthodox: Indicative ("I AM")
   - Heresy: ANY weakening to possibility ('might be')

10. **Perseverance Exhortations** (Heb 10:23) - Imperative vs. 'should'
    - Stakes: **MEDIUM** - Apostolic authority, perseverance
    - Orthodox: Imperative ("Hold fast")
    - Heresy: 'should' (weakens urgency)

### 4.2 Arbitrary Contexts (85% of verbs, low stakes)

- Historical narrative (Indicative default)
- Travel itineraries
- Crowd sizes
- Routine daily actions
- Interrogative Indicative (non-rhetorical questions)
- Purpose clauses (non-theological)
- Non-doctrinal hypotheticals
- Human speculation

**Key Takeaway**: Mood is **arbitrary in 85%+ of text** (narrative Indicative), but the **15% non-arbitrary contexts carry VERY HIGH theological stakes**. Accurate annotation is **essential** in high-stakes contexts to preserve Christian orthodoxy.

**See**: `research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml` for:
- Detailed analysis of each non-arbitrary group
- Christian orthodox positions vs. heretical alternatives
- Translator guidance for each context

---

## 5. Key Disagreements & Discrepancies

### 5.1 TBTA vs. Traditional Grammar

**Disagreement**: Greek subjunctive morphology does not map to single TBTA mood value
- **TBTA**: Prioritizes semantic function over morphological form
  - Conditional subjunctive → 'might' Potential (c)
  - Prohibition subjunctive → Forbidden Obligation (i)
  - Hortatory subjunctive → 'should' Obligation (g)
- **Traditional grammar**: Subjunctive is a single category
- **Resolution**: TBTA approach is intentional for cross-linguistic transfer

### 5.2 Source Language Analysis

**Disagreement**: Hebrew YIQTOL = future tense OR modal?
- **Traditional**: YIQTOL is future tense (imperfect)
- **Modern research** (Cook 2005): 80%+ modal function (contemplated action, non-reality)
- **TBTA**: Treats YIQTOL as context-dependent (future Indicative OR modal)

### 5.3 Scholarly Debate: Irrealis as Typological Category

**Disagreement**: Is "irrealis" a valid cross-linguistic category?
- **Pro** (Mithun 1995, Palmer 2001, Elliott 2000): Complete accord in realis/irrealis distinction
- **Con** (Bybee et al. 1994, de Haan 2012): Reject as typologically valid; too diverse to unify
- **TBTA**: Uses realis (Indicative) vs. irrealis framework but breaks irrealis into 10 distinct values

---

## 6. Remaining Open Questions

1. **Modal Strength Gradation**: How to consistently assign 6 epistemic levels (definite → impossible) and 4 deontic levels (must → may)?
   - Current: Lexical strength ratings + contextual modulation + genre conventions
   - Challenge: Inter-annotator agreement on fine-grained distinctions

2. **Subjunctive vs. Indicative in Conditionals**: First-class (εἰ + indicative) vs. third-class (ἐάν + subjunctive)?
   - Hypothesis: First-class = factual assumption (Indicative); third-class = hypothetical (Subjunctive/Potential)
   - Future work: Annotate full conditional corpus; validate with target language conditionals

3. **Evidentiality Interaction**: How should TBTA handle languages where evidentiality overlaps with mood (Turkish -mIş, Bulgarian, Persian)?
   - Current: Treat as epistemic potential if inferential
   - Open question: Should evidentiality be separate feature or integrated with mood?

---

## 7. Next Steps (Stage 2: Analysis & Validation)

**Recommended Actions**:

1. **Expand test corpus**: Beyond Matthew 24 (316 verbs) to full Gospels, Epistles, OT genres (Legal, Wisdom, Prophetic)

2. **Build Translation Database**: Implement 10-language translation database (Spanish, English, French, Greek, Arabic, Swahili, Indonesian, Tagalog, Turkish, Japanese)
   - Sample size: 100+ verses per mood value minimum
   - Generate dual outputs: answer sheets (TBTA) + question sheets (translations)

3. **Develop confidence models**: Quantify confidence per mood type
   - High (90%+): Indicative, Forbidden, strong modals (δεῖ, imperative morphology)
   - Medium (75-90%): Obligation strength, potential strength
   - Low (<75%): Rare values, context-dependent

4. **Validate with real translators**: 2-3 languages per modal system type
   - Test if TBTA annotations improve modal auxiliary/morphology selection

5. **Create transfer matrices**: Target language mapping guides
   - How each TBTA mood value transfers to 10 database languages

---

## 8. Research Files

| File | Lines | Purpose |
|------|-------|---------|
| `TBTA.md` | ~700 | Comprehensive review of TBTA documentation (values, policy, edge cases, statistics) |
| `SCHOLARLY.md` | ~800 | 31 scholarly sources (Palmer, Bybee, WALS, Grambank, Greek/Hebrew grammars, cross-linguistic studies) |
| `LANGUAGES.md` | ~500 | 1,008 languages analyzed; family-by-family encoding; 10 recommended database languages |
| `THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml` | ~600 | 10 non-arbitrary groups (theologically critical); 8 arbitrary groups; translator guidance |
| `README.md` (this file) | ~200 | Executive summary of all research |

**Total Research**: ~2,800 lines across 5 files

---

## 9. Summary Quick Facts

| Metric | Value |
|--------|-------|
| **TBTA Mood Values** | 11 distinct types |
| **Indicative Frequency** | 94.62% (Matthew 24 test data) |
| **Modal Verbs Frequency** | 5.38% (but HIGH theological impact) |
| **Source Languages** | Greek (explicit), Hebrew (partial) |
| **Scholarly Sources** | 31+ (Palmer, Bybee, WALS, Grambank, etc.) |
| **Languages Analyzed** | 1,008 from corpus |
| **Mandatory Mood Encoding** | ~30% of world's languages |
| **Optional Mood Encoding** | ~40% (via auxiliaries/particles) |
| **Theologically Critical Contexts** | 15% of verbs (10 groups identified) |
| **Arbitrary Contexts** | 85% of verbs |
| **Translation Impact** | ⭐⭐⭐⭐⭐ VERY HIGH (5/5) |

---

**Research Status**: ✅ Stage 1 Complete
**Date**: 2025-11-26
**Next Stage**: Stage 2 (Translation Database & Analysis)
=======
# Mood: Research Summary

**Feature**: Grammatical Mood (Modality)
**Stage**: 1 - Research & Definition
**Status**: Complete
**Date**: 2025-11-25

## Executive Summary

Grammatical mood (modality) encodes speaker stance toward an action: factual assertion (indicative), command (imperative), possibility (potential/subjunctive), necessity (obligation), wish (optative). TBTA supports **11 mood values** beyond traditional grammatical categories, capturing semantic modality crucial for translation. Mood is **explicitly encoded** in Greek (4 morphological moods) and **partially encoded** in Hebrew (imperative/cohortative/jussive).

**Key Finding**: Mood is **theologically critical** in ~10-15% of contexts (divine commands, conditional sentences, Trinity cohortatives) and **stylistically arbitrary** in ~85-90% (narrative indicatives). Getting mood wrong can transform divine commands into predictions or weaken salvation assurances.

## What is Mood?

**Definition**: The grammatical category expressing speaker's attitude toward the reality, certainty, or necessity of an action.

**TBTA Values** (11 total):
| Value | Code | Frequency | Description |
|-------|------|-----------|-------------|
| Indicative | I | 94.62% | Factual statements |
| 'might' Potential | a | 2.53% | Uncertain possibility |
| 'must' Obligation | f | 1.58% | Strong necessity |
| Forbidden Obligation | i | 0.63% | Strong prohibition |
| 'should' Obligation | g | 0.32% | Moderate advice |
| 'should not' Obligation | h | 0.32% | Negative advice |
| 'may' Permissive | - | <0.1% | Permission granted |
| Probable Potential | b | <0.1% | Likely outcome |
| Definite Potential | c | <0.1% | Certain capability |
| Subjunctive | S | Rare | Hypothetical/conditional |
| Optative | O | Rare | Wishes/prayers |

**Source Language Encoding**:
- **Greek**: 4 morphological moods (indicative, subjunctive, optative, imperative) - fully explicit
- **Hebrew**: Partial - imperative, cohortative, jussive marked; other modality via syntax/lexicon

**TBTA Status**: Tier A (Essential), #10 in feature catalog, "Complete" status, affects 1000+ languages

## Key Research Findings

### 1. TBTA Documentation ([TBTA.md](TBTA.md))

**Policy**: Semantic modality over grammatical morphology
- Greek subjunctive may be coded as Indicative if semantically factual
- Greek imperative may be coded as 'must' Obligation for semantic precision
- Position 3 in 9-character verb encoding scheme

**Critical Issue Found** ({tbta-source/CRITIQUE.md}):
> "Morphological imperative mood coded as semantic 'Indicative' mood"
- ALL Greek imperatives marked as Indicative instead of Imperative
- Affects thousands of NT command instances
- Target languages need source morphology for imperative morphology choice

**Test Data**: Matthew 24 (316 verbs, 51 verses), 96.3% reproduction accuracy

### 2. Language Family Analysis ([LANGUAGES.md](LANGUAGES.md))

**Source Language Encoding Check**:
- **Greek**: ✅ EXPLICIT - 4 moods morphologically distinct
- **Hebrew**: ⚠️ PARTIAL - volitional moods marked; other modality lexical/syntactic

**Typological Classification**:
| Language Type | Mood Marking | Examples |
|---------------|--------------|----------|
| Grammatical mood (inflectional) | Obligatory | Greek, Romance, Slavic, Arabic |
| Lexical mood (modal verbs) | Analytical | English, German, Indonesian |
| Evidential mood | Obligatory | Turkish, Azerbaijani |
| Modal auxiliaries | Semi-grammaticalized | Japanese, Korean |

**Top Language Families for Mood**:
1. **Indo-European**: Romance (mandatory subjunctive), Greek (4 moods)
2. **Turkic**: Obligatory evidential (-mIş for non-witnessed)
3. **Japonic**: Modal auxiliaries + honorific interactions
4. **Bantu**: TAM template with subjunctive final vowel
5. **Austronesian**: Variable, mostly minimal grammatical marking

**Proposed Test Languages** (Stage 2):
1. Spanish (spa) - Productive subjunctive
2. Turkish (tur) - Obligatory evidential
3. English (eng) - Modal verb system
4. Arabic (arb) - 4-mood Semitic system
5. Swahili (swh) - Bantu TAM template
6. Russian (rus) - Reduced Slavic system
7. Japanese (jpn) - Modal auxiliaries + honorifics
8. German (deu) - Modal verbs + Konjunktiv
9. French (fra) - Reduced Romance subjunctive
10. Indonesian (ind) - Minimal marking (control)

### 3. Scholarly Research ([SCHOLARLY.md](SCHOLARLY.md))

**Key Sources** (33 total):
- **Palmer (2001)**: Typology of mood/modality - propositional vs. event modality
- **Bybee et al. (1994)**: Grammaticalization pathways across 76 languages
- **Wallace (1996)**: Greek grammar - mood statistics, exegetical syntax
- **Waltke-O'Connor (1990)**: Hebrew modal system - imperative/cohortative/jussive
- **Porter (1989)**: Verbal aspect - mood relationship in Greek
- **WALS Features 75-76**: Epistemic possibility, modal overlap patterns

**Typological Databases**:
- WALS Chapter 70: Imperative systems (548 languages analyzed)
- WALS Chapter 76: Modal marker overlap (situational vs. epistemic)
- Grambank: Mood grammaticalization parameters

**Translation Principles**:
1. **Preserve imperatival force** for divine commands
2. **Distinguish conditional types** (1st/2nd/3rd class Greek conditions)
3. **Handle optative carefully** (wishes vs. prayers vs. remote possibility)
4. **Consider honorific interactions** (Japanese/Korean indirect commands)
5. **Map evidentiality where required** (Turkish -mIş for indirect knowledge)

**Case Studies**:
- **John 3:16** (Greek subjunctive): Purpose clause ἵνα μὴ ἀπόληται - "so that he should not perish"
- **Romans 15:13** (Greek optative): Benediction πληρώσαι - "may [God] fill you"
- **Genesis 1:26** (Hebrew cohortative): "Let us make" - volitional mood + Trinity

### 4. Theological Significance ([THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml))

**Classification**: 10-15% Non-Arbitrary, 85-90% Arbitrary

#### Non-Arbitrary Contexts (10-15%)

**HIGH Stakes (7-10%)**:
1. **Divine Commands** (Ten Commandments, Sermon on Mount)
   - Imperative → Indicative = command becomes prediction (weakens divine authority)
   - FIRST CHOICE: Strongest imperative; FORBIDDEN: Future indicative

2. **Greek Conditional Sentences**
   - 1st class (εἰ + indicative): Assumed true - salvation assurance passages
   - 2nd class (contrary-to-fact): Asserts opposite - Christological uniqueness
   - 3rd class (subjunctive): Uncertain - hypothetical futures

3. **Prophetic Certainty**
   - Hebrew prophetic perfect: Future events as certain as past
   - "Shall/will" (certain) vs. "might" (uncertain) affects prophetic authority

4. **Great Commission** (Matt 28:19-20)
   - Participles + imperative: Go-make disciples-baptize-teach
   - Must retain imperatival force - not suggestions

**MEDIUM Stakes (3-5%)**:
5. **Pauline Optatives** (Romans 15:5, 15:13, Galatians 6:16)
   - μὴ γένοιτο "may it not be" - rhetorical denial
   - Benedictions: Prayer-wish, not command to God

6. **Genesis 1:26 Cohortative**
   - "Let us make" - mood + number interact (Trial preferred)
   - Cohortative mood signals deliberative will

7. **Prayer Language** (Lord's Prayer, Gethsemane)
   - Greek imperatives toward God (petitionary mood)
   - Gethsemane: Jesus' human will + divine submission

#### Arbitrary Contexts (85-90%)

- **Narrative indicatives**: General storytelling (94% of verbs)
- **Questions about facts**: Interrogative indicative vs. subjunctive
- **Reported speech**: Embedded mood follows source
- **Generic conditionals**: "If anyone..." without specific referent
- **Travel/action descriptions**: "He went", "They said"

## Discrepancies Between Research Sections

| Issue | TBTA | Scholarly | Resolution |
|-------|------|-----------|------------|
| Greek imperative coding | Marked as "Indicative" | Should be "Imperative" | TBTA bug - needs fix |
| Evidentiality | Not in TBTA values | Critical for Turkic | Add for Turkish-family targets |
| Japanese modal | Not addressed | Complex modal system | Include in language analysis |
| Optative frequency | Listed as "rare" | <70 NT occurrences | Accurate - declining in Koine |

## Key Insights for Algorithm Development

1. **94.62% indicative base rate** - Majority of verbs are factual statements
2. **5.38% modal verbs** carry crucial semantic distinctions (obligation, permission, possibility)
3. **Greek conditional type** determines protasis mood (affects translation mood choice)
4. **Divine commands** must retain imperatival force - never reduce to prediction
5. **Evidentiality** may need separate treatment for Turkic target languages
6. **Honorific-mood interaction** critical for Japanese/Korean/Javanese

## Gaps Requiring Stage 2 Verification

1. **Greek imperative bug**: How many commands marked as Indicative?
2. **Optative distribution**: Verify <70 occurrences across NT
3. **Hebrew cohortative mapping**: How does TBTA encode 1st person volitional?
4. **Conditional sentence types**: Are 1st/2nd/3rd class distinguished?
5. **Turkish evidential mapping**: Do we have Turkish translations to test?

## Next Steps (Stage 2)

**Data Extraction**:
- Extract all mood annotations from TBTA database
- Frequency analysis: I/S/O/Obligation/Potential distribution
- Verify Matthew 24 baseline (316 verbs, 51 verses)

**Hypothesis Testing**:
1. Are Greek imperatives coded as Indicative? (systematic bug check)
2. How are Greek conditionals distinguished? (1st/2nd/3rd class)
3. Do subjunctive purpose clauses get appropriate mood coding?
4. How are Hebrew cohortatives mapped to TBTA mood values?

## Bibliography

See [SCHOLARLY.md](SCHOLARLY.md) for complete 33-source bibliography with citation codes.

Key references:
- {palmer-2001-mood} - Typological framework
- {wallace-1996-greek-grammar} - NT exegesis
- {waltke-oconnor-1990-hebrew} - OT modal system
- {bybee-1994-evolution} - Grammaticalization pathways
- {porter-1989-verbal-aspect} - Greek aspect-mood interaction

---

**Lines**: 198 (under 200-line progressive disclosure limit)
**Status**: Stage 1 Research Complete ✅
**Ready for**: Stage 2 Analysis
>>>>>>> origin/feat/self-learning-tbta
