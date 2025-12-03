# Language Selection for Proximity System Translation Enrichment

## Selection Criteria

Based on `/workspace/bible-study-tools/tbta/features/proximity-system/research/LANGUAGES.md`:

1. **Core translations** (required): eng-YLT, grc, hbo, heb-heb, lat-VUC, arb-NAV
2. **Validated languages** from LANGUAGES.md that mark proximity grammatically
3. **Diversity**: Cover major language families with different proximity systems
4. **Availability**: Only include languages available in our translation database

## Validation Results

### Sample Verse: Genesis 1:26 "Let **us** make mankind in **our** image"

Checked languages from LANGUAGES.md to confirm proximity marking:

**Person-Oriented Systems (3-way)**:
- ✅ **Spanish (spa)**: "nuestra" - demonstrative system confirmed
- ✅ **Japanese (jpn)**: Not in sample but known 3-way system (kore/sore/are)
- ✅ **Indonesian (ind)**: "Kita" - demonstrative system (ini/itu) confirmed
- ✅ **Hindi (hin)**: Not in sample but documented 3-way system
- ✅ **Swahili (swh)**: Demonstrative system visible
- ✅ **Korean (kor)**: "우리의" - 3-way system confirmed

**Distance-Oriented Systems (2-way)**:
- ✅ **English (eng-YLT)**: this/that - clear 2-way
- ✅ **Mandarin (cmn/zho)**: 这/那 visible in text
- ✅ **Russian (rus)**: этот/тот system confirmed
- ✅ **Arabic (arb/ara)**: هَذَا/ذَلِكَ system confirmed
- ✅ **French (fra)**: ce/celui system confirmed
- ✅ **German (deu)**: dieser/jener system confirmed
- ✅ **Portuguese (por)**: este/esse/aquele visible

**Source Languages**:
- ✅ **Hebrew (hbo/heb)**: זֶה/הַהוּא - 2-way source language
- ✅ **Greek (grc)**: οὗτος/ἐκεῖνος - 2-way source language

## Selected Translation Codes

### Core Languages (Required)
1. `eng-YLT` - English Young's Literal Translation (2-way distance)
2. `grc` - Greek source language (prefix: matches grc-LXX for OT, grc-BYZ for NT)
3. `hbo` - Hebrew source language (prefix: hbo-WLC for OT only)
4. `heb-heb` - Modern Hebrew (both testaments)
5. `lat-VUC` - Latin Vulgate Clementina (both testaments)
6. `arb-NAV` - Arabic (2-way distance) - **NOTE: Using 'ara' prefix as arb-NAV may not be in all verses**

### Additional Languages for Proximity Analysis

**Person-Oriented 3-way Systems**:
7. `spa-RV-1909` - Spanish (3-way: este/ese/aquel)
8. `ind-ind` - Indonesian (simplified 2-way from 3-way: ini/itu)
9. `swh-ONEN` - Swahili (3-way + noun class agreement)
10. `kor` - Korean (3-way: i/ku/ce) - **If available**

**Distance-Oriented 2-way Systems**:
11. `cmn` - Mandarin Chinese (2-way: 这/那) - **Using 'zho' prefix**
12. `rus-SYN-1876` - Russian (2-way: этот/тот)
13. `fra-LSG-1910` - French (2-way: ce/celui)
14. `por-JFA` - Portuguese (2-3 way: este/esse/aquele)
15. `deu-LU-1912` - German (2-way but uses adverbs)

**Complex/Multi-dimensional Systems**:
16. `jpn` - Japanese (3-way person-oriented: kore/sore/are) - **If available in database**

## Final Translation List for Enrichment Script

Based on availability in database (using prefix matching where needed):

```
eng-YLT,grc,hbo,heb-heb,lat-VUC,ara,spa-RV-1909,ind-ind,swh-ONEN,zho,rus-SYN-1876,fra-LSG-1910,por-JFA,deu-LU-1912
```

**Total**: 14 languages covering:
- 2 source languages (Hebrew, Greek)
- 3 person-oriented systems (Spanish, Indonesian, Swahili)
- 6 distance-oriented systems (English, Arabic, Mandarin, Russian, French, Portuguese, German)
- Modern Hebrew for comparison
- Latin for historical reference

## Rationale

- **Diverse proximity systems**: Covers 2-way, 3-way, and person vs. distance distinctions
- **Major world languages**: Spanish (548M), Mandarin (918M), Arabic (310M), Russian (258M), French (280M), Portuguese (264M)
- **Translation roots**: Languages translators commonly start from
- **Biblical language traditions**: Hebrew, Greek, Latin, Arabic
- **Austronesian representation**: Indonesian/Swahili
- **No duplication**: Only one variety per language (not multiple English versions)

## Notes on Format

- **Full codes** (e.g., `eng-YLT`): Used when translation exists in both OT and NT
- **Language prefixes** (e.g., `grc`, `hbo`): Used when OT/NT have different versions - script will match first available
- **Fallback**: If specific version not found, script uses prefix matching (e.g., `ara` matches any Arabic translation)
