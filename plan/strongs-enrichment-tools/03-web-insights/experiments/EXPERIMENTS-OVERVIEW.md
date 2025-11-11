# Tool 3 Experiments Overview

**Status:** Design Phase Complete
**Ready to Execute:** Yes
**Total Experiments:** 5

---

## Experiment Summary - ADVERSARIAL TESTING APPROACH

**Design Philosophy:** Test hard cases, not easy wins. Use rare words and scholarly disagreement to stress-test the system.

| Exp | Strong's | Word | Type | Adversarial Test | Timeline |
|-----|----------|------|------|------------------|----------|
| **1** | G4151 | πνεῦμα (pneuma) | Scholarly disagreement | Document divergent views fairly | 3 hrs |
| **2** | G2160 | εὐτραπελία (eutrapelia) | Rare hapax (1x) | Honest insufficient coverage | 2 hrs |
| **3** | G1161 | δέ (de) | Grammatical particle | Appropriate scope boundary (skip) | 1 hr |
| **4** | G1411 | δύναμις (dynamis) | Known error | Error correction pattern | 2 hrs |
| **5** | G1577 | ἐκκλησία (ekklesia) | Cultural debate | Translator disagreement handling | 3 hrs |

**Total Estimated Time:** ~11 hours for all 5 experiments

**Why Adversarial?** Easy words (agape, logos) guarantee success but don't reveal weaknesses. Hard cases stress-test integrity, scope boundaries, and controversial content handling.

---

## What Each Experiment Tests

### Experiment 1: Scholarly Disagreement (G4151 - πνεῦμα/pneuma)
**Adversarial Test:** Word with ongoing scholarly debate

**Why This Is Hard:**
- "spirit" vs "Spirit" (capitalization debate)
- Human spirit vs Holy Spirit disambiguation
- Charismatic vs cessationist perspectives differ
- Multiple expert views, none definitively "correct"

**Tests:**
- Can we document divergent views fairly without bias?
- Do we avoid picking sides prematurely?
- Are multiple perspectives given appropriate weight?
- Is controversy acknowledged honestly?

**Expected Outcome:** 3-5 sources with DISAGREEMENT

**Success Criteria:**
- Documents at least 2 divergent expert positions
- No bias toward one view
- Evidence for each position presented
- Acknowledges ongoing debate (not settled)

---

### Experiment 2: Rare Hapax Legomenon (G2160 - εὐτραπελία/eutrapelia)
**Adversarial Test:** Occurs once (Eph 5:4), minimal web coverage expected

