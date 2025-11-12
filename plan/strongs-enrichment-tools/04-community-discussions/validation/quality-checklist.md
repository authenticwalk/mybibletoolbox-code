# Quality Checklist: Community Discussions Validation

**Created:** 2025-11-12
**Purpose:** 3-level validation criteria for Tool 4 outputs

---

## Critical Principle

**EVERY community-discussions YAML file MUST pass ALL Level 1 (CRITICAL) checks.**

Level 2 and Level 3 are for quality improvement, but Level 1 is mandatory.

---

## Level 1: CRITICAL (100% Pass Required)

### 1.1 Error Has Real Source (URL Required)
- [ ] Error documented from actual community discussion
- [ ] Source URL provided and accessible
- [ ] Source type identified (Stack Exchange, Reddit, forum, blog, devotional, etc.)
- [ ] Date observed recorded
- [ ] NOT fabricated or hypothetical error

**Validation:**
- Click URL - does it load?
- Does source actually contain the error claimed?
- Is context accurately represented?

**If fails:** DO NOT include this controversy. Find real source or remove.

---

### 1.2 Scholarly Refutation Present (HIGH/MEDIUM Authority)
- [ ] Every error paired with scholarly correction
- [ ] Refutation source has HIGH or MEDIUM authority
- [ ] Never use LOW authority sources for refutation
- [ ] Source type identified (lexicon, journal, book, expert blog)
- [ ] Author credentials verified (when applicable)

**Authority Requirements:**
- HIGH: Published lexicons (BDAG, LSJ, BDB), peer-reviewed journals, academic books
- MEDIUM: Expert blogs with Ph.D. credentials + citations, seminary faculty
- LOW: Community discussions, general blogs (NEVER use for refutation)

**Validation:**
- Is refutation source HIGH or MEDIUM authority?
- Are credentials verified (if expert blog)?
- Does source actually refute the specific error?

**If fails:** Find HIGH/MEDIUM authority source or remove error entirely.

---

### 1.3 Evidence Provided (Not Just Assertion)
- [ ] Refutation includes factual evidence
- [ ] Not just "this is wrong" - explains WHY with facts
- [ ] Evidence types appropriate:
  - Chronological (timeline, dates)
  - Lexical (lexicon definitions, semantic range)
  - Usage (biblical examples contradicting error)
  - Linguistic (etymology, cognate analysis)
  - Historical (cultural context, development)

**Validation:**
- Does refutation cite specific facts?
- Are facts verifiable (dates, lexicon definitions, etc.)?
- Is evidence type appropriate for error type?

**If fails:** Add evidence from scholarly sources. If unavailable, remove error.

---

### 1.4 Error Type Classified
- [ ] Primary error type assigned (one of 7 types)
- [ ] Type matches error pattern
- [ ] Contributing factors identified when applicable

**7 Error Types:**
1. Etymological fallacy
2. Anachronism
3. False cognate
4. Over-specification
5. Lexical maximalism
6. Theological projection
7. Selective definition

**Validation:**
- Is error type one of the 7 defined types?
- Does classification match error pattern?
- See `research/controversy-patterns.md` for definitions

**If fails:** Re-classify or identify new type (update taxonomy if genuinely new pattern).

---

### 1.5 No Fabricated Controversies
- [ ] Error is real, not invented
- [ ] Not exaggerating or misrepresenting community discussion
- [ ] Not creating straw-man arguments
- [ ] Prevalence assessment honest (widespread/moderate/uncommon)

**Validation:**
- Does error actually exist in cited source?
- Is prevalence assessment supported by evidence?
- Are we fairly representing what community said?

**If fails:** Remove or correct representation. Never fabricate errors.

---

### 1.6 Tone Gracious (Not Mocking)
- [ ] Language respectful, not dismissive
- [ ] Acknowledges why error is tempting/common
- [ ] No mocking or condescending language
- [ ] Positive alternative framing provided

**Red Flags (Avoid):**
- "This ridiculous claim..."
- "Anyone who studied Greek knows..."
- "Obviously wrong..."
- "Ignorant teaching..."

**Good Phrasing:**
- "While this interpretation is common..."
- "Though tempting to connect these words..."
- "This claim appears in several sources, but evidence shows..."

**Validation:**
- Read through entire YAML - any mocking tone?
- Is "why_tempting" section present and sympathetic?
- Is alternative framing positive, not just negative?

**If fails:** Rewrite with gracious tone. Remember: preachers/teachers well-intentioned.

---

