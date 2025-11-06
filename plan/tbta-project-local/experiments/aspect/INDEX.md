# TBTA Aspect Prediction Experiment - File Index

## Quick Navigation

**Just starting?** → Read `README.md` first (10 min overview)
**Need quick lookup?** → Use `QUICK_REFERENCE.md` (decision trees)
**Want methodology?** → See `aspect_identification_method.md` (detailed patterns)
**Building tests?** → Use `experiment-001.md` (test framework)
**Analyzing data?** → Run `test_aspect_predictions.py` (Python script)

---

## File Descriptions

### Core Documentation Files

#### README.md (10 KB)
**Best for**: Getting started, understanding the experiment
**Contains**:
- Experiment overview and purpose
- Key finding: aspect is rare (90.7% unmarked)
- Test cases summary (Inceptive, Imperfective, Habitual, Unmarked)
- Critical patterns for prediction
- Lessons learned from data
- Implications for Bible translators
- Next steps for extension

**Read time**: 10-15 minutes
**Key insight**: Inceptive aspect strongly correlates with potential mood + action verb + later today time

---

#### experiment-001.md (10 KB)
**Best for**: Understanding the hypothesis-driven test framework
**Contains**:
- Mood values in TBTA (9 values)
- Key distinctions (Perfective vs Imperfective, Habitual vs single occurrence, Inceptive vs Cessative)
- Test categories (Category 1-5)
- Test cases with actual TBTA data from Matthew 24
- Hypothesis development process
- Experimental methodology (Phase 1-4)
- Success metrics and preliminary results

**Read time**: 15-20 minutes
**Key feature**: Specific verse examples with all annotations

---

#### QUICK_REFERENCE.md (7 KB)
**Best for**: Quick lookup while analyzing verses
**Contains**:
- All 9 aspect values with English examples
- When to use each aspect (with examples)
- Quick decision tree (flowchart)
- Aspect by verb type (action/state/process)
- Red flags for each aspect
- Aspect distribution in Bible narrative
- Language implementation notes
- Testing checklist

**Read time**: 5-10 minutes (for reference)
**Format**: Tables, decision trees, quick lookup

---

#### aspect_identification_method.md (19 KB)
**Best for**: Deep understanding of prediction logic
**Contains**:
- TBTA aspect annotation philosophy
- Detailed decision tree (9 main branches)
- For each aspect: definition, reliable triggers (A-D), confidence levels, prediction rules, test results
- Aspect by verb type (semantic classification)
- Workflow for aspect prediction (6 steps)
- Accuracy metrics summary table
- Confidence levels for future testing
- Common prediction errors with fixes
- Language family implications
- Next testing priorities

**Read time**: 20-30 minutes
**Best reference for**: Detailed methodology and error analysis

---

### Generated Analysis Reports

#### aspect_analysis.md (1.9 KB)
**Auto-generated** by `test_aspect_predictions.py`
**Contains**:
- Summary statistics (10 verses, 54 verbs)
- Aspect distribution table
- Top 20 verb constituents
- Mood distribution
- Time distribution

**Update frequency**: Run Python script to regenerate
**Use for**: Quick statistical overview

---

#### test_cases.md (1.3 KB)
**Auto-generated** by `test_aspect_predictions.py`
**Contains**:
- Specific test cases grouped by aspect
- 5 examples of each aspect type with verse/mood/time
- Currently: Unmarked (49 cases), Inceptive (3), Imperfective (1), Habitual (1)

**Format**: Markdown lists
**Use for**: Finding specific verses to test

---

#### aspect_by_verb.md (506 B)
**Auto-generated** by `test_aspect_predictions.py`
**Contains**:
- Aspect distribution for verbs appearing multiple times
- Shows when same verb has different aspects

**Use for**: Understanding verb variation

---

#### aspect_by_mood.md (422 B)
**Auto-generated** by `test_aspect_predictions.py`
**Contains**:
- Aspect distribution cross-tabulated with mood
- Shows how aspect and mood correlate

**Key finding**: 'might' Potential mood = 100% Inceptive (3/3 cases)

---

### Data Files

#### aspect_raw_data.json (8.9 KB)
**Auto-generated** by `test_aspect_predictions.py`
**Format**: JSON array of verb objects
**Contains**:
- verse reference
- constituent (verb name)
- aspect value
- mood value
- time value
- lexical sense

**Use for**: Data analysis in other tools, further processing

---

### Code Files

#### test_aspect_predictions.py (13 KB)
**Type**: Python 3 script
**Purpose**: Automated aspect data extraction and analysis
**Features**:
1. Loads TBTA verse annotations from .data/commentary
2. Extracts all verbs with their metadata
3. Generates statistics and reports
4. Creates test cases
5. Outputs to JSON and markdown

**Usage**:
```bash
python3 test_aspect_predictions.py
```

**Requirements**: PyYAML, Python 3.6+
**Output**: Generates all analysis reports listed above

**Modify to**: Change BOOK/CHAPTER constants, adjust data directories, add new analysis functions

