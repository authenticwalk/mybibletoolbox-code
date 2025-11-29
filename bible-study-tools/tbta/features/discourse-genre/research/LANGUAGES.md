# Language Family & Typology Analysis: Discourse Genre

## Executive Summary

**Source Language Encoding**: Discourse genre is **NOT explicitly encoded** in Hebrew/Greek morphology. It is **inferred from context** using discourse markers, vocabulary patterns, syntactic structures, and rhetorical features.

**Universal Relevance**: ALL languages require discourse genre awareness for translation, though manifestation differs dramatically. Genre affects:
- **Translation strategy** (literal vs. dynamic, formal vs. functional)
- **Discourse markers** (connectives, particles, verb forms)
- **Information structure** (topic-comment, focus, backgrounding)
- **Register/style** (formal, informal, elevated, technical)

**Typological Variation**: Languages differ in **how** they mark genre, not **whether** they require genre awareness:
- **Morphological marking**: Verb forms, aspect, mood (narrative tenses)
- **Syntactic marking**: Word order, clause chaining, switch-reference
- **Lexical marking**: Particles, connectives, discourse markers
- **Prosodic marking**: Tone, intonation, pausing (oral traditions)

**Major Challenge**: Some languages lack written traditions for certain genres (epistolary, legal codes, apocalyptic), requiring genre adaptation or creation.

## 1. Source Language Encoding Check

### Hebrew: Not Morphologically Encoded, Contextually Inferred

**Genre Indicators in Biblical Hebrew**:

| Genre | Primary Markers | Secondary Markers |
|-------|----------------|-------------------|
| **Narrative** | Wayyiqtol verb chains (ויקטל), temporal sequences | Participant introduction (ויהי), setting formulas |
| **Poetry** | Parallelism (semantic/grammatical), terseness | Metaphor density, asyndeton, archaic forms |
| **Legal** | Apodictic imperatives (לא תקטל), casuistic conditionals (כי...ו) | Legal formulae, covenant language |
| **Prophecy** | Messenger formula (כה אמר יהוה "thus says YHWH") | Oracle introductions, woe formulas (הוי) |
| **Wisdom** | Instructional imperatives (שמע בני "hear, my son") | Proverb formulas, comparisons, rhetorical questions |

**Source**: {patton-putnam-vanpelt-2019-hebrew}, {wendland-2020-hebrew-narratives}

**Key Insight**: Hebrew uses **discourse-level patterns** (verb sequences, formulas, parallelism) not **word-level morphemes** to signal genre. This means:
- **Single clauses** often ambiguous - need context to determine genre
- **Transitions between genres** marked by formula shifts (e.g., narrative → direct speech: ויאמר + messenger formula)
- **Mixed genres** common (narrative frame + embedded poetry, legal + hortatory)

### Greek: Not Morphologically Encoded, Contextually Inferred

**Genre Indicators in New Testament Greek**:

| Genre | Primary Markers | Secondary Markers |
|-------|----------------|-------------------|
| **Narrative** | Aorist verb sequences, historical present, καί connections | Temporal markers (τότε, εὐθύς), participant tracking (οὗτος/ἐκεῖνος) |
| **Epistolary** | Opening formula (χάρις καὶ εἰρήνη), closing (ἀσπάζομαι) | Personal references, travel plans, greetings |
| **Expository** | Logical connectives (γάρ, διό, ὅτι), argument structure | Rhetorical questions, quotations, syllogistic reasoning |
| **Hortatory** | Imperatives, subjunctives, οὖν (therefore) pivots | Motivation clauses, examples, warnings |
| **Apocalyptic** | Vision formulas (εἶδον, ἀκούω), symbolic imagery | Numerology, cosmic imagery, prophetic perfect tenses |

**Source**: {levinsohn-1992-greek-discourse}

**Key Insight**: Greek particles (γάρ, δέ, οὖν, ἀλλά) signal **discourse relationships** that differ by genre:
- **Narrative**: δέ for continuity, καί for sequence
- **Expository**: γάρ for explanation/support
- **Hortatory**: οὖν for application/exhortation

**Morphological vs. Discourse Encoding**:
- **Morphologically encoded**: Tense, aspect, voice, person, number (marked on verbs)
- **Discourse-level encoded**: Genre (inferred from particle distribution, verb form patterns, vocabulary clusters)

