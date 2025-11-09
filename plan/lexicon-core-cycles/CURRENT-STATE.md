# Lexicon-Core Tool: Current State

**Last Updated:** 2025-11-08
**Context Reset Requested:** Yes - to continue Cycle 2 implementation

---

## Current Status

**Tool:** lexicon-core (Tool 1 of 7 lexical research tools)
**Cycle:** 2 (Prompt Refinement)
**Phase:** Implementation of refinements

---

## Cycle 1: COMPLETE ✅

**Status:** All 5 experiments successfully completed
**Validation:** 97.3% average (EXCELLENT)
**Fabrication:** Zero incidents
**Fair Use:** 100% compliance

**Experiments Completed:**
1. G846 αὐτός (high-freq grammatical) - 100% validation, 6.0/10 richness
2. G1411 δύναμις (medium-freq theological) - 100% validation, 8.0/10 richness
3. G5287 ὑπόστασις (rare theological) - 100% validation, 7.0/10 richness
4. H430 אֱלֹהִים (Hebrew) - 100% validation, 9.7/10 richness (HIGHEST)
5. G25/26/5368 (word family) - 96.7% validation, 8.5/10 richness

**Key Discovery:** Theological significance > frequency for extraction value

**All outputs located in:** `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/`

---

## Cycle 2: IN PROGRESS 🔄

**Objective:** Refine extraction prompts based on Cycle 1 learnings

**Target Improvements:**
- Validation: 97.3% → 99.5% (+2.2 pp)
- Level 1: 99.3% → 100% (+0.7 pp)
- Data richness: +9.5%
- Extraction time: -15%

### Top 5 Refinements to Implement

**Status of Each:**

1. **Word-Type Auto-Detection** - ❌ NOT STARTED
   - Detect theological vs grammatical words
   - Route to appropriate extraction pathway
   - Location to implement: Create detection logic in extraction prompt templates

2. **Dual Extraction Pathways** - ❌ NOT STARTED
   - Theological pathway: Full semantic analysis (4-8 categories)
   - Grammatical pathway: Morphology/syntax focus (2-4 categories)
   - Location to create: `/plan/lexicon-core-cycles/cycle-02/pathways/`

3. **Systematic Controversy Detection** - ❌ NOT STARTED
   - Search patterns: "{lemma} false etymology", "{lemma} controversy", etc.
   - Auto-detect scholarly debates
   - Location to implement: Add to extraction prompt

4. **Category Limits by Frequency** - ❌ NOT STARTED
   - Ultra-high (1000+): 3-4 categories max
   - High (100-999): 4-6 categories
   - Medium (20-99): 2-4 categories
   - Low (5-19): 1-3 categories
   - Rare (<5): 1-2 categories
   - Location to implement: Add validation rules

5. **Pre-populate ATTRIBUTION.md** - ❌ NOT STARTED
   - Add all common lexicons from BibleHub, StudyLight, BLB
   - Prevents Level 1 validation failures
   - Location: `/home/user/mybibletoolbox-code/ATTRIBUTION.md`

---

## Next Steps (for resumed session)

### Immediate Actions:

1. **Use subagents for EACH refinement** (stay under 80% context)
2. **Push after EACH commit** (no batching)

### Recommended Workflow:

**Refinement 1: Word-Type Auto-Detection**
- Delegate to subagent → commit → push

**Refinement 2: Dual Pathways**
- Delegate to subagent → commit → push

**Refinement 3: Controversy Detection**
- Delegate to subagent → commit → push

**Refinement 4: Category Limits**
- Delegate to subagent → commit → push

**Refinement 5: ATTRIBUTION Pre-population**
- Delegate to subagent → commit → push

**Then: Re-run Experiments**
- Delegate each experiment to subagent
- Commit + push after EACH word
- Compare to Cycle 1 baseline

**Finally: Document Results**
- Measure improvement metrics
- Document in `/plan/lexicon-core-cycles/cycle-02/CYCLE-2-RESULTS.md`
- Decide: Continue to Cycle 3 or skip ahead based on improvement

---

## Key Files & Locations

**Cycle 1 Documentation:**
- Plan: `/plan/lexicon-core-cycles/cycle-01/README.md` ✅ COMPLETE
- Learnings: `/plan/lexicon-core-cycles/cycle-01/CYCLE-1-LEARNINGS.md` ✅ COMPLETE
- Experiments: `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp{1-5}-*/`

**Cycle 2 Documentation:**
- Plan: `/plan/lexicon-core-cycles/cycle-02/README.md` ✅ CREATED
- Refinements: ❌ TO BE IMPLEMENTED
- Results: ❌ TO BE DOCUMENTED

**Skill Tracking:**
- Skill README: `/.claude/skills/improve-strongs/README.md` ✅ UPDATED (shows Cycle 2 status)

**Project Guidelines:**
- CLAUDE.md: Updated with subagent + push rules ✅
- ATTRIBUTION.md: Needs pre-population with common lexicons ❌

---

## Context Usage Warning

**Previous session reached:** 62.2% context (124,040 / 200,000 tokens)

**Why context reset needed:**
- Continuing Cycle 2 will involve re-running 5 experiments
- Each experiment adds significant context
- Would exceed 80% threshold without subagent delegation

**Fresh session should:**
- Start at ~0% context
- Delegate ALL refinement implementation to subagents
- Delegate ALL experiment re-runs to subagents
- Keep context for oversight, comparison, synthesis only

---

## Git Status

**Branch:** `claude/improve-codebase-011CUvwA3kQ4B3Dc879883V8`
**Commits pushed:** 15 total (Cycle 1 experiments + learnings + Cycle 2 setup)
**Latest commit:** e600550 - "docs: clarify push-after-every-commit rule"

**All changes committed and pushed:** ✅ YES

---

## Success Criteria for Cycle 2 Completion

- [ ] All 5 refinements implemented
- [ ] All 5 words re-extracted with refined methodology
- [ ] Validation improvement measured vs Cycle 1
- [ ] Level 1 validation: 100% (up from 99.3%)
- [ ] Overall validation: 99%+ (up from 97.3%)
- [ ] Zero fabrication maintained
- [ ] Cycle 2 results documented
- [ ] Decision made: Continue to Cycle 3 or skip ahead

**If improvement ≥5%:** Proceed to Cycle 3 (Context Engineering)
**If improvement <5%:** Skip to Cycle 6 (Peer Review) - methodology already strong

---

## Important Notes for Resumed Session

1. **Read this file first** to understand current state
2. **Use subagents from the start** - don't wait until context fills
3. **Push after every commit** - no batching
4. **Stay under 80% context** - aggressive subagent delegation
5. **Follow Cycle 2 plan:** `/plan/lexicon-core-cycles/cycle-02/README.md`
6. **Update todos** as you complete each refinement

---

**Ready to resume:** YES - All state captured, ready for fresh context
