# Strong's Tools Multi-Approach Validation - CORRECTED PLAN

**Date:** 2025-11-15
**Status:** Plan Corrected per STAGES.md v2.0
**Critical Fix:** Proper 30-50 word test set created with blind selection

---

## ✅ What Was Fixed

### Original Error
- Only selected 3 test words (G26, G3056, G2160)
- Did NOT create required 30-50 word stratified test set
- Violated STAGES.md Stage 1.3 requirements

### Correction Applied
- Created proper 40-word test set with full stratification
- Used blind selection protocol (researcher agent selected)
- Main agent receives word list WITHOUT metadata (prevents bias)
- 3-5 words from test set will be selected for Round 1 testing

---

## 📊 Test Set Created

**File:** `tools/scholarly-analysis/TEST-SET.yaml`
**Total Words:** 40 Greek Strong's numbers

### Stratification Matrix

#### By Frequency
- Rare (<10 occurrences): 12 words (30%)
- Medium (50-500 occurrences): 18 words (45%)
- High (1000+ occurrences): 10 words (25%)

#### By Word Type
- Theological: 16 words (40%)
- Grammatical: 12 words (30%)
- Nominal: 12 words (30%)

#### By Lexicon Coverage
- Rich (TDNT, LSJ, Trench): 16 words (40%)
- Moderate (Thayer, HELPS, Abbott-Smith): 16 words (40%)
- Sparse (limited sources): 8 words (20%)

#### Adversarial Cases (12 words = 30%)
- Controversial etymology: 3 words
- Lexicon divergence: 4 words
- Rare usage: 3 words
- Cultural sensitivity: 2 words

**Blind Protocol:** Main agent receives ONLY word numbers, no metadata

---

## 🎯 Corrected Workflow per STAGES.md v2.0

### Stage 1: Tool Selection & Test Set Development ✅ COMPLETE

**1.1 Tool Selected** ✅
- Tool: Scholarly Analysis
- Scope: ~1,000 theologically significant words
- Schema: Documented

**1.2 Word Classification** ✅
- Theological words: Full extraction
- Grammatical words: Statistics-focused
- Nominal words: Balanced approach

**1.3 Test Set Development** ✅ **FIXED**
- 40 words selected with proper stratification
- Blind selection protocol applied
- Adversarial cases included (30%)

**1.4 Three Approaches Designed** ✅
- Approach A: Journal-Emphasis (5 experiments complete)
- Approach B: Commentary-Synthesis (designed, ready)
- Approach C: Primary-Source-Diachronic (designed, ready)

---

### Stage 2: Round 1 - Initial Broad Experiments ⏳ NEXT

**Goal:** Test all 3 approaches on 3-5 words from test set (9-15 experiments)

**2.1 Execute Extraction Per Approach**

**Phase 1: Select 3-5 Words from Test Set (1 hour)**
- Review 40-word test set
- Select 3-5 diverse words for Round 1:
  - At least 1 rare word
  - At least 1 high-frequency word
  - At least 1 adversarial case
  - Mix of theological/grammatical/nominal
  - **Suggested:** 5 words (15 total experiments)

**Phase 2: Test Approach B on Selected Words (15-25 hours)**
- Execute Commentary-Synthesis on 5 words
- 3-5 hours per word × 5 words = 15-25 hours
- Save as: `{word}-scholarly-analysis-approach-B.yaml`

**Phase 3: Test Approach C on Selected Words (20-30 hours)**
- Execute Primary-Source-Diachronic on 5 words
- 4-6 hours per word × 5 words = 20-30 hours
- Save as: `{word}-scholarly-analysis-approach-C.yaml`

**Phase 4: Compare Approach A on Same Words (if needed)**
- Approach A already tested on 5 words: G26, G3056, G2160, G907, G2316
- If Round 1 selected words overlap: use existing data
- If no overlap: test Approach A on 1-2 new words for comparison

**Total Round 1 Time:** 35-55 hours (9-15 experiments)

---

**2.2 Source Access Optimization**
- Document which sources are URL-templatable
- Identify paywall barriers
- Assess scalability for production

**2.3 Review Committee** (Optional for Round 1)
- STAGES.md recommends 8-10 reviewers
- Can be simulated or deferred to Round 2

**2.4 Apply 3-Level Validation**
- L1: Critical (100% required)
- L2: High priority (80%+ target)
- L3: Medium priority (60%+ target)

**2.5 Cross-Approach Evaluation** ⏳ CRITICAL
- Compare all 3 approaches on same 3-5 words
- Use STAGES.md Stage 2.5 criteria:
  - **Richness:** Which provides most unique insights?
  - **Accuracy:** Which maintains highest standards?
  - **Efficiency:** Which is most time-efficient?
  - **Source Access:** Which has best source accessibility?
  - **Scalability:** Which works for full 1,000-word scope?

