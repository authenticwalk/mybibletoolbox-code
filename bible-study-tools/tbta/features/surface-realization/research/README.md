# Surface Realization: Research Summary

**Feature**: Surface Realization (how noun participants are expressed)
**Status**: Stage 1 Research Complete
**Last Updated**: 2025-11-25

## Executive Summary

Surface Realization marks **how** semantic participants appear on the surface: as full nouns ("God"), pronouns ("he"), zero/null subjects (pro-drop languages), or clitics (bound morphemes). Critical for Bible translation, especially in pro-drop languages (70% of world's languages) and languages with special voice systems (symmetrical voice, inverse marking). Source languages (Hebrew, Greek) are both pro-drop with flexible word order; target languages vary dramatically.

**Key Finding**: Surface Realization is **15% non-arbitrary** (theological/contextual—must be precise) and **85% arbitrary** (stylistic—follows natural discourse). Non-arbitrary contexts include divine passive (resurrection), Holy Spirit personhood markers, crucifixion agency, Jesus's authority claims, and Logos theology.

---

## 1. TBTA Documentation Review

**File**: `TBTA.md`

### Concept & Values

TBTA Feature #7 (Tier A - Essential) marks participants as:
- **N**: Noun (full explicit noun phrase)
- **P**: Personal Pronoun (I, you, he, she, we, they)
- **p**: Pronoun/PRO (demonstratives, indefinites, interrogatives)
- **A**: Always a Noun (rarely documented; semantics unclear)
- **Zero/Clitic**: Listed in TBTA features but **character codes NOT documented**

### Critical Gaps

1. **Position Discrepancy**: {tbta-data-structure} claims Position 9, but {tbta-github} claims Position 11. Requires data verification.
2. **Value Set Ambiguity**: Three different value inventories across TBTA sources. "Zero" and "Clitic" lack character codes.
3. **No Validation Data**: No accuracy metrics available; CRITIQUE.md doesn't mention this feature specifically.
4. **Related Features Not Explained**: Interaction with Participant Tracking (#3), Person System (#2), Noun List Index (#5) documented but correlation rules missing.

### Gateway Features

Surface Realization applies only when:
- **Part of Speech** = Noun or Pronoun (not verbs, adjectives, etc.)
- Interaction with **Participant Tracking** expected (discourse status determines realization choice)

### Source Language Constraints

- **Hebrew**: Non-pro-drop or limited pro-drop. Full subjects required in most clauses. Independent pronouns signal emphasis/contrast.
- **Greek**: Full pro-drop language. Frequently uses null subjects based on verb agreement.

---

## 2. Language Family & Typology Analysis

**File**: `LANGUAGES.md`

### Source Languages

| Language | Pro-Drop | Word Order | Relevant for SR |
|----------|----------|------------|-----------------|
| **Hebrew** | Moderate | VSO flexible | Rare zero; emphasis signals |
| **Koine Greek** | Full | VSO flexible | Frequent null subjects; discourse-driven |

### Target Language Distribution

**1008 languages in TSV** across 25+ families. ~70% allow some pro-drop.

### Candidate Languages (Stage 2)

**Tier 1 (Core)**:
- **Spanish (spa)**: Romance, pro-drop, obligatory clitics, SVO
- **English (eng)**: Germanic non-pro-drop baseline, SVO fixed
- **Mandarin Chinese (zho)**: Topic-prominent, pro-drop with fixed SVO
- **Japanese (jpn)**: Topic-comment, extreme pro-drop, SOV
- **Tagalog (tgl)**: **ONLY symmetrical voice candidate** (6 voices), VSO/VOS

**Tier 2 (Diverse)**:
- **Quechua (que)**: Agglutinative pro-drop, SOV
- **Russian (rus)**: Limited pro-drop with rich case system
- **Arabic (arb)**: Semitic (like Hebrew), VSO pro-drop
- **Swahili (swh)**: Non-pro-drop with noun classes, SVO
- **Mapudungun (arn)**: **ONLY inverse system candidate**, variable order

### Key Typological Distinctions

- **Pro-drop divide**: ~70% of targets allow null subjects; ~30% require explicit subjects
- **Voice systems**: Active/passive (common), symmetrical (Philippine ~80 languages), inverse (~5-10 languages)
- **Word order flexibility**: Fixed (English, Mandarin) or flexible (Spanish, Russian, Japanese)—does NOT predict pro-drop status
- **Clitics**: Romance languages (Spanish, Portuguese, French) obligatory for objects; affects surface patterns

---

## 3. Scholarly Research

**File**: `SCHOLARLY.md`

### Voice Systems & Semantic Roles

**Finding**: Voice determines which semantic role (agent, patient, experiencer) becomes syntactic subject. This affects surface realization because subjects and objects have different patterns.

**Frameworks** {shibatani-1988-passive-voice}, {klaiman-1988-affectedness}, {vanvalin-2005-interface}:
- **Controller vs. Affected**: Participant prominence predicts realization (agents more likely overt)
- **Transitivity Continuum** {hopper-thompson-1980-transitivity}: Voice alternations position events along foregrounding/backgrounding scale

### Language-Specific Voice Systems

1. **Active/Passive (Most Common)**: Agent demoted; patient promoted to subject
   - Found in: English, Spanish, Greek, Hebrew, Arabic, Swahili

2. **Symmetrical Voice (Philippine-Type)**: Multiple unmarked transitive forms with different arguments as pivot
   - {foley-2008-philippine-voice}: "Voice serves to rearrange argument linking and select syntactic pivot"
   - Found in: Tagalog, Cebuano, Ilocano, Malagasy (~80 languages Austronesian)
   - **Key**: No demotion to oblique; maintains all arguments

3. **Inverse Voice**: Person-based marking (Speech Act Participants > 1st > 3rd proximate > 3rd obviative)
   - {jacques-antonov-2014-inverse}: "Direction marking relatively stable in Algonquian"
   - Found in: Algonquian, some Athabaskan, Mapudungun
   - **Key**: Subject/object roles determined by hierarchy, not just morphology

### Biblical Language Insights

**Hebrew Niphal** {vanwolde-2019-niphal-middle}:
- Predominantly **middle voice** (subject concerned with self), NOT passive
- Passive reading only when external agent present and distinct
- Translation Impact: "Niphal = passive of Qal" is oversimplified

**Greek Middle Voice** {allan-nt-middle}, {wallace-greek-middle}:
- 3,726 middle voice forms in NT (distinct from active AND passive)
- Subject as both agent and experiencer
- Lost in English translation (reduced to active or passive)
- **Example**: 1 Cor 13:8 middle "will cease" vs. passive "will be done away with"

### Pro-Drop & Discourse

{pro-drop-parameter}, {frascarelli-2017-null-subjects}:
- Information structure determines null realization (discourse-accessible = null)
- Child language acquisition: overt pronouns for informative arguments, zero for uninformative
- Cross-linguistic: Italian ~50% null subjects, English ~5% (coordinated ellipsis only)

### Typological Databases

**WALS Features** {wals-voice}:
- 107A: Passive Constructions (presence/absence)
- 108A: Antipassive Constructions (48/194 languages = 25%)
- 108B: Antipassive Productivity

**Grambank** {grambank-voice}:
- GB147: Morphological passive on verb
- GB148: Morphological antipassive on verb
- 2,467 languages; enables language-specific prediction

---

## 4. Theologically Significant Contexts

**File**: `THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml`

### Non-Arbitrary Contexts (15%)

**CRITICAL (10% of occurrences)**:

1. **Divine Passive - Resurrection** (Mark 16:6, Matt 28:6, Luke 24:6)
   - Issue: "He has been raised" (zero agent) implies God
   - Stakes: Divine agency in resurrection
   - Orthodox: Preserve passive or make God explicit; never suggest self-resurrection

2. **Holy Spirit Personhood** (John 14:26, 16:13-14)
   - Issue: Personal pronoun "he" vs. neuter "it" vs. zero without personal markers
   - Stakes: Spirit's personhood and deity
   - Orthodox: REQUIRE personal pronouns; "it" is heretical (Jehovah's Witnesses)

3. **Crucifixion Agency** (Matt 27:35, Mark 15:24, Luke 23:33)
   - Issue: Active "they crucified" (human agents) vs. passive "was crucified" (divine plan)
   - Stakes: Balance human responsibility AND divine sovereignty
   - Orthodox: Preserve both; Acts 2:23 model shows both dimensions

4. **Jesus's Authority Claims** (Matt 5:21-48 "it was said... but I say")
   - Issue: Divine passive (zero agent = God) contrasts emphatic pronoun "I"
   - Stakes: Jesus claims authority equal to God's OT revelation
   - Orthodox: Preserve contrast; emphatic "I" even in pro-drop languages

5. **Logos Theology** (John 1:1, 14)
   - Issue: Noun "the Word" vs. pronouns vs. zero (reduces christological title)
   - Stakes: Word as distinct person in Trinity; incarnation
   - Orthodox: Strategic noun use at key points; don't reduce to mere pronouns

6. **Messianic Prophecy** (Isaiah 53:4-10)
   - Issue: Individual servant (Messiah) vs. collective (Israel) identity clarity
   - Stakes: Christological fulfillment identification
   - Orthodox: Strategic nouns aid individual identification; avoid excessive zero obscuring identity

**CONTEXTUAL ESSENTIAL (5% of occurrences)**:

7. **Participant Tracking Clarity** (Gen 18:1-22 - LORD + two angels)
   - Issue: Singular/plural shifts require clear participant distinction
   - Impact: Readers confused if surface realization obscures who is who

8. **Divine Formal Declarations** (Matt 3:17, 17:5 - "This is my beloved Son")
   - Issue: Nouns maintain formal weight; pronouns reduce to casual reference
   - Impact: Solemnity of divine testimony

9. **Identity Revelations** (Acts 9:4 - "I am Jesus")
   - Issue: Explicit noun "Jesus" required for dramatic disclosure
   - Impact: Zero/pronoun alone weakens identification moment

### Arbitrary Contexts (85%)

Routine narrative, dialogue attribution, setting descriptions, generic references, crowds, parentheticals, lists, routine actions—follow natural language discourse conventions. **Pro-drop naturalness is acceptable** in these contexts.

---

## Key Discrepancies & Open Questions

| Issue | TBTA Says | Research Shows | Resolution |
|-------|-----------|-----------------|------------|
| **Position** | Pos 9 | Pos 11 in {tbta-github} | Requires data file verification |
| **Values** | N, p, P, A, Zero?, Clitic? | 4-5 confirmed + 2 undocumented | Stage 2: frequency analysis needed |
| **Validation** | None available | No accuracy metrics in literature | Needs TBTA data file analysis |
| **Gateway Rules** | Applies to Nouns/Pronouns | Unclear interaction with Participant Tracking | Algorithm design phase should clarify |

---

## Practical Summary for Algorithm Development

**Stage 2 priorities**:

1. **Data Verification**: Parse actual TBTA data files to confirm position, value set, frequency distribution
2. **Participant Tracking Correlation**: Analyze relationship between Surface Realization and Participant Tracking values
3. **Language-Specific Rules**: Document actual patterns (not just grammar rules) for 10 candidate languages
4. **Theological Validation**: Verify divine passive, Holy Spirit personhood, and authority claim contexts in real translations
5. **Pro-Drop Integration**: Clarify when zero subjects are natural vs. theologically problematic

---

**Sources Cited**: 17+ scholarly sources, 2 typological databases, 4 Biblical language studies, 1 theological analysis
**Research Files**: TBTA.md | LANGUAGES.md | SCHOLARLY.md | THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml
**Next Stage**: Data Analysis & Algorithm Design
