# Topic NP: Research Synthesis

**Feature**: Topic NP (Discourse Topic Marking)
**TBTA Status**: Tier A Essential | Category 105 (Clause-level) | Position 4
**Date**: 2025-11-25 | **Researcher**: Claude Code

---

## Executive Summary

Topic NP identifies which noun phrase serves as the discourse topic (what the clause is "about"), distinct from grammatical subject. This feature is critical for ~25-30% of world languages (topic-prominent: Japanese, Korean, Mandarin, Tagalog) where grammatical topic markers (wa/ga, eun/neun) are mandatory for natural translation. In subject-prominent languages (English, Spanish), topic-marking is optional. **Theologically, this is primarily an arbitrary/stylistic feature (95% of contexts); theological stakes are non-arbitrary only in rare contrastive or emphatic polemical passages (~5%).**

---

## 1. Feature Definition (see TBTA.md)

**Concept**: Clause-level feature distinguishing topic (discourse pragmatics: what the clause is "about") from subject (grammatical syntax: who/what performs the verb).

**Foundational Distinction** (Li & Thompson 1976):
- Subject-prominent languages (~60%): English, French, German. Subject is primary syntactic pivot.
- **Topic-prominent languages (~25-30%): Mandarin, Japanese, Korean, Thai, Vietnamese, Indonesian, Tagalog.** Topic is primary; topic-comment structure takes precedence.
- Both systems (~10-15%): Austronesian (Tagalog); distinct topic AND subject systems.

**Key Values**:
| Value | Meaning | Frequency | Encoding |
|-------|---------|-----------|----------|
| **A** | Agent-like Topic | 15-20% | "Most Agent-like" |
| **P** | Patient-like Topic | 10-15% | "Most Patient-like" |
| **N** | No Topic (subject-predicate) | 70% | Field absent |

**Gateway Feature**: Part = "Clause" (Category 105). Valid only for clauses with overt NP.

---

## 2. Typological Distribution (see LANGUAGES.md)

**Source Languages**:
- **Hebrew**: Mixed (VSO neutral order → topic-fronting marks SVO). No morphological topic markers.
- **Greek**: Subject-prominent. Preverbal position signals pragmatic prominence (topic or focus).

**Database Coverage** (1,009 translation varieties analyzed):

| Family | Languages | Topic-Requirement | Status |
|--------|-----------|-------------------|--------|
| **Japonic** | Japanese (1) | Mandatory (wa/ga) | Excellent |
| **Sino-Tibetan** | Mandarin (3), Burmese (2) | Strong | Good |
| **Koreanic** | Korean (0) | Mandatory (eun/neun) | **CRITICAL GAP** |
| **Kra-Dai** | Thai (1) | Strong (positional) | Good |
| **Austroasiatic** | Vietnamese (2) | Moderate | Good |
| **Austronesian** | Tagalog, Cebuano, Indonesian (176 total) | Mixed (Both systems) | Excellent |
| **Indo-European** | English, Spanish, French, German (135+) | Optional (emphatic only) | High coverage |

**Recommended 8 Candidates for Stage 2**: English, Mandarin, Japanese, Thai, Tagalog, Indonesian, Spanish, Vietnamese. **Critical gap**: Korean (~82M speakers) absent from database.

---

## 3. Scholarly Foundation (see SCHOLARLY.md)

**Core Linguistic Theory** (30+ sources):
- **Li & Thompson (1976)**: Foundational four-way typology distinguishing topic from subject.
- **Lambrecht (1994)**: Information structure framework. Topic = "already established matter of current concern."
- **Chafe (1976)**: Given/new distinction. Topics typically GIVEN; new information → focus.
- **Givón (1983)**: Topic as SCALAR property (gradient, not binary), measured by referential distance, persistence.
- **Vallduví & Engdahl (1996)**: Cross-linguistic variation in encoding information structure (intonation vs syntax).

**Application to Biblical Texts**:
- **Levinsohn (2000)**, **Runge (2010)**: Discourse Features of Greek NT. Identify propositional topics, points of departure.
- **Shimasaki (1999)**: Focus Structure in Biblical Hebrew. Hebrew word order (VSO → SVO) marks topic/focus.
- **Dooley & Levinsohn (2001)**: SIL Bible Translators' Manual. Topic-comment structures essential for Asian languages.

**Translation Case Studies**:
- **Japanese**: wa (topic) vs ga (subject). John 8:12 "Jesus-WA... Jesus as continuing topic.
- **Korean**: eun/neun (topic) vs i/ga (subject). Matthew 5:3 "Blessed the poor": poor as topic.
- **Mandarin**: Topic-comment structure natural for fronted elements. Psalm 118:22: "Stone (topic) - rejected builders (comment)."

