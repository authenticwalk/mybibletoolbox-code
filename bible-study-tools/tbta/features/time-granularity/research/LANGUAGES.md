# Language Family & Typology Analysis: Time Granularity

<<<<<<< HEAD
**Feature**: Time Granularity (Temporal Remoteness)
**Research Stage**: Stage 1, Section 2
**Date**: 2025-11-25

## Executive Summary

Time granularity refers to the **temporal remoteness** or **distance from reference point** - not simple tense (past/present/future), but HOW FAR in the past or future an event occurred. This feature is:

- **NOT encoded morphologically in Hebrew/Greek** - temporal distance inferred from context
- **Obligatory in ~150+ languages** across Bantu, Austronesian, Trans-New Guinea, Quechuan families
- **Critical for translation**: Prevents errors like using "recent past" for Genesis creation
- **Variable granularity**: Systems range from 2-way (recent/remote) to 20+ distinctions

**Key Finding**: While source languages (Hebrew/Greek) lack explicit temporal remoteness marking, target languages often REQUIRE translators to choose specific temporal distance markers, making this feature essential for accurate Bible translation.

---

## 1. Source Language Encoding: Hebrew & Greek

### Biblical Hebrew (Afro-Asiatic)

**CRITICAL FINDING**: Hebrew does NOT explicitly encode temporal granularity/remoteness morphologically.

**Temporal System**:
- **Aspect-prominent**, not tense-based {bhebrew-forum}
- **Qatal** (perfect): Completed action - NO temporal distance marker
- **Yiqtol** (imperfect): Incomplete/ongoing - NO temporal distance marker
- **Wayyiqtol**: Narrative sequential - NO temporal distance marker
- **Participle**: Progressive/present - NO temporal distance marker

**Temporal Distance Inference**:
- Context determines remoteness: genealogies, narrative framing, cultural knowledge
- Genesis 1:1 "in the beginning" (בְּרֵאשִׁית) - primordial/ancient time from CONTEXT, not morphology
- No distinction between "yesterday" vs. "6,000 years ago" in verb form

**Source**: {cook-2012-bhvs} - Hebrew verbal system is "aspect-prominent," expressing aspectual, tensed, and modal meanings through context rather than dedicated temporal remoteness morphology.

### Koine Greek (Indo-European)

**CRITICAL FINDING**: Greek does NOT explicitly encode temporal remoteness/granularity morphologically.

**Temporal System**:
- **Aspect-prominent** with tense implications {ntgreek-tenses}
- **Aorist**: Perfective aspect - completed action as whole (no remoteness marking)
- **Present**: Imperfective aspect - ongoing (no temporal distance)
- **Perfect**: Stative aspect - completed with present relevance (not remoteness)
- **Pluperfect**: Anteriority - prior to reference point (relative, not absolute distance)
- **Future**: Prospective - future time (no distance granularity)

**Temporal Distance Inference**:
- Context, not morphology, determines remoteness
- Matthew 1:1 "genealogy of Jesus" - historical distance from discourse framing
- John 1:1 "in the beginning" (Ἐν ἀρχῇ) - timeless/primordial from context

**Important Note**: Greek tense forms indicate aspect (perfective/imperfective/stative) more than temporal remoteness {koine-aspect-guide}.

**Exegetical Warning**: Attaching undue significance to Greek aorist as indicating specific temporal distance is an exegetical fallacy {aorist-fallacy}.

**Source**: {campbell-2007-aspect} - Greek verbal system primarily marks aspect; temporal meaning emerges from context and discourse factors.

### Summary: Source Language Status

| Language | Family | Temporal Remoteness Encoding | How Temporal Distance Expressed |
|----------|--------|------------------------------|----------------------------------|
| Hebrew | Afro-Asiatic | ❌ **ABSENT** | Context, genealogies, narrative framing |
| Greek | Indo-European | ❌ **ABSENT** | Context, discourse structure, adverbials |

**Implication**: Translators working from Hebrew/Greek must INFER temporal remoteness from context, then ENCODE it explicitly in target languages that require grammatical marking.

---

## 2. Language Families Requiring Time Granularity

### Analysis Methodology

Languages analyzed from `/src/constants/languages.tsv` (1,009 total entries, 836 unique language-family pairs).

**Classification Criteria**:
- **Mandatory**: Language MUST grammatically mark temporal remoteness (obligatory)
- **Optional**: Language CAN mark temporal remoteness (context-dependent)
- **Absent**: Language does not mark temporal remoteness
- **(suspected)**: Classification from LLM internal knowledge, not cited research

**Major Families in Corpus** (by count):
1. Austronesian (176)
2. Trans-New Guinea (141)
3. Indo-European (135)
4. Niger-Congo (89)
5. Otomanguean (69)
6. Mayan (41)
7. Australian (36)
8. Afro-Asiatic (25)
9. Sino-Tibetan (18)
10. Quechuan (18)

---

## 3. Typological Classification by Family

### 3.1 Niger-Congo (Bantu) - HIGH GRANULARITY MANDATORY

**Count**: 89 languages in corpus
**Temporal Remoteness**: **MANDATORY** (obligatory marking)
**Source**: {bantu-tam-obligatory}

**Characteristics**:
- **All Bantu languages encode both aspect AND tense** {tense-aspect-niger-congo}
- **Obligatory TAM marking**: 100% of Bantu languages require TAM marking
- **Granularity**: Typically 4-8 temporal distinctions (past + future)
- **Hodiernal distinctions**: Today vs. before-today common

**Temporal Systems**:

**ChiBemba (Zambia)** - Symmetrical 4+4 system:
- **Past**: Today-past, recent past, mid-distance past, remote past
- **Future**: Today-future, near future, mid-distance future, remote future
- **Marking**: Tense/Aspect/Mood prefix + tonal variation
- **Bible**: Revised Bemba Bible (2015) {givon-1972-chibemba}

**Swahili (Tanzania)** - Multiple past markers:
- **-li-**: Recent past (within living memory)
- **-me-**: Perfect (completed, present relevance)
- **-ka-**: Sequential narrative
- **-ki-**: Simultaneous action
- Minimum 2-way remoteness: near vs. remote past (suspected)

**Other Bantu Examples**:
- **Gĩkũyũ (Kenya)**: 4 grades past tense, 3 grades future tense {language-families-doc}
- **Mwera (Tanzania)**: Hodiernal (today) vs. pre-hodiernal (before today) + remote past {language-families-doc}

**Translation Impact**: Translator MUST choose among 4-8 temporal forms for every past/future event.

**Languages in Corpus** (sample): Swahili (swh), Baatonum (bba), Bemba (bem), Shona (sna), Zulu (zul)

---

### 3.2 Austronesian - VARIABLE (LOW TO MEDIUM GRANULARITY)

**Count**: 176 languages in corpus
**Temporal Remoteness**: **OPTIONAL** (27.1% obligatory marking) {tam-obligatory-study}
**Source**: {tense-aspect-mood-family-size}

**Characteristics**:
- **Optional vs. obligatory TAM varies by language**
- **Optionality correlates with time adverbials**: "Yesterday I go" → past inferred from "yesterday"
- **Some languages**: Obligatory preverbal particles/affixes
- **Interaction**: Focus systems affect temporal interpretation

**Aspect-Based Examples**:

**Tagalog (Philippines)** - Aspect-based with temporal adverbs {talkpal-tagalog-tense}:
- **Obligatory aspect marking**: Perfektibo (completed), Imperfektibo (ongoing), Kontemplatibo (contemplated)
- **Optional temporal adverbs** for remoteness specification:
  - *Kagagawa lang* (just now)
  - *Kanina* (earlier today)
  - *Kahapon* (yesterday)
  - *Kamakailan* (recently, days/weeks)
  - *Noong unang panahon* (ancient times)
