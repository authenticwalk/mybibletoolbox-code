# Person System (Grammatical Person + Clusivity)

Grammatical marking of discourse participant relationships (speaker, addressee, other). The critical distinction for Bible translation is **clusivity** - inclusive vs. exclusive first person plural ("we").

## Quick Facts

| Aspect | Details |
|--------|---------|
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
