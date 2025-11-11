# Lexicon-Core Tool: Cycle 3 - Context Engineering

**Cycle:** 3 of 7+
**Started:** 2025-11-09
**Status:** 🔄 READY TO BEGIN

---

## Purpose

Optimize extraction efficiency through context engineering while maintaining Cycle 2's quality achievements. Focus on eliminating redundancy, adaptive depth strategies, and parallelization to reduce extraction time without sacrificing data richness or validation scores.

---

## Baseline (from Cycle 2)

**Average Validation:** 100% (PERFECT)
- Level 1 (CRITICAL): 100%
- Level 2 (HIGH): 100%
- Level 3 (MEDIUM): 100%

**Data Richness by Type:**
- Theological terms: 9.0/10 average (+21.6% from Cycle 1)
- Grammatical terms: 8.5/10 average (+42% from Cycle 1)

**Extraction Time:**
- Theological pathway: ~75 min
- Grammatical pathway: ~55 min
- Average: ~65 min per word

**Data Efficiency:**
- Current ROI: ~1.2 points/min (9.0 richness / 75 min)
- Target ROI: ~1.4 points/min (9.0 richness / 64 min)

---

## Cycle 3 Objectives & Targets

### Primary Objectives
1. **Maintain Quality**: 100% validation, 9.0/10 richness (acceptable: 8.9-9.1)
2. **Improve Efficiency**: Reduce time from 75min → 64min (-15%)
3. **Increase ROI**: 1.2 pts/min → 1.4 pts/min (+17%)
4. **Zero Fabrication**: Maintain perfect record

### Target Improvements
| Metric | Cycle 2 Baseline | Cycle 3 Target | Change |
|--------|------------------|----------------|--------|
| **Validation** | 100% | 100% | Maintain |
| **Data Richness** | 9.0/10 | 8.9-9.1/10 | ±0.1 acceptable |
| **Extraction Time** | 75 min | 64 min | -15% |
| **ROI (pts/min)** | 1.20 | 1.40 | +17% |
| **Fabrication** | 0% | 0% | Maintain |

---

## Top 5 Refinements to Implement

### 1. Redundancy Elimination
**Problem:** Overlapping content between sections wastes time and tokens
**Time Impact:** 3 minutes saved per word

**Redundancies Identified:**
- **Classical + Papyri overlap**: Both describe pre-Christian Greek usage with similar patterns
- **Etymology vs Diachronic overlap**: Etymology section often repeats in Classical Greek analysis
- **Semantic Range vs Synonym overlap**: Synonym distinctions repeat category definitions
- **Source redundancy**: LSJ consulted for both etymology AND diachronic; TDNT for both theology AND synonyms

**Solution:**

```yaml
consolidations:
  diachronic_periods:
    before: ["Classical Greek (5 min)", "Papyri (4 min)", "LXX (3 min)", "NT/Koine (3 min)"]
    after: ["Pre-NT Development (4 min)", "LXX (3 min)", "NT Specialization (3 min)"]
    merge: "Classical + Papyri → Pre-NT Development"

  source_strategy:
    eliminate_double_lookups:
      - "LSJ: Use ONLY in etymology, reference in diachronic"
      - "TDNT: Use ONLY in theological dictionaries, reference in synonyms"
      - "Trench: Use ONLY in synonym network, reference elsewhere"
```

**Implementation:**
- Consolidate Classical Greek + Papyri into single "Pre-NT Development" section (4 min total, not 9 min)
- Remove etymology repetition from diachronic section (use cross-reference)
- Document synonyms WITHIN semantic categories when appropriate

**Expected Savings:** 3 minutes per word
**Richness Impact:** -0.1 points (minimal - redundant content removed, unique content preserved)

**Test:** Re-extract G1411 δύναμις - should maintain all unique insights with consolidated structure

---

### 2. Adaptive Depth Strategies
**Problem:** Same depth of analysis applied to all words regardless of type/significance
**Time Impact:** 5-7 minutes saved per word (varies by word type)