- **Status**: Temporal remoteness via adverbs, NOT obligatory verb morphology {filipinopod101-tenses}

**Indonesian (Austronesian)** - Optional temporal marking:
- **Sudah**: Already/perfective - completed action
- **Sedang**: Progressive - ongoing action
- **Akan**: Prospective - future action
- **Temporal adverbs**: Required for precision (kemarin=yesterday, dulu=before, nanti=later)
- **Status**: Temporal distance through adverbs, not obligatory morphology (suspected)

**Translation Impact**: Check language-specific requirements; cannot assume obligatory marking across family.

**Languages in Corpus** (sample): Indonesian (ind), Tagalog (tgl), Agutaynen (agn), Ilocano (ilo), Malagasy (mlg)

---

### 3.3 Trans-New Guinea - MEDIUM TO HIGH GRANULARITY MANDATORY

**Count**: 141 languages in corpus
**Temporal Remoteness**: **MANDATORY** (obligatory in most) (suspected)
**Source**: {language-families-doc}

**Characteristics**:
- **Multiple deictic temporal distance markers**
- **Common pattern**: Present → Today's past → Yesterday's past → Remote past → Habitual
- **Hodiernal/hesternal distinctions**: Today vs. yesterday vs. remote
- **Extensive verbal morphology** with large paradigms

**Examples**:

**Amele**: Morphological future affix -an (irrealis), clear present/past/future {language-families-doc}

**Mian**: Verb *s-* 'sleep' grammaticalized into hesternal (yesterday) past - shows verb → tense grammaticalization {language-families-doc}

**Kobon**: Future suffix -nab (irrealis), modal component in future marking {language-families-doc}

**Hodiernal Systems**: Today's past vs. Yesterday's past vs. Remote past - critical for narrative temporal progression

**Translation Impact**: Must verify hodiernal/hesternal distinctions; affects translation of "today" and "yesterday" in narrative.

**Languages in Corpus** (sample): Agarabi (agd), Amele (aey), Benabena (bef), Kamano (kbq), Ömie (aom)

---

### 3.4 Quechuan - MEDIUM GRANULARITY MANDATORY (FUSED WITH EVIDENTIAL)

**Count**: 18 languages in corpus
**Temporal Remoteness**: **MANDATORY** (fused with evidentiality)
**Source**: {language-families-doc}, {beslin-mayan-temporal}

**Characteristics**:
- **Temporal + evidential fusion**: Remoteness AND source of knowledge in same marker
- **Immediate vs. Remote past** with evidential overlay
- **Metaphorical extension**: Temporal distance → narrative structure, emotional affect

**Temporal-Evidential Markers**:

**-rqa/-ra**: Direct experience (witnessed past)
- "I directly witnessed this event"
- Recent events speaker participated in
- Narrative introduction and explanations

**-sqa/-sha**: Indirect experience (non-witnessed/remote past)
- Events not directly experienced or before speaker's lifetime
- Used for ancient historical events (Genesis creation)
- Developed from present perfect morphology

**South Conchucos Quechua**:
- Remote past for peripheral narrative (orientation, side remarks)
- Immediate past for main narrative events
- Emotional distance: Events speaker regrets may use remote past even if recent

**Translation Examples**:
- Genesis 1:1 "In the beginning God created" → **-sqa/-sha** (remote, not witnessed)
- Mark 1:21 "They went into Capernaum" → **-rqa/-ra** (narrative mainline, witnessed tradition)
- Acts 2:1 "When Pentecost came" → **-sqa/-sha** (historical, not personally witnessed)

**Languages in Corpus** (sample): Quechua, South Bolivian (quh), Quechua, Cusco (quz), Quechua, Ayacucho (quy)

---

### 3.5 Otomanguean - MEDIUM GRANULARITY MANDATORY

**Count**: 69 languages in corpus
**Temporal Remoteness**: **MANDATORY** (100% obligatory TAM marking) {tam-obligatory-study}
**Source**: {tense-aspect-mood-family-size}

**Characteristics**:
- **Aspect more relevant than tense** in verbal system {otomanguean-gulper}
- **100% obligatory TAM marking** - highest prevalence alongside Indo-European, Afro-Asiatic
- **Valency and aspect** marked by prefixes/proclitics
- **Temporal distinctions**: Multiple past/future degrees (specific systems vary by language)

**Translation Impact**: ALL Otomanguean languages require explicit TAM marking; translator must select temporal form.

**Languages in Corpus** (sample): Amuzgo, Guerrero (amu), Amuzgo, San Pedro Amuzgos (azg), Chinantec (various), Mixtec (various)

---

### 3.6 Mayan - ASPECT-BASED (LOW TEMPORAL GRANULARITY)

**Count**: 41 languages in corpus
**Temporal Remoteness**: **OPTIONAL** (aspect-based, not tense-based)
**Source**: {mayan-temporal-beslin}, {language-families-doc}

**Characteristics**:
- **Tenseless systems** (traditionally): Binary aspect (completive vs. incompletive)
- **Recent debate**: Some scholars argue K'iche' markers are tense, not aspect {beslin-tense-kiche}
- **Proto-Mayan**: 7 aspects (incompletive, progressive, completive, imperative, potential, optative, perfective)
- **Temporal meaning**: From CONTEXT + ASPECT, not dedicated tense affixes

**Temporal Expression**:
- **Completive aspect**: Completed events (past interpretation in narrative)
- **Incompletive aspect**: Ongoing/habitual (present/future interpretation)
- **Context determines**: Whether event is recent past vs. remote past

**Recent Development**:
- Colonial/post-colonial: Continuous formation of TAM auxiliaries {language-families-doc}
- Yucatec Maya: Grammaticalization of auxiliaries for finer TAM distinctions
- Shift from status system to auxiliary-based system

**Translation Impact**: Cannot map English tenses directly; must analyze aspect and context.
- Prophecy: Incompletive/potential aspect
- Narrative: Completive aspect
- Teaching: Incompletive for ongoing truths

**Languages in Corpus** (sample): Achi (acr), Akateko (knj), Awakateko (agu), K'iche' (quc), Mam (mam)

---

### 3.7 Australian - VARIABLE (MEDIUM GRANULARITY)

**Count**: 36 languages in corpus
**Temporal Remoteness**: **OPTIONAL TO MANDATORY** (varies by language) (suspected)
**Source**: {language-families-doc}

**Characteristics**:
- **Relative vs. absolute tense** (some languages distinguish)
- **Grammatical expression**: Through clitics/particles, not inflections
- **Mixed focus/temporal meaning**: Elements paraphrased as 'now' vs. 'then'
- **Tense-case interactions** in Pama-Nyungan languages
- **Modal-tense interactions**: Creating hypothetical/counterfactual meanings

**Narrative Function**:
- **Temporal/focus clitics CRUCIAL** for proper ordering in narrative events
- Distinct from Indo-European temporal connectives
- Wrong clitic choice disrupts narrative flow

**Research Gap**: Subtle, context-sensitive TAME categories difficult to document; requires native speaker consultation {language-families-doc}

**Translation Challenge**: Limited documentation; requires native speaker input for accurate temporal marking.

**Languages in Corpus** (sample): Arrernte, Eastern (aer), Alyawarr (aly), Anmatyerre (amx), Anindilyakwa (aoi), Awabakal (awk)