**Why This Is Hard:**
- Too rare for most expert blogs
- Not theologically central (won't find debates)
- Should find 0-1 sources beyond lexicons
- Tests honest "insufficient coverage" decision

**Tests:**
- Do we avoid fabrication when sources lacking?
- Can we honestly document "skip" decision?
- Is exhaustive search actually exhaustive?
- Do we force content to appear "complete"?

**Expected Outcome:** 0-1 sources (SKIP word likely)

**Success Criteria:**
- Exhaustive search documented (10+ queries)
- Honest assessment: "Insufficient web coverage"
- NO fabrication to fill gaps
- Skip decision = SUCCESS (not failure)

---

### Experiment 3: Grammatical Particle (G1161 - δέ/de)
**Adversarial Test:** Common particle "but/and/now" - outside Tool 3 scope

**Why This Is Hard:**
- Very common (2,792 occurrences)
- Grammatical function word (not lexical)
- Should recognize as outside Tool 3 scope
- Tests appropriate boundary detection

**Tests:**
- Do we recognize this is Tool 1 territory?
- Can we appropriately skip without feeling incomplete?
- Is scope boundary clearly documented?
- Do we avoid overreach into grammar?

**Expected Outcome:** SKIP (appropriate boundary)

**Success Criteria:**
- Recognizes particle is grammatical, not lexical
- Documents skip reason clearly
- Cites scope boundary (Tool 3 = practical insights, not grammar)
- Skip = SUCCESS (demonstrates appropriate scope)

---

### Experiment 4: Known Error (G1411 - δύναμις/dynamis)
**Adversarial Test:** Well-documented false etymology (dynamite fallacy)

**Why This Is Hard:**
- Error is widespread in popular teaching
- Need gracious tone while correcting
- Multiple refutations available (synthesis required)
- Tests error correction pattern completely

**Tests:**
- Can we find expert corrections (KEEP)?
- Is error + refutation + evidence complete?
- Is tone gracious (not mocking)?
- Do we provide correct teaching alongside correction?

**Expected Outcome:** 2-4 sources with error corrections

**Success Criteria:**
- Complete pattern: error + refutation + evidence
- Gracious tone maintained
- Correct understanding provided
- Authority MEDIUM+ for corrections

---

### Experiment 5: Cultural/Translation Debate (G1577 - ἐκκλησία/ekklesia)
**Adversarial Test:** "Church" vs "assembly" with cultural/theological implications

**Why This Is Hard:**
- Ongoing translator debate (not settled)
- Cultural baggage varies by context
- Post-colonial concerns vs traditional rendering
- Multiple valid perspectives exist

**Tests:**
- Can we document translator disagreement fairly?
- Do we avoid imposing one solution as "correct"?
- Are cultural sensitivities acknowledged?
- Is guidance helpful without being prescriptive?

**Expected Outcome:** 3-5 sources with DIVERGENT approaches

**Success Criteria:**
- Documents multiple translation approaches
- Acknowledges cultural/theological stakes
- No single "correct" answer imposed
- Guidance presents options, not edicts

---

## Experiment Execution Order

**Recommended Sequence:**

1. **Start with Exp 1 (Agape)** - High success probability, establishes methodology
2. **Then Exp 3 (Dynamis)** - Tests error correction (important feature)
3. **Then Exp 2 (Righteousness)** - Tests moderate coverage handling
4. **Then Exp 4 (Snow)** - Tests translator resources (specialized)
5. **End with Exp 5 (Rare)** - Tests integrity (critical validation)

**Rationale:**
- Build confidence with success (Exp 1)
- Test important features early (Exp 3)
- Handle edge cases progressively (Exp 2, 4)
- End with integrity test (Exp 5) to validate no fabrication creep

---

## Success Criteria Summary

### Overall Experiment Phase Success

**Must Achieve (CRITICAL):**
- ✅ 5/5 experiments demonstrate NO fabrication
- ✅ Authority detection framework works consistently
- ✅ Content adds value beyond lexicon data
- ✅ All sources have verifiable credentials
- ✅ Honest about coverage limitations

**Should Achieve (HIGH PRIORITY - 4/5):**
- ✅ Error correction pattern works (Exp 3)
- ✅ Translator guidance extractable (Exp 4)
- ✅ Multiple sources for high-coverage words (Exp 1, 3)
- ✅ Quality maintained with fewer sources (Exp 2)
- ✅ Skip decision acceptable for insufficient coverage (Exp 5)

**Nice to Have (MEDIUM PRIORITY - 3/5):**
- ✅ All audience categories covered (translators, preachers, students)
- ✅ Teaching helps present when appropriate
- ✅ Cross-references to other tools working
- ✅ Extraction process efficient (<3 hours per word)

---

## Decision Points After Experiments

### Minimum Source Threshold
**Question:** What's the minimum source count for Tool 3 inclusion?

**Test:**
- Exp 1: 5+ sources (excellent)
- Exp 2: 2-3 sources (moderate)
- Exp 5: 0-1 sources (insufficient)

**Decision to Make:**
- Is 1 source enough? (with caveats)
- Is 2 sources the minimum?
- How to mark coverage levels?

### Authority Level Application
**Question:** Are authority criteria clear and consistently applicable?

**Test:**
- All 5 experiments apply authority detection framework
- Do assignments feel consistent?
- Are edge cases handled?

**Decision to Make:**
- Refine criteria if inconsistent
- Add examples to authority-detection.md
- Clarify edge cases

### Coverage Strategy
**Question:** Which 2,000 words should Tool 3 target?

**Test:**
- Exp 1: Theologically central (definitely include)
- Exp 2: Important but less popular (probably include)
- Exp 5: Rare/obscure (skip)

**Decision to Make:**
- Define "high-priority" word categories
- Identify "medium-priority" categories
- Accept that ~12,000 words will NOT have Tool 3 coverage

### Error Correction Viability
**Question:** Is error correction reliably discoverable?

**Test:**
- Exp 3: Known error (dynamis/dynamite)

**Decision to Make:**
- Should we proactively search for errors?
- Create list of controversial words to check?
- Integrate with Tool 4 (community discussions)?

### Translator Resource Access
**Question:** Can we reliably find translator-focused content?

**Test:**
- Exp 4: Cultural challenge (snow)

**Decision to Make:**
- Is SIL/Wycliffe content accessible?
- Do we need different search strategies?
- Can we supplement Tool 6 (translation patterns)?

---

## Experiment Outputs

### Each Experiment Produces:

**1. Output YAML (if sources sufficient)**
- `{strongs}-output.yaml` - Following schema.yaml structure
- Demonstrates methodology working
- Validation against quality checklist

**2. Learnings Document (always)**
- `{strongs}-learnings.md` - What worked, what didn't
- Methodology refinements needed
- Patterns discovered
- Edge cases identified

**3. Sources Log (always)**
- `{strongs}-sources-log.md` - All searches attempted
- Sources found and evaluated
- Authority assessments
- Coverage assessment

**4. Validation Report (always)**
- `{strongs}-validation.md` - Quality checklist results
- Pass/fail per validation level
- Issues identified
- Recommendations

### Aggregate Outputs:

**5. Combined Learnings**
- `LEARNINGS.md` - Synthesis across all 5 experiments
- Common patterns
- Methodology refinements
- Decision recommendations

**6. Methodology Updates**
- Updates to README.md based on learnings
- Refinements to schema.yaml if needed
- Updates to research documents

---

## Timeline for Experiment Phase

**Week 1 (Days 1-3):**
- Experiment 1: Agape (Day 1)
- Experiment 3: Dynamis (Day 2)
- Experiment 2: Righteousness (Day 3)

**Week 2 (Days 4-5):**
- Experiment 4: Snow (Day 4)
- Experiment 5: Rare word (Day 5)

**Week 2 (Days 6-7):**
- Aggregate learnings
- Methodology refinements
- Prepare validation phase documentation

**Total:** 2 weeks

---

## After Experiments: Validation Phase

**Week 3:**
1. Review all 5 outputs against quality checklists
2. Cross-compare for consistency
3. Refine schema based on learnings
4. Update authority detection guidelines
5. Establish coverage strategy (which 2,000 words)
6. Create production phase plan

---

## Production Phase Preview

**After successful experiments, production targets:**

**High-Priority (~500 words):**
- Theologically central (love, grace, faith, sin, righteousness)
- Known controversies (dunamis, logos, agape/phileo)
- Cultural challenges (snow, lamb, bread in non-standard cultures)
- 5+ sources expected

**Medium-Priority (~1,000 words):**
- High-frequency with practical interest
- Good web coverage (2-4 sources)
- Translation-focused vocabulary

**Low-Priority (~500 words):**
- Opportunistic (if good source found, include)
- 1-2 sources minimum
- Skip if insufficient

**Explicitly Skip (~12,000 words):**
- Rare words with no web coverage
- Technical terms without special interest
- Rely on Tool 1 (lexicon-core) for these

---

## Key Success Factor

**Quality over Quantity**

Tool 3 should target ~2,000 words where web sources provide genuine value-add. Not all 14,197 Strong's words need Tool 3 coverage - that's what Tool 1 (lexicon-core) is for.

Success = Supplementing lexicon data with modern insights and practical applications for words where expert web sources exist.

NOT success = Forcing coverage for all words through fabrication.

---

## Next Actions

1. ✅ Experiment designs complete
2. ⏳ Execute experiments (2 weeks)
3. ⏳ Validation phase (1 week)
4. ⏳ Production phase (4 weeks)

---

**Status:** Ready to begin Experiment 1 (Agape)
**Confidence Level:** HIGH - Methodology is sound, experiments are well-designed
**Risk Areas:** Translator resources (Exp 4) may be harder to find than expected
