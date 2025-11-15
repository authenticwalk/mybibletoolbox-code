# Strong's Extended Enrichment: Production Workflow (STAGES)

**Status:** Production-Ready Methodology
**Based on:** 80+ experiments across lexicon-core, web-insights, and TBTA-hints tools
**Last Updated:** 2025-11-15
**Quality Standard:** 100% Level-1 validation, 80%+ Level-2, 60%+ Level-3

---

## Overview: Single-Tool-to-Completion Methodology

**CRITICAL PRINCIPLE:** Take ONE tool to full production readiness before starting the next.

**Why This Works:**
- Deep expertise in one domain
- Reproducible methodology
- Production-quality outputs
- Manageable context

**Historical Evidence:** 80+ experiments validated 7 proven patterns (word type classification, convergence/divergence, 90% morphology coverage, multi-discipline search, 5-part error correction, multi-perspective framework, 3-level validation). See **LEARNINGS.md** for detailed evidence and discoveries.

**This File:** Pure execution workflow (what to DO, not what was learned).

---

## STAGE 1: Tool Selection & Test Set Development (2-3 hours)

### 1.1 Select Tool for Production

**DO:**
1. Review available tools in `/bible-study-tools/strongs-extended/tools/`
2. Select ONE tool for full production (6-9 week commitment)
3. Read schema/README/templates for tool

**CHECKPOINT:** Tool selected, schema understood

### 1.2 Classify Word Strategy

**DO:**
1. Identify tool's primary word types:
   - **Theological** (rare-medium frequency, rich semantics)
   - **Grammatical** (high frequency, functional)
   - **Nominal** (medium frequency, balanced)

2. Select extraction strategy per word type:
   - Theological: Full extraction (5-8 categories, LSJ emphasis)
   - Grammatical: Statistics-focused (morphology, usage patterns)
   - Nominal: Balanced approach

**NOTE:** Classification optimizes extraction depth. Even for full corpus work, word type determines resource allocation and validation criteria.

**REFERENCE:** See LEARNINGS.md §1 for word type classification evidence

**CHECKPOINT:** Word classification strategy documented

### 1.3 Develop Authoritative Test Set

**CRITICAL:** Test sets MUST be stratified, adversarial, and blind-developed.

**DO:**
1. **Stratify by frequency** (30-50+ words total):
   - **Rare** (<10 occurrences): 10-15 words
   - **Medium** (50-500 occurrences): 15-20 words
   - **High** (1000+ occurrences): 5-10 words

2. **Stratify by word type:**
   - Theological: 40% of test set
   - Grammatical: 30% of test set
   - Nominal: 30% of test set

3. **Stratify by lexicon coverage:**
   - Rich coverage (TDNT, LSJ, Trench): 40%
   - Moderate coverage (Thayer, HELPS, Abbott-Smith): 40%
   - Sparse coverage (limited sources): 20%

4. **Include adversarial cases** (30% of test set):
   - Controversial etymology (folk etymology risks)
   - Lexicon divergence (disagreement patterns)
   - Rare usage contexts (hapax legomena)
   - Cultural sensitivity (translation debates)

5. **Test set selection protocol:**
   - **SPAWN:** Subagent to select test words (main agent never sees selection criteria)
   - Main agent receives only: word list (no metadata, no frequencies)
   - Prevents bias toward "easy" words
   - **CRITICAL:** Test words must NOT be used in LEARNINGS.md or methodology documentation until validation complete

**TEMPLATE:**
```yaml
test_set:
  metadata:
    total_words: 42
    stratification:
      frequency:
        rare: 12 (29%)
        medium: 18 (43%)
        high: 12 (29%)
      word_type:
        theological: 17 (40%)
        grammatical: 13 (31%)
        nominal: 12 (29%)
      coverage:
        rich: 17 (40%)
        moderate: 17 (40%)
        sparse: 8 (19%)
      adversarial: 13 (31%)
  words:
    - strongs: G5287
      greek: ὑπόστασις
      english: substance, confidence, reality
      # (rare, theological, rich, adversarial: theological depth)
    - strongs: G0846
      greek: αὐτός
      english: he, she, it, self
      # (high, grammatical, sparse, normal)
    - strongs: G1411
      greek: δύναμις
      english: power, strength, ability
      # (medium, theological, rich, adversarial: folk etymology)
    # ... 39 more words
```