---

### 3.8 Indo-European - LOW GRANULARITY OPTIONAL

**Count**: 135 languages in corpus
**Temporal Remoteness**: **OPTIONAL** (adverbials, not obligatory morphology)
**Source**: Internal knowledge (suspected)

**Characteristics**:
- **Simple past/present/future** with adverbials for specificity
- **Temporal distance NOT grammatically obligatory**
- **English**: Past/present/future + adverbs ("yesterday," "long ago," "recently")
- **Spanish**: Preterite vs. imperfect (aspect-based) + adverbs
- **German**: Perfect vs. simple past (more regional than temporal) + adverbs
- **Russian**: NO pluperfect or future perfect - uses absolute tenses {relative-absolute-tense-wiki}

**Translation Impact**: Temporal remoteness expressed through optional adverbials, not obligatory morphology.

**Languages in Corpus** (sample): English (eng), Spanish (spa), German (deu), French (fra), Portuguese (por), Russian (rus)

---

### 3.9 Afro-Asiatic (excluding Hebrew) - VARIABLE

**Count**: 25 languages in corpus
**Temporal Remoteness**: **OPTIONAL TO MANDATORY** (varies by branch)
**Source**: {tam-obligatory-study}, internal knowledge (suspected)

**Characteristics**:
- **Arabic (Standard)**: Perfect/imperfect aspect-based system; temporal distance through context + adverbs (suspected)
- **Assyrian Neo-Aramaic**: Similar to Hebrew; aspect-prominent (suspected)
- **Amharic (Ethiopia)**: Perfective/imperfective aspect; temporal adverbs for remoteness (suspected)

**Translation Impact**: Varies by language; check specific branch (Semitic, Cushitic, Chadic).

**Languages in Corpus** (sample): Arabic, Standard (arb), Hebrew (heb), Hebrew, Ancient (hbo), Assyrian Neo-Aramaic (aii)

---

### 3.10 Sino-Tibetan - ASPECT-BASED (OBLIGATORY TEMPORAL ADVERBS)

**Count**: 18 languages in corpus
**Temporal Remoteness**: **OPTIONAL MORPHOLOGY, MANDATORY ADVERBS**
**Source**: {mandarin-time-expressions}

**Characteristics**:
- **NO grammatical tense** in Mandarin Chinese
- **Aspect particles**: 了 (le) perfective, 过 (guo) experiential, 着 (zhe) durative
- **Temporal adverbs OBLIGATORY** for time specification:
  - 刚才 (gāngcái): Just now
  - 昨天 (zuótiān): Yesterday
  - 以前 (yǐqián): Before/in the past
  - 古代 (gǔdài): Ancient times
  - 将来 (jiānglái): Future

**Mandarin Temporal Precision**:
- **Measure words obligatory**: 点 (diǎn) for hour, 分 (fēn) for minute {mandarin-time-guide}
- **Hierarchical structure**: Largest time unit → smallest (year → month → day → hour)
- **No prepositions**: Time expressions precede verb directly
- **Sentence position**: Time expression typically precedes verb

**Translation Impact**: While morphology doesn't encode remoteness, temporal adverbs + aspect particles create OBLIGATORY temporal context.

**Languages in Corpus** (sample): Chinese, Mandarin (cmn), Zaiwa (atb)

---

## 4. Root Languages Analysis

**Root Languages**: Major Bible translation languages translators often start from (priority: Hebrew, Greek, then regional parent languages).

| Language | ISO-639-3 | Family | Temporal Remoteness | Role in Translation | Corpus Count |
|----------|-----------|--------|---------------------|---------------------|--------------|
| **Hebrew** | heb/hbo | Afro-Asiatic | ❌ Absent | Source language (OT) | 3 versions |
| **Greek** | grc | Indo-European | ❌ Absent | Source language (NT) | 8 versions |
| **Latin** | lat | Indo-European | ❌ Absent (optional) | Historical bridge | 1 version |
| **English** | eng | Indo-European | ❌ Optional | Major bridge language | 44 versions |
| **Spanish** | spa | Indo-European | ❌ Optional | Regional bridge (Latin America) | 6 versions |
| **French** | fra | Indo-European | ❌ Optional | Regional bridge (Francophone Africa) | 4 versions |
| **German** | deu | Indo-European | ❌ Optional | Regional bridge (Europe) | 4 versions |
| **Portuguese** | por | Indo-European | ❌ Optional | Regional bridge (Brazil, Africa) | 4 versions |
| **Russian** | rus | Indo-European | ❌ Optional | Regional bridge (Eastern Europe) | 1 version |
| **Arabic** | arb | Afro-Asiatic | ❌ Optional (suspected) | Regional bridge (Middle East, N. Africa) | 2 versions |
| **Indonesian** | ind | Austronesian | ❌ Optional | Regional bridge (SE Asia) | 2 versions |
| **Swahili** | swh | Niger-Congo | ✅ **Mandatory** | Regional bridge (E. Africa) | 3 versions |
| **Mandarin** | cmn | Sino-Tibetan | ⚠️ Adverbs mandatory | Regional bridge (E. Asia) | 3 versions |

**Key Insight**: Most root languages (Hebrew, Greek, English, Spanish, French, German, Portuguese, Arabic, Indonesian) do NOT obligatorily encode temporal remoteness. **Swahili is the EXCEPTION** - a major regional bridge language with obligatory temporal granularity marking.

**Translation Implications**:
- Translators from English/Spanish → Bantu languages must ADD temporal remoteness (not in source)
- Translators from Hebrew/Greek → ANY language must INFER temporal remoteness from context
- Swahili translations can serve as **models** for temporal remoteness decisions in other Bantu target languages

---

## 5. Candidate Languages for Translation Database (Stage 2)

**Selection Criteria**:
- Mix of marking vs. non-marking languages
- Diverse language families
- Available in corpus (languages.tsv)
- Represent different temporal granularity systems
- Include at least one root/bridge language

### Recommended 10 Candidate Languages

| # | Language | ISO-639-3 | Family | Temporal Remoteness | Granularity Level | Rationale |
|---|----------|-----------|--------|---------------------|-------------------|-----------|
| 1 | **English** | eng | Indo-European | Optional | Low (3-way) | Root language; baseline for comparison |
| 2 | **Swahili** | swh | Niger-Congo (Bantu) | **Mandatory** | Medium-High (5-8 distinctions) | Bridge language + obligatory marking |
| 3 | **Mandarin** | cmn | Sino-Tibetan | Adverbs mandatory | Medium (aspect + adverbs) | Major bridge language; aspect-based system |
| 4 | **Quechua, Cusco** | quz | Quechuan | **Mandatory** | Medium (fused evidential) | Temporal-evidential fusion |
| 5 | **Tagalog** | tgl | Austronesian | Optional (adverbs) | Medium (aspect + adverbs) | Aspect-based Austronesian; temporal adverbs |
| 6 | **Amele** | aey | Trans-New Guinea | **Mandatory** | Medium (hodiernal system) | Trans-New Guinea representative |
| 7 | **K'iche'** | quc | Mayan | Optional | Low (aspect-based) | Aspect-based, minimal temporal remoteness |
| 8 | **Amuzgo, Guerrero** | amu | Otomanguean | **Mandatory** | Medium | 100% obligatory TAM family |
| 9 | **Spanish** | spa | Indo-European | Optional | Low (aspect + adverbs) | Major bridge language; preterite/imperfect |
| 10 | **Indonesian** | ind | Austronesian | Optional | Low (adverbs) | Bridge language; optional TAM |

