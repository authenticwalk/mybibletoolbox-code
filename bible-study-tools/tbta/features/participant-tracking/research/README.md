# Participant Tracking: Research Summary

**Feature**: Participant Tracking (Discourse Referent Tracking)
**Research Status**: Stage 1 Complete | **Last Updated**: 2025-11-25

---

## Executive Summary

Participant tracking marks how discourse entities (characters, objects) are introduced, maintained, and reactivated across narrative. Universally necessary (all languages track participants somehow), but the grammatical encoding varies dramatically: 250+ switch-reference languages require morphological marking; topic-prominent languages (Japanese, Korean) use particles; pro-drop languages (Spanish, Hebrew, Greek) use zero pronouns; non-pro-drop languages (English, German) require explicit pronouns. This feature is **20% theologically or contextually critical** (Trinity passages, resurrection witnesses, vision disambiguation) and **80% stylistically flexible**.

---

## 1. TBTA Documentation Analysis

**[Full Details: TBTA.md](./TBTA.md)**

### Concept
Linguistic feature marking discourse status of noun/pronoun referents. Controls when full noun vs. pronoun vs. zero anaphora is appropriate.

### Values (9 defined, 5 productive)
| Code | Value | Usage | Status |
|------|-------|-------|--------|
| **D** | Routine | 73% | PRIMARY |
| **G** | Generic | 14% | High |
| **F** | Frame Inferable | 7.5% | Medium |
| **I** | First Mention | 5.4% | Low |
| **Q** | Interrogative | 0.2% | Rare |
| R | Restaging | 0% | **UNUSED** |
| i | Integration | 0% | **UNUSED** |
| E | Exiting | 0% | **UNUSED** |
| O | Offstage | 0.006% | **Negligible** |

### Key Finding: Gap Between Theory and Practice
TBTA defines 9 values but only uses 5. **Critical Gap**: Restaging (participant reintroduction after absence) defined but never annotated, despite biblical narrative containing ~50-100 restaging instances (Joseph in Genesis 37→39+; prophets reintroducing characters). Languages like Japanese (は wa) and Korean (은/는) require explicit restaging markers—TBTA provides no guidance.

### Gateway Feature
**Constraint**: Part = Noun or Pronoun (not applicable to verbs, adjectives)

### Labeling Policy
**Semantic rather than morphological**: God marked "Routine" in Genesis 1:1 despite being first textual mention (presupposition treated as routine). Conflates cultural presupposition with textual anaphora—problematic for ~50-100 entities (God, sun, moon, well-known locations).

### Coverage
11,649 verses across 34 books (~37% Bible), prioritizing narrative where participant tracking is critical.

---

## 2. Language Family & Typology Analysis

**[Full Details: LANGUAGES.md](./LANGUAGES.md)**

### Source Language Check
- **Biblical Hebrew**: Pro-drop (zero subjects); uses definiteness, word order, verb morphology
- **Biblical Greek (Koine)**: Pro-drop with article system
- **Neither language explicitly encodes participant tracking as discrete category**; both use multiple mechanisms

### Required Language Families
| Family | Languages | Requirement |
|--------|-----------|-------------|
| **Trans-New Guinea** | 200+ (Huli, Alekano, Kuman) | **MANDATORY** switch-reference morphology |
| **Sepik** | Iatmul, Manambu | **MANDATORY** switch-reference |
| **Japonic** | Japanese | **MANDATORY** topic particles (wa/ga) |
| **Koreanic** | Korean | **MANDATORY** topic particles (은/는) |
| **Romance** | Spanish, Portuguese, Italian | **MANDATORY** verb morphology; **OPTIONAL** pronouns |
| **Slavic** | Russian, Polish, Czech | **MANDATORY** verb morphology; **OPTIONAL** pronouns |
| **Sino-Tibetan** | Mandarin, Burmese | **MANDATORY** topic-prominence + classifiers |

### Candidate Languages (for Stage 2 Database)
1. **Iatmul** (Sepik): Switch-reference system, 27 books
2. **Huli** (Trans-New Guinea): Switch-reference, 78 books
3. **Japanese**: Topic-prominent (wa/ga distinction), 27 books
4. **Mandarin Chinese**: Topic-prominent + classifiers, 66 books
5. **Spanish**: Pro-drop + articles, 81 books
6. **Greek (Koine)**: Primary source language, 27 books
7. **English**: Non-pro-drop baseline, 81 books
8. **Swahili**: Noun class system, 66 books
9. **Quechua**: Pro-drop agglutinative, 66 books
10. **Tagalog**: Topic-prominent focus system, 66 books

---

