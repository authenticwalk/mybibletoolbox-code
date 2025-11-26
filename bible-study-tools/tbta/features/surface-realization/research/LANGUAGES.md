# Language Typology Analysis: Surface Realization

**Feature**: Surface Realization (Pro-Drop, Word Order, Voice Systems)
**Stage**: 1 - Research & Definition
**Section**: 2 - Language Family & Typology Analysis

## Executive Summary

Surface realization—how semantic and syntactic content appears on the language surface—varies dramatically across the world's languages. Key dimensions include:

- **Pro-drop**: ~70% of world languages allow null subjects; Biblical Hebrew and Koine Greek both exhibit pro-drop
- **Word order flexibility**: Ranges from fixed (English) to highly flexible (Latin, Russian, Australian languages)
- **Voice systems**: Include simple active/passive (English), symmetrical voice (Philippine-type), and inverse marking (Algonquian)
- **Our TSV coverage**: 1008 languages across 25+ families, with major concentrations in Austronesian (176), Trans-New Guinea (141), and Indo-European (135)

**Critical Finding**: The source languages (Hebrew/Greek) are both pro-drop with flexible word order, but most target languages require different surface realization strategies.

---

## 1. Source Language Encoding: Hebrew & Greek

### 1.1 Biblical Hebrew

**Pro-Drop Status**: YES - Moderately pro-drop language

**Morphological Foundation**:
- Rich verbal inflection with portmanteau morphs carrying person, number, gender features
- Finite verbs inflected for subject agreement
- Subject pronouns NOT obligatory; overt pronouns signal Topic or Focus emphasis

**Word Order**:
- Basic order: **VSO** (Verb-Subject-Object)
- No noun case system
- Word order flexibility used for discourse purposes
- Pro-drop interacts with VSO to create varied surface patterns

**Key Citations**:
- {ancienthebrewgrammar-2010}: "Biblical Hebrew exhibits 'pronoun dropping,' describing a feature where overt arguments are not required"
- {holmstedt-2010}: "Though full-scale study is lacking, it has long been observed that the subject pronoun is not obligatory"
- {naude-qumran}: Focused study on null subjects in Qumran Hebrew

**Implications for Translation**:
- Hebrew frequently uses null subjects in narrative
- Explicit pronouns mark emphasis or topic shift
- Target languages must decide: preserve zeros (if pro-drop) or pronominalize (if non-pro-drop)

### 1.2 Koine Greek

**Pro-Drop Status**: YES - Full pro-drop language

**Morphological Foundation**:
- Rich verb morphology inflects for person and number
- Subject pronouns "usually omitted when they can be inferred from context"
- Greek exhibits "several characteristics of pro-drop languages which are allowed by its rich morphology"

**Word Order**:
- Neutral order for Koine: **VSO** (shift from Classical Greek SOV)
- "Non-configurational language" - word order driven by information structure
- Highly flexible order for discourse purposes
- Old information precedes new; assumed information precedes asserted

**Key Citations**:
- {greek-pro-drop-researchgate}: "Greek is a pro-drop language where subject pronouns are usually omitted"
- {greek-word-order-academia}: "SOV is the neutral/basic and most frequent order for Classical Greek, but significant change can be located in Koine Greek"
- {koine-greek-2023}: "Greek word order, as a non-configurational language, is driven by information structure"

**Implications for Translation**:
- Greek narrative extensively uses null subjects
- Word order changes signal information structure, not grammatical role
- Target languages must encode information structure through their own mechanisms

### 1.3 Critical Insight

**Both source languages are pro-drop with flexible word order**, meaning:
1. The "base text" extensively uses null subjects
2. Word order carries pragmatic meaning, not just syntax
3. Target languages must adapt to their own constraints
4. Non-pro-drop languages (English, German, Bantu) must ADD explicit subjects
5. Pro-drop languages (Spanish, Japanese, Quechua) can mirror source patterns more naturally

---

## 2. Language Family Analysis from TSV

Our translation database (`/src/constants/languages.tsv`) contains **1008 languages** across **25+ families**. Here's the typological breakdown:

### 2.1 Family Distribution (Top 20)

