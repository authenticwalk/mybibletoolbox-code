# Language Family & Typology Analysis: Time Granularity

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
