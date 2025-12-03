<<<<<<< HEAD
# Time Granularity: Research Synthesis

**Feature Definition**: Time granularity captures temporal remoteness—how distant an event is from the discourse moment (now/reference point). Distinct from tense (past/present/future) and aspect (perfective/imperfective), it specifies HOW FAR in the past/future an event occurred.

**Theological Significance**: 15% of biblical contexts are non-arbitrary (crucifixion hours, "third day" resurrection, creation origins, eschatological timing); 85% are stylistically flexible.

---

## 1. TBTA Documentation (`TBTA.md`)

**Complete Value Inventory**: 23-24 character codes organized in three temporal domains:
- **Past** (13 values): P=Present; D/A/a/b/c/d/e/f/g/h/i/q=past distances (immediate to eternity past, unknown)
- **Future** (8 values): E/F/j/k/l/m/n/o/p=future distances (immediate today to year ahead, unknown)
- **Atemporal** (2 values): r=Discourse, T=Timeless

**Gateway Features**: Time applies to **Verbs only** (position 1 of 9-position code). Mood constraints unclear; Aspect co-occurs but independent. Discourse Genre may influence selection (narrative=historic past; teaching=timeless).

**Policy Gaps**: No explicit rule for semantic vs. morphological priority; discourse perspective (modern/original audience/internal story time) unstated; semantic temporal distance marked, not source language morphology.

**Known Issues**: Aspect overgeneralized as "Unmarked" (CRITIQUE.md); no Aktionsart classification; Greek imperatives miscoded as Indicative; coverage complete within 11,649-verse corpus (~37% Bible).

**Discrepancies**:
- **h-value semantics**: "Historic Past" (GitHub) vs "Remote Past/living memory" (DATA-STRUCTURE.md)
- **c-value range**: "3 Days Ago" (GitHub) vs "2-7 days ago" (DATA-STRUCTURE.md)
- **Total values**: "20+" stated vs 23 documented

**Edge Cases**: Timeless vs Present distinction policy absent; Discourse vs Timeless in teaching contexts unclear; flashbacks/anteriority unmarked in documentation; eschatological future encoding absent (archived research included `L` value not in official export).

---

## 2. Language Typology (`LANGUAGES.md`)

**Source Languages**: ❌ **Hebrew & Greek lack explicit temporal remoteness morphology**. Both are aspect-prominent; context determines remoteness, not morphology. Translators must infer temporal distance from context (genealogies, narrative framing, cultural knowledge), then encode it for target languages requiring grammatical marking.

**Language Family Patterns** (1,009 languages analyzed):

| Family | Count | Status | Granularity | Pattern |
|--------|-------|--------|-------------|---------|
| **Niger-Congo (Bantu)** | 89 | ✅ Mandatory | High (4-8) | Hodiernal/hesternal/remote |
| **Austronesian** | 176 | ⚠️ Optional (27%) | Variable | TAM optional, adverb-dependent |
| **Trans-New Guinea** | 141 | ✅ Majority mandatory | Medium-High | Hodiernal/hesternal systems |
| **Indo-European** | 135 | ❌ Optional | Low | Simple past/present/future + adverbs |
| **Quechuan** | 18 | ✅ Mandatory | Medium | **Fused with evidentiality** |
| **Otomanguean** | 69 | ✅ 100% mandatory | Medium | Obligatory TAM |
| **Sino-Tibetan** | 18 | ⚠️ Adverbs mandatory | Medium | Aspect particles + temporal adverbs |
| **Mayan** | 41 | ❌ Optional | Low | Aspect-based, minimal remoteness |

**Root Languages**: 11/13 (Hebrew, Greek, English, Spanish, French, German, Portuguese, Arabic, Russian, Indonesian, Mandarin) lack obligatory temporal remoteness. **Swahili exception**: Mandatory Bantu system.

