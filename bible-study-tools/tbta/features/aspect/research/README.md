# Aspect Research Summary

**Stage**: Stage 1 - Research & Definition (Complete)
**Feature**: Grammatical Aspect
**TBTA Tier**: A (Essential - affects 1000+ languages)
**Last Updated**: 2025-11-29

---

## Quick Reference

**What is Aspect?** The grammatical encoding of how an action unfolds over time - whether viewed as complete (perfective), ongoing (imperfective), habitual, or specific beginning/completion.

**Source Languages**: Both Hebrew and Greek EXPLICITLY encode aspect morphologically
- **Hebrew**: Binary perfective/imperfective (qatal/yiqtol)
- **Greek**: Three-way perfective/imperfective/stative (aorist/present/perfect)

**Critical Translation Languages**: Slavic (Russian, Polish), Niger-Congo (Swahili), Austronesian (Tagalog), Sino-Tibetan (Mandarin)

**Theological Stakes**: HIGH for specific contexts (habitual sin - 1 John 3:6,9), MEDIUM for imperatives and prophecy, LOW for most narrative

---

## Executive Summary

### The Feature

**Aspect** differs from tense:
- **Tense** = WHEN an event occurs (past, present, future)
- **Aspect** = HOW an event unfolds (complete whole, ongoing process, habitual pattern)

**Core Distinction** (Comrie 1976):
- **Perfective**: Views action externally as complete whole with beginning, middle, end
- **Imperfective**: Views action internally, emphasizing ongoing process or internal structure
- **Progressive**: Sub-type of imperfective, action currently in progress
- **Habitual**: Sub-type of imperfective, repeated/customary action

### Why It Matters

**Source Languages Encode It**:
- Hebrew qatal (perfective) vs yiqtol (imperfective) - fundamental OT distinction
- Greek aorist (perfective) vs present (imperfective) vs perfect (stative) - fundamental NT distinction

**Many Target Languages Require It**:
- **Mandatory**: Slavic, many Niger-Congo, some Austronesian, Sino-Tibetan
- **Optional**: Romance (past tense), some Austronesian
- **Minimal**: Germanic (English/German progressive only)

**TBTA Problem** (Critique):
- TBTA overgeneralizes to "Unmarked" - most verbs not analyzed
- Lacks Aktionsart (lexical aspect) database
- Cannot leverage verb class + morphology to predict semantic aspect
- Aspect-prominent languages (Russian, Swahili, Mandarin) left without guidance

### Key Findings by Research Area

**TBTA Documentation** → [TBTA.md](TBTA.md):
- 8 documented aspect values: Perfective, Imperfective, Progressive, Habitual, Inceptive, Completive, Gnomic, Unmarked
- Character position 2 in verb encoding
- Gateway feature: Part of Speech = Verb
- Critical limitation: Defaults to "Unmarked" rather than making predictions

**Language Typology** → [LANGUAGES.md](LANGUAGES.md):
- Perfective/imperfective marking forms Eurasian-African belt (WALS 65)
- 10 languages selected for Stage 2 translation database across 7 families
- Source languages (Hebrew, Greek) both aspect-prominent
- 7 of 11 root/bridge languages have grammatical aspect

**Scholarly Research** → [SCHOLARLY.md](SCHOLARLY.md):
- 25+ sources including Comrie (1976), Bybee et al. (1994), Dahl (1985)
- Vendler's Aktionsart classification essential: States, Activities, Accomplishments, Achievements
- Greek NT aspect debate: Porter (aspect only) vs Fanning (aspect + tense)
- Hebrew TAM system: Aspect more prominent than tense

**Theological Significance** → [THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml):
- HIGH stakes: 1 John 3:6,9 (habitual sin - imperfective REQUIRED or creates heresy)
- MEDIUM stakes: Imperatives (aorist vs present), prophecy (prophetic perfect)
- 80% of contexts: Aspect is stylistic choice, not theologically critical

---

## Research Section Summaries

### 1. TBTA Documentation Review

**File**: [TBTA.md](TBTA.md) (350 lines)

**Key Points**:
- Aspect is Tier A feature #9 (Essential for 1000+ languages)
- Values: Perfective, Imperfective, Progressive, Habitual, Inceptive, Completive, Gnomic, Unmarked
- Character codes: I (imperfective), C (completive), H (habitual), G (gnomic), U (unmarked)
- Gateway feature: Verbs only
- Policy: Semantic vs morphological priority unclear; defaults to "Unmarked"

