# Trans-New Guinea Language Family

## Overview

Trans-New Guinea (TNG) is one of the world's largest language families, with probable membership of 300-500 languages, making it possibly the third-largest language family by number of languages. [Pawley & Hammarström 2018]

**Dataset Coverage**: 129 unique TNG languages represented in our myBibleToolbox dataset (from languages.tsv)

**Geographic Distribution**:
- **Primary location**: Papua New Guinea (vast majority)
- **Secondary locations**: Indonesia (West Papua/Papua provinces)
- **Region**: Primarily the interior highlands and mountains of New Guinea island

## TBTA Translation Features

Features unique to Trans-New Guinea languages that require translation decisions not explicit in Greek/Hebrew source texts.

### Switch-Reference - ESSENTIAL

**Present in**: Nearly all 129 languages (universal feature)
**Pattern**: Medial verbs marked for same-subject (SS) vs different-subject (DS)
**Dominant example - Amele**:
- Same-subject: `-en` suffix (next clause has same subject)
- Different-subject**: `-ig` suffix (next clause has different subject)

**Biblical translation examples**:
- **Mark 1:9** "Jesus came from Nazareth and was baptized" → Same-subject (Jesus...Jesus)
- **Mark 1:10** "As Jesus came up, he saw heaven torn open" → Same-subject (Jesus...he)
- **Mark 1:11** "A voice came from heaven: 'You are my Son'" → Different-subject (Jesus...voice)

**Translation impact**: Every narrative sentence requires analyzing who does the next action. Maintains participant tracking automatically through verb morphology.

### Evidentiality - ESSENTIAL (Highlands only)

**Present in**: ~14 Highlands languages (Fasu, Dani, Yali, Kobon, etc.)
**Absent in**: Lowland languages (~115 languages)
**Dominant example - Fasu**:
- Visual evidential: `a-...-re` (I saw it happen)
- Reported: unmarked or narrative markers
- Inferred: separate particles

**Biblical translation examples**:
- **Luke 2:10** "I bring you good news" → Visual (angel speaking) or divine knowledge marker
- **Acts 1:3** "He appeared to them" → Visual (apostles witnessed)
- **Hebrews 11:1** "Faith is confidence" → Generic/gnomic (not witnessed)
- **All prophecy** → Reported or divine revelation marker

**Translation impact**: Cannot translate without deciding information source. Testimonial passages (Gospels, Acts) need visual markers. Epistles need generic/gnomic markers.

**Variants**: Some languages have 2-way systems, others have 3+ distinctions (visual/auditory/inferred/reported).

### Dual Number - CRITICAL

**Present in**: Very common across family
**Dominant examples**:
- **Mian, Telefol**: Pronouns and verbs mark dual
- **Wantoat**: Singular/dual/plural in pronouns

**Biblical translation examples**:
- **Luke 24:13** "Two of them" → Dual pronouns/verbs
- **Acts 13:2** "Barnabas and Saul" → Dual throughout passage
- **Genesis 1:27** "Male and female" → Dual or plural depending on focus

### Elevation Deixis - CRITICAL (Some languages)

**Present in**: Various languages with topographical sensitivity
**Pattern**: Verbs mark uphill/downhill/level motion
**Example pattern**:
- "Go up" = motion toward mountains/higher ground
- "Go down" = motion toward lowlands/coast
- "Go across" = level motion

**Biblical translation examples**:
- **Luke 10:30** "Going down from Jerusalem to Jericho" → Downhill marker (Jerusalem is higher)
- **Luke 2:4** "Joseph went up to Judea, to Bethlehem" → Uphill marker
- **Matthew 17:1** "Jesus led them up a high mountain" → Uphill marker

**Variants**: Some languages grammaticalize elevation, others use lexical verbs.

## Key Typological Features

Trans-New Guinea languages share significant typological characteristics that create unique challenges and opportunities for Bible translation:

### Core Grammatical Profile

1. **Word Order**: Subject-Object-Verb (SOV) - opposite of Greek/Hebrew
2. **Clause Chaining**: Medial vs. final verb distinctions with switch-reference systems
3. **Verb Morphology**: Complex, with object prefixes and subject suffixes
4. **Case Systems**: Often ergative-absolutive on nouns, nominative-accusative in verbs
5. **Number**: Dual number (two) is very common
6. **TAM Marking**: Multiple past tense distinctions (today's, yesterday's, remote)
7. **Serial Verbs**: Extremely productive to compensate for small verb inventories

### Regionally Concentrated Features

**The Highlands Evidentiality Area**: At least 14 languages with grammatical evidentiality marking information source (visual, sensory, inferential, reportive, etc.). Critical for Bible translation.

**Elevation-based Spatial Systems**: Uphill/downhill distinctions grammaticalized in motion verbs and spatial reference.

## Classification

