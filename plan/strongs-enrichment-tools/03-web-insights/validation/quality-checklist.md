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

- [ ] **If error correction: Error + refutation + evidence complete**
  - Check: Error clearly stated (not vague)
  - Check: Expert refutation present
  - Check: Evidence provided for correction
  - FAIL if: Incomplete error correction pattern

- [ ] **Error corrections have MEDIUM+ authority minimum**
  - Check: Corrections from Ph.D. scholars or M.Div. with sources
  - Check: Not from anonymous forums or unverified sources
  - FAIL if: Low authority corrections

---

## Level 2: HIGH PRIORITY Validation

**Pass Requirement:** 80%+ (4 out of 5 criteria)

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

- [ ] **Error corrections documented with complete evidence**
  - Check: Common claim stated
  - Check: Why it's wrong explained
  - Check: Correct understanding provided
  - FAIL if: Only negative (error) without positive (correction)

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

**Pass Requirement:** 60%+ (3 out of 5 criteria)

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

### Scenario: Error Correction Content

**Additional Checks:**
- [ ] Error clearly stated (specific claim)
- [ ] Prevalence accurately described
- [ ] Refutation from expert (MEDIUM+ authority)
- [ ] Evidence for correction provided
- [ ] Correct teaching included (positive)
- [ ] Tone is gracious, not mocking

**Pass Criteria:** Complete pattern, appropriate authority, gracious tone

### Scenario: Translator-Focused Word

**Additional Checks:**
- [ ] Solutions are field-tested (not speculation)
- [ ] Specific language examples provided
- [ ] Cultural context explained
- [ ] Theological stakes assessed
- [ ] Multiple strategies when available
- [ ] Authority marked as "HIGH for practical applications"

**Pass Criteria:** Field evidence, practical value, appropriate authority

### Scenario: Zero Web Sources Found

**Additional Checks:**
- [ ] Exhaustive search documented
- [ ] Assessment: "insufficient web coverage"
- [ ] Recommendation: skip word OR include with major caveats
- [ ] NO OUTPUT FILE created (skip is acceptable)
- [ ] Search log documents attempts

**Pass Criteria:** Honest assessment, no fabrication, skip decision documented

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
