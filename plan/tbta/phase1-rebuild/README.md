# Phase 1 Encoding Rebuild from Semantic Encoding

**Status**: ✅ COMPLETED - Scripts implemented and tested

**Objective**: Create a Python utility to rebuild the `Verse` column (phase_1_encoding) from the `AnalyzedVerse` column (semantic_encoding) in TBTA's Bible CSV files.

---

## Key Findings

### Data Analysis Results

| Metric | Count |
|--------|-------|
| Total verses with AnalyzedVerse | 11,649 |
| Empty records (no TBTA data) | 19,122 |
| Verses with Verse but no AnalyzedVerse | 304 |
| Verses with very low overlap (<15%) | 338 |

**Important Discovery**: All verses that have AnalyzedVerse data also already have Verse data. There are no "missing" Verse entries to fill from AnalyzedVerse.

The 19,122 "empty" records are books that don't have TBTA annotations yet (like Romans, which is 100% empty).

### Reconstruction Behavior

The reconstructor produces **lemmatized text** (base word forms), not inflected English:

| Original Verse | Reconstructed |
|----------------|---------------|
| "King David was very old" | "David king be old" |
| "David felt cold" | "David feel cold" |
| "God started creating the heavens" | "God create sky" |

This is expected because AnalyzedVerse contains lemmas, not inflected forms.

---

## Scripts Location

Complete implementation is in: `/home/user/tbta_db_export/`

```
tbta_db_export/
├── scripts/
│   ├── README.md           # Usage documentation
│   ├── parser.py           # AnalyzedVerse parser (28 tests)
│   ├── reconstructor.py    # Phase1 reconstructor
│   └── rebuild.py          # Main CLI tool
├── tests/
│   ├── test_parser.py
│   ├── test_reconstructor.py
│   └── test_rebuild.py
├── requirements.txt
├── BEFORE-AFTER-SAMPLE.md  # Sample comparison report
└── .gitignore
```

---

## Usage

```bash
cd /home/user/tbta_db_export

# Analyze missing verses
python scripts/rebuild.py csv/Bible/ --analyze-missing report.md

# Generate before/after comparison
python scripts/rebuild.py csv/Bible/ --before-after report.md --overwrite-all

# Dry run on all files
python scripts/rebuild.py csv/Bible/ --all --dry-run -v
```

---

## PR Status

Branch `fix/phase-1-encoding-rebuild` created locally with 2 commits:
1. feat: add phase_1 encoding rebuild scripts
2. chore: add .gitignore and remove pycache files

**To complete PR**: Need to fork AllTheWord/tbta_db_export or get write access to push.
