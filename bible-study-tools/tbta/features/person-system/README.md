<<<<<<< HEAD
# Person System (Grammatical Person + Clusivity)

Grammatical marking of discourse participant relationships (speaker, addressee, other). The critical distinction for Bible translation is **clusivity** - inclusive vs. exclusive first person plural ("we").
=======
# Person System (with Clusivity)

**Grammatical person** distinguishes speaker (1st), addressee (2nd), and others (3rd). **Clusivity** is the distinction in first person plural between "we" including the addressee (inclusive) vs excluding the addressee (exclusive). Affects ~31.5% of world languages, nearly universal in Austronesian.

---
>>>>>>> origin/feat/self-learning-tbta

## Quick Facts

| Aspect | Details |
|--------|---------|
<<<<<<< HEAD
| **TBTA Tier** | A - Essential (affects 1,000+ languages) |
| **Values** | 5: First (1), Second (2), Third (3), First Inclusive (A), First Exclusive (B) |
| **Global Prevalence** | ~31.5% of languages have clusivity distinction (WALS) |
| **Source Languages** | Hebrew/Greek: NO clusivity - TBTA annotations are **interpretive** |
| **Major Families** | Austronesian (near-universal), Australian, Dravidian, Sino-Tibetan |
| **Dataset Coverage** | 176 Austronesian + others ≈ 200-250 languages with clusivity |
| **Theological Stakes** | HIGH - Trinity contexts, prayer theology, apostolic authority |

## What is Clusivity?

**Inclusive "we"** (Code: A): Speaker + Listener(s) - "you and I together"
- Tagalog: *tayo*
- Malay/Indonesian: *kita*
- Example: Hebrews 4:14 "Let us hold fast" (author + readers)

**Exclusive "we"** (Code: B): Speaker + Others, excluding Listener - "they and I, but not you"
- Tagalog: *kami*
- Malay/Indonesian: *kami*
- Example: Acts 15:25 "It seemed good to us" (apostles, not congregation)

## Examples: Translation Choices

### Example 1: Prayer Theology (CRITICAL)

| Verse | English | Clusivity | Stakes |
|-------|---------|-----------|--------|
| Matthew 6:9 | "Our Father..." | **MUST be EXCLUSIVE** | Inclusive = heretical (God prays to himself) |

**Guidance**: God is addressee, NOT part of "our/we" praying. Early missionaries used inclusive - had to be corrected.

### Example 2: Trinity Reference (HIGH STAKES)

| Verse | English | Clusivity | Number | Stakes |
|-------|---------|-----------|--------|--------|
| Genesis 1:26 | "Let us make man..." | Inclusive preferred | Trial (if available) | Trinity doctrine |

**Guidance**: Trinitarian interpretation - "us" = intra-Trinitarian dialogue (Father, Son, Holy Spirit).
- ✅ **FIRST CHOICE**: Trial number (exactly 3) + Inclusive person (Kilivila, Larike, Fijian)
- ✅ **ACCEPTABLE**: Plural + Inclusive (if no trial)
- ❌ **FORBIDDEN**: Dual number (implies only 2 persons - Arianism/Binitarianism)

### Example 3: Apostolic Authority (MEDIUM STAKES)

| Verse | English | Clusivity | Stakes |
|-------|---------|-----------|--------|
| Acts 15:25 | "It seemed good to us..." | **MUST be EXCLUSIVE** | Ecclesiology |

**Guidance**: Apostles deciding FOR church, not WITH congregation. Inclusive would incorrectly imply congregational participation in apostolic decision-making.

### Example 4: Epistolary "We" (CONTEXT-DEPENDENT)

| Verse | Context | Clusivity | Reasoning |
|-------|---------|-----------|-----------|
| 1 Cor 3:9 | "We are God's fellow workers" | Exclusive | Paul + Apollos (not all Corinthians are apostles) |
| 1 Cor 15:51 | "We shall all be changed" | Inclusive | All believers together (Paul + readers) |

**Guidance**: NO blanket rule for entire epistle - analyze each instance separately.

## Target Audiences

**Primary**: Bible translators in clusivity-marking languages (1,000+ languages)
- Austronesian: Tagalog, Malay, Indonesian, Filipino languages, Pacific languages
- Australian: Non-Pama-Nyungan languages
- Asian: Dravidian (Tamil, Telugu), Sino-Tibetan (Mandarin)
- American: Quechuan, some Mesoamerican and North American languages

**Challenge**: Source languages (Hebrew, Greek, English) lack clusivity - translators need interpretive guidance for EVERY first person plural context.

**See**: [research/LANGUAGES.md](research/LANGUAGES.md) for full typological analysis

## TBTA Encoding