## 3. Scholarly Research

**[Full Details: SCHOLARLY.md](./SCHOLARLY.md)**

### Foundational Theories
- **Givón (1983)**: Topic continuity scalar; referential distance, topic persistence, potential interference metrics
- **Comrie (1999)**: Two universal principles—coreference MORE marked locally; non-coreference MORE marked across clauses
- **Gundel-Hedberg-Zacharski (1993)**: Cognitive status ≠ accessibility; six distinct statuses predict referring expression form
- **Centering Theory (Grosz et al. 1995)**: Backward-looking center (current focus) predicts pronoun vs. full NP choice
- **Ariel (1990)**: Accessibility marking scale (full name > description > demonstrative > pronoun > zero)

### Key Finding: Theory-Practice Mismatch
Academic research provides quantitative methods (referential distance, topic persistence) for predicting participant reference form. TBTA uses semantic/intuitive labels (First Mention, Routine) without algorithmic rules. **Stage 2 Analysis should apply Givón's metrics to validate TBTA values or detect systematic deviation**.

### 29+ Scholarly Sources
Comprehensive coverage: linguistic typology, biblical discourse analysis, cognitive frameworks, translation case studies, WALS/Grambank databases. All cited with URLs in SCHOLARLY.md.

---

## 4. Theological & Contextual Significance

**[Full Details: THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](./THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)**

### Distribution
- **20% Non-Arbitrary**: Theological stakes (Trinity, Christology) or contextual confusion (participant enumeration, pronoun ambiguity)
- **80% Arbitrary**: Stylistic/optional (clear narratives, obvious pronouns, generic participants)

### CRITICAL (Theological): ~12%
1. **Trinity contexts** (Gen 1:26, 3:22, 11:7, Isa 6:8): "Let us"—participant ambiguity affects Trinity doctrine. Orthodox: Father, Son, Spirit. Non-orthodox: divine council (angels create—rejected), polytheism (heretical).
2. **Christology** (John 1:1): Word vs. God distinction. Wrong tracking = modalism (same person) or Arianism (lesser god).
3. **Trinitarian formula** (Matt 28:19): Three persons, one name. Wrong = tritheism (three gods) or modalism.
4. **Resurrection witnesses** (Mary Magdalene, 1 Cor 15:3-8): Historical verification. Wrong tracking undermines apologetic.
5. **Divine visions** (Rev 1:10-20, Matt 17:1-8): Christ as divine speaker. Wrong = obscures deity.
6. **Christophanies** (Gen 18, Judg 6): Angel of LORD as pre-incarnate Christ. Wrong = misses divine appearance theology.

### HIGH (Contextual Precision): ~8%
- **Participant enumeration** (John 21:2—seven disciples, five named)
- **Pronoun ambiguity resolution** (Acts 9/22/26—Paul's conversion: who heard/saw what?)
- **Singular/plural shifts** (Gen 18—confusing participant tracking)

---

## Key Discrepancies & Issues

| Issue | TBTA Finding | Research Finding | Impact |
|-------|-------------|------------------|--------|
| **Encoding Position** | Position 5 vs. 6 (discrepancy in sources) | Requires verification | Technical implementation |
| **Restaging Usage** | 0% (never annotated) | ~50-100 biblical instances + language requirement | **Critical gap** for Asian languages |
| **Presupposition** | Conflated with Routine | Should be distinct category | Confuses translators; ~50-100 instances |
| **Frame Inferable** | Inconsistent application | "Intuitive, not algorithmic" | No validation protocol |
| **Validation** | No cross-reference consistency | Single-pass annotation only | **15% improvement possible** via multi-stage validation |

---

## How to Use This Research

1. **Stage 2 (Analysis)**: Apply Givón's metrics (referential distance, topic persistence) to TBTA data. Validate whether Routine/Frame Inferable/Generic values correspond to linguistic predictions. Check restaging gap.

2. **Stage 3 (Experimentation)**: Test participant tracking in 5-10 candidate languages (switch-reference, topic-prominent, pro-drop varieties). Develop language-specific algorithms.

3. **Stage 4 (Validation)**: Train translators using this research. Test comprehension with participant enumeration (seven disciples), pronoun ambiguity (Saul's conversion), Trinity contexts (Gen 1:26).

---

**Total Research Compiled**: 750 lines across 4 files (TBTA, LANGUAGES, SCHOLARLY, THEOLOGICALLY-SIGNIFICANT-GROUPS) | **Citation Code**: {llm-cs45} (internal knowledge) + 29 scholarly sources | **Peer Review Required**: Trinity interpretation, Christophany identification, resurrection witness enumeration