**CHECKPOINT:** Test set of 30-50+ words documented with stratification matrix

---

## STAGE 2: Initial Experiments (Cycle 1) (8-12 hours)

### 2.1 Execute Extraction Per Schema

**DO:**
1. Review tool-specific methodology from previous experiments:
   - **Lexicon Core:** Word type classification → extraction depth (LEARNINGS.md §1)
   - **Web Insights:** Multi-discipline search (5 disciplines, LEARNINGS.md §4)
   - **TBTA Hints:** LLM logic tree pattern detection from 900+ translations

2. For each test word, apply proven patterns:
   - Read base Strong's file FIRST (`.data/strongs/{STRONGS_ID}/{STRONGS_ID}-strongs.strongs.yaml`)
   - Execute tool extraction per schema/README
   - Apply inline citations: `content {source}`
   - Document time taken
   - Note any difficulties/edge cases

3. Save outputs to: `{word}.strongs-{tool}.yaml`

**REFERENCE:** See LEARNINGS.md for all 7 proven patterns with evidence from 80+ experiments

**CHECKPOINT:** Initial outputs created for all test words

### 2.2 Apply 3-Level Validation

**DO:**
1. **Level 1 (CRITICAL - Must Pass 100%):**
   - ✅ No fabricated data (every claim sourced)
   - ✅ Inline citations: `content {source}`
   - ✅ No percentages/numeric predictions
   - ✅ Base file read FIRST
   - ✅ All sources documented with proper citations
     - **URL-templatable sources** → ATTRIBUTION.md (e.g., BibleHub, StudyLight with URL patterns)
     - **One-off sources** → Bottom of YAML file (unique articles, specific blog posts)

2. **Level 2 (HIGH PRIORITY - Iterate Until <5% Improvement):**
   - ✅ Etymology from 2+ lexicons
   - ✅ Semantic categories appropriate for word type/frequency
   - ✅ Usage statistics match sources exactly
   - ✅ Convergence/divergence documented

3. **Level 3 (MEDIUM PRIORITY - Continue Refinement):**
   - ✅ Cross-reference codes extracted
   - ✅ Diachronic analysis when relevant
   - ✅ Fair use compliant
   - ✅ Related words documented

**STOPPING RULE:** Continue refinement cycles until improvements <5% per cycle (diminishing returns)

**REFERENCE:** See LEARNINGS.md §7 for validation framework details

**CHECKPOINT:** Validation results documented with improvement metrics

### 2.3 Analyze Extraction Quality

**Peer Review Validation:**

**DO:**
1. Document extraction analysis:
   - What was harder than expected?
   - What sources were missed?
   - What word types had surprises?

2. **Validate source quality:**
   - Can credentials be verified? Are sources authoritative?
   - Do 3+ independent sources agree (convergence)?
   - Can every claim be traced to a source (no fabrication)?

3. **User impact testing** (see TEMPLATE.md peer review methodology):
   - Would a Bible translator copy this to their notes?
   - Would a pastor use this in sermon preparation?
   - Would a seminary student trust this analysis?
   - What mistakes were avoided due to this enrichment?
   - What data was most valuable?

**REFERENCE:** See bible-study-tools/TEMPLATE.md for peer review methodology

**CHECKPOINT:** Quality analysis documented with user impact assessment

### 2.4 Document Cycle 1 Learnings

**DO:**
1. Create `/plan/strongs-enrichment-tools/{tool}/experiments/cycle-01/`
2. Document:
   - Time per word (average, min, max)
   - Validation pass rates (L1, L2, L3)
   - Common failures (patterns)
   - Tool-specific insights

**CHECKPOINT:** Cycle 1 summary documented

---

## STAGE 3: Methodology Refinement (Cycles 2-4) (12-20 hours)

### 3.1 Cycle 2: Prompt Refinement

