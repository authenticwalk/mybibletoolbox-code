# TBTA Linguistic Features

Comprehensive research on TBTA's linguistic annotation system, organized by feature category. This directory consolidates findings from multiple research projects into practical guidance for reproducing TBTA annotations.

## Overview

TBTA (Translation by Translation Annotation) provides semantic features for biblical texts to enable accurate translation into 1000+ languages. Each feature captures linguistic distinctions that may be obligatory in target languages but ambiguous in source texts.

**See also:** [FEATURE-SUMMARY.md](./FEATURE-SUMMARY.md) - Quick reference table of all features

---

## Person Systems

Clusivity (inclusive/exclusive "we") affects 200+ languages, predominantly Austronesian. Critical for theological interpretation: Lord's Prayer, apostolic authority statements, church unity passages require explicit decisions.

**Key Finding:** Austronesian languages almost universally exhibit clusivity (kita/kami pattern). Validation shows 100% accuracy when proper context analysis applied.

**Status:** Complete with validated examples

[Read detailed analysis →](person-systems/)

---

## Number Systems

Dual (2), trial (3), and paucal (few) number distinctions affect translation accuracy. Languages like Hawaiian, Samoan, Arabic require explicit marking beyond singular/plural.

**Key Finding:** TBTA encodes 8+ number values. Target language mapping shows clear patterns by language family (Austronesian = dual/trial common, Semitic = dual common, Slavic = occasional dual preservation).

**Status:** Complete with language breakdown

[Read detailed analysis →](number-systems/)

---

## Proximity Systems

