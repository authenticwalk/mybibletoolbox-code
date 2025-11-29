# Proximity System

## Feature Description

**Proximity System** captures spatial, temporal, and discourse distance distinctions through demonstrative systems (this/that/yonder) and related distance-based grammatical categories.

## Quick Facts

| Attribute | Value |
|-----------|-------|
| **TBTA Field** | `Proximity` (position 8 in noun semantic string) |
| **Part of Speech** | Nouns only |
| **Total Values** | 10 (including "Not Applicable") |
| **Source Languages** | Hebrew: 2-way (זֶה/הַהוּא); Greek: 2-3 way (οὗτος/ἐκεῖνος/ὅδε) |
| **Critical Languages** | Spanish, Japanese, Korean, Hindi, Swahili, Tagalog (3-way person-oriented) |
| **TBTA Tier** | **A - Essential** (affects 1000+ languages, cannot be easily inferred) |
| **Theological Stakes** | 5-10% non-arbitrary (Trinity, Christology, Resurrection contexts) |
| **Estimated Frequency** | ~40-60% of nouns (excluding generic nouns/proper names) |

## Value Inventory

| Code | Value | Domain | Example Context |
|------|-------|--------|----------------|
| `n` | Not Applicable | - | Generic nouns, proper names |
| `N` | Near Speaker and Listener | Spatial | "this bread" (both at table) |
| `S` | Near Speaker | Spatial | John 1:29 "Behold the Lamb" |
| `L` | Near Listener | Spatial | "that (by you)" in person-oriented languages |
| `R` | Remote within Sight | Spatial | "that mountain" (visible, distant) |
| `r` | Remote out of Sight | Spatial | "that city" (beyond view) |
| `T` | Temporally Near | Temporal | Heb 1:2 "these last days" |
| `t` | Temporally Remote | Temporal | Gen 1:1 "In the beginning" |
| `C` | Contextually Near with Focus | Discourse | Acts 1:11 "THIS Jesus" (emphatic) |
| `c` | Contextually Near | Discourse | Rom 8:1 "those who..." (anaphoric) |

## Target Audiences

**Primary**: 1000+ languages with multi-way demonstrative systems requiring finer distinctions than English this/that.

### Language Family Requirements

- **Austronesian** (280+ in database): Mandatory - 2-3 way person-oriented (Tagalog, Indonesian, Fijian)
- **Trans-New Guinea** (180+ in database): Mandatory - 2-5+ way, often with elevation/visibility
- **Niger-Congo/Bantu** (80+ in database): Mandatory - 3-way with noun class agreement (Swahili)
- **Indo-European** (50+ in database):
  - Romance: Mandatory - 3-way person-oriented (Spanish, Portuguese) or 2-way (French)
  - Indo-Aryan: Mandatory - 3-way (Hindi, Tamil, Telugu)
  - Slavic: Mandatory - 2-way (Russian)
  - Germanic: Mandatory (English) to Optional (German uses adverbs)
- **Japonic**: Mandatory - 3-way person-oriented (Japanese: kore/sore/are)
- **Sino-Tibetan**: Mandatory - 2-way (Mandarin: 这/那)

**Key Distinction**: **Person-Oriented** (near speaker vs. near listener vs. remote) vs. **Distance-Oriented** (proximal vs. distal).

[See full language analysis →](research/LANGUAGES.md)

## Translation Examples

### ✅ High-Stakes Theological Context

**John 1:29** - "Behold the Lamb of God"

| Language | Demonstrative | TBTA Value | Notes |
|----------|---------------|------------|-------|
| English | "the" (article) | S (Near Speaker) | Distance unmarked in English |
| Spanish | "ese" (medial) | L (Near Listener) | Jesus approaching, visible |
| Japanese | それ (sore) | L (Near Listener) | Middle distance, visible |
| Tagalog | iyan (near you) | L (Near Listener) | Person-oriented: near addressee |

**Theological Import**: Correct demonstrative shows Jesus is visible, identifiable, approaching - not distant or inaccessible. ✅ Medium stakes for Christology.

---

**Luke 24:39** - "See my hands and my feet"

| Language | TBTA Value | Critical? |
|----------|------------|-----------|
| All languages | S (Near Speaker) | **✅ CRITICAL** |

