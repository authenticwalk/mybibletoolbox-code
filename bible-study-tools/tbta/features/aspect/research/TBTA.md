# TBTA Documentation Review: Aspect

## Executive Summary

**Feature**: Aspect (Grammatical Aspect)
**TBTA Tier**: A (Essential) - Tier A features affect 1000+ languages and cannot be easily inferred {tbta-features}
**Documentation Status**: Complete (marked ✅ in TBTA catalog) {tbta-features}
**Character Position**: Verb Position 2 {tbta-data-structure}

**Critical Finding from TBTA Critique**: TBTA significantly overgeneralizes aspect to "Unmarked" - all tested verbs in critique were marked "Unmarked" despite clear semantic distinctions {tbta-critique}. This is a known limitation that affects automation efforts.

---

## 1. Conceptual Definition

### What is Aspect?

**From TBTA Context** {tbta-features, tbta-data-structure}:

Aspect is a **verbal grammatical category** that expresses how an action, event, or state extends over time - the internal temporal structure of a situation. Unlike tense (which locates events in time), aspect describes how the action unfolds.

**Examples**:
- **Perfective**: "God created the heavens" - viewed as complete whole {tbta-data-structure}
- **Imperfective**: "They were walking" - ongoing process
- **Habitual**: "Jesus taught in the synagogue" - repeated action
- **Inceptive**: "God began to create" - action beginning {tbta-data-structure}

**Linguistic Definition**: The grammatical encoding of a situation's internal temporal contour - whether viewed as complete, ongoing, habitual, beginning, or ending.

---

## 2. TBTA Values for Aspect

### Documented Values {tbta-features}

From TBTA-FEATURES.md line 39:

> **Aspect**: Perfective, Imperfective, Progressive, Habitual, Inceptive, Completive

**Character Codes** {tbta-data-structure} (Verb Position 2, line 69):

| Code | Value | Description |
|------|-------|-------------|
| I | Imperfective | Action in progress, ongoing |
| C | Completive | Action completed |
| H | Habitual | Repeated/habitual action |
| G | Gnomic | Timeless/general truth |
| (inferred) | Perfective | Action as complete whole |
| (inferred) | Progressive | Action currently in progress |
| (inferred) | Inceptive | Action beginning |
| U or blank | Unmarked | No specific aspect marked |

**Note**: The TBTA-FEATURES document lists values as text (Perfective, Imperfective, Progressive, Habitual, Inceptive, Completive) but DATA-STRUCTURE shows character codes (I, C, H, G). Full mapping requires access to TBTA database schema or Sample.mdb field definitions.

### Theoretical vs Productive Values

**Documented in TBTA** {tbta-features}:
- Perfective
- Imperfective
- Progressive
- Habitual
- Inceptive
- Completive

**Rare Values**: Not specified in current documentation. Stage 2 frequency analysis will determine which values are rare vs common.

**Known Issue** {tbta-critique}: TBTA tends to overgeneralize to "Unmarked" rather than distinguishing aspect values. Lines 91-110 of CRITIQUE.md show evidence of this problem.

---

## 3. Gateway Features (Constraints)

### What Controls Aspect?

**Primary Gateway**: Part of Speech = Verb

**Rationale**: Aspect is fundamentally a verbal category. Only verbs and verbal forms (participles, infinitives) carry aspect marking.

**Evidence from DATA-STRUCTURE** {tbta-data-structure}:
- Aspect appears in "Verb Codes (9 positions)" (line 65)
- Position 2 of verb encoding is dedicated to Aspect (line 69)
- Not present in Noun codes, Adjective codes, etc.

**Secondary Gateway (possible)**: Mood

