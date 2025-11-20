# TBTA Feature Mapping for Language Families

## Objective

Systematically map all 57 TBTA features to language families, highlighting features that DON'T exist in Greek/Hebrew but are OBLIGATORY in target languages.

## Problem Statement

Current language family documentation describes grammatical features broadly, but doesn't systematically answer:
- **Which TBTA features are critical vs irrelevant for each family?**
- **Which features require translator decisions that aren't in the source text?**
- **How do dominant languages solve these issues (as reference)?**
- **Which minor languages have unique requirements?**

## Critical TBTA Features NOT in Greek/Hebrew

### Definitional Scope
Greek/Hebrew have: Person (1/2/3), Number (Sg/Pl), basic tense, basic mood, cases, gender
Target languages ADD: Features below are **decision points** for translators

### Features Requiring Translator Decisions

#### 1. Person Systems (CRITICAL)
**Not in source**: Clusivity (inclusive/exclusive "we")
- **Austronesian**: Universal (172 languages) - kita/kami distinction
- **Algic**: Obviation (4th person) - Ojibwe, Cree
- **Dravidian**: Clusivity common
- **Indo-European**: T-V distinctions (tu/vous) - French, German, Spanish, Russian
- **Examples**: "Let us make" (Gen 1:26) - inclusive or exclusive?

#### 2. Number Systems (CRITICAL)
**Not in source**: Dual, Trial, Paucal
- **Austronesian-Oceanic**: Dual/Trial widespread - Samoan, Hawaiian, Fijian
- **Semitic**: Dual preserved - Arabic (all varieties)
- **Slavic**: Dual rare - Slovenian, Sorbian (only 2 in dataset!)
- **Examples**: "Two disciples" - Greek plural → target dual?

#### 3. Evidentiality (CRITICAL)
**Not in source**: Information source marking (visual/reported/inferred)
- **Trans-New Guinea Highlands**: Obligatory in ~50 languages
- **Quechuan**: 3-way system (direct/reported/inferred)
- **Tucanoan**: 5-way system (most complex)
- **Examples**: "Jesus rose" - witnessed or reported?

#### 4. Switch-Reference (CRITICAL)
**Not in source**: Same/different subject marking
- **Trans-New Guinea**: Nearly universal - medial verbs
- **Uto-Aztecan**: Common
- **Examples**: "He came and sat down" - same subject marker required

#### 5. Honorifics/Register (CRITICAL)
**Not in source**: Age, social status, formality levels
- **Japanese**: 5+ politeness levels
- **Korean**: 6 speech levels
- **Javanese**: 3 register systems
- **Thai**: Royal language vs common
- **Examples**: All Jesus quotes require honorific decision

#### 6. Voice/Focus Systems (CRITICAL)
**Not in source**: Philippine-type voice systems
- **Philippine Austronesian**: 4-voice obligatory - Tagalog, Cebuano, Ilokano
- **Western Austronesian**: 2-voice - Indonesian, Malay
- **Examples**: "God created" - actor focus or patient focus?

#### 7. Noun Classes (CRITICAL)
**Not in source**: 10-20 class agreement
- **Niger-Congo Bantu**: 10-20 classes obligatory
- **Examples**: Abstract concepts ("word", "faith") require class assignment

#### 8. Topic Marking (CRITICAL)
**Not in source**: Explicit topic particles
- **Japanese**: wa/ga distinction
- **Korean**: eun/neun vs i/ga
- **Mandarin**: Topic-comment structure
- **Examples**: Every sentence requires topic decision

#### 9. Classifiers (CRITICAL)
**Not in source**: Numeral/possessive classifiers
- **Mayan**: Shape/function classifiers obligatory
- **Sino-Tibetan**: Numeral classifiers
- **Examples**: "Twelve tribes" requires classifier choice

#### 10. Proximity Systems (CRITICAL)
**Not in source**: 3+ way demonstratives
- **Japanese**: 3-way (ko/so/a)
- **Korean**: 3-way (i/geu/jeo)
- **Spanish**: 3-way historically (este/ese/aquel)
- **Greek has**: 3-way (hode/houtos/ekeinos) **BUT**
- **Hebrew has**: Simple 2-way (zeh/hu)
- **Examples**: Hebrew "this" → which of 3 in target?

## Language Family Priorities

### Critical Gaps in Current Documentation

1. **Missing dominant language examples** showing how solutions work
2. **Missing feature-by-language matrices** (which languages have which features)
3. **Not grouped by shared patterns** with exceptions called out
4. **Not TBTA-focused** (grammatical description vs translation decisions)

## Proposed Documentation Structure

### For Each Language Family

```markdown
## {Family Name}

### TBTA Feature Overview
| Feature | Applicable? | Pattern | Exceptions |
|---------|-------------|---------|------------|
| Clusivity | Universal | Inclusive/Exclusive | - |
| Dual Number | Common | Pronouns only | Tagalog (nouns too) |
| Evidentiality | No | - | - |

### Critical Features (Obligatory in most family members)
1. **Clusivity** (172/172 languages)
   - Dominant language reference: Tagalog kita/kami
   - Minor language examples: Ilocano, Cebuano patterns
   - Theological implications: Lord's Prayer exclusive

### Important Features (Common but not universal)
2. **Dual Number** (87/172 Oceanic only)
   - Languages with: Samoan, Fijian, Hawaiian
   - Languages without: Tagalog, Indonesian, Malay
   - Decision rules: Biblical pairs → dual

### Rare Features (Few languages)
3. **Trial Number** (12/172 languages)
   - Languages: Some Oceanic only
   - Use cases: Trinity references
```

## Implementation Plan

### Phase 1: Create TBTA Feature Matrix
Create `/languages/TBTA-FEATURE-MATRIX.md` showing:
- All 57 TBTA features
- Which families have which features
- Dominant vs minor languages for each

### Phase 2: Enhance Family Documentation
For each family README:
1. Add "TBTA Translation Features" section
2. List critical/important/rare features
3. Provide dominant language examples
4. List minor language exceptions
5. Link to theological implications

### Phase 3: Create Cross-Reference
Link TBTA features to language documentation:
- Each feature directory → which families need it
- Each family directory → which features apply

## Expected Outcome

Translators can:
1. Look up their target language family
2. See which TBTA features are critical
3. Find dominant language examples
4. Identify if their language is an exception
5. Make informed translation decisions

## Priority Families for Enhancement

1. **Austronesian** - Most features not in Greek/Hebrew (clusivity, voice, dual/trial)
2. **Trans-New Guinea** - Switch-reference, evidentiality
3. **East Asian** - Honorifics, topic, classifiers
4. **Niger-Congo** - Noun classes, tone
5. **Mayan** - Classifiers, positionals, ergativity
6. **Quechuan** - Evidentiality

## Next Steps

1. Create TBTA-FEATURE-MATRIX.md
2. Read through all 13 feature directories for examples
3. Update each family README with TBTA feature sections
4. Add dominant language examples throughout
5. Create exception lists for minor languages
