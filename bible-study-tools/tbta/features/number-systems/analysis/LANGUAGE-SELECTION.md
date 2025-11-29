# Language Selection for Number Systems Feature

## Core Languages (Required)

These translations are required for all TBTA features:

| Code | Format | Testament Coverage | Reason |
|------|--------|-------------------|--------|
| `eng-YLT` | full | Both OT & NT | Young's Literal Translation - preserves Hebrew/Greek structure |
| `grc` | prefix | NT only (grc-BYZ/SR) | Greek New Testament source language |
| `hbo` | prefix | OT only (hbo-WLC) | Hebrew Old Testament source language |
| `heb-heb` | full | Both OT & NT | Modern Hebrew translation |
| `lat-VUC` | full | Both OT & NT | Latin Vulgate - historical reference |
| `arb-NAV` | full | Both OT & NT | Arabic - Semitic language with dual morphology |

## Feature-Specific Languages (Number Marking)

Languages selected based on their grammatical number systems:

### Indo-European Languages

| Code | Format | Number System | Reason |
|------|--------|---------------|--------|
| `deu-1912` | full | S/P | German - representative Germanic |
| `fra-LSG` | full | S/P | French - representative Romance |
| `spa-BES` | full | S/P | Spanish - representative Romance |
| `rus-SYN` | full | S/P | Russian - Slavic (no productive dual in modern) |

### Austronesian Languages

| Code | Format | Number System | Reason |
|------|--------|---------------|--------|
| `ind-AYT` | full | Optional marking | Indonesian - major Austronesian, optional number |
| `haw` | prefix | S/D/P | Hawaiian - Polynesian with dual marking |
| `meu` | prefix | S/D/P (trial suspected) | Motu - PNG Austronesian, potential trial |
| `ceb` | prefix | S/P | Cebuano - Philippine Austronesian |
| `chk` | prefix | S/P | Chuukese - Micronesian Austronesian |

### Additional Languages (Validated)

Languages that provide additional insight into number marking:

| Code | Format | Number System | Reason |
|------|--------|---------------|--------|
| `zho-CUV` | prefix | Classifiers | Chinese - different number encoding strategy |
| `swh-ONEN` | full | S/P with noun classes | Swahili - Bantu language |
| `tha` | full | Optional with classifiers | Thai - different encoding strategy |

## Validation Results

### Sample Verse: GEN.001.026 "Let us make..."

**Target constituent**: "us" (plural pronoun, Trinity context)

✅ **eng-YLT**: "Let **Us** make man in **Our** image" - Clearly identifies plural pronouns
✅ **hbo**: נַֽעֲשֶׂ֥ה (na'aseh, cohortative plural) - Source morphology visible
✅ **grc-LXX**: Ποιήσωμεν (Poiēsōmen, 1st plural subjunctive) - Plural marking clear
✅ **arb**: نَعْمَلُ (na'malu, 1st plural) - Plural verb form
✅ **lat-VUC**: "Faciamus" (1st plural subjunctive) - Plural marked
✅ **deu-1912**: "Laßt **uns** Menschen machen" - Plural pronoun visible
✅ **fra-LSG**: "Faisons l'homme à **notre** image" - Plural forms visible
✅ **spa**: "Hagamos al hombre a **nuestra** imagen" - Plural visible

## Translation Code Selection

Final translation codes for enrichment script:

```
eng-YLT,grc,hbo,heb-heb,lat-VUC,arb-NAV,deu-1912,fra-LSG,spa-BES,ind-AYT,rus-SYN,zho-CUV,swh-ONEN,tha,haw,meu,ceb,chk
```

**Total**: 18 translations
- 6 core (required)
- 12 feature-specific (number marking diversity)

## Notes

1. **Dual/Trial languages** (2025-11-29 Update):
   - ✅ **Hawaiian (haw)** - ADDED: Polynesian with productive dual morphology
   - ✅ **Motu (meu)** - ADDED: PNG Austronesian, suspected trial marking
   - ✅ **Cebuano (ceb)** - ADDED: Philippine Austronesian for family diversity
   - ✅ **Chuukese (chk)** - ADDED: Micronesian Austronesian for regional coverage
   - ❌ **Slovenian (slv)** - Not in eBible corpus
   - ❌ **Kilivila, Fijian** - Limited or no Bible translation coverage

2. **Rationale for Additions**:
   - Hawaiian and Motu provide critical dual/trial marking data for testing TBTA's Trial annotations
   - Cebuano and Chuukese expand Austronesian family coverage across Philippine and Micronesian regions
   - These languages are essential for validating the feature's handling of complex number systems beyond S/P

3. **Focus**: Expanded from S/P-only to include dual/trial marking languages (research LANGUAGES.md identified these as critical)

4. **Validation**: Languages selected from research/LANGUAGES.md analysis of Austronesian number systems

5. **Coverage**: Balanced between:
   - Source languages (Hebrew, Greek)
   - Major world languages (English, Spanish, French, German, Russian, Arabic, Chinese)
   - Representative families (Indo-European, Austronesian, Afro-Asiatic, Niger-Congo, Sino-Tibetan, Tai-Kadai)
   - **NEW**: Dual/trial-marking languages (Hawaiian, Motu) for complete number system coverage