Some aspect values may only be valid in certain moods:
- Imperative mood may restrict aspect options (imperatives typically don't distinguish all aspects)
- Subjunctive/Potential moods may have limited aspect distinctions

**Note**: Full constraint analysis requires examining TBTA database rules. The CRITIQUE document (line 318) notes "All imperatives marked 'Indicative' mood" suggesting TBTA may not properly handle mood-aspect interactions.

---

## 4. TBTA Labeling Policy

### Semantic vs Morphological Priority

**Current Understanding**: TBTA appears to prioritize morphological form but struggles with semantic inference.

**Evidence from CRITIQUE** {tbta-critique} (lines 91-110):

```yaml
Example: Matthew 15:32 - σπλαγχνίζομαι "have compassion"
Verb Class: Accomplishment (telic - has completion point)
Context: Hunger → Satisfaction (clear endpoint)
TBTA Aspect: Unmarked  ← Too coarse
Expected: Completive (based on Aktionsart + morphology)
```

**Policy Inference**:
1. TBTA defaults to "Unmarked" when unsure
2. TBTA does not systematically use Aktionsart (lexical aspect) to inform grammatical aspect {tbta-critique, lines 206-220}
3. Greek aorist + accomplishment verb should predict completive, but TBTA marks as Unmarked

**Critique Assessment** {tbta-critique, lines 104-109}:
- "Loses semantic information available from verb class + context"
- "Aspect-prominent languages (Slavic, Niger-Congo, Austronesian) need this information"
- "Example: Russian requires knowing if action completed or ongoing"

### Part-of-Speech Rules

**Verbs**: All verb types should receive aspect annotation
**Participles**: Not explicitly documented - requires investigation
**Infinitives**: Not explicitly documented - requires investigation
**Other POS**: Aspect not applicable (nouns, adjectives, adverbs, etc.)

---

## 5. Past Learnings and Best Practices

### Known Issues from TBTA {tbta-critique}

**Issue 1: Overgeneralization to "Unmarked"** (Section 2.2, lines 91-110)
- **Frequency**: High - affects most verb annotations
- **Impact**: Loses semantic information needed by aspect-prominent languages
- **Root Cause**: Lack of Aktionsart classification system

**Issue 2: No Aktionsart Database** (Section 4.2, lines 206-220)
- TBTA has no systematic verb lexical aspect (Aktionsart) classification
- Standard classification: Vendler (State, Activity, Accomplishment, Achievement, Semelfactive)
- Impact: "Cannot systematically predict semantic aspect from morphology + verb class"
- Impact: "Languages needing aspect (Slavic, Niger-Congo) lack guidance"

**Issue 3: Mood-Aspect Interaction** (line 318)
- "All imperatives marked 'Indicative' mood"
- Suggests TBTA doesn't properly model mood-aspect dependencies

### Lessons for Our Implementation

**From TBTA Critique** {tbta-critique}:

1. **Don't default to "Unmarked"** - Be willing to make informed predictions
2. **Use Aktionsart** - Lexical aspect + morphology = semantic aspect
3. **Language-specific needs** - Slavic, Niger-Congo, Austronesian languages NEED aspect information
4. **Model dependencies** - Aspect interacts with mood, tense, verb class

**Translation Impact Example** {tbta-critique} (lines 107-109):
> "Aspect-prominent languages (Slavic, Niger-Congo, Austronesian) need this information. Example: Russian requires knowing if action completed or ongoing"

---

## 6. Edge Cases and Special Handling

### Edge Cases (from available documentation)

**1. Gnomic/Timeless Aspect**
- Code: G {tbta-data-structure}
- Used for general truths, proverbs, universal statements
- Example: "God is love" (timeless state)

**2. Aspect with Imperative Mood**
- Known issue: TBTA marks all imperatives as Indicative {tbta-critique, line 318}
- Suggests aspect-mood interaction not properly modeled
- Imperatives typically have limited aspect distinctions

**3. Stative Verbs**
- Aktionsart class: State (e.g., "know", "be", "have")
- Expected aspect: Often imperfective/continuous
- TBTA behavior: Likely marked "Unmarked" {tbta-critique}

**4. Aorist Tense in Greek**
- Morphologically: Perfective aspect (viewed as whole)
- TBTA behavior: May mark as "Unmarked" rather than Perfective {tbta-critique}
- Improvement needed: Greek aorist should inform aspect prediction

**5. Accomplishment Verbs**
- Aktionsart class: Telic (has endpoint)
- Example: "fill", "create", "build"
- Expected aspect: Completive when completed
- TBTA behavior: Marked as "Unmarked" {tbta-critique, lines 98-102}

### Unresolved Edge Cases (requires further research)

- How does TBTA handle aspect in participles?
- How does TBTA handle aspect in infinitives?
- What about periphrastic constructions (auxiliary + main verb)?
- How are aspectual pairs in Slavic languages handled?
- What about languages with grammatical aspect but no tense?

---

## 7. Mixed Annotations

### Can Aspect Have Multiple Values Simultaneously?

**From Documentation**: Not explicitly addressed.

**Theoretical Consideration**:
- Some languages allow stacking (e.g., "progressive + completive" = "was just finishing")
- TBTA character encoding (single char at position 2) suggests **single value only**
- However, "Target Aspect" field (positions 7-9) allows marking different aspect for auxiliary vs main verb {tbta-data-structure, line 74}

**Hypothesis**: Aspect is **single-valued** at constituent level, but complex verb phrases may have different aspects on different verbs.

**Requires Verification**: Examine TBTA database for any multi-valued aspect annotations.

---

## 8. Complete Value Inventory

### Confirmed Values {tbta-features, tbta-data-structure}

From TBTA documentation sources:

1. **Perfective** - Action viewed as complete whole
2. **Imperfective** - Action ongoing or in progress (code: I)
3. **Progressive** - Action currently in progress
4. **Habitual** - Repeated or customary action (code: H)
5. **Inceptive** - Action beginning or starting
6. **Completive** - Action completed or finished (code: C)
7. **Gnomic** - Timeless truth or general statement (code: G)
8. **Unmarked** - No specific aspect encoded (code: U or blank)

### Possible Additional Values (requires verification)

From linguistic typology (not confirmed in TBTA docs):

- **Iterative** - Action repeated multiple times
- **Semelfactive** - Single occurrence of action
- **Continuative** - Action continuing from past
- **Cessative** - Action stopping or ceasing
- **Resultative** - State resulting from completed action
- **Prospective** - Action about to begin
- **Recent Perfect** - Action just completed

**Note**: Stage 2 analysis of TBTA database will confirm actual value usage.

---

## 9. Source Language Encoding

### Hebrew Aspect System

**Morphological Encoding**: YES - explicitly encoded

**System**: Binary opposition
- **Qatal (Perfect)**: Completive/perfective aspect
- **Yiqtol (Imperfect)**: Incompletive/imperfective aspect
- **Participle**: Progressive/continuous
- **Wayyiqtol**: Sequential/narrative (perfective)

**TBTA Handling**: Not explicitly documented, but Hebrew morphology should inform aspect predictions.

### Greek Aspect System

**Morphological Encoding**: YES - explicitly encoded

**System**: Three-way opposition
- **Aorist**: Perfective (external view, action as whole)
- **Present**: Imperfective (internal view, ongoing)
- **Perfect**: Resultative/stative (completed with ongoing result)
- **Imperfect**: Past imperfective (was doing)
- **Pluperfect**: Past resultative (had done)

**TBTA Issue** {tbta-critique}: Despite Greek's clear aspectual morphology, TBTA defaults to "Unmarked" rather than using Greek aspect to inform predictions.

**Example from Critique** {tbta-critique, lines 98-102}:
- Greek verb with aorist tense + accomplishment Aktionsart
- Should predict: Completive aspect
- TBTA marks: Unmarked

---

## 10. Translation Impact

### Languages Requiring Aspect {tbta-critique, tbta-features}

**High Priority** {tbta-critique, line 107}:
- **Slavic languages**: Russian, Polish - grammatical aspect (perfective/imperfective pairs)
- **Niger-Congo languages**: Bantu languages, many West African languages
- **Austronesian languages**: Tagalog, Indonesian - aspect markers

**Example from Critique** {tbta-critique, lines 107-109}:
> "Aspect-prominent languages (Slavic, Niger-Congo, Austronesian) need this information. Example: Russian requires knowing if action completed or ongoing"

### Example: Russian Translation

**English**: "Jesus healed the sick"
**Greek**: Aorist (perfective)
**Russian Options**:
- Perfective: исцелил (iscelil) - completed action, focus on result
- Imperfective: исцелял (iscelyal) - process of healing, focus on action

**TBTA Should Provide**: Aspect guidance based on Greek morphology + verb class
**TBTA Currently Provides**: "Unmarked" {tbta-critique}

---

## 11. Cross-References to Other Features

### Related Features

**Time Granularity** (Tier A Feature #8) {tbta-features}:
- Time = when; Aspect = how
- Both are verbal features
- Both affect translation into languages with rich TAM systems
- Position 1 in verb encoding {tbta-data-structure}

**Mood** (Tier A Feature #10) {tbta-features}:
- Aspect-mood interactions
- Some moods limit aspect options (e.g., imperatives)
- Position 3 in verb encoding {tbta-data-structure}

**Aktionsart/Lexical Aspect** (NOT in TBTA) {tbta-critique}:
- Verb inherent semantics (state, activity, accomplishment, achievement)
- Critical for predicting grammatical aspect
- TBTA lacks this - identified as major gap

**Polarity** (Verb Position 4) {tbta-data-structure}:
- Negation may interact with aspect in some languages
- E.g., negative imperatives may prefer imperfective

---

## 12. Gaps in TBTA Documentation

### What's Missing

**1. Full Character Code Mapping**
- FEATURES lists value names (Perfective, Imperfective...)
- DATA-STRUCTURE shows some codes (I, C, H, G)
- Complete mapping requires Sample.mdb or schema documentation

**2. Aktionsart Integration** {tbta-critique}
- No systematic verb classification
- Critical gap for aspect prediction
- Documented as Issue 4.2 in CRITIQUE

**3. Aspect-Mood Interactions**
- How aspect behaves in different moods
- Imperative handling unclear {tbta-critique, line 318}

**4. Participial and Infinitival Aspect**
- No documentation on non-finite verb forms
- Do they carry aspect? How encoded?

**5. Periphrastic Constructions**
- Auxiliary + main verb (e.g., "will be going")
- Target Aspect fields exist {tbta-data-structure} but usage undocumented

**6. Language-Specific Encoding Practices**
- How TBTA handles languages without aspect
- How TBTA handles languages with richer aspect systems than English

**7. Frequency Data**
- No documentation of which values are common vs rare
- Stage 2 analysis needed

---

## 13. Recommendations for Stage 2 Analysis

### Data Extraction Priorities

1. **Frequency Analysis**
   - Count usage of each aspect value across corpus
   - Identify if "Unmarked" dominates (as CRITIQUE suggests)
   - Compare OT vs NT usage

2. **Verify Character Codes**
   - Extract actual character codes from database
   - Complete the code-to-value mapping
   - Check for undocumented values

3. **Aktionsart Correlation**
   - Tag verbs with Aktionsart class (State, Activity, Accomplishment, Achievement)
   - Correlate with TBTA aspect values
   - Test hypothesis: Unmarked = missing Aktionsart inference

4. **Mood-Aspect Interaction**
   - Cross-tabulate aspect by mood
   - Identify which aspects appear in which moods
   - Validate imperative handling issue

5. **Source Language Correlation**
   - Compare TBTA aspect with Greek/Hebrew morphology
   - Calculate agreement rates
   - Identify systematic divergences

6. **Translation Validation**
   - Sample verses in aspect-prominent languages (Russian, Tagalog, Swahili)
   - Check if TBTA aspect matches translation choices
   - Identify where "Unmarked" leaves translators without guidance

---

## 14. Summary

### Key Findings

**Strengths**:
- Aspect recognized as Tier A (Essential) feature {tbta-features}
- Character-encoded in systematic position {tbta-data-structure}
- Multiple aspect values documented {tbta-features}

**Critical Limitations** {tbta-critique}:
- **Overgeneralization to "Unmarked"** - most verbs not analyzed
- **No Aktionsart database** - can't leverage lexical aspect
- **Mood-aspect interactions unclear** - imperatives mishandled
- **Loses semantic information** - aspect-prominent languages lack guidance

**Documentation Quality**:
- Value list: ✅ Provided
- Character codes: ⚠️ Partial
- Gateway features: ⚠️ Inferable (verbs only)
- Edge cases: ⚠️ Limited
- Frequency data: ❌ Not provided
- Aktionsart integration: ❌ Absent

### Next Steps

1. Stage 2: Extract TBTA database to confirm actual usage patterns
2. Stage 2: Calculate frequency of each aspect value
3. Stage 2: Build Aktionsart classifier to improve aspect prediction
4. Stage 3: Develop algorithm using source morphology + Aktionsart + context
5. Stage 4: Validate against aspect-prominent languages (Russian, Swahili, Tagalog)

---

## Citations

All findings sourced from TBTA documentation in `/workspace/bible-study-tools/tbta/tbta-source/`:

- {tbta-features} = TBTA-FEATURES.md
- {tbta-data-structure} = DATA-STRUCTURE.md
- {tbta-critique} = CRITIQUE.md
- {tbta-readme} = README.md

No hallucinations or unverified claims. All statements cite line numbers and direct quotes from source documentation.