**Candidate Languages for Stage 2** (10 selected):
1. English (Indo-European, baseline)
2. **Swahili** (Bantu, mandatory, bridge language)
3. Mandarin (aspect + adverbs, bridge)
4. Quechua, Cusco (temporal-evidential fusion)
5. **Tagalog** (Austronesian, aspect-based with temporal adverbs)
6. Amele (Trans-New Guinea, hodiernal)
7. K'iche' (Mayan, aspect-based)
8. Amuzgo (Otomanguean, 100% obligatory)
9. Spanish (Indo-European, bridge)
10. Indonesian (optional TAM)

**Cultural Nuances**: Lunar calendars (Hebrew, Chinese, Islamic); event-based time reckoning (Amazonian languages—no metric units); relative hour systems (biblical "third hour" = variable-length hours); absolute vs. relative tense variation (Russian lacks pluperfect/future perfect).

---

## 3. Scholarly Research (`SCHOLARLY.md`)

**28+ Scholarly Sources** organized in 4 sections:

- **Linguistic Theory** (Comrie, Dahl, Bybee, Klein, Cook, Haspelmath, Reichenbach): Foundational frameworks for aspect vs. tense, temporal remoteness typology, grammaticalization pathways, Reichenbach's E-R-S temporal coordinates.

- **Typological Databases** (WALS, Grambank, 2,467 languages): ~20% of languages mark remoteness distinctions; 99-language WALS sample shows salient non-marking in Southeast Asia; Grambank covers 195 grammatical features including tense/aspect domains.

- **Translation Case Studies**:
  - **Crucifixion Timing** (Mark 15:25 vs John 19:14): Jewish (sunrise-based) vs Roman (midnight-based) hour systems create apparent contradiction. Resolved through different temporal reference frames. Theological stakes: Passover typology, supernatural darkness, divine timing.
  - **"Three Days and Three Nights"** (Matthew 12:40): Hebrew inclusive reckoning (part of day = full day). Corroborated by Esther 4:16-5:1, Genesis 42:17-18, 1 Samuel 30:12-13. Cross-cultural variation: some languages share this idiom, others require footnote.
  - **Papua New Guinea Bible Translation**: Event-based time reckoning (Kaluli) lacked metric calendar/clock concepts. Missionization introduced new vocabulary, creating evidential value for temporal markers. Hybrid solutions blend indigenous seasonal terms with borrowed calendar terms.

- **Key Biblical Passages**: 25+ verses analyzed for temporal precision requirements (Genesis genealogies, Daniel 9 prophetic weeks, Revelation eschatological durations, Passion Week chronology, crucifixion/resurrection timing).

**Findings**: Temporal precision is **non-arbitrary in 15% of contexts** (atonement theology, resurrection apologetics, creation historicity, divine sovereignty, eschatological certainty). Most temporal references (85%) are stylistically flexible (narrative past distinctions, wisdom literature vagueness, travel narrative sequencing).

---

## 4. Theological Classification (`THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml`)

**Non-Arbitrary Contexts (15%)**:

**HIGH DOCTRINAL STAKES**:
- **Crucifixion hours** (Mark 15:25, 33-34): 3rd/6th/9th hour precision connects to Passover lamb timing, temple sacrifice schedule. Vague marking loses theological connection.
- **Resurrection "third day"** (1 Cor 15:4): Creedal formula, prophetic fulfillment (Jonah sign). Specific day-count essential for historical verification.
- **Genesis 1:1** ("In beginning"): Historic/primordial past required (not recent past, not timeless myth). Seven-day structure establishes Sabbath theology.
- **Jesus' "hour"** (John 2:4, 12:23): Appointed/eschatological time (not casual future). Demonstrates sovereignty over Passion timing.
- **Second Coming** (Matthew 24:36): Eschatological future + unknown timing (not calculable near/remote future). Prevents date-setting, maintains watchfulness.

**MEDIUM CONTEXTUAL STAKES**:
- **Sabbath/festival timing**: Hodiernal subdivisions required for obedience (twilight for Passover lamb, "between evenings").
- **Prayer hours** (Acts 2:15, 3:1, 10:9): 3rd/6th/9th hours establish daily rhythm of early church, narrative context.
- **Flood chronology** (Genesis 7-8): Precise calendar dates mark historical narrative genre (not mythology).

