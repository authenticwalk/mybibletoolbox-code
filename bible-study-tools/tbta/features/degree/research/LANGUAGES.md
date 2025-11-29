# Language Family & Typology Analysis: Degree

**Feature**: Degree (Comparative/Superlative/Intensified)
**Analysis Date**: 2025-11-29
**Corpus**: 1,009 Bible translation languages

---

## Executive Summary

Degree marking exhibits extreme typological diversity. While the semantic concept (comparing qualities or intensifying them) appears universal, the grammatical encoding ranges from:
- **Mandatory morphology** (Greek, Latin, Arabic) to
- **Optional syntax** (Mandarin, many Austronesian) to
- **Context-dependent periphrasis** (Biblical Hebrew)

**Critical finding**: Degree is MORPHOLOGICALLY EXPLICIT in Greek but SEMANTICALLY INFERRED in Hebrew, requiring different prediction strategies for OT vs NT.

**Coverage**: Analysis of 176 Austronesian, 141 Trans-New Guinea, 135 Indo-European, 89 Niger-Congo, and 400+ other languages from our corpus.

---

## 1. Source Language Encoding (CRITICAL)

### 1.1 Koine Greek: EXPLICIT Morphological Encoding

**Status**: MORPHOLOGICALLY MANDATORY for gradable adjectives/adverbs

**Formation**:
- **Comparative**: -τερος/-τέρα/-τερον (-teros/-tera/-teron)
  - Example: μέγας (megas "great") → μείζων (meizōn "greater")
- **Superlative**: -τατος/-τάτη/-τατον (-tatos/-tatē/-taton) or -ιστος/-ίστη/-ιστον (-istos/-istē/-iston)
  - Example: μέγας → μέγιστος (megistos "greatest")

**Frequency in NT**: Superlatives are RARE {greek-nt-grammar}
- Most common: πρῶτος (prōtos "first"), ἔσχατος (eschatos "last")
- Comparative often used with superlative/elative meaning

**Morphology ≠ Semantics**:
- Comparative form can function as: comparative, superlative, OR elative
- Superlative form can function as: superlative, comparative, OR elative
- Context determines semantic function

**Implication**: Greek provides EXPLICIT morphological cues, but semantic interpretation still required.

### 1.2 Biblical Hebrew: NO Dedicated Degree Morphology

**Status**: PERIPHRASTIC ONLY - no morphological degree marking

**Formation Strategies**:

**1. Comparative**: Preposition מִן (min "from/than")
```
Structure: Adjective + מִן + Standard
Example: "David is tall from Saul" = "David is taller than Saul"
```

**2. Superlative**: Definite article or construct state
```
Strategy A: Article + Adjective + Genitive
Example: "the good of the land" = "the best land"

Strategy B: Noun + Genitive Noun (X of Xs)
Example: "song of songs" = "greatest song"
```

**3. Elative/Intensification**: Genitive construction
```
Structure: Adjective + Genitive "of God"
Example: "mighty of God" = "very mighty"
```

**Biblical vs. Modern Hebrew**:
- **Modern Hebrew**: HAS developed comparative/superlative paradigm
- **Biblical Hebrew**: Lacks dedicated degree morphology
- **Implication**: All OT degree annotations are INTERPRETIVE, not morphological

**Challenge**: Identifying which periphrastic constructions express degree vs. other meanings requires deep syntactic/contextual analysis.

### 1.3 Summary: Source Language Asymmetry

| Aspect | Koine Greek | Biblical Hebrew |
|--------|-------------|-----------------|
| **Morphology** | Explicit (-τερος, -τατος) | None |
| **Syntax** | Morphology + periphrastic | Periphrastic only (מִן, construct) |
| **Ambiguity** | Form exists, function varies | Function inferred from syntax |
| **Frequency** | Productive (esp. comparative) | Context-dependent |
| **Prediction** | Morphology + context | Context + syntax only |

**CRITICAL**: Algorithms must handle morphological AND periphrastic systems.

---

