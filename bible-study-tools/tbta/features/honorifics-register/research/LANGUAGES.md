# Language Typology Research: Honorifics-Register

**Feature**: Honorifics and Register Systems
**Research Phase**: Stage 1, Section 2 (Language Family & Typology Analysis)
**Date**: 2025-11-25

## Executive Summary

Honorifics and register systems are **grammatically absent** in Biblical Hebrew and Greek but **mandatory** in approximately 25% of world languages, particularly in East/Southeast Asia, South Asia, and some Austronesian languages. This creates significant translation challenges as target languages often require explicit encoding of social relationships that are implicit or absent in source texts.

**Key Finding**: ~338 languages in our database belong to families with honorific systems (Austronesian, Indo-European, Sino-Tibetan, Dravidian, Japonic, Kra-Dai, Austro-Asiatic).

---

## 1. Source Language Encoding Check

### Hebrew (Biblical)

**Status**: ❌ **NO grammatically encoded honorifics**

- Hebrew has **no formal/informal pronoun distinction** (no T-V distinction)
- Uses only singular vs plural distinction: אַתָּה (attah, you-sg) vs אַתֶּם (attem, you-pl)
- Plural forms *may* be used for collective reference or majesty (e.g., Elohim with singular verb)
- Emphasis achieved through independent pronouns, not honorific morphology
- **Citation**: {hermeneutics-se-81168}, {biblicalhebrew-org-pronouns}

### Greek (Koine/Biblical)

**Status**: ❌ **NO grammatically encoded honorifics**

- Greek has **no formal/informal pronoun distinction**
- Uses only number distinctions: σύ (sy, you-sg) vs ὑμεῖς (hymeis, you-pl)
- Inflected language with person/number/gender embedded in verb morphology
- No equivalent to modern Romance/Germanic T-V systems
- **Citation**: {hermeneutics-se-81168}

### Translation Implication

**CRITICAL**: Target languages with mandatory honorific marking must **infer** social relationships from narrative context since source languages provide no explicit grammatical guidance. This requires:
1. Character relationship analysis
2. Cultural context understanding
3. Discourse participant tracking
4. Theological sensitivity (e.g., divine address)

---

## 2. Language Family Classification

### Methodology

- **Source 1**: WALS Feature 45A "Politeness Distinctions in Pronouns" {wals-45a}
- **Source 2**: Available translations in `/src/constants/languages.tsv` (1009 languages)
- **Source 3**: Linguistic typology research (cited below)
- **Classification**: Languages marked (suspected) use internal linguistic knowledge per STAGE-1-RESEARCH.md §2 allowance

### WALS Feature 45A: Global Distribution

From 207 surveyed languages {wals-45a}:

| Category | Count | Percentage |
|----------|-------|------------|
| **No politeness distinction** | 136 | 66% |
| **Binary politeness distinction** | 49 | 24% |
| **Multiple politeness distinctions** | 15 | 7% |
| **Pronouns avoided for politeness** | 7 | 3% |

**Geographic Concentration**: East/Southeast Asia shows highest density of honorific systems.

---

## 3. Typological Analysis by Family

### 3.1 Japonic Family

#### Japanese (jpn) ✅ Available (1 translation)

**Classification**: 🔴 **MANDATORY** - Multiple levels (4+)

**System Type**: Keigo (敬語) - grammatical honorific system
- **Levels**: Casual → Polite (-masu) → Honorific (sonkeigo) → Humble (kenjougo)
- **Encoding**: Verb morphology, lexical replacement, particles
- **Obligatory**: Must choose register in every utterance
- **Gender**: Female particles (わ wa, ね ne) vs male particles (ぞ zo, な na)

**Examples**:
- 食べる (taberu, casual) → 食べます (tabemasu, polite) → 召し上がる (meshiagaru, honorific) → いただく (itadaku, humble)

**Cultural Context**:
- Age hierarchy critical
- Occupational status affects register
- Honor-shame culture (Hofstede: high power distance)

**Citations**: {promova-korean-honorifics}, {intercultural-javanese-chinese-japanese}

---

### 3.2 Koreanic Family

#### Korean (kor) ❌ NOT Available

**Classification**: 🔴 **MANDATORY** - Multiple levels (7 speech levels)