**Current Issue:**
- Grammatical words get full diachronic analysis (limited value)
- Ultra-high frequency words get exhaustive morphology (diminishing returns)
- Rare words get extensive controversy searches (usually none exist)

**Solution:**

```yaml
adaptive_strategies:
  diachronic_analysis:
    grammatical_words: "Frequency shifts only (3 min vs 10 min)"
    rare_words: "Focus on NT usage only (5 min vs 10 min)"
    theological_words: "Full 3-stage analysis (10 min)"

  controversy_detection:
    grammatical_words: "SKIP - pronouns/particles rarely controversial (save 10 min)"
    high_freq_words: "2-3 patterns (7 min vs 10 min)"
    theological_words: "Full 5-6 patterns (10 min)"

  morphology_extraction:
    ultra_high_freq: "Top 10 forms only (10 min vs 15 min)"
    normal_freq: "All forms with significance threshold"
    rare_words: "Complete paradigm (limited forms anyway)"
```

**Word-Type Rules:**

| Word Type | Diachronic | Controversy | Morphology | Time Saved |
|-----------|------------|-------------|------------|------------|
| **Grammatical** | Frequency shifts | SKIP | Top 10 forms | 7 min |
| **Theological** | Full 3-stage | Full patterns | N/A | 0 min |
| **Rare (<20 occur)** | NT focus | 3 patterns | Full paradigm | 5 min |
| **Ultra-high (1000+)** | Frequency only | 2 patterns | Top 10 | 5 min |

**Implementation:**
- Use existing word-type detection from Cycle 2
- Add frequency tier detection (already have occurrence counts)
- Route to appropriate depth strategy automatically
- Document reasoning in metadata (transparency)

**Expected Savings:** 5-7 minutes per word (average across word types)
**Richness Impact:** Neutral to positive (better depth alignment = more relevant content)

**Test:**
- G846 αὐτός (grammatical) - should skip controversy, limit morphology
- G1411 δύναμις (theological) - should get full analysis
- G5287 ὑπόστασις (rare) - should focus on NT usage

---

### 3. Template Optimization
**Problem:** Verbose section headers and redundant subsections add overhead
**Time Impact:** 1-2 minutes saved per word

**Current Inefficiencies:**
- Long explanatory headers in prompts
- Separate subsections that could be combined
- Repetitive formatting instructions

**Solution:**

```yaml
template_optimizations:
  section_headers:
    before: "## Semantic Range Analysis (4-8 categories based on frequency)"
    after: "## Semantic Range"

  subsection_consolidation:
    combine:
      - "Etymology + Root Analysis → Etymology"
      - "Scholarly Controversies + Translation Debates → Controversies"
      - "Cross-references + Related Words → Related Terms"

  instruction_streamlining:
    remove_repetition: "Don't repeat inline citation reminder in every section"
    use_templates: "Standard YAML structure templates, not full descriptions"
```

**Specific Changes:**
1. **Simplify headers**: Remove explanatory text from section titles
2. **Combine related subsections**: Etymology sections, controversy sections
3. **Template-based schema**: Provide YAML template once, not repeated per section
4. **Eliminate redundant reminders**: Citation format explained once, not per section

**Implementation:**
- Streamline extraction prompts (remove verbose headers)
- Create consolidated sections in schema
- Use reference-style instructions ("See citation format above")

**Expected Savings:** 1-2 minutes per word
**Richness Impact:** Zero (organizational change only)

**Test:** Time comparison on same word with old vs new template

---

### 4. Source Prioritization
**Problem:** All sources checked equally, regardless of value for specific tasks
**Time Impact:** 2 minutes saved per word

**Current Approach:**
- Check multiple lexicons for synonym distinctions even when Trench exists
- Search HELPS for grammatical words (rarely have entries)
- Consult general lexicons before specialized dictionaries

**Solution:**