**Critical Findings**:
- **Overgeneralization to "Unmarked"**: Most verbs not analyzed (CRITIQUE Section 2.2)
- **No Aktionsart database**: Cannot predict aspect from verb class + morphology (CRITIQUE Section 4.2)
- **Mood-aspect interaction unclear**: All imperatives marked "Indicative" (CRITIQUE line 318)
- **Translation impact**: Aspect-prominent languages (Slavic, Niger-Congo, Austronesian) lack guidance

**Recommendations**:
- Stage 2: Build Aktionsart classifier (Vendler categories)
- Stage 3: Use source morphology + Aktionsart + context for prediction
- Don't default to "Unmarked" - make informed predictions

---

### 2. Language Family & Typology Analysis

**File**: [LANGUAGES.md](LANGUAGES.md) (400+ lines)

**Key Points**:
- **Source languages**: Hebrew (binary pf/impf), Greek (three-way pf/impf/stative) - both explicit
- **Geographic distribution**: Eurasian-African belt (Europe → China, down to equator in Africa)
- **Language families**:
  - **Mandatory aspect**: Slavic, Niger-Congo (Bantu), Austronesian (Philippine), Sino-Tibetan, Afro-Asiatic (Semitic)
  - **Optional aspect**: Romance (past only), Austronesian (Indonesian type), Germanic (progressive)
  - **Minimal aspect**: Uralic, some Germanic

**Selected Languages for Stage 2** (10 total):

**Tier 1 - Mandatory Aspect**:
1. Russian (rus) - Slavic, binary mandatory
2. Swahili (swh) - Niger-Congo, 5-way system
3. Tagalog (tgl) - Austronesian, aspect-voice merger
4. Mandarin (zho) - Sino-Tibetan, aspect particles (no tense)

**Tier 2 - Optional Aspect**:
5. Spanish (spa) - Romance, past aspect
6. Polish (pol) - Slavic transitional
7. Arabic (ara) - Semitic, binary like Hebrew
8. Indonesian (ind) - Austronesian, optional particles

**Tier 3 - Limited Aspect**:
9. English (eng) - Germanic, progressive only
10. German (deu) - Germanic, limited aspect

**Critical Distinctions**:
- Slavic: Every verb MUST be marked perfective or imperfective
- Niger-Congo: 5-way system (richer than binary)
- Mandarin: No tense, only aspect particles (了 le, 着 zhe, 过 guo)
- Austronesian: Philippine type (mandatory) vs Indonesian type (optional)

---

### 3. Scholarly Research

**File**: [SCHOLARLY.md](SCHOLARLY.md) (500+ lines with 25+ sources)

**Foundational Works**:
1. **Comrie (1976)** - *Aspect* - Foundational typological framework
2. **Bybee et al. (1994)** - *Evolution of Grammar* - 76 languages, universal grammaticalization paths
3. **Dahl (1985)** - *Tense and Aspect Systems* - Comprehensive cross-linguistic analysis
4. **Vendler (1957)** - Aktionsart classification: States, Activities, Accomplishments, Achievements

**Biblical Languages**:
- **Porter (1989)**: Greek has aspect only, no tense (controversial)
- **Fanning (1990)**: Greek has aspect + tense in indicative
- **Agreement**: All agree aorist = perfective, present = imperfective
- **Hebrew** (Cook 2012): TAM system, aspect more prominent than tense

**Typological Databases**:
- **WALS Feature 65**: Perfective/imperfective distribution worldwide
- **Grambank GB086**: Binary classification (aspect present/absent)

**Language-Specific**:
- **Slavic**: Aspectual pairs, prefixation for perfective, East-West division
- **Niger-Congo**: 5 aspects (FAC/IPFV/PFT/PRG/HAB), verbal extensions
- **Austronesian**: 4 aspects + outer markers ('still', 'already')
- **Mandarin**: 3 particles (了 le perfective, 着 zhe durative, 过 guo experiential)

**Translation Case Studies**:
1. Genesis 1:26 - Trinity (number interaction with aspect)
2. John 3:16 - Aorist "loved" (perfective = single historical act)
3. 1 John 3:6,9 - Present "sins" (imperfective = habitual action - CRITICAL)
4. Matthew 28:19-20 - Aorist imperative vs present participle

**Key Insight**: Aktionsart (lexical aspect) + Morphology → Semantic aspect prediction
- Greek aorist + Accomplishment verb → Completive
- Greek present + State verb → Continuous
- TBTA lacks this - major gap

---

### 4. Theological Significance Classification

