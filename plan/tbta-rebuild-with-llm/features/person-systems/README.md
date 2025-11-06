# Person Systems in Bible Translation Languages

## Executive Summary

Person systems vary dramatically across languages, with many languages in our TSV file exhibiting features like clusivity (inclusive/exclusive distinctions), obviation (fourth person), and complex number systems (dual, trial). These grammatical distinctions have significant implications for Bible translation accuracy and theological meaning.

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

## Key Person System Features

### 1. Clusivity (Inclusive vs Exclusive "We")

#### What is Clusivity?

Clusivity is a grammatical distinction in first-person plural pronouns that explicitly marks whether the addressee is included or excluded:

- **Inclusive "we"** = speaker + addressee(s) + possibly others ("we including you")
- **Exclusive "we"** = speaker + others, but NOT addressee ("we but not you")

#### Languages with Clusivity from Our List

##### Austronesian Languages (Most Common)
From our TSV file, the following Austronesian languages likely have clusivity:

**Philippines:**
- Tagalog (tgl): tayo (inclusive) vs kami (exclusive)
- Inabaknon (abx)
- Agutaynen (agn)
- Atta, Pamplona (att)
- Binukid (bkd)
- Blaan varieties (bpr, bps)
- Tagabawa (bgs)
- Manobo, Ata (atd)
- Agta, Central Cagayan (agt)

**Indonesia:**
- Indonesian (ind): kita (inclusive) vs kami (exclusive)
- Malay varieties (zlm): kita (inclusive) vs kami (exclusive)
- Amarasi (aaz)
- Alune (alp)
- Ambai (amk)
- Balantak (blz)

**Papua New Guinea (Austronesian):**
- Multiple languages including: Miniafia Oyan (aai), Adzera (adz), Arosi (aia), and others

**Solomon Islands:**
- Arosi (aia), Sa'a (apb), Bughotu (bgt), and others

##### Algic Languages
From our TSV file:
- Algonquin (alq): Has inclusive/exclusive distinction
- Arapaho (arp): Likely has clusivity (Algic family trait)
- Blackfoot (bla): Likely has clusivity

**Ojibwe/Anishinaabemowin examples (not in our list but related):**
- giinawind = inclusive "we"
- niinawind = exclusive "we"

**Cree examples (related language):**
- niyanân = inclusive "we"
- kiyânaw = exclusive "we"

##### Mayan Languages
From our TSV file, these Mayan languages may have clusivity:
- Achi (acr)
- Kaqchikel (cak)
- Awakateko (agu)
- Chuj (cac)
- Ch'orti' (caa)

Note: While Mayan languages have complex pronoun systems, explicit documentation of inclusive/exclusive distinctions is limited.

##### Cariban Languages
From our TSV file:
- Akawaio (ake)
- Bakairí (bkq)

Cariban languages show suppletive patterns where the exclusive form (like "anna" in Macushí) is phonologically unrelated to other pronouns.

### 2. Fourth Person (Obviation)

#### What is Obviation?

Obviation distinguishes between multiple third-person referents based on discourse importance:
- **Proximate** (3rd person): The more important/topical referent
- **Obviative** (4th person): The less important/secondary referent

#### Languages with Obviation

##### From Our TSV (Known or Likely):
- **Algic languages**: Algonquin (alq), potentially Arapaho (arp) and Blackfoot (bla)
- **Athabaskan languages**: Apache, Western (apw) - related to Navajo which has 4th person

### 3. Number Systems Beyond Singular/Plural

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

### Critical Translation Challenges

1. **Ambiguous Greek/Hebrew "We"**
   - Source languages lack clusivity distinctions
   - Translators must interpret context to choose inclusive vs exclusive
   - Wrong choice can alter theological meaning

2. **Example Passages Requiring Clusivity Decisions:**

   a) **Lord's Prayer (Matthew 6:9)**
   - "Our Father" - Is this inclusive of all believers or exclusive to disciples?
   - Languages with clusivity must choose

   b) **Paul's Epistles**
   - "We are ambassadors for Christ" (2 Cor 5:20)
   - Exclusive = "we apostles" vs Inclusive = "we believers"

   c) **Jesus to Disciples**
   - "We must work the works of him who sent me" (John 9:4)
   - Does Jesus include the disciples or not?

3. **Obviation Challenges**
   - Determining discourse prominence between biblical characters
   - Maintaining reference tracking across long narratives
   - Example: In stories with multiple third-person characters (Jesus, disciples, Pharisees)

### Real Translation Examples

**Tagalog (Philippines):**
- Must distinguish between tayo (inclusive) and kami (exclusive)
- Critical in passages about church unity vs apostolic authority

**Indonesian/Malay:**
- kita vs kami distinction affects interpretation of community texts
- Particularly important in Acts and Epistles

**Algonquian languages:**
- Complex person systems with both clusivity and obviation
- Requires careful tracking of discourse participants

## Predicting/Detecting Clusivity Needs

### Language Family Indicators

**High Probability of Clusivity:**
1. **Austronesian languages** (especially Philippines, Indonesia, Pacific)
2. **Australian Aboriginal languages**
3. **Many Native American language families:**
   - Algic (Algonquian)
   - Some Mayan languages
   - Cariban languages
   - Various South American families

**Lower Probability:**
1. Indo-European languages (except some Indo-Aryan)
2. Sino-Tibetan languages (with exceptions)
3. Most African language families (with regional exceptions)

### Geographic Patterns

**Clusivity Hotspots:**
- Southeast Asia (Philippines, Indonesia, Malaysia)
- Pacific Islands
- Northern Australia
- North American indigenous regions (especially Great Lakes, Plains)
- Parts of South America

### Quick Detection Method

For any language in our TSV:
1. Check language family - Austronesian = likely clusivity
2. Check geographic region - Southeast Asia/Pacific = likely
3. Look for multiple "we" pronouns in basic vocabulary
4. Check related languages in same family

## Implications for TBTA Project

### Data Structure Considerations

Commentary files should accommodate:
1. **Clusivity annotations** where relevant
2. **Obviation tracking** for narrative texts
3. **Number system notes** (dual/trial) where applicable

### Tool Development Needs

1. **Pronoun analysis tools** that flag ambiguous "we" in source texts
2. **Context extractors** to help determine inclusive vs exclusive intent
3. **Cross-reference systems** linking similar clusivity decisions

### Priority Languages for Special Attention

Based on our TSV file, prioritize person-system analysis for:

**Tier 1 (Known Clusivity):**
- Tagalog, Indonesian, Malay
- Algonquin
- Hawaiian

**Tier 2 (Likely Clusivity):**
- Philippine languages (30+ in list)
- Indonesian regional languages (15+ in list)
- Papua New Guinea Austronesian languages (50+ in list)
- Mayan languages (10+ in list)

**Tier 3 (Complex Person Systems):**
- Arabic (dual number)
- Native American languages
- Australian Aboriginal languages

## Sources and References

1. Wikipedia: Clusivity - https://en.wikipedia.org/wiki/Clusivity
2. WALS Online - Chapter on Inclusive/Exclusive Distinction
3. APiCS Online - Parameters for Creole clusivity patterns
4. Language-specific grammars and linguistic descriptions
5. Bible translation forums and discussions on pronoun challenges
6. Academic papers on obviation and person systems

## Next Steps

1. Develop language-specific person system profiles
2. Create clusivity decision matrices for common biblical passages
3. Build automated detection tools for person-system features
4. Compile translation best practices for clusivity handling
5. Document theological implications of person-system choices