**Key Biblical Passages Requiring Topic Analysis**:
- **John 1:1**: Predicate nominative topic-comment. "The Word (topic) was God (comment)."
- **Matthew 5:3-11**: Beatitudes predicative. "Blessed (adjective) - poor/meek (topic)."
- **Genesis 1:26**: Trinitarian context with "us" reference. Topic-marking affects emphasis on divine plurality.
- **John 8:12-59**: Extended dialogue. Topic continuity with Jesus as continuing topic across 47 verses.

---

## 4. Theological Stakes (see THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)

**Default Classification**: **ARBITRARY (95%)** — Choice is stylistic/discourse-structural, not doctrinal.

**Why Mostly Arbitrary**:
- Topic-NP encodes INFORMATION STRUCTURE (given vs new), not PROPOSITIONAL CONTENT (who, what, relationships).
- Theological truth is SEMANTIC (predicates, quantifiers, relationships), not discourse-structural.
- Example: "Jesus healed the man" = "Jesus (topic), he healed the man" → Same propositional content, different topic-marking.

**Non-Arbitrary Contexts** (5%): Contextual, not Theological
1. **Contrastive Polemic** (Romans 3:28, Galatians 2:16): Topic-marking emphasizes "faith" vs "works" in justification debate. Affects CLARITY, not doctrine. Acceptable values: A-topic or N-subject.
2. **Trinitarian Statements** (John 1:1, Philippians 2:6): Topic-marking affects INFORMATION FLOW about Christ's deity, not the fact itself. Predicate ("was God") carries doctrine, not topic-structure. **Acceptable**: Any marking. **No forbidden values**.
3. **Beatitudes** (Matthew 5:3-11): Topic-marking natural for predicative constructions. Preferred: P-topic (patient). Acceptable: N-subject.
4. **Discourse Coherence** (John 8:12-59): Topic continuity essential for narrative clarity. Theological stakes: LOW (coherence only).

**Theological Safety**: Topic-marking CANNOT cause heresy. Arianism, Modalism, Works-Righteousness are SEMANTIC errors (wrong predicates), not topic-marking errors.

---

## 5. Key Discrepancies & Clarifications

**Discrepancy 1: Value Encoding**
- **TBTA.md** describes "N" value for "no topic" clauses
- **Actual TBTA data** (samples): Field is ABSENT for clauses without topics (not explicitly "N")
- **Implication**: Annotation practice: clauses with topics receive A/P; clauses without topics have no "Topic NP" field

**Discrepancy 2: Non-A/P Topics**
- **Linguistic reality**: Topics can be locative (room), temporal (tomorrow), instrumental (hammer)
- **TBTA limitation**: Only encodes A/P (borrowed from Semantic Role terminology)
- **Impact**: Non-A/P topics likely unmarked or assigned N in TBTA

**Clarification: Information Structure vs Discourse Function**
- **TBTA policy**: "Discourse function over morphological form" (pragmatic, not structural)
- **Practice**: Topic NP values derived from Semantic Role (A/P), which is a simplification of richer linguistic reality

---

## 6. Research Files & Links

- **`TBTA.md`** (368 lines): Comprehensive TBTA documentation review with policy details, edge cases, validation strategy
- **`LANGUAGES.md`** (325 lines): Typological analysis of 1,009 translation varieties; language family breakdown; candidate selection for Stage 2
- **`SCHOLARLY.md`** (1,050 lines): 30+ scholarly sources, information structure theory, Biblical language analysis, translation case studies, 8 key verses
- **`THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml`** (368 lines): Arbitrary/non-arbitrary classification with translator guidance for Christian orthodoxy

---

## 7. Next Steps (Stage 2: Translation Database)

1. **Prioritize** 8 candidate languages: English, Mandarin, Japanese, Thai, Tagalog, Indonesian, Spanish, Vietnamese
2. **Seek Korean** translation data (critical gap; major language with grammaticalized topic markers)
3. **Integrate** with Surface Realization (zero/pronoun/full NP) and Participant Tracking (new/given/routine/restaging)
4. **Test theological contexts**: Genesis 1:26 (Trinity), John 1:1 (Christology), Matthew 5:3-12 (Beatitudes)
5. **Validate** topic-marking accuracy via topic-prominent language translations (75-85% expected accuracy)

---

**Research Status**: COMPLETE. Ready for Stage 2 (Translation Database & Algorithm Development).
