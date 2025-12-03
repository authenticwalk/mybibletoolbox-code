# Aspect Feature Analysis - Stage 2.1 Complete

**Status**: Dataset creation complete
**Date**: 2025-11-29

## Overview

This directory contains the analysis dataset for the Aspect TBTA feature, prepared according to Stage 2.1 of the TBTA feature development methodology.

## Contents

### Data Files
- `data/train.jsonl` - Training dataset (2,295 entries)
- `data/validate.jsonl` - Validation dataset (286 entries, labels visible)
- `data/validate.secret.jsonl` - Validation dataset with full data (286 entries)
- `data/test.jsonl` - Test dataset (288 entries, labels visible)
- `data/test.secret.jsonl` - Test dataset with full data (288 entries)
- `data/leftovers.jsonl` - Remaining TBTA extractions not in train/validate/test (67,852 entries)

### Documentation
- `README.md` - This file
- `distribution.yaml` - Distribution of Aspect values in TBTA database
- `LANGUAGE-SELECTION.md` - Rationale for selected translation languages
- `audit-data.md` - Data quality audit report

### Secret/Archive Files
- `enriched.secret.jsonl` - Full enriched dataset before splitting (2,869 entries)
- `tbta-extract.secret.jsonl` - Complete TBTA extraction (72,089 entries)

## Dataset Statistics

### Total Extractions
- **TBTA Annotations**: 72,089
- **Unique Verses**: 11,544
- **Balanced Sample**: 2,869 (one per verse, balanced by genre and constituent)

### Split Distribution
- **Train**: 2,295 entries (80%)
- **Validate**: 286 entries (10%)
- **Test**: 288 entries (10%)
- **Leftovers**: 67,852 entries

### Aspect Value Distribution (Original TBTA)
| Value | Count | Percentage |
|-------|-------|------------|
| Unmarked | 69,430 | 96.31% |
| Imperfective | 927 | 1.29% |
| Inceptive | 471 | 0.65% |
| Continuative | 391 | 0.54% |
| Cessative | 354 | 0.49% |
| Routinely | 271 | 0.38% |
| Completive | 116 | 0.16% |
| Gnomic | 102 | 0.14% |
| Habitual | 27 | 0.04% |

### Translation Coverage
**Core Languages** (Required):
- eng-YLT (English Young's Literal) - 99.5%
- grc (Greek source) - 89.8% (NT only)
- hbo (Hebrew source) - 64.9% (OT only)
- heb-heb (Modern Hebrew) - 99.5%
- lat-VUC (Latin Vulgate) - 99.4%
- arb-NAV (Arabic) - 99.5%

**Additional Aspect-Marking Languages**:
- rus-SYN-1876 (Russian) - Perfective/Imperfective marking
- pol-UBG (Polish) - Perfective/Imperfective marking
- bul (Bulgarian) - Perfective/Imperfective marking
- ces (Czech) - Perfective/Imperfective marking
- zho-CUV-SIMP (Chinese) - Aspect particles
- tur-YTC (Turkish) - Aspect suffixes

All additional languages: 97.6-99.5% coverage

## Data Schema

Each entry contains:
```json
{
  "verse": "GEN-001-001",
  "label": "Inceptive",
  "constituent": "create",
  "part": "Verb",
  "path": "Clause[1]/Clause[1]/VP[0]",
  "text": "God **create** sky and earth",
  "strongs": "H0871a H7225 H1254-he.created ...",
  "strongs_number": "H1254",
  "genre": "History",
  "dataset": {
    "split": "train",
    "section": "OT",
    "literary_type": "history",
    "difficulty": "typical",
    "reason_group": "BEGIN_ACTION"
  },
  "translations": {
    "eng-YLT": "In the beginning of God's preparing the heavens and the earth —",
    "grc-LXX": "ΕΝ ΑΡΧΗ ἐποίησεν ὁ θεὸς τὸν οὐρανὸν καὶ τὴν γῆν.",
    "hbo-hbo": "בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃",
    ...
  }
}
```

## Reason Groups

Entries are categorized by reason groups to enable systematic analysis:

**Unmarked Aspect**:
- SIMPLE_STATE (be, exist, have)
- SIMPLE_ACTION (do, make, go, come, say)
- PERCEPTION (see, hear, know, understand)
- MOTION (walk, run, move, travel)
- COMMUNICATION (speak, ask, answer, pray)
- DEFAULT (other)

**Inceptive (Beginning of Action)**:
- BEGIN_SPEECH (say, speak, tell, ask, answer)
- BEGIN_MOTION (go, come, rise, depart, march)
- BEGIN_ACTION (do, make, work, build, fight)
- BEGIN_STATE (be, become, grow, turn)
- DEFAULT

**Continuative (Ongoing Action)**:
- ONGOING_ACTION (make, do, work, serve)
- ONGOING_CONFLICT (fight, war, battle)
- ONGOING_SPEECH (speak, preach, teach)
- ONGOING_MOTION (walk, follow, pursue)
- DEFAULT

**Cessative (Stopping Action)**:
- STOP_ACTION (work, labor, serve)
- STOP_CONFLICT (fight, war, battle)
- STOP_SPEECH (speak, complain, cry)
- STOP_MOTION (walk, travel, pursue)
- STOP_SIN (lie, sin, rebel)
- DEFAULT

**Other Aspects**: Similar categorical breakdown for Imperfective, Completive, Routinely, Gnomic, and Habitual.

**Note**: 68.3% of entries are in DEFAULT categories, indicating room for future refinement of verb categorization.

## Quality Metrics

- **Translation Coverage**: 99.5% excellent
- **Reason Group Assignment**: 100% complete
- **Strong's Number Coverage**: 94.0% (6% missing due to sparse checkout)
- **Data Validation**: Passed all audit checks (see audit-data.md)

## Next Steps (Stage 2.2+)

1. **Analyze Translations**: Study how aspect is realized in different languages
2. **Pattern Discovery**: Identify translation patterns that correlate with aspect values
3. **Algorithm Development**: Create PROMPT1.md based on discovered patterns
4. **Systematic Testing**: Validate against validate.jsonl dataset
5. **Error Analysis**: Use 6-step process to refine approach

## Notes

- Test dataset should remain untouched until final evaluation
- Validate dataset can be used for iterative development
- Translation data enables discovery-based approach: "what did real translators do?"
- Focus on marked aspect cases (3.69% of data) as these are most informative