| Family | Count | Pro-Drop Pattern | Voice System | Word Order |
|--------|-------|------------------|--------------|------------|
| **Austronesian** | 176 | Variable (focus-driven) | Symmetrical voice (Philippine-type) | VSO/VOS common |
| **Trans-New Guinea** | 141 | Variable (clause-chaining) | Active/passive, some ergative | SOV dominant |
| **Indo-European** | 135 | Mixed (Romance=yes, Germanic=no) | Active/passive, clitics | SVO/SOV/VSO |
| **Niger-Congo** | 89 | Mostly no (noun class tracking) | Active/passive | SVO dominant |
| **Otomanguean** | 69 | Variable (suspected) | Active/passive | VSO (suspected) |
| **Mayan** | 41 | Limited | Ergative-absolutive | VSO/VOS |
| **Australian** | 36 | Variable (free word order) | Ergative, some split-S | Free, often SOV |
| **Afro-Asiatic** | 25 | Yes (Semitic), Variable (Cushitic) | Active/passive | VSO (Semitic), SOV (Cushitic) |
| **Uto-Aztecan** | 21 | Variable (suspected) | Active/passive | SOV (suspected) |
| **Maipurean** | 20 | Variable (suspected) | Active/passive | Variable |
| **Sino-Tibetan** | 18 | High (Chinese), Variable (Tibetan) | Active/passive, some topic-comment | SVO/SOV |
| **Quechuan** | 18 | High | Active/passive, agglutinative | SOV |
| **Creole** | 15 | Variable by substrate | Active/passive | SVO common |
| **Tucanoan** | 14 | Variable (suspected) | Active/passive | SOV (suspected) |
| **Sepik** | 14 | Variable (suspected) | Variable | SOV (suspected) |
| **Tupian** | 12 | Variable (suspected) | Active/passive | Variable |
| **Torricelli** | 12 | Variable (suspected) | Variable | SOV (suspected) |
| **Language isolate** | 10 | Case-by-case | Case-by-case | Case-by-case |
| **Panoan** | 8 | Variable (suspected) | Ergative (suspected) | Variable |
| **Nilo-Saharan** | 8 | Variable (suspected) | Variable | Variable |

*Note: "(suspected)" indicates classifications based on linguistic knowledge where specific documentation was not verified in research phase.*

### 2.2 Key Observations

**Pro-Drop Distribution**:
- **~70% of our languages** likely allow some form of pro-drop (estimated ~700 languages)
- **High pro-drop**: East Asian (Sino-Tibetan), Quechuan, Romance (Indo-European), most Austronesian
- **No pro-drop**: Germanic (Indo-European), most Bantu (Niger-Congo), some Mayan
- **Variable/Complex**: Trans-New Guinea, Philippine Austronesian (focus-driven), Australian

**Regional Concentrations**:
- **Papua New Guinea**: 318 languages (mostly Trans-New Guinea + Austronesian) - highly diverse systems
- **Philippines**: 115 languages (Austronesian) - symmetrical voice systems
- **Africa**: 120+ languages - mostly non-pro-drop with noun class systems
- **Americas**: 180+ languages - highly variable typology

---

## 3. Voice System Classification

Voice systems determine how languages encode agent/patient relationships and affect surface realization of arguments.

### 3.1 Active/Passive Systems (Most Common)

**Definition**: Two-way distinction where active marks agent-as-subject, passive demotes agent.

**Distribution**: Found in most Indo-European, Afro-Asiatic, Sino-Tibetan, and many other families.

**Examples from Our TSV**:
- **English** (eng): Prototypical active/passive
  - Active: "John loves Mary" (agent=subject)
  - Passive: "Mary is loved (by John)" (patient=subject, agent demoted/optional)
- **Spanish** (spa): Active/passive + pro-drop + clitics
  - Active: "(Él) ama a María" = "(He) loves Mary"
  - Passive: "María es amada (por él)" = "Mary is loved (by him)"
- **Arabic** (arb): Active/passive with pro-drop
  - Rich agreement enables extensive pro-drop
- **Mandarin Chinese** (zho): Active (no passive morphology; uses disposal constructions)
  - Topic-prominent; extensive zero anaphora

**Pro-Drop Correlation**: Active/passive systems can be pro-drop (Spanish, Greek) or non-pro-drop (English, German) - voice system doesn't determine pro-drop status.

### 3.2 Symmetrical Voice (Philippine-Type) Systems

**Definition**: Multiple voices of equal grammatical status; one argument marked as "trigger" or "topic"; voice morphology indicates semantic role of trigger.

**Distribution**: Philippine languages, Formosan (Taiwan), northern Borneo, northern Sulawesi, Madagascar.

**Key Characteristics**:
- 3-6 distinct voices (Actor Voice, Patient Voice, Locative Voice, Benefactive Voice, Instrument Voice, Reason Voice)
- Trigger marked with special case particle (Tagalog: *ang*)
- Voice affix on verb indicates semantic role of trigger
- Pro-drop interacts with focus/trigger structure