The most recent comprehensive classification [Pawley & Hammarström 2018] accepts **35 subgroups** with strong claims to TNG membership. Major groups include:

- **Madang** (~80+ languages) - Largest by language count
- **Finisterre-Huon** (~60-65 languages)
- **Kainantu-Goroka** (Eastern Highlands)
- **Enga-Kewa-Huli** (Engan) - 400,000+ speakers
- **Ok-Oksapmin** - Evidentiality area
- **Angan** (~12 languages)
- **Binandere** (~14 languages)
- Many smaller families

See [classification.md](classification.md) for complete 35-subgroup list and methodology.

## Translation Priorities

### High-Priority Features for Bible Translation

1. **Clause Chaining** - Narrative restructuring required
2. **Evidentiality** (in ~14 languages) - Mark information source for every statement
3. **Dual Number** - Important for pairs in Scripture
4. **Multiple Past Tenses** - Temporal precision needed
5. **Ergative Case** - Agent-patient relations
6. **Serial Verbs** - Causatives, benefactives, complex events
7. **Spatial Deixis** - Elevation marking for "go up/down"
8. **Possession** - Alienable/inalienable distinction

### Key Translation Challenges

**Discourse Restructuring**: SOV order and clause chaining require complete restructuring from Greek/Hebrew coordinate clauses.

**Information Addition**: Evidential systems may require adding information absent in source text (e.g., marking prophetic statements as divine revelation).

**Morphological Complexity**: Large verbal paradigms create learning difficulty; poor documentation for many languages.

**Limited Verb Lexicons**: Small verb root inventories (some as few as 60) require creative serial constructions to match Greek/Hebrew semantic richness.

## Documentation Structure

This research is organized into the following files:

- **README.md** (this file) - Overview and key findings
- **[language-list.md](language-list.md)** - Complete list of 129 languages in dataset
- **[classification.md](classification.md)** - 35 subgroups and proto-TNG reconstructions
- **[grammatical-features-part1.md](grammatical-features-part1.md)** - Verb systems, word order, case, number, serial verbs, TAM
- **[grammatical-features-part2.md](grammatical-features-part2.md)** - Evidentiality, spatial systems, possession, discourse, quotatives
- **[translation-guide.md](translation-guide.md)** - Translation considerations and recommendations
- **[sub-families.md](sub-families.md)** - Individual sub-family characteristics
- **[sources.md](sources.md)** - Complete bibliography and citations

## Quick Facts

- **Languages in dataset**: 129
- **Total family size**: 300-500 languages (estimates vary)
- **Major subgroups**: 35 [Pawley & Hammarström 2018]
- **Speaker populations**: Range from a few hundred to 400,000+ (Enga)
- **Countries**: Papua New Guinea, Indonesia
- **Typology**: SOV, head-marking, polysynthetic to isolating
- **Evidentiality**: ~14 languages (Highlands area)
- **Documentation**: Variable - some well-documented, many poorly described

## Key Insight for Bible Translation

The Trans-New Guinea family exhibits remarkable consistency in core typological features (SOV, clause chaining, complex verb morphology) while showing substantial variation in specific implementations. Bible translators must:

1. Understand the **general TNG profile** (this overview)
2. Identify the **specific sub-family** features (sub-families.md)
3. Document the **individual language's system** through fieldwork
4. Apply **TNG-appropriate translation strategies** (translation-guide.md)

The most critical feature for translation is the **clause chaining system with switch-reference**, which affects virtually every narrative passage in Scripture. In languages with evidentiality, marking information source becomes equally critical.

## Comparison with Other Families

Trans-New Guinea shares features with:
- **Other SOV families** (Turkish, Japanese, Korean) - word order, postpositions
- **Ergative families** (Mayan, Georgian, Basque) - case marking patterns
- **Evidential families** (Tibetan, Quechan, Cherokee) - information source marking
- **Polysynthetic families** (Mohawk, Greenlandic) - complex verbal morphology

However, the combination of clause chaining, switch-reference, and (in Highlands) evidentiality creates a unique grammatical profile not fully paralleled elsewhere.

## Research Status

- **Primary classification source**: Pawley & Hammarström (2018)
- **Document prepared**: 2025-11-05
- **Research method**: Web-based academic literature review
- **Documentation quality**: Variable across languages

Many TNG languages remain poorly documented. Ongoing linguistic research is necessary alongside translation work.

## Conclusion

The Trans-New Guinea language family represents one of the world's most linguistically diverse and typologically distinctive families. With 129 languages in our dataset spanning 35 major subgroups, careful attention to both shared typological features and language-specific variation is essential for effective Bible translation work.

The extensive morphological variation and discourse-level grammatical features make TNG languages particularly challenging for translators from Indo-European backgrounds but offer rich opportunities for culturally natural translation that leverages the grammatical resources these languages provide.

---

*For detailed information on any topic, consult the specialized files listed above.*
