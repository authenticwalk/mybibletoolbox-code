# Features Consolidation Summary

**Date:** 2025-11-06
**Source Directories:**
- plan/tbta-project-local/features/
- plan/tbta-project/features/

**Target Directory:** plan/tbta-rebuild-with-llm/features/

---

## What Was Consolidated

### Total Features: 13

#### From tbta-project-local (9 features):
1. **person-systems** - Clusivity, obviation, with excellent examples
2. **discourse-genre** - Genre classification
3. **honorifics-register** - Demographics and social relationships
4. **illocutionary-force** - Speech acts
5. **time-granularity** - Temporal precision
6. **surface-realization** - Noun/pronoun/zero realization
7. **polarity** (source 1)
8. **number-systems** (source 1)
9. **proximity-systems** - Demonstrative systems by language

#### From tbta-project (6 features):
1. **degree** - Comparison and intensification
2. **participant-tracking** - Information structure
3. **verb-tam** - Tense-aspect-mood
4. **polarity** (source 2)
5. **number-systems** (source 2)
6. **proximity** - TBTA annotation system

---

## Overlapping Features - Merge Decisions

### 1. Polarity
**Strategy:** Kept both versions with naming convention
- `polarity/README.md` - From tbta-project-local (9,978 bytes)
- `polarity/README-project.md` - From tbta-project (34,154 bytes)
- `polarity/LEARNINGS.md` - From tbta-project-local (7,536 bytes)
- `polarity/LEARNINGS-project.md` - From tbta-project (21,155 bytes)
- Additional files: SUMMARY.md, experiment-001.md from tbta-project-local

**Rationale:** Both sources provide valuable but different perspectives - project-local focuses on practical application, project provides deeper theoretical analysis.

### 2. Number Systems
**Strategy:** Kept both versions with naming convention
- `number-systems/README.md` - From tbta-project-local (9,200 bytes)
- `number-systems/README-project.md` - From tbta-project (25,865 bytes)
- `number-systems/LEARNINGS.md` - From tbta-project-local (7,205 bytes)
- `number-systems/LEARNINGS-project.md` - From tbta-project (22,148 bytes)
- Additional files:
  - From project-local: LANGUAGE-PREDICTIONS.md
  - From project: LANGUAGE-BREAKDOWN.md, TBTA-EXAMPLES.md, experiment-001.md

**Rationale:** Complementary content - project-local has language predictions, project has detailed examples and breakdown.

### 3. Proximity vs Proximity-Systems
**Strategy:** Kept both as separate directories
- `proximity/` - TBTA annotation system (from tbta-project)
- `proximity-systems/` - Language systems typology (from tbta-project-local)

**Rationale:** These are complementary, not overlapping. One focuses on the TBTA encoding system, the other on cross-linguistic demonstrative systems.

---

## Special Assets Copied

1. **ALL-FEATURES.md** (28,226 bytes) - Comprehensive feature catalog
2. **FEATURE-SUMMARY.md** (6,627 bytes) - Quick reference table
3. **README.md** (9,299 bytes, 200 lines) - New consolidated overview following progressive disclosure format

---

## Directory Structure Created

```
plan/tbta-rebuild-with-llm/features/
├── README.md (NEW - consolidated overview)
├── ALL-FEATURES.md
├── FEATURE-SUMMARY.md
├── degree/
├── discourse-genre/
├── honorifics-register/
├── illocutionary-force/
├── number-systems/ (MERGED)
├── participant-tracking/
├── person-systems/ (includes clusivity subdirectory with verse examples)
├── polarity/ (MERGED)
├── proximity/
├── proximity-systems/
├── surface-realization/
├── time-granularity/
└── verb-tam/
```

---

## Files Excluded

- **Python files**: 0 files (confirmed - no .py files in either source)
- **Temporary files**: None found
- **Build artifacts**: None found

---

## Key Features of Consolidation

### 1. Progressive Disclosure Format
The new README.md follows the progressive disclosure pattern from `.claude/skills/progressive-disclosure/SKILL.md`:
- ≤200 lines (exactly 200)
- Self-contained with key findings inline
- Links to detailed documentation
- NOT just a file list

### 2. Preserved All Research
- No data loss - all files from both sources preserved
- Overlapping files kept with -project suffix
- All experiments, learnings, and examples retained

### 3. Clear Organization
- 13 distinct feature directories
- Consistent structure across features
- Quick reference materials at top level

---

## Statistics

- **Total files:** 66
- **Python files:** 0 ✓
- **Features covered:** 13
- **Source projects:** 2
- **Merge conflicts:** 2 (polarity, number-systems) - resolved by keeping both
- **Complementary features:** 2 (proximity/proximity-systems) - kept separate

---

## Notable Highlights

### Person Systems
Contains **excellent clusivity examples** with actual verse analyses:
- `person-systems/clusivity/exclusive/MAT-006-009.md` (Lord's Prayer)
- `person-systems/clusivity/exclusive/JHN-003-011.md`
- Multiple other verse-specific analyses

### Proximity
Two comprehensive documents:
- **Proximity-systems** (247 lines): Cross-linguistic demonstrative typology
- **Proximity** (1086 lines): Complete TBTA annotation methodology with Biblical Hebrew/Greek systems

### Merged Features
Both polarity and number-systems now have rich documentation from both sources, giving users multiple perspectives and approaches.

---

## Recommendations

1. **Primary Reference:** Start with consolidated README.md for overview
2. **Quick Lookup:** Use FEATURE-SUMMARY.md for rapid reference
3. **Deep Dive:** Explore individual feature directories
4. **Merged Features:** For polarity and number-systems, read both versions:
   - Default files (no suffix) = practical/concise
   - -project files = comprehensive/theoretical

---

## Next Steps (Recommended)

1. Review merged features and potentially create unified versions
2. Validate all cross-references work correctly
3. Add language-specific decision trees to feature directories
4. Create feature-to-language mapping tables
5. Develop validation test suites for each feature

---

**Consolidation completed successfully with zero data loss and full preservation of research from both source projects.**