**DO:**
1. Analyze Cycle 1 failures (validation, time, coverage)
2. Refine prompts to address:
   - Level 1 failures (fabrication, missing citations)
   - Level 2 failures (insufficient etymology, wrong categories)
   - Time inefficiencies (over-extraction, under-extraction)

3. Re-run 10-15 test words with refined prompts
4. Document improvements (validation metrics, time reduction)

**CHECKPOINT:** Cycle 2 results show measurable improvement (validation +10%, time -15%)

### 3.2 Cycle 3: Context Engineering

**DO:**
1. Analyze Cycle 2 failures (remaining gaps)
2. Engineer context to address:
   - Word type classification (theological vs grammatical strategy)
   - Coverage sweet spots (90% morphology, not 100%)
   - Multi-discipline search (5 disciplines for rare words)

3. Re-run 10-15 test words with engineered context
4. Document improvements

**CHECKPOINT:** Cycle 3 results show further improvement (validation +5%, time -10%)

### 3.3 Cycle 4: Edge Case Handling

**DO:**
1. Focus on adversarial test cases (30% of test set):
   - Controversial etymology
   - Lexicon divergence
   - Rare usage contexts
   - Cultural sensitivity

2. Apply proven patterns:
   - **5-part error correction** (error statement, classification, refutation, expert validation, correct alternative)
   - **Multi-perspective framework** (scholarly debates documented fairly)
   - **Bias detection tests** (reversal, respect, evidence)

3. Re-run adversarial words with edge case handling
4. Document improvements

**REFERENCE:** See LEARNINGS.md §5-6 for error correction and multi-perspective frameworks

**CHECKPOINT:** Cycle 4 results show edge case mastery (adversarial words pass validation)

### 3.4 6-Step Error Analysis

**FOR ERRORS:** Apply rigorous debugging process.

**DO:**
1. **Verify data:** Re-check source files (was data actually present?)
2. **Re-analyze:** Run extraction again (was it hallucination or extraction failure?)
3. **Test hypotheses:** What caused the error?
   - Prompt ambiguity?
   - Context limitation?
   - Schema misunderstanding?
4. **Isolate variables:** Change ONE thing, re-test
5. **Document fix:** What specific change resolved it?
6. **Generalize solution:** Does this fix apply to other words?

**REFERENCE:** TBTA 6-step error analysis technique

**CHECKPOINT:** All errors analyzed with documented fixes

---

## STAGE 4: Schema & Template Finalization (Cycle 5) (4-6 hours)

### 4.1 Adjust Schema Based on Experiments

**DO:**
1. Review schema against 4 cycles of outputs
2. Adjust schema to reflect:
   - What's actually extractable (vs theoretical)
   - What's valuable (vs noise)
   - What's consistent (vs one-off)

3. Update schema with:
   - Required fields (100% present)
   - Optional fields (context-dependent)
   - Deprecated fields (never populated)

**CHECKPOINT:** Schema updated and validated against test outputs

### 4.2 Create Production Templates

**DO:**
1. **Standard extraction template:**
   - Default prompt for normal words
   - Word type classification logic
   - Inline citation patterns
   - Convergence/divergence handling

2. **Error correction template:**
   - 5-part structure
   - Multi-layered refutation
   - Expert validation
   - Correct methodology

3. **Multi-perspective template:**
   - Scholarly debate structure
   - Bias detection tests
   - Fair documentation of all positions

4. **Skip decision template:**
   - When to skip word (insufficient data)
   - Confidence markers for sparse coverage

**CHECKPOINT:** 4 templates created and tested on 5-10 words each

### 4.3 Update Validation Checklist

**DO:**
1. Customize 3-level validation for this tool:
   - Tool-specific Level 2 requirements
   - Tool-specific Level 3 enhancements
2. Create validation script (if automatable)
3. Document manual validation steps

**CHECKPOINT:** Tool-specific validation checklist finalized

---

## STAGE 5: Peer Review (Cycle 6) (6-8 hours)

### 5.1 Blind Subagent Validation

**CRITICAL:** Subagent NEVER sees reference answers during development.

