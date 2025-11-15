# Tool 3 Quality Checklist

**Purpose:** Systematic validation criteria for Strong's Web Insights outputs
**Version:** 1.0.0
**Last Updated:** 2025-11-11

---

## Overview

This checklist provides 3 levels of validation criteria for Tool 3 outputs. Each level has different pass requirements:

- **Level 1: CRITICAL** - Must pass 100% (blocking issues)
- **Level 2: HIGH PRIORITY** - Must pass 80%+ (quality issues)
- **Level 3: MEDIUM PRIORITY** - Must pass 60%+ (enhancement opportunities)

---

## Level 1: CRITICAL Validation

**Pass Requirement:** 100% - ALL criteria must pass

**If ANY Level 1 criteria fails → Reject output, fix before proceeding**

### 1.1 Source Credentialing

- [ ] **All sources have verifiable author credentials OR institutional backing**
  - Check: Can we verify author has Ph.D., M.Div., or institutional affiliation?
  - Check: Is "About" page, faculty page, or bio accessible?
  - Check: Are credentials documented in output YAML?
  - FAIL if: Anonymous source, unverifiable credentials, fake credentials

- [ ] **Authority level clearly marked for EVERY insight/application**
  - Check: Every modern_insights entry has `authority_level` field
  - Check: Every practical_applications entry has `authority_level` field
  - Check: Authority note explains basis (e.g., "MEDIUM - Ph.D. scholar, blog format")
  - FAIL if: Any entry lacks authority marking

### 1.2 Citation and Fabrication

- [ ] **Inline citations present: `content {source}` format**
  - Check: All claims cite source inline
  - Check: Citation codes match ATTRIBUTION.md
  - Check: Not just URL field - inline citation in content text
  - FAIL if: Unsourced claims, citations only in metadata

- [ ] **No fabricated data - all content extracted from real sources**
  - Check: Every insight traceable to specific source
  - Check: No "invented" etymology, statistics, or claims
  - Check: Quotes/paraphrases accurate to source
  - FAIL if: Any fabricated content detected

- [ ] **No percentages or statistics without explicit source**
  - Check: Use qualitative language ("most", "many", "some")
  - Check: If percentage used, source provides it explicitly
  - FAIL if: Made-up statistics ("80% of scholars agree...")

### 1.3 Tool Integration

- [ ] **Tool 1 (lexicon-core) read FIRST - no contradictions**
  - Check: `lexicon_core_read: true` in metadata
  - Check: No contradictions between Tool 3 and Tool 1 data
  - Check: Tool 3 supplements (not duplicates) Tool 1
  - FAIL if: Tool 1 not consulted, contradictions present

- [ ] **Content adds value beyond lexicon data**
  - Check: Not just repeating Thayer's or Strong's definitions
  - Check: Provides modern insights, practical applications, or error corrections
  - Check: Value-add is demonstrable
  - FAIL if: Only duplicates lexicon information

### 1.4 Attribution

- [ ] **All sources in ATTRIBUTION.md**
  - Check: Every cited source has entry in ATTRIBUTION.md
  - Check: Copyright notices present
  - Check: Citation codes documented
  - FAIL if: New source used without attribution entry

### 1.5 Error Handling (When Applicable)

- [ ] **If error correction: 5-part structure complete (from Exp 4)**
  - Check: Part 1 - Error Statement (clear, non-mocking)
  - Check: Part 2 - Classification (fallacy type named)
  - Check: Part 3 - Multi-Layered Refutation (4-5 evidence types)
  - Check: Part 4 - Expert Validation (authorities stacked)
  - Check: Part 5 - Correct Alternative (methodology taught)
  - FAIL if: Any part missing or incomplete

- [ ] **Error corrections have proper authority minimum**
  - Check: Minimum 2 sources (MEDIUM-HIGH or higher)
  - Check: At least 1 HIGH or VERY HIGH authority
  - Check: Not from anonymous forums or unverified sources
  - FAIL if: Insufficient authority for correction

### 1.6 Scope Boundaries (from Exp 3)

- [ ] **Word is appropriate for Tool 3 scope**
  - Check: Not a grammatical particle (δέ, γάρ, etc.)
  - Check: Not a pure function word without semantic content
  - Check: Tool 3 adds value beyond Tool 1 lexicon data
  - FAIL if: Should be skipped (document skip decision)