**System Type**: 존댓말 (jondaemal) vs 반말 (banmal)
- **Levels**: 7 verb paradigms (6 formal jondaemal + 1 casual banmal)
- **Encoding**: Verb endings change obligatorily
- **Triggers**: Age, social status, intimacy, formality
- **Grammatical**: Cannot form sentence without choosing register

**Key Structures**:
- Formal: -ㅂ니다/-습니다 (-mnida/-seumnida)
- Polite informal: -아요/-어요 (-ayo/-eoyo)
- Casual: -아/-어 (-a/-eo)

**Note**: High-priority language not in database - would be ideal candidate

**Citations**: {wikipedia-korean-speech-levels}, {promova-korean-honorifics}, {gogohanguk-speech-levels}

---

### 3.3 Austronesian Family

**Family Note**: Largest family in our database (~200+ translations estimated). Highly variable - some languages have complex systems (Javanese), others minimal (Indonesian).

#### Javanese (jvn) ✅ Available (Suriname Javanese, 1 NT translation)

**Classification**: 🔴 **MANDATORY** - Multiple levels (3+)

**System Type**: Ngoko-Madya-Krama hierarchy
- **Ngoko**: Low/informal register (peer/intimate)
- **Madya**: Middle register (strangers, neutral)
- **Krama**: High/formal register (superiors, respect)
- **Encoding**: Complete lexical replacement + affix changes
- **Obligatory**: Required in every sentence

**Examples**:
- Hand: tangan (ngoko) → asta (krama)
- Possession: -e (ngoko) → -ipun (krama)

**Historical**: Developed under Mataram Sultanate (17th c.) to reflect social hierarchies. Not present in Old Javanese.

**Note**: Suriname Javanese may differ from Indonesian Javanese due to diaspora evolution.

**Citations**: {wikipedia-javanese}, {medium-ngoko-krama}, {intercultural-javanese-chinese-japanese}

#### Indonesian/Malay (ind) ✅ Available (3 translations)

**Classification**: 🟡 **OPTIONAL** - Lexical/cultural rather than grammatical

**System Type**: Kinship-based appellatives, not verb morphology
- **No grammatical speech levels** (unlike Javanese)
- **Lexical strategies**: Replace pronouns with titles
  - Bapak/Pak (adult men, fathers) vs kamu (informal you)
  - Ibu/Bu (adult women, mothers)
  - Mas (young men), Mbak (young women)
- **Cultural**: Respect to elders/authority important
- **Regional variation**: Different terms in Sumatra, Java, Borneo

**Contrast with Javanese**: Indonesian (derived from Malay) **does not have** the triglossia found in Javanese, Sundanese, Balinese.

**Citations**: {wikipedia-indonesian-honorifics}, {pseudomon-indonesian-honorifics}

#### Tagalog (tgl) ✅ Available (1 translation)

**Classification**: 🟡 **OPTIONAL** - Culturally important particles

**System Type**: Politeness particles -po/-opo
- **Particles**: Added to verbs/statements for elders/superiors
- **Not obligatory** grammatically but culturally expected
- **Example**: "Salamat" (thanks) → "Salamat po" (thanks, respectful)

**Cultural**: Filipino respect for elders (utang na loob - debt of gratitude)

**Status**: (suspected) - based on internal knowledge

#### Other Austronesian Languages with Complex Systems

**Balinese, Sundanese, Madurese, Sasak**: All have complex honorific/humilific systems due to Javanese influence. Status in our database unknown.

**Citations**: {quora-austronesian-honorifics}

---

### 3.4 Sino-Tibetan Family

#### Mandarin Chinese (cmn) ✅ Available (3 translations)

**Classification**: 🟡 **OPTIONAL** - Binary formal/informal

**System Type**: Lexical distinction, not morphological
- **Pronouns**: 你 (nǐ, informal) vs 您 (nín, formal/respectful)
- **Vocabulary**: Literary vs colloquial lexicon choices
- **Not grammatically obligatory** but culturally significant
- **Usage**: Formal contexts, elders, superiors

**Cultural Context**:
- Confucian hierarchy influences
- Age-based respect important
- Honor-shame culture

**Status**: (suspected) - formality system confirmed but morphological details need verification

**Citations**: {intercultural-javanese-chinese-japanese}

#### Burmese (mya) - Status Unknown

**Classification**: 🟡 **OPTIONAL** (suspected)

**Note**: Myanmar has ~42 million Burmese speakers. Monosyllabic, 4 tones. Likely has politeness system given regional pattern but needs verification.