**File**: [THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml) (250+ lines)

**Distribution**:
- **Non-arbitrary (theological)**: 5% - HIGH stakes
- **Non-arbitrary (contextual)**: 15% - MEDIUM stakes
- **Arbitrary (stylistic)**: 80% - LOW stakes

**HIGH Stakes Contexts**:

**1. Habitual Sin (1 John 3:6,9)** - CRITICAL:
- Greek: Present tense (imperfective) = "keeps on sinning", "makes a practice of"
- NOT aorist (perfective) which would mean single act
- **Theological impact**: Imperfective = Christians don't habitually sin (orthodox)
                         Perfective = Christians never sin (sinless perfectionism - HERESY)
- **Required**: MUST use imperfective/habitual aspect or lexical equivalents
- **Forbidden**: Perfective aspect (changes theology)

**MEDIUM Stakes Contexts**:

**2. Great Commission Imperatives (Matthew 28:19-20)**:
- "Make disciples" (aorist imperative) = single decisive command
- "Teaching" (present participle) = ongoing process
- Aspect affects understanding: Command accomplished through ongoing process

**3. Prophetic Perfect (Isaiah 9:6)**:
- Hebrew qatal (perfective) for future event = certainty
- "Unto us a child IS BORN" (prophetic perfect)
- Emphasizes divine decree and certainty

**4. Imperative Aspect Distinction**:
- Aorist imperative: Do this once (decisive action)
- Present imperative: Keep doing this (ongoing habit)
- Example: "Give us... bread" (aorist) = single request for today

**LOW Stakes Contexts**:
- Narrative sequences (foreground vs background)
- Parable key moments
- General past events (70% of all contexts)

**Common Translation Error to Avoid**:
- Using perfective for 1 John 3:6,9 → Creates sinless perfectionism heresy

---

## Key Discrepancies and Issues

### Discrepancy 1: TBTA vs Scholarly Research

**TBTA Approach**:
- Defaults to "Unmarked" for most verbs
- Does not use Aktionsart classification
- Cannot leverage verb class + morphology

**Scholarly Consensus**:
- Aktionsart (Vendler 1957) is standard
- Lexical aspect + grammatical morphology → semantic aspect
- Predictable patterns: Aorist + Accomplishment = Completive

**Impact**: TBTA provides less guidance than linguistically possible

---

### Discrepancy 2: TBTA Policy Unclear

**TBTA Documentation**:
- Does not specify semantic vs morphological priority
- Unclear whether participles/infinitives carry aspect
- Mood-aspect interactions not documented
- All imperatives marked "Indicative" (error)

**Scholarly Understanding**:
- Greek: Imperative can be aorist (perfective) or present (imperfective)
- Hebrew: Aspect more fundamental than tense
- Participles carry aspect in both languages

**Impact**: TBTA implementation may have gaps in edge cases

---

### Discrepancy 3: Binary vs Multi-way Systems

**TBTA Values**: 8 aspect values (Perfective, Imperfective, Progressive, Habitual, Inceptive, Completive, Gnomic, Unmarked)

**Language Reality**:
- Slavic: Binary (perfective/imperfective)
- Niger-Congo: 5-way (FAC/IPFV/PFT/PRG/HAB)
- Greek: 3-way (perfective/imperfective/stative)
- Mandarin: 3 particles with different functions

**Question for Stage 2**: How to map TBTA's 8 values to target language systems?
- Does Progressive collapse into Imperfective for Slavic?
- Does Completive = Factative for Niger-Congo?
- Need translation evidence to resolve

---

## Recommendations for Stage 2 (Analysis)

### Data Collection Priorities

1. **Frequency Analysis**:
   - Extract all aspect values from TBTA database
   - Count actual usage (confirm "Unmarked" dominance)
   - Compare OT vs NT distributions

2. **Aktionsart Classification**:
   - Tag Greek/Hebrew verbs with Vendler classes (States, Activities, Accomplishments, Achievements)
   - Correlate with TBTA aspect values
   - Test: Does Aktionsart predict aspect?

3. **Translation Database** (10 languages):
   - Collect translations for 100+ verses per aspect value
   - Sample: Balanced OT/NT, narrative/discourse, typical/adversarial
   - Languages: Russian, Swahili, Tagalog, Mandarin, Spanish, Polish, Arabic, Indonesian, English, German

4. **Mood-Aspect Interaction**:
   - Cross-tabulate aspect by mood
   - Identify valid combinations
   - Test: Does imperative restrict aspect options?

