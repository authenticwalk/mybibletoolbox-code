# Topic NP - TBTA Documentation Review

**Feature**: Topic NP
**TBTA Tier**: Tier A (Essential) - Feature #15
**Status**: 🟨 Documented
**Category**: Clause-level feature (Category 105)

## Sources

- `{tbta-features}`: /bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md
- `{tbta-data-structure}`: /bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md
- `{tbta-readme}`: /bible-study-tools/tbta/tbta-source/README.md
- `{plan-readme}`: /plan/tbta/tbta-rebuild-with-llm/features/topic-np/README.md
- `{plan-topic-prominent}`: /plan/tbta/tbta-rebuild-with-llm/features/topic-np/TOPIC-PROMINENT-LANGUAGES.md
- `{plan-topic-vs-subject}`: /plan/tbta/tbta-rebuild-with-llm/features/topic-np/TOPIC-VS-SUBJECT.md
- `{tbta-samples}`: /plan/tbta/tbta-rebuild-with-llm/tbta-data/samples/*.json

---

## 1. Feature Definition

### Concept

**Topic NP identifies which noun phrase serves as the discourse topic (what the clause is "about"), distinct from grammatical subject.** `{plan-readme}`

**Topic vs. Subject - The Critical Distinction**: `{plan-topic-vs-subject}`

| Concept | Definition | Question Answered | Level |
|---------|------------|-------------------|-------|
| **SUBJECT** | Grammatical relation; verb agrees with it | "Who/what does the verb?" | Syntax |
| **TOPIC** | Discourse relation; what sentence is "about" | "What is this sentence about?" | Pragmatics |

**Key Insight**: In English (subject-prominent), subject and topic usually align. In Japanese/Korean/Chinese (topic-prominent), they frequently diverge. `{plan-topic-vs-subject}`

### Language Typology

`{plan-topic-vs-subject}` Li & Thompson (1976) four-way typology:

| Type | Description | Examples | % of Languages |
|------|-------------|----------|----------------|
| **Subject-prominent** | Subject is primary | English, French, German, Russian | ~60-65% |
| **Topic-prominent** | Topic is primary | Mandarin, Japanese, Korean, Thai | ~25-30% |
| **Both** | Distinct systems | Tagalog, Austronesian | ~10-15% |
| **Neither** | Verb-prominent | Some Philippine languages | <5% |

**Biblical languages**: Greek (subject-prominent), Hebrew (mixed). `{plan-topic-vs-subject}`

### Translation Impact

`{tbta-features}` Lists as Tier A Essential for: Japanese, Korean, Chinese, Tagalog

`{plan-readme}` Without Topic NP annotation, translators face:
- Wrong particle selection (Japanese wa vs ga, Korean eun/neun vs i/ga)
- Incorrect word order in topic-prominent languages
- Misaligned voice systems (Tagalog agent vs patient voice)
- Unnatural or ungrammatical translations

### Schema Location

`{plan-readme}` **Category 105 (Clauses), Position 4**. Applies to complete clauses only, not words or phrases.

---

## 2. Value Inventory

### Official Values

`{tbta-features}` "Topic NP | Agent-like, Patient-like | Japanese, Korean, Chinese, Tagalog"

`{plan-readme}` Complete enumeration:

| Code | Value | Meaning | Frequency | Data Label |
|------|-------|---------|-----------|------------|
| **A** | Agent-like Topic | Topic with agent-like semantic role | ~15-20% | "Most Agent-like" |
| **P** | Patient-like Topic | Topic with patient-like semantic role | ~10-15% | "Most Patient-like" |
| **N** | No Topic | Subject-predicate structure | ~70% | Field absent |

### Empirical Data

`{tbta-samples}` Analysis of 18 sample JSON files:
- "Most Agent-like": 126 instances (majority)
- "Most Patient-like": 2 instances (genesis_001_009.json, genesis_002_001.json)
- Field appears at Clause level alongside Illocutionary Force, Discourse Genre, Salience Band

**Example structure** (genesis_001_009.json):
```json
{
  "Part": "Clause",
  "Type": "Independent",
  "Illocutionary Force": "Declarative",
  "Topic NP": "Most Agent-like",
  "Discourse Genre": "Climactic Narrative Story"
}
```

### Frequency by Genre

`{plan-readme}` Expected distribution:

| Genre | Topic Marking Rate | Pattern |
|-------|-------------------|---------|
| Narrative (Gospels, Acts) | ~35% | Topic continuity |
| Epistles (Teaching) | ~25% | Subject-predicate |
| Prophetic/Poetry | ~40% | Contrastive topic-fronting |
| Legal (Leviticus) | ~15% | Generic/impersonal |

### Discrepancy Note

`{plan-readme}` describes three values (A/P/N) with N for "No explicit topic," but `{tbta-samples}` shows only clauses WITH topics are annotated. Clauses without topics have no "Topic NP" field rather than "N" value.

---

## 3. Gateway Features & Constraints

### Controlling Feature

**Gateway**: Part = "Clause" (Category 105). `{tbta-data-structure}`

**Valid when**:
- Part = Clause
- Clause has overt noun phrase
- Information structure supports topic-comment analysis

**Not applicable**:
- Phrase or word level
- Presentational/existential constructions
- Weather constructions
- Imperatives with no overt topic

### Strong Correlations

`{plan-readme}` Gateway feature analysis:

| If Feature X = Value | Then Topic NP | Confidence |
|---------------------|---------------|------------|
| Participant Tracking = Restaging | = A or P | 70% |
| Semantic Role = A + Sentence-initial | = A | 80% |
| Surface Realization = Zero + Previous Topic | = (continued) | 75% |
| Salience Band = Foreground | More likely topic | 60% |

**Inverse correlations**:
- Indefinite NP → UNLIKELY topic (5%)
- First Mention → LESS likely topic (15%)

### Relationship to Semantic Role

**Distinction**: `{plan-readme}`
- **Semantic Role** (NP-level): Grammatical/thematic role (Agent, Patient, Source, etc.)
- **Topic NP** (Clause-level): Discourse role (what clause is "about")

**Borrowing**: Topic NP values (A/P) borrowed from Semantic Role terminology. This is a simplification - topics can have ANY semantic role (location, time, instrument), but TBTA only encodes A/P. `{plan-topic-vs-subject}`

---

## 4. TBTA Labeling Policy

### Semantic vs Morphological Priority

**Policy**: Prioritizes **discourse function over morphological form**. `{plan-readme}` Topic NP is discourse-pragmatic, not morphological.

### Assignment Criteria

`{plan-readme}` **Mark as A (Agent-like)**:
- Restaging participant who is agent/subject
- Contrastive topic in agent role
- Generic statements ("Lions hunt")
- Continuing topic from previous discourse

**Mark as P (Patient-like)**:
- Fronted patient/object ("Stone, builders rejected")
- Predicate constructions ("Blessed are the poor")
- Experiencers as topic
- Passive constructions

**Mark as N (No topic)**:
- New information (presentational)
- Subject-predicate dominant
- Weather/existential constructions

### Information Structure

`{plan-topic-vs-subject}` Lambrecht (1994) principles:

| | Given Information | New Information |
|---|------------------|------------------|
| **Typical topic?** | YES | NO |
| **Definiteness** | DEFINITE/generic | Can be indefinite |
| **Discourse role** | Frame-setting | Focus, informative |

**Strategy**: Given info (Participant Tracking = Routine/Restaging) → likely Topic. New info (First Mention) → unlikely Topic.

### Part-of-Speech Rules

**Not explicitly documented** in reviewed files. Topic NP is clause-level, not word-level, so no POS-specific rules needed.

---

## 5. Edge Cases & Special Patterns

### Topic Continuity + Pro-drop

`{plan-readme}` When same participant is topic across 3+ clauses, pro-drop languages use zero anaphora.

**Interaction**: Topic NP = A/P + Surface Realization = Zero → Continued topic, dropped pronoun

**Example**: John 8:12
```
TBTA: Topic NP = A (Jesus) + Surface Realization = Zero
Japanese: "(∅)また彼らに語られた" (topic continues, zero anaphora)
```

### Contrastive Topics

`{plan-readme}` Contrastive topics marked even when new to discourse.

**Example**: John 3:11 "We speak... but you [don't receive]"
- TBTA: Topic NP = A for both "we" and "you" (contrastive agents)
- Japanese: 私たちは...あなたがたは (both wa particles)

### Patient Topics (Topic ≠ Subject)

`{plan-topic-vs-subject}` **Psalm 118:22**:
```
Hebrew: אֶבֶן מָאֲסוּ הַבּוֹנִים (Stone builders-rejected)
Japanese: 建てる者たちが捨てた石は
         Tateru mono-tachi-GA suteta ishi-WA
         Builders-SUBJ rejected stone-TOPIC

Analysis:
- Stone = topic (wa), Patient of "reject"
- Builders = subject (ga), Agent of "reject"
- TBTA: Topic NP = P
```

### Predicative Topics

`{plan-readme}` **Matthew 5:3**: "Blessed are the poor in spirit"
- Poor = topic (wa in Japanese), Patient/Experiencer of "blessed"
- TBTA: Topic NP = P

### Non-A/P Topics (Limitation)

`{plan-topic-vs-subject}` TBTA only encodes A/P, missing:
- Location topics: "As for this room..." (room = location)
- Time topics: "Tomorrow..." (tomorrow = time)
- Instrument topics: "As for this hammer..." (hammer = instrument)

**TBTA handling**: Not documented. Likely coded as N or not annotated.

### Indefinite Topics

`{plan-readme}` Rare (5% inverse correlation). Topics typically DEFINITE/generic, not indefinite.

**Exceptions**: Generic indefinites ("A lion hunts"), conditional topics ("If a man says..."). Handling not documented.

---

## 6. Past Learnings

### Terminology Borrowing

`{tbta-samples}` Values "Most Agent-like" and "Most Patient-like" mirror Semantic Role feature values. `{tbta-data-structure}`

**Inference**: TBTA borrowed A/P from Semantic Role to classify topics. Pragmatic but loses information about non-A/P topics.

### Li & Thompson (1976) Typology

`{plan-topic-vs-subject}` **"Subject and Topic: A New Typology of Language"**

**Contribution**: Identified topic-prominence as distinct type. TBTA applies this to Bible translation, recognizing ~25-30% of languages are topic-prominent.

### Lambrecht (1994) Information Structure

`{plan-topic-vs-subject}` **"Information Structure and Sentence Form"**

**Contribution**: Topic is PRAGMATIC, subject is GRAMMATICAL. TBTA integrates this by encoding pragmatic topic distinct from grammatical subject.

---

## 7. Mixed Annotations

### Multiple Topics

**Not supported**. `{tbta-samples}` shows single "Topic NP" field per clause.

**Linguistic reality**: Some languages allow double-topic (Mandarin, Japanese contrastive). TBTA would encode only primary topic.

### Topic Shift Within Verse

`{plan-topic-vs-subject}` **John 1:1**: Topic changes between clauses.
```
Clause 1: "In beginning was the Word" → Topic NP = N (Word is NEW)
Clause 2: "and the Word was with God" → Topic NP = A (Word now GIVEN)
```

**Approach**: Each clause has independent Topic NP. No consistency constraint.

### Ambiguous Cases

**Not documented**: Guidelines for ambiguous topic assignment (multiple potential topics, embedded clauses, coordinate structures).

---

## 8. Cross-Feature Integration

`{plan-readme}` Related features:

1. **Participant Tracking**: Restaging → often Topic
2. **Surface Realization**: Topic continuity → zero allowed
3. **Semantic Role**: Topic inherits A/P designation
4. **Salience Band**: Foreground → more topic marking

**Hierarchical dependency**:
```
Clause (Topic NP = A)
├── NP (Semantic Role = Most Agent-like)
│   └── Noun (Participant Tracking = Restaging, Surface = Noun)
```

---

## 9. Documentation Gaps

1. **Encoding position**: `{plan-readme}` claims Position 4 in Category 105, but not confirmed in official TBTA docs
2. **"N" value**: Unclear if "no topic" = explicit "N" or field absence
3. **Ambiguity resolution**: No guidelines documented
4. **Non-A/P topics**: Handling not specified
5. **Embedded clauses**: Independent Topic NP annotation unclear
6. **Frequency validation**: Estimates not validated against full corpus

**Uncertainties marked "Not listed"**:
- Exact character position (claimed but unconfirmed)
- Annotation decision algorithm
- Inter-annotator agreement statistics
- Full corpus coverage statistics

---

## 10. Validation Strategy

`{plan-readme}` Compare with topic-prominent language translations:

**Japanese**: TBTA A/P → wa particle; TBTA N → ga particle
**Korean**: TBTA A/P → eun/neun; TBTA N → i/ga
**Mandarin**: TBTA A/P → sentence-initial or 的話; TBTA N → subject-predicate

**Expected accuracy**: 75-85% (discourse features challenging). Higher in narrative, lower in poetry.

---

## Summary

**Definition**: Clause-level feature identifying discourse topic (what clause is "about"), distinct from grammatical subject. `{tbta-features}`, `{plan-readme}`

**Values**: A (Agent-like ~15-20%), P (Patient-like ~10-15%), N (No topic ~70%, field absent). `{plan-readme}`, `{tbta-samples}`

**Critical for**: Japanese, Korean, Mandarin, Tagalog (~25-30% of world's languages are topic-prominent). `{tbta-readme}`, `{plan-topic-vs-subject}`

**Gateway features**: Participant Tracking (Restaging → Topic), Semantic Role (A/P inheritance), Surface Realization (Zero → continued topic), Salience Band. `{plan-readme}`

**Policy**: Discourse function over morphological form. Topics typically given/definite, not new/indefinite. `{plan-readme}`, `{plan-topic-vs-subject}`

**Edge cases**: Topic continuity + pro-drop, contrastive topics, patient topics (topic ≠ subject), predicative topics. `{plan-readme}`, `{plan-topic-vs-subject}`

**Limitations**: Only A/P (not location/time/instrument topics), no multi-topic, ambiguity guidelines missing. `{plan-topic-vs-subject}`

**Linguistic basis**: Li & Thompson (1976) topic-prominence typology, Lambrecht (1994) information structure, Chafe (1976) given/new. `{plan-topic-vs-subject}`