```yaml
source_hierarchy:
  synonym_analysis:
    first: "Trench Synonyms (if section exists, use primarily this)"
    then: "TDNT synonym notes (if theological)"
    last: "Individual lexicons (only if gaps remain)"

  theological_depth:
    first: "TDNT (comprehensive theological treatment)"
    then: "HELPS (practical application)"
    then: "Individual lexicons (for specific nuances)"

  grammatical_analysis:
    first: "Abbott-Smith (morphology focus)"
    skip: "HELPS (rarely has grammatical word entries)"
    then: "LSJ (classical usage patterns)"
```

**Smart Source Selection:**

| Task | Primary Source | Time if Found | Secondary Sources | Total Time |
|------|---------------|---------------|-------------------|------------|
| **Synonyms** | Trench | 3 min (done) | TDNT if theological | 3-5 min |
| **Theology** | TDNT | 4 min (done) | HELPS for application | 6 min |
| **Grammar** | Abbott-Smith | 3 min (done) | Skip HELPS | 3 min |

**Implementation:**
- Check Trench FIRST for synonyms - if comprehensive section exists, use it primarily
- TDNT before individual lexicons for theological words
- Skip HELPS lookups for grammatical-pathway words
- Document source hierarchy in prompts

**Expected Savings:** 2 minutes per word
**Richness Impact:** Neutral (same or better quality from authoritative sources)

**Test:** G1411 δύναμις - Trench section should minimize need for other synonym sources

---

### 5. Parallel Extraction
**Problem:** Sequential searches when parallel execution possible
**Time Impact:** 3 minutes saved per word

**Currently Sequential:**
1. **Controversy searches**: 5-6 patterns run one at a time (10 min total)
2. **TDNT + Trench + HELPS**: Looked up separately (6 min total)
3. **Synonym lookups**: Each synonym researched individually (4 min total)

**Parallelization Opportunities:**

```yaml
parallel_execution:
  controversy_patterns:
    current: "Sequential: pattern1 → pattern2 → pattern3 (10 min)"
    optimized: "Parallel: all 5-6 patterns simultaneously (7 min)"
    savings: "3 minutes"

  specialized_sources:
    current: "Sequential: TDNT → HELPS → Trench (6 min)"
    optimized: "Parallel: all 3 sources simultaneously (4 min)"
    savings: "2 minutes (but may overlap with other savings)"

  synonym_network:
    current: "Sequential: synonym1 → synonym2 → synonym3 (6 min)"
    optimized: "Batch lookup of top 5 synonyms (4 min)"
    savings: "2 minutes (but overlaps with other optimizations)"
```

**Implementation:**
- **PRIMARY TARGET**: Parallelize controversy searches (5-6 WebSearch calls in single response)
- Execute TDNT/HELPS/Trench lookups simultaneously
- Batch synonym research where possible

**Technical Approach:**
```yaml
# Instead of sequential:
WebSearch: "{lemma} false etymology"
WebSearch: "{lemma} controversy"
WebSearch: "{lemma} scholarly debate"

# Parallel execution:
WebSearch calls:
  - "{lemma} false etymology"
  - "{lemma} controversy"
  - "{lemma} scholarly debate"
  - "{lemma} vs {synonym} distinction"
  - "{lemma} meaning disputed"
```

**Expected Savings:** 3 minutes per word (primarily from controversy parallelization)
**Richness Impact:** Zero (same searches, faster execution)

**Test:** Time 5 sequential searches vs 5 parallel searches - should save ~3 min

---

## Combined Time Savings Summary

| Refinement | Time Saved | Risk Level | Richness Impact |
|------------|------------|------------|-----------------|
| **1. Redundancy Elimination** | 3 min | Low | -0.1 pts |
| **2. Adaptive Depth Strategies** | 5-7 min | Low | Neutral/Positive |
| **3. Template Optimization** | 1-2 min | None | Zero |
| **4. Source Prioritization** | 2 min | Low | Neutral |
| **5. Parallel Extraction** | 3 min | None | Zero |
| **TOTAL** | **14-17 min** | **Low** | **-0.1 to 0 pts** |

**Expected Results:**
- Current time: 75 min
- Savings: 14-17 min
- New target: 58-61 min
- **Conservative target: 64 min (-15%)** ← achievable with 11 min savings