**Position**: 10 in noun/pronoun encoding
**Codes**:
- `1` = First Person (ambiguous clusivity - used when source language doesn't distinguish)
- `2` = Second Person
- `3` = Third Person
- `A` = First Inclusive (speaker + listener)
- `B` = First Exclusive (speaker + others, not listener)

**Note**: Honorific person systems (T-V distinction, Japanese keigo) encoded separately via Speaker Demographics feature.

**See**: [research/TBTA.md](research/TBTA.md) for full TBTA documentation analysis

## Research Files

| File | Content | Lines |
|------|---------|-------|
| [research/README.md](research/README.md) | Research summary | 200 |
| [research/TBTA.md](research/TBTA.md) | TBTA documentation review | 350 |
| [research/LANGUAGES.md](research/LANGUAGES.md) | Language typology & families | 450 |
| [research/SCHOLARLY.md](research/SCHOLARLY.md) | 27+ scholarly sources + case studies | 500+ |
| [research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml) | Non-arbitrary contexts | 500 |

**Total Research**: ~2,000 lines, 27+ scholarly sources, 4 typological databases

---

**Status**: Stage 1 Research Complete
**Next**: Stage 2 Data Analysis & Frequency Validation
=======
| **TBTA Values** | First (10,207), First Exclusive (1,272), First Inclusive (1,386), Second (16,732), Third (141,890) - 5 core values + 3 edge cases |
| **Total Entries** | 171,876 annotations across ~12,000 verses |
| **Source Languages** | Hebrew & Greek do NOT encode clusivity (TBTA annotations are interpretive) |
| **Critical Languages** | Austronesian (Tagalog, Malay, Fijian), Australian (Arrernte), some Sino-Tibetan (Mandarin optional) |
| **Theological Stakes** | **HIGH** - Wrong choice can create heresy (e.g., Trinity, prayers, apostolic authority) |
| **Prevalence** | ~31.5% of world languages (WALS); ~30-35% of our translation database |
| **TBTA Tier** | A (Essential - affects 1000+ languages, cannot be easily inferred) |

---

## Target Audience

### Languages That REQUIRE Clusivity (Mandatory)

**Austronesian** (~250-300 in our database): Tagalog *tayo* (incl) vs *kami* (excl), Malay *kita* vs *kami*, Fijian, Cebuano, Chuukese, Chamorro, 100+ PNG/Philippines languages

**Australian** (~30): Arrernte *ngali* (dual incl) vs *ngaliju* (dual excl), Alyawarr, Burarra

**Sino-Tibetan** (partial): Mandarin 咱们 *zánmen* (incl) vs 我们 *wǒmen* (ambiguous), Chin languages

**Dravidian**: Tamil, Telugu (not in current database)

**Vietnamese**: *chúng ta* (incl) vs *chúng tôi* (excl)

### Languages That LACK Clusivity (Absent)

**Indo-European**: English, Spanish, German, French, Russian, Greek (all use ambiguous "we")

**Afro-Asiatic**: Hebrew, Arabic, Coptic

**Most Papuan languages** (despite proximity to Austronesian)

**Key Distinction**: Root languages (Hebrew, Greek, English) lack clusivity; target languages often require it → **translators must infer from context**.

See [research/LANGUAGES.md](research/LANGUAGES.md) for detailed typology.

---

## Examples: Translation Choices

### ✅ Correct: The Lord's Prayer (Matt 6:12, Luke 11:4)

| Language | "Forgive us our sins" | Clusivity | Rationale |
|----------|----------------------|-----------|-----------|
| **English** | "Forgive us" (ambiguous) | N/A | No distinction |
| **Tagalog** | *Patawarin mo **kami*** | **EXCLUSIVE** ✅ | We humans (not you God) sinned |
| **ERROR (Kwara'ae)** | ~~Inclusive "we"~~ | ❌ **HERETICAL** | Would imply God shares in human sin! |

**CRITICAL**: Exclusive "we" excludes God from "our sins" (God is sinless). Inclusive would be heresy.

### ✅ Correct: Trinity (Gen 1:26)

| Language | "Let us make man" | Clusivity | Number | Interpretation |
|----------|-------------------|-----------|--------|----------------|
| **Hebrew** | נַעֲשֶׂה (na'aseh) | Ambiguous | Plural | Original text |
| **Fijian** | 1PL Inclusive | **INCLUSIVE** ✅ | **TRIAL** (exactly 3) | Trinity (Father, Son, Spirit) |
| **English** | "Let us" | Ambiguous | Plural | Allows multiple interpretations |

**Orthodox interpretation**: First Inclusive + Trial Number = God (3 Persons) speaking within Godhead.

**FORBIDDEN**: Second person (would include humans in creating), Third person alone (divine council, not Trinity).

### ⚠️ Ambiguous: Galatians 2:15

| Interpretation | Clusivity | Who is "we"? |
|----------------|-----------|--------------|
| Paul addresses Peter (Antioch speech) | **INCLUSIVE** | Paul + Peter (both Jews) |
| Paul addresses Galatians (letter shift) | **EXCLUSIVE** | Paul + Jewish Christians (not Gentile Galatians) |

**Scholarly disagreement**: Greek text does not clarify speech boundary. Translators must make interpretive choice.

---

## TBTA Encoding

- **Field Name**: "Person"
- **Position**: 10 in noun character codes
- **Values**: `1` (First), `2` (Second), `3` (Third), `A` (First Inclusive), `B` (First Exclusive)
- **Part of Speech**: Nouns/pronouns only (NOT verbs, despite many languages marking person on verbs)
- **Annotation Method**: Semantic interpretation based on discourse context (since Hebrew/Greek lack morphological clusivity)

**Key Policy**: TBTA prioritizes **semantic meaning** over morphological form. Annotators determine clusivity from:
1. Participant roles (who is speaking to whom?)
2. Theological analysis (Trinity references, prayers, apostolic authority)
3. Discourse context (exhortations include audience; decisions by leaders exclude audience)

See [research/TBTA.md](research/TBTA.md) for full documentation.

---

## For More Information

- **[research/README.md](research/README.md)**: Executive summary of all research (200 lines)
- **[research/TBTA.md](research/TBTA.md)**: TBTA annotation policies, values, edge cases
- **[research/LANGUAGES.md](research/LANGUAGES.md)**: Language families, typology, our translation database
- **[research/SCHOLARLY.md](research/SCHOLARLY.md)**: 25+ scholarly sources, case studies
- **[research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)**: High-stakes vs arbitrary contexts

---

**Document Status**: Stage 1 Research Complete
**Last Updated**: 2025-11-29
**Lines**: 75 (at progressive disclosure limit)
>>>>>>> origin/feat/self-learning-tbta
