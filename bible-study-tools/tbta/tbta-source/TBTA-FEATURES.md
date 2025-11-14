# TBTA Feature Catalog

**Total**: 59 features across 15 categories
**Source**: Comprehensive review of TBTA implementation (2025-11-14)

## Overview

TBTA (Text-Based Translation Assistance) provides linguistic annotations across three priority tiers:

- **Tier A (19 features)**: Essential for most translation projects - affects 1000+ languages, cannot be easily inferred
- **Tier B (20 features)**: Important for many projects - common features, sometimes inferable from context
- **Tier C (20 features)**: Specialized use cases - helpful but often derivable or language-specific

**Current Implementation Status**:
- Tier A: 68% complete (13/19), 100% documented (19/19)
- Tier B: 15% complete (3/20), 100% documented (20/20)
- Tier C: 0% complete (0/20), 70% documented (14/20)

---

## Tier A: Essential Features (19 Features)

**Priority**: Highest - affects 1000+ languages, cannot be easily inferred from context

### Noun Features (7 features)

| # | Feature | Values/Options | Example Languages | Status |
|---|---------|----------------|-------------------|--------|
| 1 | **Number System** | Singular (S), Dual (D), Trial (T), Quadrial (Q), Paucal (p), Plural (P) | Hawaiian, Samoan, Slovenian | ✅ Complete |
| 2 | **Person System** | 1st/2nd/3rd + Inclusive/Exclusive (8-way system) | Tagalog, Malay, Fijian, Vietnamese | ✅ Complete |
| 3 | **Participant Tracking** | First Mention, Routine, Exiting, Restaging, Frame Inferable | Japanese, Korean, Bantu languages | ✅ Complete |
| 4 | **Proximity System** | Near Speaker/Listener/Both, Remote Visible/Invisible, Temporal, Discourse (10-way) | Japanese, Korean, Spanish, Tagalog | ✅ Complete |
| 5 | **Noun List Index** | 1-9, A-Z, a-z (entity tracking) | Navajo, Kiowa, PNG languages | ✅ Complete |
| 6 | **Polarity** | Affirmative, Negative | Turkish, Finnish, Russian | ✅ Complete |
| 7 | **Surface Realization** | Noun, Pronoun, Zero, Clitic | Spanish, Japanese, Italian | ✅ Complete |

### Verb Features (3 features)

| # | Feature | Values/Options | Example Languages | Status |
|---|---------|----------------|-------------------|--------|
| 8 | **Time Granularity** | Immediate/Today/Yesterday/Remote/Discourse (20+ values) | Tagalog, Yagua, Kiksht, ChiBemba | ✅ Complete |
| 9 | **Aspect** | Perfective, Imperfective, Progressive, Habitual, Inceptive, Completive | Russian, Polish, Mandarin, Arabic | ✅ Complete |
| 10 | **Mood** | Indicative, Imperative, Subjunctive, Potential, Obligation | Turkish, Japanese, Greek | ✅ Complete |

### Noun Phrase Features (1 feature)

| # | Feature | Values/Options | Example Languages | Status |
|---|---------|----------------|-------------------|--------|
| 11 | **Semantic Role** | Agent, Patient, Source, Destination, Instrument, Beneficiary | Ergative languages, Filipino | 🟨 Documented |

### Clause Features (8 features)

| # | Feature | Values/Options | Example Languages | Status |
|---|---------|----------------|-------------------|--------|
| 12 | **Illocutionary Force** | Declarative, Interrogative, Imperative, Suggestive, Jussive | Japanese, Chinese, Korean | ✅ Complete |
| 13 | **Speaker Demographics** | 6 sub-features: Age, Gender, Relationship, Attitude, Speech Style | Japanese, Korean, Javanese, Thai | ✅ Complete |
| 14 | **Discourse Genre** | Narrative, Expository, Poetic, Legal, Prophetic, Epistolary | All languages | ✅ Complete |
| 15 | **Topic NP** | Agent-like, Patient-like | Japanese, Korean, Chinese, Tagalog | 🟨 Documented |
| 16 | **Salience Band** | Foreground, Background, Setting, Pivotal | Bantu languages, many African | 🟨 Documented |
| 17 | **Speaker** | Identity and characteristics | All languages | ✅ Complete |
| 18 | **Listener** | Identity and characteristics | All languages | ✅ Complete |
| 19 | **Speaker-Listener Age** | Relative age relationships | Japanese, Korean, Javanese | ✅ Complete |