**Why Critical**: Body parts are maximally proximal to speaker (Jesus). Remote or Near Listener demonstrative would:
- Imply vision/apparition (not physical body)
- Weaken resurrection evidence
- ❌ **FORBIDDEN**: Any distant demonstratives

---

### ⚠️ Person-Oriented Language Challenge

**English "that"** is ambiguous:
- Could mean "near you" (addressee) → L
- Could mean "far from both" → R

**Solution**: TBTA distinguishes L vs. R, allowing Japanese (sore vs. are), Spanish (ese vs. aquel), Hindi (vah vs. vo) to select correctly.

## TBTA Encoding Details

**Position**: Character 8 in noun semantic string

**Format**: `N-{complexity}{sense}{index}{Number}{ParticipantTracking}{Polarity}{Proximity}{Future}{Person}{SurfaceRealization}{ParticipantStatus}........`

**Example**: `N-1A1SDAnK3NN........`
- Position 8 = `n` → "Not Applicable"

**Example**: `N-1A3SDAsK2NN........`
- Position 8 = `s` → Would be "Near Speaker" (lowercase 's' in encoding, uppercase 'S' in JSON export)

**Gateway Rule**: `Part of Speech = Noun` → Proximity evaluated; otherwise → `n`

[See full TBTA documentation →](research/TBTA.md)

## Development Status

**Stage**: 1 - Research & Definition ✅ **COMPLETE**

**Completed**:
- ✅ TBTA documentation review ([TBTA.md](research/TBTA.md))
- ✅ Scholarly research: 25+ sources ([SCHOLARLY.md](research/SCHOLARLY.md))
- ✅ Language family analysis: 1,008 languages ([LANGUAGES.md](research/LANGUAGES.md))
- ✅ Theological classification ([THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml))
- ✅ Research summary ([research/README.md](research/README.md))

**Next Stage**: 2 - Generate Test Set with Translation Data

[See complete research findings →](research/README.md)

## Critical Warnings

### **FORBIDDEN** Demonstrative Choices (Theologically)

| Verse | Forbidden Value | Why Heretical/Wrong |
|-------|----------------|---------------------|
| Luke 24:39 | Remote, Near Listener | Contradicts physical bodily resurrection |
| Heb 1:2 | Temporally Remote | Makes Christ's revelation seem past, not present era |
| Acts 1:11 | Remote Visible | Obscures identity: SAME Jesus will return |

### **Preferred** Demonstrative Choices (High Stakes)

| Verse | Preferred Value | Doctrinal Significance |
|-------|----------------|------------------------|
| Gen 1:26 "Let us" | Near Speaker and Listener (N) | Trinity unity, not separation |
| John 1:29 | Near Speaker (S) or Near Listener (L) | Christ visible, accessible |
| Luke 24:39 | Near Speaker (S) | Physical resurrection evidence |

## Research Highlights

**Cross-Linguistic**:
- 54% of languages use 2-way systems (WALS)
- 38% use 3-way systems (person vs. distance oriented)
- 8% use 4+ way systems (rare)
- Yupik: extreme outlier with 29-way system (elevation × direction × visibility × motion)

**Biblical Corpus**:
- ~5,000+ verses with proximity marking (estimated, across 11,649 TBTA verses)
- 90-95% arbitrary (stylistic choices)
- 5-10% non-arbitrary (theological or critical contextual significance)
- High stakes: ~1-2% (Trinity, Christology, Resurrection, Eschatology)

**Source Languages**:
- Hebrew: 2-way morphological (זֶה/הַהוּא)
- Greek: 2-3 way (οὗτος/ἐκεῖνος/ὅδε, Koine typically 2-way)
- TBTA extends beyond morphology → **contextual inference required**

[See full scholarly research →](research/SCHOLARLY.md)

## Resources

- **Research Summary**: [research/README.md](research/README.md)
- **TBTA Documentation**: [research/TBTA.md](research/TBTA.md)
- **Scholarly Sources**: [research/SCHOLARLY.md](research/SCHOLARLY.md)
- **Language Analysis**: [research/LANGUAGES.md](research/LANGUAGES.md)
- **Theological Significance**: [research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)
- **Development Methodology**: [../STAGES.md](../STAGES.md)