**Additional Candidates** (if resources allow):
- **Bemba** (bem): Niger-Congo - Symmetrical 4+4 system (if available in corpus)
- **Arrernte, Eastern** (aer): Australian - Tense-case interactions
- **Achi** (acr): Mayan - Additional Mayan representative

---

## 6. Cultural Nuances: Calendars and Time Reckoning

### 6.1 Lunar Calendar Systems

**Prevalence**: Probably most humans use lunar-based calendars {lunar-calendar-systems}
**Families**: Chinese, Indian, Islamic, Jewish, several indigenous cultures
**Historical**: Earliest detectable timing systems (Stone Age) {lunar-calendar-systems}

**Lunisolar Calendars** (month tied to moon, year adjusted to sun):
- Chinese, Buddhist, Burmese, Hebrew, Jain, Nepali, Hindu, Japanese, Korean, Mongolian, Tibetan, Vietnamese

**Pure Lunar Calendars** (Islamic):
- Islamic months shift through all four seasons over 33-year cycle {calendar-ancient-systems}

**Biblical Context**:
- **Hebrew calendar**: Lunisolar, months of 29-30 days {hebrew-calendar-wiki}
- **Month names**: Numbers (first month, second month) by 6th century BCE; later Babylonian-Aramaic names (Tishri, Kislev)
- **Day beginning**: Genesis 1 suggests morning start; later texts (Exodus 12:18) indicate sunset start

**Translation Impact**: Genesis creation days ("evening and morning") reflect Hebrew sunset-to-sunset reckoning; affects temporal framing.

---

### 6.2 Event-Based Time Reckoning

**Definition**: Time intervals defined by events, not metric units {event-based-time-amazonian}

**Examples**:

**Huni-Kuĩ, Awetý, Kamaiurá (Amazonian/Xinguan)**:
- **Exclusively event-based time intervals**
- Rich lexical/phrasal expressions based on:
  - Environmental indices (rainy season, dry season)
  - Celestial indices (moon phases, sun position)
  - Social norms (planting time, harvest time)
- **Non-metric**: "One planting season ago" not "three months ago"

**Amondawa, Yélî Dnye**: Similar event-based systems

**Translation Impact**:
- "In the beginning" (Genesis 1:1) may map to "at creation time" (event-based)
- "The third day" (Genesis 1:13) may require event framing, not metric days
- "40 days and 40 nights" (Genesis 7:12) - may translate as "rainy season" in event-based cultures

---

### 6.3 Relative Hour Systems

**Hebrew/Jewish Context**:
- **Relative hour** (*shaʿah zǝmanit*): Divides day into 12 hours, night into 12 hours, year-round {relative-hour-wiki}
- **Variable length**: One hour ≈ 45 minutes (winter solstice) to 75 minutes (summer solstice) at Mediterranean latitude
- **Biblical reference**: "The third hour," "the sixth hour," "the ninth hour" in Gospels

**Translation Impact**:
- New Testament time references ("third hour" = ~9 AM) use relative hours
- Target languages may need cultural notes or metric conversion
- Hour-marking languages (Mandarin 点 diǎn) may require precision choices

---

### 6.4 Absolute vs. Relative Time

**Absolute Tense**: Event time relative to speech moment (most tensed languages) {relative-absolute-tense-wiki}
**Relative Tense**: Event time relative to another event (pluperfect, future perfect)

**Cross-Linguistic Variation**:
- **Russian**: NO pluperfect or future perfect; uses absolute past/future instead
- **Burmese, Dyirbal, Chinese**: Tenseless languages (no grammatical tense)

**Event-Based vs. Deictic Time** {event-based-time-cognition}:
- **D-time (Deictic/A-series)**: Centered on speaker's "now" (ego-based reference point)
- **S-time (Sequential/B-series)**: Event-independent temporal sequence ("X happened before Y")
- **Cultural variation**: Event-independent metric "time as such" is NOT universal; it's a cultural/historical construction based on cognitive technologies

**Translation Impact**:
- Western "clock time" concepts may not exist in event-based cultures
- "At the sixth hour" (John 4:6) may need event framing: "at midday" or "when sun highest"

---

## 7. Temporal Precision Requirements: Classification

### High Precision Required (Hour/Minute Level)

**Languages with obligatory hour markers**:
- **Mandarin Chinese**: 点 (diǎn) for hour, 分 (fēn) for minute - grammatically obligatory {mandarin-time-guide}
- **Japanese**: 時 (ji) for hour, 分 (fun) for minute (suspected)
- **Korean**: 시 (si) for hour, 분 (bun) for minute (suspected)

**Biblical Context**: "About the sixth hour" (John 19:14), "at the third hour" (Acts 2:15) - require precision in hour-marking languages.

---

### Medium Precision Required (Day/Week/Month Level)

**Languages with obligatory day-level distinctions**:
- **Bantu hodiernal systems**: Today vs. yesterday vs. before-yesterday
- **Trans-New Guinea hesternal systems**: Today vs. yesterday vs. remote
- **Tagalog**: Immediate/today/yesterday/recent distinctions

**Biblical Context**: "On the third day" (Genesis 1:13), "after three days" (Mark 8:31) - require day-level precision.

---

### Low Precision Required (General Past/Future)

**Languages with 2-4 way systems**:
- **Most Indo-European**: Past/present/future (+ perfect forms)
- **Mayan**: Completive/incompletive aspect
- **Some Austronesian**: Perfective/imperfective with optional temporal adverbs

**Biblical Context**: General narrative past ("God created") maps easily to simple past.

---

## 8. Summary: Key Findings

### Source Language Encoding
- ❌ **Hebrew**: NO explicit temporal remoteness morphology (aspect-based, context determines)
- ❌ **Greek**: NO explicit temporal remoteness morphology (aspect-based, context determines)

### Language Family Patterns

| Family | Count | Obligatory? | Granularity | Key Pattern |
|--------|-------|-------------|-------------|-------------|
| **Niger-Congo (Bantu)** | 89 | ✅ 100% | High (4-8 distinctions) | Hodiernal/pre-hodiernal + remote |
| **Austronesian** | 176 | ⚠️ 27% | Variable (low-high) | Optional TAM, adverb-dependent |
| **Trans-New Guinea** | 141 | ✅ Majority | Medium-High | Hodiernal/hesternal systems |
| **Quechuan** | 18 | ✅ 100% | Medium (fused evidential) | Temporal + evidential fusion |
| **Otomanguean** | 69 | ✅ 100% | Medium | Aspect-based, obligatory TAM |
| **Mayan** | 41 | ❌ Optional | Low (aspect-based) | Completive/incompletive aspect |
| **Australian** | 36 | ⚠️ Variable | Medium | Clitics/particles, tense-case interaction |
| **Indo-European** | 135 | ❌ Optional | Low (adverbs) | Simple tense + adverbials |
| **Sino-Tibetan** | 18 | ⚠️ Adverbs mandatory | Medium (aspect + adverbs) | Aspect particles + temporal adverbs |
| **Afro-Asiatic** | 25 | ⚠️ Variable | Low-Medium | Aspect-based (Hebrew/Arabic) |

### Root Languages
- **11/13 root languages**: Optional/absent temporal remoteness
- **1/13 root language**: Mandatory (Swahili)
- **1/13 root language**: Mandatory adverbs (Mandarin)

### Cultural Nuances
- **Lunar calendars**: Chinese, Hebrew, Islamic systems affect temporal framing
- **Event-based time**: Amazonian/Xinguan languages use non-metric intervals
- **Relative hours**: Biblical "third hour," "sixth hour" use variable-length hours
- **Absolute vs. Relative**: Cross-linguistic variation in temporal reference frames

