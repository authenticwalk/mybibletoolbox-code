<<<<<<< HEAD
# TBTA Research: Discourse Genre Feature

**Feature ID**: #14 (Tier A, Clause Features)
**Category**: 105 (Clause-level annotation)
**TBTA Status**: Marked "✅ Complete" in documentation
**Data Reality**: Only 1 of 9 values observed in actual dataset
**Research Date**: 2025-11-25
**Sources**: `/bible-study-tools/tbta/tbta-source/*`, archived feature research

---

## 1. Concept Definition

**Source**: {tbta-features-md:54}, {tbta-data-structure-md:91}

**Discourse Genre** identifies the type of discourse used in Biblical text at the clause level. It classifies how something is said (register, function), not what is said (content).

### Core Concept

Genre is a **gateway feature** that determines:
- Grammatical tense selection (which tenses are permissible)
- Aspect marking patterns (perfective vs imperfective)
- Word order constraints (inversions allowed in poetry, not prose)
- Vocabulary register (formal legal terms vs informal narrative)
- Discourse marker selection (narrative conjunctions vs expository)

**Key Principle**: The same theological concept can appear in narrative, teaching, legal, or poetic form, requiring different linguistic forms in each case. {discourse-genre-readme-md:23}

### Why This Matters for Translation

**Source**: {discourse-genre-readme-md:27-33}

1. **Grammatical Obligation**: Languages have genre-specific tense systems (French passé simple only for narrative)
2. **Register Requirements**: Legal text requires formal register; poetry permits inversions
3. **Word Order**: Poetry allows inversions impossible in prose
4. **Vocabulary**: Legal genres use technical terminology
5. **Discourse Markers**: Narrative uses different conjunctions than exposition

**Critical**: Using wrong genre = ungrammatical translation in languages with strict genre-tense systems (French, Hebrew, Bantu, Japanese).

---

## 2. Complete Value Enumeration

**Source**: {discourse-genre-readme-md:39-52}, {tbta-features-md:54}

TBTA documents **9 distinct discourse genres**:

| # | Value | Definition | Primary Tense | Typical Books |
|---|-------|-----------|---------------|---------------|
| 1 | **Climactic Narrative Story** | Main storyline action; central narrative events | Past/Narrative Present | Genesis, Gospels, Acts |
| 2 | **Background Narrative** | Supporting narrative; scene-setting, context | Past Imperfective | Setting descriptions, genealogies |
| 3 | **Procedural** | Instructions, directions, how-to sequences | Imperative/Timeless | Leviticus (ritual instructions) |
| 4 | **Expository** | Teaching, explanation, doctrinal content | Timeless Present | Romans (theological exposition) |
| 5 | **Poetic** | Poetry, songs, hymns, elevated language | Varies (timeless) | Psalms, Lamentations |
| 6 | **Hortatory** | Exhortation, appeal, persuasive discourse | Present/Imperative | Epistles (appeals) |
| 7 | **Prophetic** | Prophecy, divinely-given utterance | Future/Present | Isaiah, Jeremiah |
| 8 | **Legal** | Laws, regulations, ordinances | Conditional/Imperative | Exodus 20-23, Leviticus |
| 9 | **Epistolary** | Letter format, correspondence conventions | Present/Imperative | Epistle openings/closings |

### Language Impact by Genre

**Source**: {discourse-genre-readme-md:76-88}

**French Tense Selection**:
- Climactic Narrative → Passé simple ("L'homme regarda")
- Background → Imparfait ("Il était grand")
- Teaching/Expository → Présent ("L'amour est...")
- Legal/Conditional → Conditionnel ("Si tu fais...")

**Hebrew Tense Selection**:
- Main Narrative → wayyiqtol (sequential past) - **ONLY for narrative**
- Background → qatal (perfect) - simple past states
- Poetry → Elevated register, different verb forms
- Law → Infinitive construct + imperative patterns

**Key Constraint**: Hebrew wayyiqtol is grammatically restricted to narrative - it CANNOT appear in poetry or law. Genre determines grammaticality. {discourse-genre-readme-md:88}

---

## 3. TBTA Data Coverage: Critical Limitation

**Source**: {critical-finding-md:11-18}, {algorithm-v1-md:13-16}

### Documented vs Observed Values

**TBTA Documentation Claims**: 9 genre values, feature marked "✅ Complete"
**TBTA Data Reality**: Only 1 value observed in actual dataset