- [ ] **If skipped: Skip decision documented properly**
  - Check: Skip reason clear (grammatical_particle, function_word, insufficient_coverage, tool_1_sufficient)
  - Check: Skip rationale detailed
  - Check: Search effort documented (if insufficient_coverage)
  - FAIL if: Skip without proper documentation

---

## Level 2: HIGH PRIORITY Validation

**Pass Requirement:** 80%+ (7 out of 9 criteria)

**If <80% pass → Review output, consider revision or flag for human review**

### 2.1 Content Quality

- [ ] **Modern insights based on expert analysis (not just opinion)**
  - Check: Insights cite scholarly basis
  - Check: Not personal opinion without support
  - Check: Expertise relevant to claim
  - FAIL if: Unsupported opinions, speculation

- [ ] **Practical applications grounded in evidence or field experience**
  - Check: Translator guidance cites field experience or testing
  - Check: Preacher applications reference sound methodology
  - Check: Not invented examples
  - FAIL if: Speculative applications, no grounding

- [ ] **Error corrections use 5-part structure completely (from Exp 4)**
  - Check: All 5 parts present (Error, Classification, Refutation, Validation, Alternative)
  - Check: Multi-layered refutation (4-5 evidence types)
  - Check: Expert validation (authority pyramid)
  - Check: Positive alternative teaching included
  - FAIL if: Incomplete structure, missing evidence types

- [ ] **Error corrections maintain gracious, pedagogical tone (from Exp 4)**
  - Check: Not mocking or condescending
  - Check: Acknowledges error is widespread (not "stupid mistake")
  - Check: Explains WHY wrong, not just THAT wrong
  - Check: Teaches methodology to avoid similar errors
  - FAIL if: Harsh, mocking, condescending tone

- [ ] **Multi-perspective fairness for controversial words (from Exp 1, 5)**
  - Check: If scholarly disagreement exists, multiple positions documented
  - Check: Each position has evidence and advocates
  - Check: Strengths AND considerations for each view
  - Check: No single "correct" answer imposed
  - FAIL if: One-sided presentation of controversial topic

- [ ] **Bias detection tests passed (when applicable, from Exp 5)**
  - Check: Reversal Test - Could presentation order reverse without changing implications?
  - Check: Respect Test - Would advocates of each view feel fairly represented?
  - Check: Evidence Test - Strongest arguments for all positions presented?
  - FAIL if: Any bias test fails

- [ ] **Teaching helps are appropriate and non-sensationalist**
  - Check: Pedagogically sound
  - Check: No clickbait language
  - Check: Grounded in scholarship
  - FAIL if: Sensationalist, over-simplified, misleading

- [ ] **Multiple sources when available (not relying on single blog post)**
  - Check: High-coverage words have 3+ sources
  - Check: Medium-coverage words have 2+ sources
  - Check: Single-source words marked as "limited coverage"
  - FAIL if: Relies heavily on one source when more available

---

## Level 3: MEDIUM PRIORITY Validation

**Pass Requirement:** 60%+ (5 out of 8 criteria)

**If <60% pass → Note improvements for future iterations**

### 3.1 Documentation Completeness

- [ ] **Author credentials fully documented in output**
  - Check: Highest degree listed
  - Check: Institution/affiliation when applicable
  - Check: Published works mentioned if relevant
  - NICE TO HAVE: Credentials strengthen authority assessment

- [ ] **Translator guidance is field-tested (when applicable)**
  - Check: Solutions from real translations
  - Check: Language examples with ISO codes
  - Check: Field experience cited
  - NICE TO HAVE: Enhances practical value

- [ ] **Cross-references to other tools (when relevant)**
  - Check: Tool 1 referenced appropriately
  - Check: Tool 2 referenced if theological content
  - Check: Tool 6 referenced if translation patterns related
  - NICE TO HAVE: Improves integration

- [ ] **Verification dates recorded**
  - Check: `verification_date` field present
  - Check: Dates reasonable (not future, not too old)
  - NICE TO HAVE: Enables future re-verification

- [ ] **Coverage notes explain limitations clearly**
  - Check: If limited sources, noted in metadata
  - Check: If gaps exist, acknowledged
  - Check: Honest assessment of coverage
  - NICE TO HAVE: Transparency about limitations

- [ ] **Discipline-specific coverage noted (from Exp 2)**
  - Check: Disciplines searched documented (theology, linguistics, virtue ethics, etc.)
  - Check: If coverage is discipline-specific, appropriate framing provided
  - Check: Specialized coverage recognized as legitimate (not "insufficient")
  - NICE TO HAVE: Multi-discipline search documented

