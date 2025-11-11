# Tool 3 Experiments Overview

**Status:** Design Phase Complete
**Ready to Execute:** Yes
**Total Experiments:** 5

---

## Experiment Summary

| Exp | Strong's | Word | Coverage | Primary Test | Timeline |
|-----|----------|------|----------|--------------|----------|
| **1** | G26 | ἀγάπη (agape) | High | Abundant sources, value-add | 2.5 hrs |
| **2** | G1343 | δικαιοσύνη (righteousness) | Medium | Moderate sources, quality maintenance | 2 hrs |
| **3** | G1411 | δύναμις (dynamis) | High | Error correction, controversy | 2 hrs |
| **4** | H7950 | שֶׁלֶג (snow) | Medium | Translator guidance, cultural challenges | 2.5 hrs |
| **5** | G4944 | συνωδίνω (rare) | Low | Honesty, no fabrication | 2 hrs |

**Total Estimated Time:** ~11 hours for all 5 experiments

---

## What Each Experiment Tests

### Experiment 1: Abundant Coverage (G26 - Agape)
**Tests:**
- Can we find 5+ quality sources?
- Does Tool 3 add value beyond Tool 1 (lexicon-core)?
- Are authority levels assigned correctly?
- Do practical applications emerge?

**Expected Outcome:** SUCCESS - Agape has excellent coverage

**Key Validation:**
- Authority detection works
- Content supplements (not duplicates) Tool 1
- Multiple audience applications (translators, preachers, students)

---

### Experiment 2: Moderate Coverage (G1343 - Righteousness)
**Tests:**
- Can we maintain quality with 2-3 sources?
- How to handle gaps gracefully?
- Is there still value with fewer sources?

**Expected Outcome:** SUCCESS with adaptations

**Key Validation:**
- Quality maintained despite fewer sources
- Honest about coverage limitations
- Establishes minimum viable source count

---

### Experiment 3: Controversy/Error Correction (G1411 - Dynamis)
**Tests:**
- Can we find expert error corrections?
- Is error + refutation + evidence pattern complete?
- Are corrections authoritative?

**Expected Outcome:** SUCCESS - Known false etymology

**Key Validation:**
- Complete error correction pattern
- Gracious tone (not mocking)
- Correct teaching alongside correction

---

### Experiment 4: Translator Practical (H7950 - Snow)
**Tests:**
- Can we find field-tested translator solutions?
- Are cultural translation challenges documented?
- Is authority appropriate for practical guidance?

**Expected Outcome:** SUCCESS if SIL/Wycliffe resources available

**Key Validation:**
- Field-tested solutions (not speculation)
- Multiple language examples
- MEDIUM-HIGH authority for practical applications

---

### Experiment 5: Low Coverage / Honesty (G4944 - Rare Word)
**Tests:**
- Do we avoid fabrication when sources scarce?
- Can we honestly say "insufficient coverage"?
- Is skip decision acceptable?

**Expected Outcome:** ZERO sources (most likely) - Test of integrity

**Key Validation:**
- No fabrication
- Honest coverage assessment
- Skip word if insufficient data
- Quality over quantity

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