Demonstrative proximity (near/far distinctions) varies dramatically: 2-way systems (54% of languages), 3-way systems (38%), up to 29-way systems (Chevak Cup'ik). Special features include visibility distinctions, elevation marking, person-orientation.

**Key Finding:** TBTA's 10-value system (5 spatial, 2 temporal, 2 discourse, 1 N/A) covers ~90% of cross-linguistic needs. Greek 3-way system (ὅδε/οὗτος/ἐκεῖνος) maps cleanly; Hebrew unmarked system (זֶה) requires context inference.

**Status:** Complete with typological analysis

[Read detailed analysis →](proximity/)
[Read language typology →](proximity/language-typology.md)

---

## Polarity

Negative marking (affirmative vs negative) affects scope, constituent negation, and negative concord languages. Critical for languages with multiple negative strategies or negative concord requirements.

**Key Finding:** TBTA's 7-value system captures sentential negation, constituent negation, and complex polarity interactions. Essential for accurate negative scope in target languages.

**Status:** Complete

[Read detailed analysis →](polarity/)

---

## Degree

Comparative, superlative, and intensification marking for adjectives, adverbs, verbs. Different parts of speech have different available values (11 for adjectives, 8 for adverbs/verbs).

**Key Finding:** Degree is constructional, not just morphological. Annotators must analyze full constructions (morphology + syntax + lexical items). Language typology determines strategy: synthetic (Slavic, Germanic) vs analytic (English, Mandarin) vs mixed (Romance).

**Status:** Complete with cross-linguistic methodology

[Read detailed analysis →](degree/)

---

## Verb TAM (Tense-Aspect-Mood)

Time, aspect, and modality annotation for verbs. Four-stage process: source language analysis → semantic mapping → discourse integration → target validation.

**Key Finding:** Time feature uses 9 values with discourse-relative anchoring. Aspect captures viewpoint (perfective/imperfective) + phasal (inceptive/cessative). Mood includes epistemic and deontic modality.

**Status:** Complete with annotation methodology

[Read detailed analysis →](verb-tam/)

---

## Participant Tracking

Information structure marking: first mention, routine reference, exit, restage. Critical for languages with switch-reference, topic marking, or obligatory participant tracking.

**Key Finding:** Discourse-level feature requiring multi-verse analysis. Essential for Japanese/Korean topic particles, Bantu participant tracking, switch-reference languages.

**Status:** Complete with validation experiments

[Read detailed analysis →](participant-tracking/)

---

## Discourse Genre

Genre classification (narrative, expository, poetic, legal, prophetic, epistolary) affects register, verb selection, clause structure, and information packaging.

**Key Finding:** Genre distinctions are obligatory in many languages for verb aspect selection, honorific levels, and clause linkage strategies. Mixed genres (e.g., narrative embedded in epistle) require careful analysis.

**Status:** Complete

[Read detailed analysis →](discourse-genre/)

---

## Honorifics and Register

Speaker/listener demographics (age, gender, social relationship, attitude) determine honorific marking in Japanese, Korean, Javanese, Thai, and others.

**Key Finding:** Multi-dimensional system encoding relative age, social distance, formality, and attitude. Biblical texts require cultural translation: Roman social hierarchies → target culture equivalents.

**Status:** Complete with language matrix

[Read detailed analysis →](honorifics-register/)

---

## Illocutionary Force

Speech act classification (declarative, interrogative, imperative, exclamative, etc.) determines sentence-final particles, intonation, and clause structure.

**Key Finding:** East Asian languages (Japanese, Mandarin, Korean) require explicit sentence particles. Rhetorical questions vs information-seeking questions need distinction. Indirect speech acts complicate annotation.

**Status:** Complete

[Read detailed analysis →](illocutionary-force/)

---

## Time Granularity

Temporal precision distinctions (immediate, today, yesterday, last week, remote past, future timeframes) required by languages with obligatory temporal distance marking.

**Key Finding:** TBTA Time feature uses discourse-relative anchoring, not absolute timeframes. Languages vary: Yagua (5-way past/present/future), ChiBemba (multiple past tenses), Kiksht (proximal/distal temporal).

**Status:** Complete

[Read detailed analysis →](time-granularity/)

---

## Surface Realization

How participants are expressed: noun, pronoun, zero anaphora, clitic. Critical for pro-drop languages (Spanish, Japanese, Italian) and languages with obligatory overt subjects (English, French).

**Key Finding:** Discourse continuity determines realization strategy. Topic continuity → zero/clitic; topic shift → full noun; emphasis → pronoun. Language-specific constraints override general preferences.

**Status:** Complete

[Read detailed analysis →](surface-realization/)

---

## Additional Features Identified from Language Family Research

Based on comprehensive language family analysis (see [../languages/](../languages/)), the following additional features have been identified as critical for Bible translation. These features are OBLIGATORY in multiple language families and require translator decisions not explicit in Greek/Hebrew source texts.

**Status:** Proposed features requiring documentation and tool development

### NEW Features Requiring Implementation

1. **Voice Systems** - Austronesian symmetrical voice (Philippine-type)
   - 4-voice obligatory systems (Tagalog, Cebuano, Ilokano): actor, patient, location, instrument focus
   - Every verb requires voice marking decision
   - Affects 176 Austronesian languages

2. **Evidentiality** - Information source marking (Trans-New Guinea, Quechuan)
   - ~50 Highlands languages: OBLIGATORY witnessed/reported/inferential marking
   - Critical for Gospel narratives: "Jesus rose" requires evidential marking
   - Categories: visual, reportive, inferential, participatory

3. **Switch-Reference** - Same/different subject marking (Trans-New Guinea)
   - Nearly universal in Trans-New Guinea (141 languages)
   - Medial verbs mark subject continuity across clause chains
   - Example: "He came and sat down" requires same-subject marker

4. **Noun Classes** - Niger-Congo gender/class systems
   - 10-20 classes OBLIGATORY in Bantu (94 languages)
   - Every noun (God, Jesus, angels, abstract concepts) requires class assignment
   - Classes affect all concordial agreements (adjectives, verbs, pronouns)

5. **Serial Verb Constructions** - Trans-New Guinea verb serialization
   - Limited verb roots (some languages ~60!) require serial constructions
   - Causative: serial "give" + main verb
   - Aspectual: serial "stay" (progressive), "finish" (completive)
   - Benefactive: serial "give" for recipient marking

6. **Spatial Deixis/Elevation** - Vertical/directional marking
   - Trans-New Guinea: "go up/down" requires elevation specification
   - Biblical "go up to Jerusalem" maps naturally to elevation systems
   - Ascension/descension language highly salient

7. **Tone Systems** - Lexical and grammatical tone
   - Niger-Congo: Tone NOT optional - as essential as consonants/vowels
   - Otomanguean: Tone for INFLECTION - most complex systems in world
   - Prevents theological misunderstanding, affects definiteness

8. **Numeral Classifiers** - Shape/function classification (Mayan, Sino-Tibetan)
   - All 22 Mayan languages: ESSENTIAL feature
   - "Twelve tribes" requires classifier choice (shape/group/people?)
   - Affects theological emphasis: "Body of Christ" classifier choice matters

9. **Positional Verbs** - Posture/configuration marking (Mayan)
   - 250-500 distinct roots per Mayan language
   - "Jesus sat down" requires specific seated positional
   - Position carries cultural/theological meaning (authority, readiness, rest)

10. **Ergative-Absolutive Alignment** - Case marking systems
    - All 22 Mayan languages, many Australian languages
    - Transitive subjects marked differently than intransitive
    - Affects translation of Greek passive, active voice

11. **Directional Morphology** - Motion direction encoding (Mayan, Ch'olan)
    - Verbal affixes encode toward/away/up/down motion
    - "Come to me" vs "go away" through directional marking
    - Missional directionality: sending vs gathering

12. **Root-and-Pattern Morphology** - Non-linear morphology (Afro-Asiatic)
    - Consonantal roots, vowel patterns add grammatical information
    - Arabic K-T-B root: KiTaB (book), KaTaBa (write), maKTaB (office)
    - Cannot segment linearly, must recognize root-pattern interdigitation

13. **Polysynthetic Structures** - Single-word sentences (Uto-Aztecan, some Eskimo-Aleut)
    - Verb can encode subject, object, tense, aspect, mode in one word
    - Nahuatl: "onikpix" = complete sentence "I held it"
    - Extensive incorporation of arguments into verb complex

14. **Kinship-Influenced Grammar** - Australian dual variations
    - Dual pronouns vary by relationship between the two referents
    - Warlpiri: Different dual forms for kin vs. non-kin pairs
    - "Triangular terms" indicate relation of speaker + listener to referent

**See Also:** [Language Family Insights Application](../../language-insights-application.md) for complete feature list with family-specific examples

### Enhanced Features Requiring Expansion

The following existing features should be expanded with family-specific insights:

1. **Person Systems** → Add T-V distinction (Indo-European formal/informal "you")
2. **Number Systems** → Add class-based number (Niger-Congo), kinship-influenced dual (Australian)
3. **Honorifics** → Add age-based kinship terms (Niger-Congo), T-V cultural variations
4. **Possession Systems** → Add inalienable/alienable distinctions (Mayan, Austronesian, Trans-New Guinea)
5. **Aspect Systems** → Add aspect-prominence vs tense-prominence (Slavic, Mayan, Otomanguean)

---

## Integration Priorities

**Always Check:**
1. NounListIndex (participant tracking across clauses)
2. Participant Tracking (information structure)
3. LexicalSense (polysemy resolution)

**Check for Ambiguity:**
1. Person (inclusive/exclusive distinctions)
2. Number (dual/trial/paucal)
3. Semantic Role (case marking, word order)

**Check for Register:**
1. Speaker Demographics (honorifics)
2. Discourse Genre (register selection)
3. Illocutionary Force (sentence particles)

**Check for Your Language:**
- Austronesian → Person, Number, Proximity
- East Asian → Proximity, Demographics, Topic, Particles
- Native American → Person, Proximity, Switch-reference
- Bantu → Participant Tracking, Salience, Agreement
- Slavic → Aspect, Case, Degree

---

## Methodology Summary

All features follow a consistent annotation methodology:

1. **Source Analysis**: Identify morphological, syntactic, and contextual indicators in Greek/Hebrew
2. **Semantic Mapping**: Map to language-neutral TBTA feature values
3. **Discourse Integration**: Consider multi-verse context and discourse structure
4. **Target Validation**: Verify applicability across diverse target language systems
5. **Iterative Refinement**: Update based on translation feedback and edge cases

---

## Research Status

**Complete Features:** All 13 features documented with practical annotation guidelines
**Validation:** Multiple experiments completed across feature types
**Coverage:** 1009 languages analyzed for typological patterns
**Next Steps:** Systematic validation across full biblical corpus, language-specific decision trees

---

## Using This Documentation

1. **Overview First**: Read this README for high-level understanding
2. **Feature Deep-Dive**: Explore individual feature directories for details
3. **Practical Application**: Use LEARNINGS.md files for annotation methodology
4. **Quick Reference**: Use FEATURE-SUMMARY.md for rapid lookup
5. **Comprehensive Catalog**: Use ALL-FEATURES.md for complete feature inventory

Each feature directory contains:
- **README.md**: Overview and key findings
- **LEARNINGS.md**: Practical methodology for reproducing annotations
- **Experiments**: Validation studies and test cases
- **Examples**: Annotated biblical passages showing feature application

---

**Last Updated:** 2025-11-06
**Consolidated from:** Multiple research branches
**Consolidated For:** tbta-rebuild-with-llm