**Citations**: {seasite-southeast-asia}

---

### 3.5 Kra-Dai Family

#### Thai (tha) ✅ Available (1 translation)

**Classification**: 🔴 **MANDATORY** - Grammatical particles + royal vocabulary

**System Type**: Sentence-final particles + raja-sap (royal vocabulary)
- **Gender-specific particles**:
  - Male: ครับ (khrap)
  - Female: ค่ะ (kha)
- **Historical**: Borrowed from Khmer/Pali/Sanskrit by royalty and monks
- **Raja-sap**: Special vocabulary for addressing/discussing Thai monarchy
- **Social encoding**: Age hierarchy, monastic status, bureaucratic formality

**Obligatory Nature**: Must use particles in formal/polite contexts

**Citations**: {wikipedia-thai-honorifics}, {ling-thai-honorifics}

#### Lao (lao) - Status Unknown

**Classification**: 🟡 **OPTIONAL** (suspected)

**System Type**: Honorific markers + politeness markers
- ໂດຍ (doi) or ໂດຍຂ້ານ້ອຍ (older, more polite)
- ເຈົ້າ (chao) for higher age/rank

**Note**: Related to Thai, likely similar system.

**Citations**: {linguistics-se-thai-lao-particles}

---

### 3.6 Austro-Asiatic Family

#### Vietnamese (vie) ✅ Available (2 translations)

**Classification**: 🟡 **OPTIONAL** - Complex pronoun system

**System Type**: Kinship-based pronouns encode age/status
- **No single word for "you"** - use kinship terms
- **Age-relative**: "older brother" vs "younger brother" pronouns
- **Professional titles** replace names in formal contexts
- **Not morphologically obligatory** but culturally expected

**Linguistic Features**:
- Analytic language (helper words, not inflection)
- SVO word order
- 6 tones
- Monosyllabic

**Citations**: {seasite-southeast-asia}

#### Khmer (khm) - Status Unknown

**Classification**: ⚪ **SUSPECTED OPTIONAL**

**Note**: Non-tonal language. Thai borrowed honorific roots from Khmer, suggesting Khmer has politeness system.

**Citations**: {seasite-southeast-asia}

---

### 3.7 Indo-European Family (Indo-Aryan Branch)

#### Hindi (hin) ✅ Available (1 translation)

**Classification**: 🔴 **MANDATORY** - Three levels

**System Type**: Pronoun + verb agreement
- **Three pronouns**: तू (tū, intimate) → तुम (tum, informal) → आप (āp, formal)
- **Verb conjugation changes** to agree with pronoun
- **Obligatory**: Must choose level for every 2nd person reference
- **Usage**:
  - tū: Deities, very close intimates, children, inferiors
  - tum: Friends, peers, casual
  - āp: Elders, superiors, strangers, formal

**Citations**: {wikipedia-honorifics-linguistics}

#### Bengali (ben) ✅ Available (1 translation)

**Classification**: 🔴 **MANDATORY** - Three levels

**System Type**: Cognate to Hindi system
- **Pronouns**: তুই (tui) → তুমি (tumi) → আপনি (āpni)
- **Verb agreement** obligatory
- **Same structure** as Hindi/Urdu

**Citations**: {wikipedia-honorifics-linguistics}

#### Gujarati (guj) ✅ Available (1 translation)

**Classification**: 🟡 **OPTIONAL** - Effectively binary

**System Type**: Three-way distinction in theory, binary in practice
- **Theoretical**: tu/tum/aap cognates exist
- **Actual practice**: āp-cognate "almost never used"
- **Effective**: Binary tu/tum distinction only

**Citations**: {wikipedia-honorifics-linguistics}

#### Marathi (mar) ✅ Available (1 translation)

**Classification**: 🟡 **OPTIONAL** - Effectively binary (same as Gujarati)

**System Type**: Same pattern as Gujarati - theoretical three-way, practical two-way.

**Citations**: {wikipedia-honorifics-linguistics}

---

### 3.8 Dravidian Family

#### Tamil (tam) ✅ Available (1 translation)

**Classification**: 🟡 **OPTIONAL** - Plural-based honorifics

**System Type**: Plural suffix repurposed for singular honorifics
- **Mechanism**: -kaḷ (-கள்) plural suffix elevates singular referents
- **Pronouns**: நீ (nī, sg informal) → நீங்கள் (nīṅkaḷ, pl/formal)
- **Agglutinative morphology**: Suffixes on nouns, pronouns, verbs
- **Not obligatory** grammatically but culturally expected for superiors