## 2. Root Translation Languages

### 2.1 Major Bible Translation Source Languages

Languages translators commonly start from (priority order):

| Language | ISO-639-3 | Family | Degree Status | Evidence |
|----------|-----------|--------|---------------|----------|
| **Hebrew** | heb | Afro-Asiatic | Periphrastic only | Biblical source (OT) |
| **Greek** | ell | Indo-European | Morphological | Biblical source (NT) |
| **English** | eng | Indo-European | Morphological + analytic | Global lingua franca |
| **Spanish** | spa | Indo-European | Morphological (más/menos) | Latin America, Philippines |
| **French** | fra | Indo-European | Analytic (plus/moins) | Francophone Africa |
| **Arabic** | arb | Afro-Asiatic | Morphological (af'al pattern) | Middle East, North Africa |
| **Indonesian** | ind | Austronesian | Analytic (lebih/paling) | Southeast Asia, 175M speakers |
| **Swahili** | swa | Niger-Congo | Analytic (zaidi, kuliko) (suspected) | East Africa |
| **Portuguese** | por | Indo-European | Morphological (mais/menos) | Brazil, Lusophone Africa |
| **German** | deu | Indo-European | Morphological (-er, -ste) | Historical translation base |
| **Latin** | lat | Indo-European | Morphological (-ior, -issimus) | Historical Vulgate |

**Observation**: 9 of 11 root languages have GRAMMATICALIZED degree marking (morphological or analytic). Only Biblical Hebrew lacks it.

### 2.2 Degree Status in Root Languages

**Mandatory Morphological**: Greek, Latin, German, Arabic
**Mandatory Analytic**: English (mixed), Spanish, French, Portuguese, Indonesian, Swahili (suspected)
**Periphrastic/Optional**: Biblical Hebrew

**Implication**: Most translators work from languages WHERE degree IS marked, translating INTO languages where it may or may not be.

---

## 3. Typological Classification by Language Family

### 3.1 Indo-European (135 languages in corpus)

**Degree Status**: **MANDATORY** in most branches

**Characteristics**:
- Strong tradition of morphological degree (inherited from Proto-IE)
- Three-way system: positive, comparative, superlative
- Morphological (Germanic, Slavic, Baltic) OR analytic (Romance, some Germanic)

**Examples from Corpus**:

| Language | ISO-639-3 | Comparative Strategy | Superlative Strategy |
|----------|-----------|---------------------|---------------------|
| Spanish | spa | más + Adj (analytic) | el más + Adj (analytic) |
| Russian | rus | -ее/-ей (morphological) (suspected) | -ейший (morphological) (suspected) |
| Hindi | hin | ज़्यादा zyādā + Adj (suspected) | सबसे sabse + Adj (suspected) |
| Albanian | als | më + Adj (suspected) | më + Adj (suspected) |
| Lithuanian | lit | -esn- (morphological) (suspected) | -iausi- (morphological) (suspected) |

**Key Pattern**: Romance languages (Spanish, French, Portuguese) use ANALYTIC degree (más/plus/mais), while Germanic/Slavic prefer MORPHOLOGICAL.

**Theological Relevance**: Indo-European languages dominate global Christianity; most have explicit degree marking.

### 3.2 Austronesian (176 languages in corpus)

**Degree Status**: **OPTIONAL** - analytic constructions available but not obligatory

**Characteristics**:
- Analytic degree marking using separate words
- Reduplication for intensification common
- Stative verbs often blur adjective/verb distinction

**Examples from Corpus**:

| Language | ISO-639-3 | Comparative Strategy | Intensification |
|----------|-----------|---------------------|-----------------|
| Tagalog | tgl | mas + Adj (suspected) | Reduplication (mabuti → mabubuti) {austronesian-2025} |
| Indonesian | ind | lebih + Adj / paling (superlative) (suspected) | sangat "very" (suspected) |
| Malay | zsm | lebih + Adj (suspected) | amat "very" (suspected) |
| Fijian | fij | analytic (suspected) | Context-dependent |
| Malagasy | mlg | kokoa + Adj (suspected) | Context-dependent |

**Key Pattern**: Stative verbs function as adjectives; reduplication marks plurality/intensity {austronesian-grammar-2025}.

**Challenge**: Distinguishing intensification (reduplication) from true comparison requires contextual analysis.

**Theological Relevance**: 176 languages = 17% of corpus. Philippines (Catholic/Protestant), Indonesia (Muslim-majority, Christian minority) = major mission fields.

### 3.3 Trans-New Guinea (141 languages in corpus)

**Degree Status**: **VARIES** - highly language-specific, often minimal

**Characteristics**:
- Many languages lack grammaticalized comparison
- Contextual/pragmatic comparison common
- Verb-oriented; fewer pure adjectives

**Examples** (suspected, limited documentation):
- Many TNG languages: Contextual comparison without dedicated morphology
- Comparison expressed through clausal constructions ("X surpasses Y in Z")
- Intensification through adverbs or verb modality

**Challenge**: TNG languages notoriously under-documented; degree systems poorly understood.

**Theological Relevance**: 141 languages, mostly Papua New Guinea. High linguistic diversity, low resource availability.

### 3.4 Niger-Congo (89 languages in corpus)

**Degree Status**: **ANALYTIC** - separate degree words, postposed to adjective

**Characteristics**:
- Degree words FOLLOW adjectives {niger-congo-2025}
- Noun-initial noun phrases (adjectives follow noun)
- Agreement systems (noun classes) affect degree marking (suspected)

**Examples from Corpus**:

| Language | ISO-639-3 | Comparative Strategy | Notes |
|----------|-----------|---------------------|-------|
| Swahili | swa | zaidi (more), kuliko (than) (suspected) | Bantu noun class agreement |
| Akan | aka | sene (than/more) (suspected) | Kwa branch |
| Yoruba | yor | jù (more/surpass) (suspected) | Isolating structure |

**Key Pattern**: Degree words are POSTPOSED (follow adjective), unlike English {niger-congo-typology-2025}.

**Theological Relevance**: 89 languages, Sub-Saharan Africa. Christianity dominant in many regions.

### 3.5 Afro-Asiatic (25 languages in corpus)

**Degree Status**: **MORPHOLOGICAL** (Semitic) or **ANALYTIC** (other branches)

**Characteristics**:
- Semitic: Templatic morphology (Arabic af'al pattern)
- Elative conflates comparative/superlative
- Rich intensification systems

**Examples from Corpus**:

| Language | ISO-639-3 | Branch | Degree Strategy |
|----------|-----------|--------|-----------------|
| Arabic (Standard) | arb | Semitic | af'al pattern (elative) {arabic-morphology-2025} |
| Amharic | amh | Semitic | Semitic patterns (suspected) |
| Hausa | hau | Chadic | Analytic (suspected) |
| Oromo | orm | Cushitic | Analytic (suspected) |

**Arabic Elative**: Pattern af'al (أَفْعَل) serves as BOTH comparative and superlative:
- Indefinite + min = comparative ("greater than")
- Definite = superlative ("the greatest")
- Alone = elative ("very great")

**Theological Relevance**: Arabic is a major root language for Middle Eastern translations.

### 3.6 Sino-Tibetan (18 languages in corpus)

**Degree Status**: **ANALYTIC** - particles mark degree, no morphology

**Characteristics**:
- Mandarin: 更 gèng (more), 最 zuì (most) {mandarin-grammar-2025}
- Particle-based intensification
- No adjective inflection

**Examples from Corpus**:

| Language | ISO-639-3 | Comparative | Superlative | Intensification |
|----------|-----------|-------------|-------------|-----------------|
| Mandarin | cmn | 更 gèng + Adj | 最 zuì + Adj | 很 hěn "very" |
| Cantonese | yue | 更 gang + Adj (suspected) | 最 zeoi + Adj (suspected) | 好 hou (suspected) |

**Key Pattern**: Preverbal/pre-adjectival particles. No agreement, no morphology.

**Theological Relevance**: Mandarin = 1.1B speakers, largest Bible translation market.

### 3.7 Quechuan (18 languages in corpus)

**Degree Status**: **SUFFIXAL MORPHOLOGY** (suspected)

**Characteristics**:
- Agglutinative morphology
- Rich suffix inventory (suspected)
- Evidentiality markers (MANDATORY) may interact with degree (suspected)

**Evidence**: Limited documentation available. Quechuan languages are suffixing; degree likely marked by dedicated suffixes.

**Theological Relevance**: 18 languages, Andean region (Peru, Bolivia, Ecuador). Catholic/Evangelical missions.

### 3.8 Mayan (41 languages in corpus)

**Degree Status**: **VARIES** - complex morphology, degree may be marked

**Characteristics**:
- Verb-initial languages
- Complex agreement systems
- Degree marking under-documented

**Evidence**: Mayan languages have rich derivational morphology; comparative/superlative may be marked morphologically or periphrastically (suspected).

**Theological Relevance**: 41 languages, Mesoamerica (Guatemala, Mexico). High indigenous Christian populations.

---

## 4. Typological Parameters

### 4.1 Morphological vs. Analytic

**Morphological Degree** (affixes on adjective):
- Indo-European: Germanic (English -er/-est, German -er/-ste), Slavic, Baltic
- Afro-Asiatic: Arabic (af'al pattern)
- Latin: -ior (comparative), -issimus (superlative)
- Greek: -τερος (comparative), -τατος/-ιστος (superlative)

**Analytic Degree** (separate words):
- Indo-European: Romance (más, plus, mais), English (more/most)
- Sino-Tibetan: Mandarin (更, 最)
- Austronesian: Indonesian (lebih, paling), Tagalog (mas)
- Niger-Congo: Swahili (zaidi, kuliko) (suspected)

**Periphrastic (syntactic constructions)**:
- Biblical Hebrew (מִן comparative, construct superlative)
- Many Trans-New Guinea languages (clausal comparison)

**Distribution in Corpus**:
- **Morphological**: ~30% (Indo-European, Afro-Asiatic Semitic, some agglutinative)
- **Analytic**: ~50% (Romance, Sino-Tibetan, Austronesian, Niger-Congo)
- **Periphrastic/Minimal**: ~20% (Trans-New Guinea, some Austronesian, Biblical Hebrew)

### 4.2 Comparative Construction Types (WALS Chapter 121)

From WALS typology {wals-comparative-2025}:

**1. Particle Comparative** (European base):
- English: "taller than"
- Spanish: "más alto que"
- French: "plus grand que"

**2. Exceed Comparative** (Africa, East/Southeast Asia):
- Structure: "X exceeds Y in Z"
- Common in Sub-Saharan Africa, China, SE Asia

**3. Conjoined Comparative** (Australia, New Guinea, Amazon):
- Structure: "X is tall and Y is short" → "X is taller than Y"
- Stronghold: Australia, Papua New Guinea, Amazon basin

**4. Locational Comparative**:
- Uses spatial metaphors ("X is big from Y")
- Hebrew מִן (min) fits this pattern

**Distribution Relevance**:
- **Corpus languages**: Heavily weighted toward Particle (Indo-European, Austronesian) and Exceed (Niger-Congo, Sino-Tibetan) types
- **Conjoined type**: Present in Trans-New Guinea (141 languages) and some Amazonian (Tupian, Maipurean)

### 4.3 Elative vs. Superlative

**Relative Superlative**: "X is the most Y" (comparison to set)
- English: "the tallest person"
- Spanish: "el más alto"

**Absolute Superlative / Elative**: "X is very Y" (no comparison)
- English: "a most interesting tale"
- Spanish: "-ísimo" (altísimo "very tall")
- Arabic: af'al pattern without min

**Cross-linguistic Prevalence**:
- **Elative morphology**: Arabic, Semitic languages, some Indo-European (Spanish -ísimo, Italian -issimo)
- **Elative as function**: Greek/Latin superlative forms used elatively
- **Intensification separate**: English "very", Mandarin 很 hěn, Indonesian sangat

**TBTA Relevance**: TBTA's "Intensified" and "Extremely Intensified" categories capture elative/intensification distinct from true comparison.

### 4.4 Equative Constructions

**Definition**: "as X as Y" constructions

**Typology** (Haspelmath & Buchholz 1998) {equative-typology-2025}:
- **European pattern**: Adverbial relative pronouns (as, wie, comme)
- **Non-European**: Diverse strategies (verb "equal", spatial metaphors, reduplication)

**Morphological Equatives** (rare):
- Welsh: distinct equative suffix
- Finno-Ugric, Kartvelian, Tagalog, Indonesian: morphological marking (suspected)

**TBTA Data**: 7 instances of "Equality" value (0.1%) suggests equatives are RARE or conflated with other degree values.

---

## 5. Language Selection for Translation Database (Stage 2)

### 5.1 Selection Criteria

1. **Typological Diversity**: Mix of morphological, analytic, periphrastic
2. **Family Representation**: Major families (Indo-European, Austronesian, Niger-Congo, etc.)
3. **Marking vs. Non-marking**: Languages that MUST mark degree vs. those that don't
4. **Resource Availability**: Languages with accessible translations
5. **Theological Importance**: Major Christian populations, diverse traditions

### 5.2 Proposed 10 Languages

| # | Language | ISO-639-3 | Family | Degree Type | Why Selected |
|---|----------|-----------|--------|-------------|--------------|
| 1 | **English** | eng | Indo-European | Morphological + analytic | Global standard, both strategies |
| 2 | **Spanish** | spa | Indo-European | Analytic (más/menos) | Major mission language, Latin America |
| 3 | **Mandarin** | cmn | Sino-Tibetan | Analytic (更/最) | 1.1B speakers, particle-based |
| 4 | **Arabic** | arb | Afro-Asiatic | Morphological (af'al elative) | Semitic (like Hebrew), templatic |
| 5 | **Indonesian** | ind | Austronesian | Analytic (lebih/paling) | Austronesian family, 175M speakers |
| 6 | **Swahili** | swa | Niger-Congo | Analytic (zaidi) | Bantu, postposed degree words |
| 7 | **Russian** | rus | Indo-European | Morphological | Slavic morphology, rich inflection |
| 8 | **Tagalog** | tgl | Austronesian | Analytic + reduplication | Philippine-type, intensification patterns |
| 9 | **French** | fra | Indo-European | Analytic (plus/moins) | Romance, analytic degree, global reach |
| 10 | **German** | deu | Indo-European | Morphological (-er/-ste) | Germanic morphology, theological tradition |

### 5.3 Additional Candidates (Backup/Expansion)

| Language | ISO-639-3 | Family | Rationale |
|----------|-----------|--------|-----------|
| Quechua (any variety) | que | Quechuan | Agglutinative, Andean missions |
| Yoruba | yor | Niger-Congo | West African, isolating structure |
| Amharic | amh | Afro-Asiatic | Ethiopian Orthodox, Semitic |
| Japanese | jpn | Isolate | Honorifics, postposed degree (suspected) |
| Hindi | hin | Indo-European | Indo-Aryan, 600M speakers |

### 5.4 Justification for Each Selection

**English**: Baseline; mixed morphological/analytic system provides both strategies.

**Spanish**: Purely analytic (más/menos/el más); huge corpus of translations; Latin America = major mission field.

**Mandarin**: Particle-based, no morphology; tests whether algorithm can handle isolating languages; massive speaker base.

**Arabic**: Templatic morphology (af'al elative conflates comparative/superlative); closest to Hebrew structure; major Middle Eastern language.

**Indonesian**: Austronesian analytic system; Southeast Asia; 175M speakers; tests family with stative verb/adjective blur.

**Swahili**: Bantu noun class agreement (suspected interaction with degree); tests postposed degree words; East African missions.

**Russian**: Rich morphological inflection; tests Slavic synthetic system; Orthodox theological tradition.

**Tagalog**: Reduplication for intensification; Philippine-type Austronesian; Catholic-majority country.

**French**: Romance analytic (like Spanish but different particles); Francophone Africa; Quebec missions.

**German**: Germanic morphology (synthetic); Luther's theological tradition; contrasts with English (mixed).

---

## 6. Cultural Nuances & Honorifics

### 6.1 Languages with Register/Honorific Systems

**Japanese** (jpn) - (not in top 10 but relevant):
- Honorific register affects adjective choice
- Degree may interact with politeness (suspected)
- Intensification culturally constrained (excessive praise = impolite)

**Korean** (kor) - (not in top 10 but relevant):
- Similar to Japanese; honorific suffixes
- Comparative constructions interact with social register (suspected)

**Javanese** (jav) - (Austronesian, in corpus):
- Elaborate honorific levels (ngoko, madya, krama)
- Degree marking may vary by register (suspected)

**Tagalog** (tgl):
- Modest honorific system (po/opo)
- Less elaborate than Japanese/Korean but present

### 6.2 Theological/Cultural Taboos

**Superlative for God**:
- Many languages restrict superlatives to deity
- Arabic: الله أكبر "Allahu Akbar" (God is greater/greatest) uses elative
- Theological implication: Using superlative for non-divine may be culturally sensitive

**Excessive Intensification**:
- Some cultures avoid hyperbole (Japanese, Korean)
- Others embrace it (Arabic, Spanish)
- Biblical translation must balance literal text with cultural appropriateness

**Comparative of "Good/Bad"**:
- Suppletive forms common (good/better/best, bad/worse/worst)
- Cross-linguistic: Suppletive comparatives nearly universal for "good/bad" (Bobaljik 2012) {bobaljik-universals-2025}
- Theological: "God is good" → "Who is better than God?" = sensitive construction

---

## 7. Mandatory vs. Optional Degree Marking

### 7.1 Mandatory (Must Mark Comparison)

**Languages where comparison REQUIRES degree morphology/syntax**:
- **Indo-European (most)**: Cannot express "X is taller than Y" without morphology (English -er) or analytic (Spanish más)
- **Arabic**: af'al pattern required for comparison
- **Mandarin**: Must use 更 gèng or 比 bǐ for comparison

**Implication**: Translators INTO these languages MUST determine degree even if source language doesn't mark it.

### 7.2 Optional (Comparison Can Be Implicit)

**Languages where comparison can be contextual**:
- **Some Trans-New Guinea**: Juxtaposition ("X is big, Y is small") implies comparison
- **Conjoined comparative languages**: Coordination implies comparison
- **Some Austronesian**: Context + intonation may suffice

**Implication**: Translators may omit explicit degree marking if context is clear.

### 7.3 Distribution in Corpus

**Estimated**:
- **Mandatory**: 70% of corpus (Indo-European, Afro-Asiatic, Sino-Tibetan, most Austronesian, Niger-Congo)
- **Optional**: 30% (Trans-New Guinea, some Austronesian, some Amazonian)

**Critical**: Even languages with MANDATORY degree marking may differ in morphological vs. analytic realization.

---

## 8. Key Distinctions Between Languages

### 8.1 Morphological Degree Languages

**Characteristics**:
- Degree marked by affixes on adjective/adverb
- Positive-Comparative-Superlative paradigm
- Often synthetic (one word)

**Examples**: German, Russian, Greek, Latin, Arabic (elative)

**Challenge**: Identifying which adjectives are gradable (can take degree morphology).

### 8.2 Analytic Degree Languages

**Characteristics**:
- Degree marked by separate words (particles, adverbs)
- Adjective remains unchanged
- Often multi-word phrases

**Examples**: Spanish (más), French (plus), Mandarin (更), Indonesian (lebih)

**Challenge**: Distinguishing degree markers from other intensifiers/modifiers.

### 8.3 Periphrastic/Minimal Degree Languages

**Characteristics**:
- No dedicated degree morphology
- Comparison expressed through syntactic constructions
- Often contextual

**Examples**: Biblical Hebrew (מִן), many Trans-New Guinea, some Austronesian

**Challenge**: Interpreting whether a construction expresses degree vs. other meanings.

### 8.4 Mixed Systems

**Characteristics**:
- Some degree marked morphologically, some analytically
- Often depends on adjective length/type

**Examples**:
- **English**: Short adjectives morphological (tall-taller-tallest), long adjectives analytic (beautiful-more beautiful-most beautiful)
- **German**: Both synthetic and analytic forms exist

**Challenge**: Predicting which strategy is used for which adjective.

---

## 9. Summary: Implications for Algorithm Development

### 9.1 Source Language Challenges

**Greek**: Morphology is EXPLICIT but semantics are AMBIGUOUS (comparative form may be superlative/elative)
- Algorithm must: Identify morphology (easy) → Determine semantic function (hard)

**Hebrew**: NO morphology; all degree is INFERRED from syntax
- Algorithm must: Parse syntax (hard) → Identify comparative constructions (very hard) → Distinguish from non-degree uses (very hard)

**Asymmetry**: OT and NT require DIFFERENT prediction strategies.

### 9.2 Target Language Diversity

**70% of corpus REQUIRES degree marking** (mandatory morphology or syntax)
- Implication: Even if source is ambiguous, target may FORCE a decision

**30% of corpus allows OPTIONAL degree**
- Implication: Translators may omit degree if context is clear

**Algorithm must**:
1. Identify when degree is NECESSARY (gradable adjective in comparative context)
2. Determine degree TYPE (comparative, superlative, intensified, etc.)
3. Account for target language CONSTRAINTS (mandatory vs. optional marking)

### 9.3 Typological Priorities

**High Priority** (must handle well):
1. Morphological degree (Greek -τερος, Arabic af'al) - EXPLICIT cues
2. Analytic degree (más, plus, 更) - separate words, clearer
3. Periphrastic Hebrew (מִן, construct) - HARDEST, most ambiguous

**Medium Priority**:
4. Intensification (very, sangat, 很) - common but less translation-critical
5. Elatives (absolute superlatives) - theological nuance

**Lower Priority** (rare in corpus):
6. Equatives (as...as) - only 7 instances in TBTA data
7. Inverse comparative/superlative (less/least) - 58 instances combined

---

## 10. Citations

**Primary Sources**:
- {wals-comparative-2025}: WALS Chapter 121 - Comparative Constructions (https://wals.info/chapter/121)
- {bobaljik-universals-2025}: Bobaljik, Jonathan David (2012). *Universals in Comparative Morphology*. MIT Press.
- {equative-typology-2025}: Haspelmath, Martin & Buchholz, Oda (1998). "Equative and similative constructions in the languages of Europe."

**Language-Specific Sources**:
- {greek-nt-grammar}: New Testament Greek grammar resources on comparative/superlative
- {mandarin-grammar-2025}: Chinese Grammar Wiki - Superlative "zui" & Comparative "geng" (https://resources.allsetlearning.com/)
- {arabic-morphology-2025}: Arabic elative (af'al pattern) - "All The Arabic You Never Learned" (https://allthearabicyouneverlearnedthefirsttimearound.com/)
- {austronesian-2025}: Austronesian languages grammatical overview (Britannica)
- {niger-congo-2025}: Niger-Congo typology - degree words postposed to adjectives

**Corpus Data**:
- `/workspace/src/constants/languages.tsv` - 1,009 Bible translation languages

---

**Document Status**: Language Family & Typology Analysis Complete
**Lines**: 575
**Coverage**: 10 language families, 10 proposed database languages, source language analysis complete
**Typological Parameters**: Morphological vs. analytic, comparative construction types, mandatory vs. optional
**Readiness**: Ready for Stage 2 - Translation Database Creation