**Arbitrary Contexts (85%)**:
- General past narratives (remote vs. historic distinction stylistic)
- Vague wisdom literature ("in time," "one day")
- Travel narratives ("after this," "then," "later")
- Timeless/gnomic statements (eternal truths, no temporal change)

---

## Key Discrepancies & Gaps

| Issue | TBTA | Languages | Scholarly | Resolution |
|-------|------|-----------|-----------|-----------|
| Source lang encoding | Not listed | ❌ Neither Hebrew nor Greek marks remoteness morphologically | Confirmed: aspect-prominent, context-dependent | Translators must infer from context |
| Semantic vs morphological | Not stated | N/A | "Semantic temporal remoteness" priority implied by Genesis example | TBTA extracts contextual meaning, not morphology |
| Discourse perspective | Not listed | Not listed | Modern reader perspective (2025) vs. original audience (1st century) | Likely original audience; needs verification |
| Eschatological future | 23 values documented | Mandatory in many families | Special category needed (end-times vs calculable) | Consider adding if not already present |
| Frequency distribution | "Complete" (11,649 verses) | Languages analyzed, not values | Not calculated | Stage 2 analysis needed |

---

## Implications for Algorithm

1. **For high-granularity languages** (Bantu, Trans-New Guinea, Quechuan): Map biblical contexts to appropriate remoteness markers. Critical in 15% theological contexts; flexible in 85%.

2. **For aspect-based languages with temporal adverbs** (Tagalog, Mandarin): Obligatory aspect marking (completed/ongoing/contemplated) combined with optional temporal adverbs. TBTA guides adverb selection; non-arbitrary contexts require explicit temporal adverbs.

3. **For low-granularity languages** (English, Indo-European): Adverbials carry precision ("at the third hour," "on the third day," "in the beginning"). TBTA provides classification, translators add explicit temporal markers.

4. **For languages without obligatory temporal marking**: Temporal choice is optional; translator decides based on theological/contextual priority. Non-arbitrary contexts require precision; arbitrary contexts allow flexibility.

5. **For event-based languages** (Amazonian): May require conceptual shift from metric time to natural/social event cycles. Hybrid solutions blend indigenous and introduced temporal frameworks.

---

**Confidence Levels**: TBTA documentation well-researched (23-value inventory confirmed); language typology data-backed (1,009 language corpus); scholarly analysis comprehensive (28+ sources); theological classification requires peer review (marked unverified where inferred from Scripture).

**Next Stage**: Language translation database (Stage 2) should verify TBTA values in actual corpus, test theological assessments with peer review, validate translation impact claims with field translators working in high-granularity languages.
=======
# Time Granularity: Stage 1 Research Summary

**Feature**: Time Granularity (Temporal Remoteness / Metrical Tense)
**Research Completed**: 2025-11-29
**Status**: Ready for Stage 2 (Language Study)

## Quick Reference

| Aspect | Summary |
|--------|---------|
| **What it is** | Grammatical encoding of temporal distance from present (how long ago/from now) |
| **TBTA Values** | 20+ values ranging from immediate past to legendary past, plus future and timeless |
| **Source Languages** | NOT encoded in Hebrew or Greek - all values inferential |
| **Global Prevalence** | ~20% of world languages (1000+ languages) |
| **Critical Families** | Bantu (80% have feature), some Amazonian, scattered others |
| **Theological Stakes** | MINIMAL - 95%+ arbitrary; few contextual clarity issues |
| **Translation Impact** | CRITICAL for ~1000 languages; impossible to infer without contextual analysis |

## What is Time Granularity?

**Time granularity** answers: "How far from now did this happen?" or "How precise is the temporal reference?"

Unlike simple tense (past/present/future), time granularity makes fine distinctions:
- **Immediate past**: Just now, today
- **Hesternal**: Yesterday
- **Recent past**: Days or weeks ago
- **Remote past**: Months or years ago, within living memory
- **Historic/Legendary past**: Ancient times, beyond living memory