**Examples from Our TSV**:
- **Tagalog** (tgl): 6 voices
  - Actor Voice: *Bumili ang lalaki ng isda* = "The man bought fish" (man=trigger)
  - Patient Voice: *Binili ng lalaki ang isda* = "The fish was bought by the man" (fish=trigger)
  - Pro-drop: Trigger can be null if highly salient in discourse
- **Cebuano** (ceb): Similar system
- **Ilocano** (ilo): Similar system
- **Pampangan** (pam): Similar system

**Our TSV Count**: Estimated **50-80 languages** with symmetrical voice systems (primarily Philippine Austronesian).

**Translation Implications**:
- Voice choice affects which participant surfaces as trigger
- Pro-drop applies to trigger, but rules differ from active/passive languages
- Information structure drives voice selection
- Cannot mechanically translate from Greek/Hebrew voice

**Citations**:
- {wikipedia-symmetrical-voice}: "Symmetrical voice, also known as Austronesian alignment or the Austronesian focus system, is a typologically unusual kind of morphosyntactic alignment"
- {language-closet-2025}: Philippine-type has "four voices (or sometimes three)"

### 3.3 Inverse Voice Systems

**Definition**: Voice marking determined by person/animacy hierarchy; "direct" when subject outranks object, "inverse" when object outranks subject.

**Person Hierarchy** (typical): 2nd > 1st > 3rd proximate > 3rd obviative

**Distribution**: Algonquian, some Athabaskan, rGyalrong (Sino-Tibetan), Kopar (Sepik), some Mixe-Zoquean.

**Key Characteristics**:
- Obligatory marking on transitive verbs
- Subject/object roles determined by hierarchy + voice marking
- No case distinctions on nouns (in Algonquian)
- Pro-drop may interact with hierarchy

**Examples from Research**:
- **Ojibwe** (Algonquian):
  - Direct: "I saw him" (1st > 3rd)
  - Inverse: "He saw me" (1st still outranks 3rd, but 3rd is agent → inverse marking)
- **Cree** (Algonquian): Similar system
- **Navajo** (Athabaskan): Inverse-like system (suspected)
- **Mapudungun** (arn in our TSV): Documented inverse system

**Our TSV Count**: Limited - perhaps **5-10 languages** with clear inverse systems.

**Languages in Our TSV**:
- **arn** (Mapudungun): Chile, Mapudungu family - CONFIRMED inverse system
- **apw** (Western Apache): Eyak-Athabaskan - inverse-like (suspected)
- **bea** (Beaver): Eyak-Athabaskan - inverse-like (suspected)
- **alq** (Algonquin): Algic family - inverse system (suspected, needs verification)

**Translation Implications**:
- Voice marking automatic based on person hierarchy
- Cannot always mirror Greek/Hebrew voice choices
- Pro-drop may be constrained by hierarchy salience
- Translators must learn language-specific hierarchy

**Citations**:
- {wikipedia-direct-inverse}: "Direct–inverse alignment involves different grammar for transitive predications according to the relative positions of their 'subject' and 'object' on a person hierarchy"
- {delancey-2024}: Inverse systems relate to topic structure

### 3.4 Other Voice/Alignment Systems

**Ergative-Absolutive**:
- **Distribution**: Many Mayan, some Australian, some Caucasian
- **Our TSV**: Mayan (41 languages), some Australian (36 languages)
- **Example**: Kaqchikel (cak), Achi (acr)
- **Surface realization**: Absolutive argument has same marking as intransitive subject

**Split Ergativity**:
- Some languages use ergative in some contexts, active/passive in others
- (suspected) in some Australian languages in our TSV

**Active-Stative (Split-S)**:
- Some intransitive subjects marked like transitive agents, others like transitive patients
- Distribution: Some Native American languages (suspected)

---

## 4. Word Order Flexibility Analysis

### 4.1 Fixed Word Order Languages

**Definition**: Strong constraints on constituent order; changing order is ungrammatical or highly marked.

**Distribution**: ~40% of world's languages (estimated)

**Examples from Our TSV**:

| Language | Code | Family | Order | Pro-Drop | Notes |
|----------|------|--------|-------|----------|-------|
| English | eng | Indo-European | SVO | No | Rigid order; pronouns required |
| Mandarin Chinese | zho | Sino-Tibetan | SVO | Yes | Fixed order but extensive pro-drop |
| French | fra | Indo-European | SVO | Limited | Clitic placement constrained |
| Thai | tha | Tai-Kadai | SVO | Yes (suspected) | Fixed order (suspected) |
| Vietnamese | vie | Austroasiatic | SVO | Yes | Fixed order, topic-prominent |

**Key Pattern**: Fixed order does NOT predict pro-drop status. Chinese is fixed SVO but high pro-drop; English is fixed SVO but no pro-drop.

