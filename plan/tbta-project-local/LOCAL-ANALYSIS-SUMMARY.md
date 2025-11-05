# TBTA Local Analysis - Summary

## What Was Created

This branch adds the **local analysis workflow** for TBTA features using actual Bible translation data from `.data/commentary/`.

### New Files

1. **LOCAL-ANALYSIS-WORKFLOW.md** - Complete workflow guide
   - Step-by-step instructions for local analysis
   - Sparse-checkout management
   - Data extraction techniques
   - Analysis template

2. **features/person-systems/ebible-analysis.md** - Example analysis
   - Genesis 1:26 clusivity analysis
   - 6 languages analyzed (Tagalog, Indonesian, Swahili, English×2, German)
   - TBTA validation: ✅ Perfect match
   - Demonstrates the entire workflow

## The Workflow

### Core Concept

Instead of global research across all languages (already completed), perform **targeted local analysis**:

1. **Select 3 verse fragments** that cover all states of a feature
2. **Choose languages** you know encode the feature (from ebible data)
3. **Extract actual translations** from `.data/commentary/.../translations-ebible.yaml`
4. **Analyze patterns** and disagreements
5. **Validate against TBTA** annotations in `.data/commentary/.../*-tbta.yaml`
6. **Document** in `features/{feature}/ebible-analysis.md`

### Why This Matters

- **Validates** global research with real translations
- **Grounds** findings in actual data, not just linguistic typology
- **Discovers** edge cases and disagreements between languages
- **Demonstrates** TBTA's value with concrete examples

## Example Results

### Genesis 1:26 Clusivity Analysis

**Feature tested**: First Person Inclusive vs Exclusive

**Finding**: Languages with clusivity marking ALL agree:
- **Tagalog**: `natin` (from `tayo` = inclusive)
- **Indonesian**: `Kita` (inclusive)
- **TBTA encoding**: `Person: First Inclusive` ✅

**Theological implication**: Trinity members addressing each other (inclusive "we"), not God addressing external audience (exclusive "we")

**Validation**: Perfect match between TBTA and actual language choices

## Data Structure

### Available in `.data/` (sparse-checkout)

```
.data/commentary/
├── GEN/001/          # Genesis chapter 1
├── JHN/003/          # John chapter 3
└── MAT/005/          # Matthew chapter 5
```

Each verse directory contains:
- `{BOOK}.{chap}.{verse}-translations-ebible.yaml` - Translations in 700+ languages
- `{BOOK}-{chap}-{verse}-tbta.yaml` - TBTA annotations
- `{BOOK}-{chap}-{verse}-macula.yaml` - Source language morphology

### Adding More Verses

```bash
cd .data
git sparse-checkout add commentary/ROM/008
git sparse-checkout add commentary/ACT/015/025  # For Acts 15:25
```

## Next Steps

### For Each Feature

Create `features/{feature}/ebible-analysis.md` following the template in LOCAL-ANALYSIS-WORKFLOW.md:

**Recommended features to analyze**:
1. ✅ **person-systems/clusivity** - DONE (Genesis 1:26)
2. **number-systems** - Genesis 1:26 (Trial), other verses for Dual
3. **proximity-systems** - Demonstratives (this/that distinctions)
4. **time-granularity** - Temporal markers in narrative
5. **honorifics-register** - Speaker-listener relationships
6. **illocutionary-force** - Commands, questions, declarations
7. **polarity** - Negation strategies
8. **surface-realization** - How concepts are expressed

### Workflow for New Feature

1. Read `features/{feature}/README.md` (global research)
2. Pick 3-5 verses demonstrating all feature states
3. Add verses to sparse-checkout if needed
4. Select 3-5 languages that encode the feature
5. Extract translations from ebible files
6. Analyze patterns and disagreements
7. Check TBTA validation
8. Document in `ebible-analysis.md`

## Key Benefits

### 1. Validation
- Confirms global research with real data
- Shows TBTA accuracy in actual translations

### 2. Concrete Examples
- Moves from theory ("Tagalog has clusivity") to practice ("Tagalog uses 'tayo' in Gen 1:26")
- Demonstrates AI grounding with actual verses

### 3. Translation Guidance
- Provides specific recommendations for translators
- Shows common pitfalls with real examples

### 4. AI Training
- Creates training data for AI Bible translation assistants
- Links TBTA features to actual language choices

## Usage

### For Developers
Read LOCAL-ANALYSIS-WORKFLOW.md and create analyses for features you're implementing.

### For Translators
Read `features/{feature}/ebible-analysis.md` for concrete examples in your target language.

### For Researchers
Use this workflow to validate TBTA predictions against real translation data.

## Tools Needed

- **Git sparse-checkout** - Managing .data directory
- **YAML reading** - Extracting translations
- **Linguistic knowledge** - Understanding target languages
- **TBTA reference** - Validation against annotations

## Limitations

- Sparse-checkout limits initial verses (GEN/001, JHN/003, MAT/005)
- Requires adding more verses for comprehensive analysis
- Depends on ebible coverage (not all languages/verses available)
- Requires linguistic expertise in target languages

## Future Work

1. **Complete all features** - Create ebible-analysis.md for each feature
2. **Expand verse coverage** - Add verses from Acts, Romans, Epistles
3. **Language diversity** - Include more language families
4. **Automation** - Scripts to extract and compare translations
5. **Visualization** - Charts showing language family patterns

---

**Status**: Workflow established, example created for person-systems/clusivity
**Next**: Create ebible-analysis.md for remaining 7+ features