**Critical distinction**: Time granularity is about DISTANCE, not ASPECT (how action unfolds).

## Core Research Findings

### 1. TBTA Documentation ([TBTA.md](TBTA.md))

**Feature Status**: ✅ Complete in TBTA (Tier A Essential)

**Value Inventory**:
- ~13 values explicitly documented with character codes
- 20+ values claimed in TBTA documentation
- Includes: Present (P), Immediate Past (D), Yesterday (a), Historic Past (i), Timeless (T), Immediate Future (E)

**Critical Finding**: Time granularity is **Position 1 in Verb codes** - only applies to verbs.

**Gateway Feature**: Part of Speech → must be Verb
**No Dependencies**: Orthogonal to Aspect, Mood, Polarity

**Policy**: TBTA prioritizes **semantic/contextual reality** over morphology. Values reflect actual temporal distance of event described, not Greek/Hebrew tense forms.

**Example**: Genesis creation marked as Historic Past (i), regardless of Hebrew verb form, because events are thousands of years old.

**Gap**: Only ~13 of 20+ values have documented character codes. Future granularity largely undocumented.

### 2. Language Typology ([LANGUAGES.md](LANGUAGES.md))

**Global Distribution**: ~20% of world languages make remoteness distinctions {wals-66}

**CRITICAL FINDING**: Neither Hebrew nor Greek encode time granularity
- Hebrew wayyiqtol = narrative sequence, NOT temporal distance
- Greek aorist = simple past, NOT remoteness
- **All TBTA values are 100% inferential from context**

**Language Families**:

| Family | Status | System | Notes |
|--------|--------|--------|-------|
| **Bantu** | MANDATORY (80%) | 2-4 past, 0-4 future | Best documented, family-wide feature |
| **Amazonian** | MANDATORY (some) | Up to 5 past | Yagua has richest system (5-way) |
| **Austronesian** | VARIABLE | 0-2 | Mixed; Tagalog aspect-based, Hawaiian tenseless |
| **Indo-European** | ABSENT (mostly) | 0 | Rare exceptions (Balochi) |
| **Sino-Tibetan** | ABSENT | 0 | Tenseless systems |
| **Afro-Asiatic** | ABSENT | 0 | Includes Hebrew, Arabic |

**Universal Pattern**: Primary division is almost always **hodiernal** (today) vs. **pre-hodiernal** (before today).

**Asymmetry**: Languages make MORE past distinctions than future (past is known, future uncertain).

**Recommended Test Languages** (for Stage 4):
1. **Yagua** (yad) - 5 past (maximum complexity)
2. **ChiBemba** (bem) - 4 past + 4 future (symmetric)
3. **Swahili** (swh) - 2-3 past (major translation language)
4. **Tagalog** (tgl) - Variable (aspect-based edge case)
5. **English, Spanish, Mandarin** - Controls (absent)

### 3. Scholarly Research ([SCHOLARLY.md](SCHOLARLY.md))

**25+ sources reviewed**, including:

**Foundational Works**:
- Comrie (1985) _Tense_ - Defines tense as "grammaticalization of location in time"
- Dahl (1985) _Tense and Aspect Systems_ - Establishes hodiernal/hesternal/pre-hodiernal terminology
- Nurse (2008) _Tense and Aspect in Bantu_ - Database of 210 Bantu languages, 80% have feature

**Critical Edge Case**:
- Payne & Payne (1990) on Yagua: Documents 5 past tenses (immediate, hesternal, week-month, months-years, legendary)
- Only 2 languages worldwide with 4+ distinctions (Yagua, Chakobo)

**Biblical Language Insight**:
- Hebrew wayyiqtol = "narrative engine," NOT temporal distance marker
- Greek aorist = "snapshot" of action, NOT remoteness (Stagg 1972: "The Abused Aorist")
- Discourse analysis: Genre (narrative vs. teaching) determines time reference more than morphology

**Translation Case Studies**:

**Yagua (5-way system)**:
- Genesis 1:1 → MUST use legendary past (value 5) or be semantically incoherent
- Acts 1:1 → Mid-distance past (value 3-4) for Luke's recent work
- Matthew 5:3 → Timeless for teaching content (not past)

**ChiBemba (4+4 symmetric)**:
- Rigid boundaries - using P0 (today) for yesterday = ungrammatical
- Tests TBTA's future granularity annotations (less common cross-linguistically)

**Tagalog (aspect-based)**:
- No tenses, only aspects (perfective, imperfective, contemplated)
- Time distance through adverbs, not verb morphology
- TBTA's listing as "requiring time granularity" may be overstated

**Key Theoretical Insight**: Graded tense has compositional semantics (Mucha 2012 on Gĩkũyũ) - not arbitrary labels but systematic quantification over times.

### 4. Theological Significance ([THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml))

**Default Classification**: ARBITRARY (95%+ of contexts)

**Theological Stakes**: MINIMAL - time granularity rarely affects core doctrine

**Key Principle**: **HISTORICITY matters theologically, TEMPORAL DISTANCE does not.**
- Doctrine: God created (Genesis 1) → critical
- Distance: "Remote past" vs "Legendary past" → arbitrary

**Non-Arbitrary Contexts** (CONTEXTUAL, not DOCTRINAL):

1. **Timeless Teaching vs Historical Narrative**
   - Sermon on Mount: Teaching content = TIMELESS, narrative frame = HISTORIC PAST
   - Affects application (eternal vs culturally bound) but not core doctrine
   - Stakes: MEDIUM

2. **Character Perspective in Discourse**
   - Joseph's brothers: "Yesterday we..." = RECENT from their view, HISTORIC from ours
   - Use character's temporal perspective for clarity
   - Stakes: LOW

3. **Prophecy Fulfillment**
   - Isaiah 53: FUTURE from Isaiah, HISTORIC from Christians, or TIMELESS
   - Translation philosophy choice, not doctrinal determinant
   - Stakes: MEDIUM

4. **Eschatological Prophecy**
   - Revelation: Past visions, future events (or fulfilled?)
   - Doesn't determine eschatological interpretation
   - Stakes: LOW-MEDIUM

**Forbidden Values**: NONE - no time granularity choice is heretical

**Contrast with Other Features**:
- **Number** (Gen 1:26): Dual = HERETICAL (denies Trinity), Trial = CORRECT → HIGH stakes
- **Time Granularity**: All choices acceptable, clarity varies → LOW stakes

## Research Discrepancies

### TBTA vs Linguistic Literature

**Discrepancy 1: Tagalog**
- **TBTA claims**: Tagalog requires time granularity
- **Linguistic research**: Tagalog is aspect-based (no tenses), time via adverbs
- **Resolution**: TBTA may mean "adverbial time framing needed," not grammatical tense
- **Implication**: Algorithm should account for aspectual + adverbial strategies, not just tense

**Discrepancy 2: Value Count**
- **TBTA claims**: "20+ values"
- **Documentation shows**: ~13 values with explicit character codes
- **Resolution**: Complete inventory needs extraction from actual TBTA data exports
- **Implication**: Stage 2 must include data mining to find all 20+ values

**Discrepancy 3: Future Granularity**
- **TBTA claims**: Symmetric system with future distinctions
- **Typology shows**: Future remoteness less common than past
- **Documentation**: Only 1 future value (E = Immediate Future) explicitly coded
- **Resolution**: Future system may be less articulated than past
- **Implication**: Don't assume symmetric past/future in algorithm

## Key Insights for Algorithm Development

### Challenge: Total Inference Required