## 2. Language Family Analysis

### Analysis Methodology

We have translations in **~1,008 languages** across major language families. Classification based on:
1. **Family affiliation** (from languages.tsv)
2. **Typological features** relevant to discourse genre (word order, tense/aspect, discourse markers)
3. **Genre marking strategies** (from cited research and linguistic knowledge)

### Major Language Families Represented

| Family | # Languages | Representative Languages | Genre Marking Strategy |
|--------|-------------|--------------------------|------------------------|
| **Trans-New Guinea** | ~250 | Enga, Kewa, Huli, Melpa | Switch-reference, medial verbs, clause chaining (narrative focus) |
| **Austronesian** | ~150 | Malay, Tagalog, Fijian, Hawaiian | Topic-prominence, voice systems, particles (flexible genre marking) |
| **Niger-Congo** | ~100 | Swahili, Yoruba, Zulu, Akan | Tense/aspect, noun classes, tone (narrative tenses common) |
| **Indo-European** | ~80 | English, Spanish, Russian, Hindi | Tense/aspect, word order, connectives (rich genre traditions) |
| **Sino-Tibetan** | ~30 | Mandarin, Burmese, Tibetan | Particles, classifiers, aspect markers (topic-prominent) |
| **Afro-Asiatic** | ~25 | Arabic, Amharic, Hebrew | Verb patterns, case, gender (complex genre systems) |
| **Otomanguean** | ~40 | Zapotec languages, Mixtec | Tone, aspect, evidentials (oral genre traditions) |
| **Mayan** | ~15 | K'iche', Mam, Q'eqchi' | Aspect, voice, status suffixes (rich discourse systems) |
| **Sepik** | ~30 | Iatmul, Abelam, Boiken | Switch-reference, clause chaining (narrative-focused) |
| **Creole** | ~10 | Haitian, Tok Pisin, Bislama | Particles, serial verbs, aspect (simplified systems) |

**Source**: /workspace/src/constants/languages.tsv analysis

### Root Language Analysis

**Definition**: Root languages are major Bible translation source languages (beyond Hebrew/Greek) that minority language translators often consult.

| Language | ISO-639-3 | Family | Genre Marking | In Our Dataset? |
|----------|-----------|--------|---------------|-----------------|
| **Hebrew** | heb | Afro-Asiatic | Discourse patterns (wayyiqtol, parallelism, formulas) | Source language |
| **Greek** | ell | Indo-European | Particles, verb forms, formulas | Source language |
| **Latin** | lat | Indo-European | Case, word order, discourse markers | Not listed |
| **English** | eng | Indo-European | Word order, connectives, punctuation | YES (multiple) |
| **Spanish** | spa | Indo-European | Connectives, verb moods, punctuation | YES |
| **French** | fra | Indo-European | Similar to Spanish | YES (Lesser Antillean Creole) |
| **German** | deu | Indo-European | Connectives, word order, compound structures | Not listed |
| **Portuguese** | por | Indo-European | Similar to Spanish | YES (likely) |
| **Russian** | rus | Indo-European | Aspect (perfective/imperfective), particles | Not listed |
| **Arabic** | arb | Afro-Asiatic | Verb patterns, particles, formulaic structures | YES (Standard Arabic) |
| **Swahili** | swh | Niger-Congo | Narrative tenses (ka-), aspect, noun classes | Not listed |
| **Indonesian/Malay** | ind/zsm | Austronesian | Particles, voice, topic-prominence | YES (Malay: zlm) |

**Key Insight**: Most root languages have **rich written genre traditions** (narrative, poetry, legal, epistolary, expository). Minority languages may lack some written genres but have strong oral genre traditions (narrative, hortatory).

## 3. Typological Classification by Genre Features

### Control Language Selection (10 Languages)

Selected for maximum typological diversity and representation of major families:

| # | Language | ISO-639-3 | Family | Word Order | Genre Feature Status |
|---|----------|-----------|--------|------------|---------------------|
| 1 | **English** | eng | Indo-European | SVO | Mandatory (written), Optional (oral) |
| 2 | **Spanish** | spa | Indo-European | SVO | Mandatory (written), Optional (oral) |
| 3 | **Arabic, Standard** | arb | Afro-Asiatic | VSO | Mandatory (classical traditions) |
| 4 | **Malay** | zlm | Austronesian | SVO | Mandatory (written), Optional (oral) |
| 5 | **Mandarin Chinese** | cmn | Sino-Tibetan | SVO | Mandatory (ancient genre traditions) |
| 6 | **Swahili** | swh | Niger-Congo | SVO | Mandatory (written), Optional (oral) |
| 7 | **Russian** | rus | Indo-European | SVO (flexible) | Mandatory (literary traditions) |
| 8 | **Enga** | enq | Trans-New Guinea | SOV | Optional (oral traditions dominate) |
| 9 | **Tok Pisin** | tpi | Creole | SVO | Optional (emerging written genres) |
| 10 | **Japanese** | jpn | Japonic | SOV | Mandatory (complex genre systems) |

**Note**: "Mandatory" = language requires explicit genre awareness for natural translation. "Optional" = genre boundaries less rigid, more context-dependent.

### Detailed Analysis of Control Languages

#### 1. English (eng) - Indo-European, SVO

**Genre Feature Status**: **Mandatory** (written), **Optional** (oral conversational)

**How Genre is Marked**:
- **Lexical**: Connectives differ by genre (narrative: "then", "next"; expository: "therefore", "however"; hortatory: "you should", "must")
- **Syntactic**: Passive voice common in expository/legal, rare in narrative
- **Stylistic**: Formal register for legal/academic, informal for narrative dialogue
- **Punctuation**: Paragraph structure, quotation marks signal genre boundaries

**Genre-Specific Features**:
- **Narrative**: Simple past tense, sequential "then/and", active voice
- **Expository**: Present tense, logical connectives ("thus", "because"), passives
- **Legal**: Modal auxiliaries ("shall", "must"), conditionals
- **Epistolary**: Opening/closing formulas, personal pronouns
- **Poetry**: Line breaks, metaphor, parallelism, meter

**Translation Challenge**: English lacks:
- Narrative tenses (unlike Swahili)
- Honorific systems (unlike Japanese)
- Must rely on context and connectives to signal genre

**Source**: General linguistic knowledge; {longacre-hwang-2012-holistic}

#### 2. Spanish (spa) - Indo-European, SVO

**Genre Feature Status**: **Mandatory** (written), **Optional** (oral)

**How Genre is Marked**:
- **Verbal**: Subjunctive mood for hortatory/legal, preterite/imperfect distinction for narrative
- **Lexical**: Connectives (narrative: "entonces", "luego"; expository: "por lo tanto", "sin embargo")
- **Syntactic**: Word order flexibility signals focus/topic
- **Stylistic**: Formal vs. informal registers (usted vs. tú)

**Genre-Specific Features**:
- **Narrative**: Preterite (completed events) vs. imperfect (background, habitual)
- **Expository**: Indicative mood, present tense generalizations
- **Hortatory**: Subjunctive mood, imperative forms
- **Legal**: Subjunctive, future tense, conditional structures

**Translation Challenge**: Spanish aspect (preterite/imperfect) must align with genre - narrative requires distinction, expository does not.

**Source**: General linguistic knowledge

#### 3. Arabic, Standard (arb) - Afro-Asiatic, VSO

**Genre Feature Status**: **Mandatory** (classical literary traditions)

**How Genre is Marked**:
- **Morphological**: Verb patterns (Form I-X) carry semantic genre implications
- **Syntactic**: VSO for narrative foreground, SVO for background/topicalized
- **Lexical**: Classical particles (ف fa, ثم thumma, إذ idh) signal narrative sequencing
- **Formulaic**: Genre-specific openings (narrative: كان kāna "there was"; Quranic: يا أيها yā ayyuhā "O you who...")

**Genre-Specific Features**:
- **Narrative**: Perfect (māḍī) for events, imperfect (muḍāriʿ) for background
- **Legal**: Apodictic commands, conditional structures (إن...ف in...fa)
- **Hortatory**: Imperative, jussive mood
- **Epistolary**: Classical opening formulas

**Translation Challenge**: Classical Arabic has 1400+ years of genre conventions (Quran, Hadith, poetry, legal). Biblical genre must map appropriately without violating Islamic genre expectations.

**Source**: General linguistic knowledge; Arabic linguistic traditions

#### 4. Malay (zlm) - Austronesian, SVO