**Tier A Summary**: 13/19 complete (68%), 19/19 documented (100%)

---

## Tier B: Important Features (20 Features)

**Priority**: Medium - common linguistic features, but sometimes inferable from context

### Word-Level Features (12 features)

| # | Feature | Category | Values/Options | Status |
|---|---------|----------|----------------|--------|
| 20 | **Reflexivity** | Verb | Reflexive, Non-reflexive | 🟨 Documented |
| 21 | **Degree** | Adjective/Adverb | Positive, Comparative, Superlative | 🟨 Documented |
| 22 | **Lexical Sense (Verbs)** | Verb | Multiple senses per verb | 🟨 Documented |
| 23 | **Lexical Sense (Adpositions)** | Adposition | Multiple senses per preposition | 🟨 Documented |
| 24 | **Lexical Sense (Conjunctions)** | Conjunction | Multiple senses per conjunction | 🟨 Documented |
| 25 | **Special Types** | Adposition | Genitive, Kinship relationships | 🟨 Documented |
| 26 | **Implicit Flag** | Conjunction | Explicit, Implicit | 🟨 Documented |
| 27 | **Particle Type** | Particle | QuoteBegin, QuoteEnd, Focus, Topic | 🟨 Documented |
| 28 | **Usage** | Adjective | Attributive, Predicative | 🟨 Documented |
| 29 | **Polarity (Verb)** | Verb | Affirmative, Negative | ✅ Complete |
| 30 | **Degree (Verb)** | Verb | Positive, Comparative, Superlative | 🟨 Documented |
| 31 | **Degree (Adverb)** | Adverb | Positive, Comparative, Superlative | 🟨 Documented |

### Phrase-Level Features (5 features)

| # | Feature | Category | Values/Options | Status |
|---|---------|----------|----------------|--------|
| 32 | **Sequence** | All Phrase Types | Ordering information | 🟨 Documented |
| 33 | **Implicit Flag** | All Phrase Types | Explicit, Implicit | 🟨 Documented |
| 34 | **Relativized** | Noun Phrase | Relative clause indicators | 🟨 Documented |
| 35 | **Thing Relationship** | Noun Phrase | Relationship types | ⬜ Rare field |
| 36 | **Usage (Phrase)** | Adjective Phrase | Attributive, Predicative | 🟨 Documented |

### Clause Features (3 features)

| # | Feature | Category | Values/Options | Status |
|---|---------|----------|----------------|--------|
| 37 | **Clause Type** | Clause | Main, Subordinate, Relative, etc. | 🟨 Documented |
| 38 | **Implicit Information** | Clause | Implicit elements | 🟨 Documented |
| 39 | **Rhetorical Question** | Clause | True question vs. rhetorical | 🟨 Documented |

**Tier B Summary**: 3/20 complete (15%), 20/20 documented (100%)

---

## Tier C: Specialized Features (20 Features)

**Priority**: Lower - helpful but often derivable or language-specific

### Word-Level Features (6 features)

| # | Feature | Category | Values/Options | Status |
|---|---------|----------|----------------|--------|
| 40 | **Participant Status** | Noun | Status indicators | 🟨 Documented |
| 41 | **Target Tense** | Verb | Target language tense | ⬜ Not documented |
| 42 | **Target Aspect** | Verb | Target language aspect | ⬜ Not documented |
| 43 | **Target Mood** | Verb | Target language mood | ⬜ Not documented |
| 44 | **Multi-word Expressions** | Phrasal | Phrasal units | ⬜ Not documented |
| 45 | **Degree (Adjective)** | Adjective | Positive, Comparative, Superlative | 🟨 Documented |

### Phrase-Level Features (4 features)

| # | Feature | Category | Values/Options | Status |
|---|---------|----------|----------------|--------|
| 46 | **Sequence (NP)** | Noun Phrase | Ordering | 🟨 Documented |
| 47 | **Sequence (VP)** | Verb Phrase | Ordering | 🟨 Documented |
| 48 | **Sequence (AdjP)** | Adjective Phrase | Ordering | 🟨 Documented |
| 49 | **Sequence (AdvP)** | Adverb Phrase | Ordering | 🟨 Documented |

### Clause Features (7 features)