### 1.7 All Sources in ATTRIBUTION.md
- [ ] Every citation code used appears in ATTRIBUTION.md
- [ ] Copyright notices present
- [ ] URLs or book citations provided
- [ ] Fair use compliance noted

**Validation:**
- List all {citation-codes} used in YAML
- Check each one exists in ATTRIBUTION.md
- Verify copyright info present

**If fails:** Add sources to ATTRIBUTION.md before releasing file.

---

## Level 2: HIGH PRIORITY (80%+ Pass Required = 7 of 9)

### 2.1 Prevalence Assessed with Evidence
- [ ] Prevalence marked (widespread/moderate/uncommon)
- [ ] Assessment supported by observable evidence
- [ ] Multiple sources for "widespread" claims
- [ ] Google search results or publication frequency noted

**Scoring:** Pass if prevalence is assessed AND supported.

---

### 2.2 Multiple Refutation Sources (When Available)
- [ ] 2+ refutation sources provided when available
- [ ] Mix of source types (lexicon + scholarly book, etc.)
- [ ] Convergence across sources documented

**Scoring:** Pass if 2+ sources OR if comprehensive single source + note explaining.

---

### 2.3 Helpful Guidance Provided
- [ ] "what_to_avoid" section present and specific
- [ ] "alternative_framing" section provides positive teaching
- [ ] "memory_aid" or pedagogical help offered
- [ ] Not just correction - provides constructive alternative

**Scoring:** Pass if alternative framing is constructive and actionable.

---

### 2.4 Related Errors Documented (When Applicable)
- [ ] If error pattern applies to other words, those listed
- [ ] Cross-references to similar errors provided
- [ ] Pattern generalization noted (e.g., "all phonetic fallacies")

**Scoring:** Pass if related errors documented OR explicit note "no related errors found."

---

### 2.5 Integration with Tools 1-3 Checked
- [ ] Tool 1 lexicon-core checked (if file exists)
- [ ] Etymology section compared to error claim
- [ ] Semantic range used in refutation
- [ ] Tool 2/3 checked if applicable

**Scoring:** Pass if integration section present OR note explaining unavailability.

---

### 2.6 Common Questions Answered (If Exist)
- [ ] If common questions exist about this word, 1+ documented
- [ ] Expert answers provided (not just community answers)
- [ ] Sources cited for answers

**Scoring:** Pass if questions answered OR explicit note "no common questions found."

---

### 2.7 Pedagogical Notes on Why Error Tempting
- [ ] "why_tempting" section present
- [ ] Explains psychological/pedagogical appeal
- [ ] Helps teachers understand how error spreads
- [ ] Empathetic to those who made error

**Scoring:** Pass if why_tempting is detailed and empathetic.

---

### 2.8 Error Classification Detailed
- [ ] Primary type identified
- [ ] Contributing factors listed
- [ ] Secondary types noted when overlap exists

**Scoring:** Pass if classification goes beyond just primary type.

---

### 2.9 Helpful Cautions Provided
- [ ] 1+ caution documented
- [ ] Caution type identified (etymological, semantic, theological, etc.)
- [ ] Reason and evidence provided
- [ ] Generalizable principle noted

**Scoring:** Pass if cautions are specific and helpful.

---

## Level 3: MEDIUM PRIORITY (60%+ Pass Required = 5 of 8)

### 3.1 Comprehensive Evidence Types
- [ ] 3+ evidence types used (chronological, lexical, usage, etc.)
- [ ] Evidence types appropriate for error
- [ ] Each evidence item cited

**Scoring:** Pass if 3+ types OR comprehensive use of 2 types.

---

### 3.2 Scholarly Debates Distinguished (When Relevant)
- [ ] If legitimate scholarly debate exists, separated from popular error
- [ ] Community confusion vs. scholarly disagreement clarified
- [ ] Translator guidance for genuine uncertainty provided

**Scoring:** Pass if distinction made OR note "no scholarly debate on this word."

---

### 3.3 Positive Alternative Framing
- [ ] Not just "don't say X" but "DO say Y"
- [ ] Valid memory aids or teaching approaches offered
- [ ] Constructive, not just corrective

**Scoring:** Pass if positive alternatives are actionable and grounded in truth.

---

### 3.4 Cross-References to Related Tools
- [ ] Tool 1 etymology compared
- [ ] Tool 2 theological insights integrated (if exists)
- [ ] Tool 3 web insights cross-checked (if exists)

**Scoring:** Pass if integration attempted OR unavailability noted.

---

