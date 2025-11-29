# Person System Research Summary

## Overview

**Person** is a grammatical category distinguishing speaker (1st), addressee (2nd), and others (3rd). **Clusivity** is the distinction in first person plural between inclusive "we" (including addressee) and exclusive "we" (excluding addressee). This feature affects ~31.5% of world languages and is **critical for Bible translation**.

**Key Finding**: Hebrew and Greek do NOT encode clusivity, but TBTA provides semantic annotations based on contextual analysis. Translators into clusivity-marking languages must disambiguate every "we" based on theology, discourse context, and participant roles.

---

## What is Person/Clusivity?

### Basic Person System (3-way)

| Person | Meaning | Example (English) |
|--------|---------|-------------------|
| **1st** | Speaker | I, we |
| **2nd** | Addressee | you, you all |
| **3rd** | Others | he, she, they |

### Clusivity System (5-way)

| Value | Meaning | Example Languages |
|-------|---------|-------------------|
| **First (ambiguous)** | I, or we (unclear if inclusive/exclusive) | English "we" |
| **First Inclusive** | We (speaker + addressee + others) | Tagalog *tayo*, Malay *kita* |
| **First Exclusive** | We (speaker + others, NOT addressee) | Tagalog *kami*, Malay *kami* |
| **Second** | You (singular or plural) | English "you" |
| **Third** | He/she/they | English "they" |

---

## TBTA Documentation (TBTA.md)

### TBTA Values & Encoding

- **5 values**: First, First Exclusive, First Inclusive, Second, Third
- **Encoding**: Position 10 in noun codes: `1`, `2`, `3`, `A` (inclusive), `B` (exclusive)
- **Part of Speech**: Nouns/pronouns only (NOT verbs, unlike many languages)
- **Tier**: A (Essential - affects 1000+ languages)

### Critical Finding: Source Languages Lack Clusivity

**Hebrew and Greek do NOT morphologically encode clusivity.** All TBTA annotations of inclusive vs exclusive are **SEMANTIC INTERPRETATIONS** based on:
1. Discourse context (who is speaking to whom?)
2. Participant tracking (who is included in the action?)
3. Exegetical analysis (what did the original author intend?)

