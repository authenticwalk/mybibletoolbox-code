# TBTA Language-Specific Annotation Adaptation Guide

**Document Purpose**: Practical guide for adapting TBTA annotations to the grammatical realities of specific language families
**Target Audience**: Bible translators, linguistic consultants, annotation specialists
**Date**: 2025-11-05
**Status**: Complete

---

## Table of Contents

1. [Introduction](#introduction)
2. [How to Use This Guide](#how-to-use-this-guide)
3. [Family-by-Family Adaptation Guides](#family-by-family-adaptation-guides)
   - [1. Austronesian](#1-austronesian-176-languages)
   - [2. Trans-New Guinea](#2-trans-new-guinea-129-languages)
   - [3. Indo-European](#3-indo-european-135-languages)
   - [4. Niger-Congo](#4-niger-congo-94-languages)
   - [5. Otomanguean](#5-otomanguean-69-languages)
   - [6. Mayan](#6-mayan-41-languages)
   - [7. Australian](#7-australian-36-languages)
   - [8. Afro-Asiatic](#8-afro-asiatic-25-languages)
   - [9. Sino-Tibetan](#9-sino-tibetan-18-languages)
   - [10. Quechuan](#10-quechuan-18-languages)
4. [Cross-Family Comparison Tables](#cross-family-comparison-tables)
5. [Recommendations for Under-Documented Languages](#recommendations-for-under-documented-languages)
6. [Conclusion](#conclusion)

---

## Introduction

### The Challenge of Universal Annotation

The Bible Translator's Assistant (TBTA) provides a rich semantic annotation system designed to facilitate Bible translation across the world's linguistic diversity. However, the 1,009 languages in our dataset exhibit radically different grammatical systems. What is **obligatory** in one language may be **impossible** to express in another. What requires **complex morphology** in one family may be **lexically encoded** or **contextually inferred** in another.

This guide addresses the fundamental question: **Which TBTA annotations matter most for which language families?**

### Core TBTA Features Analyzed

This guide focuses on six major TBTA annotation categories:

1. **Number Systems** - Singular, Dual, Trial, Quadrial, Paucal, Plural
2. **Verb TAM** - Time (16+ values), Aspect (9 values), Mood (11 values)
3. **Participant Tracking** - 9 states from First Mention to Generic
4. **Degree** - Comparative, superlative, intensification (11 values)
5. **Proximity** - Spatial, temporal, discourse deixis (10 values)
6. **Polarity** - Affirmative vs. Negative

### Annotation Philosophy

**Three Principles Guide This Analysis:**

1. **Critical Features**: Grammatically obligatory in the target language; omission causes ungrammaticality
2. **Relevant Features**: Grammatically optional but semantically important; omission causes unnaturalness
3. **Irrelevant Features**: Not distinguished in the target language; forcing the distinction creates awkwardness

**Translation Strategy**: Prioritize critical features, preserve relevant features where possible, and gracefully collapse irrelevant distinctions.

### Dataset Overview

Our 1,009 languages represent:
- **70+ language families**
- **22 countries** (for African languages alone)
- **Geographic spread**: Every inhabited continent
- **Typological diversity**: Isolating to polysynthetic, tonal to stress-based, SOV to VSO

The top 10 families account for **747 languages (74%)** of our dataset, making them the primary focus of this guide.

---

## How to Use This Guide

### For Translators

**Step 1: Identify Your Language Family**

Look up your target language in the dataset. Note its family classification:
```
Example: Tok Pisin (tpi) → Creole (Melanesian Pidgin)
         Refer to: Austronesian patterns + Creole simplification notes
```

**Step 2: Read Your Family Section**

Each family section provides:
- ✅ **CRITICAL features** - Annotate with extreme care
- ⚠️ **RELEVANT features** - Important but may have flexibility
- ❌ **IRRELEVANT features** - Can be collapsed or ignored
- 🔧 **Special considerations** - Unique grammatical interactions

**Step 3: Apply Annotation Adjustments**

Follow the **Recommended Annotation Strategy** for your family:
- Which TBTA values to prioritize
- Which distinctions can be merged
- Where to add external documentation

**Step 4: Validate Against Reference Grammars**

Cross-check with:
- Published grammars for your specific language
- Existing Bible translations in related languages
- Native speaker intuitions (critical!)

### For Linguistic Consultants

**Use This Guide To:**

1. **Train translators** on which grammatical features require careful attention
2. **Explain mismatches** between source languages (Greek/Hebrew) and target languages
3. **Develop language-specific annotation schemas** extending TBTA's universal system
4. **Identify research gaps** where better grammatical descriptions are needed

### For Annotation Specialists

**Workflow Integration:**

```
1. Parse source text (Greek/Hebrew) → Generate/Predict TBTA annotations
2. Identify target language family → Load family-specific profile (this guide)
3. Map critical features → Preserve obligatory distinctions
4. Collapse irrelevant features → Simplify where target language doesn't distinguish
5. Add family-specific extensions → Capture unique grammatical categories
6. Validate output → Check against family-specific constraints
```

### Reading the Family Profiles

Each profile follows this template:

- **Language Count** - How many languages from this family in dataset
- **Geographic Distribution** - Where these languages are spoken
- **Typological Profile** - Overview of shared grammatical features
- **CRITICAL FEATURES** - Must-annotate categories with rationale
- **RELEVANT FEATURES** - Important but flexible categories
- **IRRELEVANT FEATURES** - Can be safely collapsed
- **Special Considerations** - Unique interactions and edge cases
- **Common Translation Challenges** - Frequent problem areas
- **Recommended Annotation Strategy** - Practical workflow guidance
- **Example Languages** - Specific languages illustrating patterns

### Notation Conventions

- ✅ **CRITICAL** - Grammatically obligatory, high priority
- ⚠️ **RELEVANT** - Semantically important, medium priority
- ❌ **IRRELEVANT** - Not grammatically distinguished, low priority
- 🔧 **SPECIAL** - Requires unique handling, consult grammar
- 📊 **STAT** - Statistical information about feature distribution

---

## Family-by-Family Adaptation Guides

---

## 1. Austronesian (176 Languages)

### Overview

**Dataset Count**: 176 languages (17.4% of total)
**Geographic Distribution**:
- Papua New Guinea: 87 languages (50.6%)
- Philippines: 45 languages (26.2%)
- Indonesia: 18 languages (10.5%)
- Micronesia, Solomon Islands, Vanuatu: 28 languages (16.2%)
- Other (Pacific, Madagascar): 4 languages (2.3%)

**Major Subgroups in Dataset**:
- **Oceanic**: ~109 languages (Melanesia, Polynesia, Micronesia)
  - Melanesian: Majority of PNG languages
  - Polynesian: Hawaiian, Tongan
  - Micronesian: Chuukese, Pohnpeian, Kosraean
- **Western Malayo-Polynesian**: ~63 languages (Philippines, western Indonesia)
  - Philippine-type: Tagalog, Cebuano, Ilocano, Manobo languages
  - Indonesian-type: Indonesian, Malay
- **Central Malayo-Polynesian**: Several eastern Indonesian languages

### Typological Profile

**Key Grammatical Features**:
- **Voice systems**: Symmetrical voice (Philippine-type: 4 voices; Indonesian-type: 2 voices)
- **Pronouns**: Inclusive/exclusive distinction nearly universal
- **Number**: Dual common in Oceanic languages
- **TAM**: Realis/irrealis primary modal distinction
- **Morphology**: Affixation-heavy (prefixes, suffixes, infixes, circumfixes)
- **Word order**: VSO/VOS (Philippine), SVO (Indonesian, most Oceanic)
- **Possession**: Alienable/inalienable distinction (especially Oceanic)

---

### ✅ CRITICAL Features for Austronesian

#### 1. **Number - Dual Distinction** (Oceanic subgroup)

**Why Critical**:
- **Obligatory** in many Oceanic languages (Polynesian, Micronesian)
- Grammatically encoded in pronouns, verbs, adjectives
- **Failure to distinguish** = ungrammatical sentences

**Languages Affected**: ~109 Oceanic languages in dataset

**Annotation Strategy**:
- Mark all references to **exactly two entities** with Dual (D)
- Common contexts:
  - "Two disciples" → Dual
  - "They two" (Luke 24:13) → Dual
  - "Both" constructions → Dual
  - Paired body parts (eyes, hands) → Dual in some languages

**Example**: Tongan
- Singular: *au* "I"
- Dual: *kita* "we two (inclusive)", *maua* "we two (exclusive)"
- Plural: *kitautolu* "we all (inclusive)", *mautolu* "we all (exclusive)"

**Source Annotation**: Since Greek lacks productive dual, annotators must **infer from context** when exactly two referents are involved.

---

#### 2. **Inclusive/Exclusive Pronouns**

**Why Critical**:
- **Obligatory** in almost all Austronesian languages
- Fundamental semantic distinction: Does "we" include the addressee?
- Misuse changes **meaning** of scriptural passages

**Languages Affected**: ~170+ languages (nearly universal in family)

**Annotation Strategy**:
- **Inclusive (I)**: "We" includes addressee
  - Acts 16:10: "God had called **us** to preach" → Exclusive (Paul's group, not Philippians)
  - Matthew 28:20: "I am with **you**" → If recast as "we," likely Inclusive
- **Exclusive (E)**: "We" excludes addressee
  - Epistolary "we" (Paul + coworkers, not readers) → Exclusive
  - Narrative "we" (disciples, not audience) → Exclusive

**Critical Passages**:
- Genesis 1:26: "Let **us** make man" → Inclusive (Trinity) or Exclusive (God + angels)?
- Theological interpretation required

**Common Pitfall**: English "we" is ambiguous. Greek lacks this distinction. Annotators must **analyze discourse participants**.

---

#### 3. **Realis/Irrealis Mood**

**Why Critical**:
- **Central organizing principle** of Austronesian TAM systems
- Often conflated with:
  - Tense (realis = past/present, irrealis = future)
  - Polarity (negation → irrealis)
  - Mood (imperatives → irrealis)

**Languages Affected**: Majority of Austronesian languages

**Annotation Strategy**:
- **Realis (R)**: Events that happened or are happening
  - Past perfective → Realis
  - Present imperfective → Realis
  - Gnomic/habitual → Realis
- **Irrealis (I)**: Events that have not (yet) happened
  - Future → Irrealis
  - Conditionals → Irrealis
  - Negation → Often triggers irrealis
  - Commands → Irrealis

**Example** (Tagalog):
- Realis: *nag-* (perfective), *nag-...-ang* (imperfective)
- Irrealis: *mag-* (future, imperative, conditional)

**Translation Challenge**: Greek aorist is **aspectual** (perfective), not modal. May map to realis or irrealis depending on context.

---

#### 4. **Voice/Focus Systems** (Philippine-type languages)

**Why Critical**:
- **Obligatory** voice marking on every verb
- Determines which semantic role is the "topic/focus" of the clause
- Four voices in Philippine-type:
  1. **Actor Voice**: Agent is topic
  2. **Patient Voice**: Patient is topic
  3. **Locative Voice**: Location is topic
  4. **Instrumental/Benefactive Voice**: Instrument or beneficiary is topic

**Languages Affected**: ~45 Philippine languages, some northern Indonesian

**Annotation Strategy**:
- **Analyze information structure** of source text:
  - Is the agent new or given information?
  - Is the patient in focus or backgrounded?
  - Is location pragmatically prominent?
- **Select voice** based on discourse flow:
  - New agent → Patient voice (agent demoted)
  - Given agent → Actor voice (agent promoted)
  - Location-oriented narrative → Locative voice

**Example** (Tagalog): "Jesus healed the man"
- Actor focus: *Nag-pahid si Jesus sa lalaki* (Jesus is-the-one-who-healed the man)
- Patient focus: *Pinag-pahid ni Jesus ang lalaki* (The man is-the-one-who-was-healed by Jesus)

**Translation Challenge**: Greek and Hebrew don't use voice systems this way. **Information structure analysis** of source text is required.

---

### ⚠️ RELEVANT Features for Austronesian

#### 5. **Possession - Alienable/Inalienable**

**Why Relevant**:
- **Pervasive** in Oceanic languages (Micronesian especially)
- Semantic categorization of possessed nouns:
  - **Inalienable**: Body parts, kinship, inherent attributes
  - **Alienable**: Separable possessions, general ownership
- Different morphological marking for each category

**Languages Affected**: ~100+ Oceanic languages

**Annotation Strategy**:
- Mark **semantic relationship** between possessor and possessed:
  - "My body" (1 Cor 6:19) → Inalienable
  - "My Father" (Jesus re: God) → Inalienable (kinship)
  - "My sheep" (John 10:27) → Alienable (ownership)
  - "Our possessions" → Alienable

**Micronesian Complexity**: Some languages have **multiple alienable classes**:
- Food possession ("my food to eat")
- Drink possession ("my water to drink")
- General possession

**Annotation Extension**: Consider adding **possession type** metadata beyond standard TBTA.

---

#### 6. **Participant Tracking**

**Why Relevant**:
- Austronesian languages vary in **pronoun dropping** (pro-drop):
  - **Philippine**: Generally pro-drop (subject pronouns optional)
  - **Indonesian**: Less pro-drop (subject pronouns more common)
  - **Oceanic**: Variable
- **Surface realization** differs from tracking state

**Annotation Strategy**:
- Use standard TBTA participant tracking states:
  - First Mention, Routine, Generic, etc.
- But recognize **surface form** may be:
  - **Zero (Ø)** in pro-drop languages (Routine participants)
  - **Full NP** in non-pro-drop languages (Routine participants)
- **Tracking state ≠ Surface form**

---

#### 7. **Reduplication**

**Why Relevant**:
- **Very common** throughout Austronesian
- Semantic functions:
  - **Plurality**: Bahasa Indonesia *anak-anak* "children" (from *anak* "child")
  - **Intensification**: More intense form of property
  - **Distributive**: Each one, separately
  - **Future tense**: Tagalog *la-lakad* "will walk" (from *l-um-akad* "walk")

**Annotation Strategy**:
- **Number**: Full reduplication for plural → Mark as Plural (P)
- **Degree**: Reduplication for intensification → Mark as Intensified (I)
- **Aspect/Tense**: Reduplication for future → Mark as appropriate time value

**Challenge**: Same morphological process (reduplication) serves **multiple functions**. Context determines which.

---

### ❌ IRRELEVANT Features for Austronesian

#### 8. **Grammatical Gender**

**Why Irrelevant**:
- **Absent** in Austronesian languages
- No masculine/feminine/neuter distinction
- Pronouns not gendered (except through noun class in some languages)

**Annotation Adjustment**:
- TBTA gender marking can be **ignored** for Austronesian targets
- Source language gender (Greek masculine/feminine/neuter) **does not transfer**
- Use **semantic gender** only when referring to biological sex

**Example**: Greek πνεῦμα (pneuma, "spirit") is **neuter**. In Austronesian languages, there is no grammatical consequence of this.

---

#### 9. **Case Systems** (mostly irrelevant)

**Why Mostly Irrelevant**:
- **Philippine-type**: Have case-like markers (ang, ng, sa), but these mark **focus/topic**, not syntactic case
- **Indonesian-type**: No case marking
- **Oceanic**: Generally no case marking

**Exception**: Ergative case marking exists in some Austronesian languages, but it's not widespread in our dataset.

**Annotation Adjustment**:
- Greek/Hebrew case distinctions (nominative/accusative/genitive/dative) **do not map** to Austronesian
- Word order and prepositions/postpositions encode relationships instead
- Focus on **semantic roles** (agent, patient, location) rather than syntactic cases

---

### 🔧 Special Considerations for Austronesian

#### Voice System + Realis/Irrealis Interaction

**Complex Interaction**:
- **Voice morphology** differs in realis vs. irrealis
- Same semantic voice has **different affixes** depending on mood
- Example (Tagalog):
  - Actor Voice Realis: *nag-*
  - Actor Voice Irrealis: *mag-*

**Annotation Strategy**:
- Mark **both** voice and mood
- Ensure consistency across interaction

---

#### Elevation-Based Deixis (Some Oceanic Languages)

**Phenomenon**: Languages in mountainous regions (e.g., parts of Papua New Guinea classified as Austronesian) may have **elevation-based spatial deixis**.

**Languages**: Not widespread in Austronesian (more common in Trans-New Guinea), but some contact effects.

**Annotation**: Use TBTA proximity codes, but recognize **vertical dimension** may be implicit:
- "Go up to Jerusalem" → Proximal + upward motion (verb-encoded)
- "Come down from mountain" → Proximal + downward motion (verb-encoded)

---

### Common Translation Challenges

1. **Greek Aorist → Realis or Irrealis?**
   - Greek aorist = **perfective aspect** (not just past tense)
   - In past contexts → Realis
   - In subjunctive/optative → Irrealis
   - **Solution**: Analyze mood and context

2. **Inclusive/Exclusive Ambiguity**
   - English/Greek "we" is ambiguous
   - **Solution**: Discourse analysis, identify participants
   - Consult commentaries for theological passages

3. **Voice Selection**
   - Greek doesn't use Philippine-type voice systems
   - **Solution**: Analyze information structure
   - Given information → Background
   - New information → Focus
   - Pragmatic prominence guides voice choice

4. **Zero Anaphora**
   - Pro-drop languages drop pronouns for Routine participants
   - TBTA marks tracking state, not surface form
   - **Solution**: Surface realization ≠ Tracking state

---

### Recommended Annotation Strategy

**Priority Hierarchy**:

1. **HIGHEST PRIORITY**:
   - Inclusive/Exclusive pronouns (semantic change if wrong)
   - Realis/Irrealis mood (grammatically obligatory)
   - Dual number for Oceanic languages (obligatory)

2. **HIGH PRIORITY**:
   - Voice/focus systems for Philippine-type languages
   - Alienable/inalienable possession for Oceanic
   - Participant tracking (affects surface realization)

3. **MEDIUM PRIORITY**:
   - Time distinctions (map to realis/irrealis + tense particles)
   - Aspect distinctions (perfective/imperfective often marked)
   - Reduplication contexts

4. **LOW PRIORITY**:
   - Grammatical gender (not distinguished)
   - Case systems (not applicable)
   - Many degree distinctions (often lexical, not morphological)

**Workflow**:
1. Annotate inclusive/exclusive for all 1st person plural
2. Annotate realis/irrealis for all verbs
3. For Oceanic: Annotate dual for all pair references
4. For Philippine: Analyze information structure for voice
5. Mark possession type where relevant
6. Collapse gender and case distinctions

---

### Example Languages

**Hawaiian (Polynesian, Oceanic)**:
- ✅ Dual number (obligatory)
- ✅ Inclusive/exclusive (obligatory)
- ✅ VSO word order (matches Hebrew, not Greek)
- ❌ No gender
- ❌ No case system

**Tagalog (Philippine)**:
- ✅ Four-voice system (CRITICAL)
- ✅ Inclusive/exclusive (obligatory)
- ✅ Realis/irrealis (obligatory)
- ⚠️ Reduplication for plural and future
- ❌ No gender
- ❌ No grammatical case (focus markers instead)

**Indonesian/Malay (Western MP)**:
- ✅ Realis/irrealis (less robust than Philippine)
- ✅ Inclusive/exclusive (obligatory)
- ⚠️ Reduplication for plurality
- ⚠️ Passive voice common (Indonesian-type 2 voices)
- ❌ Minimal inflection
- ❌ No gender, no case

**Tok Pisin (Melanesian Pidgin, contact language)**:
- ✅ **Trial number** (yumitripela "we three inclusive")
- ✅ Inclusive/exclusive (obligatory)
- ⚠️ Simplified TAM (preverbal particles)
- ❌ No voice system
- ❌ No case system

---

## 2. Trans-New Guinea (129 Languages)

### Overview

**Dataset Count**: 129 languages (12.8% of total)
**Geographic Distribution**: Papua New Guinea (interior highlands and mountains), Indonesia (West Papua/Papua provinces)

**Major Subgroups in Dataset**:
- Eastern Highlands (Kainantu-Goroka): ~15 languages
- Engan-Chimbu: ~15 languages
- Madang: ~15 languages
- Finisterre-Huon: ~10 languages
- Ok-Oksapmin: ~6 languages
- Bosavi: ~2 languages
- Binandere, Goilalan, Angan, and 20+ other smaller subgroups

### Typological Profile

**Key Grammatical Features**:
- **Word order**: SOV (Subject-Object-Verb) universal
- **Verb morphology**: Medial vs. final verb distinction (clause chaining)
- **Switch-reference**: Morphological marking of subject continuity/change
- **Case**: Often ergative-absolutive (especially optional ergativity)
- **Number**: Dual common, some languages have paucal
- **TAM**: Obligatory marking (94.7% of nuclear TNG languages)
- **Evidentiality**: Concentrated in Highlands Evidentiality Area (14+ languages)
- **Spatial deixis**: Elevation-based systems (uphill/downhill) in highlands

### ✅ CRITICAL Features for Trans-New Guinea

#### 1. **Switch-Reference and Clause Chaining**

**Why Critical**:
- **Defining feature** of Trans-New Guinea languages
- **Obligatory** marking on medial verbs
- Distinguishes:
  - **SS (Same Subject)**: Next clause has same subject
  - **DS (Different Subject)**: Next clause has different subject
- Maintains participant tracking across multi-clause chains

**Languages Affected**: Vast majority of TNG languages

**Annotation Strategy**:
- **Participant tracking** becomes **critical**
- Must track:
  - **Referential distance**: Clauses since last mention
  - **Subject continuity**: Does subject change?
- Mark **medial vs. final verbs**:
  - **Medial**: Clause-chaining, switch-reference marking
  - **Final**: Sentence-final, full TAM marking

**Example** (Usan):
- Same-subject medial: *qamb* (say.SS) "said and [same subject]..."
- Different-subject medial: *-ig* (DS) "said and [different subject]..."
- Final verb: Full tense/aspect/mood paradigm

**Translation Challenge**: Greek coordinate clauses ("and...and...and") map to **clause chains** with switch-reference. Must restructure to match TNG discourse patterns.

---

#### 2. **Evidentiality** (Highlands Languages Only)

**Why Critical**:
- **Grammatically obligatory** in ~14 languages (Highlands Evidentiality Area)
- Every statement requires **marking information source**:
  - Visual (saw it)
  - Nonvisual (heard it)
  - Inferential (inferred from evidence)
  - Reportive (hearsay)
  - Assumed (assumed truth)
- **Omission = ungrammatical**

**Languages Affected** (Highlands Evidentiality Area):
- **Ok-Oksapmin family**: Telefol, Oksapmin, Tifal, Faiwol, Bimin, Mian
- **Duna-Bogaya family**: Duna
- **Engan family**: Enga, Huli, Ipili
- **Kutubuan family**: Fasu, Foe (East/West Kutubu)
- **Bosavi family**: Kaluli

**Annotation Strategy**:
- **EXTEND TBTA** with evidential metadata:
  - **Visual**: Direct eyewitness
  - **Sensory**: Heard/felt/smelled
  - **Inferential**: Evidence-based conclusion
  - **Reportive**: Hearsay/reported
  - **Assumed**: General knowledge
- **Critical for Biblical genres**:
  - **Gospels**: Eyewitness (visual) vs. reported (from others)
  - **Epistles**: Paul's direct experience (visual) vs. transmitted teaching (reportive)
  - **Prophecy**: Divine revelation (requires special evidential - "factual" or "visual"?)
  - **OT narrative**: Depends on narrator's perspective

**Example** (Tuyuca, related language):
Five evidential paradigms:
- *díiga* "he played soccer" (I saw him)
- *díihi* "he played soccer" (I heard him)
- *díiyá* "he played soccer" (I infer from evidence)
- *díiyigɨ* "he played soccer" (someone told me)
- *díihɨ* "he played soccer" (assumed/general knowledge)

**Translation Challenge**: Biblical languages (Greek/Hebrew) **do not mark evidentiality**. Annotators must **infer** from:
- Genre (Gospel = eyewitness)
- Source statements ("We have seen...", "I heard...", "They report...")
- Context clues

---

#### 3. **Dual Number**

**Why Critical**:
- **Obligatory** in many TNG languages
- Marked on:
  - Pronouns (universal)
  - Verbs (subject/object agreement)
  - Nouns (some languages)

**Languages Affected**: Majority of TNG languages

**Annotation Strategy**:
- Mark all references to **exactly two entities** as Dual (D)
- Common Biblical contexts:
  - "Two disciples" → Dual
  - "Both" → Dual
  - "They two" (Luke 24:13) → Dual
  - Paired participants in narrative

**Proto-TNG Reconstruction**: Dual suffixes *-li* and *-t*

**Translation Challenge**: Greek lacks productive dual. Must infer from context and numerals.

---

#### 4. **Multiple Past Tenses** (Remoteness Distinctions)

**Why Critical**:
- **Extremely common** in TNG languages
- Many languages distinguish 3-6 past tenses by **temporal distance**

**Typical Systems**:
- **Present**: Current time
- **Hodiernal/Today's past**: Earlier today
- **Hesternal/Yesterday's past**: Yesterday
- **Recent past**: Few days ago
- **Remote past**: Before recent memory
- **Distant/Mythological past**: Ancient events

**Example** (Amele, Madang):
- Present
- Today's past
- Yesterday's past
- Remote past (before yesterday)
- Habitual past
- Future

**Languages Affected**: Majority of TNG languages

**Annotation Strategy**:
- Use TBTA's **fine-grained time values**:
  - `A` (Earlier Today)
  - `a` (Yesterday)
  - `b` (2 Days Ago)
  - `c` (3 Days Ago)
  - `g` (During Speaker's Lifetime)
  - `h` (Historic Past)
  - `i` (Eternity Past)
- Match temporal distance from narrative "now"

**Translation Challenge**: Greek aorist is **aspectual**, not temporal. Must analyze narrative timeline to determine **temporal distance**.

---

#### 5. **Ergative Case Marking** (Optional Ergativity)

**Why Critical**:
- **Common** in TNG languages
- Pattern: **Optional ergative** based on:
  - **Animacy**: More animate subjects → ergative
  - **Agentivity**: More volitional actions → ergative
  - **Focus**: Emphasized/contrastive subjects → ergative
  - **Disambiguation**: Ergative used when patient could be confused with subject

**Languages Affected**: Many TNG languages (Yali, Lower Grand Valley Dani, Kaluli, Ku Waru, Duna, etc.)

**Annotation Strategy**:
- **Extend TBTA** with ergative marking metadata:
  - Mark transitive subjects that require ergative case
  - Note animacy, volitionality, focus
- **Critical for**:
  - Divine agents (highly animate, highly volitional → ergative)
  - Human agents in foreground narrative
  - Contrastive/emphasized subjects

**Example Pattern**:
- Intransitive subject: Absolutive case (unmarked)
- Transitive subject (high animacy/agency): Ergative case
- Transitive object: Absolutive case (unmarked)

**Translation Challenge**: Greek/Hebrew are nominative-accusative. Agent-patient relationships must be **reanalyzed** for ergative alignment.

---

### ⚠️ RELEVANT Features for Trans-New Guinea

#### 6. **Serial Verb Constructions**

**Why Relevant**:
- **Extremely common and productive**
- Compensate for **small verb root inventories** (some languages: only ~60 verb roots)
- Functions:
  - **Causative**: Using 'get'/'make' verb
  - **Benefactive**: Using 'give' verb
  - **Aspectual**: Progressive (from 'stay'), completive (from 'finish')
  - **Directional**: Motion verbs in series

**Languages Affected**: Most TNG languages

**Annotation Strategy**:
- Mark **each verb** individually in TBTA
- But recognize they form a **semantic unit**:
  - Shared polarity (all affirmative or all negative)
  - Shared TAM scope
  - Shared subject
- Greek compound verbs may map to serial constructions

**Example** (Kalam, extensively studied):
- *nŋ- d- ap-* (eat-do-go.up) = "went up and ate" (directional serial)

---

#### 7. **Possession - Alienable/Inalienable**

**Why Relevant**:
- Present in many TNG languages
- Semantic categories:
  - **Inalienable**: Body parts, kinship, inherent attributes
  - **Alienable**: Separable possessions

**Example** (Wano):
Alienable/inalienable distinguished by:
- Nominal generalization patterns
- Plurality coding
- Possessive construction types

**Annotation Strategy**: Same as Austronesian (see Section 1, Feature 5)

---

#### 8. **Elevation-Based Spatial Deixis**

**Why Relevant**:
- **Concentrated in TNG highlands**
- Mountainous environment → vertical orientation grammaticalized
- Spatial terms encode **uphill/downhill/level**

**Languages Affected**: Highland languages (~50-80 estimated)

**Key Languages**:
- **Yupno** (Finisterre): Motion verbs distinguish up/down/level
  - **Temporal metaphor**: Uphill = future, Downhill = past
- **Kewapi** (Enga-Kewa-Huli): 13 demonstratives (9 with elevation)
- **Tauya** (Madang): Topographical deixis

**Annotation Strategy**:
- Use TBTA **proximity codes** for horizontal distance:
  - `S` (Near Speaker), `L` (Near Listener), `R` (Remote)
- **Add metadata** for vertical dimension:
  - Uphill, Downhill, Level
- **Biblical relevance**:
  - Hebrew עָלָה ('alah "go up") → Uphill forms
  - Hebrew יָרַד (yarad "go down") → Downhill forms
  - "Ascension" language maps naturally
  - "Go up to Jerusalem" (elevated city)

**Translation Challenge**: Elevation may be **implicit** in source text. Explicit in TNG target.

---

### ❌ IRRELEVANT Features for Trans-New Guinea

#### 9. **Articles**

**Why Irrelevant**:
- **Absent** in most TNG languages
- No definite/indefinite articles
- Definiteness inferred from context, demonstratives, or word order

**Annotation Adjustment**:
- Greek article system (ὁ, ἡ, τό) **does not transfer**
- Hebrew definite article (ה) **does not transfer**
- Use demonstratives for **emphatic definiteness** only

---

#### 10. **Grammatical Gender**

**Why Irrelevant**:
- **Not a widespread feature** in TNG
- When present, usually limited scope

**Annotation Adjustment**: Same as Austronesian (ignore gender for most languages)

---

### 🔧 Special Considerations for Trans-New Guinea

#### Clause Chaining + Evidentiality Interaction

**Phenomenon**: In languages with both clause chaining and evidentiality:
- Evidential marking typically on **final verb only**
- **Scope**: Evidential covers entire clause chain
- **Challenge**: Must determine evidential for entire narrative sequence

---

#### SOV Word Order

**Why Significant**:
- **Universal in TNG**
- Opposite of:
  - Greek: SVO (dominant)
  - Hebrew: VSO/VOS
- **Complete clause restructuring** required

**Annotation Impact**:
- Word order in source text **cannot be preserved**
- Focus on **semantic roles** (agent, patient, location)
- Relative clauses precede head noun (prenominal relatives)

---

#### Small Verb Inventories

**Challenge**: Languages with ~60 verb roots use **serial verbs** to expand meaning.

**Implication**:
- Single Greek verb may → multiple TNG verbs in series
- Greek compound verb may → serial verb construction

**Annotation**: Mark complex Greek verbs as potentially requiring serialization in target language.

---

### Common Translation Challenges

1. **Clause Chaining**
   - Greek coordination (καί "and") ≠ TNG medial verbs
   - **Solution**: Restructure into medial/final verb chains

2. **Evidentiality** (Highlands languages)
   - Source languages don't mark information source
   - **Solution**: Genre analysis (eyewitness vs. reported)
   - Prophecy requires special handling

3. **Multiple Past Tenses**
   - Greek aorist conflates all past times
   - **Solution**: Analyze narrative timeline, temporal adverbs
   - TBTA's 16+ time values help

4. **Ergativity**
   - Greek nominative-accusative ≠ ergative-absolutive
   - **Solution**: Analyze animacy, agency, focus for optional ergative

5. **Elevation**
   - "Go up" / "Come down" must specify vertical dimension
   - **Solution**: Hebrew עָלָה/יָרַד provide clues

---

### Recommended Annotation Strategy

**Priority Hierarchy**:

1. **HIGHEST PRIORITY** (Grammatically obligatory):
   - Participant tracking (for switch-reference)
   - Evidentiality (Highlands languages only)
   - Dual number
   - Multiple past tenses (temporal remoteness)

2. **HIGH PRIORITY**:
   - SOV word order restructuring (affects all clauses)
   - Ergative case marking (optional but semantically important)
   - Medial vs. final verb distinction

3. **MEDIUM PRIORITY**:
   - Serial verb constructions
   - Elevation-based deixis (highlands)
   - Possession type

4. **LOW PRIORITY**:
   - Articles (absent)
   - Gender (mostly absent)
   - Many degree distinctions (often lexical)

**Workflow for Highlands Languages**:
1. Annotate participant tracking (CRITICAL for switch-reference)
2. Annotate evidentiality (CRITICAL, grammatically obligatory)
3. Annotate dual number
4. Annotate temporal remoteness (TBTA time values)
5. Mark ergative contexts (animacy + agency + focus)
6. Identify serial verb contexts
7. Note elevation contexts

**Workflow for Non-Highlands TNG**:
- Same as above, but **skip evidentiality** (not grammatically obligatory)

---

### Example Languages

**Telefol (Ok-Oksapmin, Highlands)**:
- ✅ Evidentiality (CRITICAL, 5+ categories)
- ✅ Switch-reference (obligatory)
- ✅ Dual number (obligatory)
- ✅ Triple-indexing (subject, object, beneficiary on verb)
- ✅ Multiple past tenses
- ⚠️ Ergative case (optional)
- ❌ No articles, no gender

**Amele (Madang, lowlands)**:
- ✅ Switch-reference (obligatory)
- ✅ Multiple past tenses (6 distinctions)
- ✅ Dual number
- ⚠️ Serial verb constructions (productive)
- ⚠️ 32 possessive classes (most complex in TNG)
- ❌ No evidentiality (not in Highlands Area)
- ❌ No articles, no gender

**Warlpiri (Pama-Nyungan, AUSTRALIAN - included for comparison)**:
- Note: Not TNG, but similar features
- ✅ Free word order (but SOV basic)
- ✅ Ergative-absolutive case
- ✅ Dual number
- ⚠️ Paucal number
- ❌ No evidentiality

---

## 3. Indo-European (135 Languages)

### Overview

**Dataset Count**: 135 languages (13.4% of total)
**Geographic Distribution**: Europe, South Asia, Middle East, Americas (colonial spread)

**Major Branches in Dataset**:
- **Indo-Iranian**: 20 languages (Hindi, Urdu, Bengali, Persian, etc.)
- **Balto-Slavic**: 20 languages (Russian, Polish, Lithuanian, etc.)
- **Germanic**: 5 languages (English, German, Dutch, Swedish, Danish)
- **Italic (Romance)**: 6 languages (Spanish, French, Italian, Portuguese, Romanian, Latin)
- **Greek**: 1 language (Ancient Greek - Koine)
- **Celtic**: 1 language (Breton)
- **Albanian**: 1 language
- **Armenian**: 0 languages (none in current dataset)
- **Romani**: 2 languages

### Typological Profile

**Key Grammatical Features**:
- **Original system** (Proto-Indo-European):
  - 8 cases (nominative, accusative, genitive, dative, ablative, locative, instrumental, vocative)
  - 3 numbers (singular, dual, plural)
  - 3 genders (masculine, feminine, neuter)
  - Rich verbal morphology (person, number, tense, aspect, voice, mood)
- **Modern variation**: Ranges from highly conservative (Slavic, Baltic, Sanskrit) to highly analytic (English, Romance)

---

### ✅ CRITICAL Features for Indo-European

#### 1. **Case Systems** (Varies by Branch)

**Why Critical** (for some branches):
- **Slavic languages**: 6-7 cases (obligatory)
- **Baltic languages**: 7 cases (obligatory)
- **Sanskrit**: 8 cases (most conservative)
- **Germanic**: 4 cases (German) to essentially caseless (English)
- **Romance**: 0-2 cases (Romanian preserves 2, others lost all)

**Languages Affected**:
- **CRITICAL**: Slavic (7 languages), Baltic (1 language), Greek (1 language)
- **IRRELEVANT**: Romance (6 languages), English

**Annotation Strategy for High-Case Languages** (Slavic, Baltic, Greek):
- Preserve **Greek case distinctions**:
  - Nominative (subject)
  - Genitive (possession, partitive)
  - Dative (indirect object, beneficiary)
  - Accusative (direct object)
  - Vocative (direct address)
- These languages can express **Greek case nuances directly**
- **Advantage**: More precise than English translation

**Annotation Strategy for Low-Case Languages** (Romance, English):
- Collapse case distinctions
- Use **word order + prepositions** instead
- **Loss of nuance** inevitable

**Example** (Russian):
- Nominative: *книга* (kniga) "book" (subject)
- Genitive: *книги* (knigi) "of book"
- Dative: *книге* (knige) "to book"
- Accusative: *книгу* (knigu) "book" (object)
- Instrumental: *книгой* (knigoj) "with book"
- Prepositional/Locative: *книге* (knige) "about book"

---

#### 2. **Aspect Systems** (Slavic Branch)

**Why Critical**:
- **Slavic languages**: Aspect is **MORE fundamental than tense**
- **Obligatory perfective/imperfective distinction**
- Marked by:
  - Prefixes (*про-*, *на-*, *за-*, etc.)
  - Suffixes (*-ива-*, *-ва-*)
  - Suppletion (entirely different verb stems)

**Languages Affected**: Russian, Polish, Czech, Belarusian, Ukrainian, Croatian, Serbian, etc. (All Slavic languages in dataset)

**Annotation Strategy**:
- **Match Greek aspectual system**:
  - Greek **aorist** (perfective) → Slavic perfective
  - Greek **present/imperfect** (imperfective) → Slavic imperfective
  - Greek **perfect** (resultative) → Slavic perfective (with additional nuance)
- **Best match** among Indo-European languages for Greek aspect

**Example** (Russian):
- Imperfective: *читать* (čitat') "to read / be reading"
- Perfective: *прочитать* (pročitat') "to read (completely)"

**Translation Advantage**: Slavic can preserve **Greek aspectual distinctions** that English collapses.

---

#### 3. **Dual Number** (Slovene, Sorbian Only)

**Why Critical**:
- **Obligatory** in Slovene, Upper Sorbian, Lower Sorbian
- **Lost** in all other modern IE languages
- Marked on nouns, verbs, adjectives, pronouns

**Languages Affected**: Slovene (slv) ✓ in dataset, Sorbian (NOT in dataset)

**Annotation Strategy** (Slovene only):
- Mark all references to **exactly two entities** as Dual (D)
- Same as Austronesian/TNG dual (see Sections 1, 2)
- **Matches Greek NT dual forms** (rare but present)

**Example** (Slovene):
- Singular: *hiša* "house"
- Dual: *hiši* "two houses"
- Plural: *hiše* "houses (3+)"

**Translation Advantage**: Slovene can **perfectly preserve** Greek dual forms that all other IE languages must render as plural.

---

#### 4. **Ergativity** (Indo-Aryan Split Ergativity Only)

**Why Critical**:
- **Unique in Indo-European**: Indo-Aryan languages developed ergativity
- **Split ergativity**: Ergative in perfective aspects ONLY
- **Affected languages**: Hindi, Urdu, Marathi, Gujarati, Punjabi (Western Indo-Aryan)
- **NOT ergative**: Bengali, Odia (Eastern Indo-Aryan lost it)

**Pattern**:
- **Perfective transitive clause**:
  - Subject takes **ergative case** (marked with *-ne* in Hindi)
  - Verb agrees with **object** (not subject)
- **Imperfective/intransitive**:
  - Normal nominative-accusative alignment

**Annotation Strategy**:
- Mark **ergative contexts**:
  - Perfective aspect + transitive verb → Ergative subject
- **Verb agreement** shifts to object in ergative clauses

**Example** (Hindi):
- **Imperfective** (nominative-accusative):
  - *Rām kitāb paṛhtā hai* (Ram-NOM book-ACC reads)
  - "Ram reads the book"
  - Verb agrees with subject (masculine singular)

- **Perfective** (ergative-absolutive):
  - *Rām **ne** kitāb paṛhī* (Ram-**ERG** book-ABS read)
  - "Ram read the book"
  - Verb agrees with object (feminine singular, *kitāb* is feminine)

**Translation Challenge**: Greek is nominative-accusative. Must **reanalyze** agent-patient relationships for ergative constructions.

---

### ⚠️ RELEVANT Features for Indo-European

#### 5. **Gender Systems**

**Why Relevant**:
- **3 genders** (masculine, feminine, neuter) in:
  - Slavic, Baltic, Greek, German, Icelandic
- **2 genders** (masculine, feminine) in:
  - Romance (lost neuter)
- **No gender** in:
  - English (lost almost entirely)
  - Persian, Kurdish (Iranian branch)

**Annotation Strategy**:
- For **3-gender languages**: Preserve Greek gender distinctions
- For **2-gender languages**: Assign neuter nouns to masculine or feminine (theological implications!)
- For **genderless languages**: Ignore gender

**Theological Impact**:
- Greek πνεῦμα (pneuma, "spirit") is **neuter**
- Romance languages must choose masculine or feminine → Affects personhood of Holy Spirit

---

#### 6. **Tense vs. Aspect Prominence**

**Why Relevant**:
- **Aspect-prominent**: Slavic, Greek
- **Tense-prominent**: Germanic, Romance
- Different translation strategies needed

**Annotation Strategy**:
- **Aspect-prominent targets**: Emphasize TBTA aspect values
- **Tense-prominent targets**: Emphasize TBTA time values
- **Both required**, but prominence differs

**Example**:
- Greek aorist = **perfective aspect** (not just past tense)
- English typically renders with simple past (loses aspect)
- Russian renders with perfective verb (preserves aspect)

---

#### 7. **Negation - Genitive of Negation** (Slavic)

**Why Relevant**:
- **Unique Slavic feature**: Object changes case under negation
- Pattern: Accusative → Genitive in negative clauses

**Example** (Russian):
- Affirmative: *Я читаю **книгу*** (I read book-ACC)
- Negative: *Я не читаю **книги*** (I not read book-GEN)

**Annotation Strategy**:
- TBTA polarity marks negation
- **Add metadata** for case change in Slavic
- **Genitive of negation** = asymmetric negation (structural change under negation)

---

#### 8. **Articles** (Present in Some Branches)

**Why Relevant**:
- **Present**: Romance, Germanic, Greek, Celtic, Albanian
- **Absent**: Slavic, Baltic, most Indo-Iranian

**Annotation Strategy**:
- For languages **with articles**: Mark definiteness
- For languages **without articles**: Definiteness inferred from context
- **Slavic/Baltic more similar to Hebrew** (no articles)

---

### ❌ IRRELEVANT Features for Indo-European

#### 9. **Inclusive/Exclusive Pronouns**

**Why Irrelevant**:
- **Absent** in all Indo-European languages
- "We" is ambiguous (includes or excludes addressee?)

**Annotation Adjustment**:
- TBTA inclusive/exclusive distinctions **cannot be expressed** in IE languages
- Must use **context/paraphrase** to clarify if critical
  - "We (including you)" vs. "We (not including you)"

---

#### 10. **Trial, Quadrial, Paucal Numbers**

**Why Irrelevant**:
- **Dual** survives only in Slovene and Sorbian
- **Trial, Quadrial, Paucal** = entirely absent
- Expressed with numerals + plural instead

---

### 🔧 Special Considerations for Indo-European

#### Conservative vs. Analytic Spectrum

**Highly Conservative** (retain most PIE features):
- **Lithuanian**: 7 cases, pitch accent, archaic morphology
- **Slavic**: 6-7 cases, 3 genders, aspect-prominent
- **Greek**: 5 cases, rich verbal system
- **Sanskrit**: 8 cases (most conservative)

**Highly Analytic** (lost most inflection):
- **English**: Essentially no cases, no gender, minimal inflection
- **French**: Lost cases, minimal inflection, obligatory articles
- **Persian**: Lost gender, lost case, minimal inflection

**Translation Implication**: Conservative languages can **preserve Greek/Hebrew grammatical distinctions** that analytic languages must render periphrastically.

---

#### Word Order Flexibility

**Flexible word order** (due to case system):
- Slavic, Baltic, Greek: Can vary word order for **pragmatic emphasis**
- Matches Greek's pragmatic word order

**Rigid word order** (compensates for case loss):
- English, Romance: Fixed SVO order
- **Cannot** match Greek emphasis through word order

**Annotation Impact**:
- For flexible languages: Preserve **information structure** from Greek
- For rigid languages: Use **other devices** (cleft constructions, "it is X who...")

---

#### Celtic VSO Word Order

**Unique feature**: Celtic languages are **VSO** (Verb-Subject-Object)
- **Matches Hebrew** VSO/VOS
- **Differs from Greek** SVO

**Languages Affected**: Breton (bre) in dataset

**Annotation Impact**: Celtic word order **naturally matches Hebrew narrative** but requires restructuring for Greek.

---

### Common Translation Challenges

1. **Aspect in Germanic/Romance**
   - Germanic/Romance are **tense-prominent**
   - Greek **aspect-prominent**
   - **Solution**: Slavic preserves aspect perfectly; Germanic/Romance lose nuance

2. **Case System Loss**
   - English/Romance lost cases
   - Greek has 5 cases with semantic distinctions
   - **Solution**: Prepositions + word order, but some nuance lost

3. **Dual Number**
   - Only Slovene preserves dual
   - Greek occasionally uses dual
   - **Solution**: Slovene perfect match; others use plural

4. **Ergativity** (Indo-Aryan)
   - Greek is nominative-accusative
   - Hindi/Urdu have split ergativity
   - **Solution**: Analyze aspect (perfective → ergative)

5. **Gender Assignment**
   - 2-gender Romance must assign neuter nouns to M/F
   - Theological implications (πνεῦμα "spirit")

---

### Recommended Annotation Strategy

**For Slavic Languages** (HIGHEST PRESERVATION):
1. **Preserve case distinctions** (matches Greek)
2. **Preserve aspect** (perfective/imperfective)
3. Mark gender (3-way system)
4. No articles (similar to Hebrew)
5. **Best overall match** for Greek grammar

**For Germanic Languages**:
1. Collapse case distinctions (English has none)
2. Use tense-based rendering (aspect secondary)
3. Mark gender (German 3-way, English none)
4. Articles required (definite/indefinite)

**For Romance Languages**:
1. Collapse case distinctions (use prepositions)
2. Multiple past tenses (but tense, not aspect)
3. Gender: 2-way only (must choose for neuter)
4. Articles required

**For Indo-Aryan Languages**:
1. **CRITICAL**: Ergative marking in perfective
2. Aspect vs. tense (varies by language)
3. No articles (similar to Hebrew/Greek)
4. Case systems vary (2-8 cases)

**For Baltic Languages** (Lithuanian):
1. Preserve case distinctions (7 cases)
2. Mark gender (3-way)
3. No articles
4. Pitch accent (unique retention)

---

### Example Languages

**Russian (Slavic)**:
- ✅ 6 cases (high preservation of Greek)
- ✅ Aspect-prominent (perfective/imperfective matches Greek)
- ✅ 3 genders
- ✅ Genitive of negation (asymmetric)
- ❌ No articles (similar to Hebrew)
- ❌ No dual (lost)
- **BEST MATCH** for Greek grammar in IE family

**English (Germanic)**:
- ❌ No cases (except pronouns)
- ❌ Tense-prominent (loses Greek aspect)
- ❌ No grammatical gender (except pronouns)
- ✅ Articles (definite/indefinite)
- ❌ No dual
- **POOREST MATCH** for Greek grammar

**Hindi (Indo-Aryan)**:
- ✅ Split ergativity (UNIQUE, requires special handling)
- ⚠️ 2-3 cases (reduced from Sanskrit 8)
- ⚠️ 2 genders (masculine, feminine)
- ❌ No articles
- ❌ No dual
- **SPECIAL CASE**: Ergativity creates unique challenges

**Slovene (Slavic)**:
- ✅ 6 cases
- ✅ Aspect-prominent
- ✅ 3 genders
- ✅ **DUAL NUMBER** (ONLY modern IE language in dataset)
- ❌ No articles
- **UNIQUE**: Only IE language that can preserve Greek dual

**Spanish (Romance)**:
- ❌ No cases (lost all)
- ❌ Tense-prominent
- ⚠️ 2 genders (lost neuter, must choose for πνεῦμα)
- ✅ Articles required
- ❌ No dual
- ⚠️ Multiple past tenses (but not aspectual)

---

## 4. Niger-Congo (94 Languages)

### Overview

**Dataset Count**: 94 languages (9.3% of total)
**Geographic Distribution**: West, Central, East, and Southern Africa (22 countries)

**Major Subgroups in Dataset**:
- **Bantu** (Southern Bantoid, Benue-Congo): ~60 languages
  - East African: Swahili, Gikuyu, Ganda, Chichewa
  - Tanzania cluster: ~20 languages
  - Mozambique: ~6 languages
  - Central Africa: Lingala
  - Southern Africa: Several languages
  - Cameroon: ~4 languages
- **Atlantic (West Atlantic/Senegambian)**: ~8 languages
  - Fula/Fulfulde cluster: 4 languages
  - Wolof, Susu, others
- **Gur (Voltaic)**: ~12 languages (Burkina Faso, Ghana, Togo, Benin)
- **Kwa**: ~5 languages (Ghana, Côte d'Ivoire)
- **Mande**: ~4 languages (Mali, Guinea)
- **Benue-Congo (non-Bantu)**: ~15 languages
  - Defoid (Yoruba), Igboid, Edoid, Nupoid, etc.

### Typological Profile

**Key Grammatical Features**:
- **Noun class systems**: 3-25 classes with concordial agreement (most characteristic feature)
- **Tone**: Most languages are tonal (2-5 tone levels)
- **Serial verb constructions**: Very common, especially in West African languages
- **Aspect-prominent**: Aspect more basic than tense historically
- **Agglutinative morphology**: Bantu languages especially
- **SVO word order**: Dominant (except Ijoid = SOV, some Gur = VSO)

---

### ✅ CRITICAL Features for Niger-Congo

#### 1. **Noun Class Systems** (Bantu and Other Subgroups)

**Why Critical**:
- **Most characteristic feature** of Niger-Congo
- **Obligatory** class assignment for all nouns
- **Concord/agreement**: Determiners, adjectives, quantifiers, and often verbs agree with noun class
- Classes range from **3-25** depending on language

**Bantu Specifics**:
- Proto-Bantu: 19 classes (Meinhof classification: 22 total)
- Modern Bantu: 10-21 classes
  - Ganda: 21 classes (highest preservation)
  - Swahili: 15-18 classes
- Each class has **distinct singular/plural** markers

**Examples**:
- **Swahili** (Class 1/2 - people):
  - Singular: *m-tu* "person" (Class 1)
  - Plural: *wa-tu* "people" (Class 2)
  - Agreement: *m-tu **m**-refu* "tall person", *wa-tu **wa**-refu* "tall people"

- **Swahili** (Class 7/8 - objects):
  - Singular: *ki-tabu* "book" (Class 7)
  - Plural: *vi-tabu* "books" (Class 8)
  - Agreement: *ki-tabu **ki**-refu* "long book", *vi-tabu **vi**-refu* "long books"

**Annotation Strategy**:
- **Assign noun class** to every noun (beyond TBTA scope, requires language-specific metadata)
- **Critical for**:
  - God, Jesus, angels → Which class? (Theological implications)
  - Abstract concepts → Appropriate semantic class
  - Body parts → Typically dedicated class
  - Tools/instruments → Dedicated class
- **All modifiers** must agree with noun class

**Translation Challenge**: Greek/Hebrew don't have noun class systems. Translators must:
1. Assign every Biblical entity to an appropriate class
2. Ensure all concord throughout the text
3. Consider **semantic/cultural appropriateness** of class choice

---

#### 2. **Tone Systems**

**Why Critical**:
- **Most Niger-Congo languages are tonal**
- Tone levels: 2-5 (typically 2-3)
- Tone has **lexical** and **grammatical** functions:
  - Lexical: Different tones = different words
  - Grammatical: Tone marks tense, aspect, negation, definiteness

**Distribution**:
- **Tonal**: Bantu (most), Gur, Kwa, Adamawa-Ubangi, Kru
- **Non-tonal exceptions**: Swahili (Bantu), Fula/Fulfulde (Atlantic)

**Examples**:
- **Yoruba** (Benue-Congo): 3 tones (high, mid, low)
  - *igbá* (high-high) = "calabash"
  - *ìgbá* (low-high) = "garden egg"
  - *ìgbà* (low-low) = "time/season"

**Annotation Strategy**:
- **Written translations MUST mark tone** correctly
- Tonal errors → Wrong words, theological problems
- **Beyond TBTA**: Tone is phonological, not typically in TBTA
- **Concern**: Ensure source texts provide tonal information for annotators

**Translation Challenge**: Early Bible translations in African languages often **lacked tone marking** → Ambiguity, errors. Modern translations must mark tone accurately.

---

#### 3. **Serial Verb Constructions**

**Why Critical**:
- **Extremely common** in West African Niger-Congo languages
- **Defining feature** of SVCs:
  - Multiple verbs, single subject
  - Shared tense/aspect/mood/polarity
  - No coordination/subordination markers
  - Acts as single predicate

**Distribution**: Kwa (very common), Benue-Congo, Gur, Kordofanian, Mande, Atlantic, Ijoid

**Example** (Akan, Kwa):
- *Kofi de sekan no twaa abofra no* (Kofi take knife DEF cut child DEF)
- "Kofi cut the child with the knife"
- Two verbs: *de* "take" + *twaa* "cut" = serial construction

**Annotation Strategy**:
- **Unity of TAM**: All verbs in series share:
  - Same polarity (all affirmative or all negative)
  - Same tense/aspect marking
  - Same mood
- **Annotate each verb** individually in TBTA
- But recognize **semantic unity**

**Functions**:
- **Causative**: Using 'get'/'make' verb
- **Benefactive**: Using 'give' verb
- **Instrumental**: Using 'take' verb
- **Directional**: Motion verbs

**Translation Challenge**: Greek compound verbs may map to serial constructions. Biblical complex events may require verb serialization.

---

#### 4. **Aspect-Prominent TAM Systems**

**Why Critical**:
- **Aspect historically primary** in Niger-Congo
- Five widespread aspects:
  1. **Factative/Perfective** (completed)
  2. **Imperfective** (ongoing/habitual)
  3. **Perfect** (completed with present relevance)
  4. **Progressive** (ongoing at reference time)
  5. **Habitual/Iterative** (repeated/customary)

**Bantu Specifics**:
- "Verbal element is characteristically conflated to mark tense and aspect and more often than not, the morphemes marking tense and aspect cannot be isolated"
- Inseparable tense-aspect morphemes

**Annotation Strategy**:
- **Emphasize TBTA aspect values** over time values
- Bantu conflates tense+aspect → Both needed, but aspect primary
- Match **Greek aspectual system**:
  - Greek aorist (perfective) → Niger-Congo perfective
  - Greek present/imperfect (imperfective) → Niger-Congo imperfective

**Translation Challenge**: Greek aspect distinctions can be preserved, unlike in English (which loses aspect).

---

### ⚠️ RELEVANT Features for Niger-Congo

#### 5. **Negation - Multiple Strategies**

**Why Relevant**:
- **Extreme diversity** in negation strategies across Niger-Congo
- Bantu often uses **double/triple negation**:
  - Preverbal particle + verb suffix + clause-final particle
- **Tone changes** under negation common

**Example** (Kongo, Bantu):
- Triple negation: *ka* (preverbal) + verb *-a* (suffix) + *kó* (clause-final)

**Annotation Strategy**:
- Mark TBTA polarity (Affirmative/Negative)
- **Recognize multiple morphemes** may express single negation
- Tone changes (not in TBTA, but present in language)

---

#### 6. **Person/Number Marking**

**Why Relevant**:
- **Subject indexation** common (agreement markers on verb)
- **Object indexation** less common (restricted to topical/definite objects)
- **No grammatical gender** in personal pronouns for many languages
  - Third person pronouns encode **noun class**, not biological gender

**Annotation Strategy**:
- Person/number marking standard
- **Gender note**: Many languages lack masculine/feminine pronoun distinction
  - Greek ὁ/ἡ (he/she) may both → single 3rd person pronoun
  - Gender must be inferred from context, not grammar

---

#### 7. **Agglutinative Morphology** (Bantu)

**Why Relevant**:
- **"All Bantu languages are agglutinative"**
- Single word can encode:
  - Subject agreement
  - Tense/aspect
  - Object agreement
  - Verb root
  - Extensions (causative, applicative, reciprocal, passive)
  - Finality
- Example: Verb can = entire English clause

**Verb Extensions** (Critical for Bantu):
- **Causative** (*-is-* or *-y-*): Makes someone do action
- **Applicative** (*-il-* or *-el-*): Adds beneficiary or location
- **Reciprocal** (*-an-*): Mutual action
- **Passive** (*-w-*): Object → subject position

**Annotation Strategy**:
- Mark **semantic roles** (causative, benefactive, passive)
- Extensions stack in **specific order** (annotate each layer)

---

### ❌ IRRELEVANT Features for Niger-Congo

#### 8. **Dual, Trial, Quadrial, Paucal Numbers**

**Why Irrelevant**:
- **Absent** in Niger-Congo languages
- Only singular/plural distinction
- Expressed with numerals if needed

---

#### 9. **Ergative Case Systems**

**Why Irrelevant**:
- **Nominative-accusative** alignment (like Greek/Hebrew)
- No ergative-absolutive patterns

---

### 🔧 Special Considerations for Niger-Congo

#### Noun Class Assignment for Biblical Entities

**Critical Decisions**:

1. **God/Deity Class**
   - Which class for God?
   - Some languages have dedicated **deity class**
   - Others use **person class** (Class 1/2 in Bantu)
   - **Theological implications** of class choice

2. **Abstract Concepts**
   - "Faith," "hope," "love" → Which classes?
   - Abstract noun classes vary by language
   - Semantic appropriateness critical

3. **Body Parts**
   - Often dedicated class
   - Metaphorical uses ("body of Christ") must maintain class agreement

**Recommendation**: Consult **existing translations** in related languages for precedent. Class assignment decisions affect **entire translation**.

---

#### Tone + Negation Interaction

**Phenomenon**: Negation may **override lexical tone** on verbs with negative tone pattern.

**Implication**: Tonal transcription must account for **grammatical tone changes**, not just lexical tones.

---

#### Serial Verbs + Negation Unity

**Principle**: Entire serial verb construction shares **single polarity**.

**Example**:
- Affirmative: V1 + V2 + V3 + Object
- Negative: NEG + V1 + V2 + V3 + Object

All verbs marked "Negative" if series is negated.

---

### Common Translation Challenges

1. **Noun Class Assignment**
   - No precedent in source languages
   - **Solution**: Consult existing translations, semantic appropriateness

2. **Tonal Accuracy**
   - Source languages not tonal
   - **Solution**: Lexical databases with tone, native speaker validation

3. **Serial Verb Constructions**
   - Greek/Hebrew don't use SVCs the same way
   - **Solution**: Analyze event structure, choose appropriate serialization

4. **Aspect Conflation**
   - Bantu conflates tense+aspect inseparably
   - **Solution**: Both TBTA time and aspect values needed

5. **Locative Usage**
   - Bantu locative forms used questionably in early translations
   - **Solution**: Follow modern natural usage, not early translation precedent

---

### Recommended Annotation Strategy

**Priority Hierarchy**:

1. **HIGHEST PRIORITY**:
   - Noun class assignment (affects all concord)
   - Tone marking (lexical accuracy)
   - Aspect marking (grammatically primary)
   - Serial verb unity (TAM scope)

2. **HIGH PRIORITY**:
   - Agglutinative verb extensions (Bantu)
   - Negation strategies (multiple morphemes)
   - Participant tracking (affects agreement)

3. **MEDIUM PRIORITY**:
   - Tense distinctions (secondary to aspect)
   - Person/number agreement
   - Word order (mostly SVO)

4. **LOW PRIORITY**:
   - Gender (not in pronouns for most languages)
   - Dual/trial/paucal (absent)
   - Case systems (absent)

**Workflow for Bantu Languages**:
1. Assign noun class to every noun
2. Mark aspect (perfective/imperfective primary)
3. Identify serial verb constructions
4. Mark tone accurately (phonological, not TBTA)
5. Mark verb extensions (causative, applicative, etc.)
6. Mark negation (may involve multiple morphemes)
7. Ensure noun class concord throughout

**Workflow for West African Languages** (Kwa, Gur, Mande):
1. Identify serial verb constructions (CRITICAL)
2. Mark aspect (primary over tense)
3. Assign noun class (if applicable)
4. Mark tone (most are tonal)
5. Mark negation strategies
6. Participant tracking

---

### Example Languages

**Swahili (Bantu, East African)**:
- ✅ 15-18 noun classes (obligatory concord)
- ✅ Agglutinative verb morphology
- ✅ Aspect-prominent (perfective/imperfective)
- ❌ **Non-tonal** (unusual for Bantu)
- ❌ No serial verbs (not common in East African Bantu)
- ⚠️ No gender in pronouns (noun class instead)

**Yoruba (Benue-Congo, Defoid)**:
- ✅ Tonal (3 levels - CRITICAL)
- ✅ Serial verb constructions (common)
- ❌ No noun class system (Mande-like)
- ⚠️ 7 oral vowels, 5 nasal vowels
- ⚠️ SVO word order
- **Note**: Largest L1 speaker count in Niger-Congo

**Akan (Kwa)**:
- ✅ Serial verb constructions (very productive)
- ✅ Tonal (2 levels)
- ⚠️ Aspect/modality prominent over tense
- ❌ Limited noun class system
- ⚠️ Prefixes for verbal categories

**Wolof (Atlantic/Senegambian)**:
- ❌ **Non-tonal** (pitch-accent instead)
- ✅ Noun classes (8 singular, 2 plural)
- ✅ **Unique**: Pronouns conjugate, not verbs
- ⚠️ Implosive consonants (mb, nd)
- ⚠️ Consonant mutation

---

## 5. Otomanguean (69 Languages)

### Overview

**Dataset Count**: 69 languages (6.8% of total)
**Geographic Distribution**: Mesoamerica (Mexico: Oaxaca, Puebla, Guerrero, Veracruz states)

**Major Subgroups in Dataset**:
- **Zapotecan**: ~25 languages (Zapotec varieties)
- **Mixtecan**: ~15 languages (Mixtec varieties)
- **Popolocan**: ~10 languages (Popoloca, Mazatec, Ixcatec)
- **Chinantecan**: ~8 languages (Chinantec varieties)
- **Otopamean**: ~6 languages (Otomí varieties)
- **Amuzgoan**: ~2 languages
- **Tlapanec-Manguean**: ~2 languages
- **Cuicatecan**: ~2 languages

### Typological Profile

**Key Grammatical Features**:
- **Tone**: ALL Otomanguean languages are tonal (defining feature)
  - Oldest language family with evidence of tonal contrast in proto-language
  - 2-5 tone levels (3-tone systems most common)
  - Tone distinguishes **both lexical meaning AND grammatical categories**
- **Morphology**: Complex inflectional systems
  - Inflection encoded by: tone changes, affixes (prefixes/suffixes), and stem alternations
  - **"Some of the most complex inflection systems in the world"**
- **Aspect-oriented**: Aspect more relevant than tense
- **Word order**: VSO (verb-initial) predominant
- **Verb-centered**: Extensive marking on verbs

---

### ✅ CRITICAL Features for Otomanguean

#### 1. **Tone Systems** (UNIVERSAL AND CRITICAL)

**Why Critical**:
- **ALL Otomanguean languages are tonal**
- **Obligatory** for lexical and grammatical meaning
- Tone levels: 2-5 (3-tone most common)
  - 3 tones: Popolocan, Tlapanec, Amuzgo, Mixtecan, Zapotecan, Chinantecan
  - 2 tones: Oto-Pamean
  - 5 tones: Usila Chinantec (complex extreme)

**Functions of Tone**:
1. **Lexical**: Different tones = different words
2. **Inflectional**: Tone marks:
   - Tense/aspect
   - Person/number
   - Mood
   - Transitivity
3. **Derivational**: Tone creates new word forms

**Example** (Mazatec):
- Same consonants/vowels, different tones = different words
- Tone alone distinguishes word meanings

**Annotation Strategy**:
- **Tonal accuracy is CRITICAL**
- Incorrect tone → Wrong word, theological error
- **Beyond TBTA scope** (phonological), but **essential for translation**
- Source texts must provide **tonal transcription** for every word

**Translation Challenge**: Greek/Hebrew are **not tonal**. Annotators cannot rely on source language phonology. Must use:
- **Lexical databases** with tone marking
- **Native speaker validation**
- **Existing translations** for tonal precedent

---

#### 2. **Complex Inflectional Morphology**

**Why Critical**:
- **"Most complex inflection systems in the world"** (due to tone + affixes + stem changes all simultaneously marking single word)
- Inflection encodes:
  - Person/number of subject and object
  - Tense/aspect
  - Mood
  - Valency (transitive, intransitive, causative, inchoative, iterative)
- **Three simultaneous processes**:
  1. **Tone changes**: Different tonal pattern for different inflection
  2. **Affixation**: Prefixes/suffixes/proclitics/enclitics
  3. **Stem alternations**: Root changes

**Example Pattern**:
- Same root can have 50+ inflected forms
- Each form distinguished by **tone + affix + stem** combination

**Annotation Strategy**:
- **Mark all TAM categories** carefully (TBTA time, aspect, mood)
- **Mark person/number** for subject and object
- Recognize single word may encode **entire clause's worth of information**

**Translation Challenge**: Low-resource technology drastically underperforms for Otomanguean due to this complexity.

---

#### 3. **Aspect-Oriented Verb Systems**

**Why Critical**:
- **Aspect more relevant than tense**
- Valency and aspect marked by **prefixes/proclitics**:
  - Transitive, intransitive, causative, inchoative, iterative
  - Imperfective, perfective
- Person/number of subject/object marked by **suffixes/clitics**

**Annotation Strategy**:
- **Emphasize TBTA aspect values**:
  - Perfective/Imperfective primary
  - Inceptive (inchoative = beginning)
  - Routinely/Habitual (iterative)
- Time values secondary

**Translation Challenge**: Greek aspect system should map well, but tone + inflectional complexity creates implementation challenges.

---

#### 4. **VSO Word Order**

**Why Critical**:
- **Verb-Subject-Object** predominant
- Head-initial structure (like Celtic)

**Annotation Strategy**:
- **Matches Hebrew** VSO/VOS patterns
- **Differs from Greek** SVO
- Restructuring needed for Greek source texts

**Translation Advantage**: Otomanguean word order **naturally matches Hebrew narrative** style.

---

### ⚠️ RELEVANT Features for Otomanguean

#### 5. **Noun Classifiers**

**Why Relevant**:
- Some Otomanguean languages have classifiers
- Categories: human, familiar person, animate, house, fruit
- Not universal across family

**Annotation Strategy**:
- Where present: Mark classifier category
- Similar to Niger-Congo noun classes, but less elaborate

---

#### 6. **Head-Initial Structure**

**Why Relevant**:
- Noun modifiers (adjectives, articles) **follow the noun**
- Matches some Biblical patterns

---

### ❌ IRRELEVANT Features for Otomanguean

#### 7. **Grammatical Gender**

**Why Irrelevant**:
- Gender systems not characteristic of family
- No masculine/feminine/neuter distinction

---

#### 8. **Dual, Trial, Paucal Numbers**

**Why Irrelevant**:
- Not attested in Otomanguean
- Singular/plural distinction

---

#### 9. **Case Systems**

**Why Irrelevant**:
- No elaborate case marking
- Relationships encoded by word order and prepositions

---

### 🔧 Special Considerations for Otomanguean

#### Tone + Inflection Interaction

**Phenomenon**: Tone is **part of inflectional paradigm**, not just lexical.

**Implication**:
- Grammatical changes (aspect shift, person change) → **Tone changes**
- Cannot separate tone from grammar
- **Tonal accuracy essential** for grammatical correctness

---

#### Low-Resource Technology Challenge

**Problem**: "Models drastically underperform for Oto-Manguean languages due to complex inflection in stems, affixes, AND tonal changes all present in one word"

**Implication for Annotation**:
- **AI-assisted annotation** may be less reliable
- **Human validation** more critical than for other families
- **Lexical databases** essential

---

### Common Translation Challenges

1. **Tonal Accuracy**
   - No source language equivalent
   - **Solution**: Lexical databases, native speakers, existing translations

2. **Inflectional Complexity**
   - Single word = entire Greek/Hebrew clause
   - **Solution**: Analyze all morphological layers, mark each separately

3. **Aspect vs. Tense**
   - Greek aspect maps well, but tone complicates
   - **Solution**: Focus on aspect, mark tone correctly

4. **VSO Word Order**
   - Hebrew matches, Greek differs
   - **Solution**: Restructure Greek, preserve Hebrew order

5. **Low-Resource Context**
   - Limited technological support
   - **Solution**: Manual annotation, community involvement

---

### Recommended Annotation Strategy

**Priority Hierarchy**:

1. **HIGHEST PRIORITY**:
   - Tone marking (CRITICAL, affects meaning and grammar)
   - Aspect marking (grammatically primary)
   - VSO word order (obligatory)
   - Person/number (complex subject/object marking)

2. **HIGH PRIORITY**:
   - Valency distinctions (transitive/intransitive/causative/inchoative/iterative)
   - Inflectional layers (tone + affix + stem)
   - Participant tracking

3. **MEDIUM PRIORITY**:
   - Noun classifiers (where present)
   - Temporal distinctions (secondary to aspect)

4. **LOW PRIORITY**:
   - Gender (absent)
   - Case (not elaborate)
   - Dual/paucal (absent)

**Workflow**:
1. **Mark tone** for every word (phonological database essential)
2. Analyze inflectional paradigm (tone + affix + stem all matter)
3. Mark aspect (perfective/imperfective primary)
4. Mark person/number (subject and object)
5. Mark valency (transitive/causative/etc.)
6. Ensure VSO word order
7. Validate with native speakers (CRITICAL due to tone complexity)

---

### Example Languages

**Zapotec (Isthmus, Miahuatlán, etc.) - ~25 varieties**:
- ✅ Tonal (3 levels typically)
- ✅ VSO word order
- ✅ Aspect-prominent
- ✅ Complex tone + inflection interaction
- ⚠️ Extensive dialectal variation

**Mixtec (multiple varieties) - ~15 varieties**:
- ✅ Tonal (3 levels typically)
- ✅ VSO word order
- ✅ Complex inflection (tone + affix)
- ⚠️ High dialectal diversity

**Mazatec (Huautla, Jalapa de Díaz, etc.)**:
- ✅ Tonal (3-4 levels)
- ✅ Very complex tone system
- ✅ Aspect-oriented
- ✅ VSO

**Otomí (Eastern Highland, Mezquital, etc.)**:
- ✅ Tonal (2 levels - Oto-Pamean)
- ✅ Complex inflection
- ✅ VSO
- ⚠️ Simpler tone system than Mixtecan/Zapotecan

---

## 6. Mayan (41 Languages)

### Overview

**Dataset Count**: 41 languages (4.1% of total)
**Geographic Distribution**: Mesoamerica (Mexico, Guatemala, Belize, Honduras)

**Major Subgroups in Dataset**:
- **K'iche'an**: K'iche', Kaqchikel, Tz'utujil, Achi, Sakapultek, Uspanteko
- **Mamean**: Mam, Ixil, Awakateko, Tektiteko
- **Q'eqchi'an**: Q'eqchi'
- **Yucatecan**: Lacandon, Mopán Maya
- **Tzeltal-Tzotzil (Cholan-Tzeltalan)**: Tzotzil, Chol
- **Chujean**: Chuj, Akateko
- **Huastecan**: Huastec (Wastek)
- **Cholan**: Ch'orti', Chontal (Tabasco)
- **Jakalteko**

### Typological Profile

**Key Grammatical Features**:
- **Ergativity**: Morphologically ergative alignment (defining feature)
  - Syntactic ergativity also present (extraction constraints)
- **Polysynthetic**: Rich verbal morphology (both prefixes and suffixes)
- **Verb-initial**: VOS or VSO word order
- **Voice systems**: Multiple voice-changing operations (passive, antipassive)
- **Complex TAM**: Aspect, tense, mood all marked
- **Directional clitics**: Grammaticalized motion/direction

---

### ✅ CRITICAL Features for Mayan

#### 1. **Ergative-Absolutive Alignment**

**Why Critical**:
- **Defining feature** of Mayan languages
- **Morphologically ergative**:
  - Subject of intransitive verb (S) = Object of transitive verb (O) → **Absolutive** (Set B affixes)
  - Subject of transitive verb (A) → **Ergative** (Set A affixes)
- **Two sets of person affixes**:
  - **Set A (Ergative)**: Transitive subjects + possessors
  - **Set B (Absolutive)**: Intransitive subjects + transitive objects

**Example Pattern**:
- Intransitive: "I sleep" → Set B prefix (absolutive)
- Transitive: "I see you" → Set A prefix (ergative for "I") + Set B suffix (absolutive for "you")

**Annotation Strategy**:
- **Mark ergative vs. absolutive** contexts
- Greek/Hebrew are **nominative-accusative** → Must reanalyze:
  - Greek nominative (subject) → Mayan ergative (if transitive) or absolutive (if intransitive)
  - Greek accusative (object) → Mayan absolutive
- **Ergative critical** for:
  - Transitive verbs (all active constructions)
  - Possessors (Set A also marks possessors)

**Translation Challenge**: Complete realignment of grammatical relations. "Subject" in Greek ≠ "subject" in Mayan ergative system.

---

#### 2. **Syntactic Ergativity** (Extraction Constraints)

**Why Critical**:
- Beyond morphological ergativity, Mayan has **syntactic ergativity**
- **Constraints**:
  - Transitive subjects (ergative) **cannot be extracted** for:
    - Focus constructions
    - Interrogatives (questions)
    - Negation
    - Relativization
- **Solution**: Use **antipassive** voice to make transitive verb intransitive
  - Transitive subject → Intransitive subject (absolutive) → Now extractable

**Example**:
- Cannot focus transitive subject directly
- Must first antipassive the verb
- Then extract the now-absolutive subject

**Annotation Strategy**:
- **Mark contexts requiring extraction**:
  - Questions ("Who did X?")
  - Focus/emphasis ("It was X who did Y")
  - Relative clauses ("The one who did X")
- **Flag for antipassive** voice when transitive subject needs extraction

**Translation Challenge**: Greek word order and focus strategies don't have these constraints. Mayan requires **voice operations** that Greek doesn't signal.

---

#### 3. **Polysynthetic Verb Complex**

**Why Critical**:
- Verbs are **polysynthetic** with extensive morphology:
  - **Prefixes**: Aspect, absolutive agreement, directionals
  - **Root**: Verb stem
  - **Suffixes**: TAM, mood, plurality
- Single verb = entire clause in simpler languages

**Affix Order** (typical):
```
Aspect - Absolutive - (Directional) - ROOT - (Ergative) - TAM - Mood
```

**Example Pattern**:
- Intransitive: *Aspect-ABS-ROOT-TAM*
- Transitive: *Aspect-ABS-ROOT-ERG-TAM*

**Annotation Strategy**:
- **Mark all layers**:
  - Aspect (perfective/imperfective/etc.)
  - Person/number (Set A and Set B)
  - Directionals (if present)
  - TAM
  - Mood
- Recognize single word encodes many TBTA features

---

#### 4. **Voice Systems** (Passive, Antipassive, etc.)

**Why Critical**:
- Multiple voice-changing operations:
  - **Passive**: Agent demotion, patient promotion
  - **Antipassive**: Patient demotion, agent remains as intransitive subject
  - Proto-Mayan had at least one passive construction
  - Antipassive critical for extraction (see syntactic ergativity)

**Functions**:
- **Antipassive**: Allows focus/question/relative clause on transitive subject
- **Passive**: Downplay agent, promote patient

**Annotation Strategy**:
- Mark **voice**:
  - Active (default)
  - Passive
  - Antipassive
- **Antipassive required** for transitive subject extraction

**Translation Challenge**: Greek passive maps to Mayan passive. But Mayan **antipassive has no Greek equivalent** → Must be inferred from discourse context.

---

#### 5. **Directional Clitics**

**Why Critical**:
- Grammaticalized directional meanings
- Placement: After aspect/absolutive markers
- Position varies:
  - Before verb (intransitive)
  - Before ergative marker (transitive)

**Functions**:
- Motion toward/away
- Deictic orientation (toward speaker, away from speaker)
- Elevation changes (in some languages)

**Annotation Strategy**:
- **Mark directionality** in motion verbs
- **Biblical relevance**:
  - "Come" vs. "Go" (toward speaker vs. away)
  - "Ascend" vs. "Descend" (directional + elevation)

**Translation Challenge**: Greek motion verbs may not explicitly encode all directional nuances Mayan requires.

---

### ⚠️ RELEVANT Features for Mayan

#### 6. **Verb-Initial Word Order** (VOS/VSO)

**Why Relevant**:
- VOS or VSO (verb-initial) predominant
- **Matches Hebrew** VSO/VOS
- **Differs from Greek** SVO

**Annotation Strategy**:
- Restructure Greek for verb-initial order
- Hebrew order can be preserved more naturally

---

#### 7. **Complex TAM Systems**

**Why Relevant**:
- Aspect, tense, mood all marked
- Not as complex as some TNG or Otomanguean, but still rich

**Annotation Strategy**:
- Standard TBTA TAM annotation
- Mark all three categories (time, aspect, mood)

---

### ❌ IRRELEVANT Features for Mayan

#### 8. **Dual, Trial, Paucal Numbers**

**Why Irrelevant**:
- Singular/plural only
- No dual, trial, or paucal attested

---

#### 9. **Noun Class Systems**

**Why Irrelevant**:
- No Niger-Congo-style noun classes
- Classifiers exist (possessive, numeral), but not obligatory class assignment

---

### 🔧 Special Considerations for Mayan

#### Ergativity + Possession

**Phenomenon**: Set A (ergative) markers also mark **possessors**.

**Pattern**:
- Ergative subject = Set A prefix
- Possessor = Set A prefix
- **Same morphology**, different syntactic role

**Implication**: Must distinguish ergative (verb agreement) from possessive (noun marking) contexts.

---

#### Antipassive for Extraction

**Critical Rule**: Cannot extract transitive subjects without antipassive.

**Biblical Contexts**:
- "Who did X?" → If X is transitive subject, requires antipassive
- "It was Peter who did X" → If transitive, requires antipassive
- Relative clauses on transitive subjects → Antipassive

**Workflow**:
1. Identify extraction context (question, focus, relative)
2. Is extracted element a transitive subject?
3. If yes → Flag for antipassive voice
4. If no → No special marking needed

---

### Common Translation Challenges

1. **Ergative Alignment**
   - Greek nominative-accusative ≠ Mayan ergative-absolutive
   - **Solution**: Reanalyze grammatical relations
   - Transitive subjects → Ergative
   - Intransitive subjects → Absolutive
   - Objects → Absolutive

2. **Syntactic Ergativity**
   - Extraction constraints on transitive subjects
   - **Solution**: Use antipassive for focus/question/relative constructions

3. **Polysynthetic Verbs**
   - Single verb encodes clause
   - **Solution**: Mark all morphological layers (aspect, agreement, TAM, mood, directionals)

4. **Directional Clitics**
   - Greek motion verbs may not encode all directionality
   - **Solution**: Infer from context (toward/away, up/down)

5. **Verb-Initial Order**
   - Greek SVO must restructure
   - **Solution**: Hebrew VSO provides better model

---

### Recommended Annotation Strategy

**Priority Hierarchy**:

1. **HIGHEST PRIORITY**:
   - Ergative-absolutive alignment (obligatory)
   - Antipassive for extraction contexts (syntactic ergativity)
   - Polysynthetic verb layers (aspect, agreement, TAM, mood)
   - VOS/VSO word order (obligatory)

2. **HIGH PRIORITY**:
   - Directional clitics (grammaticalized)
   - Voice systems (passive, antipassive)
   - TAM marking (aspect, tense, mood)

3. **MEDIUM PRIORITY**:
   - Possession marking (Set A = ergative markers)
   - Participant tracking

4. **LOW PRIORITY**:
   - Gender (not present)
   - Dual/paucal (not present)
   - Noun classes (not elaborate)

**Workflow**:
1. Identify verb transitivity (transitive → ergative, intransitive → absolutive)
2. Mark Set A (ergative/possessor) and Set B (absolutive) agreement
3. Identify extraction contexts → Flag for antipassive if transitive subject
4. Mark aspect, tense, mood (all present)
5. Mark directional clitics
6. Ensure VOS/VSO word order
7. Mark voice (active, passive, antipassive)

---

### Example Languages

**K'iche' (K'iche'an, Guatemala)**:
- ✅ Ergative-absolutive (morphological + syntactic)
- ✅ Polysynthetic verbs
- ✅ VOS word order
- ✅ Antipassive for extraction
- ✅ Complex TAM
- ✅ Directional clitics

**Mam (Mamean, Guatemala)**:
- ✅ Ergative-absolutive
- ✅ VOS word order
- ✅ Polysynthetic
- ✅ Antipassive
- ⚠️ Directionals

**Q'eqchi' (Q'eqchi'an, Guatemala)**:
- ✅ Ergative-absolutive
- ✅ VSO word order (variation from VOS)
- ✅ Polysynthetic
- ✅ Complex TAM
- ⚠️ Directionals

**Yucatec (Yucatecan, Mexico) - Note: May not be in dataset, Lacandon/Mopán are**:
- ✅ Ergative-absolutive
- ✅ VOS word order
- ✅ Polysynthetic
- ✅ Tonal (unusual for Mayan)

---

## 7. Australian (36 Languages)

### Overview

**Dataset Count**: 36 languages (3.6% of total)
**Geographic Distribution**: Australia (various language families within continent)

**Note**: "Australian languages" refers to the diverse indigenous languages of Australia, not a single genetic family. Major families include:
- **Pama-Nyungan** (largest, covers most of continent)
- **Non-Pama-Nyungan** families (northern Australia)
- Some isolates

**Languages in Dataset**: Includes Warlpiri, Pitjantjatjara, Arrernte, Murrinh-Patha, and 32 others

### Typological Profile

**Key Grammatical Features**:
- **Free word order**: Many languages (especially Pama-Nyungan)
- **Ergative-absolutive case**: Very common (often split ergativity)
- **Rich case systems**: 4-8 cases typical
- **Kinship-influenced grammar**: Unique to Australian languages
  - Dual pronouns vary based on relationship between referents
  - Triangular kinship terms
- **Avoidance speech registers**: Special lexicon in presence of certain relatives
- **Paucal number**: Common (in addition to singular/plural)

---

### ✅ CRITICAL Features for Australian

#### 1. **Ergative-Absolutive Case Systems** (Often Split)

**Why Critical**:
- **Very common** in Australian languages
- Often **split ergativity**:
  - **Split by person/animacy**:
    - 1st/2nd person pronouns → Nominative-accusative
    - 3rd person → Ergative-absolutive
  - **Alternative split**:
    - Animate → Nominative-accusative
    - Inanimate → Ergative-absolutive

**Example Pattern** (Common Split):
- "I see you" (1st/2nd person) → Nominative-accusative alignment
- "He sees him" (3rd person) → Ergative-absolutive alignment

**Annotation Strategy**:
- **Identify split conditions**:
  - Person (1st/2nd vs. 3rd)
  - Animacy (human vs. non-human)
- Mark **ergative vs. absolutive** for applicable contexts
- Greek/Hebrew nominative-accusative must be reanalyzed (like Mayan)

**Languages Affected**: Majority of Australian languages in dataset

---

#### 2. **Free Word Order**

**Why Critical**:
- Many Australian languages feature **free word order**
- Syntactic coherence created by:
  - **Verb inflection** (person/number agreement)
  - **Noun case marking** (shows grammatical relations)
  - **NOT by word order** (unlike English)

**Implication**:
- Word order used for **pragmatic purposes** (focus, topic, emphasis)
- **NOT for grammatical role identification**

**Annotation Strategy**:
- **Cannot rely on word order** to determine subject/object
- Must use **case marking** instead
- **Information structure** determines order:
  - New information → Later in clause
  - Given information → Earlier in clause
  - Focus → Special position (varies by language)

**Translation Challenge**: Greek uses word order for pragmatics. Australian languages also use word order for pragmatics. But Greek has less flexible order (basic SVO), while Australian order is extremely flexible.

**Advantage**: Australian languages can **match Greek pragmatic word order** variations more easily than English can.

---

#### 3. **Paucal Number**

**Why Critical**:
- **Common** in Australian languages (uncommon globally)
- **Paucal** = "a few" (small, indefinite number)
- Typically: Singular, Dual, Paucal, Plural

**Examples**:
- **Warlpiri**: Has paucal number (attested in research)
- **Murrinh-Patha**: Paucal range ~10-15 (unusually large)
- **Warndarrang** (extinct): Paucal range ~5

**Annotation Strategy**:
- Use TBTA **Paucal (p)** value
- **Range varies by language**:
  - Typical: 3-5 (dual covers 2)
  - Murrinh-Patha: 10-15 (exceptional)
- **Context clues**:
  - "A few disciples" → Paucal
  - "Several people" → Paucal
  - "Many/all" → Plural

**Translation Challenge**: Greek/Hebrew don't distinguish paucal. Must infer from context:
- Explicit numerals (3-10 typically) → Paucal
- Quantifiers ("a few," "several") → Paucal
- Indefinite small groups → Paucal

---

#### 4. **Kinship-Influenced Grammar**

**Why Critical**:
- **Unique to Australian languages** ("seen nowhere else")
- Kinship relations **shape grammar**:
  - **Dual pronouns**: Distinct forms based on relationship between two referents
  - **Triangular terms**: Indicate relation of both speaker and listener to referent
    - Example (Warlpiri): "my mother who is also your father's sister"

**Annotation Strategy**:
- **Beyond TBTA scope** (requires kinship metadata)
- **Translation implication**:
  - Biblical kinship terms may need **specification** of relationship type
  - "Uncle" in English → Different words for:
    - Mother's brother
    - Father's brother
    - Mother's sister's husband
    - Father's sister's husband

**Example**: Western Desert languages distinguish:
- Mother's brother ≠ Father's brother (English "uncle" covers both)

**Translation Challenge**: Biblical languages have less specific kinship systems than Australian languages. Translators must **choose specific kinship term** where Biblical text uses general term.

---

#### 5. **Avoidance Speech Registers**

**Why Critical** (Culturally):
- Special speech registers used in presence of certain close relatives (e.g., mother-in-law)
- **Features**:
  - Share phonology and grammar with standard language
  - **Different lexicon** (restricted vocabulary)
  - Certain words taboo in avoidance context

**Annotation Strategy**:
- **Beyond TBTA scope** (sociolinguistic)
- **Translation implication**:
  - May need **multiple translations** of certain passages for different social contexts
  - Kinship scenes (e.g., Ruth and Boaz) may require avoidance register

**Example**: Cannot use certain words when mother-in-law is present (must use avoidance vocabulary).

---

### ⚠️ RELEVANT Features for Australian

#### 6. **Rich Case Systems**

**Why Relevant**:
- 4-8 cases typical
- **Case marking** shows grammatical relations (since word order doesn't)
- Cases include:
  - Ergative/Absolutive (or Nominative/Accusative for 1st/2nd person)
  - Dative
  - Locative
  - Instrumental
  - Ablative
  - Allative (toward)
  - Others

**Annotation Strategy**:
- Mark **case** for nouns (where applicable)
- Critical for understanding grammatical relations in free word order

---

#### 7. **Dual Number**

**Why Relevant**:
- Common (though paucal more distinctive)
- Dual = exactly two
- May vary based on **kinship relationship** between referents (unique feature)

**Annotation Strategy**:
- Mark Dual (D) for pairs
- Note kinship relationship if grammatically relevant

---

### ❌ IRRELEVANT Features for Australian

#### 8. **Grammatical Gender**

**Why Irrelevant**:
- **Absent** in most Australian languages
- No masculine/feminine/neuter

---

#### 9. **Tense Systems**

**Why Mostly Irrelevant**:
- Many Australian languages have **minimal tense distinctions**
- Temporal reference often inferred from context or marked lexically
- Aspect may be more relevant than tense

---

### 🔧 Special Considerations for Australian

#### Free Word Order + Case Marking

**Critical Principle**: **Case determines grammatical role, not word order**.

**Implication for Annotation**:
- Cannot use word order to identify subject/object
- Must rely on **case morphology**
- Pragmatic order varies freely

---

#### Split Ergativity Patterns

**Common Pattern**: 1st/2nd person pronouns use nominative-accusative, 3rd person uses ergative-absolutive.

**Implication**:
- Different alignment for different persons
- Must track **person** to determine correct case alignment

---

#### Kinship Untranslatability

**Challenge**: English kinship terms (uncle, aunt, cousin) have **no exact equivalents**.

**Solution**:
- Choose **specific kinship term** in target language
- May require **exegetical decision** about exact relationship

---

### Common Translation Challenges

1. **Ergativity** (Often Split)
   - Greek nominative-accusative ≠ Australian ergative (for 3rd person/inanimate)
   - **Solution**: Reanalyze grammatical relations based on person/animacy

2. **Free Word Order**
   - Cannot preserve Greek word order mechanically
   - **Solution**: Use case marking for roles, word order for pragmatics

3. **Paucal Number**
   - Greek/Hebrew don't distinguish "a few" grammatically
   - **Solution**: Infer from numerals and quantifiers

4. **Kinship Specificity**
   - Biblical languages have general terms, Australian languages require specific
   - **Solution**: Exegetical analysis of family relationships, choose appropriate specific term

5. **Avoidance Registers**
   - May need alternate lexicon for certain kinship contexts
   - **Solution**: Identify scenes requiring avoidance register, provide alternate vocabulary

---

### Recommended Annotation Strategy

**Priority Hierarchy**:

1. **HIGHEST PRIORITY**:
   - Ergative-absolutive marking (with split conditions)
   - Case marking (shows grammatical roles)
   - Paucal number (distinctive feature)
   - Free word order pragmatics (information structure)

2. **HIGH PRIORITY**:
   - Kinship relationships (affects grammar)
   - Dual number
   - Participant tracking (affects case agreement)

3. **MEDIUM PRIORITY**:
   - Aspect (more relevant than tense)
   - Temporal reference (often lexical, not grammatical)

4. **LOW PRIORITY**:
   - Tense (minimal in many languages)
   - Gender (absent)
   - Articles (absent)

**Workflow**:
1. Identify person and animacy (determines split ergativity)
2. Mark ergative/absolutive (or nominative/accusative for 1st/2nd person)
3. Mark case for all nouns
4. Identify paucal contexts (3-10 typically)
5. Mark dual for pairs
6. Analyze information structure (determines word order)
7. Note kinship relationships (may affect grammatical choices)
8. Identify avoidance register contexts (if applicable)

---

### Example Languages

**Warlpiri (Pama-Nyungan)**:
- ✅ Free word order (extremely flexible)
- ✅ Ergative-absolutive case
- ✅ Paucal number
- ✅ Dual number
- ✅ Kinship-influenced grammar (triangular terms)
- ❌ No gender
- **CRITICAL**: Case marking, not word order, shows grammatical relations

**Pitjantjatjara (Pama-Nyungan, Western Desert)**:
- ✅ Ergative-absolutive
- ✅ Free word order
- ✅ Split ergativity (likely)
- ✅ Specific kinship terms (mother's brother ≠ father's brother)
- ❌ No gender

**Murrinh-Patha (Non-Pama-Nyungan, Northern Australia)**:
- ✅ Paucal number (range ~10-15, unusual specificity)
- ✅ Complex verb morphology (Non-Pama-Nyungan polysynthesis)
- ✅ Ergative-absolutive case
- ✅ Free word order
- ❌ No gender

---

## 8. Afro-Asiatic Family (25 languages)

### Overview

The **Afro-Asiatic family** comprises 25 languages in our dataset, including major Biblical languages (Hebrew, Arabic, Aramaic). This family spans North Africa, the Horn of Africa, and the Middle East, with representation from the Semitic, Chadic, and Cushitic branches.

**Languages in dataset**: Arabic (Standard), Assyrian Neo-Aramaic, Coptic, Dangaléat, Dawro, Gamo, Gofa, Hamer-Banna, Hausa, Hdi, Hebrew (Ancient and Modern), Male, Mbuko, Merey, Muyang, Somali, Wolaytta

**Total languages**: 25

---

### Typological Profile

**Morphological type**: **Non-linear** (root-and-pattern, especially Semitic)

**Word order**: Varies by branch (Semitic typically VSO, Cushitic SOV/SVO, Chadic SVO)

**Distinctive features**:
- **Root-and-pattern morphology** (Semitic): consonantal roots with vowel patterns
- **Grammatical gender** (masculine/feminine)
- **Tonal in some branches** (Chadic, Cushitic, Omotic) but NOT Semitic/Berber
- **Gemination** (consonant lengthening) and vowel lengthening
- **VSO word order** (Semitic)

---

### ✅ CRITICAL Features for Afro-Asiatic

#### 1. **Root-and-Pattern Morphology** (SEMITIC ONLY)

**Why Critical**:
- Word meaning resides in **consonantal root** (typically 3 consonants)
- Vowel pattern (and affixes) modify meaning
- Example: Arabic K-T-B root (writing):
  - KiTaB = book
  - KaTaBa = to write
  - maKTuuB = fate ("that which is written")

**Implication for Annotation**:
- Cannot segment words linearly
- Must recognize **root** vs. **pattern**
- Related concepts share consonantal root
- Cross-referencing by root is critical

---

#### 2. **Grammatical Gender** (Masculine/Feminine)

**Why Critical**:
- Most Afro-Asiatic languages distinguish masculine/feminine
- Gender agreement throughout noun phrase and verb
- Exceptions: some Central Chadic languages lack gender

**Implication**:
- Mark gender on all nouns
- Track gender concord across sentence
- Greek/Hebrew gender may not match target language gender assignments

---

#### 3. **VSO Word Order** (SEMITIC)

**Why Critical**:
- Classical Hebrew, Classical Arabic, and related languages use **verb-initial** word order
- Differs from Greek (SVO) and English (SVO)

**Implication**:
- Cannot mechanically follow Greek word order
- Verb-fronting is natural, not emphatic
- Information structure may differ from Greek

---

#### 4. **Tone Systems** (CHADIC, CUSHITIC, OMOTIC ONLY)

**Why Critical** (for tonal branches):
- Tone is phonemic (changes word meaning)
- Chadic and Cushitic languages require tone marking
- Semitic and Berber are **NOT tonal**

**Implication**:
- For tonal languages: Mark tone on every syllable
- For Semitic languages: Irrelevant

---

### ⚠️ RELEVANT Features for Afro-Asiatic

#### 5. **Gemination and Vowel Lengthening**

**Why Relevant**:
- Consonant lengthening (gemination) common throughout family
- Vowel lengthening also frequent
- Both can be phonemic (change meaning)

**Implication**:
- Mark lengthening where phonemic
- Affects transliteration and phonology

---

#### 6. **Dual Number** (LIMITED)

**Why Relevant**:
- Classical Arabic has dual
- Modern spoken varieties often lost dual
- Hebrew has dual for paired body parts (hands, eyes)

**Implication**:
- Mark dual where present
- May need to distinguish dual from plural

---

#### 7. **Case Systems** (SEMITIC, LIMITED)

**Why Relevant**:
- Classical Arabic has case (nominative, accusative, genitive)
- Modern spoken varieties largely lost case
- Hebrew has construct state (genitive-like)

**Implication**:
- Mark case in literary varieties
- Construct state affects word order and meaning

---

### ❌ IRRELEVANT Features for Afro-Asiatic

#### 8. **Inclusive/Exclusive Pronouns**

**Why Irrelevant**:
- Not a feature of Afro-Asiatic languages

---

#### 9. **Switch-Reference**

**Why Irrelevant**:
- Not present in Afro-Asiatic

---

#### 10. **Evidentiality**

**Why Irrelevant**:
- No grammaticalized evidential systems in Afro-Asiatic

---

### 🔧 Special Considerations for Afro-Asiatic

#### Non-Linear Morphology (Semitic)

**Critical Principle**: **Roots are consonantal; patterns add grammatical meaning**.

**Example**:
- Arabic root: K-T-B (writing)
- Pattern CaCaCa (active perfect) → KaTaBa (he wrote)
- Pattern CuCiCa (passive perfect) → KuTiBa (it was written)
- Pattern maCCaC (place) → maKTaB (office, place of writing)

**Implication for Annotation**:
- Cannot treat words as linear sequences of morphemes
- Must identify **root** + **pattern** + **affixes**
- Related concepts (semantically) share root

---

#### Gender Asymmetry with Greek/Hebrew

**Challenge**: Target language gender assignments may differ from source.

**Example**:
- Greek "pneuma" (spirit) = neuter
- Arabic "rūḥ" (spirit) = feminine
- Hebrew "rūaḥ" (spirit) = feminine

**Solution**:
- Use target language gender
- Note mismatches where they affect agreement

---

#### VSO Word Order in Translation

**Challenge**: Greek SVO order differs from Semitic VSO.

**Solution**:
- Use natural VSO order in Semitic target languages
- Verb-fronting is unmarked, not emphatic

---

### Common Translation Challenges

1. **Root-and-Pattern Morphology** (Semitic)
   - Greek/Hebrew words segment linearly; Arabic uses interdigitated roots/patterns
   - **Solution**: Identify consonantal root, apply appropriate pattern

2. **Gender Agreement**
   - Greek neuter has no equivalent in most Afro-Asiatic languages
   - **Solution**: Assign masculine or feminine based on semantic category

3. **VSO Word Order** (Semitic)
   - Greek word order cannot be preserved mechanically
   - **Solution**: Use natural VSO order; adjust only for marked information structure

4. **Tone** (Chadic, Cushitic)
   - Greek/Hebrew have no tone; target language requires tone assignment
   - **Solution**: Analyze semantic context to determine appropriate tone contour

5. **Construct State** (Hebrew-like)
   - Genitive relationships expressed through word order and vowel changes
   - **Solution**: Use construct state for possession/attribution

---

### Recommended Annotation Strategy

**Priority Hierarchy**:

1. **HIGHEST PRIORITY**:
   - Root-and-pattern morphology (Semitic)
   - Grammatical gender (masculine/feminine)
   - VSO word order (Semitic)
   - Tone systems (Chadic, Cushitic, Omotic)

2. **HIGH PRIORITY**:
   - Gemination and vowel lengthening
   - Dual number (where present)
   - Case systems (Classical Arabic, Hebrew construct)

3. **MEDIUM PRIORITY**:
   - Verb conjugation (person, number, gender)
   - Tense/Aspect (varies by language)

4. **LOW PRIORITY**:
   - Features absent from Afro-Asiatic (switch-reference, evidentiality, etc.)

**Workflow**:
1. Identify branch (Semitic, Chadic, Cushitic, Omotic)
2. For Semitic: Extract consonantal root + vowel pattern
3. Mark grammatical gender on all nouns
4. For Chadic/Cushitic: Mark tone on every syllable
5. Use VSO word order for Semitic languages
6. Mark gemination and vowel lengthening where phonemic
7. Mark dual number (if present)
8. Mark case (if present in literary varieties)

---

### Example Languages

**Classical Hebrew (Semitic)**:
- ✅ Root-and-pattern morphology (tri-consonantal roots)
- ✅ VSO word order (verb-initial)
- ✅ Grammatical gender (masculine/feminine)
- ✅ Dual number (limited: paired body parts)
- ✅ Construct state (genitive)
- ❌ No tone
- **CRITICAL**: Root extraction and pattern analysis

**Arabic (Semitic)**:
- ✅ Root-and-pattern morphology (most developed)
- ✅ VSO word order
- ✅ Grammatical gender
- ✅ Dual number (Classical; often lost in modern spoken varieties)
- ✅ Case system (Classical: nom/acc/gen)
- ❌ No tone
- **CRITICAL**: Root-and-pattern, gender agreement, VSO order

**Hausa (Chadic)**:
- ✅ Tone system (2-3 tones, phonemic)
- ✅ Grammatical gender (masculine/feminine)
- ✅ SVO word order (differs from Semitic)
- ⚠️ Aspect-prominent (not tense-prominent)
- ❌ No root-and-pattern morphology (Chadic ≠ Semitic)
- **CRITICAL**: Tone marking, gender, aspect

**Somali (Cushitic)**:
- ✅ Tone system (2 tones)
- ✅ Grammatical gender (masculine/feminine)
- ✅ SOV word order
- ✅ Case system (nominative/absolutive/genitive)
- ❌ No root-and-pattern morphology
- **CRITICAL**: Tone, gender, case, SOV word order

---

## 9. Sino-Tibetan Family (18 languages)

### Overview

The **Sino-Tibetan family** comprises 18 languages in our dataset, spanning East Asia, Southeast Asia, and South Asia. This family is one of the world's most structurally diverse, ranging from highly isolating (analytic) languages like Mandarin Chinese to polysynthetic languages like Kiranti and Gyalrongic.

**Languages in dataset**: Burmese, Chin (Eastern Khumi, Matu, Siyin, Thado, Thaiphum, Zyphe), Chinese (Mandarin), Limbu, Sunwar, Tamang (Eastern), Zaiwa

**Total languages**: 18

---

### Typological Profile

**Morphological type**: **Highly variable** (isolating to polysynthetic)
- **Isolating**: Chinese, Burmese (minimal inflection)
- **Polysynthetic**: Gyalrongic, Kiranti (complex verb morphology)

**Word order**: **Mostly SOV** (except Chinese, Bai, Karenic, Mruic which are SVO/VSO)

**Distinctive features**:
- **Tone systems** (most languages, 2-9 tones)
- **Classifier systems** (Chinese, Burmese, not Tibetan)
- **Monosyllabic words** (vast majority)
- **Analytic grammar** (especially Sinitic, Lolo-Burmese)
- **Word order conveys grammatical relations** (not morphology, in analytic branches)

---

### ✅ CRITICAL Features for Sino-Tibetan

#### 1. **Tone Systems**

**Why Critical**:
- Most Sino-Tibetan languages are tonal
- Tone is **phonemic** (changes word meaning)
- Number of tones varies:
  - Tibetan: 2 tones
  - Burmese: 3 tones
  - Mandarin Chinese: 4 tones
  - Cantonese: up to 9 tones

**Implication for Annotation**:
- Mark tone on every syllable
- Tonal errors change meaning entirely
- Greek/Hebrew lack tone; must infer from semantic context

---

#### 2. **Classifier Systems** (CHINESE, BURMESE)

**Why Critical**:
- Nouns are typically **collective terms** (refer to all members of class)
- To count or modify with demonstrative, must use **classifier**
- Classifier = specific counter for semantic category
- Example (Mandarin):
  - 三本书 (sān běn shū) = three [CLASSIFIER-flat-things] book = "three books"
  - 三只狗 (sān zhī gǒu) = three [CLASSIFIER-animals] dog = "three dogs"

**Implication**:
- Cannot directly translate numbers without classifiers
- Must choose appropriate classifier for noun category
- Semantic knowledge required

**NOTE**: Classifiers **absent in Tibetan**, appear late in Burmese and Chinese.

---

#### 3. **Analytic Grammar** (ISOLATING BRANCHES)

**Why Critical**:
- Languages like Chinese and Burmese rely heavily on **word order**, not morphology
- Few or no inflections
- Grammatical relations shown by position, not case/agreement

**Implication**:
- Word order changes = meaning changes
- Cannot rearrange words freely
- Must preserve grammatical word order

---

#### 4. **Monosyllabic Words**

**Why Critical**:
- Vast majority of morphemes are monosyllabic
- Complex ideas expressed through **multi-word compounds**
- Example (Mandarin): 电脑 (diàn-nǎo) = electric-brain = "computer"

**Implication**:
- Long Greek compounds may require multi-word expressions
- Single-syllable morphemes combine to form complex meanings

---

#### 5. **SOV vs. SVO Word Order**

**Why Critical**:
- Most Sino-Tibetan languages are **SOV** (verb-final)
- BUT Chinese, Bai, Karenic, Mruic are **SVO** (verb-medial)
- Different word order = different parsing strategy

**Implication**:
- Know which branch your language belongs to
- Use appropriate word order consistently
- Greek SVO order may match Chinese but not most Sino-Tibetan

---

### ⚠️ RELEVANT Features for Sino-Tibetan

#### 6. **Aspect Systems**

**Why Relevant**:
- Sino-Tibetan languages tend to mark **aspect** more than tense
- Perfective vs. imperfective often grammaticalized

**Implication**:
- Focus on aspect distinctions
- Tense may be inferred from context

---

#### 7. **Serial Verb Constructions**

**Why Relevant**:
- Multiple verbs in sequence without conjunctions
- Common in many Sino-Tibetan languages

**Implication**:
- Complex events may require serial verbs
- Cannot always use Greek conjunctions

---

#### 8. **Topic-Comment Structure**

**Why Relevant**:
- Many Sino-Tibetan languages are topic-prominent (not subject-prominent)
- Topic marked by position or particle

**Implication**:
- Information structure differs from Greek
- Topic ≠ subject

---

### ❌ IRRELEVANT Features for Sino-Tibetan

#### 9. **Grammatical Gender**

**Why Irrelevant**:
- Sino-Tibetan languages do not distinguish gender

---

#### 10. **Case Systems**

**Why Irrelevant** (for isolating branches):
- Analytic languages like Chinese have no case morphology
- **Exception**: Polysynthetic branches (Gyalrongic, Kiranti) may have case

---

#### 11. **Number Distinctions** (Beyond Singular/Plural)

**Why Mostly Irrelevant**:
- Dual, trial, paucal generally absent
- Plurality often optional or unmarked

---

### 🔧 Special Considerations for Sino-Tibetan

#### Structural Diversity

**Critical Principle**: **Sino-Tibetan is one of the world's most structurally diverse families**.

**Range**:
- **Isolating**: Chinese, Burmese (minimal morphology)
- **Polysynthetic**: Gyalrongic, Kiranti (complex verb morphology)

**Implication**:
- Must know which branch your language belongs to
- Annotation strategy varies dramatically by branch

---

#### Classifiers Require Semantic Knowledge

**Challenge**: Choosing correct classifier requires knowing semantic category of noun.

**Example (Mandarin)**:
- 一条鱼 (yī tiáo yú) = one [CLASSIFIER-long-flexible] fish
- 一本书 (yī běn shū) = one [CLASSIFIER-flat-object] book
- 一只鸟 (yī zhī niǎo) = one [CLASSIFIER-small-animal] bird

**Solution**:
- Learn classifier inventory for target language
- Analyze noun semantics to choose appropriate classifier

---

#### Word Order = Grammar

**Critical Principle**: In analytic Sino-Tibetan languages, **word order is grammar**.

**Implication**:
- Changing word order changes meaning
- Subject-Verb-Object in Chinese is rigid
- Cannot rearrange for stylistic purposes without changing meaning

---

### Common Translation Challenges

1. **Tone Assignment**
   - Greek/Hebrew lack tone; Sino-Tibetan requires tone on every syllable
   - **Solution**: Analyze semantic context to determine meaning, then assign appropriate tone

2. **Classifier Selection**
   - Greek/Hebrew lack classifiers; Chinese/Burmese require classifier for counting
   - **Solution**: Analyze noun semantics, choose appropriate classifier

3. **Analytic Grammar**
   - Greek has rich morphology; Chinese relies on word order
   - **Solution**: Express grammatical relations through position, not inflection

4. **Monosyllabic Constraint**
   - Greek compound words may have no single-word equivalent
   - **Solution**: Use multi-word compounds

5. **Topic-Prominence**
   - Greek is subject-prominent; many Sino-Tibetan languages are topic-prominent
   - **Solution**: Restructure sentences to foreground topic (may differ from subject)

---

### Recommended Annotation Strategy

**Priority Hierarchy**:

1. **HIGHEST PRIORITY**:
   - Tone systems (mark every syllable)
   - Classifier systems (choose appropriate classifier)
   - Word order (SOV vs. SVO)
   - Analytic grammar (word order = grammatical relations)

2. **HIGH PRIORITY**:
   - Aspect systems (perfective/imperfective)
   - Serial verb constructions
   - Topic-comment structure

3. **MEDIUM PRIORITY**:
   - Monosyllabic structure (compound formation)

4. **LOW PRIORITY**:
   - Gender (absent)
   - Case (absent in analytic branches)
   - Number distinctions beyond singular/plural

**Workflow**:
1. Identify branch (isolating vs. polysynthetic, Sinitic vs. Tibeto-Burman)
2. Mark tone on every syllable
3. For Chinese/Burmese: Choose appropriate classifier for counts and demonstratives
4. Use correct word order (SOV or SVO)
5. Express grammatical relations through word order (analytic branches)
6. Mark aspect (perfective/imperfective)
7. Identify topic vs. subject
8. Use serial verbs where appropriate

---

### Example Languages

**Mandarin Chinese (Sinitic, Isolating)**:
- ✅ 4-tone system (phonemic)
- ✅ Classifier system (obligatory for counting)
- ✅ SVO word order (exception among Sino-Tibetan)
- ✅ Analytic grammar (minimal inflection)
- ✅ Monosyllabic morphemes
- ✅ Topic-prominent
- ❌ No gender
- ❌ No case
- ❌ No number agreement
- **CRITICAL**: Tone, classifiers, word order, topic-prominence

**Burmese (Lolo-Burmese, Isolating)**:
- ✅ 3-tone system
- ✅ Classifier system
- ✅ SOV word order (verb-final)
- ✅ Analytic grammar
- ✅ Monosyllabic tendency
- ❌ No gender
- **CRITICAL**: Tone, classifiers, SOV order

**Limbu (Kiranti, Polysynthetic)**:
- ⚠️ Tone (may have tone or not, varies by dialect)
- ✅ SOV word order
- ✅ Complex verb morphology (polysynthetic)
- ✅ Person/number agreement on verb
- ❌ No classifiers (unlike Chinese)
- **CRITICAL**: Verb morphology, SOV order, agreement

**Tamang (Bodic/Tibetic, Moderately Synthetic)**:
- ✅ Tone system (2 tones in some dialects)
- ✅ SOV word order
- ⚠️ Moderate morphology
- ❌ No classifiers
- **CRITICAL**: Tone (if present), SOV order

---

## 10. Quechuan Family (18 languages)

### Overview

The **Quechuan family** comprises 18 languages in our dataset, spread across the Andean region of South America (Peru, Bolivia, Ecuador, Colombia, Argentina, Chile). Quechua is known for its highly agglutinative morphology and obligatory evidentiality system.

**Languages in dataset**: Inga, Quechua (Cajamarca, Eastern Apurímac, Huallaga, Huamalíes-Dos de Mayo Huánuco, Huaylas Ancash, Huaylla Wanca, Lambayeque, Margos-Yarowilca-Lauricocha, North Bolivian, North Junín, Northern Conchucos Ancash, Panao, San Martín, South Bolivian, Southern Conchucos), Quichua (Northern Pastaza, Southern Pastaza)

**Total languages**: 18

---

### Typological Profile

**Morphological type**: **Highly agglutinative**
- Words built from roots + multiple suffixes
- Each suffix carries one meaning
- Very regular (not fusional)
- Single words can express complex ideas

**Word order**: **SOV** (verb-final)

**Distinctive features**:
- **THREE-TERM EVIDENTIAL SYSTEM** (direct/reported/inferred) — **MOST DISTINCTIVE FEATURE**
- **Bipersonal conjugation** (verb agrees with subject AND object)
- **Topic particles**
- **Benefactive suffixes** (who benefits from action)
- **Attitudinal suffixes** (speaker's attitude toward action)

---

### ✅ CRITICAL Features for Quechuan

#### 1. **Evidentiality** (THREE-TERM SYSTEM)

**Why Critical**:
- **Obligatory grammatical category** in Quechua
- Speakers must indicate **source of information**:
  - **-mi** (direct evidence): "I saw it myself"
  - **-si** (reported evidence): "I heard it from someone"
  - **-cha** (inferred evidence): "I infer it"
- Evidentials are **second position enclitics** (attach to first constituent)
- NOT a grammatical requirement in Greek, Hebrew, or English

**Example**:
- Paymi hamushan. = "He is coming (I see him)."
- Paysi hamushan. = "He is coming (I was told)."
- Paycha hamushan. = "He is coming (I infer from evidence)."

**Implication for Annotation**:
- Must analyze **source of knowledge** for every statement
- Narrative passages: usually direct evidence (witnessed)
- Reported speech: reported evidence
- Prophecy/inference: inferred evidence
- **Cannot leave evidentiality unmarked**

---

#### 2. **Agglutinative Morphology**

**Why Critical**:
- Quechua words can be **very long** with multiple suffixes
- Each suffix adds one meaning
- Regular and predictable (unlike fusional languages)
- Example: Wasi-y-ku-nchis-man = house-1SG.POSS-PLURAL-1PL.INCL-ALLATIVE = "to our (incl.) houses"

**Implication**:
- Cannot translate word-for-word
- Must analyze morpheme-by-morpheme
- Single Quechua word may equal entire Greek phrase

---

#### 3. **Bipersonal Conjugation**

**Why Critical**:
- Verbs agree with **both subject and object**
- Both marked on verb simultaneously
- Example: Riku-wa-nki = see-1SG.OBJ-2SG.SUBJ = "You see me"

**Implication**:
- Must mark both participants on verb
- Object pronouns often omitted (incorporated into verb)

---

#### 4. **Topic Particles**

**Why Critical**:
- Topic marked with particles (e.g., **-qa**)
- Topic ≠ subject
- Information structure differs from Greek

**Implication**:
- Identify topic (what sentence is about)
- May differ from Greek subject

---

#### 5. **Attitudinal and Benefactive Suffixes**

**Why Critical**:
- Speaker's attitude grammatically encoded
- Benefactive shows who benefits from action
- Not expressed grammatically in Greek

**Implication**:
- Must infer speaker attitude from context
- Identify beneficiaries of actions

---

### ⚠️ RELEVANT Features for Quechuan

#### 6. **SOV Word Order**

**Why Relevant**:
- Quechua is consistently SOV (verb-final)
- Greek is SVO
- Cannot preserve Greek word order

---

#### 7. **Switch-Reference** (SOME VARIETIES)

**Why Relevant**:
- Some Quechua varieties have switch-reference systems
- Marks whether subject changes across clauses

---

#### 8. **Aspect Systems**

**Why Relevant**:
- Quechua marks aspect (progressive, habitual, etc.)
- Tense less prominent than aspect

---

### ❌ IRRELEVANT Features for Quechuan

#### 9. **Grammatical Gender**

**Why Irrelevant**:
- Quechua lacks grammatical gender

---

#### 10. **Number Beyond Singular/Plural**

**Why Irrelevant**:
- No dual, trial, paucal distinctions
- Only singular vs. plural

---

#### 11. **Case Systems** (BEYOND BASIC)

**Why Mostly Irrelevant**:
- Quechua has case suffixes (nominative, accusative, genitive, etc.)
- But system is regular and agglutinative, not complex like Russian

---

### 🔧 Special Considerations for Quechuan

#### Evidentiality is Obligatory

**Critical Principle**: **Every statement must be marked for evidentiality**.

**Challenge**: Greek and Hebrew do not grammaticalize evidentiality.

**Solution**:
- **Narrative**: Usually direct evidence (narrator witnessed or presents as witnessed)
- **Reported speech**: Use reported evidential (-si)
- **Prophecy**: Inferred or direct (depending on theology)
- **Miracles seen**: Direct evidential
- **Miracles reported**: Reported evidential

---

#### Agglutinative vs. Fusional

**Critical Difference**:
- Greek = fusional (one morpheme carries multiple meanings)
- Quechua = agglutinative (one morpheme = one meaning)

**Example**:
- Greek: λύω (lýō) = "I loose" (person, number, tense, mood, voice all in one ending)
- Quechua: riku-ni = see-1SG = "I see" (each suffix adds one meaning)

**Implication**:
- Quechua requires multiple suffixes for what Greek expresses in one ending

---

#### Topic-Prominence

**Challenge**: Quechua is topic-prominent; Greek is subject-prominent.

**Solution**:
- Identify **topic** (what sentence is about)
- Topic ≠ subject
- Mark topic with -qa

---

### Common Translation Challenges

1. **Evidentiality**
   - Greek lacks evidentiality; Quechua requires it
   - **Solution**: Analyze narrative perspective (witnessed, reported, inferred)

2. **Agglutinative Morphology**
   - Greek fusional endings ≠ Quechua agglutinative suffixes
   - **Solution**: Break down Greek morphology into separate Quechua suffixes

3. **Bipersonal Conjugation**
   - Greek marks subject on verb; Quechua marks subject AND object
   - **Solution**: Add object markers to verb

4. **Topic-Comment Structure**
   - Greek subject-prominent; Quechua topic-prominent
   - **Solution**: Identify topic, mark with -qa

5. **Attitudinal Suffixes**
   - Greek does not grammaticalize speaker attitude; Quechua does
   - **Solution**: Infer attitude from context (certainty, surprise, etc.)

---

### Recommended Annotation Strategy

**Priority Hierarchy**:

1. **HIGHEST PRIORITY**:
   - Evidentiality (direct/reported/inferred)
   - Agglutinative morphology (multiple suffixes)
   - Bipersonal conjugation (subject + object on verb)
   - Topic marking (-qa)

2. **HIGH PRIORITY**:
   - Attitudinal suffixes (speaker attitude)
   - Benefactive suffixes (who benefits)
   - SOV word order (verb-final)

3. **MEDIUM PRIORITY**:
   - Aspect systems (progressive, habitual)
   - Switch-reference (if present)

4. **LOW PRIORITY**:
   - Gender (absent)
   - Number distinctions beyond singular/plural (absent)

**Workflow**:
1. Analyze **evidentiality**: direct, reported, or inferred?
2. Identify **topic** (mark with -qa)
3. Mark **bipersonal conjugation** (subject + object on verb)
4. Build agglutinative word structure (root + multiple suffixes)
5. Add **attitudinal suffixes** (speaker certainty, surprise, etc.)
6. Add **benefactive suffixes** (who benefits from action)
7. Use **SOV word order** (verb-final)
8. Mark aspect (progressive, habitual, etc.)

---

### Example Languages

**South Bolivian Quechua**:
- ✅ Three-term evidential system (-mi/-si/-cha)
- ✅ Highly agglutinative
- ✅ Bipersonal conjugation
- ✅ Topic marking (-qa)
- ✅ Attitudinal suffixes
- ✅ Benefactive suffixes
- ✅ SOV word order
- ❌ No gender
- ❌ No dual/trial/paucal
- **CRITICAL**: Evidentiality, agglutination, bipersonal agreement, topic-prominence

**Inga (Colombian Quechua)**:
- ✅ Evidential system
- ✅ Agglutinative
- ✅ Bipersonal conjugation
- ✅ SOV word order
- **CRITICAL**: Evidentiality, agglutination

**Northern Pastaza Quichua (Ecuador)**:
- ✅ Evidential system
- ✅ Agglutinative
- ✅ Bipersonal conjugation
- ✅ Topic marking
- ✅ SOV word order
- **CRITICAL**: Evidentiality, agglutination, topic-prominence

---

---

# Cross-Family Comparison Tables

## Table 1: Number Systems

| Family | Singular | Dual | Trial | Paucal | Plural | Notes |
|--------|----------|------|-------|--------|--------|-------|
| **Austronesian** | ✅ | ✅ (common) | ⚠️ (rare) | ❌ | ✅ | Dual very common, trial in Oceanic |
| **Trans-New Guinea** | ✅ | ✅ (common) | ⚠️ (some) | ⚠️ (some) | ✅ | Dual common, trial/paucal in Highlands |
| **Indo-European** | ✅ | ⚠️ (Slovene only) | ❌ | ❌ | ✅ | Dual mostly lost except Slovene |
| **Niger-Congo** | ✅ | ❌ | ❌ | ❌ | ✅ | Simple singular/plural |
| **Otomanguean** | ✅ | ❌ | ❌ | ❌ | ✅ | Simple singular/plural |
| **Mayan** | ✅ | ❌ | ❌ | ❌ | ✅ | Simple singular/plural |
| **Australian** | ✅ | ✅ (common) | ⚠️ (some) | ✅ (distinctive) | ✅ | Paucal (3-10) highly distinctive |
| **Afro-Asiatic** | ✅ | ⚠️ (Classical Arabic/Hebrew) | ❌ | ❌ | ✅ | Dual in classical varieties |
| **Sino-Tibetan** | ✅ | ❌ | ❌ | ❌ | ⚠️ (optional) | Plurality often unmarked |
| **Quechuan** | ✅ | ❌ | ❌ | ❌ | ✅ | Simple singular/plural |

**Key**:
- ✅ = Present and critical
- ⚠️ = Present in some languages or limited contexts
- ❌ = Absent

---

## Table 2: Verb TAM Features

| Family | Tense-Prominent | Aspect-Prominent | Mood Systems | Evidentiality | Realis/Irrealis |
|--------|----------------|------------------|--------------|---------------|----------------|
| **Austronesian** | ⚠️ | ✅ | ⚠️ | ❌ | ✅ (critical) |
| **Trans-New Guinea** | ⚠️ (multiple pasts) | ✅ | ⚠️ | ✅ (Highlands) | ⚠️ |
| **Indo-European** | ✅ (Germanic/Romance) | ✅ (Slavic) | ✅ (varied) | ❌ | ❌ |
| **Niger-Congo** | ⚠️ | ✅ | ⚠️ | ❌ | ⚠️ |
| **Otomanguean** | ⚠️ | ✅ | ⚠️ | ❌ | ⚠️ |
| **Mayan** | ⚠️ | ✅ | ✅ (varied) | ❌ | ⚠️ |
| **Australian** | ❌ (minimal) | ⚠️ | ⚠️ | ❌ | ⚠️ |
| **Afro-Asiatic** | ⚠️ (varies) | ⚠️ (varies) | ⚠️ | ❌ | ❌ |
| **Sino-Tibetan** | ❌ (minimal) | ✅ | ⚠️ | ❌ | ❌ |
| **Quechuan** | ⚠️ | ✅ | ⚠️ | ✅ (CRITICAL) | ⚠️ |

**Notes**:
- **Austronesian**: Realis/irrealis distinction critical
- **Trans-New Guinea Highlands**: Evidentiality (seen/unseen) critical
- **Indo-European**: Varies by branch (Slavic aspect-prominent, Germanic/Romance tense-prominent)
- **Quechuan**: Evidentiality (direct/reported/inferred) obligatory and most distinctive feature

---

## Table 3: Case and Alignment Systems

| Family | Case System | Alignment | Split Ergativity | Free Word Order |
|--------|-------------|-----------|------------------|----------------|
| **Austronesian** | ⚠️ (Philippine-type) | ⚠️ (Varied, some ergative) | ⚠️ | ❌ |
| **Trans-New Guinea** | ✅ (common) | ✅ Ergative-Absolutive (common) | ⚠️ | ⚠️ |
| **Indo-European** | ✅ (Slavic/Baltic/Greek) | Nominative-Accusative | ✅ (Indo-Aryan split) | ⚠️ (Slavic) |
| **Niger-Congo** | ❌ (mostly) | Nominative-Accusative | ❌ | ❌ |
| **Otomanguean** | ❌ (minimal) | Nominative-Accusative | ❌ | ❌ |
| **Mayan** | ❌ (minimal) | ✅ Ergative-Absolutive | ⚠️ (some) | ⚠️ |
| **Australian** | ✅ (critical) | ✅ Ergative-Absolutive | ✅ (very common) | ✅ (extremely flexible) |
| **Afro-Asiatic** | ⚠️ (Classical varieties) | Nominative-Accusative | ❌ | ⚠️ (Semitic VSO) |
| **Sino-Tibetan** | ❌ (isolating branches) | ⚠️ (varied) | ⚠️ | ❌ (word order = grammar) |
| **Quechuan** | ✅ (agglutinative) | Nominative-Accusative | ❌ | ⚠️ (SOV rigid) |

**Notes**:
- **Australian**: Split ergativity very common (1st/2nd person nominative-accusative, 3rd person ergative-absolutive)
- **Indo-European**: Indo-Aryan has split ergativity (perfective = ergative, imperfective = nominative-accusative)
- **Mayan**: Some languages have syntactic ergativity (case extends to syntax)
- **Sino-Tibetan**: Isolating branches (Chinese) have minimal case; polysynthetic branches (Kiranti) may have case

---

## Table 4: Distinctive Grammatical Features

| Family | Most Distinctive Features |
|--------|---------------------------|
| **Austronesian** | 1. **Inclusive/Exclusive pronouns** (universal)<br>2. **Realis/Irrealis mood** (critical)<br>3. **Voice systems** (Philippine-type)<br>4. **Dual number** (common) |
| **Trans-New Guinea** | 1. **Switch-reference** (critical)<br>2. **Evidentiality** (Highlands: seen/unseen)<br>3. **Multiple past tenses** (by remoteness)<br>4. **Elevation-based deixis** (Highlands) |
| **Indo-European** | 1. **Case systems** (Slavic/Baltic: 6-7 cases)<br>2. **Aspect systems** (Slavic: perfective/imperfective)<br>3. **Gender** (masculine/feminine/neuter)<br>4. **Dual number** (Slovene only) |
| **Niger-Congo** | 1. **Noun class systems** (Bantu: 10-20 classes)<br>2. **Tone systems** (phonemic)<br>3. **Serial verb constructions**<br>4. **Aspect-prominent TAM** |
| **Otomanguean** | 1. **Tone systems** (2-4 tones, universal)<br>2. **Complex inflection** (person/number/tense/aspect)<br>3. **Aspect-oriented verbs**<br>4. **VSO word order** |
| **Mayan** | 1. **Ergative-absolutive** (universal)<br>2. **Polysynthetic verbs** (complex morphology)<br>3. **Voice systems** (passive, antipassive, etc.)<br>4. **Directional clitics** |
| **Australian** | 1. **Paucal number** (3-10, highly distinctive)<br>2. **Split ergativity** (by person)<br>3. **Free word order** (extremely flexible)<br>4. **Kinship-influenced grammar** |
| **Afro-Asiatic** | 1. **Root-and-pattern morphology** (Semitic)<br>2. **VSO word order** (Semitic)<br>3. **Tone** (Chadic/Cushitic, not Semitic)<br>4. **Grammatical gender** (M/F) |
| **Sino-Tibetan** | 1. **Tone systems** (2-9 tones)<br>2. **Classifier systems** (Chinese/Burmese)<br>3. **Analytic grammar** (isolating branches)<br>4. **Monosyllabic words** |
| **Quechuan** | 1. **Evidentiality** (direct/reported/inferred, obligatory)<br>2. **Agglutinative morphology** (highly regular)<br>3. **Bipersonal conjugation** (subject + object on verb)<br>4. **Topic-prominence** |

---

## Table 5: Polarity and Negation Strategies

| Family | Negation Strategy | Genitive of Negation | Negative Concord | Double Negation |
|--------|-------------------|----------------------|------------------|----------------|
| **Austronesian** | Negative particles/affixes | ❌ | ⚠️ | ❌ |
| **Trans-New Guinea** | Negative affixes (common) | ❌ | ⚠️ | ❌ |
| **Indo-European** | Negative particles | ✅ (Slavic) | ✅ (Slavic/Romance) | ❌ |
| **Niger-Congo** | Negative particles/affixes | ❌ | ⚠️ | ❌ |
| **Otomanguean** | Negative particles | ❌ | ⚠️ | ❌ |
| **Mayan** | Negative particles/affixes | ❌ | ⚠️ | ❌ |
| **Australian** | Negative particles/affixes | ❌ | ⚠️ | ❌ |
| **Afro-Asiatic** | Negative particles | ❌ | ⚠️ | ❌ |
| **Sino-Tibetan** | Negative particles | ❌ | ⚠️ | ❌ |
| **Quechuan** | Negative suffixes | ❌ | ⚠️ | ❌ |

**Notes**:
- **Genitive of Negation**: Slavic languages require genitive case after negated verbs (unique to Indo-European)
- **Negative Concord**: Multiple negative elements reinforce negation (Slavic, Romance); not truly "double negation"
- Most families use straightforward negation without complex interactions

---

## Table 6: Participant Tracking Priority

| Family | Participant Tracking Priority | Notes |
|--------|------------------------------|-------|
| **Austronesian** | ✅ High | Inclusive/exclusive affects reference; voice systems track participants |
| **Trans-New Guinea** | ✅ Very High | Switch-reference is critical for tracking subject continuity |
| **Indo-European** | ⚠️ Medium | Gender/case agreement aids tracking; less critical than switch-reference |
| **Niger-Congo** | ⚠️ Medium | Noun class agreement aids tracking |
| **Otomanguean** | ⚠️ Medium | Standard participant tracking |
| **Mayan** | ✅ High | Ergative-absolutive affects tracking; voice systems |
| **Australian** | ✅ High | Free word order requires case for tracking; kinship affects reference |
| **Afro-Asiatic** | ⚠️ Medium | Gender agreement aids tracking |
| **Sino-Tibetan** | ⚠️ Medium | Topic-prominence affects tracking strategy |
| **Quechuan** | ✅ High | Bipersonal conjugation tracks subject + object; topic-prominence |

---

---

# Recommendations for Under-Documented Languages

When working with languages that lack extensive grammatical descriptions, follow this systematic approach to identify which TBTA features are critical:

---

## Step 1: Identify Language Family

**Action**: Determine which of the 10 major families (or other family) your language belongs to.

**Resources**:
- Ethnologue (ethnologue.com)
- Glottolog (glottolog.org)
- WALS (World Atlas of Language Structures)

**Why**: Family membership provides **typological baseline** assumptions.

**Example**:
- If language is Austronesian → likely has inclusive/exclusive pronouns, realis/irrealis
- If language is Trans-New Guinea → likely has switch-reference, ergative case
- If language is Mayan → likely has ergative-absolutive, polysynthetic verbs

---

## Step 2: Consult Family-Specific Guide (Above)

**Action**: Read the relevant family section in this guide.

**Use**:
- **Critical features** = assume present unless evidence to contrary
- **Irrelevant features** = assume absent unless evidence to contrary
- **Relevant features** = investigate further

---

## Step 3: Analyze Related Languages

**Action**: If your specific language lacks documentation, analyze closely related languages.

**Method**:
1. Identify sister languages (same branch)
2. Read grammatical descriptions of sister languages
3. Assume shared typological features unless proven otherwise

**Example**:
- If working on **undocumented Austronesian language**, analyze related languages:
  - Same branch (e.g., other Oceanic languages)
  - Assume inclusive/exclusive pronouns, realis/irrealis, dual number
  - Check for voice systems (more variable)

---

## Step 4: Use Parallel Texts

**Action**: Analyze existing translations in the target language.

**Method**:
1. Obtain Bible translations or other parallel texts
2. Analyze grammatical patterns:
   - How are pronouns distinguished? (inclusive/exclusive, dual, etc.)
   - How are verbs inflected? (tense, aspect, mood, evidentiality, etc.)
   - What is word order? (SVO, SOV, VSO, VOS, free)
   - Are there case markers? (ergative, nominative, accusative, etc.)
   - How is negation expressed?

**Example Analysis**:
- Find verses with "we" in English
- Compare target language forms
- If two forms appear, likely inclusive/exclusive distinction

---

## Step 5: Consult with Native Speakers

**Action**: If possible, work with native speakers or fluent translators.

**Questions to Ask**:

### Pronouns:
- "How do you say 'we' (including you) vs. 'we' (not including you)?"
- "Is there a special form for exactly two people?"
- "Is there a form for a few people (3-10)?"

### Verbs:
- "How do you show that something definitely happened vs. might happen?"
- "How do you show that you saw it yourself vs. heard about it?"
- "Does the verb change when the subject changes? When the object changes?"

### Word Order:
- "Can you rearrange these words? Does the meaning change?"

### Case:
- "How do you show who did the action vs. who received it?"
- "Does the word ending change based on its role in the sentence?"

---

## Step 6: Prioritize High-Impact Features

**Action**: Focus annotation effort on features that:
1. Are **family-typical** (assume present)
2. **Affect translation accuracy** (e.g., inclusive/exclusive changes meaning)
3. **Have cross-linguistic impact** (e.g., ergativity affects all clauses)

**Low Priority** (can omit if under-documented):
- Features absent in language family
- Features that don't affect meaning (stylistic only)
- Features with minimal cross-linguistic variation

---

## Step 7: Document Uncertainty

**Action**: When uncertain about a grammatical feature:
1. **Mark as uncertain** in annotation
2. **Provide alternative analyses** if possible
3. **Note need for further research**

**Example**:
```yaml
number: dual  # UNCERTAIN: May be paucal (3-5) rather than dual (2). Needs native speaker verification.
```

---

## Step 8: Iterative Refinement

**Action**: As more information becomes available:
1. **Update annotations** based on new grammatical insights
2. **Revise family-specific guidelines** if language differs from family pattern
3. **Share findings** with other translators

---

---

## Universal Baseline for All Languages

Regardless of documentation level, **all languages have**:

1. **Nouns** and **Verbs**
2. **Subjects** and **Objects** (or equivalent grammatical relations)
3. **Singular** and **Plural** (at minimum)
4. **Affirmative** and **Negative** (polarity)
5. **Past**, **Present**, and/or **Future** reference (may be lexical, not grammatical)

**Start with these**, then add family-specific features.

---

## Red Flags: When to Seek Expert Help

Seek consultation from linguists or experienced translators if:

1. **Language behavior contradicts family patterns**
   - Example: Austronesian language lacks inclusive/exclusive pronouns
   - May indicate unusual historical development or misclassification

2. **Multiple conflicting analyses exist**
   - Example: Language described as both ergative and accusative
   - May have split ergativity or conflicting sources

3. **Translation sounds unnatural despite following rules**
   - May indicate missing grammatical category or incorrect analysis

4. **Parallel texts show unexplained variation**
   - May reveal optional grammatical categories or stylistic variation

---

---

# Conclusion

This guide provides **practical, family-specific recommendations** for adapting TBTA annotations to the typological realities of 10 major language families representing **714 languages** in our dataset.

## Key Principles

1. **Not all TBTA features matter equally for all languages**
   - Dual number is critical for Austronesian, irrelevant for Niger-Congo
   - Evidentiality is critical for Quechuan, irrelevant for most other families
   - Ergativity is critical for Australian/Mayan, irrelevant for Indo-European (except Indo-Aryan split)

2. **Family membership predicts typological features**
   - Knowing the language family provides baseline assumptions
   - Critical features are family-typical
   - Irrelevant features are family-atypical

3. **Under-documented languages can be annotated using family patterns**
   - Start with family-typical features (assume present unless proven absent)
   - Analyze related languages
   - Use parallel texts and native speaker consultation
   - Document uncertainty and refine iteratively

4. **Annotation priority should match linguistic reality**
   - Focus effort on critical features (family-typical, high-impact)
   - De-emphasize irrelevant features (family-atypical, low-impact)
   - Document relevant features where they affect translation accuracy

---

## Using This Guide

**For Bible Translators**:
- Identify your target language family
- Read the relevant family section
- Focus annotation effort on **critical** and **relevant** features
- Skip **irrelevant** features (language doesn't distinguish them)

**For Translation Consultants**:
- Use family-specific sections to guide translator training
- Highlight critical features during workshops
- Provide examples of how family-typical features affect translation

**For Annotation Specialists**:
- Use cross-family comparison tables to understand typological variation
- Apply family-specific workflows for efficient annotation
- Document uncertainty for under-documented languages

**For Researchers**:
- Use this guide to identify gaps in grammatical descriptions
- Compare family patterns to identify outliers (unusual languages)
- Contribute refinements as new grammatical analyses become available

---

## Future Directions

As the TBTA project expands, we recommend:

1. **Adding more families** (Dravidian, Turkic, Uto-Aztecan, etc.)
2. **Refining family-specific workflows** based on translator feedback
3. **Creating language-specific supplements** for high-priority languages
4. **Developing automated family detection** based on typological features
5. **Building family-specific validation rules** for annotation quality control

---

**This guide is a living document**. As grammatical research progresses and translator feedback accumulates, we will update family-specific recommendations to better serve the global Bible translation community.

---