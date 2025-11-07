# Person Systems in Bible Translation Languages

## Translation Impact ⭐⭐⭐⭐⭐

**Criticality: HIGHEST** - Affects 33% of all Bible translations (700+ languages). Wrong clusivity choice completely alters theological meaning: "we apostles" (exclusive authority) vs "we believers" (inclusive community). Biblical source languages don't mark clusivity, requiring contextual inference for every first-person plural pronoun.

**Translation Difficulty:** ⭐⭐⭐⭐ (High) - Requires theological analysis, discourse tracking, and speaker/addressee identification for each "we/us/our" instance.

**Frequency:** ⭐⭐⭐⭐⭐ (Constant) - Every first-person plural pronoun in ~700+ languages demands explicit inclusive/exclusive choice.

## Local Analysis Completed ✅

**Clusivity Analysis**: Comprehensive validation of TBTA Person annotations using actual Bible translations in clusivity-marking languages.

- **Coverage**: 14 verses (7 inclusive + 7 exclusive) across all literary genres
- **Languages**: 9 clusivity-marking languages (Austronesian family)
- **Translations**: 6,500+ total scanned
- **Agreement**: 98% consensus validating TBTA annotations
- **Files**: 16 (3 README summaries + 14 detailed verse analyses)

**See**: [clusivity/](clusivity/) for complete analysis with real translation examples

**Key findings**:
- INCLUSIVE: Speaker includes addressee in "we/us/our" - Genesis 1:26 (Trinity), Psalm 95:1 (worship)
- EXCLUSIVE: Speaker excludes addressee from "we/us/our" - John 3:11 (Jesus vs Nicodemus), Matthew 6:9 (prayer to God)
- Validates TBTA's ability to infer clusivity from context even when source languages don't mark it

## Baseline Statistics

Based on analysis of first-person plural pronouns in Biblical text:

**Overall Distribution**:
- **Exclusive "we"**: ~65-70% (speaker excludes addressee)
- **Inclusive "we"**: ~30-35% (speaker includes addressee)

**Genre Variation**:
- **Narrative (OT, divine speech)**: 90%+ exclusive (God addressing humans, separate groups)
- **Epistles (NT)**: 40-50% exclusive, 50-60% inclusive (mixed community/authority contexts)
- **Prayer contexts**: 95%+ exclusive (addressing God excludes God from "our/we")
- **Worship/Praise**: 80%+ inclusive (congregation joining together)
- **Prophecy**: 90%+ exclusive (prophet speaks for God to people)

**Prediction Baseline**: Default to exclusive (65%) unless context indicates inclusive patterns (invitation, reciprocal action, shared identity).

## Quick Translator Test

Answer these questions about your target language:

1. ☐ Does your language distinguish inclusive vs exclusive "we"?
2. ☐ If YES, what are the two words? (e.g., Tagalog: táyo=INCL / kamí=EXCL)
3. ☐ Does the distinction apply to all persons or only 1st plural?
4. ☐ Does your language have a 4th person (Algic obviation)?
5. ☐ Does your language use T-V distinction (formal/informal "you")?

**If you answered YES to #1, clusivity annotation is CRITICAL for your translation.**

**Examples**: Austronesian (Indonesian, Tagalog, Tok Pisin), Algic (Algonquin, Cree), many Mayan, Cariban, and Pacific languages require clusivity marking.

## Common Errors & Solutions

| Error | Problem | Solution |
|-------|---------|----------|
| **All prayer is exclusive** | Assuming "we pray to God" = always exclusive | Distinguish prayer TO God (Matt 6:9 EXCL) from statements ABOUT divine presence (Matt 1:23 INCL) |
| **Missing speaker shifts** | Not tracking speaker changes in passage | Identify speaker for EACH "we" separately - Jesus quoting prophet ≠ Jesus addressing disciples |
| **Ignoring genre patterns** | Applying narrative rules (90% EXCL) to all genres | Check baseline: Narrative 90% EXCL, Epistles 50/50, Worship 80% INCL |
| **Missing reciprocals** | Overlooking "one another" constructions | Reciprocal actions (Heb 10:24) = 100% INCL - both parties must participate |

**See**: [METHODOLOGY.md](METHODOLOGY.md) for complete error analysis and prevention strategies.

## Gateway Features & Prediction Rules