5. **Source Language Correlation**:
   - Map Greek tense-forms to TBTA aspect
   - Map Hebrew verb forms to TBTA aspect
   - Calculate agreement rates

### Algorithm Development Insights

**Don't Default to "Unmarked"**:
- TBTA's weakness: Too conservative
- Better: Make informed predictions using Aktionsart + morphology

**Use Multi-Source Evidence**:
1. Greek/Hebrew morphology (aorist → perfective)
2. Aktionsart (accomplishment → completive)
3. Context (narrative sequence → perfective)
4. Translation consensus (80%+ agreement → strong signal)

**Consider Language-Specific Needs**:
- Slavic: Binary choice (collapse Progressive → Imperfective)
- Niger-Congo: 5-way system (map Completive → Factative)
- Mandarin: Choose particle (Perfective → 了 le)

**Handle Theological Contexts Specially**:
- 1 John 3:6,9: Lock to imperfective/habitual (non-negotiable)
- Imperatives: Preserve aorist/present distinction when possible
- Other contexts: Allow stylistic variation

---

## File Organization

```
/workspace/bible-study-tools/tbta/features/aspect/research/
├── README.md (this file) - Summary and synthesis
├── TBTA.md - TBTA documentation review (350 lines)
├── LANGUAGES.md - Language typology analysis (400+ lines)
├── SCHOLARLY.md - Academic research (500+ lines, 25+ sources)
└── THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml - Theological classification (250+ lines)
```

**Total Research**: 1500+ lines across 4 detailed documents + this summary

---

## Next Steps

### Stage 2: Generate Test Set with Translation Data

**Tasks**:
1. Extract TBTA aspect annotations from database
2. Build Aktionsart classifier for Greek/Hebrew verbs
3. Collect 10-language translation corpus (100+ verses per aspect value)
4. Analyze translation patterns and consensus

**Deliverables**:
- Frequency analysis report
- Aktionsart-tagged verb database
- Translation database (10 languages x 100+ verses)
- Pattern discovery analysis

**Success Criteria**:
- Balanced dataset (each aspect value adequately represented)
- High inter-translator agreement in aspect-prominent languages
- Clear correlation between Aktionsart + morphology and aspect

### Stage 3: Analyze Translations & Develop Algorithm

**Tasks**:
1. Discover patterns from translation consensus
2. Build prediction algorithm using source morphology + Aktionsart
3. Handle theological contexts separately (1 John 3:6,9)
4. Test algorithm on development set

**Deliverables**:
- Algorithm specification
- Training set predictions
- Error analysis

**Success Criteria**:
- Accuracy ≥ 90% on typical cases
- 100% accuracy on theological HIGH-stakes verses
- Outperforms TBTA "Unmarked" default

---

## Citation Summary

### Primary Sources

**TBTA Internal**:
- /workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md
- /workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md
- /workspace/bible-study-tools/tbta/tbta-source/CRITIQUE.md

**Major Scholarly Works**:
- Comrie 1976 - *Aspect*
- Bybee et al. 1994 - *Evolution of Grammar*
- Dahl 1985 - *Tense and Aspect Systems*
- Vendler 1957 - "Verbs and Times"
- Porter 1989 - *Verbal Aspect in the Greek NT*
- Fanning 1990 - *Verbal Aspect in NT Greek*
- Cook 2012 - *Time and the Biblical Hebrew Verb*

**Typological Databases**:
- WALS Feature 65 (Perfective/Imperfective Aspect)
- WALS Chapter S7 (Tense and Aspect)
- Grambank GB086 (Aspect on Verbs)

**Language-Specific**:
- Slavic aspect research (Wikipedia, academic papers)
- Niger-Congo aspect (Nurse, Hyman)
- Austronesian aspect (Kaufman et al.)
- Mandarin Chinese aspect (multiple sources)

**Total**: 25+ scholarly sources, 3 typological databases, 5 language family studies

---

## Research Completion

**Stage 1 Status**: ✅ COMPLETE

**Deliverables**:
- ✅ TBTA.md (350 lines)
- ✅ LANGUAGES.md (400+ lines)
- ✅ SCHOLARLY.md (500+ lines)
- ✅ THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml (250+ lines)
- ✅ research/README.md (this file, 200 lines)
- ⏳ feature/README.md (pending - max 75 lines)

**Ready for Stage 2**: Yes - comprehensive research foundation established

---

**Last Updated**: 2025-11-29
**Researcher**: Claude (Sonnet 4.5)
**Review Status**: Awaiting peer review