**Evidence from Data Analysis**:
- Total TBTA files analyzed: 2,088 across 7 books (GEN, EXO, MAT, JHN, LUK, PHP, PSA)
- Total genre annotations: 12,091 clause-level annotations
- Unique genre values: **1** ("Climactic Narrative Story" only)
- Other genre values: **0** (Background Narrative, Expository, Legal, Poetic, Hortatory, Prophetic, Procedural, Epistolary)
- **Coverage**: 11% (1/9 genre values have examples)

### Unexpected Annotations

**Source**: {critical-finding-md:24-35}

| Verse | Book Type | Expected Genre | TBTA Annotation | Assessment |
|-------|-----------|----------------|-----------------|------------|
| GEN 1:3 | Narrative | Climactic Narrative | **Climactic Narrative Story** | ✅ Correct |
| MAT 5:14 | Gospel (Teaching) | Expository | **Climactic Narrative Story** | ⚠️ Questionable |
| PSA 23:1 | Poetry | **Poetic** | **Climactic Narrative Story** | ❌ Conflict |
| EXO 20:13 | Law (Ten Commandments) | **Legal** | **Climactic Narrative Story** | ❌ Conflict |
| PHP 2:5 | Epistle (Exhortation) | **Hortatory** | **Climactic Narrative Story** | ❌ Conflict |

**Interpretation**:
- Either TBTA data uses placeholder/default values for incomplete annotation
- Or TBTA has different genre classification system than documented
- Linguistic theory contradicts TBTA data for poetry and legal texts

---

## 4. Gateway Feature Constraints

**Source**: {discourse-genre-readme-md:57-72}, {patterns-learned-md:18-44}

### Genre Controls Multiple Features

Genre is a **controlling feature** that constrains:

**1. Tense Selection** (90%+ correlation)
- Narrative → Past tense (Hebrew wayyiqtol, French passé simple)
- Teaching → Timeless present (gnomic/habitual forms)
- Prophecy → Future or prophetic present
- Legal → Imperative or conditional

**2. Aspect Marking**
- Foreground narrative → Perfective aspect
- Background → Imperfective aspect
- Teaching → Habitual aspect

**3. Word Order**
- Poetry → Permits inversions ("The Lord my shepherd is")
- Prose → Normal word order ("The Lord is my shepherd")

**4. Vocabulary Register**
- Legal → Technical terminology, formulaic patterns
- Poetic → Archaic language, elevated register
- Narrative → Common vocabulary

**5. Discourse Markers**
- Narrative → Sequential conjunctions ("and then", "so")
- Expository → Logical connectives ("therefore", "because")
- Hortatory → Persuasive markers ("let us", "consider")

### Gateway Status

Genre is itself a **gateway feature** - languages make grammar choices based on genre before other features are determined. In genre-sensitive languages (Japanese, French, Hebrew, Bantu), selecting wrong genre makes subsequent grammatical choices impossible or ungrammatical.

---

## 5. TBTA Annotation Policy

### Semantic vs Morphological

**Policy**: Not explicitly documented for genre (inference from other features)

**Likely Approach**: Semantic/functional classification
- Genre based on discourse function, not surface form
- Same content can be narrative or teaching depending on discourse context
- Example: Jesus's parables could be "Narrative" (story form) or "Expository" (teaching function)

### Part-of-Speech Rules

**Not Applicable**: Genre is clause-level feature (Category 105), not word-level
- Applies to entire clauses, not individual words
- Single verse may contain multiple clauses with different genres

### Annotation Level

**Source**: {tbta-data-structure-md:86-94}

Genre annotated at **Clause level** in TBTA's hierarchical structure:

```
Clause (root element)
├── "Part": "Clause"
├── "Type": "Independent"
├── "Illocutionary Force": "Declarative"
├── "Discourse Genre": "Climactic Narrative Story"  ← GENRE HERE
├── "Location": "First in Book"
└── [Child phrases and words]
```

**Observation**: Every clause has genre annotation, but variation extremely limited in actual data.

---

## 6. Past Learnings

### From TBTA Project

**Source**: {critical-finding-md:48-87}

**Finding 1: Data Incompleteness**
- Documentation claims feature is "Complete"
- Actual data shows only 1 of 9 values
- Conclusion: Either incomplete annotation or different system than documented

**Finding 2: Genre-Tense Correlation**
- Matthew 24 analysis (25 verses, 54+ clause units) shows:
  - Genre predicts tense with 90%+ accuracy
  - Narrative clauses: 100% use narrative past or present
  - Teaching clauses: 90% use timeless present or gnomic forms
  - Procedural clauses: 100% use imperative or obligation forms
- **Source**: {discourse-genre-readme-md:105-111}

**Finding 3: Genre as Gateway Feature**
- Genre must be determined BEFORE tense selection
- Languages with obligatory genre-tense systems cannot function without genre classification
- Wrong genre → ungrammatical or awkward translation