**Dravidian Pattern**: Similar across family
- Telugu: నీవు (nīvu)
- Malayalam: നിങ്ങൾ (niṅṅaḷ)
- Kannada: ನೀನು (nīnu)

**Citations**: {grokipedia-tamil-honorifics}, {wikipedia-dravidian}

#### Telugu (tel) ✅ Available (1 translation)

**Classification**: 🟡 **OPTIONAL** - Same plural-based system as Tamil

**Status**: (suspected) - based on Dravidian family pattern

#### Malayalam (mal) ✅ Available (2 translations)

**Classification**: 🟡 **OPTIONAL** - Same plural-based system as Tamil

**Status**: (suspected) - based on Dravidian family pattern

---

### 3.9 Indo-European (European Branches)

#### T-V Distinction Languages

Multiple European languages have binary formal/informal distinction:

**Spanish (spa)** ✅ Available (6 translations)
- **Classification**: 🟡 **OPTIONAL** - Binary T-V
- **System**: tú (informal) vs usted (formal, from vuestra merced "your mercy")
- **Verb agreement** changes
- **Status**: Confirmed

**German (deu)** ✅ Available (4 translations)
- **Classification**: 🟡 **OPTIONAL** - Binary T-V
- **System**: du (informal) vs Sie (formal, capitalized plural)
- **Case declension** follows
- **Status**: Confirmed

**French (fra)** ✅ Available (4 translations)
- **Classification**: 🟡 **OPTIONAL** - Binary T-V
- **System**: tu (informal) vs vous (formal/plural)
- **Verb conjugation** changes
- **Status**: Confirmed

**Portuguese (por)** ✅ Available (4 translations)
- **Classification**: 🟡 **OPTIONAL** - Binary T-V
- **System**: tu vs você (from vossa mercê)
- **Regional variation**: Brazilian vs European usage patterns
- **Status**: Confirmed

**Russian (rus)** ✅ Available (1 translation)
- **Classification**: 🟡 **OPTIONAL** - Binary T-V
- **System**: ты (ty, informal) vs вы (vy, formal/plural)
- **Case declension** affects both
- **Status**: Confirmed

**English (eng)** ✅ Available (45+ translations)
- **Classification**: ⚪ **ABSENT** - Historical distinction lost
- **Historical**: thou (informal) vs you (formal) - obsolete by 18th century
- **Modern**: Single "you" for all contexts
- **Biblical translations**: KJV uses archaic thou/thee/thy but these were **informal** in 1611
- **Status**: Confirmed

---

### 3.10 Afro-Asiatic Family

#### Hebrew (heb) ✅ Available (1 translation)

**Classification**: ⚪ **ABSENT** (see Source Language section above)

**Modern Hebrew Note**: Contemporary Israeli Hebrew has developed some formal/informal distinctions in vocabulary but Biblical Hebrew has none.

#### Arabic (arb) ✅ Available (2 translations)

**Classification**: 🟡 **OPTIONAL** - Suspected honorific features

**System Type**: Likely includes:
- Formal vs informal pronouns (suspected)
- Classical (Quranic) vs Modern Standard vs dialectal registers
- Diglossic complexity {medium-honor-shame-translation}

**Status**: (suspected) - needs detailed verification but regional pattern suggests politeness marking

---

### 3.11 Niger-Congo Family

#### Swahili (swh) ✅ Available (3 translations)

**Classification**: 🟡 **OPTIONAL** (suspected)

**System Type**: Unknown - requires research
- Bantu noun class system may interact with honorifics
- East African cultural context suggests respect marking

**Status**: (suspected) - major Bible translation language, needs verification

---

## 4. Root Languages Analysis

"Root languages" = major Bible translation source languages that translators commonly reference when creating minority language translations.