### 4.2 Flexible Word Order Languages

**Definition**: Multiple word orders grammatical; order conveys pragmatic meaning (topic/focus/emphasis).

**Distribution**: ~60% of world's languages (estimated)

**Examples from Our TSV**:

| Language | Code | Family | Dominant Order | Pro-Drop | Flexibility |
|----------|------|--------|----------------|----------|-------------|
| **Spanish** | spa | Indo-European | SVO | Yes | Moderate; can front topics/objects |
| **Portuguese** | por | Indo-European | SVO | Yes | Moderate; similar to Spanish |
| **Russian** | rus | Indo-European | SVO (neutral) | Limited | High; case marks roles |
| **Japanese** | jpn | Japonic | SOV | Yes | Moderate; topic-comment structure |
| **Turkish** | tur | Turkic | SOV | Yes | High; SOV is default but all orders possible |
| **Latin** | lat | Indo-European | SOV (default) | Yes | Very high; case system allows freedom |
| **Quechua** | que | Quechuan | SOV | Yes | Moderate (suspected) |
| **Australian languages** | various | Australian | SOV (often) | Variable | Very high; free word order common |

**Key Pattern**: Flexible order often correlates with:
- Rich case marking (Russian, Latin, Turkish)
- Pro-drop (most Romance, Slavic, Quechuan)
- Discourse-driven order (Japanese, Turkish)

**Citations**:
- {wals-word-order}: "Many languages have case marking systems that let speakers shuffle words around more freely without messing up the meaning"
- {dryer-1997}: Six-way word order typology with flexibility parameters

### 4.3 Clause-Chaining and Medial Clauses

**Special Category**: Trans-New Guinea and some other families use clause-chaining where medial clauses have different word order and pro-drop constraints than final clauses.

**Distribution**: Widespread in **Trans-New Guinea family (141 languages in our TSV)**.

**Characteristics**:
- Medial clauses: Special verb forms, often pro-drop
- Final clauses: Full inflection, may require subjects
- Switch-reference: Indicates whether subject is same or different across clauses

**Examples from Our TSV** (suspected):
- **Agarabi** (agd): Subject drop in medial clauses
- **Amele** (aey): Complex clause-chaining pro-drop
- **Awa** (awb): Clause-chaining (suspected)

**Translation Implications**:
- Cannot apply uniform pro-drop rules
- Medial vs. final clause distinction critical
- Switch-reference affects pro-drop decisions

---

## 5. Root Languages: Translation Bridge Analysis

"Root languages" are major Bible translation sources that translators commonly reference. Understanding their surface realization properties is critical.

### 5.1 Primary Source Languages

| Language | Code | Pro-Drop | Word Order | Voice System | Clitic System | Translation Status |
|----------|------|----------|------------|--------------|---------------|-------------------|
| **Biblical Hebrew** | hbo | Yes (moderate) | VSO flexible | Active/passive | No | SOURCE - Old Testament |
| **Koine Greek** | grc | Yes (full) | VSO flexible | Active/passive | No | SOURCE - New Testament |

### 5.2 Major Bridge Languages

**European Root Languages**:

| Language | Code | Pro-Drop | Word Order | Voice System | Clitic System | Role |
|----------|------|----------|------------|--------------|---------------|------|
| **Latin** | lat | Yes | SOV flexible | Active/passive | No | Historical bridge (Vulgate) |
| **English** | eng | No | SVO fixed | Active/passive | No | Dominant modern bridge |
| **Spanish** | spa | Yes | SVO moderate flex | Active/passive | Yes (obligatory) | Latin America bridge |
| **Portuguese** | por | Yes | SVO moderate flex | Active/passive | Yes (obligatory) | Brazil/Africa bridge |
| **French** | fra | Limited | SVO fixed | Active/passive | Yes (obligatory) | Africa bridge |
| **German** | deu | No | SOV/V2 moderate flex | Active/passive | No | Europe bridge |

**Asian/African/Global Root Languages**:

| Language | Code | Pro-Drop | Word Order | Voice System | Clitic System | Role |
|----------|------|----------|------------|--------------|---------------|------|
| **Arabic** | arb | Yes | VSO flexible | Active/passive | No | Middle East/North Africa bridge |
| **Mandarin Chinese** | zho | Yes (full) | SVO fixed | Active (no passive) | No | East Asia bridge (suspected) |
| **Indonesian** | ind | Yes | SVO (suspected) | Active/passive | No | Southeast Asia bridge |
| **Swahili** | swh | No | SVO | Active/passive | No | East Africa bridge |

### 5.3 Critical Insights