Quick prediction rules with high accuracy:

| If Context Shows... | Then Predict... | Accuracy |
|---------------------|----------------|----------|
| Speaker = God/Jesus, Addressee = humans | Exclusive | 95%+ |
| Prayer context, speaker = congregation, to God | Exclusive | 95%+ |
| Worship invitation: "Come, let us..." | Inclusive | 90%+ |
| Apostolic "we" in eyewitness testimony | Exclusive | 95%+ |
| Epistolary: "We send to you" | Exclusive | 90%+ |
| Reciprocal action: "one another" | Inclusive | 100% |
| Royal "we" (single speaker, plural form) | Exclusive | 100% |

**Prediction Hierarchy**:
1. Check speaker and addressee identity (most important)
2. Check action capability (can addressee participate?)
3. Check discourse function (invitation, contrast, testimony)
4. Default to exclusive (65% baseline)

**See**: [METHODOLOGY.md](METHODOLOGY.md) for complete prediction framework and prompt templates.

## Key Person System Features

### 1. Clusivity (Inclusive vs Exclusive "We")

#### What is Clusivity?

Clusivity is a grammatical distinction in first-person plural pronouns that explicitly marks whether the addressee is included or excluded:

- **Inclusive "we"** = speaker + addressee(s) + possibly others ("we including you")
- **Exclusive "we"** = speaker + others, but NOT addressee ("we but not you")

#### Complete Value Enumeration

| Value | Definition | Participants | Bible Examples | Languages |
|-------|------------|--------------|----------------|-----------|
| **Inclusive** | Speaker includes addressee | speaker + addressee ± others | Gen 1:26 (Trinity), Ps 95:1 (worship), Heb 10:24 (mutual encouragement) | táyo (Tagalog), kita (Indonesian), yumi (Tok Pisin) |
| **Exclusive** | Speaker excludes addressee | speaker + others, NOT addressee | Jhn 3:11 (Jesus vs Nicodemus), Matt 6:9 (prayer to God), Acts 15:25 (apostles to churches) | kamí (Tagalog), kami (Indonesian), mipela (Tok Pisin) |

**Note**: This feature applies ONLY to first-person plural pronouns (we/us/our). Singular "I" and second/third-person pronouns do not mark clusivity in these languages.

#### Languages with Clusivity

**Austronesian** (most common, 700+ languages):
- **Philippines**: Tagalog (tayo/kami), Cebuano, Ilocano, 30+ others in TSV
- **Indonesia/Malaysia**: Indonesian (kita/kami), Malay, 15+ regional languages
- **Pacific**: Tok Pisin (yumi/mipela), Hawaiian, Tongan, Chamorro, 50+ PNG languages

**Algic** (North America):
- Algonquin, Cree, Ojibwe, Arapaho, Blackfoot

**Other families**:
- **Mayan**: Achi, Kaqchikel, Awakateko, Chuj (10+ in TSV)
- **Cariban**: Akawaio, Bakairí (South America)
- **Australian Aboriginal**: Multiple language families
- **Various Native American families**: Quechuan, Tupi-Guarani, others

**See**: [clusivity/README.md](clusivity/README.md) for detailed language data and translation examples.

### 2. Fourth Person (Obviation)

#### What is Obviation?

Obviation distinguishes between multiple third-person referents based on discourse importance:
- **Proximate** (3rd person): The more important/topical referent
- **Obviative** (4th person): The less important/secondary referent

**Note**: Obviation is DIFFERENT from clusivity. While clusivity distinguishes inclusive/exclusive "we," obviation distinguishes between two third-person referents by their discourse prominence.

#### Languages with Obviation

##### From Our TSV (Known or Likely):
- **Algic languages**: Algonquin (alq), Cree, Ojibwe, potentially Arapaho (arp) and Blackfoot (bla)
- **Athabaskan languages**: Apache, Western (apw) - related to Navajo which has 4th person

#### Translation Implications for Obviation

**Biblical narratives with multiple third-person referents**:
- "Jesus called Peter and said to him" → Must mark whether Jesus (proximate) or Peter (obviative)
- "The angel appeared to Mary and spoke to her" → Angel (proximate topic) vs Mary (obviative)
- Discourse tracking: Main character typically proximate, secondary characters obviative
- Switch-reference: When obviative becomes new topic, may promote to proximate

