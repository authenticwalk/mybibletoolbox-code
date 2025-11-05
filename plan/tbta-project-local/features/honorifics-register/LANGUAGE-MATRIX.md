# Language Honorific Systems Matrix

Quick reference showing which languages in TBTA have which honorific/register features.

## Languages with Honorific Systems in TBTA Project

| Language | Code | Family | Age-Based | Social Status | Politeness Levels | Gender Differences | Priority |
|----------|------|--------|-----------|----------------|-------------------|-------------------|----------|
| Japanese | jpn | Japonic | ✓✓✓ Critical | ✓✓✓ Critical | ✓✓✓ 4 Levels | ✓✓ Significant | Phase 1 |
| Korean | kor | Isolate | ✓✓✓ Critical | ✓✓✓ Critical | ✓✓✓ Multiple | ✓✓ Significant | Phase 1 |
| Mandarin Chinese | cmn | Sino-Tibetan | ✓✓ Important | ✓✓ Important | ✓✓ Moderate | ✓ Present | Phase 1 |
| Thai | tha | Kra-Dai | ✓✓ Important | ✓✓✓ Critical | ✓✓ Moderate | ✓ Present | Phase 2 |
| Vietnamese | vie | Austro-Asiatic | ✓✓ Important | ✓✓ Important | ✓✓ Moderate | ✓ Present | Phase 2 |
| Indonesian | ind | Austronesian | ✓ Present | ✓✓ Important | ✓ Present | ✓ Minor | Phase 2 |
| Hindi | hin | Indo-European | ✓✓ Important | ✓✓ Important | ✓✓ Moderate | ✓ Present | Phase 3 |
| Bengali | ben | Indo-European | ✓✓ Important | ✓✓ Important | ✓✓ Moderate | ✓ Present | Phase 3 |
| Gujarati | guj | Indo-European | ✓✓ Important | ✓✓ Important | ✓ Present | ✓ Minor | Phase 3 |
| Marathi | mar | Indo-European | ✓✓ Important | ✓✓ Important | ✓ Present | ✓ Minor | Phase 3 |
| Tamil | tam | Dravidian | ✓✓ Important | ✓✓ Important | ✓✓ Moderate | ✓ Present | Phase 3 |
| Telugu | tel | Dravidian | ✓✓ Important | ✓✓ Important | ✓ Present | ✓ Minor | Phase 3 |
| Malayalam | mal | Dravidian | ✓✓ Important | ✓✓ Important | ✓ Present | ✓ Minor | Phase 3 |
| Tagalog | tgl | Austronesian | ✓✓ Important | ✓✓ Important | ✓✓ Moderate | ✓ Present | Phase 4 |
| Hebrew | heb | Afro-Asiatic | ✓ Present | ✓ Present | ✓ Present | ✓ Minor | Phase 4 |
| Arabic | arb | Afro-Asiatic | ✓✓ Important | ✓✓ Important | ✓✓ Moderate | ✓ Present | Phase 4 |
| Sanskrit | san | Indo-European | ✓✓ Important | ✓✓ Important | ✓ Present | ✓ Minor | Phase 4 |

---

## Key Findings

### Critical Systems (Must Implement - Impact Translation Accuracy)
- **Japanese (jpn)**: Most complex - keigo system with 4+ politeness levels
- **Korean (kor)**: Grammatically obligatory honorific markers
- **Thai (tha)**: Grammatical particles encode status/age differences

### Important Systems (Should Implement - Major Audience Impact)
- **Mandarin Chinese (cmn)**: Large audience, formal/informal distinction
- **Vietnamese (vie)**: Complex pronoun system reflecting age/status
- **Indonesian (ind)**: Cultural emphasis on respect to elders/authority
- **Hindi (hin)**: Large audience, obligatory formal/informal distinction
- **Bengali (ben)**: Large audience, formal/informal conjugations
- **Tamil/Telugu/Malayalam**: Large Dravidian-speaking audiences
- **Tagalog (tgl)**: Philippine Christian market growth

