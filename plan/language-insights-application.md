# Language Family Insights Application to TBTA Features

## Task Overview
Apply key linguistic insights from recently merged language family data into specific TBTA features.

## Key Insights to Apply

### 1. Person Systems (Clusivity)
**Current Status**: Well-documented with Austronesian focus
**New Insights to Add**:
- **Algic Family**: Obviation (4th person) in Algonquin, Cree, Ojibwe - different from clusivity
- **Indo-European**: T-V distinction (tu/vous) across Romance, Slavic branches
- **Language-specific notes**: Some languages may have superstitions about 3rd person usage

### 2. Number Systems
**Current Status**: Good coverage of dual/trial/paucal
**New Insights to Add**:
- **Indo-European Dual**: Only Slovene, Upper Sorbian, Lower Sorbian, Kashubian preserve dual (NOT in current dataset!)
- **Austronesian Trial**: Specific to ~12 Oceanic languages
- **Niger-Congo**: Number in noun classes (singular/plural mediated through class systems)
- **Trans-New Guinea**: Dual widespread, some trial in specific families

### 3. Honorifics/Register
**Current Status**: Excellent Asian language coverage
**New Insights to Add**:
- **Indo-European T-V**: French tu/vous, German du/Sie, Spanish tú/usted, Russian ты/вы
- **Age-based kinship**: Niger-Congo languages distinguish older/younger siblings (kaka/dada in Swahili)
- **Cultural notes**: Some cultures find certain honorific levels superstitious or inappropriate

### 4. Voice Systems (NEW - needs feature file)
**From Austronesian family**:
- Philippine-type: 4-voice obligatory (Tagalog, Cebuano, Ilokano)
- Western Austronesian: 2-voice (Indonesian, Malay)
- Actor focus vs Patient focus decisions required for every verb

### 5. Evidentiality (NEW - needs feature file)
**From Trans-New Guinea family**:
- ~50 Highlands languages: OBLIGATORY information source marking
- Categories: visual (witnessed), reportive (hearsay), inferential (deduced), participatory
- Critical for Gospel narratives: "Jesus rose" requires witnessed vs reported marking

### 6. Switch-Reference (NEW - needs feature file)
**From Trans-New Guinea family**:
- Nearly universal in Trans-New Guinea
- Medial verbs mark same/different subject
- Example: "He came and sat down" requires same-subject marker

### 7. Aspect vs Tense
**From Indo-European family**:
- **Slavic**: Aspect-prominent (matches Greek perfectly) - perfective/imperfective distinction
- **Romance/Germanic**: Tense-prominent (struggles with Greek aorist)
- **Greek aorist problem**: Perfective aspect, not simple past - Slavic captures this, English loses it

### 8. Case Systems
**From Indo-European family**:
- **Slavic (6-7 cases)**: Can express Greek nuances precisely
- **English (0-1 cases)**: Requires rigid word order, loses emphasis patterns
- **Trans-New Guinea**: Ergative case marking (optional, based on animacy/focus)

### 9. Noun Classes (NEW - needs feature file)
**From Niger-Congo family**:
- 10-20 classes OBLIGATORY in Bantu
- Every noun (including God, Jesus, angels) requires class assignment
- Classes affect all concordial agreements
- Abstract concepts like "word", "faith" require class decisions

### 10. Kinship Age Distinctions (enhancement to honorifics)
**From Niger-Congo family**:
- **Swahili**: kaka (older brother) vs. younger sibling distinction
- **Bantu-wide**: Age-based kinship terms obligatory
- Translation challenge: Biblical "brother" may need age specification

### 11. Serial Verb Constructions (NEW - needs feature file)
**From Trans-New Guinea family**:
- Causatives: use serial "give" + main verb
- Benefactives: use serial "give"
- Aspectual: use serial "stay" (progressive), "finish" (completive)
- Limited verb roots (some languages have only 60!) require serial constructions

### 12. Spatial Deixis/Elevation (NEW - needs feature file)
**From Trans-New Guinea family**:
- "Go up" vs "go down" requires elevation specification
- Biblical "go up to Jerusalem" maps naturally
- Ascension/descension language highly salient

### 13. Tone Systems (NEW - needs feature file)
**From Niger-Congo family**:
- Tone is NOT optional - as essential as consonants/vowels
- Prevents theological misunderstanding
- Affects definiteness marking in some languages

### 14. Possession Systems
**From Trans-New Guinea and Austronesian families**:
- **Inalienable**: body parts, kinship, "Son of God"
- **Alienable**: objects, possessions
- **Niger-Congo**: Possession through noun class agreement
- Translation: "Our Father" = inalienable kinship marking

### 15. Word Order and Pragmatics
**From Indo-European family**:
- **Greek**: Flexible SVO for emphasis (fronting for focus)
- **Slavic**: Can match Greek pragmatic order
- **English/Romance**: Rigid SVO, loses emphasis patterns
- **Celtic**: VSO (matches Hebrew but not Greek)

## Application Plan

### Phase 1: Enhance Existing Features
1. **Person Systems**: Add Indo-European T-V, Algic obviation notes
2. **Number Systems**: Add Indo-European dual notes (Slovene etc.), Niger-Congo class-based number
3. **Honorifics**: Add Indo-European T-V examples, Niger-Congo age-based kinship

### Phase 2: Create New Feature Files (if missing)
4. **Voice Systems**: Philippine-type focus systems
5. **Evidentiality**: Trans-New Guinea obligatory source marking
6. **Switch-Reference**: Trans-New Guinea medial verb systems
7. **Noun Classes**: Niger-Congo 10-20 class systems
8. **Serial Verb Constructions**: Trans-New Guinea limited verb roots
9. **Spatial Deixis**: Elevation marking systems
10. **Tone**: Niger-Congo tonal systems

### Phase 3: Add Language-Specific Examples
- Extract dominant language examples from family READMEs
- Add minor language exceptions
- Include cultural notes (superstitions, taboos, special uses)

### Additional Insights from Mayan Family

16. **Numeral Classifiers**: ESSENTIAL (all 22 languages) - shape/function/abstract properties
17. **Positional Verbs**: ESSENTIAL (250-500 roots per language) - exact position, posture, shape at rest
18. **Ergative-Absolutive**: CRITICAL (all Mayan) - transitive subjects marked differently than intransitive
19. **Directional Morphology**: Verbal affixes encode motion direction (up/down/toward/away)

### Additional Insights from Other Major Families

20. **Otomanguean**: Tone for INFLECTION (not just lexical) - most complex inflection systems in world
21. **Australian**: Kinship-influenced grammar - dual pronouns vary by relationship between referents
22. **Afro-Asiatic**: Root-and-pattern morphology - consonantal roots, vowel patterns add grammar
23. **Uto-Aztecan**: Polysynthetic - single verb can be complete sentence with subject/object/tense/mode

## Next Steps
1. ✅ Read other language family data (Mayan, other-families)
2. Update existing TBTA feature READMEs with insights
3. Create new feature directories where needed
4. Commit and push changes