**Pro-Drop Divide**:
- **Pro-drop bridges**: Greek, Hebrew, Latin, Spanish, Portuguese, Arabic, Chinese, Indonesian
- **Non-pro-drop bridges**: English, German, Swahili, French (limited)

**Implication**: Translators from pro-drop sources (Greek/Hebrew) into non-pro-drop targets (English, German, Swahili) must ADD pronouns. Those into pro-drop targets (Spanish, Arabic, Chinese) can PRESERVE null subjects more naturally.

**Word Order Divide**:
- **Fixed**: English, French, Chinese
- **Flexible**: Hebrew, Greek, Latin, Spanish, Russian, Arabic, German (V2)

**Voice System**: Nearly all root languages use active/passive (no Philippine-type or inverse systems), making those target languages more challenging.

---

## 6. Candidate Language Selection (5-10 Languages)

Based on typological diversity, documentation quality, speaker population, and representation in our TSV, here are **10 candidate languages** for Stage 2 Translation Database creation:

### Tier 1: Core Candidates (Well-Documented, High Priority)

#### 1. **Spanish (spa)** - Romance Pro-Drop with Clitics
- **Family**: Indo-European (Romance)
- **Pro-Drop**: Yes (all persons)
- **Word Order**: SVO, moderate flexibility
- **Voice**: Active/passive
- **Clitics**: Obligatory for objects
- **Speakers**: 500+ million
- **Why Selected**: Dominant Latin American bridge language; well-documented; distinct from English; obligatory clitic system tests object realization

#### 2. **English (eng)** - Non-Pro-Drop Baseline
- **Family**: Indo-European (Germanic)
- **Pro-Drop**: No
- **Word Order**: SVO, fixed
- **Voice**: Active/passive
- **Clitics**: No
- **Speakers**: 1.5+ billion
- **Why Selected**: Source translation baseline; contrastive case (no pro-drop); most common bridge language

#### 3. **Mandarin Chinese (zho)** - Topic-Prominent Pro-Drop
- **Family**: Sino-Tibetan
- **Pro-Drop**: Yes (extensive)
- **Word Order**: SVO, fixed
- **Voice**: Active (no passive morphology; disposal constructions)
- **Clitics**: No
- **Speakers**: 1+ billion
- **Why Selected**: Topic-prominent structure; extensive zero anaphora; fixed word order + full pro-drop combination; East Asian representative

#### 4. **Japanese (jpn)** - Topic-Comment with Pro-Drop
- **Family**: Japonic (isolate)
- **Pro-Drop**: Yes (extensive)
- **Word Order**: SOV, topic-comment structure
- **Voice**: Active/passive
- **Clitics**: No (particles instead)
- **Speakers**: 125+ million
- **Why Selected**: Topic-comment structure; extreme pro-drop including objects; SOV order contrasts with Hebrew/Greek; well-documented

#### 5. **Tagalog (tgl)** - Symmetrical Voice System
- **Family**: Austronesian
- **Pro-Drop**: Variable (focus-driven)
- **Word Order**: VSO/VOS (flexible)
- **Voice**: Symmetrical (6 voices: actor, patient, locative, benefactive, instrument, reason)
- **Clitics**: No
- **Speakers**: 25+ million (L1), 60+ million (L2)
- **Why Selected**: ONLY Philippine-type symmetrical voice in candidates; critical test case for voice systems; Austronesian representative (176 languages in TSV)

### Tier 2: High-Value Candidates (Diverse Typology)

#### 6. **Quechua (que)** - Agglutinative Pro-Drop
- **Family**: Quechuan
- **Pro-Drop**: Yes (extensive)
- **Word Order**: SOV
- **Voice**: Active/passive
- **Clitics**: No
- **Speakers**: 8-10 million
- **Why Selected**: Agglutinative morphology; rich agreement enables pro-drop; SOV order; South American indigenous representative; 18 varieties in TSV

#### 7. **Russian (rus)** - Limited Pro-Drop with Case
- **Family**: Indo-European (Slavic)
- **Pro-Drop**: Limited (primarily 3rd person)
- **Word Order**: SVO (neutral), highly flexible
- **Voice**: Active/passive
- **Clitics**: Yes (limited)
- **Speakers**: 250+ million
- **Why Selected**: Partial pro-drop system (asymmetry between persons); rich case system enables word order flexibility; Slavic representative

#### 8. **Arabic (arb)** - VSO Pro-Drop
- **Family**: Afro-Asiatic (Semitic)
- **Pro-Drop**: Yes (moderate to high)
- **Word Order**: VSO, flexible
- **Voice**: Active/passive
- **Clitics**: No
- **Speakers**: 300+ million
- **Why Selected**: Related to Hebrew (Semitic family); VSO like source languages; major bridge language for Middle East/North Africa; pro-drop with agreement