- [ ] **Cultural sensitivity addressed (when applicable, from Exp 5)**
  - Check: Post-colonial sensitivities noted if relevant
  - Check: Denominational implications acknowledged
  - Check: Contemporary movements considered
  - NICE TO HAVE: Cultural considerations enhance translator guidance

- [ ] **Scope boundaries respected (from Exp 3)**
  - Check: Clear distinction between Tool 1 and Tool 3 territory
  - Check: Skip decisions appropriately made for function words/particles
  - Check: No overreach into pure grammar
  - NICE TO HAVE: Demonstrates appropriate self-restraint

---

## Validation Workflow

### Step 1: Quick Scan (5 minutes)
Review output for obvious issues:
- Sources look credible?
- Authority levels marked?
- Citations present?
- No fabricated-sounding content?

**If obvious issues → STOP, address immediately**

### Step 2: Level 1 Validation (15 minutes)
Work through ALL Level 1 criteria systematically:
- Check credentials
- Verify citations
- Check Tool 1 integration
- Verify attribution
- Check error correction completeness

**If ANY Level 1 fails → REJECT output, fix before proceeding**

### Step 3: Level 2 Validation (10 minutes)
Check 5 HIGH PRIORITY criteria:
- Content quality
- Evidence grounding
- Multiple sources
- Appropriateness

**If <80% pass → Flag for revision**

### Step 4: Level 3 Validation (5 minutes)
Check 5 MEDIUM PRIORITY criteria:
- Documentation completeness
- Cross-references
- Coverage notes

**If <60% pass → Note for improvement**

### Step 5: Overall Assessment
**PASS:** Level 1 = 100%, Level 2 ≥ 80%, Level 3 ≥ 60%
**CONDITIONAL PASS:** Level 1 = 100%, Level 2 ≥ 80%, Level 3 < 60%
**REVISE:** Level 1 = 100%, Level 2 < 80%
**REJECT:** Level 1 < 100%

---

## Common Failure Patterns

### Pattern 1: Unverified Credentials
**Symptom:** Author name without verifiable credentials
**Detection:** Cannot find author bio, faculty page, or publication record
**Fix:** Find credentials OR exclude source

### Pattern 2: Lexicon Duplication
**Symptom:** Content just repeats Thayer's definitions
**Detection:** Compare to Tool 1 output - no new information
**Fix:** Find sources with genuine value-add OR note insufficient coverage

### Pattern 3: Fabricated Statistics
**Symptom:** "75% of scholars agree..." without citation
**Detection:** No source provides this specific statistic
**Fix:** Remove statistic OR find source that provides it

### Pattern 4: Opinion Masquerading as Insight
**Symptom:** Author's personal opinion presented as scholarly insight
**Detection:** No scholarly support, just "I think..."
**Fix:** Mark as opinion OR remove if not valuable

### Pattern 5: Anonymous/Low Authority Corrections
**Symptom:** Error correction from forum post or unknown source
**Detection:** Cannot verify author credentials
**Fix:** Find expert correction OR note controversy in Tool 4 instead

---

## Validation Checklist Template

Use this template for each output:

```markdown
# Validation Report: {Strong's Number}

**Date:** YYYY-MM-DD
**Validator:** {Name}
**Output File:** {filename}

## Level 1: CRITICAL (Must Pass 100%)

### Source Credentialing
- [ ] All sources credentialed: ___/___
- [ ] Authority levels marked: ___/___
- Notes: {any issues}

### Citation and Fabrication
- [ ] Inline citations present: YES/NO
- [ ] No fabricated data: YES/NO
- [ ] No unsourced statistics: YES/NO
- Notes: {any issues}

### Tool Integration
- [ ] Tool 1 read first: YES/NO
- [ ] No contradictions: YES/NO
- [ ] Content adds value: YES/NO
- Notes: {any issues}

### Attribution
- [ ] All sources in ATTRIBUTION.md: YES/NO
- Notes: {any issues}

### Error Handling (if applicable)
- [ ] Complete error pattern: YES/NO/NA
- [ ] Authority MEDIUM+: YES/NO/NA
- Notes: {any issues}

**Level 1 Result:** PASS / FAIL
**If FAIL, stop here and fix issues**

---

## Level 2: HIGH PRIORITY (Must Pass 80%+)

- [ ] Modern insights expert-based
- [ ] Practical apps grounded
- [ ] Error corrections complete
- [ ] Teaching helps appropriate
- [ ] Multiple sources when available

**Level 2 Result:** ___/5 = ___%  PASS / FAIL

---

## Level 3: MEDIUM PRIORITY (Must Pass 60%+)

- [ ] Credentials documented
- [ ] Translator guidance field-tested
- [ ] Cross-references present
- [ ] Verification dates recorded
- [ ] Coverage notes clear

**Level 3 Result:** ___/5 = ___%  PASS / FAIL

---

## Overall Assessment

**Level 1:** PASS / FAIL
**Level 2:** ___% PASS / FAIL
**Level 3:** ___% PASS / FAIL

**FINAL DECISION:**
- [ ] PASS - Ready for production
- [ ] CONDITIONAL PASS - Minor improvements noted
- [ ] REVISE - Level 2 issues need addressing
- [ ] REJECT - Level 1 failures, cannot proceed

**Action Items:**
1. {specific fix needed}
2. {specific fix needed}

**Reviewer Signature:** _______________
```

