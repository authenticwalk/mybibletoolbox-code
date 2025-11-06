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