### Reference Systems (Cultural/Scholarly Value)
- **Hebrew (heb)**: Already in source texts, historical interest
- **Arabic (arb)**: Diglossic complexity, important for Arabic-speaking audiences
- **Sanskrit (san)**: Scholarly reference, Hindu context value

---

## Implementation Guidance by Feature

### Age-Based Honorifics
**Tier 1 Priority** (must distinguish age relationships):
- Japanese: Strict keigo protocol changes with every age/generation
- Korean: Jeondaemal vs banmal based on age differences
- Thai: Age hierarchy encoded in pronouns and particles
- Vietnamese: Complex pronoun system from "older" to "younger"

**Tier 2 Priority** (culturally important):
- Hindi/Bengali/Dravidian: Verb conjugation changes with age
- Indonesian: Title usage (Pak/Bu) reflects generational respect
- Tagalog: Obligatory -po/opo particles for elders

### Social Status Markers
**Critical** (affects most utterances):
- Japanese: Occupational status, educational level, formal context all affect register
- Korean: Professional rank, educational attainment determine speech forms
- Thai: Monastic status, royal context, bureaucratic formality

**Important** (affects character differentiation):
- Chinese: Formal pronouns (您) for superiors vs casual (你)
- Vietnamese: Professional titles used instead of names in many contexts
- Hindi: Class/caste historically significant (modern translations may deemphasize)

### Politeness Levels
**4+ Distinct Levels**:
- Japanese: Casual, polite, honorific, humble
- Korean: Multiple registers with distinct verb endings
- Thai: Formal particles vs casual speech patterns

**2-3 Distinct Levels**:
- Most other Asian languages: Formal vs informal, possibly intermediate

### Gender-Based Speech Differences
**Very Significant**:
- Japanese: Female particles (わ, ね) vs male particles (ぞ, な)
- Korean: Final particles differ by gender (강조, 의문, 완화)
- Thai: Final particles explicitly gendered (ครับ vs ค่ะ)

**Significant**:
- Vietnamese: Tonal patterns differ between perceived genders
- Chinese: Softer final particles for female speakers
- Hindi: Softer pronunciation preferences for traditional female speech

**Minor/Eroding**:
- Indonesian: Modern urban speech shows less differentiation
- Tagalog: Modern young speakers increasingly neutral on gender

---

## Resource Implications

### Data Collection Priority
1. Japanese translation examples (formal/informal pairs)
2. Korean register usage examples
3. Thai particle usage documentation
4. Chinese formal/informal vocabulary lists
5. Vietnamese pronoun usage contexts

### Validation Checklist
For each language tool that implements honorifics:
- [ ] Age-based register differentiation working correctly
- [ ] Status-based forms producing appropriate output
- [ ] Politeness level selection reflected in final output
- [ ] Gender patterns applied (where relevant)
- [ ] Biblical character relationships honored
- [ ] Native speaker validation completed

---

## Notes for Development

### Translation Quality Impact
Languages marked as "Phase 1" significantly impact translation accuracy if honorific systems are not implemented. A Japanese translation without proper keigo system will:
- Sound disrespectful to God/Jesus
- Misrepresent character relationships
- Confuse cultural context of authority structures
- Fail validation by native speakers

### Audience Expectations
- **Asian-language audiences**: Expect culturally appropriate register usage
- **South Asian audiences**: Expect respect for family/age hierarchy
- **Southeast Asian audiences**: Expect politeness and harmony emphasis
- **Semitic-language audiences**: Expect title-based respect forms

### Comparative Difficulty
- **Most difficult**: Japanese, Korean (obligatory systems, multiple levels)
- **Moderately difficult**: Thai, Vietnamese, Mandarin (grammatical encoding)
- **Less difficult**: Indonesian, Tagalog (cultural rather than obligatory)
- **Reference only**: Hebrew, Sanskrit (already in source or historical)

---

## Links and References
See main README.md in this directory for:
- Detailed feature descriptions per language
- Academic references and research citations
- Implementation data structure examples
- Tool development priorities and phases