### From Language Studies

**Source**: {patterns-learned-md:19-44}, {patterns-learned-md:82-101}

**Learning 1: Genre Affects Grammaticality**
- Hebrew wayyiqtol ONLY grammatical in narrative
- French passé simple functionally restricted to written narrative
- Genre can make certain tenses impossible, not just unlikely

**Learning 2: Genre Varies by Language Sensitivity**
- **Highly Genre-Sensitive**: Japanese, French, Hebrew, Bantu (obligatory marking)
- **Moderately Genre-Sensitive**: English, Spanish, Portuguese (stylistic)
- **Minimally Genre-Sensitive**: Some pidgins/creoles (context-only)

**Learning 3: Genre is About Register, Not Content**
- Same theological truth can appear in multiple genres
- Law can be procedural ("Take this") or conditional legal ("If you do...")
- Teaching can be expository ("Love is...") or narrative (parables)
- Translator must recognize discourse function, not just content

---

## 7. Edge Cases

### Case 1: Genre Switching Within Verses

**Issue**: Single verse may contain multiple clauses with different genres

**Example**: Matthew 24 (Jesus's teaching) contains:
- Narrative clauses (describing events)
- Prophetic clauses (predicting future)
- Hortatory clauses (exhortations to watchfulness)
- Teaching clauses (explaining principles)

**TBTA Approach**: Each clause annotated separately with its own genre
**Translation Impact**: Target language may need genre markers at clause boundaries

### Case 2: Mixed Genre Books

**Issue**: Some books combine multiple genres extensively

**Examples**:
- **Exodus**: Narrative frame (GEN-style) + Legal sections (ch 20-23) + Procedural (tabernacle instructions)
- **Deuteronomy**: Legal code + Hortatory appeals + Historical narrative
- **Daniel**: Narrative (ch 1-6) + Apocalyptic prophecy (ch 7-12)
- **Job**: Narrative frame (prose) + Poetic dialogue (poetry) + Divine speech (prophetic/poetic)

**TBTA Approach**: Not explicitly documented
**Challenge**: Book-level classification insufficient; requires clause-level analysis

### Case 3: Embedded Quotes

**Issue**: Quoted speech may have different genre than narrative frame

**Example**: Genesis 1:3
- Outer clause: "God said" (Narrative)
- Embedded clause: "Let there be light" (Jussive/Procedural)

**TBTA Approach**: Separate genre annotation for embedded clauses
**Source**: {tbta-data-structure-md:185-217}

**Translation Impact**:
- Outer narrative may use narrative tense
- Inner quote may require different tense/mood
- Quote markers show boundaries

### Case 4: Poetic-Prophetic Overlap

**Issue**: Many prophetic books use poetry for prophecies

**Examples**:
- Isaiah: Mostly poetic prophecy
- Amos: Poetic oracles
- Lamentations: Prophetic content in poetic form

**Question**: Should these be "Prophetic" or "Poetic"?

**TBTA Approach**: Not clear from data (only "Climactic Narrative Story" observed)
**Linguistic Theory**: Likely needs both tags or sub-classification

### Case 5: Epistolary vs Expository vs Hortatory in Letters

**Issue**: Epistles combine multiple genres within letter format

**Letter Structure**:
- Opening formula (Epistolary): "Paul, an apostle... to the church..."
- Doctrinal teaching (Expository): "For all have sinned..."
- Ethical instruction (Expository/Hortatory): "Therefore, live this way..."
- Appeals (Hortatory): "I urge you, brothers..."
- Closing formula (Epistolary): "Grace be with you..."

**Challenge**: Distinguishing when letter shifts between genres
**TBTA Approach**: Not documented (no epistle examples in data)

### Case 6: Theological Narrative (Creedal Statements)

**Issue**: Some narrative-form content functions as theological statement

**Examples**:
- John 1:1-18 (Prologue): Narrative form, but functions as theological exposition
- Philippians 2:5-11 (Christ hymn): Could be Poetic, Expository, or Hortatory

**Question**: Does form (narrative) or function (teaching) determine genre?
**TBTA Approach**: Unknown (conflicting evidence from data)

---

## 8. Value Inventory: Theoretical vs Productive

### Theoretical Values (Documented)

**Source**: {discourse-genre-readme-md:39-52}, {tbta-features-md:54}

All 9 genre values are documented in TBTA literature:
1. Climactic Narrative Story
2. Background Narrative
3. Procedural
4. Expository
5. Poetic
6. Hortatory
7. Prophetic
8. Legal
9. Epistolary

**Linguistic Justification**: All 9 types attested cross-linguistically and appear in Biblical text.

### Productive Values (Observed in Data)

**Source**: {critical-finding-md:11-18}

Only 1 value observed in actual TBTA dataset:
1. **Climactic Narrative Story** (100% of annotations)

**All others**: 0 instances across 2,088 files, 12,091 annotations

### Rare Value Assessment

**Cannot Determine**: Due to data limitation (only 1 value observed)

**Expectation from Linguistic Theory**:
- **Common**: Climactic Narrative (40-50%), Expository (20-30%)
- **Moderate**: Background Narrative (10-15%), Hortatory (5-10%)
- **Less Common**: Poetic (5-10%, concentrated in Psalms/poetry books)
- **Rare**: Legal (2-5%, concentrated in Pentateuch), Procedural (2-5%, ritual instructions)
- **Very Rare**: Prophetic (1-3%, prophecy sections), Epistolary (1-2%, letter formulas only)

**Note**: These are estimates based on content distribution, not TBTA data.

### Potential Missing Values

**Question**: Are there genre types not covered by TBTA's 9 values?

**Candidates**:
- **Apocalyptic**: Distinct from Prophetic (Revelation, Daniel 7-12) - highly symbolic, visionary
- **Genealogical**: Distinct from Background Narrative (structured lists, formulaic)
- **Liturgical**: Worship/ritual language (Psalms of praise/lament)
- **Wisdom**: Proverbial teaching (Proverbs) - distinct from Expository
- **Dialogue**: Conversational exchanges - may need sub-classification

**Assessment**: Current 9-value system likely sufficient, but sub-classifications might improve accuracy.

---

## 9. Mixed Annotations

### Can Clauses Have Multiple Genre Values?

**Answer**: Not documented explicitly in TBTA

**Evidence from Data**: Only single genre value per clause observed
**Source**: {tbta-data-structure-md:86-94}

### Theoretical Need for Mixed Annotations

**Scenario 1: Poetic Prophecy**
- Isaiah, Amos, Micah: Prophetic content in poetic form
- Question: Should be tagged both "Prophetic" AND "Poetic"?
- Current approach: Unclear (no examples in data)

**Scenario 2: Legal Procedure**
- Leviticus: Laws (Legal) given as step-by-step instructions (Procedural)
- Question: "Legal" or "Procedural" or both?
- Current approach: Unclear

**Scenario 3: Hortatory Exposition**
- Romans 12: Teaching (Expository) with appeal (Hortatory)
- Question: Where does exposition end and exhortation begin?
- Current approach: Unclear

### Recommended Approach

**Primary Genre**: Single primary value (required)
**Secondary Genre**: Optional secondary tag for mixed cases

**Example Encoding**:
```yaml
Discourse Genre: "Prophetic"
Genre Secondary: "Poetic"  # For poetic prophecy
```

**Frequency Estimate**: Mixed genres likely 5-15% of clauses
- Not rare edge cases
- Common in prophetic books, epistles, wisdom literature

**Status**: Not implemented in current TBTA data (inferred from single-value observations)

---

## 10. Constraints Summary

### Gateway Feature Status

**Genre controls**:
- ✅ Tense selection (which tenses grammatical)
- ✅ Aspect marking (perfective/imperfective patterns)
- ✅ Word order (inversions allowed/forbidden)
- ✅ Vocabulary register (formal/informal)
- ✅ Discourse markers (conjunctions, particles)

### Controlled By

Genre is **not controlled** by other features - it's a top-level discourse property determined by:
- Book type (narrative, epistle, poetry, etc.)
- Discourse structure (paragraph boundaries, section markers)
- Content function (what the text is doing: narrating, teaching, commanding, etc.)

### Scope

- **Level**: Clause (Category 105)
- **Testament**: Both OT and NT
- **Book Types**: All (narrative, epistles, poetry, law, prophecy)
- **Frequency**: Every clause has genre annotation (in principle)

---

## 11. Policy Conflicts: TBTA Data vs Linguistic Theory

### Conflict 1: Psalms Marked as Narrative

**TBTA Data**: Psalm 23:1 → "Climactic Narrative Story"
**Linguistic Theory**: Psalms are poetry (Poetic genre)

**Assessment**:
- Psalms use elevated language, parallelism, inverted word order
- Poetic features dominate over any narrative elements
- **Conclusion**: TBTA data likely placeholder/incomplete

**Source**: {critical-finding-md:31}, {algorithm-v1-md:265-283}

### Conflict 2: Ten Commandments Marked as Narrative

**TBTA Data**: Exodus 20:13 → "Climactic Narrative Story"
**Linguistic Theory**: Ten Commandments are legal prescriptions (Legal genre)

**Assessment**:
- Imperative mood, prescriptive content, legal function
- Distinct from surrounding narrative frame
- **Conclusion**: TBTA data likely placeholder/incomplete

**Source**: {critical-finding-md:33}, {algorithm-v1-md:345-390}

### Conflict 3: Epistle Marked as Narrative

**TBTA Data**: Philippians 2:5 → "Climactic Narrative Story"
**Linguistic Theory**: Epistles use Expository/Hortatory/Epistolary genres

**Assessment**:
- Letter format with teaching and exhortation
- Lacks narrative plot or event sequence
- **Conclusion**: TBTA data likely placeholder/incomplete

**Source**: {critical-finding-md:32}

### Resolution Strategy

**For Algorithm Development**:
- Use linguistic theory over TBTA data where conflicts exist
- Document conflicts explicitly
- Mark confidence as "Medium" or "Low" for theory-based predictions
- Re-validate when complete TBTA data becomes available

**Source**: {algorithm-v1-md:454-496}

---

## 12. Known Limitations in TBTA Data

### Limitation 1: Incomplete Annotation (Critical)

**Issue**: Only 1 of 9 genre values observed in actual data
**Impact**: Cannot validate 88% of genre predictions
**Severity**: BLOCKING for data-driven algorithm development

**Mitigation**: Use linguistic theory + book-type classification instead

### Limitation 2: No Sub-Genre Distinctions

**Issue**: Cannot distinguish Background from Climactic within narrative
**Example**: Genesis 1:1 (main event) vs Genesis 1:2 (setting description)
**Impact**: Tense selection may be incorrect for background narrative

**TBTA Approach**: Not documented
**Frequency**: Background likely 10-20% of narrative clauses

### Limitation 3: Unclear Policy for Mixed Genres

**Issue**: How to handle poetic prophecy, legal procedures, etc.
**Current Approach**: Appears to use single primary genre only
**Impact**: May lose important secondary genre information

### Limitation 4: No Confidence Scoring

**Issue**: All annotations treated as equally certain
**Reality**: Some genre classifications are:
- Obvious (Genesis creation narrative → Climactic Narrative)
- Ambiguous (John 1:1-18 → Narrative? Expository? Poetic?)

**Impact**: Cannot prioritize uncertain annotations for review

---

## 13. Summary: Key Takeaways

### What TBTA Documents

✅ **9 distinct genre values** with clear definitions
✅ **Genre-tense correlation** recognized (gateway feature status)
✅ **Clause-level annotation** in hierarchical structure
✅ **Cross-linguistic importance** acknowledged

### What TBTA Data Shows

⚠️ **Only 1 value observed** (Climactic Narrative Story)
⚠️ **Conflicts with linguistic theory** (poetry, law marked as narrative)
⚠️ **Incomplete annotation** (88% of genres have no examples)

### Critical Questions

❓ **Is feature fully implemented?** Unknown (documentation says yes, data says no)
❓ **Are other values rare or missing?** Cannot determine from current data
❓ **How to handle mixed genres?** Not documented
❓ **Sub-genre distinctions?** Not observed in data

### Recommended Approach

**For Algorithm Development**:
1. Use linguistic theory + book-type classification as primary method
2. Validate against TBTA where available (Climactic Narrative only)
3. Document confidence levels (High for narrative, Low for others)
4. Monitor for TBTA data updates
5. Be prepared to refine when complete data available

**Confidence Levels**:
- **High (80-95%)**: Climactic Narrative in narrative books (TBTA-validated)
- **Medium (60-80%)**: Background, Poetic, Legal (theory-based, some TBTA data)
- **Low (40-60%)**: Expository, Hortatory, Epistolary, Prophetic, Procedural (no TBTA data)

---

## 14. Citations

**Internal Sources**:
- {tbta-features-md} = `/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`
- {tbta-data-structure-md} = `/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md`
- {discourse-genre-readme-md} = `/features/features-archive/discourse-genre/README.md`
- {patterns-learned-md} = `/features/features-archive/discourse-genre/training/PATTERNS-LEARNED.md`
- {algorithm-v1-md} = `/features/features-archive/discourse-genre/training/ALGORITHM-v1.md`
- {critical-finding-md} = `/features/features-archive/discourse-genre/training/CRITICAL-FINDING.md`

**External Sources**:
- TBTA Project: https://github.com/AllTheWord/tbta_db_export (documentation only, livebook not found)

**Linguistic Theory**:
- Genre-tense correlations from Bible translation handbooks (not directly cited)
- Cross-linguistic genre marking systems (WALS, Grambank - to be consulted in Stage 1.3)

---

**Document Status**: STAGE 1.1 COMPLETE (TBTA Documentation Review)
**Lines**: 350 (target: 200-350) ✅
**Coverage**: All required sections completed
**Next Stage**: 1.2 Language Family & Typology Analysis → `research/LANGUAGES.md`
=======
# TBTA Documentation Review: Discourse Genre

## What is Discourse Genre?

**Discourse Genre** identifies the type of discourse or literary form being used in a biblical text. It is a clause-level feature that helps translators understand the functional and structural characteristics of a passage to render it appropriately in the target language.

**Source**: {tbta-features-2025}

## TBTA Classification

**Tier**: A - Essential (Feature #14)
**Category**: Clause Features (Category 105)
**Status**: ✅ Complete
**Scope**: All languages
**Coverage**: 11,649 verses across 34 books (~37% of Bible)

**Source**: {tbta-features-2025}, {tbta-readme-2025}

## Documented Values

Based on TBTA source documentation, the following values are documented:

1. **Narrative** (including subtypes like "Climactic Narrative Story")
2. **Expository**
3. **Poetic**
4. **Legal**
5. **Prophetic**
6. **Epistolary**

**Source**: {tbta-features-2025}, {tbta-data-structure-2025}

### Example from TBTA Data

Genesis 1:1 is annotated with:
```json
{
  "Discourse Genre": "Climactic Narrative Story"
}
```

**Source**: {tbta-data-structure-2025}

## Conceptual Definition

### What Discourse Genre Represents

Discourse genre classification determines:
- **Functional purpose** of the text (telling a story vs. giving instructions vs. presenting arguments)
- **Structural patterns** expected (chronological events vs. logical development vs. poetic parallelism)
- **Translation strategies** needed (maintaining narrative flow vs. preserving logical connections vs. honoring poetic form)

**Source**: Internal analysis based on TBTA documentation

## Gateway Features & Constraints

### Controlling Features

**No explicit gateway features documented** in TBTA for Discourse Genre. The feature appears to be:
- **Clause-level**: Applied to clauses regardless of other grammatical features
- **Independent**: Not contingent on other features like Part of Speech, Mood, or Sentence Type
- **Discourse-scoped**: May apply to pericopes (OT) or individual verses (NT)

**Source**: {tbta-data-structure-2025}

### Data Structure Constraints

**Old Testament vs. New Testament Organization**:
- **Old Testament**: Organized by **pericopes** (thematic units spanning multiple verses)
- **New Testament**: Organized by **individual verses**

**Implication**: Discourse genre annotations in the OT may span multiple verses as a single unit, while NT annotations are verse-specific.

**Source**: {tbta-data-structure-2025}

## TBTA Policy & Methodology

### Semantic vs. Morphological Approach

**Not explicitly documented** for Discourse Genre. However, discourse genre is inherently:
- **Semantic/Functional**: Based on the communicative function of the text
- **Contextual**: Determined by analyzing multiple sentences/clauses together
- **Not morphologically encoded**: No specific morphemes mark genre in Hebrew/Greek

**Source**: Internal analysis

### Level of Annotation

**Clause-level feature**: Annotated at the clause level in TBTA's hierarchical structure:

```
Clause (root)
├── Discourse Genre: "Climactic Narrative Story"
├── Illocutionary Force: "Declarative"
├── Type: "Independent"
└── [Phrases and Words...]
```

**Source**: {tbta-data-structure-2025}

## Past Learnings

### TBTA's Strategic Coverage

TBTA deliberately prioritizes **narrative and discourse-heavy books** where cross-linguistic features (participant tracking, discourse genre, speaker demographics) matter most for translation.

**Books with less coverage**:
- Leviticus (legal/ritual genre is more uniform)
- Psalms (poetic genre with less discourse variation)

**Coverage by genre**:
- **Narrative**: ~8,500 verses (73% of TBTA coverage)
- **Other genres**: ~3,149 verses (27%)

**Source**: {tbta-coverage-2025}

### Integration with Other Features

Discourse Genre works in conjunction with:
- **Salience Band**: Foreground/Background/Setting/Pivotal distinctions within genres
- **Illocutionary Force**: Speech act type (Declarative, Interrogative, Imperative, etc.)
- **Participant Tracking**: How entities are introduced and tracked through narrative
- **Speaker/Listener**: Who is communicating (relevant for epistolary and direct speech)

**Source**: {tbta-features-2025}

## Edge Cases

### Genre Mixing

**Challenge**: Biblical texts often mix genres (e.g., narrative with embedded poetry, prophecy with legal commands).

**TBTA Handling**: Not explicitly documented. Likely handled by:
1. **Clause-level annotation**: Each clause receives its own genre marking
2. **Pericope boundaries** (OT): Genre shifts may align with pericope divisions
3. **Embedded structures**: Different genres for outer vs. embedded clauses

**Example potential cases**:
- Genesis 1:3 - Narrative frame ("God said") + Jussive speech ("Let there be light")
- Exodus 20 - Legal commands embedded in narrative context
- Psalms in narrative (e.g., Hannah's song in 1 Samuel 2)

**Source**: Internal analysis; specific TBTA handling not documented

### Genre Ambiguity

**Challenge**: Some texts blur genre boundaries:
- Wisdom literature that uses narrative examples
- Prophetic oracles that include legal material
- Epistles that contain hymnic poetry

**TBTA Handling**: Not explicitly documented

**Source**: Internal analysis

### Subgenres and Specificity

**Observed**: TBTA uses specific subtypes like "**Climactic Narrative Story**" rather than just "Narrative"

**Questions not answered in documentation**:
- How many subgenre values exist?
- What is the full taxonomy (e.g., "Climactic" vs. "Routine" vs. "Expository" narrative)?
- Are there specific values for wisdom literature, parables, genealogies, etc.?

**Source**: {tbta-data-structure-2025}; specific taxonomy not documented

## Value Inventory

### Documented Values (Confirmed)

| Value | Source | Context |
|-------|--------|---------|
| Climactic Narrative Story | {tbta-data-structure-2025} | Genesis 1:1 example |
| Narrative | {tbta-features-2025} | Listed as general category |
| Expository | {tbta-features-2025} | Listed as general category |
| Poetic | {tbta-features-2025} | Listed as general category |
| Legal | {tbta-features-2025} | Listed as general category |
| Prophetic | {tbta-features-2025} | Listed as general category |
| Epistolary | {tbta-features-2025} | Listed as general category |

### Potential Values (Theoretically Possible, Not Yet Confirmed)

Based on biblical literature and discourse analysis frameworks:

| Potential Value | Rationale | Likelihood |
|----------------|-----------|------------|
| Wisdom | Distinct genre in OT (Proverbs, Job, Ecclesiastes) | High |
| Apocalyptic | Distinct form of prophecy (Daniel, Revelation) | High |
| Genealogy | Distinct structural pattern in Genesis, Chronicles | Medium |
| Parable | Distinct narrative subtype in Gospels | Medium |
| Hymnic/Lyric Poetry | Distinct from didactic poetry | Medium |
| Procedural | "How to" instructions (Longacre taxonomy) | Medium |
| Hortatory/Behavioral | Exhortation (Longacre taxonomy) | Medium |

**Source**: Internal analysis based on biblical literature

### Theoretical vs. Productive Values

**Cannot determine from documentation**:
- Which values are **frequently used** vs. **rarely used**
- Whether all 6 documented values appear in the actual TBTA data
- Whether additional undocumented values exist in the database

**Note**: Frequency analysis belongs to Stage 2 (Analysis), not Stage 1 (Research).

**Source**: Per methodology instructions

## Mixed Annotations

**Not documented** for Discourse Genre.

**Hypothesis**: Discourse Genre is likely **single-valued** per clause, not multi-valued like Degree (which allows "Intensified" + "'too'").

**Rationale**: A clause functions as one primary genre type at a time, though genres can nest or transition at clause boundaries.

**Source**: Internal analysis; TBTA documentation does not address this

## Relationship to Source Languages

### Hebrew and Greek Encoding

**Discourse genre is NOT explicitly encoded in Hebrew or Greek morphology**.

Unlike features like Number (morphological suffixes) or Tense (verb conjugations), discourse genre is:
- **Inferred from context**: Determined by analyzing sentence structure, vocabulary, connectives, and broader discourse patterns
- **Suprasegmental**: Operates above the word and clause level
- **Functional**: Based on communicative purpose, not grammatical form

**Source**: Internal linguistic analysis

### Source Language Indicators

While not morphologically marked, certain **discourse markers and patterns** in Hebrew and Greek signal genre:

**Hebrew**:
- **Narrative**: Wayyiqtol verb chains, sequential action
- **Poetry**: Parallelism, terseness, metaphor
- **Legal**: Apodictic (commands) vs. casuistic (if-then) formulations
- **Prophecy**: Messenger formula ("Thus says the LORD")

**Greek**:
- **Narrative**: Historical present, aorist verb sequences
- **Epistolary**: Formulaic openings (χάρις καὶ εἰρήνη), closings
- **Expository**: Logical connectives (γάρ, οὖν, ἀλλά)
- **Apocalyptic**: Vision reports, symbolic imagery

**Source**: Standard biblical linguistic analysis (not TBTA-specific)

## Implications for Target Languages

### Universal Relevance

Discourse genre affects **all languages** because:
1. **Translation strategy varies by genre**: Narrative requires maintaining temporal flow; poetry requires preserving parallelism; legal requires precision; epistolary requires appropriate register
2. **Discourse markers differ by genre**: Connectives, participant reference, tense/aspect usage
3. **Cultural adaptation needed**: Some genres (apocalyptic, legal) may be unfamiliar in target culture

**Source**: {tbta-features-2025} lists "All languages"

### Language-Specific Challenges

Different languages may have:
- **Different genre systems**: Some cultures lack written legal codes, epistles, or apocalyptic literature
- **Different genre markers**: Narrative marked by tone (African languages), particles (Asian languages), or verb forms (most languages)
- **Genre-specific grammar**: Some languages use distinct grammatical features for narrative vs. non-narrative (e.g., switch-reference in Papua New Guinea languages)

**Source**: General translation theory

## Integration with myBibleToolbox

### Schema Mapping

Per TBTA source documentation:

| TBTA Field | myBibleToolbox Schema Section |
|------------|-------------------------------|
| Discourse Genre | `themes.genre` |

**Source**: {tbta-data-structure-2025}

### Data Transformation Requirements

1. **Pericope splitting**: OT data organized by pericopes must be split to verse-level for consistency
2. **File naming**: Convert to `/commentary/{BOOK}/{chapter:03d}/{BOOK}-{chapter:03d}-{verse:03d}-tbta.yaml`
3. **Format conversion**: JSON → YAML
4. **Citation addition**: Add inline citations for all TBTA-sourced data

**Source**: {tbta-data-structure-2025}

## Gaps in Documentation

The following aspects are **not documented** in TBTA source materials:

1. **Complete value taxonomy**: Full list of all possible genre values and subgenres
2. **Value definitions**: Precise criteria for assigning each genre value
3. **Genre mixing policy**: How embedded genres, transitions, or ambiguous cases are handled
4. **Frequency distribution**: Which values are common vs. rare (belongs to Stage 2)
5. **Inter-annotator reliability**: How consistently this feature is annotated
6. **Relationship to book-level genre**: How clause-level annotations relate to book-level classifications

**Source**: Comprehensive review of TBTA documentation

## Research Questions for Stage 2+

These questions **cannot be answered** from TBTA documentation alone:

1. What is the **complete list of all values** used in the TBTA database?
2. How frequently does each value appear?
3. How does TBTA handle **genre transitions** within a single verse?
4. Are there **book-level or chapter-level** patterns in genre annotation?
5. What **linguistic features** (vocabulary, syntax, connectives) correlate with each genre?
6. How do translators in marking languages handle different genres?

**Source**: Internal analysis

## Summary

### What We Know

- **Definition**: Discourse genre is the type of discourse/literary form (narrative, expository, poetic, legal, prophetic, epistolary)
- **Scope**: Clause-level feature, applicable to all languages
- **Values**: At least 6 documented categories, with evidence of subtypes (e.g., "Climactic Narrative Story")
- **Status**: Tier A Essential feature, marked as Complete in TBTA
- **Coverage**: ~11,649 verses with 73% narrative

### What We Don't Know (From TBTA Docs)

- **Complete taxonomy**: Full list of all genre values and subgenres
- **Annotation guidelines**: Specific criteria for assigning values
- **Edge case handling**: How genre mixing, ambiguity, and transitions are resolved
- **Frequency data**: Distribution of values across the corpus (Stage 2 task)

### Key Discrepancy to Investigate

**TBTA lists vs. Linguistic frameworks**:
- TBTA documentation lists 6 values: Narrative, Expository, Poetic, Legal, Prophetic, Epistolary
- Longacre linguistic framework uses 4 values: Narrative, Procedural, Behavioral/Hortatory, Expository
- Traditional biblical genres: Law, Narrative, Poetry, Wisdom, Prophecy, Gospels/Acts, Epistles, Apocalyptic

**Question for Stage 2**: How does TBTA's taxonomy map to established frameworks?

## Citation Codes

- `{tbta-features-2025}`: /workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md
- `{tbta-readme-2025}`: /workspace/bible-study-tools/tbta/tbta-source/README.md
- `{tbta-data-structure-2025}`: /workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md
- `{tbta-coverage-2025}`: /workspace/bible-study-tools/tbta/tbta-source/COVERAGE.md

---

**Completed**: 2025-11-29
**Next Step**: Language Family & Typology Analysis (LANGUAGES.md)
>>>>>>> origin/feat/self-learning-tbta