**DO:**
1. **SPAWN:** Subagent with NO context of prior cycles
2. Provide subagent:
   - Tool schema/README/templates
   - 10-15 test words (no prior outputs)
3. Subagent extracts independently
4. **COMPARE:** Subagent outputs vs main agent outputs
5. Document divergences (reveals methodology gaps)

**REFERENCE:** TBTA blind validation technique

**CHECKPOINT:** Blind validation completed with divergence analysis

### 5.2 Adversarial Peer Review

**DO:**
1. **SPAWN:** 4 adversarial reviewers with distinct perspectives:
   - **Theological reviewer:** Check doctrinal accuracy, theological precision
   - **Linguistic reviewer:** Check etymology, morphology, semantics
   - **Methodological reviewer:** Check citations, fair use, validation
   - **Practitioner reviewer:** Check translation usefulness, real-world applicability

2. Each reviewer:
   - Reviews 5-10 stellar examples
   - Critiques methodology
   - Documents concerns/improvements

3. Main agent addresses ALL critiques

**REFERENCE:** TBTA critical peer review technique

**CHECKPOINT:** 4 adversarial reviews completed with documented responses

### 5.3 Implement Feedback

**DO:**
1. Prioritize feedback (critical vs enhancement)
2. Update methodology/templates/schema
3. Re-run affected test words
4. Validate improvements

**CHECKPOINT:** All critical feedback addressed

---

## STAGE 6: Production Validation (Cycle 7) (4-6 hours)

### 6.1 Run Full Validation Suite

**Validation Ground Truth:**
- **Strong's Ground Truth**: Published lexicons + scholarly consensus (authoritative INPUT)
- **Validation Method**: 3-tier framework (100% L1, 80%+ L2, 60%+ L3)
- **Convergence = Validation**: 3+ independent sources agreeing = verified

**Process:**
1. **DO**: Apply 3-tier validation checklist to ALL test words (30-50+)
   - **Level 1 (CRITICAL - 100%)**: No fabrication, inline citations, sources verified
   - **Level 2 (HIGH - 80%+)**: Convergence documented (3+ lexicons), appropriate semantic categories
   - **Level 3 (MEDIUM - 60%+)**: Cross-references, diachronic analysis where relevant

2. **SPAWN**: Peer review panel
   - **Source Verification**: Can credentials be verified? Are sources authoritative?
   - **Convergence Analysis**: Do 3+ independent sources agree?
   - **Fabrication Detection**: Can every claim be traced to a source?
   - **Scope Boundary Validation**: Is skip decision appropriate? (not all words need all data)

3. **DO**: Adversarial testing (not just easy cases)
   - Rare words (coverage patterns)
   - Scholarly disagreement (multi-perspective needed)
   - Scope boundaries (when to skip = success)

4. **CHECKPOINT**: All validation criteria met (100% L1, 80%+ L2, 60%+ L3)

**Output:** Validation report with tier scores, peer review feedback

### 6.2 Translation Impact Testing

**DO:**
1. **ROLE-PLAY:** Translator scenarios for 5-10 words:
   - Bible translator in minority language
   - Pastor preparing sermon
   - Seminary student researching theology

2. Document for each scenario:
   - What mistakes were avoided (thanks to enrichment data)?
   - What mistakes were made (despite enrichment data)?
   - What data was most valuable?
   - What data was missing?

3. Update methodology/schema based on impact analysis

**REFERENCE:** TBTA translation impact testing technique

**CHECKPOINT:** Translation impact analysis documented

### 6.3 Measure Success Metrics

**DO:**
1. **Quality metrics:**
   - Level 1 validation: 100%
   - Level 2 validation: 80%+
   - Level 3 validation: 60%+

2. **Efficiency metrics:**
   - Average time per word
   - Time by word type (theological, grammatical, nominal)
   - Time by frequency (rare, medium, high)

3. **Coverage metrics:**
   - Percentage of test words successfully enriched
   - Percentage requiring skip (insufficient data)
   - Percentage with stellar quality (90%+ L2, 80%+ L3)

**CHECKPOINT:** Success metrics documented and meet standards