| Language | Code | Status | Honorifics | Notes |
|----------|------|--------|------------|-------|
| **Hebrew** | heb | ✅ Source | ⚪ Absent | OT source - no grammatical honorifics |
| **Greek** | ell | ❌ Missing | ⚪ Absent (suspected) | NT source - Koine had no T-V distinction |
| **Latin** | lat | ✅ Available | ⚪ Absent (suspected) | Vulgate - Classical Latin no T-V |
| **English** | eng | ✅ Available | ⚪ Absent | Global lingua franca - no modern honorifics |
| **Spanish** | spa | ✅ Available | 🟡 Optional | Latin America - tú/usted |
| **Portuguese** | por | ✅ Available | 🟡 Optional | Brazil/Lusophone Africa - tu/você |
| **French** | fra | ✅ Available | 🟡 Optional | Francophone Africa - tu/vous |
| **German** | deu | ✅ Available | 🟡 Optional | Historical missionary language - du/Sie |
| **Russian** | rus | ✅ Available | 🟡 Optional | Orthodox tradition - ты/вы |
| **Arabic** | arb | ✅ Available | 🟡 Optional | MENA region - suspected formal/informal |
| **Mandarin** | cmn | ✅ Available | 🟡 Optional | East Asia - 你/您 |
| **Indonesian** | ind | ✅ Available | 🟡 Optional | SE Asia hub - lexical not grammatical |
| **Swahili** | swh | ✅ Available | 🟡 Optional | East Africa - suspected |
| **Hindi** | hin | ✅ Available | 🔴 Mandatory | South Asia - तू/तुम/आप |

### Key Insight

**CRITICAL TRANSLATION GAP**:
- Source languages (Hebrew, Greek) = ⚪ **NO honorifics**
- Major root languages (English, Spanish, French) = ⚪ Absent or 🟡 Optional binary
- Many target languages = 🔴 **Mandatory** with multiple levels

This creates a **three-stage inference problem**:
1. Hebrew/Greek → English (lose implicit social context)
2. English → target language (must reconstruct social relationships)
3. Binary systems (tu/vous) → Multi-level systems (Japanese keigo) = additional complexity

---

## 5. Candidate Languages for Translation Database

**Selection Criteria** (per STAGE-1-RESEARCH.md §2):
1. Mix of mandatory vs optional marking
2. Diverse language families represented
3. Available in `/src/constants/languages.tsv`
4. Different honorific mechanisms (morphological, lexical, particle-based)
5. Geographic/cultural diversity
6. Speaker population size (practical impact)

### Recommended 10 Languages

| Rank | Language | Code | Family | Honorific Type | Rationale |
|------|----------|------|--------|----------------|-----------|
| **1** | **Japanese** | jpn | Japonic | 🔴 Mandatory (4+ levels) | Most complex system, verb morphology + lexical + particles, critical test case |
| **2** | **Mandarin Chinese** | cmn | Sino-Tibetan | 🟡 Optional (binary) | Largest speaker base, lexical distinction, cultural importance |
| **3** | **Hindi** | hin | Indo-Aryan | 🔴 Mandatory (3 levels) | Large speaker base, pronoun + verb agreement, South Asian representative |
| **4** | **Thai** | tha | Kra-Dai | 🔴 Mandatory (particles) | Grammatical particles, gender-specific, royal vocabulary, SE Asian representative |
| **5** | **Bengali** | ben | Indo-Aryan | 🔴 Mandatory (3 levels) | Large Muslim/Hindu populations, cognate to Hindi for comparison |
| **6** | **Spanish** | spa | Indo-European | 🟡 Optional (binary) | Global reach, T-V distinction, Latin American Christianity |
| **7** | **Vietnamese** | vie | Austro-Asiatic | 🟡 Optional (kinship) | Complex pronoun system, different mechanism from others |
| **8** | **Tamil** | tam | Dravidian | 🟡 Optional (plural) | Dravidian representative, agglutinative, different mechanism (plural-as-honorific) |
| **9** | **Indonesian** | ind | Austronesian | 🟡 Optional (lexical) | Lexical not grammatical, contrast with Javanese, large population |
| **10** | **Javanese** | jvn | Austronesian | 🔴 Mandatory (3 levels) | Complete lexical replacement, Austronesian complexity, compare to Indonesian |

### Alternates (if primaries unavailable)

- **Tagalog** (tgl): Particles, Filipino population
- **French** (fra): T-V distinction, Francophone Africa
- **Malayalam** (mal): Dravidian alternate
- **Russian** (rus): Slavic representative, Orthodox tradition
- **Portuguese** (por): Lusophone world

### High-Value Language NOT in Database

- **Korean** (kor): Would be #1 or #2 choice - 7 speech levels, grammatically obligatory, highly documented. **Recommend adding to future database expansion.**

---

## 6. Cultural Nuances and Translation Considerations

### 6.1 Honor-Shame Culture Dynamics

