# Language Selection for Participant Tracking Analysis

## Core Translations (Required)

These translations are included as baseline:

- **eng-YLT**: English (Young's Literal Translation) - Both OT and NT
- **grc**: Greek (prefix for Greek source texts) - NT: grc-BYZ/SR
- **hbo**: Hebrew (prefix for Hebrew source texts) - OT: hbo-WLC
- **heb-heb**: Modern Hebrew - Both OT and NT
- **lat-VUC**: Latin (Vulgate Clementina) - Both OT and NT
- **arb-NAV**: Arabic (Van Dyck) - Both OT and NT

## Additional Languages Selected

Participant tracking is relevant to languages with different reference systems:

### Pro-drop languages (allow null subjects)
- **spa-BES**: Spanish (Biblia Reina-Valera 1909) - Both OT and NT
- **ita-ITA**: Italian - Both OT and NT (if available)

### Languages with explicit participant marking
- **fra-LSG**: French (Louis Segond 1910) - Both OT and NT
- **deu-1912**: German (Luther 1912) - Both OT and NT

### Non-Indo-European languages
- **ind-AYT**: Indonesian - Both OT and NT

### MANDATORY Participant Tracking Languages (from LANGUAGES.md research)

These languages were identified in the research as having MANDATORY participant tracking systems and are critical for this analysis:

- **swh-ONEN**: Swahili - Bantu noun class agreement system, MANDATORY
- **qub-qub**: Quechua - Topic marker -qa system, MANDATORY
- **tgl-ULB**: Tagalog - Voice/focus system with definiteness, MANDATORY

### Languages NOT Available in eBible Corpus

The following languages were identified as MANDATORY in research but are not available in the eBible translation corpus:

- **jpn**: Japanese (wa/ga/zero anaphora system) - Not available in corpus
- **kor**: Korean (neun/ga/zero system) - Only available in BibleHub, not eBible corpus
- **cmn**: Mandarin Chinese - Not available as 'cmn' code (zho-CUV-TRAD/SIMP exist but not requested)

## Translation Code Format

Using the format specified in instructions:
- **Full code** (`eng-YLT`): Used when translation exists in both OT and NT
- **Language prefix** (`grc`, `hbo`): Used when OT/NT have different versions

## Final Translation List for Enrichment

Based on availability and linguistic diversity, including MANDATORY participant tracking languages:

```
eng-YLT,grc,hbo,heb-heb,lat-VUC,arb-NAV,spa-BES,fra-LSG,deu-1912,ind-AYT,swh,qub-qub,tgl
```

**Total**: 13 translations (including 10 original + 3 MANDATORY participant tracking languages)

### Languages Successfully Added
- **swh** → swh-ONEN (Swahili)
- **qub-qub** (Quechua)
- **tgl** → tgl-ULB (Tagalog)

### Languages Not Available
- **jpn** (Japanese) - Not in eBible corpus
- **kor** (Korean) - Only in BibleHub, not eBible
- **cmn** (Mandarin) - Replaced with previous selection (zho codes exist but not used)