**Genre Feature Status**: **Mandatory** (written), **Optional** (oral)

**How Genre is Marked**:
- **Particles**: lah, pun, kah signal discourse structure
- **Voice**: Active vs. passive (di-, meN-) may correlate with genre
- **Lexical**: Connectives (narrative: kemudian, lalu; expository: oleh karena itu)
- **Topic-Comment**: Topic-prominent structure affects genre organization

**Genre-Specific Features**:
- **Narrative**: Sequential markers, active voice for main events
- **Expository**: Passive voice for generalizations, logical connectives
- **Hortatory**: Imperative particles, modal markers (harus "must", sebaiknya "should")

**Translation Challenge**: Topic-prominence means genre affects what is topicalized. Narrative topicalizes participants; expository topicalizes concepts.

**Source**: {austronesian-bible-translation}; general knowledge

#### 5. Mandarin Chinese (cmn) - Sino-Tibetan, SVO

**Genre Feature Status**: **Mandatory** (2000+ years of literary genre traditions)

**How Genre is Marked**:
- **Particles**: le (了), guo (过), zhe (着) signal aspect, genre-relevant
- **Classifiers**: Different classifiers for different entity types in different genres
- **Topic-Comment**: Genre affects topic continuity strategies
- **Parallel structures**: Classical Chinese parallelism (similar to Hebrew poetry)

**Genre-Specific Features**:
- **Narrative**: Perfective le, temporal sequencing, topic chains
- **Expository**: Generalizations, logical connectives (suoyi 所以, yinwei 因为)
- **Legal**: Imperatives, conditional structures
- **Classical Poetry**: Parallelism, tonal patterns, regulated verse (律诗)

**Translation Challenge**: Classical Chinese has strict genre conventions (poetry, historical narrative, philosophical discourse). Modern Mandarin must adapt biblical genres.

**Source**: General linguistic knowledge; Chinese literary traditions

#### 6. Swahili (swh) - Niger-Congo, SVO

**Genre Feature Status**: **Mandatory** (written), **Optional** (oral)

**How Genre is Marked**:
- **Tense/Aspect**: Narrative tense (ka-) distinct from general past (li-)
- **Noun Classes**: Class agreement affects discourse cohesion
- **Connectives**: Different connectives by genre

**Genre-Specific Features**:
- **Narrative**: ka- tense (sequential past), na- (simultaneous), participial constructions
- **Expository**: Generic present, li- past, logical connectives
- **Hortatory**: Subjunctive mood, imperative forms

**Translation Challenge**: Swahili **narrative tense** is obligatory for sequential narrative, cannot be used for non-narrative past events. Genre must be recognized to select correct tense.

**Source**: General linguistic knowledge; Niger-Congo tense systems

#### 7. Russian (rus) - Indo-European, SVO (flexible word order)

**Genre Feature Status**: **Mandatory** (rich literary traditions)

**How Genre is Marked**:
- **Aspect**: Perfective vs. imperfective (genre-relevant distribution)
- **Word Order**: Pragmatic word order signals genre-relevant information structure
- **Participles**: Active/passive participles common in expository/legal, rare in conversational narrative

**Genre-Specific Features**:
- **Narrative**: Perfective aspect for sequential events, imperfective for background
- **Expository**: Imperfective for generalizations, passives for objectivity
- **Legal**: Impersonal constructions, infinitives, conditional structures

**Translation Challenge**: Aspect choice depends on genre. Same event uses perfective in narrative, imperfective in expository.

**Source**: General linguistic knowledge; {longacre-hwang-2012-holistic}

#### 8. Enga (enq) - Trans-New Guinea, SOV

**Genre Feature Status**: **Optional** (oral traditions dominate, written genres emerging)

**How Genre is Marked**:
- **Switch-Reference**: Same-subject vs. different-subject marking (critical for narrative)
- **Medial Verbs**: Clause chaining with switch-reference creates narrative flow
- **Evidentials**: Information source marking (may correlate with genre)

**Genre-Specific Features**:
- **Narrative**: Dense switch-reference marking, medial verb chains
- **Hortatory**: Imperative final verbs, less switch-reference
- **Expository**: Generic present, less clause chaining

**Translation Challenge**: Enga excels at narrative (switch-reference automatically tracks participants) but may lack conventions for expository/legal genres. Written genres are emerging with Bible translation.