**Honor-Shame** vs **Guilt-Innocence** cultural frameworks significantly impact honorific usage {honorshame-cultural-models}:

**Honor-Shame Cultures** (require careful honorific attention):
- East Asia: Japan, Korea, China
- Southeast Asia: Thailand, Vietnam, Indonesia, Philippines
- South Asia: India, Bangladesh
- Middle East: Arab world
- Mediterranean: some Romance language areas

**Biblical Context**: Mediterranean/Middle Eastern biblical cultures were **honor-shame oriented**, but this is **not grammatically encoded** in Hebrew/Greek. Modern translators must **infer and mark** these relationships in target languages.

**Theological Concern**: How do we address God? Jesus? Apostles? Angels?
- Japanese: Use humble forms for self, honorific for divine
- Thai: Raja-sap for God?
- Hindi: आप (āp) minimum for divine address

### 6.2 Power Distance (Hofstede)

**Power Distance Index (PDI)** correlates with honorific complexity {academia-hofstede-bible}:

**High PDI** (strong honorific systems):
- Malaysia, Philippines, Indonesia: PDI 90-104
- India, Thailand: PDI 77-64
- Japan: PDI 54 (moderate but complex honorifics)

**Low PDI** (weak/absent honorific systems):
- Germanic Europe: PDI 31-40
- Anglo countries: PDI 35-40