| # | Feature | Category | Values/Options | Status |
|---|---------|----------|----------------|--------|
| 50 | **Notional Structure** | Clause | Semantic structure | ⬜ Partial |
| 51 | **Alternative Analysis** | Clause | Alternative interpretations | ⬜ Partial |
| 52 | **Vocabulary Alternate** | Clause | Alternative word choices | ⬜ Not documented |
| 53 | **Sequence (Clause)** | Clause | Clause ordering | 🟨 Documented |
| 54 | **Location in Discourse** | Clause | Position in discourse | 🟨 Documented |
| 55 | **Implicit (Clause)** | Clause | Implicit elements | 🟨 Documented |
| 56 | **Implicit (VP)** | Verb Phrase | Implicit elements | 🟨 Documented |

### Discourse Features (3 features)

| # | Feature | Category | Values/Options | Status |
|---|---------|----------|----------------|--------|
| 57 | **Paragraph Markers** | Discourse | Paragraph boundaries | 🟨 Documented |
| 58 | **Episode Markers** | Discourse | Episode boundaries | 🟨 Documented |
| 59 | **Implicit (NP/AdjP/AdvP)** | Phrase | Implicit elements | 🟨 Documented |

**Tier C Summary**: 0/20 complete (0%), 14/20 documented (70%)

---

## Features by Category

### Category 1: Nouns (8 features)
1. Number System ✅
2. Person System ✅
3. Participant Tracking ✅
4. Noun List Index ✅
5. Proximity System ✅
6. Polarity ✅
7. Surface Realization ✅
8. Participant Status 🟨

### Category 2: Verbs (10 features)
1. Time Granularity ✅
2. Aspect ✅
3. Mood ✅
4. Reflexivity 🟨
5. Polarity ✅
6. Degree 🟨
7. Target Tense ⬜
8. Target Aspect ⬜
9. Target Mood ⬜
10. Lexical Sense 🟨

### Category 3: Adjectives (3 features)
1. Degree 🟨
2. Usage 🟨
3. Usage (Phrase level) 🟨

### Category 4: Adverbs (2 features)
1. Degree 🟨
2. Sequence 🟨

### Category 5: Adpositions (2 features)
1. Lexical Sense 🟨
2. Special Types (Genitive, Kinship) 🟨

### Category 6: Conjunctions (2 features)
1. Lexical Sense 🟨
2. Implicit Flag 🟨

### Category 7: Phrasal Elements (1 feature)
1. Multi-word Expressions ⬜

### Category 8: Particles (1 feature)
1. Type (QuoteBegin/End, Focus, Topic) 🟨

### Category 101: Noun Phrases (5 features)
1. Sequence 🟨
2. Semantic Role 🟨
3. Implicit 🟨
4. Thing Relationship ⬜
5. Relativized 🟨

### Category 102: Verb Phrases (2 features)
1. Sequence 🟨
2. Implicit 🟨

### Category 103: Adjective Phrases (3 features)
1. Sequence 🟨
2. Usage 🟨
3. Implicit 🟨

### Category 104: Adverb Phrases (2 features)
1. Sequence 🟨
2. Implicit 🟨

### Category 105: Clauses (18 features)
1. Clause Type 🟨
2. Illocutionary Force ✅
3. Topic NP 🟨
4. Speaker ✅
5. Listener ✅
6. Speaker's Attitude ✅
7. Speaker's Age ✅
8. Speaker-Listener Age ✅
9. Speech Style ✅
10. Discourse Genre ✅
11. Notional Structure ⬜
12. Salience Band 🟨
13. Sequence 🟨
14. Location in Discourse 🟨
15. Implicit Information 🟨
16. Alternative Analysis ⬜
17. Vocabulary Alternate ⬜
18. Rhetorical Question 🟨

### Category 110: Paragraph Markers (1 feature)
1. Paragraph Boundaries 🟨

### Category 120: Episode Markers (1 feature)
1. Episode Boundaries 🟨

---

## Status Legend

- ✅ **Complete**: Fully implemented with data generation and validation
- 🟨 **Documented**: Schema/documentation exists but data generation incomplete
- ⬜ **Not Started**: No documentation or implementation

---

## Implementation Priority

Based on the three-tier structure, development should focus on:

1. **Complete Tier A** (6 remaining features): Semantic Role, Topic NP, Salience Band
2. **Complete Tier B high-value features** (17 remaining): Focus on phrase-level and clause features
3. **Document Tier C essentials** (6 undocumented features): Target tense/aspect/mood, multi-word expressions, vocabulary alternates

---

**Last Updated**: 2025-11-14
**Source**: `/workspaces/mybibletoolbox-code/plan/tbta-comprehensive-review.md`