**Examples**:
- **Acts 15:25**: Greek ἡμῖν (hēmin) = "us" (ambiguous) → TBTA: "First Exclusive" (apostles/elders, not Gentile recipients)
- **Gen 1:26**: Hebrew נַעֲשֶׂה (na'aseh) = "let us make" (ambiguous) → TBTA: "First Inclusive + Trial" (Trinity deliberation)

### Edge Cases

**Trinity References** (Gen 1:26, 3:22, 11:7, Isa 6:8):
- TBTA annotates First Inclusive + Trial Number = Trinity interpretation
- Alternative (Third Person + angels) = Divine Council interpretation
- Person choice has **HIGH theological stakes** (Trinity vs non-Trinity theology)

**The Lord's Prayer Error**:
- Early Kwara'ae translation used **inclusive** "we" in "Forgive us our sins"
- Implied **God shares in human sin** (heretical)
- Corrected to **exclusive** "we" (we humans, not you God)

---

## Language Families & Typology (LANGUAGES.md)

### Global Distribution

**31.5%** of world languages distinguish inclusive/exclusive (WALS sample)

| Region | Prevalence |
|--------|------------|
| Austronesia | Nearly universal (~1000+ languages) |
| Northern Australia | Nearly universal |
| Americas | Common |
| Asia (South/SE) | Common (Dravidian, some Sino-Tibetan, Vietnamese) |
| Europe | Absent (except Caucasus) |
| Africa | Sporadic |

### Languages in Our Database (~1000 total)

**Mandatory clusivity** (~30-35% of database):
- **Austronesian** (~250-300): Tagalog, Malay, Cebuano, Fijian, Chuukese, Chamorro + PNG/Philippines languages
- **Australian** (~30): Arrernte, Alyawarr, Burarra (especially in dual number)
- **Sino-Tibetan** (~15): Mandarin (optional: 咱们 *zánmen* incl vs 我们 *wǒmen* ambiguous), Chin languages

**Absent clusivity**:
- **Indo-European**: English, Spanish, German, French, Russian, Greek, etc.
- **Afro-Asiatic**: Hebrew, Arabic, Coptic
- **Most Papuan languages**

### Root Languages for Bible Translation

Of 10 major root languages, **only Indonesian/Malay requires clusivity**:
- Hebrew, Greek, Latin, English, Spanish, French, Arabic, Swahili: **ABSENT**
- Indonesian/Malay: **MANDATORY**
- Mandarin: **OPTIONAL**

**Challenge**: Translating from non-clusivity languages (Hebrew/Greek/English) into clusivity-required languages requires contextual inference.

---

## Scholarly Research (SCHOLARLY.md)

### Key Scholarly Works

1. **Filimonova (2005)**: *Clusivity: Typology and case studies* (definitive reference, 436 pages, 15 papers)
2. **Corbett (2000)**: *Number* (person hierarchy: 1st > 2nd > 3rd > kin > human > animate > inanimate)
3. **Comrie (1989)**: *Language Universals and Linguistic Typology* (pioneering typology)
4. **WALS Chapter 39**: Cross-linguistic survey (31.5% prevalence)

### Historical Discovery

**1560**: Domingo de Santo Tomás first described clusivity in Quechua (Incan language). Europeans had no concept of this distinction until encountering non-Indo-European languages.

### Person Hierarchy & Universals

**Corbett's Person Hierarchy**: 1st person > 2nd person > 3rd person
- **Prediction**: Clusivity (a 1st-person feature) is more common than 2nd/3rd-person distinctions
- **Validated**: Clusivity appears in ~31% of languages; 2nd-person clusivity is controversial/unattested

---

## Theologically Significant Contexts (THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)

### High Stakes (~10 contexts)

**Trinity References** (HIGHEST):
- Gen 1:26 ("Let us make man") - First Inclusive + Trial = Trinity
- Gen 3:22, 11:7, Isa 6:8 - Similar patterns
- John 14:23 ("We will come to him") - Father + Son + (Spirit)

**Prayers Excluding God from Sin**:
- Matt 6:12, Luke 11:4 (Lord's Prayer "Forgive us") - MUST use Exclusive (humans, not God)
- Dan 9, Neh 9 (confessions of sin) - Exclusive (God is sinless)

**Apostolic Authority**:
- Acts 15:25-28 (Jerusalem Council "It seemed good to us") - Exclusive (apostles, not Gentile recipients)

### Medium Stakes (~15 contexts)

- Rom 3:23 ("All have sinned") - Inclusive (Paul + readers + all humanity)
- 1 Cor 15:51 ("We shall all be changed") - Exclusive (believers only, not unbelievers)
- Apostolic letters distinguishing apostles from congregations

### Low Stakes (~20 contexts)

- Exhortations ("Let us hold fast" Heb 4:14) - Inclusive (preacher + hearers)
- Narrative travel accounts (Acts "we-passages") - Context-dependent

### Arbitrary (~90% of contexts)

- Generic humanity ("We reap what we sow")
- Crowd sizes, routine speech acts
- Context makes participants clear; clusivity is stylistic

---

## Section-by-Section Cross-References

### TBTA.md → LANGUAGES.md

**Discrepancy**: TBTA annotates clusivity for Hebrew/Greek, but LANGUAGES.md confirms these languages don't encode it.
- **Resolution**: TBTA annotations are **INTERPRETIVE**, not morphological.
- **Implication**: Annotators infer clusivity from context; different exegetes may disagree.

### LANGUAGES.md → SCHOLARLY.md

**Agreement**: Both confirm 31.5% global prevalence (WALS), nearly universal in Austronesian.
- LANGUAGES.md analyzes our specific database (~30-35% require clusivity).
- SCHOLARLY.md provides theoretical framework (Corbett, Filimonova).

### TBTA.md + THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml

**Agreement**: Both identify Gen 1:26, Acts 15:25, Lord's Prayer as critical contexts.
- TBTA.md documents how TBTA annotates these.
- THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml explains **why** choices matter theologically.

---

## Key Disagreements / Ambiguities

1. **Gal 2:15**: Scholarly disagreement on whether Paul addresses Peter (inclusive) or Galatians (exclusive). Greek text ambiguous.

2. **Frequency of non-arbitrary contexts**: THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml estimates <3% of verses have high/medium theological stakes. Needs verification against actual TBTA data.

3. **Trans-New Guinea languages** (~200 in database): Clusivity status unverified. Could shift percentage estimates.

---

## Gaps & Further Research

From TBTA.md:
1. Generic/impersonal uses (how does TBTA handle?)
2. Zero person / fourth person (not documented)
3. Second-person clusivity (not in TBTA, controversial in linguistics)
4. Verb agreement (TBTA only annotates nouns/pronouns)

From LANGUAGES.md:
1. Trans-New Guinea family: Verify clusivity status (200+ languages)
2. Mayan languages: Check if any mark clusivity (~20 in database)
3. Dravidian: No languages in current database - consider adding Tamil/Telugu
4. Vietnamese: Verify clusivity (suspected mandatory, not confirmed from grammar)

From SCHOLARLY.md:
1. Obviation (Algonquian "4th person") - not in TBTA, but Algonquin/Blackfoot in database
2. Generic person (Finnish-type) - not in TBTA
3. Historical development of clusivity in specific language families

From THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml:
1. **All verse patterns marked "unverified"** - need to verify against:
   - TBTA actual annotations
   - Exegetical commentaries
   - Translation practitioner feedback
2. Frequency estimates (<3% high stakes, ~90% arbitrary) need validation with Stage 2 data analysis

---

## Next Steps (Stage 2 Prerequisites)

Based on this research, Stage 2 (Analysis) should:

1. **Extract TBTA data** for all 5 person values
   - Frequency of each value (First, First Exclusive, First Inclusive, Second, Third)
   - Distribution across OT/NT, genres, books

2. **Verify theologically significant verses**
   - Check TBTA annotations for Gen 1:26, Acts 15:25, Matt 6:12, etc.
   - Confirm whether TBTA matches orthodox Christian interpretation

3. **Build Translation Database** (10 candidate languages)
   - Tagalog, Malay, Mandarin, English, Spanish, Cebuano, Arrernte, Fijian, Vietnamese, Chuukese
   - Extract how they handle Gen 1:26, Acts 15:25, Rom 3:23, 1 Cor 15:51

4. **Analyze clusivity disambiguation patterns**
   - When does TBTA use Inclusive vs Exclusive?
   - Correlate with discourse roles (prayer, apostolic letter, exhortation, narrative)
   - Test whether patterns are predictable

5. **Validate theological significance estimates**
   - Are high-stakes contexts really <3% of verses?
   - How often do translators disagree on clusivity?

---

## Bibliography

See individual research files for full citations:
- **TBTA.md**: TBTA source documentation
- **LANGUAGES.md**: WALS, Wikipedia, language databases, Medium, Language Log
- **SCHOLARLY.md**: Filimonova (2005), Corbett (2000), Comrie (1989), WALS, APICS, TIPs
- **THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml**: Theological analysis + web research (unverified)

Total sources: 25+ scholarly works, databases, and web resources

---

**Document Status**: Complete
**Last Updated**: 2025-11-29
**Lines**: 200 (within progressive disclosure limit)