#### 9. **Swahili (swh)** - Non-Pro-Drop with Noun Classes
- **Family**: Niger-Congo (Bantu)
- **Pro-Drop**: No
- **Word Order**: SVO
- **Voice**: Active/passive
- **Clitics**: No
- **Speakers**: 100-150 million
- **Why Selected**: Non-pro-drop like English but with noun class system for tracking; major African bridge language; Bantu representative (30+ Bantu in TSV)

#### 10. **Mapudungun (arn)** - Inverse Voice System
- **Family**: Mapudungu (isolate)
- **Pro-Drop**: Variable (suspected)
- **Word Order**: Variable (suspected)
- **Voice**: Inverse (direct/inverse marking)
- **Clitics**: Unknown (needs research)
- **Speakers**: 200,000
- **Why Selected**: ONLY inverse system in candidates; critical test case for person hierarchy-driven voice; underrepresented typology

### Alternative Candidates (If Resources Allow)

- **Portuguese (por)**: Similar to Spanish but distinct phonology and some clitic differences
- **French (fra)**: Limited pro-drop; interesting contrast with Spanish
- **Indonesian (ind)**: Austronesian but Indonesian-type (reduced voice system)
- **Turkish (tur)**: Turkic; agglutinative; pro-drop with free word order
- **Agarabi (agd)**: Trans-New Guinea representative; clause-chaining

### Selection Rationale Summary

**Typological Coverage**:
- Pro-drop: Spanish, Chinese, Japanese, Quechua, Russian (limited), Arabic
- Non-pro-drop: English, Swahili
- Variable: Tagalog, Mapudungun

**Voice Systems**:
- Active/passive: English, Spanish, Chinese, Japanese, Quechua, Russian, Arabic, Swahili
- Symmetrical: Tagalog
- Inverse: Mapudungun

**Word Order**:
- SVO: English, Spanish, Chinese, Swahili
- SOV: Japanese, Quechua
- VSO: Arabic
- Flexible: Russian, Tagalog, Mapudungun (suspected)

**Geographic Diversity**:
- Europe: Spanish, English, Russian
- East Asia: Chinese, Japanese
- Southeast Asia: Tagalog
- South America: Quechua, Mapudungun
- Middle East: Arabic
- Africa: Swahili

### Candidate Summary Table

| # | Language | Code | Family | Pronoun Status | Voice System | Priority | Rationale |
|---|----------|------|--------|----------------|--------------|----------|-----------|
| **1** | **Spanish** | spa | Indo-European | **Optional** (pro-drop) | Active/passive | **Mandatory** | Major bridge language; obligatory clitics |
| **2** | **English** | eng | Indo-European | **Mandatory** (non-pro-drop) | Active/passive | **Mandatory** | Baseline; most common bridge language |
| **3** | **Mandarin** | zho | Sino-Tibetan | **Optional** (pro-drop) | Active | **Mandatory** | Topic-prominent; fixed SVO + pro-drop |
| **4** | **Japanese** | jpn | Japonic | **Optional** (pro-drop) | Active/passive | **Mandatory** | Extreme pro-drop; topic-comment; SOV |
| **5** | **Tagalog** | tgl | Austronesian | **Variable** (focus-driven) | Symmetrical (6 voices) | **Mandatory** | Only symmetrical voice candidate |
| **6** | **Quechua** | que | Quechuan | **Optional** (pro-drop) | Active/passive | **Optional** | Agglutinative; South American indigenous |
| **7** | **Russian** | rus | Indo-European | **Partial** (limited pro-drop) | Active/passive | **Optional** | Asymmetric pro-drop; rich case system |
| **8** | **Arabic** | arb | Afro-Asiatic | **Optional** (pro-drop) | Active/passive | **Optional** | VSO; related to Hebrew; Middle East bridge |
| **9** | **Swahili** | swh | Niger-Congo | **Mandatory** (non-pro-drop) | Active/passive | **Optional** | Noun classes; African bridge; Bantu |
| **10** | **Mapudungun** | arn | Mapudungu | **Variable** (suspected) | Inverse | **Optional** | Only inverse system candidate |

**Priority Levels**:
- **Mandatory** (Tier 1): Essential for Stage 2; represent core typological distinctions
- **Optional** (Tier 2): High value but can be deferred if resources limited

---

## 7. Cultural Nuances and Social Distinctives

Surface realization choices often carry social and cultural meaning beyond grammar.

### 7.1 Honorifics and Politeness Systems

**Japanese**:
- Pro-drop interacts with honorific system
- Zero subjects more common in plain register
- Explicit subjects may signal formality or emphasis
- Bible translation must choose register carefully

