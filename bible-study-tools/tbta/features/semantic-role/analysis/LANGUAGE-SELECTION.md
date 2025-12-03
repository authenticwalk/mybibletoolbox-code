# Language Selection for Semantic Role Analysis

## Selection Criteria

Based on `research/LANGUAGES.md`, languages were selected to represent:

1. **Source languages**: Hebrew and Greek (critical for understanding source semantic roles)
2. **Case-marking languages**: Languages with rich case systems that explicitly mark semantic roles
3. **Prepositional languages**: Languages that use prepositions/particles like Hebrew
4. **Ergative languages**: Languages with ergative-absolutive alignment (if available)
5. **Applicative languages**: Languages with applicative voice systems

## Selected Translations

### Core Languages (Mandatory)

| Code | Language | Format | Testament Coverage | Rationale |
|------|----------|--------|-------------------|-----------|
| `eng-YLT` | English (Young's Literal) | full | OT + NT | Literal English, clear word-for-word mapping |
| `grc` | Greek (Koine) | prefix | OT=LXX, NT=BYZ/SR | Source language, 5-case system, explicit roles |
| `hbo` | Hebrew (Biblical) | prefix | OT only | Source language, prepositional complexity |
| `heb-heb` | Hebrew (Modern) | full | OT + NT | Modern Hebrew perspective |
| `lat-VUC` | Latin (Vulgate) | full | OT + NT | Historical, 6-case system |
| `arb-NAV` | Arabic | full | OT + NT | Major translation language, VSO order |

### Case-Marking Languages

| Code | Language | Cases | Rationale |
|------|----------|-------|-----------|
| `rus` | Russian | 6 cases | Rich case system, explicit role marking |
| `deu-1912` | German (Luther 1912) | 4 cases | Germanic, partial case system |

### Particle/Postposition Languages

| Code | Language | Marking | Rationale |
|------|----------|---------|-----------|
| `jpn` | Japanese | Particles (が/を/に/で) | Postpositional particles mark roles explicitly |

### Applicative Voice Languages

| Code | Language | Feature | Rationale |
|------|----------|---------|-----------|
| `ind-AYT` | Indonesian | Applicative voice | Can promote Beneficiary/Instrument to core arguments |

### Additional Helpful Languages

| Code | Language | Rationale |
|------|----------|-----------|
| `fra-LSG` | French (Louis Segond) | Romance, prepositional, major hub |
| `spa-BES` | Spanish (Biblia del Oso) | Romance, prepositional, major hub |
| `tur` | Turkish | 6 cases, agglutinative, ablative marks Source clearly |

## Total Selected: 13 Translations

1. eng-YLT
2. grc (prefix - matches first available: OT=grc-BRENT, NT=grc-BYZ or grc-SR)
3. hbo (prefix - matches hbo-WLC for OT)
4. heb-heb
5. lat-VUC
6. arb-NAV
7. rus
8. deu-1912
9. jpn
10. ind-AYT
11. fra-LSG
12. spa-BES
13. tur

## Validation

Before enrichment, validated these languages using sample verses:

**GEN.001.026** (Creation - "let us make"):
- ✅ Can identify target constituent in most languages
- ✅ Case/prepositional marking visible in case-languages
- ✅ Know grammatical rules well enough to use as hints

**MAT.004.019** (NT example):
- ✅ Greek case marking clear
- ✅ Case-languages mark roles explicitly
- ✅ Preposition-languages use distinct markers

## Notes

- **Full codes** (`eng-YLT`, `heb-heb`) used when translation covers both testaments
- **Prefix codes** (`grc`, `hbo`) used when OT/NT have different versions
- **Not duplicating**: Only one English (YLT), only one Greek prefix, etc.
- **Availability**: All selected translations confirmed available in eBible corpus (per research/LANGUAGES.md and /.data structure)

## Post-Enrichment Validation

After running `enrich_extract_with_verses.py`, will verify:
- [ ] All 13 languages appear in output
- [ ] Hebrew (hbo/heb-heb) present for OT verses
- [ ] Greek (grc) present for NT verses
- [ ] Case-marking languages show expected morphology
- [ ] No missing translations for common verses