### 6.4 Document Final Methodology

**DO:**
1. Create `/bible-study-tools/strongs-extended/tools/{tool}/METHODOLOGY.md`:
   - Tool purpose and scope
   - Word classification strategy
   - Extraction approach per word type
   - Templates and examples
   - Validation requirements
   - Time estimates
   - Known limitations

2. Select 2-3 stellar examples for publication

**CHECKPOINT:** Methodology documented and reproducible

---

## STAGE 7: Production Deployment (Ongoing)

### 7.1 Prioritize Words for Production

**DO:**
1. **High-priority (~300 words):**
   - Theological terms (rare-medium frequency)
   - Translation challenges (documented in SIL/Wycliffe)
   - Controversial terms (scholarly debates)

2. **Medium-priority (~800 words):**
   - Medium-frequency nominal terms
   - Balanced semantic/grammatical
   - Standard extraction (no edge cases)

3. **Low-priority (~400 words):**
   - High-frequency grammatical
   - Minimal lexical richness
   - Statistics-focused

**CHECKPOINT:** Word priority list created

### 7.2 Execute Systematically

**DO:**
1. Use finalized templates (standard, error-correction, multi-perspective, skip)
2. Batch by priority (high → medium → low)
3. Validate continuously (spot-check 10% per batch)
4. Monitor quality trends (watch for methodology drift)

**CHECKPOINT:** Production outputs created at scale

### 7.3 Apply Stopping Rule

**STOPPING RULE:** <5% gain per cycle (diminishing returns)

**DO:**
1. After each batch (50-100 words):
   - Measure validation pass rates
   - Compare to previous batch
   - If improvement <5%, methodology is mature

2. When improvement <5%:
   - Finalize tool as "production complete"
   - Move to next tool

**CHECKPOINT:** Tool completed or next batch planned

### 7.4 Monitor and Iterate

**DO:**
1. Spot-check 10% of production outputs
2. Document any new patterns/edge cases
3. Update methodology if needed (rare)
4. Maintain quality standards (100% L1, 80% L2, 60% L3)

**CHECKPOINT:** Quality maintained across production run

---

## Success Criteria

**Per Tool (Stages 1-6):**
- ✅ 100% Level-1 validation (all test words)
- ✅ 80%+ Level-2 validation (test words)
- ✅ 60%+ Level-3 validation (test words)
- ✅ Methodology documented (reproducible)
- ✅ Stellar examples published (2-3)

**Production Deployment (Stage 7):**
- ✅ Zero fabrication (100% sourced)
- ✅ All sources credentialed/cited
- ✅ Fair-use compliant
- ✅ Time targets met
- ✅ Coverage validated

---

## Tool-Specific Quick Reference

### Lexicon-Core
- **Strategy:** Word type classification drives extraction depth
- **Coverage:** 90% morphology (not 100%)
- **Time:** Theological 59 min, Grammatical 47 min
- **Skip:** Controversial for grammatical words

### Web-Insights
- **Strategy:** Multi-discipline search (5 disciplines)
- **Templates:** Standard, error-correction (5-part), multi-perspective
- **Time:** Standard 2-3h, Error 4-5h, Multi-perspective 5-6h
- **Emphasis:** Pedagogical tone (gracious corrections)

### TBTA-Hints
- **Strategy:** Pattern extraction from 900+ translations
- **Focus:** Confidence calibration, language family clustering
- **Time:** 2-4h per word
- **Success:** +7% overall accuracy, +25% edge cases

---

## References

**For Historical Learnings:** See LEARNINGS.md (7 proven patterns with evidence)

**For Schema Details:** See tool-specific README files

**For Validation Framework:** See LEARNINGS.md §7 (3-level validation)

**For TBTA Techniques:**
- Locked predictions (Stage 2)
- 6-step error analysis (Stage 3)
- Blind subagent validation (Stage 5)
- Adversarial peer review (Stage 5)
- Translation impact testing (Stage 6)

---

**Last Updated:** 2025-11-15
**Status:** Production-ready execution workflow
**Completion:** TODO-9,175,267 ✅ RESOLVED