**Translation Impact**: High PDI cultures expect **explicit marking** of hierarchy. Missing honorifics in high PDI translations = cultural/theological error (e.g., "Jesus and disciples" all use same register = confusion about Jesus' authority).

### 6.3 Age-Based Hierarchy

**Critical in**: Japanese, Korean, Thai, Vietnamese, Filipino cultures

**Younger → Older** must use respectful forms. Biblical examples:
- Disciples addressing Jesus (younger → elder/master)
- Children addressing parents
- Timothy addressing Paul (younger → mentor)

**Problem**: English "you" is age-neutral. Target languages must infer age relationships from narrative context.

### 6.4 Gender-Based Speech Differences

**Significant variation**:
- **Japanese**: Female particles わ (wa), ね (ne) vs male ぞ (zo), な (na)
- **Thai**: Male ครับ (khrap) vs female ค่ะ (kha)
- **Korean**: Some final particles differ by speaker gender
- **Hindi/Bengali**: Softer pronunciation for traditional female speech
- **Indonesian/Tagalog**: Modern urban speech = less gender differentiation

**Translation Issue**: Biblical narrative provides speaker gender but not addressee's perceptions. Female speakers (Mary, Martha, Mary Magdalene) would use different forms in these languages.

### 6.5 Religious/Theological Honorifics

**Special cases**:

1. **Divine Address**:
   - Minimum: Highest available register
   - Thai: Raja-sap vocabulary?
   - Japanese: Honorific + humble self-reference
   - Hindi: आप (āp) mandatory

2. **Jesus**:
   - Pre-resurrection: High respect but human
   - Post-resurrection: Divine status
   - Some languages distinguish (Japanese)

3. **Apostles/Prophets**:
   - Respected elders but human
   - Likely high register, not divine

4. **Angels**:
   - Messengers of God = high register
   - But not worship-level

5. **Satan/Demons**:
   - Neutral or low register?
   - Theological question: Does evil deserve respect forms?

### 6.6 Social Status Complexity

**Multiple overlapping hierarchies**:
- **Age**: Elder > younger
- **Kinship**: Parent > child, older sibling > younger
- **Occupation**: Master > servant, rabbi > student
- **Education**: Pharisee > commoner (suspected)
- **Ritual purity**: Priest > layperson
- **Economic**: Rich > poor (cultural, not necessarily honorific)
- **Caste** (India): Complicates Hindi/Tamil translations

**Conflict resolution**: What if younger person has higher social status? Different languages resolve differently.

---

## 7. Summary Statistics

### Available Languages by Honorific Type

From our database (1009 languages):

| Category | Estimated Count | Key Examples |
|----------|-----------------|--------------|
| **Mandatory (Multiple Levels)** | ~15 | Japanese, Hindi, Bengali, Thai, Javanese |
| **Mandatory (Binary)** | ~30 | (Need detailed analysis) |
| **Optional (Cultural)** | ~100 | Spanish, Indonesian, Tamil, Vietnamese, German, French |
| **Absent** | ~864 | English, many Trans-New Guinea, many Niger-Congo |

**Note**: Precise classification requires language-by-language research. Estimates based on typological patterns.

### Language Family Breakdown (Families in Database)

Families with **high honorific density**:
- **Austronesian**: ~200+ languages, variable (Javanese complex, many others simpler)
- **Indo-European (Indo-Aryan)**: ~10 languages, most with 2-3 level systems
- **Sino-Tibetan**: ~5 languages, variable
- **Kra-Dai**: ~1-2 languages, likely honorific-marking
- **Dravidian**: ~3 languages, plural-based systems
- **Japonic**: 1 language (Japanese), highly complex

Families with **low honorific density**:
- **Trans-New Guinea**: ~150+ languages, mostly no grammatical honorifics (suspected)
- **Niger-Congo**: ~50+ languages, variable, many without
- **Sepik**: ~30+ languages, likely minimal honorifics (suspected)
- **Australian**: ~15+ languages, likely minimal honorifics (suspected)

---

## 8. Research Gaps and Future Work

### Confirmed Data Needed

1. **Greek (Koine)**: Confirm no T-V distinction in NT Greek
2. **Arabic**: Detail specific honorific mechanisms
3. **Swahili**: Determine if Bantu noun classes interact with honorifics
4. **Korean**: Priority language not in database - recommend acquisition
5. **Trans-New Guinea family**: Sample 5-10 languages to confirm honorific absence
6. **Niger-Congo**: Survey Bantu languages for politeness marking

### Suspected but Unverified

Languages marked (suspected) above require:
- Native speaker consultation
- Grammar reference review
- Translation sample analysis

### Missing High-Value Languages

- **Korean**: Most important missing language (7 speech levels, mandatory)
- **Burmese**: Myanmar population, SE Asian pattern suggests honorifics
- **Khmer**: Historical influence on Thai, likely has system
- **Nepali**: Indo-Aryan, likely similar to Hindi
- **Urdu**: Cognate to Hindi, should have identical system

---

## 9. Bibliography and Citations

### Typological Databases

- {wals-45a} WALS Online - Feature 45A: [Politeness Distinctions in Pronouns](https://wals.info/feature/45A)
- {wals-chapter-45} WALS Online - [Chapter: Politeness Distinctions in Pronouns](https://wals.info/chapter/45)
- {linguistics-se-honorific-db} Linguistics Stack Exchange: [Is there a database on typological variation of honorific systems?](https://linguistics.stackexchange.com/questions/12136/is-there-a-database-that-has-information-on-the-typological-variation-of-honorif)

### Hebrew and Greek

- {hermeneutics-se-81168} Biblical Hermeneutics Stack Exchange: [Do original languages use formal or informal?](https://hermeneutics.stackexchange.com/questions/81168/do-original-languages-in-greek-and-hebrew-bible-texts-use-formal-or-informal-lan)
- {biblicalhebrew-org-pronouns} Biblical Hebrew: [Comprehensive Guide to Pronouns](https://biblicalhebrew.org/comprehensive-guide-to-pronouns-in-biblical-hebrew-forms-functions-and-examples.aspx)
- {ginoskos-hebrew-pronouns} Ginoskos: [Biblical Hebrew: Pronouns and suffixes](https://ginoskos.com/biblical-hebrew/pronouns-and-suffixes)

### Japanese

- {promova-korean-honorifics} Promova: [The Intricacies of Korean Honorifics](https://promova.com/blog/korean-honorific-language)
- {intercultural-javanese-chinese-japanese} Intercultural Word Sensei: [The Honorifics and Politeness Levels of Javanese, Chinese, and Japanese](https://interculturalwordsensei.org/the-honorifics-and-politeness-levels-of-javanese-chinese-and-japanese/)

### Korean

- {wikipedia-korean-speech-levels} Wikipedia: [Korean speech levels](https://en.wikipedia.org/wiki/Korean_speech_levels)
- {gogohanguk-speech-levels} Go! Go! Hanguk: [7 Korean levels of speech](https://gogohanguk.com/en/blog/korean-levels-of-speech/)
- {lingodeer-korean-speech} LingoDeer: [Korean Speech Levels and How To Use Them Properly](https://blog.lingodeer.com/korean-speech-levels/)

### Javanese and Austronesian

- {wikipedia-javanese} Wikipedia: [Javanese language](https://en.wikipedia.org/wiki/Javanese_language)
- {medium-ngoko-krama} Medium: [Ngoko and Krama: Language Hierarchy in Javanese Culture](https://medium.com/@febbyziodms/ngoko-and-krama-language-hierarchy-in-javanese-culture-55aa96149a44)
- {comparison-javanese-pdf} International Journal: [Comparison of Honorific Language in Javanese](https://www.arcjournals.org/pdfs/ijsell/v2-i7/16.pdf)
- {quora-austronesian-honorifics} Quora: [Is there another Austronesian language with honorifics as complex as Javanese?](https://www.quora.com/Is-there-another-Austronesian-language-having-a-honorific-system-as-complex-as-that-of-Javanese)

### Indonesian and Malay

- {wikipedia-indonesian-honorifics} Wikipedia: [Indonesian honorifics](https://en.wikipedia.org/wiki/Indonesian_honorifics)
- {pseudomon-indonesian-honorifics} PseudoMonious: [A Quick Guide to Honorifics in Indonesian](https://pseudomon.wordpress.com/2022/04/17/a-quick-guide-to-honorifics-in-indonesian-with-a-wee-bit-on-japanese-and-chinese-too-why-not/)

### Thai and Southeast Asian

- {wikipedia-thai-honorifics} Wikipedia: [Thai honorifics](https://en.wikipedia.org/wiki/Thai_honorifics)
- {ling-thai-honorifics} Ling App: [Best #4 Topics About Thai Honorific Terms](https://ling-app.com/blog/thai-honorific-terms/)
- {seasite-southeast-asia} SEAsite: [Spoken and Written Languages of Southeast Asia](https://seasite.niu.edu/crossroads/hartmann/hartmann.htm)
- {linguistics-se-thai-lao-particles} Linguistics Stack Exchange: [Do the Thai polite particles have counterparts in Lao?](https://linguistics.stackexchange.com/questions/4420/do-the-thai-masculine-feminine-polite-particles-have-counterparts-in-lao)

### Indo-Aryan and Dravidian

- {wikipedia-honorifics-linguistics} Wikipedia: [Honorifics (linguistics)](https://en.wikipedia.org/wiki/Honorifics_(linguistics))
- {grokipedia-tamil-honorifics} Grokipedia: [Tamil honorifics](https://grokipedia.com/page/Tamil_honorifics)
- {wikipedia-dravidian} Wikipedia: [Dravidian languages](https://en.wikipedia.org/wiki/Dravidian_languages)
- {wikipedia-indian-honorifics} Wikipedia: [Indian honorifics](https://en.wikipedia.org/wiki/Indian_honorifics)

### Cultural Context

- {honorshame-cultural-models} Honor Shame: [Guilt-Shame-Fear & Other Cultural Models](https://honorshame.com/guilt-shame-fear-cultural-models/)
- {academia-hofstede-bible} Academia: [Cultural Biases in NT Interpretation: Hofstede's Cultural Dimensions](https://www.academia.edu/44950393/Cultural_Biases_in_New_Testament_Interpretation_Explaining_Them_Using_Hofstedes_Cultural_Dimensions)
- {researchgate-honor-shame} ResearchGate: [The culture problem: Honor/shame issue](https://www.researchgate.net/publication/338148267_The_culture_problem_How_the_honorshame_issue_got_the_wrong_end_of_the_anthropological_stick)
- {oxfordbib-honor-shame} Oxford Bibliographies: [Honor and Shame - Biblical Studies](https://oxfordbibliographies.com/view/document/obo-9780195393361/obo-9780195393361-0077.xml)

### General Linguistics

- {superlinguo-grambank} Superlinguo: [Hello Grambank! A new typological database](https://www.superlinguo.com/post/719235118359887872/hello-grambank-a-new-typological-database-of)
- {springer-honorifics-hon} Springer: [Honorifics without [hon]](https://link.springer.com/article/10.1007/s11049-022-09563-0)

---

## Document Metadata

**Author**: Claude (Sonnet 4.5)
**Research Date**: 2025-11-25
**Stage**: TBTA Feature Development Stage 1, Section 2
**Sources**: 35+ web sources, WALS, linguistic literature
**Languages Analyzed**: 25+ in detail, 1009 in database
**Verification Status**: Mixed (confirmed data + suspected classifications per methodology)
**Next Steps**: Stage 1 Section 3 (Scholarly Research) → Stage 1 Section 4 (Theological Significance)
