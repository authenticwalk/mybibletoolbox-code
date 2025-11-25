# Test Set Creation: Scholarly Analysis Tool

## Overview
Created stratified test set of 40 Greek Strong's numbers for validating the Scholarly Analysis tool according to STAGES.md v2.0 requirements.

## File Location
`/workspaces/mybibletoolbox-code/bible-study-tools/strongs-extended/tools/scholarly-analysis/TEST-SET.yaml`

## Stratification Summary

### By Frequency (40 words)
- **Rare (<10 occurrences)**: 12 words (30%)
- **Medium (50-500 occurrences)**: 18 words (45%)
- **High (1000+ occurrences)**: 10 words (25%)

### By Word Type (40 words)
- **Theological**: 16 words (40%) - Core theological concepts with rich TDNT coverage
- **Grammatical**: 12 words (30%) - High-frequency functional words (articles, particles, prepositions)
- **Nominal**: 12 words (30%) - Concrete and abstract nouns with balanced frequency

### By Lexicon Coverage (40 words)
- **Rich (TDNT, LSJ, Trench)**: 16 words (40%)
- **Moderate (Thayer, HELPS, Abbott-Smith)**: 16 words (40%)
- **Sparse (limited sources)**: 8 words (20%)

### Adversarial Cases (12 words = 30%)

#### Controversial Etymology (3 words)
1. **G1967 (epiousios)** - Hapax legomenon, disputed etymology, no classical parallels
2. **G0733 (arsenokoites)** - Pauline neologism, cultural translation debates
3. **G0725 (harpagmos)** - Active vs passive sense debate, theological implications

#### Lexicon Divergence (4 words)
4. **G3056 (logos)** - Johannine vs Stoic vs OT wisdom meanings
5. **G4102 (pistis)** - Faith vs faithfulness debates
6. **G4151 (pneuma)** - Spirit vs wind vs breath, trinitarian implications
7. **G2435 (hilasterion)** - Propitiation vs expiation vs mercy seat

#### Rare Usage Contexts (3 words)
8. **G3457 (mulikos)** - Hapax, specific millstone type unclear
9. **G5287 (hupostasis)** - Technical term with shifting meaning
10. **G3875 (parakletos)** - Johannine legal vs spiritual advocate

#### Cultural Sensitivity (2 words)
11. **G1242 (diatheke)** - Covenant vs testament debates
12. **G1577 (ekklesia)** - Church vs assembly, ecclesiology debates

## Selection Protocol: BLIND

### What Main Agent Receives
- **ONLY** the blind word list (40 Strong's numbers)
- **NO** metadata about:
  - Frequency bands
  - Difficulty ratings
  - Adversarial designations
  - Expected challenges

### Rationale
Prevents cognitive bias in scholarly analysis. Main agent should approach each word neutrally without preconceptions about difficulty or controversy.

## Diversity Verification

### NT Books Covered
- **Gospels**: Matthew, Luke, John (4 words)
- **Pauline Epistles**: Romans, 1Cor, Phil, Gal, 2Cor (7 words)
- **Hebrews**: 2 words
- **General Epistles**: James, 1John, 1Peter (3 words)
- **Revelation**: 1 word

### Semantic Domains
- Concrete (millstone)
- Abstract (truth, wisdom, substance)
- Relational (love, fellowship, reconciliation)
- Theological (God, lord, spirit, revelation)
- Anthropological (human, body, soul)
- Ethical (righteousness, sin)
- Covenantal (covenant)
- Eschatological (parousia, life)
- Grammatical (particles, articles, prepositions)

### Chronological Diversity
- **Early Pauline**: 1Thessalonians, Galatians, 1Corinthians
- **Later Pauline**: Philippians, 2Corinthians, Colossians
- **Johannine**: Gospel of John, 1John
- **Synoptic**: Matthew, Luke
- **General**: James, Hebrews

## Exclusions

### Avoided from Approach A Experiments
- Did NOT use words already mentioned in scholarly-analysis documentation
- Examples excluded: G25, G2198 (mentioned in prior experiments)

### Distribution Strategy
- NOT concentrated in Romans/John
- Balanced across NT corpus
- Mix of Pauline, Johannine, Synoptic, General Epistles

## Research Sources Used

### Web Resources Consulted
1. **Wiktionary**: NT word frequency appendix
2. **TDNT Coverage**: Theological dictionary references
3. **Hapax Legomena Research**: Cateclesia Institute, The Cripplegate
4. **Controversial Etymology**: Arsenokoites, Harpagmos, Epiousios debates
5. **Strong's Concordance**: BibleHub, StudyLight, Blue Letter Bible
6. **Lexicon Coverage**: Multiple online lexicons verified

### Frequency Data Sources
- Greek NT has 138,020 total word occurrences
- ~5,400 unique words
- ~1,900 hapax legomena (36% of vocabulary)
- Top 310 words (50+ occurrences) = 80% of text

## Key Statistics

### Most Frequent Words Included
- **G3588 (ho)**: 19,867 occurrences (article "the")
- **G2532 (kai)**: 9,224 occurrences (conjunction "and")
- **G1161 (de)**: Combined with kai and ho = 23% of NT

### Theological Core Words Included
- **G0026 (agape)**: Love
- **G4102 (pistis)**: Faith
- **G5485 (charis)**: Grace
- **G3056 (logos)**: Word/Reason

### Notable Rare Words
- **G1967 (epiousios)**: Occurs ONLY in Lord's Prayer (Matt 6:11, Luke 11:3), nowhere else in ancient Greek literature
- **G0725 (harpagmos)**: Occurs ONLY in Phil 2:6
- **G3457 (mulikos)**: Hapax in NT

## Next Steps

1. **Main Agent Execution**: Use blind word list for scholarly analysis generation
2. **Validation**: Compare outputs against stratification expectations
3. **Quality Metrics**: Track performance across frequency bands
4. **Adversarial Analysis**: Evaluate handling of controversial cases
5. **Coverage Assessment**: Verify lexicon source utilization

## Success Criteria

### Critical Validations (Must Pass)
- No fabricated sources
- Inline citations present
- ATTRIBUTION.md compliance
- No hallucinated frequency predictions

### High Priority (80%+ accuracy)
- Etymology accuracy (especially adversarial cases)
- Lexicon divergence handling
- Cultural sensitivity awareness
- Theological precision

### Medium Priority (60%+ coverage)
- Multiple lexicon consultation
- Classical Greek background
- LXX usage patterns
- NT contextual analysis

## File Integrity

```bash
# Verify test set
cd /workspaces/mybibletoolbox-code
wc -l bible-study-tools/strongs-extended/tools/scholarly-analysis/TEST-SET.yaml
# Expected: 192 lines

# Count words
grep "^  - G" bible-study-tools/strongs-extended/tools/scholarly-analysis/TEST-SET.yaml | wc -l
# Expected: 40 words

# Check for duplicates
grep "^  - G" bible-study-tools/strongs-extended/tools/scholarly-analysis/TEST-SET.yaml | sort | uniq -c | awk '$1 > 1'
# Expected: (no output = no duplicates)
```

## Status
✅ Test set created: 40 words
✅ Stratification verified: Frequency (30/45/25), Type (40/30/30), Coverage (40/40/20)
✅ Adversarial cases embedded: 12 words (30%)
✅ Diversity confirmed: NT books, semantic domains, chronological spread
✅ Blind protocol enforced: No difficulty metadata in word list
✅ Research documented: Web sources, frequency data, lexicon coverage
