# TBTA Documentation Review: Time Granularity

**Feature Name**: Time Granularity
**TBTA Field**: Time (Position 1 in Verb codes)
**Category**: Verb Features (Tier A - Essential)
**Status**: ✅ Complete in TBTA
**Documentation Date**: 2025-11-29

## Sources

All information extracted from:
- {tbta-data-structure} - `/workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md`
- {tbta-features} - `/workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`
- {tbta-translation-edge-cases} - `/workspace/bible-study-tools/tbta/tbta-source/TRANSLATION-EDGE-CASES.md`
- {tbta-readme} - `/workspace/bible-study-tools/tbta/tbta-source/README.md`

## Conceptual Definition

**Time Granularity** captures the level of temporal precision and distance in references to time - ranging from immediate/present actions to remote historical events beyond living memory. Unlike simple tense systems (past/present/future), time granularity provides fine-grained distinctions critical for languages that grammatically encode temporal distance.

### Core Concept

Time granularity answers: "How far from now did this happen?" or "How precise is the temporal reference?" This is distinct from:
- **Aspect** (how the action unfolds - completive, progressive, etc.)
- **Mood** (speaker's attitude - indicative, subjunctive, etc.)
- **Simple Tense** (basic past/present/future)

## TBTA Values

TBTA encodes **20+ temporal categories** using single-character codes. {tbta-data-structure}

### Complete Value Inventory

Based on {tbta-data-structure}, the documented values include:

#### Present/Timeless
| Code | Value | Description |
|------|-------|-------------|
| P | Present | Current time |
| T | Timeless/Gnomic | Universal truths, timeless principles |

#### Past Time (Fine-grained distinctions)
| Code | Value | Description |
|------|-------|-------------|
| D | Immediate Past | Today, just happened |
| A | Earlier Today | Earlier same day |
| a | Yesterday | Previous day |
| b | Day Before Yesterday | 2 days ago |
| c | 2-7 Days Ago | Recent past week |
| d | Week Ago | (Documented in {tbta-translation-edge-cases}) |
| e | Month Ago | (Documented in {tbta-translation-edge-cases}) |
| h | Remote Past | Within living memory |
| i | Historic Past | Beyond living memory, ancient events |

#### Future Time
| Code | Value | Description |
|------|-------|-------------|
| E | Immediate Future | About to happen, near future |
| (others) | (Not listed in current docs) | Likely mirrors past granularity |

#### Discourse Time
| Code | Value | Description |
|------|-------|-------------|
| (code TBD) | Discourse/Timeless | Used in teaching contexts {tbta-translation-edge-cases} |

**Note**: The complete 20+ value inventory is confirmed in {tbta-features} and {tbta-translation-edge-cases}, but only a subset is explicitly documented with character codes in the DATA-STRUCTURE.md file reviewed. The full code inventory would need to be extracted from actual TBTA data exports.

### Theoretical vs Productive Values

- **Highly Productive**: P (Present), D (Immediate Past), i (Historic Past), T (Timeless) appear frequently in biblical narratives
- **Moderately Productive**: a (Yesterday), h (Remote Past), E (Immediate Future)
- **Rare but Documented**: b, c, d, e (specific day counts) - used in contexts with precise temporal references
- **Potential Gaps**: Future time distinctions beyond E are documented to exist but specific codes not found in reviewed documentation

## Gateway Features & Constraints

### Part of Speech Constraint

**Gateway Feature**: Part of Speech
**Rule**: Time Granularity is ONLY applicable to Verbs {tbta-data-structure}

- **Applies to**: All verb forms (main verbs, auxiliaries, participles when functioning verbally)
- **Does NOT apply to**: Nouns, adjectives, adverbs, adpositions, particles

This is a hard constraint - TBTA only encodes Time in the Verb code string (Position 1).

### Interaction with Related Features

Time Granularity is Position 1 in the 9-position Verb code string: {tbta-data-structure}

| Position | Feature | Relationship to Time |
|----------|---------|---------------------|
| 1 | **Time** | Primary feature (this) |
| 2 | Aspect | Orthogonal - both can be specified independently |
| 3 | Mood | Orthogonal - both can be specified independently |
| 4 | Polarity | Orthogonal - negation doesn't affect time |
| 5 | Reflexivity | Orthogonal - reflexive actions can occur at any time |
| 6 | Degree | Orthogonal - degree doesn't affect time |
| 7-9 | Target Features | For complex verb phrases, auxiliary verbs |

**No Dependencies**: Time Granularity can be specified regardless of Aspect, Mood, or other verb features. All combinations are valid.

## TBTA Encoding Policy

### Semantic Priority

**TBTA follows semantic/pragmatic reality over morphological form.**

#### Policy: Match Actual Temporal Distance

The time value should reflect the **real-world temporal distance** of the event being described, not merely the grammatical tense used in Greek/Hebrew.

**Example from {tbta-translation-edge-cases}**:

```yaml
# Genesis narratives (creation, patriarchs)
Time: "i"  # Historic Past - thousands of years ago
Rationale: Events described are ancient, beyond living memory

# Jesus' teaching (timeless principles)
Time: "T"  # Discourse/Timeless
Rationale: Principles are universal, not time-bound

# Gospel narratives (Jesus' ministry)
Time: "h" or "i"  # Remote/Historic Past
Rationale: ~2000 years ago, beyond any living witness
```

### Narrative vs Discourse Context

TBTA distinguishes between:

1. **Narrative Time**: When did the event actually occur?
   - Genesis creation → Historic Past (i)
   - Gospel events → Remote/Historic Past (h/i)
   - Acts events → Remote/Historic Past (h/i)

2. **Discourse Time**: Timeless teachings embedded in narrative
   - Sermon on the Mount → Timeless (T)
   - Proverbs → Timeless (T)
   - Doctrinal statements in epistles → Timeless (T)

### Historical Distance Calculation

**Question**: How does TBTA determine "historic past" vs "remote past"?

**Not explicitly documented** in reviewed materials, but examples suggest:
- **Historic Past (i)**: Events clearly beyond any living memory (creation, patriarchs, exodus, most biblical events)
- **Remote Past (h)**: Events within cultural memory but not immediate (possibly used for recent prophets in their context)
- **Immediate/Recent Past (D, A, a, b, c)**: Used for events in direct discourse when characters speak about recent events

**Example**: When a character in Genesis says "yesterday we did X", that would be marked as 'a' (Yesterday) even though Genesis overall is Historic Past, because it represents the character's temporal perspective.

## Past Learnings & Best Practices

### Evolution of Time Granularity in TBTA

**Not documented** - No change history or policy evolution notes found in reviewed documentation.

### Known Edge Cases

#### 1. Flashbacks and Embedded Narratives

**Challenge**: When a narrative embedded in another narrative has different temporal distance.

**Example**: Joseph recounting his dreams (Genesis 37)
- Outer narrative: Historic Past (i) - Joseph's life thousands of years ago
- Embedded narrative (the dream): Still Historic Past (i) - from narrator's perspective
- In direct discourse: Immediate Past (D) - "I had a dream (just now)"

**TBTA Approach**: Not explicitly documented, but likely follows speaker perspective in direct discourse.

#### 2. Prophetic Future

**Challenge**: Prophecies describing future events (from text's perspective) that are now past (from reader's perspective).

**Example**: Isaiah's prophecies about the Messiah
- From Isaiah's perspective: Future
- From Christian reader's perspective: Historic Past (fulfilled in Jesus)

**TBTA Approach**: Not explicitly documented. Likely encodes from the original text's perspective (Future), not reader's perspective.

#### 3. Timeless Present in Narrative

**Challenge**: Gnomic/universal statements embedded in historical narrative.

**Example**: "God is good" stated in a Psalm
- The statement itself: Timeless (T)
- The act of stating it: Historic Past (i)

**TBTA Approach**: {tbta-translation-edge-cases} confirms use of Discourse/Timeless marker for teaching contexts, suggesting the verb "is" would be marked Timeless (T).

#### 4. Immediacy in Direct Discourse

**Challenge**: Characters speaking about events that are immediate to them but ancient to us.

**Example**: "Today Pharaoh spoke to me" (Genesis 41:9)
- From character's perspective: Earlier Today (A)
- From reader's perspective: Historic Past (i)

**TBTA Approach**: Not explicitly documented, but precedent from edge cases suggests encoding follows speaker's perspective in direct discourse.

## Mixed Annotations

**Not applicable** to Time Granularity.

Time is a single-valued feature - each verb receives exactly ONE time value. {tbta-data-structure}

Mixed annotations are mentioned for features like Degree (which allows "Intensified" + "'too'"), but Time does not permit multiple simultaneous values.

## Translation Impact

### Languages Requiring Time Granularity

From {tbta-features}, example languages include:
- **Tagalog** (Austronesian, Philippines)
- **Yagua** (Peba-Yaguan, Peru)
- **Kiksht** (Chinookan, USA)
- **ChiBemba** (Bantu, Zambia)

### Real-World Translation Impact

**Example from {tbta-translation-edge-cases}**:

**Problem without TBTA**:
- Tagalog has grammatical distinctions for temporal distance
- Translator sees Greek aorist (simple past) in Genesis
- Must guess whether to use recent past or remote past verb form
- **Risk**: Inconsistency or incorrect temporal framing

**Solution with TBTA**:
- Genesis narratives marked as Historic Past (i)
- Tagalog translator consistently uses remote past forms
- Teaching passages marked as Timeless (T)
- Tagalog translator uses generic present forms for universal principles

**Impact**: Prevents temporal confusion, ensures appropriate verb forms for temporal distance.

### Critical Translation Decisions

Time granularity affects:

1. **Verb morphology**: Languages with time-distance marking on verbs
2. **Auxiliary selection**: Choice of helping verbs based on temporal distance
3. **Adverbial modification**: Whether temporal adverbs are needed or redundant
4. **Discourse coherence**: Maintaining consistent temporal framing throughout narratives
5. **Genre recognition**: Distinguishing timeless teaching from historical narrative

## Relationship to Source Languages

### Hebrew

**Time Granularity is NOT explicitly encoded in Hebrew morphology.**

Hebrew has:
- **Perfect** (completed action)
- **Imperfect** (incomplete action)
- **Participle** (ongoing action)
- **Infinitive** (non-finite forms)

**But NOT**:
- Grammatical markers for "yesterday" vs "last week" vs "ancient times"
- Required distinctions for temporal distance

**Implication**: TBTA Time values are **inferred from context**, not decoded from Hebrew morphology. Annotators must use discourse context, narrative setting, and semantic understanding.

### Greek

**Time Granularity is NOT explicitly encoded in Greek morphology.**

Greek has:
- **Present** tense
- **Imperfect** tense (past, ongoing)
- **Aorist** tense (past, simple/punctiliar)
- **Perfect** tense (completed with ongoing result)
- **Pluperfect** tense (past perfect)
- **Future** tense

**But NOT**:
- Grammatical distinctions for temporal distance beyond basic past/present/future
- Required markers for "immediate" vs "remote" vs "historic" past

**Implication**: Like Hebrew, Time Granularity values are **contextually inferred**, not morphologically determined. The Greek aorist can represent any past time distance - context determines whether it's immediate or historic.

## Value Inventory Summary

### Confirmed Values (from documentation)

**Present/Timeless**: P, T
**Past (day-level)**: D, A, a, b, c
**Past (extended)**: d, e, h, i
**Future**: E, (others undocumented)

**Total Documented**: ~13 distinct values
**Total Claimed**: 20+ values {tbta-features}

### Gap Analysis

**Missing from reviewed documentation**:
- Future time granularity beyond "Immediate Future" (E)
- Precise codes for "Discourse" time (mentioned in text but code not listed)
- Full temporal distance scale for future events
- Possible additional past distinctions (documented as "20+")

**Recommendation for Stage 2**: Extract complete value inventory from actual TBTA data exports at https://github.com/AllTheWord/tbta_db_export to discover all 20+ values and their character codes.

## Summary

### Key Findings

1. **Feature is Complete in TBTA**: Marked as ✅ Complete with 20+ values {tbta-features}
2. **Tier A Essential**: Affects 1000+ languages, cannot be easily inferred {tbta-readme}
3. **Verb-specific**: Only applies to verbs, Position 1 in verb code string {tbta-data-structure}
4. **Context-driven**: Values inferred from narrative context, not Greek/Hebrew morphology
5. **Semantic priority**: Encodes real temporal distance, not just grammatical tense
6. **No dependencies**: Orthogonal to Aspect, Mood, and other verb features

### Critical Gaps in Documentation

1. **Incomplete value inventory**: Only ~13 of 20+ values explicitly documented with codes
2. **No policy history**: No documentation of how encoding guidelines evolved
3. **Edge case handling**: Limited explicit guidance on flashbacks, prophecy, direct discourse temporal perspective
4. **Future granularity**: Future time distinctions largely undocumented

### Recommendations for Next Stages

**Stage 2 (Language Analysis)**:
- Focus on languages with grammatical time-distance systems (Austronesian, some Bantu, some Amazonian)
- Investigate how many distinctions each language makes (2-way? 5-way? 10-way?)
- Determine which biblical contexts most need time granularity annotation

**Stage 4 (Test Set)**:
- Sample verses with clear temporal distance markers in context
- Include mix of narrative (historic), direct discourse (immediate), and teaching (timeless)
- Extract actual TBTA data to discover all 20+ values in practice

**Stage 5 (Algorithm)**:
- Train on narrative framing, discourse genre, and temporal adverbs
- Distinguish character perspective (direct discourse) from narrator perspective
- Account for genre (narrative vs teaching vs prophecy)

---

**Documentation Review Complete**: 2025-11-29
**Reviewer**: AI System
**Confidence**: High (for documented values), Medium (for undocumented edge cases)
**Next Step**: Extract actual TBTA data for complete value inventory