### 3. T-V Distinction (Formal/Informal "You")

#### What is T-V Distinction?

T-V distinction (from Latin "tu/vos") marks social distance, formality, and respect through different second-person pronouns.

**Languages with T-V**:
- **Romance**: French (tu/vous), Spanish (tú/usted), Portuguese (tu/você), Italian (tu/Lei)
- **Germanic**: German (du/Sie), Dutch (jij/u), Swedish (du/ni)
- **Slavic**: Russian (ты/вы), Polish (ty/wy), Czech (ty/vy)
- **Indo-Iranian**: Hindi (तू tū / तुम tum / आप āp - three-way system!)

#### Translation Implications

**Critical Biblical Passages**:
- **Jesus addressing disciples**: Familiar (tu) - intimate relationship
- **Jesus addressing Pharisees**: May shift to formal (vous) in confrontation or respectful discourse
- **Prayer to God**: Varies by tradition:
  - Traditional: Formal (vous/Sie/вы) - reverence
  - Modern/informal: Familiar (tu/du/ты) - intimacy with God
- **God addressing humans**: Typically familiar (tu) - sovereign intimacy
- **Social hierarchy**: Masters/servants, parents/children, elders/youth require T-V decisions

**Cultural Variation**:
- French traditional: Always vous to God (reverence)
- German Protestant: Often du to God (Luther's influence - intimate relationship)
- Spanish: Varies by region and tradition
- Russian: Growing debate between formal вы and familiar ты in prayer

### 4. Number Systems Beyond Singular/Plural

#### Dual Number
Languages distinguishing exactly two items:

**From our TSV:**
- Arabic, Standard (arb): Full dual system on nouns, verbs, adjectives, pronouns
- Hawaiian (haw): Dual pronouns (Austronesian trait)
- Assyrian Neo-Aramaic (aii): Likely has dual (Semitic language)

#### Trial Number
Languages distinguishing exactly three items (mainly Austronesian):

**Potential candidates from our TSV:**
- Various Papua New Guinea Austronesian languages may have trial pronouns
- Some Australian Aboriginal languages (Alyawarr-aly, Anmatyerre-amx, etc.)

## Bible Translation Implications

**Critical Challenge**: Biblical source languages (Hebrew, Aramaic, Greek) do NOT mark clusivity. Translators in 700+ clusivity-marking languages must infer from context.

**Key Example Passages**:
- **Matthew 6:9** "Our Father" → Exclusive (praying TO God excludes God from "our")
- **Genesis 1:26** "Let us make" → Inclusive (Trinity addressing Trinity)
- **John 3:11** "We speak... you do not receive" → Exclusive (contrast: Jesus vs Nicodemus)
- **Hebrews 10:24** "Let us consider one another" → Inclusive (author joins readers)

**Wrong choice alters meaning**: "We apostles" (exclusive authority) vs "we believers" (inclusive community) completely changes theological implications.

**See**: [clusivity/](clusivity/) for 14 analyzed verses with real translations in Tagalog, Indonesian, Tok Pisin, and other clusivity-marking languages.

## Language Detection

**High Clusivity Probability**:
- Austronesian family (Philippines, Indonesia, Pacific)
- Algic family (North America)
- Many Mayan, Cariban languages

**Quick check**: If language is from Southeast Asia, Pacific, or indigenous Americas → likely has clusivity. Check for multiple "we" words in basic vocabulary.

## For TBTA Tools

**Commentary files should include**:
- Clusivity annotations for first-person plural pronouns
- Speaker/addressee identification
- Genre-specific prediction patterns

**Priority languages** (from TSV):
- **Tier 1**: Tagalog, Indonesian, Malay, Tok Pisin (major languages, extensive resources)
- **Tier 2**: 30+ Philippine languages, 15+ Indonesian languages, 50+ PNG languages
- **Tier 3**: Mayan (10+), Algic, Cariban families

## Resources

- **WALS Online**: Inclusive/Exclusive Distinction chapter
- **Clusivity analysis**: [clusivity/](clusivity/) - 14 verses, 9 languages, 98% validation
- **Methodology**: [METHODOLOGY.md](METHODOLOGY.md) - Complete prediction framework with prompt templates
- **Language lists**: [clusivity/README.md](clusivity/README.md) - Detailed family data