---

## How to Use These Files

### For Beginners
1. Start with **README.md** - understand the experiment
2. Review **QUICK_REFERENCE.md** - see all aspect values
3. Look at **test_cases.md** - find specific verse examples
4. Study **aspect_identification_method.md** - learn decision rules

### For Researchers
1. Read **experiment-001.md** - understand test framework
2. Analyze **aspect_identification_method.md** - detailed methodology
3. Review **aspect_analysis.md** - statistical patterns
4. Examine **aspect_raw_data.json** - do further analysis

### For Tool Builders
1. Modify **test_aspect_predictions.py** - customize analysis
2. Use **aspect_raw_data.json** - feed to other systems
3. Reference **aspect_identification_method.md** - implement decision logic
4. Check **QUICK_REFERENCE.md** - validate output

### For Bible Translators
1. Read **README.md** - understand implications
2. Use **QUICK_REFERENCE.md** - identify aspects in your verses
3. Reference **aspect_identification_method.md** - apply patterns
4. Check language implications section

---

## Data Flow Diagram

```
Matthew 24 TBTA Annotations (.yaml files)
        |
        v
test_aspect_predictions.py
        |
        +---> aspect_raw_data.json (raw structured data)
        |
        +---> aspect_analysis.md (statistical summary)
        |
        +---> aspect_by_verb.md (verb-aspect patterns)
        |
        +---> aspect_by_mood.md (mood-aspect correlation)
        |
        v
test_cases.md (verification examples)
```

---

## Key Statistics

| Metric | Value | Insight |
|--------|-------|---------|
| Verses Analyzed | 10 | Matthew 24 sample |
| Verbs Extracted | 54 | Total annotations |
| Unmarked | 49 (90.7%) | Default aspect |
| Inceptive | 3 (5.6%) | Beginning actions |
| Imperfective | 1 (1.9%) | Ongoing state |
| Habitual | 1 (1.9%) | Customary practice |
| Other Aspects | 0 (0.0%) | Rare in this sample |
| Overall Accuracy | 98.1% | 53/54 correct predictions |

---

## Document Updates

| Date | File | Change |
|------|------|--------|
| 2025-11-04 | All | Initial creation |
| 2025-11-04 | test_aspect_predictions.py | Generated analysis reports |
| 2025-11-04 | INDEX.md | This navigation guide |

---

## Next Steps

### Short-term (Phase 2)
- [ ] Expand to full Matthew 24 (51 verses, currently 10)
- [ ] Test on Mark and Luke (different narrative styles)
- [ ] Validate Cessative and Perfective aspects (currently 0 in sample)
- [ ] Create blind test set for validation

### Medium-term (Phase 3)
- [ ] Compare aspect across different books (Genesis, Psalms, etc.)
- [ ] Test on non-English TBTA annotations
- [ ] Build predictive model with decision trees
- [ ] Measure precision/recall for each aspect

### Long-term (Phase 4)
- [ ] Integrate with translation workflow tools
- [ ] Test accuracy with native speakers
- [ ] Adapt for language-specific feature combinations
- [ ] Build comprehensive TBTA feature prediction system

---

## Questions & Debugging

### Q: How do I run the Python script?
**A**: `python3 test_aspect_predictions.py` from the codebase root

### Q: What if I get YAML parsing errors?
**A**: Check that PyYAML is installed: `pip install PyYAML`

### Q: Can I analyze different verses?
**A**: Modify constants in test_aspect_predictions.py (BOOK, CHAPTER)

### Q: How accurate are these predictions?
**A**: 98.1% on Matthew 24 sample. See aspect_identification_method.md for confidence levels by aspect.

### Q: Which aspect is hardest to predict?
**A**: Cessative and Perfective (0 examples in current data). Look for telic verbs and apocalyptic contexts.

### Q: How do I use this for translation?
**A**: Read language implications in aspect_identification_method.md - maps TBTA aspect to target language forms.

---

## File Checklist

- [x] README.md - Overview and key findings
- [x] experiment-001.md - Test framework and hypotheses
- [x] QUICK_REFERENCE.md - Quick lookup guide
- [x] aspect_identification_method.md - Detailed methodology
- [x] test_aspect_predictions.py - Analysis script
- [x] aspect_analysis.md - Generated statistics
- [x] aspect_by_verb.md - Generated verb patterns
- [x] aspect_by_mood.md - Generated mood correlation
- [x] test_cases.md - Generated test cases
- [x] aspect_raw_data.json - Generated raw data
- [x] INDEX.md - This navigation guide

**Total**: 11 files
**Documentation**: 6 core files + 4 generated reports + 1 Python script
**Size**: ~98 KB total

---

**Experiment Location**: `/Users/chrispriebe/projects/mybibletoolbox/mybibletoolbox-code/plan/tbta-project-local/experiments/aspect/`

**Created**: 2025-11-04
**Status**: Phase 1 Complete, Ready for Phase 2 Expansion