### 3.5 Cultural/Historical Context Provided
- [ ] If error involves anachronism, historical context explained
- [ ] 1st-century understanding vs. modern conception clarified
- [ ] Cultural gap acknowledged

**Scoring:** Pass if context relevant and helpful.

---

### 3.6 Fair Use Compliance Documented
- [ ] Attribution section complete
- [ ] Fair use strategy noted
- [ ] Transformative purpose clear (educational, corrective)
- [ ] Limited excerpts (not full lexicon entries)

**Scoring:** Pass if fair use section present and compliant.

---

### 3.7 Metadata Complete
- [ ] Validation checkboxes filled out
- [ ] Authority distribution documented
- [ ] Coverage assessment included
- [ ] Generation stats recorded

**Scoring:** Pass if metadata sections >80% complete.

---

### 3.8 Experiment Learnings Captured (For Experiments)
- [ ] What worked documented
- [ ] Challenges noted
- [ ] Learnings extracted
- [ ] Schema refinements suggested (if needed)

**Scoring:** Pass if experiment metadata present (for experiments only).

---

## Validation Process

### Step 1: Self-Check
- Review your own YAML against this checklist
- Mark each item pass/fail
- Fix failures before submitting

### Step 2: Level 1 Mandatory
- ALL 7 Level 1 checks MUST pass
- No exceptions
- If any Level 1 fails, fix before proceeding

### Step 3: Level 2 Target
- Aim for 7/9 Level 2 checks passing (80%+)
- If below 80%, improve before release
- Document which checks failed and why

### Step 4: Level 3 Aspirational
- Aim for 5/8 Level 3 checks passing (60%+)
- Nice to have, not mandatory
- Continuous improvement target

---

## Scoring Examples

### Example 1: Minimum Passing

**Level 1:** 7/7 ✅ (PASS - mandatory)
**Level 2:** 7/9 ✅ (PASS - 78% → 80% target)
**Level 3:** 3/8 ❌ (FAIL - 38% < 60%)

**Overall:** APPROVED for release (Level 1 + Level 2 pass)
**Note:** Improve Level 3 in future iterations

---

### Example 2: High Quality

**Level 1:** 7/7 ✅ (PASS)
**Level 2:** 9/9 ✅ (PASS - 100%)
**Level 3:** 7/8 ✅ (PASS - 88%)

**Overall:** EXCELLENT quality - use as model

---

### Example 3: Failing

**Level 1:** 5/7 ❌ (FAIL - missing scholarly refutation, no evidence)
**Level 2:** 4/9 ❌ (FAIL - 44%)
**Level 3:** 2/8 ❌ (FAIL - 25%)

**Overall:** REJECTED - fix Level 1 issues before resubmitting

---

## Quick Reference Card

### Must-Have (Level 1):
1. Real error source (URL)
2. HIGH/MEDIUM authority refutation
3. Evidence provided
4. Error type classified
5. No fabrication
6. Gracious tone
7. Sources in ATTRIBUTION.md

### Should-Have (Level 2):
- Multiple refutation sources
- Helpful guidance
- Pedagogical notes
- Related errors documented

### Nice-to-Have (Level 3):
- Comprehensive evidence types
- Positive alternatives
- Cross-tool integration
- Fair use documentation

---

## Red Flags (Auto-Fail)

**Immediate rejection if:**
- ❌ Error fabricated or exaggerated
- ❌ Refutation uses LOW authority sources only
- ❌ No evidence - just assertions
- ❌ Mocking or condescending tone
- ❌ Sources not in ATTRIBUTION.md
- ❌ Plagiarism (copying without citation)

---

## Success Criteria for Tool 4 Production

**Before production rollout:**
- 95%+ of outputs pass ALL Level 1 checks
- 85%+ of outputs pass Level 2 (7/9)
- 60%+ of outputs pass Level 3 (5/8)
- Zero auto-fail red flags

**Continuous monitoring:**
- Spot-check every 20th file
- Full validation every 100 files
- User feedback integration

---

## Validation Tools

### Automated Checks (Possible Future)
- URL validation (links work?)
- Citation checker (all codes in ATTRIBUTION.md?)
- Tone analyzer (flagged words?)

### Manual Checks (Current)
- Researcher reviews own work
- Peer review for sensitive topics
- Human review if `requires_human_review: true`

---

**Status:** Complete - Ready for Experimentation Validation
**Next:** Validate exp1-G1411-dunamis against this checklist
**See Also:** `../schema.yaml`, `../research/controversy-patterns.md`, `../research/refutation-sources.md`
