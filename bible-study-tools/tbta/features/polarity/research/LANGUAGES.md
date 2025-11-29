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