### Candidate Languages (10)
1. English (baseline)
2. Swahili (Bantu, obligatory, bridge)
3. Mandarin (aspect + adverbs, bridge)
4. Quechua, Cusco (evidential fusion)
5. Tagalog (high granularity)
6. Amele (Trans-New Guinea)
7. K'iche' (Mayan, aspect-based)
8. Amuzgo, Guerrero (Otomanguean, obligatory)
9. Spanish (bridge, aspect-based)
10. Indonesian (optional, bridge)

---

## 9. Bibliography & Sources

**WALS & Grambank**:
- {wals-tense-chapter-66} - WALS Chapter 66: The Past Tense - https://wals.info/chapter/66
- {wals-future-tense-67} - WALS Chapter 67: The Future Tense - https://wals.info/chapter/67
- {grambank-gb309} - Grambank Feature GB309: Multiple past/future tenses - https://grambank.clld.org/parameters/GB309
- {grambank-gb083} - Grambank Feature GB083: Past tense morphology - https://grambank.clld.org/parameters/GB083

**Hebrew Sources**:
- {bhebrew-forum} - Does Hebrew have tense and aspect? - https://bhebrew.biblicalhumanities.org/viewtopic.php?t=930
- {cook-2012-bhvs} - Cook, John A. (2012). *Time and the Biblical Hebrew Verb* - Academic study of Hebrew aspect-prominent system
- {bergstrom-2020-aspect} - Bergström, Ulf. *Aspect, Communicative Appeal, and Temporal Meaning in Biblical Hebrew* - https://www.eisenbrauns.org/books/titles/978-1-64602-140-6.html

**Greek Sources**:
- {ntgreek-tenses} - The Tenses in New Testament Greek - https://www.newtestamentgreek.net/the-tenses-in-new-testament-greek.html
- {koine-aspect-guide} - A brief guide to aspect in Greek: Part I - https://koine-greek.com/2021/12/15/a-brief-guide-to-aspect-in-greek-part-i/
- {aorist-fallacy} - The Aorist Tense In Koine Greek: A Simple Guide - https://www.mezzoguild.com/learn/greek/grammar/koine-aorist-tense/
- {campbell-2007-aspect} - Campbell, Constantine R. (2007). *Verbal Aspect in New Testament Greek*

**Cross-Linguistic Typology**:
- {relative-absolute-tense-wiki} - Relative and absolute tense - https://en.wikipedia.org/wiki/Relative_and_absolute_tense
- {event-based-time-amazonian} - Event-Based Time in Three Indigenous Amazonian and Xinguan Cultures - https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.00454/full
- {event-based-time-cognition} - Time, space, and events in language and cognition: A comparative view - ResearchGate
- {temporal-frames-reference} - Temporal frames of reference - ResearchGate

**Bantu Sources**:
- {tense-aspect-niger-congo} - Tense and Aspect in Niger-Congo - https://www.africamuseum.be/.../tense-aspect-niger-congo.pdf
- {bantu-tam-obligatory} - Tense and Aspect in Bantu - ResearchGate
- {tam-obligatory-study} - Tense–aspect–mood marking, language-family size and evolution of predication - PMC - https://pmc.ncbi.nlm.nih.gov/articles/PMC8059509/
- {givon-1972-chibemba} - Givón, Tom (1972). *Studies in ChiBemba and Bantu grammar*

**Austronesian & Other Families**:
- {tense-aspect-mood-family-size} - Tense–aspect–mood marking, language-family size - Royal Society Publishing - https://royalsocietypublishing.org/doi/10.1098/rstb.2020.0194
- {talkpal-tagalog-tense} - Tagalog Verb Tenses in Tagalog Grammar - Talkpal - https://talkpal.ai/grammar/tagalog-verb-tenses-in-tagalog-grammar/
- {filipinopod101-tenses} - Filipino Tenses: Expressing the Past, Present, and Future - FilipinoPod101 - https://www.filipinopod101.com/blog/2021/07/08/filipino-tenses/
- {tagalog-conjugation-ling} - Tagalog Conjugation: Beginner's Guide To Verbs And Aspects - Ling App - https://ling-app.com/blog/tagalog-conjugation/

**Quechuan Sources**:
- {hintz-quechua-past} - Hintz, Diane. *Past tense forms and their functions in South Conchucos Quechua*

**Mayan Sources**:
- {mayan-temporal-beslin} - Bešlin, Maša. *A Mayan temporal puzzle* - https://www.masabeslin.com/assets/pdf/beslin_mayan_temporal.pdf
- {beslin-tense-kiche} - Bešlin, Maša. *Reanalyzing K'iche' as a Tensed Language* - https://www.masabeslin.com/assets/pdf/beslin_tense.pdf
- {mayan-languages-wiki} - Mayan languages - Wikipedia - https://en.wikipedia.org/wiki/Mayan_languages

**Otomanguean Sources**:
- {otomanguean-gulper} - Otomanguean - http://www.languagesgulper.com/eng/Otomanguean.html

**Mandarin Sources**:
- {mandarin-time-expressions} - Chinese Time Expressions: Comprehensive Guide - https://www.vaia.com/en-us/explanations/chinese/chinese-grammar/chinese-time-expressions/
- {mandarin-time-guide} - Complete Guide to Time in Chinese - https://www.mandarinblueprint.com/blog/time-in-chinese-character-shi/

**Calendar & Time Systems**:
- {hebrew-calendar-wiki} - Hebrew calendar - Wikipedia - https://en.wikipedia.org/wiki/Hebrew_calendar
- {relative-hour-wiki} - Relative hour - Wikipedia - https://en.wikipedia.org/wiki/Relative_hour
- {lunar-calendar-systems} - Lunar Calendars and How They Differ - https://time.now/articles/lunar-vs-solar-calendar/
- {calendar-ancient-systems} - Calendar - Ancient, Religious, Systems - Britannica - https://www.britannica.com/science/calendar/Ancient-and-religious-calendar-systems

**Project Documentation**:
- {time-granularity-archive} - `/bible-study-tools/tbta/features/features-archive/time-granularity/README.md`
- {language-families-doc} - `/plan/tbta/tbta-rebuild-with-llm/features/time-granularity/language-families.md`

**Corpus Analysis**:
- {languages-tsv} - `/src/constants/languages.tsv` (1,009 entries, 836 unique language-family pairs)

---

**Last Updated**: 2025-11-25
**Research Stage**: Stage 1, Section 2 (Language Family & Typology Analysis)
**Agent**: Claude Code (Sonnet 4.5)
**Verification Status**: Sources cited inline; classifications marked (suspected) where based on LLM knowledge vs. cited research
=======
**Feature**: Time Granularity
**Analysis Date**: 2025-11-29
**Scope**: Cross-linguistic variation in temporal remoteness/distance marking

## Executive Summary

Time granularity (temporal remoteness/metrical tense) is a **critical but unevenly distributed** linguistic feature. Approximately **20% of world languages** grammatically encode temporal distance, with the richest systems found in:
- **Bantu languages** (Africa): 80% make multiple past distinctions
- **Some Austronesian languages** (Pacific/Southeast Asia): Variable systems
- **Some Amazonian languages** (South America): Including the richest known system (Yagua, 5 past tenses)
- **Select languages across other families**: Including some Turkic, Mongolic, and Finno-Ugric