**ROI Improvement:**
- Current: 9.0 pts / 75 min = 1.20 pts/min
- Target: 8.9-9.0 pts / 64 min = 1.39-1.41 pts/min (+17%)

---

## Implementation Strategy

### Phase 1: Low-Risk Quick Wins (Priority 1)
**Target savings:** 7-8 minutes
**Implementation time:** 1-2 hours

**Steps:**
1. ✅ **Parallelize controversy searches** (3 min saved, zero risk)
2. ✅ **Consolidate Classical + Papyri periods** (3 min saved, low risk)
3. ✅ **Streamline template headers** (1-2 min saved, zero risk)

**Expected result:** 75 min → 67-68 min

### Phase 2: Adaptive Strategies (Priority 2)
**Target savings:** 6-9 minutes
**Implementation time:** 2-3 hours

**Steps:**
4. ✅ **Implement adaptive diachronic depth** (word-type based, 2-3 min saved)
5. ✅ **Smart controversy detection** (skip for grammatical words, 3-4 min saved on those words)
6. ✅ **Top-10 morphology for high-form-count words** (3-4 min saved on grammatical words)
7. ✅ **Trench-first synonym strategy** (2 min saved)
8. ✅ **Limit synonyms to top 5** (2 min saved, from Refinement #1)

**Expected result:** 67 min → 58-61 min

### Phase 3: Validation & Measurement (Critical)
**Steps:**
9. ✅ Re-extract all 5 Cycle 2 words with optimized prompts
10. ✅ Validate richness maintained (8.9-9.1/10 target)
11. ✅ Confirm 100% validation maintained
12. ✅ Verify zero fabrication
13. ✅ Document time vs richness trade-offs

**Expected final result:**
- **Time:** 58-64 minutes (-15% to -23% from Cycle 2)
- **Richness:** 8.9-9.1/10 (maintain ±0.1-0.2 points)
- **Validation:** 100% (maintain perfect score)

---

## Experiment Plan

### Test Words (Same as Cycle 2)
Re-extract with Cycle 3 optimizations to measure improvement:

**1. G846 αὐτός (grammatical, ultra-high freq)**
- Expected savings: 7 min (skip controversy, top-10 forms, frequency-only diachronic)
- Target time: 55 min → 48 min
- Richness target: 8.5/10 (maintain or slight improvement)

**2. G1411 δύναμις (theological, medium freq)**
- Expected savings: 11 min (consolidation, parallelization, Trench-first)
- Target time: 75 min → 64 min
- Richness target: 8.5/10 (maintain)

**3. G5287 ὑπόστασις (rare, theological)**
- Expected savings: 12 min (NT-focus diachronic, limited synonyms, adaptive controversy)
- Target time: 75 min → 63 min
- Richness target: 8.5/10 (maintain)

**4. H430 אֱלֹהִים (Hebrew, high theological significance)**
- Expected savings: 11 min (full analysis justified, but streamlined)
- Target time: 75 min → 64 min
- Richness target: 9.8/10 (maintain excellence)

**5. G25/26/5368 ἀγαπάω/ἀγάπη/φιλέω (word family)**
- Expected savings: 11 min per word (controversy parallelization key)
- Target time: 75 min avg → 64 min avg
- Richness target: 9.5/10 (maintain)

### Measurement Protocol

**For each word, track:**
```yaml
metrics:
  time:
    total_extraction: "X minutes"
    per_section:
      diachronic: "X min"
      controversy: "X min"
      synonyms: "X min"
      morphology: "X min (if grammatical)"
      schema_writing: "X min"
      validation: "X min"

  richness:
    overall_score: "X.X/10"
    category_count: "X categories"
    citation_count: "X inline citations"
    controversy_count: "X controversies"

  quality:
    validation_level_1: "X%"
    validation_level_2: "X%"
    validation_level_3: "X%"
    fabrication_incidents: "0"
```

**Success Criteria:**
- Average time: ≤64 min (-15% from 75 min)
- Average richness: 8.9-9.1/10 (±0.1-0.2 acceptable)
- All validation: 100%
- Fabrication: 0 incidents
- Time savings documented per refinement

---

## Success Criteria for Cycle 3

### Critical (Must Pass)
- [x] All 5 refinements implemented in extraction prompts
- [ ] All 5 words re-extracted with optimized methodology
- [ ] Validation maintained at 100% (all levels)
- [ ] Zero fabrication incidents
- [ ] Time reduction measured vs Cycle 2 baseline

### Primary Targets
- [ ] Average extraction time: ≤64 min (vs 75 min baseline)
- [ ] Average richness: 8.9-9.1/10 (vs 9.0 baseline)
- [ ] ROI improvement: ≥1.39 pts/min (vs 1.20 baseline)
- [ ] Time savings: ≥11 min per word (-15%)

### Quality Maintenance
- [ ] Controversy detection: 18-22 total (vs 20 in Cycle 2)
- [ ] Inline citations: Maintain average per word
- [ ] Category appropriateness: Maintain quality of semantic/functional categorization
- [ ] Source quality: No reduction in authoritative source usage

### Documentation
- [ ] Time breakdown by section (measure savings per refinement)
- [ ] Richness comparison by category
- [ ] Learnings documented in CYCLE-3-RESULTS.md
- [ ] Decision on Cycle 4 continuation

---

## Risk Assessment

### Low-Risk Optimizations ✅
**Implement immediately - minimal quality impact:**
- ✅ Parallel controversy searches (zero impact, pure speed gain)
- ✅ Template streamlining (organizational only)
- ✅ Classical + Papyri consolidation (redundant content)
- ✅ Trench-first synonyms (authoritative source)
- ✅ Limit to top 5 synonyms (peripheral terms low value)

### Medium-Risk Optimizations ⚠️
**Test carefully - potential quality trade-offs:**
- ⚠️ Adaptive diachronic depth (requires accurate word-type detection)
- ⚠️ Skip HELPS for grammatical words (may miss rare entries)
- ⚠️ Top-10 morphology limit (may lose rare but significant forms)
- ⚠️ Smart controversy skip (grammatical words rarely controversial, but not never)

**Mitigation:**
- Use conservative thresholds for skipping (clear grammatical markers only)
- Document all adaptive decisions in metadata
- Manual review of first experiment from each pathway
- Revert if richness drops >0.2 points

### High-Risk Optimizations ❌
**DO NOT implement - unacceptable quality risk:**
- ❌ Skip diachronic analysis entirely (significant richness loss)
- ❌ Reduce controversy patterns below 3 (miss important debates)
- ❌ Skip validation steps (quality degradation)
- ❌ Cut semantic categories below minimums (inadequate coverage)
- ❌ Eliminate source cross-checking (fabrication risk)

---

## Expected Improvements

### Quantitative Targets
| Metric | Cycle 2 | Cycle 3 Target | Change |
|--------|---------|----------------|--------|
| **Validation (avg)** | 100% | 100% | Maintain |
| **Data Richness** | 9.0/10 | 8.9-9.1/10 | ±1% acceptable |
| **Extraction Time** | 75 min | 64 min | -15% |
| **ROI (pts/min)** | 1.20 | 1.40 | +17% |
| **Theological Time** | 75 min | 64 min | -15% |
| **Grammatical Time** | 55 min | 48 min | -13% |

### Qualitative Improvements
- **Better depth alignment**: Analysis depth matches word significance
- **Reduced redundancy**: Unique content preserved, duplicates eliminated
- **Faster execution**: Parallelization reduces wait time
- **Maintained quality**: All critical validations pass
- **Improved efficiency**: Higher data value per minute invested

### Pathway-Specific Targets

**Theological Pathway:**
- Time: 75 min → 64 min (-11 min)
- Savings from: Consolidation (3 min) + Parallelization (3 min) + Synonyms (2 min) + Sources (2 min) + Template (1 min)

**Grammatical Pathway:**
- Time: 55 min → 48 min (-7 min)
- Savings from: Skip controversy (7 min on full skip) + Morphology limit (3 min) + Diachronic (2 min) + Template (1 min)

---

## Learnings to Capture

### For Each Refinement
**Document:**
- ✅ What worked as expected?
- ✅ What didn't work?
- ✅ Unexpected benefits?
- ✅ New issues discovered?
- ✅ Further refinements needed?
- ✅ Time savings actual vs predicted

### Overall Cycle 3 Analysis
**Questions to answer:**
- Did time savings compound or conflict?
- Were there diminishing returns on optimizations?
- Did quality suffer in any specific areas?
- Which word types benefited most from optimizations?
- Are there additional bottlenecks revealed?
- What's the optimal balance point for time vs richness?

---

## Next Steps After Cycle 3

### If Time Savings ≥15% AND Quality Maintained
- **Proceed to Cycle 4:** Error Pattern Analysis
- Apply optimized prompts to new words
- Focus on edge cases and error prevention

### If Time Savings <15% OR Quality Degraded >0.3 points
- **Iterate Cycle 3:** Adjust optimizations
- Revert high-impact low-value changes
- Find better balance point

### If Time Savings >20% AND Quality Improved
- **Skip to Cycle 6:** Peer Review
- Current methodology already excellent
- Focus on external validation

---

## Context Management Strategy

**Cycle 3 Context Plan:**
- Main session: Planning, oversight, synthesis only (~30% context)
- Subagent delegation: ALL re-extraction experiments (~70% work)
- Parallel subagents: Run 2-3 words simultaneously where possible
- Push after every commit: No batching

**Subagent Tasks:**
1. Re-extract G846 with Cycle 3 optimizations
2. Re-extract G1411 with Cycle 3 optimizations
3. Re-extract G5287 with Cycle 3 optimizations
4. Re-extract H430 with Cycle 3 optimizations
5. Re-extract G25/26/5368 with Cycle 3 optimizations

**Main Session Tasks:**
- Create Cycle 3 plan (this document)
- Review experiment results from subagents
- Synthesize time savings vs richness trade-offs
- Document learnings in CYCLE-3-RESULTS.md
- Make decision on Cycle 4 continuation

---

## Files & Locations

**Cycle 3 Planning:**
- Plan: `/plan/lexicon-core-cycles/cycle-03/README.md` ✅ THIS FILE
- Bottleneck analysis: `/plan/lexicon-core-cycles/cycle-03/time-bottleneck-analysis.md` ✅ COMPLETE

**Cycle 3 Experiments:**
- Output location: `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/cycle-03/`
- Experiments: `exp1-G846/`, `exp2-G1411/`, `exp3-G5287/`, `exp4-H430/`, `exp5-family/`

**Cycle 3 Results:**
- Results doc: `/plan/lexicon-core-cycles/cycle-03/CYCLE-3-RESULTS.md` ❌ TO BE CREATED
- Learnings: To be captured in results document

**Reference Documents:**
- Cycle 2 results: `/plan/lexicon-core-cycles/cycle-02/CYCLE-2-RESULTS.md`
- Current state: `/plan/lexicon-core-cycles/CURRENT-STATE.md`
- Project guidelines: `/home/user/mybibletoolbox-code/CLAUDE.md`

---

## Validation Checklist

**Before declaring Cycle 3 complete:**
- [ ] All 5 optimizations implemented in prompts
- [ ] All 5 words re-extracted and validated
- [ ] Time measurements documented per section
- [ ] Richness scores calculated and compared
- [ ] Validation rates confirmed at 100%
- [ ] Fabrication incidents = 0
- [ ] Time savings totaled and analyzed
- [ ] Trade-offs documented (time vs richness)
- [ ] Learnings captured in CYCLE-3-RESULTS.md
- [ ] Decision made on Cycle 4 continuation
- [ ] All changes committed and pushed
- [ ] CURRENT-STATE.md updated for next cycle

---

**Status:** Ready to implement Cycle 3 optimizations
**Next Action:** Implement Priority 1 optimizations in extraction prompts
**Expected Completion:** 5 experiments + analysis = ~2-3 days with subagent delegation
