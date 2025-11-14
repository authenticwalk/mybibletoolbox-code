# Quick Reference: Person Systems in Key Languages

## Top Priority Languages with Clusivity

### Major Languages (Millions of Speakers)

| Code | Language | Family | Country | Inclusive | Exclusive | Books | Notes |
|------|----------|--------|---------|-----------|-----------|-------|-------|
| **ind** | Indonesian | Austronesian | Indonesia | kita | kami | 33 | 200M+ speakers |
| **tgl** | Tagalog | Austronesian | Philippines | tayo | kami | 66 | 20M+ speakers |
| **zlm** | Malay | Austronesian | Malaysia | kita | kami | 27 | 30M+ speakers |
| **haw** | Hawaiian | Austronesian | United States | kākou | mākou | 66 | Dual pronouns also |

### Indigenous American Languages

| Code | Language | Family | Country | Clusivity | Obviation | Books | Notes |
|------|----------|--------|---------|-----------|-----------|-------|-------|
| **alq** | Algonquin | Algic | Canada | Yes | Yes | 27 | 4th person system |
| **arp** | Arapaho | Algic | United States | Likely | Likely | 1 | Limited texts |
| **bla** | Blackfoot | Algic | Canada | Likely | Likely | 1 | Limited texts |
| **ake** | Akawaio | Cariban | Guyana | Likely | Unknown | 27 | Cariban patterns |
| **bkq** | Bakairí | Cariban | Brazil | Likely | Unknown | 27 | Cariban patterns |

### Philippine Languages (All Austronesian)

| Code | Language | Books | Likely Pattern |
|------|----------|-------|----------------|
| **abx** | Inabaknon | 27 | tayo/kami pattern |
| **agn** | Agutaynen | 27 | tayo/kami pattern |
| **att** | Atta, Pamplona | 27 | tayo/kami pattern |
| **bkd** | Binukid | 27 | tayo/kami pattern |

### Indonesian Regional Languages

| Code | Language | Region | Books | Likely Pattern |
|------|----------|--------|-------|----------------|
| **aaz** | Amarasi | Indonesia | 28 | kita/kami pattern |
| **alp** | Alune | Indonesia | 27 | kita/kami pattern |
| **amk** | Ambai | Indonesia | 27 | kita/kami pattern |

## Key Patterns by Language Family

### Austronesian Pattern
- **Inclusive:** Includes addressee ("we including you")
- **Exclusive:** Excludes addressee ("we but not you")
- **Coverage:** Nearly 100% of Austronesian languages
- **Forms:** Usually two distinct words, not morphological variants

### Algic Pattern
- **Clusivity:** Clear inclusive/exclusive distinction
- **Obviation:** Proximate vs. obviative third person
- **Complex:** Often 14+ person distinctions total
- **Verbal:** Marked on both pronouns and verbs

### Cariban Pattern
- **Exclusive:** Often suppletive (unrelated form)
- **Structural:** May not control plural agreement
- **Variable:** Patterns vary across family

## Languages Needing Investigation

From our TSV, these language families need more research:

### Mayan Languages (10+ in list)
- Achi (acr) - 3 versions
- Kaqchikel (cak) - 6 versions
- Awakateko (agu)
- Chuj (cac)
- Ch'orti' (caa)

### Trans-New Guinea (50+ in list)
- Large family with variable features
- Many PNG languages
- Documentation varies

### Australian Languages
- Alyawarr (aly)
- Anmatyerre (amx)
- Arrernte, Eastern (aer)
- Often have complex person systems

## Translation Statistics

### Coverage Analysis
- **Total languages in TSV:** ~600
- **Confirmed clusivity:** 17 (documented above)
- **Probable clusivity (Austronesian):** ~150
- **Probable clusivity (other):** ~50
- **Total affected:** ~200+ languages (33% of translations)

### Bible Book Coverage
- **Full Bible (66 books):** tgl, haw, ind (partial)
- **NT + portions (27-35 books):** Most languages
- **NT only (27 books):** Standard minimum
- **Limited (<10 books):** arp, bla, some Australian

## Decision Framework

### For Translators

**High Confidence Inclusive:**
- Community statements
- Universal prayers
- Shared faith experiences
- Invitations to participate

**High Confidence Exclusive:**
- Apostolic eyewitness claims
- Historical narratives with specific participants
- Role-based distinctions
- Group-specific references

**Requires Context Analysis:**
- Paul's letters (voice ambiguity)
- Jesus' teachings (audience layers)
- Prophetic passages (speaker identity)
- Wisdom literature (universal vs. specific)

## Data Collection Priorities

### Tier 1: Document Immediately
1. Indonesian (ind) - Massive speaker base
2. Tagalog (tgl) - Major Philippine language
3. Malay (zlm) - Regional lingua franca
4. Algonquin (alq) - Complex person system

### Tier 2: Research Needed
1. All Philippine Austronesian languages
2. All Indonesian regional languages
3. Mayan language family
4. Cariban languages

### Tier 3: Long-term Goals
1. Trans-New Guinea languages
2. Australian Aboriginal languages
3. Other Native American families
4. African languages with person features

## Integration with TBTA

### Required Data Fields
```yaml
pronouns:
  first_person:
    singular: [form]
    dual_inclusive: [if exists]
    dual_exclusive: [if exists]
    plural_inclusive: [form]
    plural_exclusive: [form]
  obviative_marking: [yes/no]
  number_systems: [singular, dual, trial, plural]
```

### Commentary Requirements
- Mark all pronoun ambiguities
- Document clusivity decisions
- Note alternative interpretations
- Cross-reference similar passages

### Tool Development
- Pronoun analyzer for source texts
- Clusivity consistency checker
- Family-based prediction system
- Decision documentation interface