---

## Special Validation Scenarios

### Scenario: Limited Coverage (1-2 sources)

**Additional Checks:**
- [ ] Metadata explicitly notes "limited coverage"
- [ ] Coverage caveat in appropriate sections
- [ ] No forced content to fill gaps
- [ ] Honest about what's missing

**Pass Criteria:** Honesty maintained, no fabrication

### Scenario: Error Correction Content (5-Part Structure from Exp 4)

**Additional Checks:**
- [ ] **Part 1 - Error Statement:** Clear, specific claim stated without mockery
- [ ] **Part 2 - Classification:** Fallacy type named (e.g., "etymological_fallacy", "semantic_anachronism")
- [ ] **Part 3 - Multi-Layered Refutation:** 4-5 evidence types present (linguistic, diachronic, contextual, scholarly consensus, etc.)
- [ ] **Part 4 - Expert Validation:** Authority pyramid (VERY HIGH → HIGH → MEDIUM), minimum 2 sources, at least 1 HIGH or VERY HIGH
- [ ] **Part 5 - Correct Alternative:** Principle + Methodology + Better Analogy + Biblical Usage Pattern
- [ ] **Tone:** Gracious and pedagogical throughout (not condescending, acknowledges error is widespread, explains WHY wrong)
- [ ] **Quality:** Minimum authority standards met (2 sources MEDIUM-HIGH+, 1 HIGH/VERY HIGH)

**Pass Criteria:** All 5 parts complete, 4+ evidence types, proper authority, gracious tone

**Examples to Study:**
- experiments/exp4-error-correction/G1411-synthesis.md (dynamis/dynamite fallacy)
- Note Carson (VERY HIGH), Cara (HIGH), Mounce (MEDIUM) authority pyramid
- Note gracious tone: "very, very dangerous" not "stupid"
- Note positive teaching: "dynamo not dynamite" memorable alternative

### Scenario: Scholarly Disagreement or Cultural Debate (Multi-Perspective from Exp 1, 5)

**Additional Checks:**
- [ ] **Multiple Positions:** Minimum 2 major positions documented with advocates
- [ ] **Fair Representation:** Each position has key arguments, strengths, and considerations
- [ ] **Evidence:** Each position supported with sources and inline citations
- [ ] **Bias Detection Tests:**
  - [ ] Reversal Test: Could presentation order reverse without changing implications?
  - [ ] Respect Test: Would advocates of each view feel fairly represented?
  - [ ] Evidence Test: Strongest arguments for all positions presented?
- [ ] **Translator Guidance:** Decision framework provided (options, NOT mandates)
- [ ] **Cultural Sensitivity:** Post-colonial, denominational, contemporary movement factors addressed if relevant
- [ ] **Tone:** Fair and charitable to all views, no mockery, professional navigation of controversy
- [ ] **No Single Answer:** Multiple valid perspectives acknowledged, no "correct" answer imposed

**Pass Criteria:** All bias tests passed, fair representation, minimum 2 positions, guidance as options

**Examples to Study:**
- experiments/exp1-scholarly-disagreement/G4151-findings.md (pneuma - 4 types of disagreement)
- experiments/exp5-cultural-debate/G1577-guidance-synthesis.md (ekklesia - church vs assembly)
- Note multi-perspective framework in action
- Note cultural sensitivity (post-colonial contexts, house church movements)
- Note decision framework not answer sheet

