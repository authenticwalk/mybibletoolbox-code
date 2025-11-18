# Number Systems: Algorithm Refinement Plan

**Date**: 2025-11-17
**Current Status**: Stage 5 complete (PROMPT1.md), Stage 6 complete (validation)
**Next Phase**: Algorithm refinement with real translation data

---

## Overview

The `fetch_verse.py` skill is now working! We can fetch translations to:
1. **Validate pattern detection** - Check if our rules match real translation data
2. **Refine algorithm** - Improve based on translation evidence
3. **Build confidence** - Cross-reference TBTA with actual usage

---

## Available Languages

### ✅ Available (BibleHub + eBible)
- **English** (eng): Multiple versions (NIV, KJV, ESV, etc.) - ~50+ versions
- **Greek** (grc): LXX (Septuagint) for OT, multiple NT manuscripts
- **Hebrew** (heb): WLC (Westminster Leningrad Codex) + variants

### ⚠️ NOT Available  
- **Minority languages**: Fijian (fij), Hawaiian (haw), Samoan (smo), Slovenian (slv), Tok Pisin (tpi)
- **Reason**: Not indexed by BibleHub, not in eBible cache

---

## Refinement Approach

### Phase 1: Sample Selection (DONE)

We already have:
- `train.yaml` - 494 verses (40%)
- `test.yaml` - 369 verses (30%)
- `validate.yaml` - 377 verses (30%)

**Strategy**: Focus refinement on TRAIN set (494 verses)

### Phase 2: Representative Sample (RECOMMENDED)

**Problem**: Fetching 494+ verses = hours of API calls

**Solution**: Create focused sample of 30-50 key verses

**Selection Criteria**:
1. **Trinity references** (Trial) - High priority, theologically significant
   - Gen 1:26, Gen 11:7, Gen 3:22 (3 verses)
2. **Explicit dual contexts** - Natural validation cases
   - Luke 24:13 ("two of them"), Mark 6:7 ("two by two"), Acts 13:2 ("Barnabas and Saul") (3 verses)
3. **Paucal contexts** - Small group validation
   - Matt 18:20 ("two or three"), John 2:6 ("six jars"), small gatherings (3 verses)
4. **Plural contexts** - Large groups
   - John 6:10 ("5,000 men"), Acts 1:15 ("120"), crowds (3 verses)
5. **Quadrial contexts** - Symbolic fours
   - Rev 4:6-7 ("four living creatures"), Ezek 1 (2 verses)
6. **Singular contexts** - Baseline
   - Single prophets, individual references (3 verses)
7. **Ambiguous cases** - Test pattern detection limits
   - Generic plurals, unclear counts (3 verses)

**Total**: ~20-25 key verses for focused validation

### Phase 3: Fetch & Analyze

**For each selected verse**:

```bash
python3 .claude/skills/quote-bible/scripts/fetch_verse.py <VERSE> --lang eng,grc,heb
```

**Analysis Questions**:
1. **Does English confirm the pattern?**
   - "Let us make" → Plural present in all English versions?
   - "Two of them" → Dual evident in English?

2. **Does Greek/Hebrew support TBTA?**
   - Hebrew plural forms in Gen 1:26 (`נַֽעֲשֶׂה` cohortative plural)?
   - Greek dual forms in NT (rare, mostly plural)?

3. **Is PROMPT1.md prediction correct?**
   - Apply PROMPT1.md rules to verse
   - Check against TBTA answer
   - Check against translation evidence

### Phase 4: Document Findings

Create `experiments/REFINEMENT-RESULTS.md`:
- Verse-by-verse analysis
- Pattern confirmation / rejection
- Algorithm adjustments needed
- Confidence assessment

### Phase 5: Iterate (if needed)

**If accuracy < 95% on sample**:
- Create PROMPT2.md with refinements
- Lock predictions
- Re-test

---

## Pragmatic Next Steps

### Option A: Manual Spot-Check (RECOMMENDED)

**Time**: 1-2 hours
**Verses**: 20-25 key verses
**Method**: Manual fetch + analysis

1. Select 20-25 verses (3-4 per number value)
2. Fetch translations manually
3. Apply PROMPT1.md rules
4. Compare with TBTA
5. Document findings

### Option B: Automated Sampling

**Time**: 3-4 hours (scripting + execution)
**Verses**: 50-100 representative verses
**Method**: Automated fetch + batch analysis

1. Create `sample_for_refinement.yaml` (50-100 verses)
2. Run `fetch_translations.py` on sample only
3. Create analysis script
4. Generate refinement report

### Option C: Full Dataset (NOT RECOMMENDED NOW)

**Time**: 10-20+ hours
**Verses**: 1,240 verses (all train/test/validate)
**Method**: Full automated pipeline

- Deferred until algorithm proven on smaller sample
- Would run overnight
- Provides comprehensive validation

---

## Current Status

✅ **Stage 1-6**: Complete (all stages finished)
✅ **fetch_verse.py**: Working correctly
✅ **English/Greek/Hebrew**: Available
⏳ **Refinement**: Ready to begin
⏳ **Sample selection**: Can proceed with Option A (recommended)

---

## Recommendation

**START WITH OPTION A** (Manual Spot-Check):
1. Select 20-25 key verses now
2. Fetch translations manually
3. Validate PROMPT1.md patterns
4. Document findings in REFINEMENT-RESULTS.md
5. If patterns hold → Algorithm validated ✅
6. If patterns fail → Create PROMPT2.md with fixes

**Why Option A?**:
- Fast (1-2 hours vs 10-20 hours)
- Focused (key verses, not exhaustive)
- Validates methodology without exhaustive testing
- Can iterate quickly if needed

---

## Example: Genesis 1:26 Validation

### Fetch
```bash
python3 .claude/skills/quote-bible/scripts/fetch_verse.py GEN.1.26 --lang eng,grc,heb
```

### Observe
- **English**: "Let **us** make mankind in **our** image" (all 50+ versions)
- **Hebrew**: `נַֽעֲשֶׂה` (na'aseh - cohortative **plural**)  
- **Greek LXX**: `Ποιήσωμεν` (Poiēsōmen - **1st person plural** subjunctive)

### PROMPT1.md Application
**Level 3, Rule 3.1**: Divine first-person plural in creation context → **Trial**

### TBTA Check
**train.yaml**: GEN.001.026 → **Trial** ✅

### Result
**Pattern CONFIRMED**: Divine plural in creation context correctly maps to Trial

---

## Conclusion

**Refinement phase is ready to begin** with:
- ✅ Working fetch_verse.py skill
- ✅ English/Greek/Hebrew available
- ✅ PROMPT1.md pattern-based algorithm
- ✅ Stratified datasets ready

**Recommended**: Manual spot-check of 20-25 key verses (Option A)

**Next Step**: Select verses and begin validation

---

**Last Updated**: 2025-11-17
**Status**: ⏳ READY FOR REFINEMENT

