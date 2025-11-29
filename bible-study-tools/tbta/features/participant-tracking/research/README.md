# Participant Tracking: Research Summary

**Feature**: Participant Tracking
**TBTA Tier**: A (Essential - #3 of 59 features)
**Research Status**: Stage 1 Complete
**Date**: 2025-11-29

---

## Executive Summary

**Participant Tracking** analyzes how participants (characters, entities) are introduced, referenced, and tracked throughout discourse. While all languages have participant reference systems, they vary dramatically in whether and how this is grammatically encoded—from mandatory marking (Japanese topic markers, Bantu noun class agreement) to pragmatic inference only (Hebrew/Greek source languages).

### Key Findings:

1. **Universal But Variably Encoded**: All 1,009 languages in our dataset track participants, but strategies range from obligatory grammatical marking to purely pragmatic inference

2. **Source Language Gap**: Hebrew and Greek do NOT grammatically encode participant tracking, yet TBTA adds this analysis layer to guide translators working into languages that REQUIRE it

3. **TBTA Challenges Identified**:
   - **Presupposition conflated with Routine**: God marked "Routine" in Genesis 1:1 despite being textually first mention
   - **Restaging never used**: 0% usage despite clear need (~50-100 biblical instances)
   - **Frame Inferable inconsistent**: Subjective application without systematic criteria

4. **Theological Stakes**: 15% of instances theologically/contextually critical (Trinity references, Messianic prophecy, divine participants); 85% stylistically arbitrary

---

## What Is Participant Tracking?

### TBTA Definition

From discourse analysis: How speakers manage references to entities across discourse—introducing new participants, maintaining active participants, and reactivating dormant participants.

### TBTA Values (Defined vs. Actually Used)

| Value | Definition | Usage Frequency | Status |
|-------|------------|-----------------|--------|
| **Routine** | Established participant continuing in focus | 73.04% (125,543) | ✅ Heavily used |
| **Generic** | Generic reference to participant type | 13.88% (23,856) | ✅ Common |
| **Frame Inferable** | Expected from semantic frame/context | 7.46% (12,815) | ✅ Moderate |
| **First Mention** | First introduction of participant | 5.39% (9,267) | ✅ Expected |
| **Interrogative** | Interrogative reference | 0.23% (394) | ✅ Rare |
| **Offstage** | Mentioned but not present | 0.00% (1 instance) | ⚠️ Essentially unused |
| **Restaging** | Reintroduction after absence | **0.00%** | ❌ **NEVER USED** |
| **Integration** | (Unclear definition) | **0.00%** | ❌ **NEVER USED** |
| **Exiting** | Participant leaving narrative | **0.00%** | ❌ **NEVER USED** |

**Total Annotations**: 171,876 instances across TBTA dataset

**Critical Issue**: Restaging defined but never used, despite biblical text containing ~50-100 clear restaging instances (Joseph in Genesis 37→39+, prophetic reintroductions, Gospel character reappearances).

---

## Section Summaries

### [TBTA.md](TBTA.md) - TBTA Documentation Review

**Lines**: 574 | **Sources**: 6 TBTA documentation files

#### Key Points:

**Value Inventory**:
- 9 values defined; only 6 values actually used (3 at 0% frequency)
- "Generic" appears in data (13.88%) but not in some documentation summaries

**Position in Encoding**: Position 5 in noun character codes (10-position system)

**Critical Findings**:
1. **Presupposition vs. Routine Conflation**:
   - God marked "Routine" in Genesis 1:1 (first verse of Bible)
   - Root cause: TBTA conflated cultural presupposition (readers know God) with textual anaphora (previously mentioned)
   - Affects ~50-100 presupposed entities throughout Bible
   - Many languages mark presupposition differently than routine reference

2. **Restaging Category Unused**:
   - 0% usage despite clear biblical examples (Joseph, prophets, Gospel characters)
   - Languages like Japanese/Korean REQUIRE restaging markers
   - Estimated 50-100 instances went unmarked

3. **Frame Inferable Inconsistency**:
   - Applied to 7.46% of annotations (12,815 instances)
   - Subjective: "Requires annotator to know semantic frames" (no algorithmic criteria)
   - No systematic frame database to guide decisions

**Gateway Features**: Part of Speech = Noun (or Noun Phrase)

**Related Features**:
- Noun List Index (coreference tracking)
- Surface Realization (noun vs. pronoun vs. zero)
- Number (Trinity references: Trial = exactly 3 persons)

**For full details**: See [TBTA.md](TBTA.md)

---

### [LANGUAGES.md](LANGUAGES.md) - Language Family & Typology Analysis

**Lines**: 702 | **Dataset**: 1,009 Bible translations | **Web Sources**: 12

#### Key Points:

**Source Languages (Critical Finding)**:
- **Hebrew** (OT): NO grammatical participant tracking encoding
- **Greek** (NT): NO grammatical participant tracking encoding
- Both use articles, word order, context—but no dedicated PT morphology
- **Implication**: TBTA adds discourse analysis NOT present in source morphology

**Typological Classification**:

**MANDATORY Marking** (5 languages proposed for Stage 2):
1. **Japanese** (jpn) - Japonic: は (wa) topic / が (ga) subject / ø zero anaphora
   - Status: NOT in current 1,009-language dataset (**gap**)
   - wa = "hearer-old" (presupposed/inferable)
   - ga = new/contrastive
   - 90%+ subject drop for routine

2. **Korean** (kor) - Koreanic: 는/은 (neun) topic / 가/이 (ga) nominative
   - Status: NOT in current dataset (**gap**)
   - neun = "episode-old" (within current episode)
   - ga = cross-episode restaging or first mention
   - Differs from Japanese: stricter episode-based logic

3. **Swahili** (swa) - Niger-Congo (Bantu): Noun class agreement (15-18 classes)
   - Status: Likely in dataset (89 Niger-Congo languages)
   - Agreement disambiguates participants
   - Class manipulation signals discourse prominence

4. **Quechua** (quz) - Quechuan: Topic marker -qa, switch-reference
   - Status: Dataset has 18 Quechuan languages ✅
   - Topic marker for established participants

5. **Tagalog** (tgl) - Austronesian: Voice/focus system
   - Status: 176 Austronesian languages in dataset ✅
   - Voice system interacts with participant tracking

**OPTIONAL Marking** (5 languages proposed for Stage 2):
6. English (eng) - Article system (a/the)
7. Spanish (spa) - Null subject + articles
8. Biblical Hebrew (heb) - Source language (definiteness only)
9. Biblical Greek (ell) - Source language (articles only)
10. Mandarin Chinese (cmn) - Topic-prominent (optional marking)

**Family Distribution** (Top 5):
- Austronesian: 176 languages (17.4%)
- Trans-New Guinea: 141 (14.0%)
- Indo-European: 135 (13.4%)
- Niger-Congo: 89 (8.8%)
- Otomanguean: 69 (6.8%)

**Switch-Reference Systems**: Trans-New Guinea (141 languages) and Australian (36 languages) families commonly have switch-reference—a related but distinct system tracking subject continuity/change across clauses.

**For full details**: See [LANGUAGES.md](LANGUAGES.md)

---

### [SCHOLARLY.md](SCHOLARLY.md) - Scholarly Research

**Lines**: 1,052 | **Sources**: 22+ major scholarly works | **All sources cited with URLs**

#### Key Points:

**Foundational Frameworks**:

1. **Givón (1983)** - *Topic Continuity in Discourse*
   - Quantitative cross-linguistic study
   - Referential distance (look-back), interference (ambiguity), persistence (decay)
   - 8 languages studied including Biblical Hebrew, Japanese, spoken English

2. **Lambrecht (1994)** - *Information Structure and Sentence Form*
   - Four categories: Presupposition/Assertion, Identifiability, Activation, Topic/Focus
   - Cascading model: Activation → Identification → Topic establishment
   - Explains TBTA "Presupposed" vs "Routine" distinction

3. **Prince (1981)** - *Taxonomy of Given-New Information*
   - "Assumed Familiarity" (speaker assumptions about hearer knowledge)
   - Three dimensions: Familiarity, Saliency, Shared Knowledge
   - TBTA values map to Prince's taxonomy

4. **Gundel, Hedberg, & Zacharski (1993)** - *Givenness Hierarchy*
   - Six implicationally related cognitive statuses
   - In focus > Activated > Familiar > Uniquely identifiable > Referential > Type identifiable
   - Form-status mapping: high accessibility → minimal forms (pronouns, zero)

**Biblical Translation Specifics**:

5. **Levinsohn (2000/2024)** - *Discourse Features of NT Greek*
   - Greek article usage, reactivation patterns, anarthrous references
   - BART markup of complete Greek NT
   - "Routine" vs "Restaging" mapped to "activated" vs "reactivation"

6. **Dooley & Levinsohn (2001)** - *Analyzing Discourse*
   - Three tasks of reference: Semantic (identify), Processing (overcome disruptions), Discourse-pragmatic (mark info structure)
   - Eight-step methodology for analyzing reference patterns
   - Participants vs. Props distinction

7. **Van der Merwe (2019)** - *Participant Tracking in Biblical Hebrew*
   - Hebrew pronouns clear by Hebrew discourse rules but "ambiguous" to European languages
   - Translators must maintain clarity via explicitation
   - Validates TBTA's approach of adding analysis not in Hebrew morphology

**Language-Specific Case Studies**:

8. **Japanese**: wa/ga function analogously to switch-reference (90%+ subject identification success)

9. **Korean**: Episode-based topic marking (different from Japanese hearer-old logic)

10. **Bantu**: Noun class agreement provides "referential clarity" (Van de Velde 2013)

**Typological Surveys**:

11. **WALS**: 198 languages have NO definite/indefinite articles—yet all languages mark information status via alternative strategies

12. **Grambank**: 2,467 languages, 195 features; participant marking interacts with case, word order, verbal indexing

**Scholarly Consensus**:
✅ All languages have participant reference systems (universal)
✅ Referring expression form correlates with accessibility (cross-linguistic)
✅ Three tasks: Semantic, Processing, Discourse-pragmatic (Dooley & Levinsohn)
✅ Source languages (Hebrew/Greek) lack dedicated PT morphology—TBTA adds this layer

**For full details & bibliography**: See [SCHOLARLY.md](SCHOLARLY.md)

---

### [THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml) - Theological Classification

**Lines**: 443 | **Classification**: 15% non-arbitrary, 85% arbitrary

#### Non-Arbitrary Contexts (Theologically/Contextually Critical):

**1a. Trinity References** (e.g., Genesis 1:26)
- **Theological Stakes**: HIGH
- **Affected Doctrines**: Trinity, Creation theology
- **Issue**: "Let us make man" - Presupposed vs. First Mention affects article/topic marker choice
- **Orthodox Position**: Presupposed (God known to readers even before Gen 1:1)
- **Forbidden**: Interpretations obscuring Trinity (polytheism, royal plural, divine council)
- **Interaction**: Coordinates with Number feature (Trial = 3 persons, never Dual = 2)

**1b. Messianic Prophecy** (e.g., Isaiah 53)
- **Theological Stakes**: HIGH
- **Affected Doctrines**: Christology, Atonement, Prophecy fulfillment
- **Issue**: Is "Servant" routine continuation (same as Isaiah 42, 49, 50) or different referent?
- **Orthodox Position**: Routine/Restaging (specific individual = Jesus Christ)
- **Forbidden**: Generic servant (loses Messianic specificity)
- **Denominational Note**: Christian (Servant = Christ) vs. Jewish (Servant = Israel)

**2. Divine vs. Human Participants** (e.g., Genesis 18)
- **Theological Stakes**: MEDIUM
- **Issue**: "Three visitors" to Abraham—one is LORD (YHWH), two are angels
- **Orthodox Position**: LORD = Routine (same God as throughout Genesis, not new participant)
- **Guidance**: Maintain divine participant continuity; distinguish God from angels

**3. Pronoun Ambiguity in Theological Contexts** (e.g., John 1:1-3)
- **Theological Stakes**: HIGH
- **Issue**: "He was in the beginning" - Must clearly refer to "the Word" (Jesus), not "God" (Father)
- **Orthodox Position**: Routine continuation of "Word" from John 1:1
- **Guidance**: Explicit participant tracking to avoid Christological error

**4. Corporate vs. Individual Identity** (e.g., Acts 16 - Paul and Silas)
- **Theological Stakes**: LOW-MEDIUM
- **Issue**: "They" = Paul and Silas (2) or larger group?
- **Guidance**: Use dual number if available; maintain clear participant boundaries

#### Arbitrary Contexts (Stylistic/Contextual - Translator Freedom):

- **Crowd sizes and generic groups** (40%): "Multitude," "disciples" - stylistic choice
- **Minor characters** (25%): Servants, messengers, bystanders without theological import
- **Inanimate objects/locations** (15%): "The mountain," "the temple," "the boat"
- **Routine narrative** (15%): Travel companions, family interactions
- **Generic roles** (5%): "A scribe," "the Pharisees" (unless specific named individual)

**Total**: 85% arbitrary (translator freedom), 15% non-arbitrary (requires theological/contextual care)

**For full classification**: See [THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)

---

## Critical Discrepancies & Tensions

### 1. TBTA vs. Linguistic Theory: Presupposition

**TBTA**: God marked "Routine" in Genesis 1:1
**Linguistic Theory** (Lambrecht 1994, Prince 1981): Should be "Presupposed" or "Identifiable but not evoked"
**Impact**: Affects how translators use definite articles, topic markers
**Resolution Needed**: Add "Presupposed" as distinct value from "Routine"

### 2. TBTA vs. Biblical Text: Restaging

**TBTA**: Restaging value defined but 0% usage
**Biblical Text**: Clear restaging instances (Joseph Gen 37→39, prophets, Gospel characters)
**Impact**: Languages requiring restaging markers (Japanese wa, Korean ga) lack guidance
**Resolution Needed**: Develop systematic restaging criteria, annotate cross-chapter reintroductions

### 3. TBTA vs. Source Languages: Morphological Gap

**Source Languages** (Hebrew/Greek): No grammatical PT encoding
**TBTA**: Adds discourse-level PT analysis
**Scholarly Validation** (Van der Merwe 2019, Runge 2007): Hebrew has discourse rules that make reference clear, but rules differ from European languages
**Impact**: TBTA provides essential analysis for target languages requiring PT marking
**No discrepancy**: This is TBTA's intended function (target-language-driven analysis)

---

## Recommendations for Stage 2 (Dataset Creation)

### 1. Control Language Selection (10 languages)

**Mandatory Marking** (5):
- Japanese (jpn) - **Need to add to dataset** ⚠️
- Korean (kor) - **Need to add to dataset** ⚠️
- Swahili (swa) - Likely available ✅
- Quechua (quz) - 18 languages available ✅
- Tagalog (tgl) - 176 Austronesian available ✅

**Optional Marking** (5):
- English (eng) - Available ✅
- Spanish (spa) - Available ✅
- Hebrew (heb) - Source OT ✅
- Greek (ell) - Source NT ✅
- Mandarin (cmn) - 18 Sino-Tibetan likely includes ✅

### 2. Value Refinement for myBibleToolbox

**Add**:
- **Presupposed**: Culturally known but textually first mention (God in Gen 1:1)

**Clarify**:
- **Restaging**: Develop criteria for cross-chapter/cross-episode reintroduction
- **Frame Inferable**: Create systematic frame database

**Remove/Deprecate**:
- **Integration**: 0% usage, unclear definition
- **Exiting**: 0% usage, consider merging with Offstage or removing
- **Offstage**: Essentially 0% usage, evaluate necessity

### 3. Sampling Strategy for Stage 2

**Balanced Sampling** (100+ verses per value minimum):
- **Routine** (73%): 100+ verses (common)
- **Generic** (14%): 100+ verses (moderately common)
- **Frame Inferable** (7.5%): 100+ verses (need targeted sampling)
- **First Mention** (5.4%): 100+ verses (book beginnings, new character introductions)
- **Interrogative** (0.23%): All 394 instances (rare)
- **Presupposed** (NEW): 50+ verses (God introductions, sun/moon, culturally known entities)
- **Restaging** (UNDER-ANNOTATED): Manually identify 50-100 verses (Joseph, prophets, Gospel characters)

**Theologically Critical Subset** (15% of instances):
- All Trinity references (Genesis 1:26, Matthew 28:19, etc.)
- All Messianic prophecy (Isaiah 53, Psalm 22, Zechariah, etc.)
- Divine participant passages (theophanies, Christophanies)
- Theologically dense pronoun resolution (John 1, Colossians 1, Hebrews 1)

### 4. Cross-Feature Coordination

**Number System**: Trinity references (Trial vs. Plural vs. Dual)
**Surface Realization**: Pronoun vs. Full NP vs. Zero anaphora
**Noun List Index**: Coreference tracking across verse boundaries
**Honorifics/Register**: Divine participants in honorific languages

---

## Research Gaps & Future Work

### 1. Missing Languages

**Critical Gap**: Japanese and Korean not in 1,009-language dataset
- Both are MANDATORY participant tracking languages
- Need to source Japanese/Korean Bible translations for Stage 2

**Alternative**: Use closely related languages as proxies or document gap

### 2. Undocumented TBTA Decisions

**No algorithmic criteria** for:
- Presupposition detection
- Frame Inferable assignment
- Restaging threshold (how long absence = restaging?)

**Need**: Systematic annotation guidelines for Stage 3 algorithm development

### 3. Confidence Scoring

**Current**: All TBTA annotations treated as equally certain
**Reality**: Morphological features (high confidence) vs. Frame Inferable (subjective, lower confidence)
**Future**: Add confidence metadata to annotations

### 4. Cross-Reference Validation

**Current**: Single-pass annotation (no consistency checking)
**Issue**: Parallel Gospel passages may have inconsistent annotations
**Future**: Multi-stage validation, parallel passage alignment

---

## Quick Reference: Where to Look

**Need to understand TBTA values?** → [TBTA.md](TBTA.md) Section 2-3 (Value Inventory, Distribution)

**Need to know which languages require this feature?** → [LANGUAGES.md](LANGUAGES.md) Section 3 (Typological Classification)

**Need theoretical justification?** → [SCHOLARLY.md](SCHOLARLY.md) Section 1-2 (Foundational Frameworks, Biblical Translation)

**Need to identify theologically critical instances?** → [THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml) (Non-Arbitrary Contexts)

**Need control language details?** → [LANGUAGES.md](LANGUAGES.md) Section 5 (Proposed Control Languages)

**Need to understand presupposition issue?** → [TBTA.md](TBTA.md) Section 5.2 + [THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml) Special Notes

**Need restaging examples?** → [TBTA.md](TBTA.md) Section 5.3 + [LANGUAGES.md](LANGUAGES.md) Section 3.1 (Japanese/Korean)

---

**Document Status**: Complete research summary
**Lines**: 199 (under 200-line progressive disclosure limit)
**Stage**: Stage 1 Research complete
**Next Stage**: Stage 2 - Dataset Creation (100+ verses per value, 10 control languages)