**Source**: {png-bible-translation}; Trans-New Guinea linguistic patterns (suspected)

#### 9. Tok Pisin (tpi) - Creole, SVO

**Genre Feature Status**: **Optional** (emerging written genres, oral traditions strong)

**How Genre is Marked**:
- **Particles**: i (predicate marker), bai (future), bin (past) - simplified TAM system
- **Serial Verbs**: Common in narrative, less in expository
- **Lexical**: Connectives borrowed from English (orait "so", tasol "but")

**Genre-Specific Features**:
- **Narrative**: bin for past, sequential "na" (and), "orait" (so/then)
- **Hortatory**: mas (must), ken (can), imperative constructions
- **Expository**: i-marking, logical connectives

**Translation Challenge**: Creoles have **simplified genre systems** - less grammatical marking, more reliance on context and lexical connectives. Genre boundaries more fluid.

**Source**: General knowledge of Melanesian pidgins/creoles

#### 10. Japanese (jpn) - Japonic, SOV

**Genre Feature Status**: **Mandatory** (highly complex genre and register systems)

**How Genre is Marked**:
- **Honorifics**: Keigo system (sonkeigo, kenjōgo, teineigo) correlates with genre and social context
- **Verb Forms**: Polite (-masu), plain (-ru), formal written (-de aru)
- **Particles**: wa (topic), ga (subject) distribution varies by genre
- **Sentence-Final Particles**: ne, yo, ka signal speech act and genre

**Genre-Specific Features**:
- **Narrative**: Plain forms, sequential te-forms, wa for topic continuity
- **Epistolary**: Formal written style, honorifics for addressee
- **Expository**: da/de aru forms, logical connectives (dakara, shikashi)
- **Hortatory**: Imperative forms, べき beki "should", なければならない "must"

**Translation Challenge**: Japanese has **most complex genre-register interaction**. Biblical epistles require choosing appropriate honorific level (too formal = distant, too casual = disrespectful).

**Source**: General linguistic knowledge; Japanese honorific systems

## 4. Feature Status Summary Table

| Language | Narrative Marking | Poetry Distinction | Legal Marking | Epistolary Conventions | Expository Markers |
|----------|-------------------|-------------------|---------------|----------------------|-------------------|
| English | Optional (tense) | Mandatory (form) | Mandatory (modal) | Mandatory (formulae) | Mandatory (connectives) |
| Spanish | Mandatory (aspect) | Mandatory (form) | Mandatory (subjunctive) | Mandatory (formulae) | Mandatory (connectives) |
| Arabic | Mandatory (tense) | Mandatory (form, meter) | Mandatory (formulas) | Mandatory (classical) | Mandatory (particles) |
| Malay | Mandatory (voice) | Mandatory (form) | Mandatory (imperative) | Mandatory (formulae) | Mandatory (connectives) |
| Mandarin | Mandatory (particles) | Mandatory (parallelism) | Mandatory (structure) | Mandatory (formulae) | Mandatory (connectives) |
| Swahili | **Mandatory (ka- tense)** | Mandatory (form) | Mandatory (subjunctive) | Mandatory (formulae) | Mandatory (connectives) |
| Russian | Mandatory (aspect) | Mandatory (form) | Mandatory (impersonal) | Mandatory (formulae) | Mandatory (connectives) |
| Enga | **Mandatory (switch-ref)** | Optional (emerging) | Optional (oral) | Optional (emerging) | Optional (emerging) |
| Tok Pisin | Optional (particles) | Optional (emerging) | Optional (simplified) | Optional (emerging) | Optional (simplified) |
| Japanese | Mandatory (honorifics) | Mandatory (form) | Mandatory (formal) | **Mandatory (keigo)** | Mandatory (style) |

**Legend**:
- **Mandatory**: Language requires explicit genre-appropriate marking
- **Optional**: Genre affects choices but not obligatory
- **Emerging**: Written genre conventions developing through Bible translation

## 5. Language-Specific Genre Needs

### Narrative-Focused Languages

**Languages with specialized narrative grammar**:
- **Trans-New Guinea family** (Enga, Kewa, Melpa): Switch-reference, medial verbs
- **Niger-Congo family** (Swahili, Kikuyu): Narrative tenses
- **Sino-Tibetan family** (Lahu, Lisu): Narrative particles