**Neither Hebrew nor Greek encode time granularity** → ALL values must be inferred from:
1. **Narrative framing** (Genesis = ancient, Gospels = historic, epistles = contemporary to recipients)
2. **Discourse genre** (narrative = time-bound, teaching = timeless, prophecy = future)
3. **Temporal adverbs** (when present: "today," "yesterday," "in those days")
4. **Cultural knowledge** (creation, exodus, Jesus' ministry = known timeframes)
5. **Discourse level** (narrator voice vs character speech)

### Default Heuristic

**Most biblical narrative** = Historic Past (beyond living memory)

Override ONLY when:
- Genre = teaching → timeless
- Direct discourse = character's perspective (may be immediate/recent in their time)
- Explicit temporal adverb forces different value

### Contextual Clues Ranking

1. **Discourse genre** (strongest predictor)
2. **Narrative setting** (Genesis vs Gospels vs Epistles)
3. **Temporal adverbs** (explicit but rare)
4. **Discourse level** (narrator vs character)
5. **Verb aspect** (completive vs ongoing vs gnomic)

### Edge Cases to Handle

1. **Flashbacks**: Time relative to narrative baseline or to characters?
2. **Embedded speech**: Character's "yesterday" = recent to them, historic to us
3. **Prophecy**: Original perspective (future) or fulfillment (past)?
4. **Timeless in narrative**: "God is good" (statement) vs "God created" (event)
5. **Epistles**: Doctrinal (timeless) vs greetings/travel (contemporary to recipients)

## Next Steps for Stage 2

### Language Selection Finalized

Must confirm Bible translation coverage for:
1. Yagua (5-way) - **Critical maximum complexity test**
2. ChiBemba (4+4) - **Symmetric system test**
3. Swahili (2-3) - **Common pattern + major translation language**
4. Tagalog (aspect) - **Edge case (non-tense system)**
5. Controls (0) - **English, Spanish, Mandarin for baseline**

### Data Mining Required

1. Extract complete TBTA time granularity inventory from https://github.com/AllTheWord/tbta_db_export
2. Map all 20+ values to character codes
3. Analyze frequency distribution (which values are common vs rare?)
4. Identify future granularity values (under-documented currently)

### Translation Database Design

**Minimum sample size**: 100 verses per value (statistical power)

**Sampling strategy**:
- OT/NT proportional
- Multiple genres (narrative, teaching, prophecy, epistles)
- Mix of typical and adversarial cases
- Direct discourse + narrator voice
- Temporal adverbs present and absent

**Output format**:
- **Answer sheets**: TBTA annotations (for training/validation)
- **Question sheets**: Raw translations (for discovery analysis)

### Feature Interactions to Explore

1. **Time × Genre**: Narrative vs teaching vs prophecy
2. **Time × Discourse Level**: Narrator vs character speech
3. **Time × Aspect**: How do completive/gnomic aspects interact with time?
4. **Time × Adverbs**: When explicit temporal markers override narrative defaults

## Confidence Assessment

| Research Area | Confidence | Notes |
|---------------|------------|-------|
| TBTA Documentation | HIGH | Clear documentation for ~13 values; gaps for future/rare values |
| Language Typology | HIGH | Strong WALS/Grambank data; Bantu well-documented |
| Source Language Analysis | HIGH | Clear that Hebrew/Greek lack feature; inference required |
| Scholarly Foundation | HIGH | 25+ sources; foundational works (Comrie, Dahl, Nurse) |
| Theological Analysis | MEDIUM-HIGH | Conservative classification; needs peer review |
| Algorithm Feasibility | MEDIUM | Inference challenge is significant but tractable |

## Files in This Directory

1. **[TBTA.md](TBTA.md)** (320 lines) - Complete TBTA documentation review
2. **[LANGUAGES.md](LANGUAGES.md)** (575 lines) - Language family and typology analysis
3. **[SCHOLARLY.md](SCHOLARLY.md)** (870 lines) - 25+ scholarly sources with detailed analysis
4. **[THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)** (380 lines) - Theological arbitrariness classification
5. **README.md** (this file) - Research summary

**Total research output**: ~2,145 lines across 5 documents

---

**Research Complete**: 2025-11-29
**Researcher**: AI System (Claude Sonnet 4.5)
**Ready for**: Stage 2 (Translation Database Generation)
>>>>>>> origin/feat/self-learning-tbta
