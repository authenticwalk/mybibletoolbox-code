# Time Granularity - TBTA Documentation Review

**Feature**: Time Granularity (Tier A, Feature #8)
**Source**: TBTA (The Bible Translator's Assistant) original annotation system
**Research Date**: 2025-11-25
**Methodology**: STAGE-1-RESEARCH.md Section 1 (TBTA Documentation Review)

---

## 1. Concept Definition

### What is Time Granularity?

**From TBTA-FEATURES.md**:
> "**Time Granularity**: Immediate/Today/Yesterday/Remote/Discourse (20+ values)" {tbta-features}

**From DATA-STRUCTURE.md**:
> "TBTA distinguishes **20+ temporal categories**" in the Time field {data-structure}

**From TRANSLATION-EDGE-CASES.md**:
> "Time Granularity - Genesis Narratives: When exactly did this happen? Some languages **require** specific time distinctions that English handles with context alone." {translation-edge-cases}

**Conceptual Definition**:
Time Granularity refers to the **temporal remoteness** or **temporal distance** of an event from the discourse moment (time of speaking or reference point). It is distinct from:
- **Tense**: Morphological form (past/present/future)
- **Aspect**: Event structure (perfective/imperfective/habitual)
- **Temporal Distance**: How linguistically distant an event is from discourse moment

**Source Language Encoding**:
Not listed in reviewed TBTA documentation whether Hebrew/Greek explicitly encode this feature morphologically.

**Translation Impact** {translation-edge-cases}:
> "Genesis narratives describe events thousands of years ago. TBTA marks these as **'Historic Past'**, guiding Tagalog translators to use the remote past verb form rather than recent past."

---

## 2. Complete Value Inventory

### 2.1 Documented Values from TBTA Sources

**From GitHub TBTA Export** (via WebFetch 2025-11-25) {tbta-github}:

#### Past References (13 values)
| Code | Time Reference | Source |
|------|----------------|--------|
| `P` | Present | {tbta-github} |
| `D` | Immediate Past | {tbta-github} |
| `A` | Earlier Today | {tbta-github} |
| `a` | Yesterday | {tbta-github} |
| `b` | 2 Days Ago | {tbta-github} |
| `c` | 3 Days Ago | {tbta-github} |
| `d` | A Week Ago | {tbta-github} |
| `e` | A Month Ago | {tbta-github} |
| `f` | A Year Ago | {tbta-github} |
| `g` | During Speaker's Lifetime | {tbta-github} |
| `h` | Historic Past | {tbta-github} |
| `i` | Eternity Past | {tbta-github} |
| `q` | Unknown Past | {tbta-github} |

#### Future References (8 values)
| Code | Time Reference | Source |
|------|----------------|--------|
| `E` | Immediate Future | {tbta-github} |
| `F` | Later Today | {tbta-github} |
| `j` | Tomorrow | {tbta-github} |
| `k` | 2 Days from Now | {tbta-github} |
| `l` | 3 Days from Now | {tbta-github} |
| `m` | A Week from Now | {tbta-github} |
| `n` | A Month from Now | {tbta-github} |
| `o` | A Year from Now | {tbta-github} |
| `p` | Unknown Future | {tbta-github} |

#### Atemporal (2 values)
| Code | Time Reference | Source |
|------|----------------|--------|
| `r` | Discourse | {tbta-github} |
| `T` | Timeless | {tbta-github} |

**Total Documented Values**: 23 distinct codes

### 2.2 Discrepancy Between Sources

**TBTA-FEATURES.md** states: "20+ values" {tbta-features}

**DATA-STRUCTURE.md** states: "20+ temporal categories" {data-structure}

**GitHub export** documents: 23 distinct values {tbta-github}

**From DATA-STRUCTURE.md example table** {data-structure}:
```
| Code | Time Reference |
|------|----------------|
| P | Present |
| D | Immediate Past (today) |
| A | Earlier Today |
| a | Yesterday |
| b | Day Before Yesterday |
| c | 2-7 days ago |
| h | Remote Past (living memory) |
| i | Historic Past (beyond living memory) |
| E | Immediate Future |
| T | Timeless (gnomic) |
```

**Note**: DATA-STRUCTURE.md provides 10 examples but states "20+" exist {data-structure}. The GitHub export provides the complete 23-value list.

### 2.3 Value Interpretation Discrepancies

**Comparing DATA-STRUCTURE.md {data-structure} vs GitHub export {tbta-github}**:

| Code | DATA-STRUCTURE.md | GitHub Export | Status |
|------|-------------------|---------------|--------|
| `b` | Day Before Yesterday | 2 Days Ago | Consistent |
| `c` | 2-7 days ago | 3 Days Ago | **DISCREPANCY** |
| `h` | Remote Past (living memory) | Historic Past | **DISCREPANCY** |
| `i` | Historic Past (beyond living memory) | Eternity Past | **DISCREPANCY** |

**Conclusion**: Value semantics not fully standardized across TBTA documentation sources.

### 2.4 Rare Values

**From TRANSLATION-EDGE-CASES.md** {translation-edge-cases}:
```yaml
Time: "h"  # Historic Past (20+ time granularity options)
# Options include:
# D (immediate past), A (earlier today), a (yesterday),
# b (2 days ago), c (3 days ago), d (week ago), e (month ago),
# h (historic past), etc.
```

**Frequency Assessment**: Not listed in reviewed documentation. No frequency data provided for individual time granularity values.

**Theoretical vs Productive**: Not listed. Unknown which values are attested in TBTA corpus vs theoretically available.

---

## 3. Gateway Features and Constraints

### 3.1 Part-of-Speech Gateway

**From DATA-STRUCTURE.md** {data-structure}:
> "### Example: Verb Codes (9 positions)
>
> | Position | Feature | Example Values |
> |----------|---------|----------------|
> | 1 | Time | P (present), D (immediate past), h (historic past), E (immediate future) |"

**Gateway Constraint**: Time Granularity applies to **Verbs only** {data-structure}.

**Evidence**:
- Noun codes (10 positions) do NOT include Time field {data-structure}
- Adjective codes: Not listed
- Verb codes (9 positions) include Time at position 1 {data-structure}

### 3.2 Mood Gateway

**Not listed** in reviewed TBTA documentation.

**Hypothesis**: Time Granularity may be constrained by Mood (e.g., only Indicative), but this is not documented in:
- TBTA-FEATURES.md
- DATA-STRUCTURE.md
- TRANSLATION-EDGE-CASES.md
- CRITIQUE.md

### 3.3 Aspect Interaction

**From DATA-STRUCTURE.md** {data-structure}:
```json
{
  "Constituent": "create",
  "Part": "Verb",
  "Time": "Historic Past",
  "Aspect": "Inceptive",
  "Mood": "Indicative",
  "Polarity": "Affirmative"
}
```

**Observation**: Time and Aspect are separate, co-occurring features on verbs. No documented constraint that Aspect controls Time Granularity applicability.

### 3.4 Discourse Genre Interaction

**Not listed** as a gateway feature.

**Observation from TRANSLATION-EDGE-CASES.md** {translation-edge-cases}:
> "Similarly, in discourse sections where Jesus teaches timeless principles, TBTA can mark time as 'Discourse/Timeless', prompting use of generic present forms."

**Implication**: Discourse Genre may influence Time Granularity value selection but is not documented as a gateway constraint.

---

## 4. Annotation Policy

### 4.1 Semantic vs Morphological Priority

**Not listed** in reviewed TBTA documentation.

**What is documented**:
- Number feature has morphological vs semantic tension (Hebrew dual morphology marked as singular) {critique}
- Time Granularity policy: **No explicit statement** in reviewed documents

### 4.2 Source Language vs Target Language

**From TRANSLATION-EDGE-CASES.md** {translation-edge-cases}:
> "Genesis narratives describe events thousands of years ago. TBTA marks these as **'Historic Past'**..."

**Implication**: TBTA encodes semantic temporal distance (real-world time reference) not Greek/Hebrew morphological tense.

**Example** {translation-edge-cases}:
- Hebrew: Wayyiqtol (narrative past) - no temporal distance marking
- TBTA: "h" (Historic Past) - adds semantic temporal distance
- Target (Tagalog): Remote past verb form

**Policy Inference**: TBTA prioritizes **semantic temporal remoteness** over source language morphology.

### 4.3 Discourse Perspective

**From TRANSLATION-EDGE-CASES.md** {translation-edge-cases}:
> "**r** = Discourse" {tbta-github}

**Question**: Is temporal distance calculated from:
1. Modern reader's perspective (2025 CE)?
2. Original audience perspective (1st century CE for NT)?
3. Discourse-internal perspective (story time)?

**Answer**: Not listed in reviewed documentation.

**Example ambiguity**:
- Genesis 1:1 from modern perspective: ~6000 years ago
- Genesis 1:1 from original audience: Already ancient
- Genesis 1:1 discourse-internal: "In the beginning"

TBTA likely uses **original audience perspective** (Genesis = historic past for ancient readers), but this is not explicitly documented.

---

## 5. Past Learnings and Known Issues

### 5.1 Verb TAM Annotation Issues

**From CRITIQUE.md** {critique}:
> "### 2.2 Overgeneralization of 'Unmarked' Aspect
>
> **Issue**: All tested verbs coded as 'Unmarked' aspect despite clear semantic distinctions."

**Impact on Time Granularity**: Aspect and Time interact. If Aspect is overgeneralized to "Unmarked," Time Granularity predictions may compensate or be affected.

**Example** {critique}:
```yaml
Matthew 5:6 - χορτασθήσονται (chortasthēsontai, "will be filled")
Verb Class: Accomplishment (telic - has completion point)
Context: Hunger → Satisfaction (clear endpoint)
TBTA Aspect: Unmarked  ← Too coarse
Expected: Completive (based on Aktionsart + morphology)
```

**Relevant to Time Granularity**: Future tense verb but temporal distance not mentioned in critique. Likely coded as `p` (Unknown Future) or specific future granularity.

### 5.2 No Aktionsart Classification

**From CRITIQUE.md** {critique}:
> "### 4.2 No Aktionsart Classification
>
> **Issue**: TBTA has no systematic verb lexical aspect (Aktionsart) database."

**Impact**: Verb lexical class (State/Activity/Accomplishment/Achievement) affects temporal interpretation but is not systematically integrated with Time Granularity.

### 5.3 Greek Imperatives Marked as Indicative

**From CRITIQUE.md** {critique}:
> "### 2.1 Greek Imperatives Marked as 'Indicative'
>
> **Issue**: Morphological imperative mood coded as semantic 'Indicative' mood."

**Relevance to Time Granularity**: Imperatives typically reference immediate or near future. If Mood is misannotated, Time Granularity may also be affected.

**Example**: Matthew 5:44 "Love your enemies" (imperative)
- Expected Time: `E` (Immediate Future) or `T` (Timeless principle)
- Actual TBTA Time: Not listed in critique

### 5.4 Coverage Completeness

**From README.md** {tbta-readme}:
> "**Coverage**: 11,649 verses across 34 books (~37% of Bible)"

**From TBTA-FEATURES.md** {tbta-features}:
> "| 8 | **Time Granularity** | ... | ✅ Complete |"

**Interpretation**: "Complete" means fully annotated within the 11,649-verse corpus, not the entire Bible.

---

## 6. Edge Cases and Special Scenarios

### 6.1 Timeless vs Present

**Ambiguity**: When should TBTA use `T` (Timeless) vs `P` (Present)?

**Example 1** {translation-edge-cases}:
- John 14:6: "I am the way, truth, and life"
- Expected: `T` (Timeless) - eternal theological truth
- Not: `P` (Present) - momentary state

**Example 2**:
- "God is love" (1 John 4:8)
- Expected: `T` (Timeless) - God's eternal nature
- Not: `P` (Present) - current state that could change

**Policy**: Not explicitly documented in reviewed sources.

### 6.2 Discourse Time in Narrative

**From GitHub export** {tbta-github}:
> "`r` = Discourse"

**From TRANSLATION-EDGE-CASES.md** {translation-edge-cases}:
> "in discourse sections where Jesus teaches timeless principles, TBTA can mark time as 'Discourse/Timeless'"

**Ambiguity**:
- Is `r` (Discourse) used for narrative present (historical present)?
- Or is `r` used for discourse-internal temporal reference?
- How does `r` differ from `T` (Timeless) in discourse contexts?

**Answer**: Not listed in reviewed documentation.

### 6.3 Flashbacks and Anteriority

**Not listed** in reviewed TBTA documentation.

**Question**: How does TBTA encode pluperfect (past before past) or flashback sequences?

**Hypothesis**: May use more remote time code (e.g., flashback within recent narrative uses `h` historic past while narrative uses `D` immediate past).

**Evidence**: None found in reviewed documents.

### 6.4 Prophetic Future vs Eschatological Future

**From archived research** (features-archive/time-granularity/README.md):
> "| **L** | Eschatological Future | End times, Second Coming | 'Day of the Lord' |"

**Note**: This value (`L`) appears in archived research but NOT in GitHub export {tbta-github}.

**Discrepancy Status**: Archived research may have extrapolated beyond TBTA's actual implementation.

**Verified values for future** {tbta-github}:
- `E` through `o`: Specific temporal distances (immediate to year)
- `p`: Unknown Future

**Eschatological Future encoding**: Not listed in GitHub export or official TBTA docs.

### 6.5 Hebrew Narrative Sequence

**From TRANSLATION-EDGE-CASES.md** {translation-edge-cases}:
> "Genesis narratives describe events thousands of years ago. TBTA marks these as **'Historic Past'**"

**Specificity**: Does TBTA mark all Genesis 1 verbs uniformly as `h` or `i`?

**Example sequence**:
- Gen 1:1 "God created" - likely `h` or `i` (historic/eternity past)
- Gen 1:3 "God said" - same temporal frame, likely same code
- Gen 1:4 "God saw" - same temporal frame, likely same code

**Policy for narrative sequences**: Not listed. Unknown if TBTA maintains temporal consistency within pericope or varies by verb.

### 6.6 Mixed Time References in Single Clause

**Question**: Can a clause have multiple verbs with different Time Granularity values?

**Example**: "God said, 'Let there be light'" (Gen 1:3)
- Main verb: "said" (historic past)
- Embedded verb: "be" (jussive, immediate future within discourse?)

**Answer**: Not listed in reviewed documentation.

**Character-based encoding** {data-structure}: Each verb has its own character-encoded Time value, so theoretically yes.

---

## 7. Value Inventory Analysis

### 7.1 Complete List with Certainty Levels

| Code | Time Reference | Source | Certainty |
|------|----------------|--------|-----------|
| `P` | Present | {tbta-github} {data-structure} | ✅ Confirmed |
| `T` | Timeless | {tbta-github} {data-structure} | ✅ Confirmed |
| `D` | Immediate Past | {tbta-github} {data-structure} {translation-edge-cases} | ✅ Confirmed |
| `A` | Earlier Today | {tbta-github} {data-structure} | ✅ Confirmed |
| `a` | Yesterday | {tbta-github} {data-structure} {translation-edge-cases} | ✅ Confirmed |
| `b` | 2 Days Ago / Day Before Yesterday | {tbta-github} {data-structure} {translation-edge-cases} | ✅ Confirmed (slight wording variation) |
| `c` | 3 Days Ago / 2-7 days ago | {tbta-github} {data-structure} {translation-edge-cases} | ✅ Confirmed (semantic discrepancy) |
| `d` | A Week Ago / week ago | {tbta-github} {translation-edge-cases} | ✅ Confirmed |
| `e` | A Month Ago / month ago | {tbta-github} {translation-edge-cases} | ✅ Confirmed |
| `f` | A Year Ago | {tbta-github} | ✅ Confirmed |
| `g` | During Speaker's Lifetime | {tbta-github} | ✅ Confirmed |
| `h` | Historic Past / Remote Past (living memory) | {tbta-github} {data-structure} {translation-edge-cases} | ✅ Confirmed (semantic discrepancy) |
| `i` | Eternity Past / Historic Past (beyond living memory) | {tbta-github} {data-structure} | ✅ Confirmed (semantic discrepancy) |
| `q` | Unknown Past | {tbta-github} | ✅ Confirmed |
| `r` | Discourse | {tbta-github} | ✅ Confirmed |
| `E` | Immediate Future | {tbta-github} {data-structure} | ✅ Confirmed |
| `F` | Later Today | {tbta-github} | ✅ Confirmed |
| `j` | Tomorrow | {tbta-github} | ✅ Confirmed |
| `k` | 2 Days from Now | {tbta-github} | ✅ Confirmed |
| `l` | 3 Days from Now | {tbta-github} | ✅ Confirmed |
| `m` | A Week from Now | {tbta-github} | ✅ Confirmed |
| `n` | A Month from Now | {tbta-github} | ✅ Confirmed |
| `o` | A Year from Now | {tbta-github} | ✅ Confirmed |
| `p` | Unknown Future | {tbta-github} | ✅ Confirmed |

**Total**: 24 values (23 from GitHub + `T` confirmed in DATA-STRUCTURE)

**Missing from GitHub export but in DATA-STRUCTURE.md**: None identified beyond semantic interpretation differences.

**Missing from DATA-STRUCTURE.md but in GitHub export**: Codes `q`, `r`, `f`, `g`, `j`, `k`, `l`, `m`, `n`, `o`, `p` (13 values)

### 7.2 Theoretical Values Not Attested

**From archived research** (not official TBTA source):
- `G` = Tomorrow (conflicts with GitHub `j` = Tomorrow)
- `H` = Day After Tomorrow
- `I` = 2-7 Days Future
- `J` = Week to Month Future
- `K` = Remote Future
- `L` = Eschatological Future
- `M` = Discourse Time
- `N` = Flashback/Anteriority

**Status**: These appear in archived feature research but NOT in official TBTA GitHub export {tbta-github}. Likely **extrapolated** or **hypothesized** values not actually used by TBTA.

**Certainty**: ❌ Not confirmed in official TBTA sources.

---

## 8. Mixed Annotations

### 8.1 Can Verbs Have Multiple Time Values?

**Character encoding structure** {data-structure}:
- Time occupies position 1 in 9-position verb code
- Single character = single value
- **Conclusion**: No mixed annotations within single verb

### 8.2 Interaction with Other Features

**From DATA-STRUCTURE.md example** {data-structure}:
```yaml
verbs:
  - word: "bara" (created)
    time: "i"      # Historic Past
    aspect: "c"    # Completive
    mood: "I"      # Indicative
    polarity: "+"  # Affirmative
```

**Observation**: Time co-occurs with Aspect, Mood, Polarity but does not "mix" with them - each is independent dimension.

### 8.3 Proximity System Temporal Values

**From TRANSLATION-EDGE-CASES.md** {translation-edge-cases}:
```yaml
Proximity: "S"  # Near Speaker (John)
# Options: N (near both), S (near speaker), L (near listener),
#          R (remote visible), r (remote invisible),
#          T (temporally near), t (temporally remote)
```

**Observation**: Proximity system (Noun feature) includes temporal categories:
- `T` (temporally near)
- `t` (temporally remote)

**Question**: How does Proximity temporal marking interact with Verb Time Granularity?

**Answer**: Not listed. Proximity applies to Nouns/Demonstratives, Time Granularity applies to Verbs - likely independent but potentially correlated in discourse.

---

## 9. Data Structure and Character Position

### 9.1 Encoding Details

**From DATA-STRUCTURE.md** {data-structure}:
> "### Example: Verb Codes (9 positions)
>
> | Position | Feature | Example Values |
> |----------|---------|----------------|
> | 1 | Time | P (present), D (immediate past), h (historic past), E (immediate future) |"

**Encoding**: Time Granularity is encoded at **position 1** of the 9-character verb code.

**Storage**: Single character code (e.g., `h`, `i`, `P`, `T`)

### 9.2 Case Sensitivity

**Observation from value inventory**:
- Uppercase: `P`, `D`, `A`, `E`, `F`, `T` (6 values)
- Lowercase: `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, `i`, `j`, `k`, `l`, `m`, `n`, `o`, `p`, `q`, `r`, `t` (18 values)

**Pattern**:
- Uppercase often used for: Present (`P`), immediate past/future (`D`, `E`, `F`), timeless (`T`), earlier today (`A`)
- Lowercase often used for: Specific past distances (`a`-`i`), future distances (`j`-`o`), unknown (`p`, `q`), discourse (`r`)

**Policy**: Not explicitly documented. Case sensitivity appears meaningful but policy not stated.

---

## 10. Integration with TBTA System

### 10.1 Related Features

**Time Granularity (#8) interacts with** {tbta-features}:
- **Aspect (#9)**: Perfective/Imperfective
- **Mood (#10)**: Indicative/Imperative/Subjunctive
- **Discourse Genre (#14)**: Narrative/Expository/Poetic
- **Salience Band (#16)**: Foreground/Background

**From archived research**:
> "**Example Correlation**:
> - Historic Past (i) + Completive Aspect → Genesis 1 creation acts
> - Timeless (T) + Indicative Mood → Theological principles
> - Discourse Time (M) + Narrative Genre → Parables"

**Note**: Value `M` (Discourse Time) claimed in archived research does not appear in GitHub export {tbta-github}.

### 10.2 Tier Placement Rationale

**From TBTA-FEATURES.md** {tbta-features}:
> "### Tier A: Essential Features (19 Features)
>
> **Priority**: Highest - affects 1000+ languages, cannot be easily inferred from context"

**Time Granularity is Tier A** because {tbta-features}:
1. Affects 1000+ languages (estimated)
2. Cannot be inferred from source language morphology alone
3. Grammatically required in target languages
4. Critical for accurate temporal reference

**Example Languages** {tbta-features}:
> "| 8 | **Time Granularity** | ... | Tagalog, Yagua, Kiksht, ChiBemba | ✅ Complete |"

---

## 11. Summary of Findings

### 11.1 What is Well-Documented

✅ **Confirmed Information**:
1. Time Granularity has 23-24 distinct values {tbta-github}
2. Encoded as single character at position 1 of verb codes {data-structure}
3. Applies to Verbs only {data-structure}
4. Tier A (essential) feature {tbta-features}
5. Affects 150+ languages with grammatical temporal marking {translation-edge-cases}
6. Used in 11,649 verses across 34 books {tbta-readme}
7. Marks semantic temporal distance, not just morphological tense {translation-edge-cases}

### 11.2 What is Poorly Documented

❌ **Missing or Unclear**:
1. Gateway features (Mood constraint?) - Not listed
2. Semantic vs morphological policy - Not explicitly stated
3. Discourse perspective (modern/original/internal) - Not listed
4. Frequency distribution of values - Not listed
5. Rare vs common values - Not listed
6. Timeless (`T`) vs Present (`P`) decision rules - Not listed
7. Discourse (`r`) vs Timeless (`T`) distinction - Not listed
8. Flashback/anteriority encoding - Not listed
9. Prophetic future encoding - Not listed
10. Narrative sequence consistency policy - Not listed

### 11.3 Discrepancies Between Sources

⚠️ **Inconsistencies**:
1. **Value semantics**:
   - Code `h`: "Historic Past" {tbta-github} vs "Remote Past (living memory)" {data-structure}
   - Code `i`: "Eternity Past" {tbta-github} vs "Historic Past (beyond living memory)" {data-structure}
   - Code `c`: "3 Days Ago" {tbta-github} vs "2-7 days ago" {data-structure}

2. **Value count**:
   - "20+ values" {tbta-features} vs 23 confirmed values {tbta-github}

3. **Value inventory**:
   - DATA-STRUCTURE.md shows 10 example values {data-structure}
   - GitHub export shows 23 values {tbta-github}
   - 13 values missing from DATA-STRUCTURE.md examples

### 11.4 Past Learnings Relevant to Time Granularity

**From CRITIQUE.md** {critique}:
1. Aspect overgeneralized to "Unmarked" - affects Time interpretation
2. No Aktionsart classification - verb lexical class not integrated
3. Greek imperatives misannotated as Indicative - may affect Time values
4. No confidence scoring - cannot distinguish certain vs uncertain Time annotations

---

## 12. Citation Index

**Source Document Codes**:
- `{tbta-features}`: `/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`
- `{data-structure}`: `/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md`
- `{translation-edge-cases}`: `/bible-study-tools/tbta/tbta-source/TRANSLATION-EDGE-CASES.md`
- `{critique}`: `/bible-study-tools/tbta/tbta-source/CRITIQUE.md`
- `{tbta-readme}`: `/bible-study-tools/tbta/tbta-source/README.md`
- `{tbta-github}`: `https://github.com/AllTheWord/tbta_db_export` (accessed via WebFetch 2025-11-25)

**Total Source Documents Reviewed**: 6 authoritative TBTA sources

---

## 13. Recommendations for Next Research Stages

### For Stage 2 (Language Study)
1. Verify which of the 23 values are actually used in TBTA corpus (frequency analysis)
2. Identify which languages in translation database require which time distinctions
3. Resolve semantic discrepancies between sources (h vs i definitions)

### For Stage 3 (Scholarly Research)
1. Find linguistic literature on "graded tense" or "temporal remoteness" systems
2. Research Tagalog, Yagua, ChiBemba, Kiksht temporal systems in detail
3. Investigate discourse time vs timeless distinction in linguistic literature

### For Stage 4 (Testing)
1. Extract actual TBTA Time values from 11,649-verse corpus
2. Calculate frequency distribution (which values are rare?)
3. Identify edge cases (flashbacks, prophetic future, narrative present)
4. Test consistency within pericopes (do sequential verbs get same Time code?)

---

**Document Status**: TBTA Documentation Review Complete
**Lines**: 343
**Methodology**: STAGE-1-RESEARCH.md Section 1 (TBTA Documentation Review)
**Compliance**: All claims cited to source documents; unclear items marked "Not listed"
**Next Stage**: Stage 1 Section 2 (Language Family & Typology Analysis)
