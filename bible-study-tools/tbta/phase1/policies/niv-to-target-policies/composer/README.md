# NIV to Tabitha Target Format Conversion

**Goal:** Convert NIV Bible text into Tabitha's intermediary format (targets.tabitha.bible) that can translate to any language.

**Approach:** Verse-by-verse analysis of Ruth 1, comparing NIV with target format to extract rules.

**Working Directory:** `niv-to-target-policies/composer/`

## Analysis Flow

For each verse:

1. **NIV Text** - Get from internal memory/quote_verse
2. **Greek/Hebrew** - Reference source language alignment
3. **Target Format** - Analyze Unchurched Adults version from targets.tabitha.bible
4. **Differences** - List all transformations
5. **Reasons** - Why each change (intermediary layer for translation)
6. **Rule Evaluation** - Match to existing rules or propose new ones

## File Structure

```
composer/
├── README.md (this file)
├── PROCESS.md (step-by-step process)
├── rules.md (master rule set - 28 rules)
├── synthesis.md (pros/cons evaluation)
├── PROGRESS.md (progress tracking)
└── verse-analysis/
    ├── RUT-1-01.md through RUT-1-22.md
    └── (22 verse analyses)
```

## Quick Start

1. **Read PROCESS.md** - Step-by-step conversion process
2. **Reference rules.md** - Complete rule set with examples
3. **Check verse-analysis/** - See worked examples

## Key Deliverables

- ✅ **28 consolidated rules** (from 34+ initial patterns)
- ✅ **14-step process** for systematic conversion
- ✅ **Complete Ruth 1 analysis** (22 verses)
- ✅ **Prioritized rule set** (Critical/High/Medium/Low)
