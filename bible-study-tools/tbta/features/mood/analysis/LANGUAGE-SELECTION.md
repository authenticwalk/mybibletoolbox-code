# Language Selection for Mood Feature Enrichment

## Core Languages (REQUIRED)

These are essential base languages that must be included:

| Code | Language | Reason | Format |
|------|----------|--------|--------|
| `eng-YLT` | Young's Literal Translation | Literal English baseline | full |
| `grc` | Greek (NT source) | Source language with 4 explicit moods | prefix |
| `hbo` | Hebrew (OT source) | Source language with partial mood marking | prefix |
| `heb-heb` | Modern Hebrew | Modern source language | full |
| `lat-VUC` | Latin Vulgate | Historic translation with mood system | full |
| `arb-NAV` | Arabic | Semitic 4-way mood system (like Hebrew) | full |

## Additional Languages from LANGUAGES.md

Selected based on diverse mood marking strategies:

| Code | Language | Family | Mood System | Reason | Format |
|------|----------|--------|-------------|--------|--------|
| `spa-BES` | Spanish | Romance | Ind/Subj/Imp | Most productive subjunctive in Romance | full |
| `fra-LSG` | French | Romance | Ind/Subj/Imp | Reduced Romance subjunctive | full |
| `deu-1912` | German | Germanic | Modal verbs + Konj | Mixed grammatical/lexical system | full |
| `tur` | Turkish | Turkic | Ind/Imp + Evidential | Obligatory evidential mood | prefix |
| `swh` | Swahili | Niger-Congo | Ind/Subj/Imp | Bantu TAM template system | prefix |
| `rus` | Russian | Slavic | Ind/Imp/Cond | Reduced Slavic mood system | prefix |
| `ind-AYT` | Indonesian | Austronesian | Minimal/Optional | Minimal marking (isolating) | full |

## Total Languages: 13

**Translation codes for enrichment script**:
```
eng-YLT,grc,hbo,heb-heb,lat-VUC,arb-NAV,spa-BES,fra-LSG,deu-1912,tur,swh,rus,ind-AYT
```

## Languages Considered but Not Available

| Code | Language | Family | Mood System | Reason for Exclusion |
|------|----------|--------|-------------|---------------------|
| `jpn` | Japanese | Japonic | Modal auxiliaries + honorific interaction | Not available in eBible corpus; requires specialized Bible translation dataset |

## Validation

Validated with sample verses:
- **GEN.001.026** (OT): Cohortative "Let us make" - tests plural volitional
- Demonstrates mood marking across all selected languages

## Rationale

This selection provides:
1. **Source languages** (Greek, Hebrew) for morphological accuracy
2. **Typological diversity**: Romance subjunctive, Germanic modals, Turkic evidential, Bantu TAM, isolating minimal
3. **Theological breadth**: Languages from major Christian traditions
4. **Practical coverage**: All languages have complete or nearly complete Bible translations

## Update History

- **2025-11-29**: Attempted to add Japanese (jpn) per research LANGUAGES.md, but discovered jpn translations not available in eBible corpus. Japanese would provide unique modal auxiliary + honorific interaction perspective but requires external data source.