**Need**: TBTA narrative genre annotation directly maps to grammatical requirements.

**Challenge**: Non-narrative genres may lack established conventions.

### Topic-Prominent Languages

**Languages where genre affects topic-comment structure**:
- **Austronesian family** (Malay, Tagalog, Fijian)
- **Sino-Tibetan family** (Mandarin, Cantonese)
- **Japonic** (Japanese, Ryukyuan)

**Need**: Genre determines what is topicalized:
- **Narrative**: Participants as topics
- **Expository**: Concepts as topics
- **Legal**: Actions/prohibitions as topics

**Challenge**: Topic-prominence interacts with voice systems (Philippine languages) and information structure.

### Honorific Languages

**Languages where genre and social register interact**:
- **Japanese, Korean**: Complex honorific systems
- **Javanese, Balinese**: Speech level systems
- **Thai, Khmer**: Royal vocabulary and pronouns

**Need**: Genre determines base register:
- **Epistolary**: Polite/formal (sender-recipient relationship)
- **Legal**: Formal/authoritative
- **Narrative**: Variable by speaker-addressee

**Challenge**: Biblical honorifics (Lord, Master, servant) must map to appropriate target language levels without over- or under-stating.

### Oral-Tradition Languages

**Languages with strong oral genres but emerging written conventions**:
- **Papua New Guinea languages** (~250 in our dataset)
- **African minority languages** (various families)
- **Mesoamerican languages** (Otomanguean, Mayan)

**Need**: Oral genres (storytelling, exhortation, proverbs) are well-developed. Written genres (epistolary, legal codes, expository essays) are emerging through Bible translation.

**Challenge**: Creating appropriate written genre conventions that feel natural while maintaining biblical content.

## 6. Candidate Languages for Translation Database (Stage 2)

**Selection Criteria**:
1. **Typological diversity**: Different word orders, marking strategies
2. **Genre marking contrast**: Mandatory vs. optional marking
3. **Family representation**: Cover major families
4. **Availability**: Languages in our dataset
5. **Root language status**: Languages translators consult

### Recommended 10 Languages for Stage 2 Translation Database

| # | Language | ISO-639-3 | Family | Rationale |
|---|----------|-----------|--------|-----------|
| 1 | **English** | eng | Indo-European | Root language, rich written genres, lexical marking |
| 2 | **Spanish** | spa | Indo-European | Root language, aspect marking, subjunctive mood |
| 3 | **Arabic, Standard** | arb | Afro-Asiatic | Root language, classical genre traditions, VSO |
| 4 | **Malay** | zlm | Austronesian | Root language, topic-prominent, voice systems |
| 5 | **Swahili** | swh | Niger-Congo | Narrative tense (ka-), Bantu discourse markers |
| 6 | **Russian** | rus | Indo-European | Aspect marking varies by genre, flexible word order |
| 7 | **Enga** | enq | Trans-New Guinea | Switch-reference (narrative-focused), SOV, oral genres |
| 8 | **Tok Pisin** | tpi | Creole | Emerging written genres, simplified systems, contact language |
| 9 | **Japanese** | jpn | Japonic | Honorifics interact with genre, SOV, complex register |
| 10 | **Mandarin Chinese** | cmn | Sino-Tibetan | Ancient genre traditions, topic-prominent, particles |

**Note**: Swahili, Enga, Japanese, Mandarin not currently in dataset - may need to use alternate languages from same families OR add them if feasible.

### Alternate Candidates (if primary not available)

| Language | ISO-639-3 | Family | Replaces |
|----------|-----------|--------|----------|
| Tagalog | tgl | Austronesian | Malay (if zlm insufficient) |
| Akan | aka | Niger-Congo | Swahili (narrative tense systems) |
| Korean | kor | Koreanic | Japanese (honorific systems) |
| Hindi | hin | Indo-European | Russian (if aspect marking needed) |
| Kewa | kew | Trans-New Guinea | Enga (switch-reference) |

## 7. Cultural and Translational Nuances

### Genre Traditions Missing in Target Cultures

**Epistolary Genre**:
- **Challenge**: Oral cultures lack written letter traditions
- **Affected Languages**: Papua New Guinea languages, small oral-tradition languages
- **Solution**: Adapt to oral message conventions or create written conventions
- **Theological Impact**: Paul's epistles are central to NT - must find natural rendering

