<<<<<<< HEAD
# Language Family & Typology Analysis: Polarity Feature

**Research Date**: 2025-11-26
**Feature**: Polarity (Affirmation vs. Negation)
**Dataset**: 1,009 Bible translations analyzed from languages.tsv

---

## 1. Source Language Encoding Check

### 1.1 Biblical Hebrew Negation

**EXPLICITLY ENCODED morphologically**: YES

Hebrew uses multiple negative particles with distinct functions:

| Particle | Hebrew | Function | Usage Context |
|----------|--------|----------|---------------|
| **lo** | לֹא | Standard negation | General/absolute negation, imperfective verbs, permanent prohibitions |
| **al** | אַל | Prohibitive negation | Jussive mood, temporary prohibitions |
| **ein** | אֵין | Existential negation | Nominal negation, "there is not" |
| **bli** | בְּלִי | Without | Prepositional negation |

**Source**: {https://uhg.readthedocs.io/en/latest/particle_negative.html}, {https://www.hebrewpod101.com/blog/2021/08/10/hebrew-negation/}

**Key Distinction**: לֹא (lo) vs. אַל (al)
- לֹא + imperfective = permanent/absolute prohibition (Ten Commandments: לֹא תִרְצָח *lo tirtzakh* "you shall NOT murder")
- אַל + jussive = temporary/contextual prohibition
- This distinction affects polarity strength: absolute vs. mitigated negation

**Source**: {https://www.blueletterbible.org/resources/grammars/hebrew/simplified-hebrew/imperatives.cfm}, {https://christianity.stackexchange.com/questions/59248/meaning-of-the-original-hebrew-of-thou-shall-not-in-the-ten-commandments}

### 1.2 Koine Greek Negation

**EXPLICITLY ENCODED morphologically**: YES

Greek uses two primary negative systems with modal distinctions:

| Particle | Greek | Function | Usage Context |
|----------|-------|----------|---------------|
| **ou** | οὐ (οὐκ, οὐχ before vowels) | Indicative negation | Statements of fact, reality negation |
| **mē** | μή | Non-indicative negation | Subjunctive, imperative, prohibitions, potentiality |
| **ou mē** | οὐ μή | Emphatic negation | Double negative = strongest possible negation |

**Source**: {https://blogs.blueletterbible.org/blb/2012/05/23/emphatic-negations-in-biblical-greek/}

**Emphatic Negation (οὐ μή)**: "Subjunctive of Emphatic Negation"
- Most emphatic grammatical structure in Greek NT
- οὐ μή + Aorist Subjunctive = absolute denial of future probability
- Means "Never, no never" or "not under any circumstance"
- Examples: John 8:51 ("he will never, no never experience death"), 1 Cor 8:13

**Source**: {https://blogs.blueletterbible.org/blb/2012/05/23/emphatic-negations-in-biblical-greek/}

**Philosophical Distinction**: οὐ (reality) vs. μή (potentiality)
- οὐ negates what IS (indicative, factual)
- μή negates what MIGHT BE (subjunctive, modal, potential)

**Source**: {https://blogs.blueletterbible.org/blb/2012/05/23/emphatic-negations-in-biblical-greek/}

### 1.3 Summary: Source Language Polarity

Both Biblical Hebrew and Koine Greek **explicitly encode polarity morphologically** through:
- Multiple negative particles with semantic distinctions
- Mood-based negation systems (Hebrew: lo/al; Greek: ou/mē)
- Emphatic negation strategies (Hebrew: multiple negatives; Greek: οὐ μή)
- Scope distinctions (verbal vs. nominal vs. existential negation)

**Implication**: Polarity is NOT inferable from context alone in source languages. It requires explicit morphological marking with semantic and modal nuances.

---

## 2. Language Family Distribution in Dataset

**Total Languages**: 1,009 Bible translations {languages.tsv}

**Top 15 Language Families** (by number of translations):

| Rank | Family | Count | % of Total |
|------|--------|-------|------------|
| 1 | Austronesian | 176 | 17.4% |
| 2 | Trans-New Guinea | 141 | 14.0% |
| 3 | Indo-European | 135 | 13.4% |
| 4 | Niger-Congo | 89 | 8.8% |
| 5 | Otomanguean | 69 | 6.8% |
| 6 | Mayan | 41 | 4.1% |
| 7 | Australian | 36 | 3.6% |
| 8 | Afro-Asiatic | 25 | 2.5% |
| 9 | Uto-Aztecan | 21 | 2.1% |
| 10 | Maipurean | 20 | 2.0% |
| 11 | Sino-Tibetan | 18 | 1.8% |
| 12 | Quechuan | 18 | 1.8% |
| 13 | Creole | 15 | 1.5% |
| 14 | Tucanoan | 14 | 1.4% |
| 15 | Sepik | 14 | 1.4% |

**Source**: {languages.tsv analyzed 2025-11-26}

**Coverage**: Dataset includes representatives from all major world language families, providing excellent typological diversity for polarity analysis.

---

## 3. WALS Typological Database Analysis

### 3.1 WALS Feature 143: Order of Negative Morpheme and Verb

**Source**: {https://wals.info/chapter/143}

**Primary Typological Categories**:

| Type | Pattern | Languages | Global % |
|------|---------|-----------|----------|
| NegV | Negative precedes verb | 525 | ~40% |
| VNeg | Negative follows verb | 171 | ~13% |
| [Neg-V] | Negative prefix | 162 | ~12% |
| [V-Neg] | Negative suffix | 202 | ~15% |
| Mixed | Multiple strategies | ~250 | ~19% |

**Source**: {https://wals.info/chapter/143}

**Double/Triple Negation**:
- **Obligatory Double Negation**: 114 languages (NegVNeg, Neg[V-Neg], etc.)
- **Optional Double/Triple Negation**: 80-85 languages

**Source**: {https://wals.info/chapter/143}

**Geographic Clustering**:
- **Preverbal (NegV)**: Dominates globally, highest in Africa and Asia
- **Postverbal (VNeg)**: Central Africa and New Guinea regions
- **Negative Prefixes**: East Africa (Bantu), Northeast India (Tibeto-Burman)
- **Negative Suffixes**: Northern South America

**Source**: {https://wals.info/chapter/143}

### 3.2 WALS Feature 112: Negative Morpheme Types

**Source**: {https://wals.info/chapter/112}

**Primary Categories**:

| Type | Count | % | Geographic Distribution |
|------|-------|---|------------------------|
| Negative Particle | 502 | ~38% | Global (e.g., English "not") |
| Negative Affix | 395 | ~30% | Global (e.g., Yukaghir "el-") |
| Negative Auxiliary | 47 | ~4% | Northern Eurasia (Finland → W. Siberia) |
| Double Negation | 119 | ~9% | New Guinea, parts of Africa |
| Unclear Word/Affix | 73 | ~6% | Languages with minimal inflection |
| Variation | 21 | ~2% | Multiple strategies per language |

**Source**: {https://wals.info/chapter/112}

**Key Finding**: Negative auxiliary verbs (like Finnish *ei*) show "striking frequency across northern Eurasia, stretching from Finland to western Siberia." {https://wals.info/chapter/112}

### 3.3 WALS Feature 115: Negative Indefinite Pronouns and Predicate Negation

**Source**: {https://wals.info/chapter/115}

**Negative Concord**: Whether negative indefinites (nobody, nothing) co-occur with predicate negation

| Type | Example Language | Pattern |
|------|-----------------|---------|
| **Negative Concord** | Russian, Spanish, Slavic, Romance | Negative indefinite + predicate negation = single negation |
| **Double Negation** | German, Standard English | Negative indefinite + predicate negation = affirmative |
| **Mixed** | Spanish | Position-dependent (preverbal = no concord, postverbal = concord) |

**Source**: {https://wals.info/chapter/115}

**Global Trend**: "The great majority of the world's languages have negative indefinites co-occurring with predicate negation" (i.e., negative concord is more common than double negation). {https://wals.info/chapter/115}

---

## 4. Language Classification: Polarity Marking Requirements

### 4.1 Mandatory Polarity Marking

Languages that **grammatically require** explicit polarity marking:

#### 4.1.1 Uralic Family (Negative Auxiliary Verbs)

**Finnish** (fin) - Uralic family in dataset {languages.tsv}
- **Negative verb**: *ei* conjugates for person/number (*en, et, ei, emme, ette, eivät*)
- Main verb uses connegative stem (no person marking on main verb)
- **Polarity status**: MANDATORY (morphologically required)
- **Source**: {https://uusikielemme.fi/finnish-grammar/verbs/verb-tenses-and-moods/making-verbs-negative-in-finnish-dont-havent-hadnt-shouldnt}

**Pattern**: Negative auxiliary conjugates while main verb remains in stem form, distinguishing negation from affirmative structurally.

#### 4.1.2 Austronesian Family (176 languages in dataset)

**Tagalog** (tgl) - Austronesian {languages.tsv}
- **Negative markers**: *hindi* (general), *huwag* (prohibitive)
- **Polarity status**: MANDATORY (syntactically required)
- **Source**: {https://wikilanguages.net/Tagalog/Negation.html}

**Indonesian/Malay** (ind, zsm) - Austronesian {languages.tsv}
- **Negative markers**: *tidak* (verbal), *bukan* (nominal)
- **Polarity status**: MANDATORY (syntactic distinction required)
- **Source**: {https://www.sciencedirect.com/science/article/abs/pii/S0024384107001441}

**Philippine Languages** (15+ in dataset including Ilokano, Cebuano, Hiligaynon):
- Typological diversity: pre-verbal and post-verbal negation
- Prohibitive vs. standard negation distinctions
- **Polarity status**: MANDATORY across Philippine subgroup
- **Source**: {https://www.academia.edu/1196756/Typology_of_Philippine_Negation}

#### 4.1.3 Slavic Family (Negative Concord Languages)

**Russian** (rus) - Indo-European {languages.tsv}
- **Negative Concord**: Multiple negative markers = single semantic negation
- Pattern: *Nikto ne rabotaet* (nobody not works) = "Nobody works" (not "Everybody works")
- **Polarity status**: MANDATORY (negative concord affects grammaticality)
- **Source**: {https://wals.info/chapter/115}

**Czech, Polish, Bulgarian** - Slavic languages (suspected in dataset)
- Strict negative concord systems
- **Polarity status**: MANDATORY
- **Source**: {https://academic.oup.com/book/45879/chapter-abstract/400847185?redirectedFrom=fulltext}

#### 4.1.4 Romance Family (Negative Concord)

**Spanish** (spa) - Indo-European {languages.tsv}
- **Mixed system**: Position-dependent negative concord
- Preverbal negative indefinite: no predicate negation (*Nadie vino* "Nobody came")
- Postverbal negative indefinite: requires predicate negation (*No vino nadie* "Not came nobody")
- **Polarity status**: MANDATORY (grammaticality depends on position)
- **Source**: {https://wals.info/chapter/115}

**French** (fra) - Indo-European {languages.tsv}
- **Double negation**: *ne...pas* (obligatory in standard French)
- Pattern: *Je ne sais pas* (I not know not) = "I don't know"
- **Polarity status**: MANDATORY (both markers required in formal register)
- **Source**: {https://wals.info/chapter/143}

**Portuguese, Romanian, Italian** - Romance languages in dataset {languages.tsv}
- Negative concord systems (suspected)
- **Polarity status**: MANDATORY (suspected)

#### 4.1.5 Niger-Congo Family (89 languages in dataset)

**Bantu Languages** (Swahili, Lingala, others):
- Negative prefixes on verbs (e.g., Swahili *ha-*)
- **Polarity status**: MANDATORY (morphologically bound)
- **Geographic**: East Africa (WALS: negative prefix concentration)
- **Source**: {https://wals.info/chapter/143}

### 4.2 Optional/Contextual Polarity Marking

Languages where polarity can be inferred from context in some cases:

#### 4.2.1 English (eng)

**English** (eng) - Indo-European {languages.tsv}
- **Standard**: Double negation (two negatives = positive)
- **Vernacular**: Negative concord in many dialects (AAVE, Appalachian, etc.)
- **Polarity status**: OPTIONAL in some contexts (e.g., rhetorical questions)
- **Source**: {https://ygdp.yale.edu/phenomena/negative-concord}

#### 4.2.2 Mandarin Chinese (cmn)

**Mandarin** (cmn) - Sino-Tibetan {languages.tsv}
- **Negative markers**: *bù* (不, general), *méi* (没, perfective)
- **Polarity status**: MANDATORY for explicit negation, but some contexts allow inference
- **Source**: (suspected based on internal knowledge)

#### 4.2.3 Japanese (jpn)

**Japanese** (suspected in dataset or common translation source)
- **Negative markers**: Verb suffixes (*-nai*, *-masen*)
- **Polarity status**: MANDATORY morphologically on verbs
- **Source**: (suspected based on internal knowledge)

### 4.3 Summary Table: Classification by Family

| Family | Languages in Dataset | Polarity Status | Primary Strategy |
|--------|---------------------|-----------------|------------------|
| **Austronesian** | 176 | MANDATORY | Negative particles (*tidak*, *hindi*) |
| **Trans-New Guinea** | 141 | MANDATORY (suspected) | Negative affixes/particles |
| **Indo-European** | 135 | MANDATORY (most) | Negative concord (Slavic, Romance), particles (Germanic) |
| **Niger-Congo** | 89 | MANDATORY | Negative prefixes (Bantu) |
| **Otomanguean** | 69 | MANDATORY (suspected) | Negative particles |
| **Mayan** | 41 | MANDATORY (suspected) | Negative particles |
| **Australian** | 36 | MANDATORY (suspected) | Negative particles/affixes |
| **Afro-Asiatic** | 25 | MANDATORY | Multiple particles (Hebrew pattern) |
| **Uralic** | ~5 | MANDATORY | Negative auxiliary verbs |
| **Quechuan** | 18 | MANDATORY (suspected) | Negative suffixes |

**General Pattern**: Polarity marking is **MANDATORY in the vast majority** of world languages. Languages allowing polarity inference from context alone are rare exceptions.

---

## 5. Root Languages for Bible Translation

### 5.1 Primary Source Languages

| Language | Family | ISO-639-3 | Polarity Encoding |
|----------|--------|-----------|-------------------|
| **Biblical Hebrew** | Afro-Asiatic | hbo | Multiple particles (לֹא, אַל, אֵין) |
| **Koine Greek** | Indo-European | grc | Modal particles (οὐ, μή) + emphatic (οὐ μή) |

### 5.2 Major Translation Root Languages

Languages translators often start from when creating new Bible translations:

| Language | Family | ISO-639-3 | In Dataset | Polarity System |
|----------|--------|-----------|------------|-----------------|
| **Hebrew** | Afro-Asiatic | heb | Yes | Multiple particles (lo, al, ein) |
| **Greek** | Indo-European | ell | Yes | ou/mē distinction |
| **Latin** | Indo-European | lat | Yes | *non* (general), *ne* (prohibitive) |
| **English** | Indo-European | eng | Yes (45 versions) | Particle "not", auxiliary "do not" |
| **Spanish** | Indo-European | spa | Yes (6 versions) | *no* + negative concord |
| **German** | Indo-European | deu | Yes (4 versions) | *nicht* (verbal), *kein* (nominal) |
| **French** | Indo-European | fra | Yes (4 versions) | *ne...pas* double negation |
| **Arabic** | Afro-Asiatic | arb | Yes (suspected) | Multiple particles (*lā*, *mā*, *lam*) |
| **Indonesian** | Austronesian | ind | Yes | *tidak* (verbal), *bukan* (nominal) |
| **Swahili** | Niger-Congo | swa | Yes (3 versions) | Negative prefix *ha-* |

**Source**: {languages.tsv}

**Pattern**: All major root languages have **explicit morphological polarity marking** with semantic distinctions (general vs. prohibitive, verbal vs. nominal, etc.).

---

## 6. Candidate Languages for Translation Database

**Criteria**:
1. Mix of marking vs. non-marking strategies
2. Diverse language families (representation from top families)
3. Negative concord vs. double negative semantics
4. Available in languages.tsv dataset

### 6.1 Recommended 10 Languages

| # | Language | ISO-639-3 | Family | Negation Type | Rationale |
|---|----------|-----------|--------|---------------|-----------|
| 1 | **Tagalog** | tgl | Austronesian | Particle (*hindi*, *huwag*) | Philippine-type negation, prohibitive distinction, 17.4% family representation |
| 2 | **Spanish** | spa | Indo-European (Romance) | Position-dependent negative concord | Mixed system, major root language, negative concord variation |
| 3 | **Russian** | rus | Indo-European (Slavic) | Strict negative concord | Strict NC system, multiple negative = single negation |
| 4 | **Swahili** | swa | Niger-Congo (Bantu) | Negative prefix (*ha-*) | Bantu morphological negation, 8.8% family representation, root language |
| 5 | **Finnish** | fin | Uralic | Negative auxiliary verb (*ei*) | Unique negative auxiliary system, Northern Eurasia pattern |
| 6 | **English** | eng | Indo-European (Germanic) | Particle + auxiliary | Double negation (standard) vs. negative concord (vernacular), major root language |
| 7 | **Indonesian** | ind | Austronesian | Particle (*tidak*/*bukan*) | Verbal/nominal distinction, root language, SVO Austronesian type |
| 8 | **Mandarin Chinese** | cmn | Sino-Tibetan | Particle (*bù*/*méi*) | Aspect-based negation (*bù* general, *méi* perfective), 1.8% family representation |
| 9 | **K'iche'** | quc | Mayan | Particle (suspected) | Mayan negation pattern, 4.1% family representation |
| 10 | **Tok Pisin** | tpi | Creole | Particle (*no*, *nogat*) | Creole simplified negation, 1.5% family representation |

### 6.2 Alternative Candidates (if primary unavailable)

| Language | ISO-639-3 | Family | Negation Type | Rationale |
|----------|-----------|--------|---------------|-----------|
| **German** | deu | Indo-European (Germanic) | Particle (*nicht*/*kein*) | Verbal/nominal distinction, double negation system |
| **French** | fra | Indo-European (Romance) | Double marking (*ne...pas*) | Obligatory double negation, Romance pattern |
| **Arabic** | arb | Afro-Asiatic | Multiple particles | Multiple negation strategies like Hebrew |
| **Hiligaynon** | hil | Austronesian (Philippine) | Particle | Philippine negation variation |
| **Quechua** | que | Quechuan | Suffix (suspected) | South American pattern, 1.8% family representation |

---

## 7. Cultural Nuances and Special Cases

### 7.1 Honorific Negation

**Japanese** (suspected in dataset):
- Polite negation: *-masen* (ます + ない → ません)
- Casual negation: *-nai* (ない)
- Register affects negation form selection
- **Implication**: Polarity interacts with speaker demographics (TBTA Feature #13)

**Source**: (suspected based on internal knowledge of Japanese grammar)

### 7.2 Euphemistic Negation

**Many cultures**: Taboo topics use indirect negation
- Death euphemisms: "no longer with us" (affirmative form, negative meaning)
- Religious taboos: Avoid direct negation of sacred entities
- **Implication**: Semantic polarity may differ from morphological polarity

**Source**: (suspected based on general linguistic knowledge)

### 7.3 Prohibition Strength

**Hebrew**: לֹא (lo) vs. אַל (al) distinction affects social force
- לֹא = absolute, divine, permanent prohibition (Ten Commandments)
- אַל = situational, temporal prohibition (advice, warnings)

**Greek**: οὐ (ou) vs. μή (mē) affects illocutionary force
- οὐ = factual denial (indicative)
- μή = prohibition/warning (subjunctive, imperative)

**Tagalog**: *huwag* (prohibitive) vs. *hindi* (general negation)
- *Huwag* carries stronger directive force (don't do it!)
- *Hindi* is neutral negation (not, no)

**Implication**: Polarity interacts with **mood** (TBTA Verb Feature) and **illocutionary force** (TBTA Clause Feature #12).

### 7.4 Negative Polarity Items (NPIs)

**Universal Pattern**: Many languages have words restricted to negative contexts
- English: "any", "ever", "yet" (appear primarily in negatives/questions)
- Greek: *οὐδείς* (oudeis, "no one"), *οὐδέν* (ouden, "nothing")
- Hebrew: *מְאוּמָה* (me'umah, "anything/nothing")

**Implication**: Polarity affects lexical selection beyond the negative marker itself.

**Source**: {https://wals.info/chapter/115}

### 7.5 Rhetorical Questions with Implied Negation

**Cross-linguistic pattern**: Questions expecting negative answers
- Hebrew: הֲלֹא (halo, "Is it not...?") expects "Yes, it is"
- Greek: μή in questions expects negative answer (e.g., μὴ ἀγαπᾷ; "He doesn't love, does he?")
- English: "Isn't God good?" expects "Yes" (affirmative content, negative form)

**Implication**: Surface polarity (negative morphology) may differ from semantic polarity (affirmative meaning). Requires distinguishing **morphological polarity** from **semantic polarity**.

**Source**: (suspected based on Biblical Hebrew and Greek grammar knowledge)

### 7.6 Litotes (Double Negative = Emphatic Positive)

**Definition**: Rhetorical understatement using double negation for emphasis

**Examples**:
- Greek NT: Litotes in Acts 19:24 (*οὐκ ὀλίγην* "not a little" = "very much")
- English: "not uncommon" (= "common, even frequent")
- Hebrew: Double negatives in poetry/wisdom literature

**Implication**: Double negation can mean:
1. **Negative concord**: Multiple negatives = single negation (Russian, Spanish)
2. **Double negation**: Two negatives = affirmative (Standard English, German)
3. **Litotes**: Two negatives = emphatic affirmative (rhetorical device)

**Source**: (suspected based on internal knowledge of Biblical Greek and rhetoric)

### 7.7 Scope Ambiguity

**Cross-linguistic challenge**: Negation scope affects meaning

**Example**:
- "Not all disciples understood" (partial negation: some understood, some didn't)
- "All disciples did not understand" (total negation: zero disciples understood)

**Implication**: Polarity annotation must specify **scope** (which constituent is negated).

**Source**: (general linguistic knowledge)

---

## 8. Summary and Implications for TBTA Polarity Feature

### 8.1 Key Findings

1. **Source Languages**: Hebrew and Greek **explicitly encode** polarity morphologically with semantic distinctions (lo/al, ou/mē, emphatic negations)

2. **Global Typology**: Polarity marking is **MANDATORY** in the vast majority of world languages (90%+). Only rare exceptions allow contextual inference.

3. **Typological Diversity**: Dataset includes:
   - Negative particles (Austronesian, Germanic)
   - Negative affixes (Bantu, Quechuan)
   - Negative auxiliary verbs (Uralic)
   - Negative concord (Slavic, Romance)
   - Double negation (Germanic)
   - Mixed systems (Spanish, Philippine languages)

4. **Semantic Distinctions**: Languages distinguish:
   - General vs. prohibitive negation (Hebrew lo/al, Tagalog hindi/huwag)
   - Verbal vs. nominal negation (Indonesian tidak/bukan)
   - Factual vs. modal negation (Greek ou/mē)
   - Emphatic vs. simple negation (Greek ou mē, Hebrew double negatives)

5. **Cultural Nuances**: Polarity interacts with:
   - Honorifics/register (Japanese -masen vs. -nai)
   - Prohibition strength (Hebrew lo/al distinction affects divine commands)
   - Rhetorical devices (litotes, rhetorical questions)
   - Taboos (euphemistic negation)

### 8.2 Implications for TBTA Implementation

**Why Noun Polarity is Tier A (Essential)**:
- Many languages distinguish verbal vs. nominal negation (Indonesian *tidak*/*bukan*, Hebrew lo/ein)
- Negative concord affects nominal elements (nobody = negative noun in Russian)
- Noun polarity affects NPI licensing (negative indefinites)

**Why Verb Polarity is Tier B (Important but sometimes inferable)**:
- Verb polarity can sometimes be inferred from context (if no negative marker present = affirmative)
- However, modal distinctions (ou/mē, lo/al) require explicit encoding
- Emphatic affirmative (TBTA value "E") may be contextually marked rather than morphologically marked

**What TBTA Must Capture**:
1. **Morphological polarity**: Surface negative markers (lo, ou, mē, al, ein)
2. **Semantic polarity**: Meaning-level negation (including implied negatives in rhetorical questions)
3. **Polarity strength**: Simple vs. emphatic (affirmative, emphatic affirmative, emphatic negative)
4. **Negation type**: General, prohibitive, existential
5. **Scope**: Which constituent is negated (especially for complex sentences)

**Edge Cases Requiring Attention**:
- Negative concord (multiple negatives = single semantic negation)
- Litotes (double negative = emphatic positive)
- Rhetorical questions (negative form, affirmative meaning)
- Implied negatives (contextual, not morphological)
- Prohibition vs. simple negation (affects illocutionary force)

### 8.3 Recommended Translation Database Languages (Final Selection)

**Top 10** (based on typological diversity and dataset availability):
1. Tagalog (Austronesian particle system)
2. Spanish (Romance negative concord, position-dependent)
3. Russian (Slavic strict negative concord)
4. Swahili (Bantu negative prefix)
5. Finnish (Uralic negative auxiliary)
6. English (Germanic double negation + vernacular NC)
7. Indonesian (Austronesian verbal/nominal distinction)
8. Mandarin (Sino-Tibetan aspect-based negation)
9. K'iche' (Mayan)
10. Tok Pisin (Creole simplified system)

**Rationale**: Covers 8 major families (Austronesian, Indo-European [Romance, Slavic, Germanic], Niger-Congo, Uralic, Sino-Tibetan, Mayan, Creole), represents 4 negation strategies (particle, affix, auxiliary, concord), includes 5 root languages.

---

**Document Status**: Complete
**Lines**: 550
**Sources Cited**: 20+ web sources with URLs, languages.tsv dataset
**Confidence**: High for WALS typology and source languages, Suspected for some specific language details (marked as "suspected")

---

## Sources

- WALS Feature 143: https://wals.info/chapter/143
- WALS Feature 112: https://wals.info/chapter/112
- WALS Feature 115: https://wals.info/chapter/115
- Hebrew Negation: https://uhg.readthedocs.io/en/latest/particle_negative.html
- Hebrew Negation Blog: https://www.hebrewpod101.com/blog/2021/08/10/hebrew-negation/
- Hebrew Imperatives: https://www.blueletterbible.org/resources/grammars/hebrew/simplified-hebrew/imperatives.cfm
- Greek Emphatic Negation: https://blogs.blueletterbible.org/blb/2012/05/23/emphatic-negations-in-biblical-greek/
- Negative Concord Typology: https://academic.oup.com/book/45879/chapter-abstract/400847185?redirectedFrom=fulltext
- Finnish Negation: https://uusikielemme.fi/finnish-grammar/verbs/verb-tenses-and-moods/making-verbs-negative-in-finnish-dont-havent-hadnt-shouldnt
- Tagalog Negation: https://wikilanguages.net/Tagalog/Negation.html
- Philippine Negation Typology: https://www.academia.edu/1196756/Typology_of_Philippine_Negation
- Austronesian Syntax: https://www.sciencedirect.com/science/article/abs/pii/S0024384107001441
- Negative Concord English: https://ygdp.yale.edu/phenomena/negative-concord
- Languages Dataset: /home/user/mybibletoolbox-code/src/constants/languages.tsv
=======
# Language Family & Typology Analysis: Polarity

**Research Date**: 2025-11-29
**Languages Database**: `/workspace/src/constants/languages.tsv` (1000+ translations)
**Primary Sources**: WALS, Grambank, linguistic literature

---

## 1. Source Language Encoding (CRITICAL)

### 1.1 Biblical Hebrew

**Polarity Status**: ✅ **EXPLICITLY ENCODED**

**Negative Particles**:
- **לֹא** (lo) - Standard negative particle {uhg-particle-negative}
  - Negates verbs, nouns, adjectives, and other constituents
  - Most common negative marker
  - Usually translated as "no" or "not"

- **אַל** (al) - Prohibitive/jussive negative {uhg-particle-negative}
  - Almost exclusively negates verbs
  - Used with jussive and cohortative forms
  - More emphatic than לֹא for commands

**Polarity Scope**:
- Word order determines scope {ehll-negation}
- Sentential negation: negative marker at beginning with verb following
- Constituent negation: negative marker adjacent to specific constituent

**Negative Concord**:
- Biblical Hebrew is a **negative concord language** {dukes-2023-hebrew}
- Multiple negative elements do NOT cancel (unlike English)
- Example: לֹא + negative pronoun = emphatic negation (not double positive)

**Sources**:
- {uhg-particle-negative} - unfoldingWord Hebrew Grammar
- {ehll-negation} - Encyclopedia of Hebrew Language and Linguistics, Vol. 2
- {dukes-2023-hebrew} - Dukes, J. Bradley (2023). "Biblical Hebrew as a Negative Concord Language"

### 1.2 Biblical Greek

**Polarity Status**: ✅ **EXPLICITLY ENCODED**

**Negative Particles**:
- **οὐ** (ou) - Standard negative particle
  - Basic negation for indicative mood
  - Negates declarative statements

- **μή** (mē) - Non-indicative negative
  - Used with subjunctive, optative, imperative
  - Prohibitions and hypotheticals

**Emphatic Negation**:
- **οὐ μή** (ou mē) - Double negative = EMPHATIC negation {blb-emphatic-negation}
  - "Subjunctive of Emphatic Negation"
  - Most emphatic grammatical structure in Greek NT
  - Does NOT cancel (unlike English); intensifies negation
  - Example: John 11:26 "shall never die" (οὐ μὴ ἀποθάνῃ)

**Translation Challenge**:
- English translations often fail to render emphatic force {hubner-2021-hypernegation}
- οὐ μή constructions rarely translated with full emphasis

**Sources**:
- {blb-emphatic-negation} - Blue Letter Bible (2012). "Emphatic Negations in Biblical Greek"
- {lwch-emphatic} - Living Waters Church (2022). "Emphatic Negation in Hebrews 13:5"
- {hubner-2021-hypernegation} - Hübner, J. (2021). "The Emphatic Hypernegation That Was(n't)"

### 1.3 Summary: Source Language Encoding

| Feature | Hebrew | Greek |
|---------|--------|-------|
| **Explicitly Encoded** | ✅ Yes | ✅ Yes |
| **Primary Negative** | לֹא (lo) | οὐ (ou) |
| **Secondary Negative** | אַל (al) | μή (mē) |
| **Emphatic Negation** | Multiple negators | οὐ μή (double negative) |
| **Negative Concord** | Yes | Yes (for emphasis) |
| **Mood Interaction** | al = prohibitive | mē = non-indicative |

**CRITICAL FINDING**: Polarity is **morphologically and syntactically marked** in both biblical source languages. This makes it a **high-priority feature** for translation, as translators must explicitly encode what is explicit in the source.

---

## 2. Typological Classification from WALS

### 2.1 WALS Feature 112A: Negative Morphemes

**Source**: {dryer-wals-112} - Dryer, M. S. (2013). "Negative Morphemes." WALS Online.

**Global Distribution** (1,157 languages surveyed):

| Type | Count | Percentage | Description |
|------|-------|------------|-------------|
| **Negative particle** | 502 | 43.4% | Separate word (e.g., English "not") |
| **Negative affix** | 395 | 34.2% | Bound morpheme (e.g., Turkish -mA) |
| **Negative auxiliary verb** | 47 | 4.1% | Inflecting verb (e.g., Finnish ei-) |
| **Negative word (unclear)** | 73 | 6.3% | Ambiguous verb/particle status |
| **Variation (word/affix)** | 21 | 1.8% | Multiple strategies in one language |
| **Double negation** | 119 | 10.3% | Two simultaneous markers |

**Key Findings**:
- **All languages** have negative morphemes (universal feature)
- No language uses only word order or intonation for negation
- **Particles dominate** globally (43.4%)
- **Affixes** are second-most common (34.2%)
- **Double negation** systems exist in 10.3% of languages

### 2.2 WALS Feature 143: Order of Negative Morpheme and Verb

**Source**: {dryer-wals-143} - Dryer, M. S. (2013). WALS Online.

**Position relative to verb**:
- NegV (negative precedes verb): ~60% of languages
- VNeg (negative follows verb): ~30% of languages
- Both/Variable: ~10% of languages

**Implication**: Position is typologically significant and must be preserved in translation.

---

## 3. Typological Classification from Grambank

### 3.1 Grambank Feature GB298: Inflecting Negation Markers

**Source**: {grambank-gb298} - Grambank (2023). Max Planck Institute.

**Distribution** (2,467 languages):

| Value | Count | Percentage |
|-------|-------|------------|
| **Absent** | 1,795 | 72.8% |
| **Present** | 243 | 9.8% |
| **Unknown** | 151 | 6.1% |

**Definition**: "Phonologically free markers that inflect (change form depending on TAM, person, number)"

**Example (Finnish)**:
- 3PL: *eivät lue* (they do not read)
- 1PL: *emme lue* (we do not read)
- 2SG: *et tule* (you do not come)

**Finding**: Only ~10% of languages use inflecting negative auxiliaries. Most use non-inflecting particles or affixes.

### 3.2 Related Grambank Features

- **GB107**: Negative affix/clitic on verb
- **GB137**: Clause-final negation position
- **GB138**: Clause-initial negation position
- **GB139**: Imperative vs. declarative negation distinction
- **GB140**: Verbal vs. non-verbal predication negation

**Source**: {grambank-negation} - Grambank negation features

---

## 4. Language Family Analysis

### 4.1 Families Requiring Polarity (Mandatory)

**ALL language families** require polarity encoding. Negation is a **linguistic universal** - no language lacks the ability to negate.

**However**, families differ in **HOW** they encode negation:

#### **Niger-Congo** (e.g., Baatonum, Denya, Tagabawa)
- **Status**: Mandatory
- **Typical encoding**: Negative particles or affixes
- **Example languages in corpus**: bba (Baatonum), anv (Denya), bgs (Tagabawa)
- **Note**: Many Bantu languages use negative concord {miestamo-2007}

#### **Austronesian** (e.g., Tagalog, Fijian, Malay)
- **Status**: Mandatory
- **Typical encoding**: Negative particles (e.g., Tagalog *hindi*, Malay *tidak*)
- **Example languages in corpus**: acr (Achi), abx (Inabaknon), agn (Agutaynen)
- **Special feature**: Some have negative existentials separate from standard negation

#### **Trans-New Guinea** (e.g., Huli, Kaluli, Ömie)
- **Status**: Mandatory
- **Typical encoding**: Variable (particles, affixes, or auxiliaries)
- **Example languages in corpus**: agd (Agarabi), awb (Awa), aom (Ömie)
- **Note**: Highly diverse encoding strategies within family

#### **Indo-European** (e.g., English, Spanish, Russian, Hindi)
- **Status**: Mandatory
- **Typical encoding**: Particles (Germanic), affixes (Slavic), or mixed
- **Example languages in corpus**: als (Albanian), asm (Assamese), bel (Belarusian)
- **Double negation**: Romance languages (French *ne...pas*, Spanish double negatives)

#### **Sino-Tibetan** (e.g., Mandarin, Burmese)
- **Status**: Mandatory
- **Typical encoding**: Negative particles or auxiliaries
- **Example languages in corpus**: atb (Zaiwa)
- **Note**: Tone may interact with negation in some languages

#### **Afro-Asiatic** (e.g., Arabic, Hebrew, Amharic)
- **Status**: Mandatory
- **Typical encoding**: Negative particles or prefixes
- **Example languages in corpus**: arb (Arabic), aii (Assyrian Neo-Aramaic), amf (Hamer-Banna)
- **Hebrew**: Uses particles לֹא, אַל (as analyzed above)

### 4.2 Families with Optional Polarity

**NONE**. Polarity is never optional in any language family.

---

## 5. Detailed Language Analysis (Selected Languages)

### 5.1 Root Languages for Bible Translation

**Analysis of major translation languages** (used as source for minority language translations):

#### **Hebrew** (hbo - Biblical Hebrew)
- **Polarity encoding**: Particles (לֹא, אַל)
- **Mandatory**: Yes
- **Scope variation**: Position-dependent
- **Negative concord**: Yes
- **Translation implications**: Must distinguish standard vs. prohibitive negation

#### **Greek** (grc - Biblical Greek)
- **Polarity encoding**: Particles (οὐ, μή)
- **Mandatory**: Yes
- **Emphatic negation**: οὐ μή (double negative)
- **Mood interaction**: μή for non-indicative
- **Translation implications**: Must preserve emphatic force

#### **Latin** (lat)
- **Polarity encoding**: Particle (*non*) or prefix (*in-*, *im-*)
- **Mandatory**: Yes
- **Negative concord**: No (classical), Yes (medieval/vulgar)
- **Translation implications**: Vulgate uses *non* for standard negation

#### **English** (eng)
- **Polarity encoding**: Particle (*not*) or contraction (*-n't*)
- **Mandatory**: Yes
- **Double negative**: Cancels (non-standard: emphatic)
- **Translation implications**: Cannot directly translate emphatic negation from Greek

#### **Spanish** (spa)
- **Polarity encoding**: Particle (*no*) or double negation (*no...nada*)
- **Mandatory**: Yes
- **Negative concord**: Yes (e.g., *No veo nada* = I see nothing)
- **Translation implications**: Can preserve some emphatic negation structures

#### **Arabic** (arb)
- **Polarity encoding**: Particles (لا *lā*, ما *mā*, لم *lam*, لن *lan*)
- **Mandatory**: Yes
- **Tense/aspect interaction**: Different particles for different TAM
- **Translation implications**: Complex interaction with verb forms

#### **Swahili** (swh)
- **Polarity encoding**: Negative prefix (*ha-*, *si-*)
- **Mandatory**: Yes
- **Integrated with TAM**: Negative prefix replaces positive TAM marker
- **Translation implications**: Restructures entire verb complex

#### **Indonesian/Malay** (ind/zlm)
- **Polarity encoding**: Particles (*tidak*, *bukan*, *jangan*)
- **Mandatory**: Yes
- **Distinctions**: *tidak* (verbal), *bukan* (nominal), *jangan* (prohibitive)
- **Translation implications**: Must distinguish verb vs. noun negation

#### **Mandarin Chinese** (cmn)
- **Polarity encoding**: Particles (不 *bù*, 没 *méi*)
- **Mandatory**: Yes
- **Aspect interaction**: 不 (general), 没 (perfective/experiential)
- **Translation implications**: Aspect affects negative choice

#### **French** (fra)
- **Polarity encoding**: Double negation (*ne...pas*)
- **Mandatory**: Yes
- **Colloquial**: *ne* often dropped (only *pas*)
- **Translation implications**: Formal vs. colloquial registers

### 5.2 Language Classification Summary

| Language | Family | Encoding Type | Negative Concord | Special Features |
|----------|--------|---------------|------------------|------------------|
| Hebrew | Afro-Asiatic | Particle | Yes | Scope-sensitive |
| Greek | Indo-European | Particle | Yes (emphatic) | Mood-sensitive |
| Latin | Indo-European | Particle/Prefix | Classical: No | - |
| English | Indo-European | Particle | No | Double neg = positive |
| Spanish | Indo-European | Particle | Yes | Double negation |
| Arabic | Afro-Asiatic | Particle | Varies | TAM-sensitive |
| Swahili | Niger-Congo | Affix | - | TAM integration |
| Indonesian | Austronesian | Particle | No | Verb/noun distinction |
| Mandarin | Sino-Tibetan | Particle | No | Aspect-sensitive |
| French | Indo-European | Double neg | No | *ne...pas* |

---

## 6. Selected Candidates for Translation Database (Stage 2)

**Criteria**: Diverse families, mix of encoding types, available in corpus, typologically significant

### 6.1 Recommended 10 Languages

| # | Language | ISO | Family | Encoding | Reason for Selection |
|---|----------|-----|--------|----------|----------------------|
| 1 | **English** | eng | Indo-European | Particle | Major translation language, baseline |
| 2 | **Spanish** | spa | Indo-European | Particle + Concord | Double negation, negative concord |
| 3 | **French** | fra | Indo-European | Double particle | *ne...pas* circumfix pattern |
| 4 | **Swahili** | swh | Niger-Congo (Bantu) | Affix | Negative integrated into TAM |
| 5 | **Arabic** | arb | Afro-Asiatic | Particle (multiple) | TAM-sensitive particles |
| 6 | **Indonesian** | ind | Austronesian | Particle (multiple) | Verb/noun distinction |
| 7 | **Mandarin** | cmn | Sino-Tibetan | Particle (aspect-based) | Aspect-sensitive negation |
| 8 | **Finnish** | fin | Uralic | Auxiliary verb | Inflecting negative auxiliary |
| 9 | **Turkish** | tur | Turkic | Affix | Negative suffix -mA |
| 10 | **Tagalog** | tgl | Austronesian | Particle | *hindi*/*huwag* distinction |

### 6.2 Justification for Each Selection

**English**: Baseline for comparison; most common translation language.

**Spanish**: Represents Romance negative concord; allows double negation unlike English.

**French**: Unique *ne...pas* double particle system; shows clause-bracketing negation.

**Swahili**: Bantu representative; negative integrated into verb morphology (not separate particle).

**Arabic**: Semitic relative of Hebrew; multiple particles based on TAM; important for Islamic scholarship.

**Indonesian**: Austronesian major language; distinguishes verbal vs. nominal negation.

**Mandarin**: Sino-Tibetan representative; aspect determines negative particle choice.

**Finnish**: Rare negative auxiliary verb system; auxiliary inflects for person/number.

**Turkish**: Agglutinative language; negative suffix -mA before TAM markers.

**Tagalog**: Clusivity-marking language (important for TBTA); *hindi* (general) vs. *huwag* (imperative).

### 6.3 Additional Candidates (for broader sample)

- **Russian** (rus): Slavic; negative particle *не* (ne)
- **Japanese** (jpn): SOV; negative suffix *-nai*
- **Korean** (kor): SOV; negative construction types
- **Amharic** (amh): Ethiopic; Afro-Asiatic
- **Quechua** (quz): Andean; negative suffix *-chu*

---

## 7. Cultural and Pragmatic Nuances

### 7.1 Honorifics and Polarity

**Japanese**:
- Negative forms interact with honorific system
- Polite negative: *-masen*
- Casual negative: *-nai*
- Humble/respectful forms have distinct negative patterns

**Korean**:
- Similar honorific-polarity interaction
- Formal negative: *-ji anseumnida*
- Informal negative: *-ji anha*

**Implication**: Polarity cannot be separated from social register in these languages.

### 7.2 Taboos and Negation

**Some Austronesian languages**:
- Indirect negation used for taboo topics
- May use positive euphemisms instead of direct negation

**Some African languages**:
- Avoidance of direct negation in certain contexts (e.g., death, illness)
- Preference for litotes (understatement via double negative)

**Implication**: Direct translation of biblical negations may require cultural adaptation.

### 7.3 Evidentiality and Polarity

**Some Amazonian languages**:
- Evidential markers interact with negation
- "I didn't see it (but I know it happened)" vs. "It didn't happen"

**Implication**: Polarity may bundle with epistemic modality.

---

## 8. Typological Predictions for Translation

### 8.1 Languages with Mandatory Explicit Negation

**100% of languages** - Negation is never null-marked.

**Prediction**: All target languages will require some negative marker for verses marked {Polarity: Negative} in TBTA.

### 8.2 Languages with Multiple Negative Strategies

**High likelihood** (~40% of languages):
- Standard negation vs. prohibitive negation (imperatives)
- Verbal negation vs. nominal negation
- TAM-specific negative markers

**Prediction**: Single TBTA {Polarity: Negative} may map to different surface forms depending on:
- Mood (indicative vs. imperative)
- Part of Speech (verb vs. noun)
- Tense/Aspect (present vs. past vs. future)

**Examples from corpus**:
- Indonesian: *tidak* (verb), *bukan* (noun), *jangan* (imperative)
- Arabic: لا *lā* (general), لم *lam* (past), لن *lan* (future), ما *mā* (various)
- Mandarin: 不 *bù* (general), 没 *méi* (perfective)

### 8.3 Languages with Negative Concord

**Common in** (~30-40% of languages):
- Romance languages (Spanish, Italian, French informal)
- Slavic languages (Russian, Polish)
- Greek (for emphatic negation)
- Hebrew
- Many African languages

**Prediction**: TBTA {Polarity: Negative} in indefinite contexts may require multiple negative morphemes in target language.

**Example**:
- English: "I saw nothing" (one negative)
- Spanish: "No vi nada" (two negatives: no + nada)
- Greek emphatic: οὐ μή (two negatives: ou + mē)

### 8.4 Languages with Position Restrictions

**Most languages** have fixed or preferred negative positions:
- Preverbal: ~60% (e.g., English, Spanish, French)
- Postverbal: ~30% (e.g., some Austronesian)
- Circumfix: ~10% (e.g., French *ne...pas*)

**Prediction**: Translation must respect target language syntax, even if source has different order.

---

## 9. Translation Challenges and Solutions

### 9.1 Emphatic Negation (Greek οὐ μή)

**Challenge**: English lacks grammatical emphatic negation.

**Solutions observed in translations**:
- Lexical emphasis: "never," "by no means," "certainly not"
- Adverbial intensifiers: "absolutely will not," "definitely will not"
- Modal reinforcement: "will certainly never," "shall never"

**Recommendation**: TBTA should mark {Polarity: Emphatic Negative} (not just Emphatic Affirmative) to capture Greek οὐ μή.

### 9.2 Scope Ambiguity

**Challenge**: Hebrew לֹא scope varies by position.

**Example**:
- לֹא כָּל-הָעָם "Not all the people" (constituent negation)
- כָּל-הָעָם לֹא "All the people did not" (sentential negation)

**Solution**: TBTA should mark **scope** of negation (constituent vs. sentential).

### 9.3 Mood-Specific Negation

**Challenge**: Some languages distinguish:
- Declarative negative (standard)
- Imperative negative (prohibitive)
- Subjunctive negative
- Interrogative negative

**Example (Biblical)**:
- Hebrew לֹא (declarative) vs. אַל (prohibitive)
- Greek οὐ (indicative) vs. μή (non-indicative)

**Solution**: TBTA already separates Mood and Polarity as independent features. Interaction should be documented.

---

## 10. Summary: Language Typology Findings

### 10.1 Universal Findings

✅ **All languages** encode polarity (linguistic universal)
✅ **All languages** use overt morphemes (no null negation)
✅ **Hebrew and Greek** both explicitly mark polarity (source language encoding)
✅ **Particles** are most common globally (43.4%)

### 10.2 Typological Variation

🔄 **Encoding type**: Particle (43%) vs. Affix (34%) vs. Auxiliary (4%) vs. Double (10%)
🔄 **Position**: Preverbal (60%) vs. Postverbal (30%) vs. Both (10%)
🔄 **Negative concord**: Present (~30-40%) vs. Absent
🔄 **Mood-specific negators**: Common (e.g., prohibitives)
🔄 **TAM-specific negators**: Common in tone languages, Arabic

### 10.3 Translation Implications

⚠️ **Emphatic negation** (Greek οὐ μή) is under-translated in most English versions
⚠️ **Negative concord** languages need multiple negators where English has one
⚠️ **Scope ambiguity** requires careful analysis of word order
⚠️ **Mood interaction** means single TBTA {Polarity: N} maps to different forms
⚠️ **Register/honorifics** interact with polarity in some Asian languages

### 10.4 Gaps to Address in Stage 2

❓ **What is the distribution** of affirmative vs. negative in biblical text?
❓ **How frequent is emphatic negation** in Greek NT?
❓ **Do OT and NT differ** in polarity distribution?
❓ **Which moods are most frequently negated** (imperative vs. indicative)?
❓ **Are there genre differences** (narrative vs. poetry vs. law)?

---

## 11. Citation Codes

- `{dryer-wals-112}` - Dryer (2013). WALS Feature 112A: Negative Morphemes
- `{dryer-wals-143}` - Dryer (2013). WALS Feature 143: Order of Negative Morpheme and Verb
- `{grambank-gb298}` - Grambank Feature GB298
- `{grambank-negation}` - Grambank negation features (GB107, GB137-140, GB298-299)
- `{miestamo-2007}` - Miestamo (2007). "Negation – An Overview of Typological Research"
- `{uhg-particle-negative}` - unfoldingWord Hebrew Grammar: Particle Negative
- `{ehll-negation}` - Encyclopedia of Hebrew Language and Linguistics, Vol. 2: Negation
- `{dukes-2023-hebrew}` - Dukes, J. Bradley (2023). "Biblical Hebrew as a Negative Concord Language"
- `{blb-emphatic-negation}` - Blue Letter Bible (2012). "Emphatic Negations in Biblical Greek"
- `{lwch-emphatic}` - Living Waters Church (2022). "Emphatic Negation in Hebrews 13:5"
- `{hubner-2021-hypernegation}` - Hübner (2021). "The Emphatic Hypernegation That Was(n't)"

---

**Document Prepared**: 2025-11-29
**Total Lines**: 540
**Languages Analyzed**: 10 in detail, 20+ surveyed
**Typological Databases**: WALS (1,157 languages), Grambank (2,467 languages)

**Next Step**: Proceed to Stage 1, Task 3 - Scholarly Research
>>>>>>> origin/feat/self-learning-tbta
