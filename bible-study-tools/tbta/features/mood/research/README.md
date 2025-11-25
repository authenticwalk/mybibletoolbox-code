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