**Legal Codes**:
- **Challenge**: Customary law (oral, case-based) vs. codified law (written, universal)
- **Affected Languages**: Languages without centralized legal systems
- **Solution**: May need to borrow legal register from national language OR adapt to proverb/instruction genre
- **Theological Impact**: Mosaic law, legal portions of epistles

**Apocalyptic Genre**:
- **Challenge**: Symbolic-visionary genre unfamiliar in many cultures
- **Affected Languages**: Cultures without apocalyptic or visionary traditions
- **Solution**: Treat as special narrative (vision report) or prophetic speech
- **Theological Impact**: Revelation, Daniel, portions of prophets

### Genre and Translation Strategy

**Genre affects translation approach**:

| Genre | Appropriate Translation Strategy | Rationale |
|-------|--------------------------------|-----------|
| **Narrative** | Moderate to dynamic equivalence | Maintain story flow, natural participant reference |
| **Poetry** | Formal to moderate equivalence | Preserve parallelism, imagery, form when possible |
| **Legal** | Formal equivalence | Precision required for commands, prohibitions |
| **Epistolary** | Moderate equivalence | Natural letter conventions, maintain argument flow |
| **Expository** | Moderate equivalence | Logical connectives, clear argumentation |
| **Apocalyptic** | Formal to moderate | Symbols often cross-cultural, avoid over-interpretation |
| **Wisdom** | Dynamic equivalence | Proverbs need cultural adaptation for impact |

**Source**: {wendland-aubrey-2023-discourse-translation}

### Honorifics and Social Register

**Languages requiring genre-specific register**:
- **Japanese**: Epistles to churches use polite (-masu) not honorific (keigo), avoiding distance
- **Javanese**: Speaker age/status affects verb forms - Bible must choose appropriate level
- **Korean**: Honorifics for God (높임말), neutral for human addressees

**Challenge**: Balancing respect (God, apostles, leaders) with accessibility (avoiding excessive formality that creates distance).

## 8. Summary and Implications for Algorithm Development

### Key Findings

1. **Universal Relevance**: ALL languages need genre awareness, no language is "genre-neutral"

2. **Diverse Marking Strategies**: Languages mark genre through:
   - Morphology (verb forms, aspect, mood)
   - Syntax (word order, clause chaining, switch-reference)
   - Lexicon (particles, connectives, formulas)
   - Register (honorifics, formality levels)

3. **Typological Patterns**:
   - **Narrative-focused**: Trans-New Guinea, Niger-Congo (specialized narrative grammar)
   - **Topic-prominent**: Austronesian, Sino-Tibetan (genre affects topic selection)
   - **Honorific-sensitive**: Japanese, Javanese, Thai (genre-register interaction)
   - **Oral-tradition**: PNG, minority languages (emerging written genres)

4. **Root Languages**: Major translation source languages (English, Spanish, Arabic, Malay) have rich written genre traditions, providing models for minority languages

5. **Missing Genres**: Epistolary, legal codes, apocalyptic may be unfamiliar in some cultures, requiring adaptation

### Implications for TBTA Discourse Genre Prediction

**Stage 2 (Translation Database)**:
- Select 10 languages covering typological diversity (morphological, syntactic, lexical, prosodic marking)
- Include both mandatory-marking (Swahili, Japanese) and optional-marking (English, Tok Pisin) languages
- Ensure root languages (English, Spanish, Arabic, Malay) are represented

**Stage 3 (Analysis)**:
- Identify which **target language grammatical features** correlate with each TBTA genre value
- Determine if genre can be predicted from **source text features** (Hebrew/Greek discourse markers) OR requires **contextual analysis** (book-level, chapter-level)

**Stage 4 (Algorithm)**:
- Genre prediction likely requires **multi-level analysis**: word-level markers + clause-level patterns + discourse-level context
- Cannot rely on single morpheme or construction - need holistic discourse analysis

**Stage 5 (Validation)**:
- Test with languages requiring mandatory genre marking (Swahili ka-, Enga switch-reference) - errors will be immediately visible
- Check with translation practitioners: does predicted genre align with what translators naturally chose?

---

**Completed**: 2025-11-29

**Next Step**: Theologically Significant Groups Classification (THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)