**Korean** (kor - in TSV):
- Similar to Japanese; honorific verb endings affect pro-drop naturalness (suspected)
- Explicit subjects may signal politeness or social distance (suspected)

**Tagalog**:
- Politeness particles (*po*, *ho*) interact with voice/focus system (suspected)
- Bible translation register affects voice choice (suspected)

### 7.2 Gender and Case Marking

**Arabic**:
- Gendered verb agreement visible in pro-drop contexts
- Bible must handle gender correctly for theological accuracy (God's attributes, Spirit references)

**Spanish/Romance**:
- Gendered adjectives/participles must agree even when subjects are null
- Clitic pronouns carry gender information

**Russian**:
- Rich case system allows word order flexibility
- Case ending errors can mislead readers even with flexible order

### 7.3 Taboos and Avoidance

**Australian Languages** (suspected):
- Some languages have "mother-in-law" registers with different vocabulary
- Avoidance registers may affect pronoun use vs. noun use
- Bible translation must respect cultural sensitivities

**Philippine Languages**:
- Some contexts prefer indirect reference rather than direct pronouns
- Voice system choice may carry politeness implications (suspected)

### 7.4 Register and Scripture Translation

**Formal vs. Colloquial**:
- Many languages have formal Bible register expectations:
  - **Spanish**: Older translations use *vosotros* (Spain formal 2pl); modern use *ustedes*
  - **French**: Bible uses formal *vous* rather than colloquial *tu*
  - **Japanese**: Older Bibles use classical forms; modern Bibles use polite modern forms

**Pro-Drop and Register**:
- Formal registers often use MORE explicit forms (nouns/pronouns) than colloquial
- Bible translators must balance accuracy, clarity, and reverence

### 7.5 Translation Movement Trends

**"Natural Language" Movement**:
- Trend toward using pro-drop naturally in target languages
- Older translations: Over-explicit (influenced by English source texts)
- Modern translations: More natural zero use in pro-drop languages
- **Example**: Spanish Bibles increasingly drop subjects where natural

**"Literal" vs. "Dynamic Equivalence"**:
- Literal approaches may preserve Greek/Hebrew pro-drop patterns mechanically
- Dynamic approaches adapt to target language norms
- Surface realization is where these philosophies clash most visibly

---

## 8. Implementation Notes for Stage 2

### 8.1 Data Collection Strategy

For each candidate language, Stage 2 should collect:

1. **Grammar Reference**: Documented pro-drop rules, voice system, word order constraints
2. **Bible Translation Corpus**: 100+ verses per language (parallel with source)
3. **Native Speaker Input**: Naturalness judgments on zero vs. pronoun vs. noun choices
4. **Linguistic Database Checks**: WALS, Grambank feature verification

### 8.2 Feature Metadata Required

For each language:
```yaml
language_code: spa
language_name: Spanish
family: Indo-European
subfamily: Romance

pro_drop:
  status: full
  persons: [1sg, 2sg, 3sg, 1pl, 2pl, 3pl]
  constraints: "None; all persons allow null subjects"

word_order:
  dominant: SVO
  flexibility: moderate
  pragmatic_order: "Allows topic fronting, object fronting for emphasis"

voice_system:
  type: active_passive
  passive_morphology: "ser/estar + past participle"

clitics:
  object_clitics: obligatory
  placement: "Before conjugated verb, after infinitive/gerund/imperative"
  examples:
    - "Le doy el libro" (to-him I-give the book)
    - "Se lo doy" (to-him-it I-give)

agreement:
  subject_verb: rich
  adjective_noun: yes (gender, number)
  participle: yes (gender, number)
```

### 8.3 Translation Patterns to Test

Stage 2 should test these contexts:

1. **Narrative Continuity**: Same subject across multiple clauses
2. **Subject Shift**: New subject introduced
3. **Emphasis**: Contrastive or emphatic subject
4. **Ambiguity**: Potential for pronoun resolution errors
5. **Theological Emphasis**: Trinity, Christology contexts
6. **Complex Clauses**: Subordinate clauses, relative clauses
7. **Direct Speech**: Quotation attribution

---

## 9. Bibliography and Citations

### Linguistic Databases

- **WALS** (World Atlas of Language Structures): https://wals.info/
  - {wals-word-order}: Chapter 81 - Order of Subject, Object and Verb
  - {wals-antipassive}: Chapter 108 - Antipassive Constructions

- **Grambank**: https://grambank.clld.org/
  - 2,467 languages, 195 grammatical features
  - {grambank-2023}: Nature Human Behaviour article

### Hebrew Sources

- {ancienthebrewgrammar-2010}: "Pro-drop in Hebrew: a summary" - https://ancienthebrewgrammar.wordpress.com/2010/06/05/pro-drop-in-hebrew/
- {holmstedt-2010}: Robert Holmstedt, "Pro-Drop" - https://www.academia.edu/4686070/Pro_Drop
- {naude-qumran}: Study on null subjects in Qumran Hebrew
- {glossa-hebrew-2018}: "Usage patterns in the development of Hebrew grammatical subjects" - https://www.glossa-journal.org/article/id/5236/

### Greek Sources

- {greek-pro-drop-researchgate}: "On weak subjects and pro-drop in Greek" - https://www.researchgate.net/publication/228605297_On_weak_subjects_and_pro-drop_in_Greek
- {greek-word-order-academia}: "How Does a Basic Word Order Become Ungrammatical? SOV from Classical to Koine Greek" - https://www.academia.edu/83781574/
- {koine-greek-2023}: "A brief note on Greek word order" - https://koine-greek.com/2023/08/18/a-brief-note-on-greek-word-order/

### Voice Systems

- {wikipedia-symmetrical-voice}: "Symmetrical voice" - https://en.wikipedia.org/wiki/Symmetrical_voice
- {language-closet-2025}: "What on Earth is the 'Austronesian alignment'?" - https://thelanguagecloset.com/2025/05/31/what-on-earth-is-the-austronesian-alignment/
- {wikipedia-direct-inverse}: "Direct–inverse alignment" - https://en.wikipedia.org/wiki/Direct–inverse_alignment
- {delancey-2024}: "Inverse / Topic" - https://pages.uoregon.edu/delancey/sb/LECT7-8.htm

### Word Order

- {wals-word-order}: WALS Chapter 81 - https://wals.info/chapter/81
- {dryer-1997}: "On the Six-Way Word Order Typology" - https://www.acsu.buffalo.edu/~dryer/Dryer6Way1997.pdf
- {wikipedia-word-order}: "Word order" - https://en.wikipedia.org/wiki/Word_order

### Previous Project Work

- {learnings-surface-realization}: `/plan/tbta/tbta-rebuild-with-llm/features/surface-realization/LEARNINGS.md`
- {languages-in-tsv}: `/bible-study-tools/tbta/features/features-archive/surface-realization/LANGUAGES-IN-TSV.md`

---

## 10. Summary: Key Findings for Algorithm Development

### Critical Insights

1. **Source Languages Are Pro-Drop**: Hebrew and Greek both extensively use null subjects with flexible word order, meaning target languages must adapt, not mirror.

2. **70% of Target Languages Are Pro-Drop**: Most of our 1008 languages allow some pro-drop, but rules vary dramatically.

3. **Three Major Voice Systems**: Active/passive (most), symmetrical (Philippine-type, ~80 languages), inverse (~5-10 languages).

4. **Word Order Does Not Predict Pro-Drop**: Chinese is fixed SVO + pro-drop; English is fixed SVO + no pro-drop.

5. **Clitics Create Obligatory Surface Realization**: Romance languages (Spanish, Portuguese, French, Italian) have obligatory object clitics that change word order and surface patterns.

6. **Trans-New Guinea Family Is Highly Complex**: 141 languages with clause-chaining, medial clause rules, switch-reference systems - cannot generalize.

7. **Root Languages Are Divided**: English/German/French (non-pro-drop) vs. Spanish/Arabic/Chinese (pro-drop) - different translation strategies needed.

8. **Cultural Nuances Matter**: Honorifics (Japanese/Korean), register (Bible formality), taboos (Australian), politeness (Tagalog).

### Algorithm Implications

- **Cannot use universal pro-drop rule**: Must classify each language individually
- **Cannot predict from morphology alone**: Chinese has no agreement but full pro-drop; English has some agreement but no pro-drop
- **Must track discourse context**: Zero vs. pronoun vs. noun depends on information structure, not just grammar
- **Must handle voice systems differently**: Symmetrical voice (Tagalog) and inverse (Mapudungun) require distinct logic
- **Must account for clitics**: Romance languages need special object realization logic
- **Must validate with native speakers**: Grammar rules insufficient; naturalness judgments required

### Next Steps (Stage 2)

1. Create translation databases for 10 candidate languages
2. Sample 100+ verses per language with diverse contexts
3. Document actual translator choices (not just grammatical rules)
4. Identify patterns: when zeros, when pronouns, when nouns
5. Develop language-specific prediction models
6. Test cross-linguistic generalizations

---

**Document Status**: Stage 1 Research Complete
**Next Stage**: Stage 2 - Translation Database Construction
**Last Updated**: 2025-11-25