**Critical finding**: Hebrew and Greek do NOT grammatically encode time granularity, making TBTA annotations purely contextual/inferential.

## Sources

- {wals-66} - [WALS Online - Chapter The Past Tense](https://wals.info/chapter/66)
- {wals-feat-66a} - [WALS Online - Feature 66A: The Past Tense](https://wals.info/feature/66A)
- {languages-of-world-past} - [Considering the past | Languages Of The World](https://www.languagesoftheworld.info/linguistic-typology/considering-the-past.html)
- {temporal-remoteness-libretexts} - [21.5: Temporal Remoteness markers ("metrical tense") - Social Sci LibreTexts](https://socialsci.libretexts.org/Bookshelves/Anthropology/Linguistics/Book:_Analyzing_Meaning_-_An_Introduction_to_Semantics_and_Pragmatics_(Kroeger)/21:_Tense/21.05:_Temporal_Remoteness_markers_(metrical_tense))
- {yagua-wals} - [WALS Online - Chapter The Past Tense](https://wals.info/chapter/66)
- {bantu-tense-springer} - [Beyond the past, present, and future: towards the semantics of 'graded tense' in Gĩkũyũ | Natural Language Semantics](https://link.springer.com/article/10.1007/s11050-012-9092-3)
- {tagalog-aspect-groningen} - [Time reference in Tagalog: Verbal aspect and morphological complexity](https://research.rug.nl/en/publications/time-reference-in-tagalog-verbal-aspect-and-morphological-complex)
- {tenseless-languages-compass} - [Languages Without Tense - Toosarvandani - 2025 - Language and Linguistics Compass](https://compass.onlinelibrary.wiley.com/doi/full/10.1111/lnc3.70017)
- {hesternal-wikipedia} - [Hesternal tense - Wikipedia](https://en.wikipedia.org/wiki/Hesternal_tense)
- {grammatical-tense-wikipedia} - [Grammatical tense - Wikipedia](https://en.wikipedia.org/wiki/Grammatical_tense)

## Source Language Encoding

### Hebrew: NOT Encoded

**Hebrew verbal morphology does NOT explicitly encode time granularity.** {llm-cs45}

Hebrew tense-aspect system:
- **Perfect (qatal)**: Completed action
- **Imperfect (yiqtol)**: Incomplete/future action
- **Participle**: Ongoing action
- **Infinitive**: Non-finite forms
- **Wayyiqtol**: Narrative past (consecutive imperfect)

**Temporal distance encoding**: NONE. Hebrew uses context, temporal adverbs, and narrative framing to indicate when events occurred, but has NO grammatical morphology distinguishing "yesterday" vs "last week" vs "ancient times."

**Implication**: TBTA time granularity values for Hebrew texts are **100% inferential**, based on:
- Narrative context (Genesis = ancient, Prophets = historic)
- Temporal adverbs when present
- Cultural/historical knowledge
- Discourse genre (teaching vs narrative)

### Greek: NOT Encoded

**Greek verbal morphology does NOT explicitly encode time granularity.** {llm-cs45}

Greek tense system:
- **Present**: Current action
- **Imperfect**: Past ongoing
- **Aorist**: Past simple/punctiliar
- **Perfect**: Completed with present relevance
- **Pluperfect**: Past perfect
- **Future**: Future action

**Temporal distance encoding**: NONE. Greek tenses indicate basic time reference (past/present/future) and aspect (perfective/imperfective), but do NOT grammatically distinguish temporal remoteness.

**Example**: The Greek aorist can represent:
- Immediate past: "I just ate" (few hours ago)
- Recent past: "I ate yesterday"
- Remote past: "I ate last year"
- Historic past: "Abraham ate" (thousands of years ago)

**Implication**: TBTA time granularity values for Greek texts are **100% inferential**, based on the same contextual factors as Hebrew.

## Linguistic Typology

### Global Distribution

**WALS Finding**: As many as **one-fifth of world languages** (approximately 20%) make remoteness distinctions {wals-66}

#### WALS Feature 66A Classification

Languages fall into four categories {wals-feat-66a}:

1. **No past tense** (~40% of languages): Tenseless, aspect-only systems
2. **Present with no remoteness distinctions** (~40%): Simple past/non-past
3. **Present with 2-3 remoteness distinctions** (~17%): Common graded tense
4. **Present with 4+ remoteness distinctions** (~3%): Rare, highly articulated systems

### Terminology

**Standard terms** in linguistic literature {temporal-remoteness-libretexts} {hesternal-wikipedia}:

| Term | Meaning | Latin Origin |
|------|---------|--------------|
| **Hodiernal** | Today (past or future) | hodie "today" |
| **Hesternal** | Yesterday | hesternus "yesterday" |
| **Pre-hesternal** | Before yesterday | (before + hesternal) |
| **Post-hodiernal** | After today | (after + hodiernal) |
| **Crastinal** | Tomorrow | crastinus "tomorrow" |
| **Metrical/Graded Tense** | Distance-based tense systems | (measurement-based) |
| **Temporal Remoteness** | General term for all such systems | (generic technical term) |

**Common division**: Almost universally, the primary division is between **hodiernal** (today) and **pre-hodiernal** (before today). Further subdivisions vary by language {hesternal-wikipedia}.

## Family-Level Analysis

### 1. Bantu Languages (Niger-Congo)

**Status**: MANDATORY for 80%+ of Bantu languages {languages-of-world-past}

**Distribution** (Nurse 2008, cited in {languages-of-world-past}):
- **210 Bantu languages surveyed**
- **80% have 2+ past distinctions**
- **50% have only 1 future distinction**
- **Most common**: 2-3 past tenses (70%+)
- **Rare**: 4 past tenses (10 languages)
- **Controversial**: 5 past tenses (some Congo varieties)

**Example: ChiBemba (Bemba)** {temporal-remoteness-libretexts}
- **System**: Symmetric 4 past + 4 future (plus present)
- **Location**: Zambia (Central Bantu)
- **Note**: One of the few symmetric systems (most Bantu have more past than future)

**Example: Haya** {hesternal-wikipedia}
- **System**: 3-way past distinction
  - Hodiernal (today)
  - Hesternal (yesterday)
  - Pre-hesternal (before yesterday)
- **Boundaries**: Rigid - cannot use hodiernal for pre-hodiernal events

**Example: Gĩkũyũ (Kikuyu)** {bantu-tense-springer}
- **System**: Graded/metrical tense with multiple past distinctions
- **Semantics**: Quantificational tenses (work like quantifiers over times)
- **Note**: Subject of detailed semantic analysis

**Other Bantu examples** {hesternal-wikipedia}:
- Zulu, Sesotho, Luganda: 2-3 way remoteness distinctions

**In our database**: Multiple Bantu languages present, including varieties from East Africa, Southern Africa

### 2. Austronesian Languages (Pacific/Southeast Asia)

**Status**: HIGHLY VARIABLE - ranges from absent to moderate complexity

**Tagalog (tgl)** {tagalog-aspect-groningen}
- **System**: Aspect-based, NOT primarily tense-based
- **Aspects**: Perfective, Imperfective, Contemplated
- **Time reference**: Achieved through aspect + temporal adverbs
- **Morphology**: Agglutinative, complex affix system (prefix, infix, suffix, circumfix)
- **Note**: TBTA lists Tagalog as requiring time granularity, but linguistic literature emphasizes aspect over tense
- **Assessment**: Time granularity may be OPTIONAL or expressed lexically rather than grammatically
- **In our database**: Yes (tgl-tglulb.txt)

**Hawaiian** {tenseless-languages-compass}
- **System**: NO past tense marking
- **Category**: Tenseless language
- **Time reference**: Lexical items (adverbs) and aspect
- **Assessment**: Time granularity is ABSENT
- **In our database**: Not found in sample

**Other Austronesian**: Highly diverse family with wide variation in tense-aspect systems

### 3. Amazonian Languages

**Status**: Some languages have richest known temporal remoteness systems

**Yagua (yad - Peba-Yaguan, Peru)** {yagua-wals}
- **System**: **5 degrees of past remoteness** - richest in WALS sample
- **Categories**:
  1. A few hours ago (immediate past)
  2. One day ago (yesterday/hesternal)
  3. Roughly 1 week to 1 month ago
  4. Roughly 1-2 months up to 1-2 years ago
  5. Distant/legendary past (historic)
- **Source**: Payne & Payne (1990: 386-388)
- **Note**: Only 2 languages in WALS with 4+ distinctions (Yagua and Chakobo, both Western Amazonia)
- **In our database**: Yes (yad-yadNT.txt)

**Guajajára (Tupi-Guaraní, Brazil)** (cited in {languages-of-world-past})
- **System**: Past temporal reference with remoteness distinctions
- **Family**: Related to Guarani (which is tenseless in some analyses)
- **Note**: Variation within Tupi-Guaraní family

**Pano languages** (cited in {languages-of-world-past})
- **Research**: Detailed study of degrees of temporal remoteness
- **Location**: Western Amazon (Peru/Brazil border)

### 4. Indo-European Languages

**Status**: MOSTLY ABSENT, with rare exceptions

**English, Spanish, German, French, Portuguese**: NO time granularity
- Simple past/present/future with NO remoteness distinctions
- Time distance expressed ONLY through adverbs ("just now", "yesterday", "long ago")
- **Assessment**: ABSENT

**Russian, Polish (Slavic)**: NO time granularity
- Rich aspect systems (perfective/imperfective) but NO remoteness
- **Assessment**: ABSENT

**Greek (Ancient & Modern)**: NO time granularity
- See "Source Languages" above
- **Assessment**: ABSENT

**Albanian (als - Tosk)** {llm-cs45} (suspected)
- **Assessment**: Likely ABSENT (standard IE pattern)
- **In our database**: Yes (als-alsSHQ.txt)

**Balochi (Indo-Iranian)** {hesternal-wikipedia}
- **System**: 2-3 way remoteness distinction
- **Note**: Rare within Indo-European
- **Assessment**: OPTIONAL or MANDATORY (requires verification)
- **In our database**: Not found in sample

### 5. Sino-Tibetan Languages

**Status**: MOSTLY ABSENT (tenseless)

**Mandarin Chinese** {tenseless-languages-compass}
- **System**: NO tense, aspect-only
- **Aspects**: Perfective (le), experiential, durative, etc.
- **Time reference**: Adverbs + aspect + context
- **Assessment**: Time granularity ABSENT
- **In our database**: Not found in sample (but likely present in full list)

**Zaiwa (atb)** {llm-cs45} (suspected)
- **Family**: Sino-Tibetan, Burmese branch
- **Assessment**: Likely tenseless or simple tense, time granularity likely ABSENT
- **In our database**: Yes (atb-atb.txt)

### 6. Trans-New Guinea Languages

**Status**: VARIABLE, requires language-specific research

**Present in our database**: Extensive representation (aak, aby, aey, agd, agm, etc.)
- **Research needed**: Most PNG languages under-documented for tense-aspect
- **General pattern**: Wide typological diversity
- **Assessment**: VARIABLE - some may have remoteness, most likely simple or absent

### 7. Mayan Languages

**Status**: VARIABLE

**Tenseless patterns** {tenseless-languages-compass}:
- Some Mayan languages described as tenseless
- Time reference through aspect and adverbs

**In our database**: Yes (acr-Achi, agu-Awakateko, amu-Amuzgo Guerrero)
- **Assessment**: Likely OPTIONAL or ABSENT for most

### 8. Afro-Asiatic Languages

**Status**: MOSTLY ABSENT

**Arabic (arb - Standard)** {llm-cs45} (suspected)
- **System**: Perfect/Imperfect primarily aspectual
- **Time reference**: Context + temporal adverbs
- **Assessment**: Time granularity likely ABSENT

**Hebrew**: See "Source Languages" - ABSENT

**Assyrian Neo-Aramaic (aii)** {llm-cs45} (suspected)
- **Assessment**: Likely similar to other Semitic - ABSENT

### 9. Turkic, Mongolic, Finno-Ugric

**Status**: SOME have 2-3 way remoteness

**Uyghur (Turkic)** {hesternal-wikipedia}
- **System**: 2-3 way remoteness distinction
- **Assessment**: OPTIONAL or MANDATORY

**Buriat (Mongolic)** {hesternal-wikipedia}
- **System**: 2-3 way remoteness distinction
- **Assessment**: OPTIONAL or MANDATORY

**Udmurt (Finno-Ugric)** {hesternal-wikipedia}
- **System**: 2-3 way remoteness distinction
- **Assessment**: OPTIONAL or MANDATORY

**Azerbaijani South (azb)** {llm-cs45} (suspected)
- **Family**: Turkic
- **Assessment**: May have remoteness like Uyghur - requires verification
- **In our database**: Yes (azb-azb.txt)

### 10. Australian Languages

**Status**: VARIABLE, often complex systems

**Examples in our database**: aer-Eastern Arrernte, aly-Alyawarr, amx-Anmatyerre, aoi-Anindilyakwa, are-Western Arrarnta, awk-Awabakal

**General pattern**: Australian languages often have complex tense-aspect-mood systems
**Assessment**: VARIABLE - some likely have remoteness, requires language-specific research

### 11. Creole Languages

**Status**: MOSTLY ABSENT (tenseless patterns common)

**Lesser Antillean French Creole (acf)** {tenseless-languages-compass}
- **Pattern**: Most creoles are tenseless or have simple tense
- **Assessment**: Time granularity likely ABSENT
- **In our database**: Yes (acf-acfNT.txt)

### 12. Other Families

**Sepik (PNG)**: Multiple languages in database (aau, abt, amp, etc.) - likely VARIABLE
**Torricelli (PNG)**: Multiple languages (aoj, aon, ape, avt) - likely VARIABLE
**Algic (North America)**: alq-Algonquin, arp-Arapaho - requires research
**Eyak-Athabaskan**: apw-Apache Western, bea-Beaver - requires research

## Root Bible Translation Languages

### Languages WITH Time Granularity (Critical for Translation)

None of the major source languages for Bible translation have grammatical time granularity:

| Language | Family | Time Granularity | Status |
|----------|--------|------------------|--------|
| Hebrew | Afro-Asiatic | ABSENT | Source language |
| Greek | Indo-European | ABSENT | Source language |
| Latin | Indo-European | ABSENT | Historic translation |
| English | Indo-European | ABSENT | Major gateway |
| Spanish | Indo-European | ABSENT | Major gateway |
| German | Indo-European | ABSENT | Major gateway |
| French | Indo-European | ABSENT | Major gateway |
| Arabic | Afro-Asiatic | ABSENT (suspected) | Regional gateway |
| Indonesian | Austronesian | ABSENT (suspected) | Regional gateway |
| Mandarin | Sino-Tibetan | ABSENT | Regional gateway |

### Languages WITHOUT Time Granularity but Used as Translation Base

**Swahili** (Bantu, East Africa)
- **Expected**: Should have time granularity (Bantu pattern)
- **Assessment**: Likely has 2-3 remoteness distinctions (MANDATORY)
- **Status**: Regional gateway for East Africa
- **In our database**: Not found in sample, but likely in full database

**Implication**: Translators working FROM languages without time granularity INTO languages requiring it must infer temporal distance from context - exactly what TBTA aims to help with.

## Target Languages Requiring Time Granularity

### Selection Criteria for Test Database (Stage 2)

Based on typological diversity, we should include:

1. **Bantu (Mandatory)**: Representing 80% of Bantu with 2-4 past distinctions
2. **Amazonian (Mandatory)**: Representing richest known systems (4-5 distinctions)
3. **Austronesian (Optional/Variable)**: Representing mixed aspect/tense systems
4. **Turkic/Mongolic (Optional)**: Representing Eurasian remoteness systems
5. **Control (Absent)**: Languages without time granularity for comparison

### Recommended Languages for Translation Database

| # | Language | Code | Family | Distinctions | In Database | Rationale |
|---|----------|------|--------|--------------|-------------|-----------|
| 1 | **Yagua** | yad | Peba-Yaguan | 5 past | ✅ Yes | Richest system, critical test case |
| 2 | **ChiBemba** | bem | Bantu | 4 past, 4 future | ❓ Check | Symmetric system, well-documented |
| 3 | **Haya** | hay | Bantu | 3 past (rigid) | ❓ Check | Clear boundaries, good for validation |
| 4 | **Swahili** | swh | Bantu | 2-3 past (suspected) | ❓ Check | Major translation language |
| 5 | **Tagalog** | tgl | Austronesian | Variable/Optional | ✅ Yes | Aspect-based, tests edge of feature |
| 6 | **Uyghur** | uig | Turkic | 2-3 past | ❓ Check | Eurasian example |
| 7 | **English** | eng | Indo-European | ABSENT | ✅ Yes | Control - no time granularity |
| 8 | **Mandarin** | cmn | Sino-Tibetan | ABSENT | ❓ Check | Control - tenseless |
| 9 | **Spanish** | spa | Indo-European | ABSENT | ✅ Yes | Control - major translation language |
| 10 | **One Australian** | TBD | Australian | Variable | Multiple | Typological diversity |

**Note**: Final selection depends on which languages have sufficient Bible translation coverage for test set generation (Stage 4).

## Cultural Nuances & Social Distinctions

### Honorifics

**Not directly related** to time granularity. Honorifics (Japanese, Korean, Javanese) affect verb forms and pronouns based on social relationships, not temporal distance.

**Potential interaction**: Some languages may have different remoteness systems in formal vs informal registers, but this is not documented in reviewed sources.

### Taboos

**Legendary/Mythological Past**: In some languages, distant/legendary past has special status:

- Used for creation myths, ancestral stories
- May carry implications of "sacred time" vs "ordinary time"
- Examples: Yimas (PNG) sometimes uses irrealis mood for legendary/highly remote past {hesternal-wikipedia}

**Implication for Bible translation**: Genesis creation narratives, patriarchal stories may require special "legendary/mythological past" forms in languages with this distinction.

### Evidentiality Interaction

**Some languages** combine temporal remoteness with evidentiality (how speaker knows the information):
- Direct witness vs. hearsay
- Personal experience vs. cultural transmission

**Example**: Biblical narratives are transmitted knowledge (not direct witness), which may affect time marking in languages with evidential systems.

**Note**: This interaction is beyond the scope of pure time granularity but relevant for comprehensive TBTA annotation.

## Analysis by Necessity

### Mandatory (Grammatically Required)

**Families where 50%+ of languages require it**:
- **Bantu** (Niger-Congo): 80% of languages
- **Some Amazonian families**: Peba-Yaguan, Pano, some Tupi-Guarani

**Estimated languages**: ~1000+ languages worldwide (based on 20% of ~7000 languages)

### Optional (Can be expressed but not required)

**Families with variable expression**:
- **Some Austronesian**: Tagalog-type aspect systems
- **Some Turkic, Mongolic, Finno-Ugric**: 2-3 way systems
- **Some Australian languages**: Complex but variable

**Estimated languages**: ~500-1000 languages

### Absent (Not expressed grammatically)

**Families where it's systematically absent**:
- **Most Indo-European** (except rare cases like Balochi)
- **Most Sino-Tibetan** (tenseless systems)
- **Most Afro-Asiatic** (including Hebrew, Arabic)
- **Many Austronesian** (Hawaiian and others)
- **Most Creoles**
- **Many Native American families** (Algic, Iroquoian, etc.)

**Estimated languages**: ~5000+ languages worldwide

## Key Findings for Algorithm Development

### 1. Source Language Challenge

**Critical**: Neither Hebrew nor Greek encode time granularity, meaning:
- ALL TBTA values are inferential
- Algorithm must learn from context, not morphology
- Cannot simply "decode" source language forms

### 2. Typological Diversity

**Wide variation** in number of distinctions:
- Tenseless: 0 distinctions (40% of languages)
- Simple: 2-3 distinctions (most common for languages with feature)
- Rich: 4-5 distinctions (rare, <3% of languages)

**Implication**: Algorithm must be flexible enough to output appropriate granularity for each target language.

### 3. Common Patterns

**Universal tendency**: Primary division at "today" boundary (hodiernal vs pre-hodiernal) {hesternal-wikipedia}

**Common pattern**: More past than future distinctions {languages-of-world-past}

**Rigid vs Flexible**: Some languages have rigid boundaries (Haya), others more flexible

### 4. Contextual Clues for Algorithm

**Indicators of temporal distance** (for Hebrew/Greek texts):
- Narrative framing (Genesis = ancient, Gospels = ~2000 years ago, Epistles = contemporary to recipients)
- Temporal adverbs ("in those days", "today", "yesterday")
- Historical knowledge (creation, exodus, exile, Jesus' ministry)
- Discourse genre (teaching = timeless, narrative = time-bound)
- Character speech in direct discourse (their temporal perspective, not narrator's)

### 5. Translation Database Implications

**Must include** languages with:
- 0 distinctions (control)
- 2-3 distinctions (most common)
- 4-5 distinctions (edge cases)
- Rigid boundaries (test precision)
- Flexible boundaries (test semantic understanding)

## Summary Table: Language Classification

| Family | Example Languages | Status | Distinctions | Notes |
|--------|------------------|--------|--------------|-------|
| Bantu | ChiBemba, Haya, Swahili | MANDATORY (80%) | 2-4 past, 0-4 future | Most articulated systems |
| Amazonian | Yagua, Chakobo, Pano langs | MANDATORY (some) | 4-5 past | Richest known systems |
| Austronesian | Tagalog, Hawaiian | VARIABLE | 0-2 past | Aspect-based, mixed |
| Indo-European | English, Spanish, Greek | ABSENT (mostly) | 0 | Balochi exception |
| Sino-Tibetan | Mandarin, Burmese | ABSENT | 0 | Tenseless systems |
| Afro-Asiatic | Hebrew, Arabic | ABSENT | 0 | Aspect-based |
| Turkic | Uyghur, Azerbaijani | OPTIONAL (some) | 2-3 past | Regional variation |
| Australian | Various | VARIABLE | Unknown | Under-documented |
| Creole | Various | ABSENT (mostly) | 0 | Simplified systems |

---

**Analysis Complete**: 2025-11-29
**Confidence**: High for major families, Medium for under-documented languages
**Next Step**: Finalize translation database language selection based on Bible coverage data
>>>>>>> origin/feat/self-learning-tbta
