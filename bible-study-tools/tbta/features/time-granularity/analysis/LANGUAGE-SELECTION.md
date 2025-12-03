# Language Selection for Time Granularity Feature

## Core Languages (Required)

| Code | Format | Testament Coverage | Rationale |
|------|--------|-------------------|-----------|
| eng-YLT | full | Both OT and NT | Young's Literal Translation - consistent word-for-word |
| grc | prefix | NT (grc-BYZ/SR) | Greek New Testament source language |
| hbo | prefix | OT (hbo-WLC) | Hebrew Old Testament source language |
| heb-heb | full | Both OT and NT | Modern Hebrew translation |
| lat-VUC | full | Both OT and NT | Latin Vulgate - historical |

## Languages That Mark Time Granularity

Based on research/LANGUAGES.md analysis:

| Code | Language | Family | Time System | Rationale |
|------|----------|--------|-------------|-----------|
| swh-ONEN | Swahili | Bantu | 2-3 past distinctions | Major Bantu language, ~80% of Bantu languages mark remoteness |
| tgl | Tagalog | Austronesian | Aspect-based, variable | Tests edge of feature - aspect + adverbial time framing |
| ind | Indonesian | Austronesian | ABSENT (aspect-only) | Control language - no grammatical time granularity |

## Additional Major Translation Languages

| Code | Format | Testament Coverage | Rationale |
|------|--------|-------------------|-----------|
| spa-BES | full | Both OT and NT | Spanish (Biblia al Español Sencillo) - major world language |
| fra-LSG | full | Both OT and NT | French (Louis Segond) - major European language |
| deu-1912 | full | Both OT and NT | German (Luther 1912) - major European language |

## Selection Notes

**Total: 11 translation codes**

**Time granularity markers**: Only Swahili (swh-ONEN) is confirmed to grammatically mark time granularity. Tagalog uses aspect-based system which may interact with temporal distance.

**Control languages**: Most of the selected languages (English, Greek, Hebrew, Latin, Spanish, French, German, Indonesian) do NOT grammatically encode time granularity, making them useful controls to verify that TBTA annotations are context-based rather than morphology-based.

**Coverage**: All selected languages have good Bible translation coverage in both testaments (except source languages which are testament-specific).

## Validation

Sample verses checked:
- GEN.001.026 (OT creation narrative - remote/legendary past)
- Translations successfully retrieved for all target languages
- Can identify target constituents in major languages