### Scenario: Translator-Focused Word

**Additional Checks:**
- [ ] Solutions are field-tested (not speculation)
- [ ] Specific language examples provided
- [ ] Cultural context explained
- [ ] Theological stakes assessed
- [ ] Multiple strategies when available
- [ ] Authority marked as "HIGH for practical applications"

**Pass Criteria:** Field evidence, practical value, appropriate authority

### Scenario: Rare Word with Discipline-Specific Coverage (from Exp 2)

**Additional Checks:**
- [ ] **Multi-Discipline Search:** Bible study platforms, theology, linguistics, virtue ethics, philosophy, translation resources all checked
- [ ] **Specialized Coverage Recognized:** If coverage exists in specific discipline (e.g., virtue ethics for eutrapelia), recognized as legitimate
- [ ] **Appropriate Framing:** Discipline context provided (e.g., "theological virtue perspective")
- [ ] **No Forced General Content:** Don't fabricate biblical content when coverage is specialized
- [ ] **Honest Assessment:** Coverage limitations noted (e.g., "excellent in virtue ethics, limited in biblical studies")
- [ ] **Synthesis Effort Realistic:** Estimate interdisciplinary synthesis time appropriately

**Pass Criteria:** Multi-discipline search completed, specialized coverage appropriately framed, no fabrication

**Examples to Study:**
- experiments/exp2-rare-hapax/G2160-assessment.md (eutrapelia - virtue ethics coverage)
- Note how specialized coverage is legitimate, not "insufficient"
- Note appropriate framing for interdisciplinary content

### Scenario: Skip Decision (Grammatical Particle or Insufficient Coverage, from Exp 3)

**Additional Checks:**
- [ ] **Skip Reason Clear:** grammatical_particle | function_word | insufficient_coverage | tool_1_sufficient
- [ ] **Skip Rationale Detailed:** Specific explanation of why word is outside Tool 3 scope
- [ ] **Search Documentation:** If insufficient_coverage, minimum 5 queries across multiple disciplines documented
- [ ] **Scope Boundary Analysis:** Clear distinction between Tool 1 (grammar/lexicon) and Tool 3 (practical insights) territory
- [ ] **Skip is Success:** Recognized as appropriate self-restraint, not failure
- [ ] **No Output File Created:** Skip decision documented separately, no forced content

**Pass Criteria:** Skip decision documented, search effort proven (if applicable), scope boundaries clear

**Examples to Study:**
- experiments/exp3-scope-boundary/G1161-boundary-assessment.md (de particle - correctly skipped)
- Note clear scope boundary reasoning
- Note skip = SUCCESS (appropriate judgment)

### Scenario: Zero Web Sources Found (Insufficient Coverage)

**Additional Checks:**
- [ ] Exhaustive search documented (minimum 5 queries)
- [ ] Multiple disciplines checked (Bible study, theology, linguistics, etc.)
- [ ] Assessment: "insufficient web coverage" clearly stated
- [ ] Recommendation: skip word OR include with major caveats
- [ ] NO OUTPUT FILE created (skip is acceptable)
- [ ] Search log documents attempts

**Pass Criteria:** Honest assessment, no fabrication, skip decision documented, exhaustive search proven

---

## Continuous Improvement

After validating multiple outputs, look for patterns:

### Positive Patterns (Reinforce)
- Sources that consistently provide quality content
- Search strategies that work well
- Content categories that add clear value
- Authority detection working smoothly

### Negative Patterns (Address)
- Sources that duplicate lexicons
- Searches that yield poor results
- Content that doesn't add value
- Authority assignments that feel inconsistent

### Update Methodology
- Refine research documents based on learnings
- Update authority-detection.md with examples
- Adjust schema if needed
- Improve search strategies

---

## Summary: Validation Priority

**Non-Negotiable (Level 1 - CRITICAL):**
1. Verifiable credentials
2. No fabrication
3. Inline citations
4. Authority marked
5. Tool 1 integration

**Essential Quality (Level 2 - HIGH PRIORITY):**
1. Expert-based insights
2. Grounded applications
3. Complete error corrections
4. Appropriate teaching
5. Multiple sources

**Quality Enhancement (Level 3 - MEDIUM PRIORITY):**
1. Full documentation
2. Field-tested guidance
3. Cross-references
4. Verification dates
5. Coverage notes

---

**Remember:** Quality over quantity. Better to skip a word than force content that fails validation.
