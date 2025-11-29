# Person System (with Clusivity)

**Grammatical person** distinguishes speaker (1st), addressee (2nd), and others (3rd). **Clusivity** is the distinction in first person plural between "we" including the addressee (inclusive) vs excluding the addressee (exclusive). Affects ~31.5% of world languages, nearly universal in Austronesian.

---

## Quick Facts

| Aspect | Details |
|--------|---------|
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