**CHECKPOINT:** Winner selected or blend designed

---

### Stages 3-8: Post-Round 1 Workflow

**Stage 3-5: Refinement Rounds** (if new winner selected)
- Test winner on 10-15 more words from test set
- Refine methodology based on learnings
- Optimize review process

**Stage 6: Winner Confirmation**
- Compare refined approaches
- Select final methodology

**Stage 7-8: Deep Refinement & Optimization**
- Test on remaining test set words
- Achieve production quality
- Execute Level 4 usefulness validation

**Stage 9: Production Deployment**
- Document final methodology
- Deploy to full 1,000-word scope

---

## 📋 Revised Timeline

### Week 1: Round 1 Execution - Approach B
- **Day 1:** Select 5 words from 40-word test set
- **Day 2-3:** Execute Approach B on words 1-2 (6-10 hours)
- **Day 4-5:** Execute Approach B on words 3-4 (6-10 hours)
- **Day 6:** Execute Approach B on word 5 (3-5 hours)
- **Day 7:** Validation and documentation

**Deliverable:** 5 words tested with Commentary-Synthesis approach

### Week 2: Round 1 Execution - Approach C
- **Day 1-2:** Execute Approach C on words 1-2 (8-12 hours)
- **Day 3-4:** Execute Approach C on words 3-4 (8-12 hours)
- **Day 5:** Execute Approach C on word 5 (4-6 hours)
- **Day 6-7:** Cross-approach evaluation & winner selection

**Deliverable:** 5 words tested with Primary-Source-Diachronic, winner selected

### Week 3-4: Winner Refinement or Production
**If Approach A wins:**
- Existing 5 experiments count as Rounds 2-5 evidence
- Proceed to optimization and Level 4 validation

**If Approach B or C wins:**
- Execute Rounds 2-5 refinement on 10-15 more words from test set
- Optimize methodology

**If Blend needed:**
- Design hybrid approach
- Test blend on 5-10 words

---

## 🎯 Tool 2 (Scholarly Analysis) - Updated Plan

### Immediate Next Step
1. ✅ Test set created (40 words, properly stratified)
2. ⏳ **Select 5 words from test set for Round 1**
3. ⏳ Execute Approach B on 5 words (15-25 hours)
4. ⏳ Execute Approach C on 5 words (20-30 hours)
5. ⏳ Cross-evaluate and select winner

### Round 1 Word Selection Criteria
From the 40-word test set, select 5 words that:
- Represent diverse frequency range (1 rare, 2-3 medium, 1-2 high)
- Include adversarial cases (2 adversarial, 3 standard)
- Mix word types (2 theological, 2 grammatical, 1 nominal)
- Test approach strengths:
  - 1 rare word (tests Primary-Source strength)
  - 1 debated word (tests Journal-Emphasis strength)
  - 1 well-documented word (tests Commentary-Synthesis efficiency)

---

## 🔧 Tool 1 (Lexicon Core) - Unchanged Plan

**Decision:** Grandfather existing work (Option B)
- 60+ experiments reorganized into STAGES.md structure
- Document Convergence-Synthesis as selected approach
- Acknowledge limitation: "Not empirically compared to alternatives"
- Execute Level 4 usefulness validation

**Timeline:** 22 hours (can work in parallel with Tool 2)

---

## ✅ What's Ready Now

**Tool 2 (Scholarly Analysis):**
- ✅ 40-word test set created with proper stratification
- ✅ Approach A: 5 experiments complete (Journal-Emphasis)
- ✅ Approach B: Designed and documented (Commentary-Synthesis)
- ✅ Approach C: Designed and documented (Primary-Source-Diachronic)
- ⏳ Next: Select 5 words from test set for Round 1

**Tool 1 (Lexicon Core):**
- ⏳ Needs reorganization and documentation (22 hours)

---

## 🤔 Next Decision Point

**Which 5 words from the 40-word test set should we use for Round 1?**

**Option 1: Random Selection from Stratified Buckets**
- Select 1 rare, 2 medium, 2 high (maintains stratification)
- Select 2 adversarial, 3 standard
- Truly blind selection

**Option 2: Strategic Selection**
- Choose words that test approach differentiators:
  - 1 rare hapax (tests Primary-Source advantage)
  - 1 heavily debated (tests Journal-Emphasis advantage)
  - 1 well-documented (tests Commentary-Synthesis efficiency)
  - 2 mid-range theological words (baseline comparison)

**Option 3: Review 40-word test set and decide together**

Which approach would you prefer for selecting the 5 Round 1 words?

---

**Plan Status:** Corrected and ready for execution
**Critical Fix Applied:** Proper 30-50 word test set now exists
**Commits:** All changes committed and pushed to git
