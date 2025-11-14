# TBTA Migration Plan - Audit Specialist Review

**Reviewer**: Audit Specialist Agent
**Date**: 2025-11-14
**Review Focus**: Verification criteria measurability, objectivity, and completeness
**Approach**: Skeptical assumption that someone will try to game the checklist

---

## Executive Summary

**Overall Assessment**: ⚠️ **MODERATE RISK** - The audit checklist has strong structure but critical measurability gaps

**Key Findings**:
- ✅ 12 audit criteria are strong (specific, measurable, objective)
- ⚠️ 9 audit criteria are weak (vague, subjective, or unverifiable)
- ❌ 11 critical audit checks are completely missing
- 🚨 3 high-risk areas where quality could slip through undetected

**Recommendation**: **DO NOT PROCEED** until the following critical gaps are addressed:
1. Add byte-level diff verification for "500+ lines" integration claim
2. Add quantitative metrics for "no information loss" verification
3. Add automated link-checking scripts (not manual grep)
4. Add feature migration completion criteria with file count verification
5. Add source citation verification (prevent hallucination)

---

## ✅ Strong Audit Criteria (Specific & Measurable)

### Phase 1 Audits

**1. README.md coverage numbers (Line 291)**
```yaml
Criterion: "README.md has correct coverage numbers (11,649 verses)"
Status: ✅ STRONG
Why: Exact number specified, easily verifiable with grep
Verification: grep "11,649" bible-study-tools/tbta/README.md
```

**2. Git commits per phase (Lines 293, 300, 307, 314)**
```yaml
Criterion: "All changes committed to git"
Status: ✅ STRONG
Why: Binary check, easily automated
Verification: git status --porcelain | wc -l (should be 0)
```

**3. 8 tbta-source files created (Line 296)**
```yaml
Criterion: "8 tbta-source/ files created"
Status: ✅ STRONG
Why: Exact count specified
Verification: ls bible-study-tools/tbta/tbta-source/*.md | wc -l (should be 8)
Improvement: Should list the 8 specific filenames
```

**4. 26 original TODOs resolved (Line 317)**
```yaml
Criterion: "All 26 original TODOs resolved"
Status: ✅ STRONG (but needs baseline)
Why: Exact count
Verification: grep -r "TODO" bible-study-tools/tbta --include="*.md" | wc -l
Improvement: Need baseline snapshot of WHICH 26 TODOs before starting
```

**5. STANDARDIZATION.md conventions (Line 319)**
```yaml
Criterion: "All files follow STANDARDIZATION.md conventions"
Status: ✅ MODERATELY STRONG
Why: Reference to specific document
Verification: Can be automated with linting rules
Improvement: Should specify which conventions to check
```

---

## ⚠️ Weak Audit Criteria (Vague or Subjective)

### Phase 1 Audits

**1. "STAGES.md has all 500+ lines integrated" (Line 289)**
```yaml
Criterion: "STAGES.md has all 500+ lines integrated"
Status: ⚠️ WEAK
Why: "500+" is imprecise, "integrated" is subjective
Issues:
- Line count could be 501 or 1000, both pass
- "Integrated" doesn't mean quality content
- No verification that it's the RIGHT 500 lines
Gaming Risk: Copy-paste 500 lines of lorem ipsum

IMPROVEMENT NEEDED:
- Specify exact sections to integrate (Stage 4, Stage 5, Stage 6)
- Verify with diff against source file
- Check for specific heading markers:
  ✓ "## Dataset Requirements" exists (Stage 4)
  ✓ "## Locked Predictions Protocol" exists (Stage 5)
  ✓ "## Structured Subagent Validation" exists (Stage 6)
  ✓ "TBTA-REVIEW.md template" section exists (Stage 6)
  ✓ "TRANSLATOR-IMPACT.md template" section exists (Stage 6)
```

**2. "No TODOs remain in STAGES.md" (Line 290)**
```yaml
Criterion: "No TODOs remain in STAGES.md"
Status: ⚠️ WEAK (but fixable)
Why: Currently there are 0 TODOs in STAGES.md (verified), but checklist references 6 specific ones
Issues:
- Checklist says "Remove resolved TODOs (lines 3, 7, 8, 13, 26, 28)"
- Current STAGES.md has 0 TODOs (already done?)
- Mismatch between plan and reality
Gaming Risk: None if baseline is established

IMPROVEMENT NEEDED:
- Verify baseline: Which 6 TODOs exist at start?
- If already 0, mark this task as N/A
- git diff verification against source file
```

**3. "3 key examples added to README.md" (Line 292)**
```yaml
Criterion: "3 key examples added to README.md"
Status: ⚠️ WEAK
Why: "Examples" is vague - what counts as an example?
Issues:
- No quality criteria for examples
- Could add 3 trivial one-liners
- No verification they're from specified source
Gaming Risk: Add any 3 examples without checking source

IMPROVEMENT NEEDED:
- Specify must include: Genesis 1:26 (clusivity), Genesis 4:8 (participant), time granularity example
- Verify examples have: feature name, verse reference, translation impact statement
- Check examples match content from plan/tbta-analysis.md lines 146-375
```

**4. "All files have inline citations" (Line 297)**
```yaml
Criterion: "All files have inline citations"
Status: ⚠️ WEAK
Why: "All" is testable, but "inline citations" format not specified
Issues:
- What format for citations? {source-id}?
- Minimum citation density?
- No check that citations are real (not hallucinated)
Gaming Risk: Add {fake-source} citations

IMPROVEMENT NEEDED:
- Specify citation format: {lang}-{version} or {llm-cs45}
- Verify all citations exist in ATTRIBUTION.md
- Minimum 1 citation per major claim
- Script to extract all {citations} and verify against ATTRIBUTION.md
```

**5. "No fabricated data (all sourced from plan files)" (Line 298)**
```yaml
Criterion: "No fabricated data (all sourced from plan files)"
Status: ❌ VERY WEAK - UNVERIFIABLE
Why: How do you prove a negative?
Issues:
- Impossible to verify without human review
- No way to detect "similar but fabricated" content
- Relies on trust, not verification
Gaming Risk: HIGH - Can make up anything

IMPROVEMENT NEEDED:
- Require explicit source references for each section:
  ## Coverage Details
  Source: plan/tbta-rebuild-with-llm/archive/features-analysis/data-coverage-analysis.md:45-67

  {content}

- Spot-check 20% of content against sources
- Flag any statistics/numbers without sources
```

**6. "Cross-references use correct paths" (Line 299)**
```yaml
Criterion: "Cross-references use correct paths"
Status: ⚠️ WEAK (easily gameable)
Why: "Correct" assumes manual verification
Issues:
- Manual grep not reliable
- Doesn't check if paths RESOLVE (file exists)
- Doesn't check if paths are RELATIVE vs ABSOLUTE
Gaming Risk: Could reference non-existent files

IMPROVEMENT NEEDED:
- Automated script that:
  1. Extracts all markdown links
  2. Resolves relative paths
  3. Checks if target files exist
  4. Reports broken links
- Zero tolerance: 0 broken links allowed
```

### Phase 3 Audits

**7. "All markdown links verified (no 404s)" (Line 303)**
```yaml
Criterion: "All markdown links verified (no 404s)"
Status: ⚠️ WEAK
Why: Uses manual grep, "(no 404s)" is web terminology for file links
Issues:
- Manual verification is error-prone
- grep -r "\[.*\](.*)" won't catch all link formats
- No automation
Gaming Risk: Miss broken links in nested directories

IMPROVEMENT NEEDED:
- Use markdown link checker tool:
  npx markdown-link-check bible-study-tools/tbta/**/*.md
- Or custom script that checks file existence
- Require: 100% link success rate
```

**8. "Progressive disclosure compliance checked" (Line 304)**
```yaml
Criterion: "Progressive disclosure compliance checked"
Status: ⚠️ WEAK
Why: "Checked" doesn't mean "passed"
Issues:
- No pass/fail criteria
- Exception for TBTA README not clearly bounded
- "Files >limits: Create subdirectory structure" is vague
Gaming Risk: "Check" doesn't mean fix

IMPROVEMENT NEEDED:
- Script to measure all .md files:
  find bible-study-tools/tbta -name "*.md" -exec wc -l {} \; | awk '$1 > 500'
- READMEs: ≤500 lines (or documented exception)
- Topic files: ≤400 lines
- List all exceptions with justification in plan
- Zero tolerance for undocumented exceptions
```

**9. "features/TEMPLATE.md created and actionable" (Line 305)**
```yaml
Criterion: "features/TEMPLATE.md created and actionable"
Status: ⚠️ WEAK
Why: "Actionable" is completely subjective
Issues:
- No objective measure of "actionable"
- Could be 10 lines of vague advice
- No content requirements specified
Gaming Risk: Create empty template

IMPROVEMENT NEEDED:
- Require specific sections:
  ✓ Reference to STAGES.md
  ✓ Checklist from FEATURE-AUDIT-TEMPLATE.md
  ✓ Progressive disclosure guidance
  ✓ Examples of good vs bad feature READMEs
- Minimum length: 200 lines
- Must include all 6 STAGES as sections
```

---

## ❌ Missing Critical Audit Checks

### PHASE 1: Missing Checks

**1. ❌ Diff verification for STAGES.md integration**
```yaml
Missing Check: Verify the RIGHT content was integrated, not just 500 lines
Why Critical: Prevents copy-paste errors, ensures source integrity
How to Add:
- git diff bible-study-tools/tbta/features/STAGES.md should show:
  + Lines matching plan/tbta-rebuild-with-llm/features/STAGES.md:45-220 (Stage 4)
  + Lines matching plan/tbta-rebuild-with-llm/features/STAGES.md:221-400 (Stage 5)
  + Lines matching plan/tbta-rebuild-with-llm/features/STAGES.md:401-550 (Stage 6)
- Use diff tool to verify 95%+ overlap with source sections

Add to Checklist:
- [ ] STAGES.md Stage 4 content matches source lines 45-220 (95%+ similarity)
- [ ] STAGES.md Stage 5 content matches source lines 221-400 (95%+ similarity)
- [ ] STAGES.md Stage 6 content matches source lines 401-550 (95%+ similarity)
- [ ] All removed TODOs are documented in git commit message
```

**2. ❌ Baseline TODO snapshot before starting**
```yaml
Missing Check: Capture which 26 TODOs exist at start
Why Critical: Can't verify "26 TODOs resolved" without knowing which 26
How to Add:
- Before Phase 1, run:
  grep -rn "TODO" bible-study-tools/tbta --include="*.md" > /tmp/tbta-todos-baseline.txt
- Save to plan/tbta-migration/TODOS-BASELINE.txt
- After completion, verify count decreased by exactly 26

Add to Pre-Execution Checklist:
- [ ] Baseline TODO list captured in TODOS-BASELINE.txt (exact 26 TODOs)
- [ ] Each TODO has file:line:content recorded
```

**3. ❌ README.md examples source verification**
```yaml
Missing Check: Verify examples come from specified source file
Why Critical: Prevents hallucinated examples
How to Add:
- Extract examples from plan/tbta-analysis.md lines 146-375
- Verify README.md contains:
  ✓ "Genesis 1:26" with "clusivity" or "trial number"
  ✓ "172 Austronesian languages" statistic
  ✓ "Genesis 4:8" with "participant tracking" or "ambiguous referent"
  ✓ Time granularity example with "20+ values"

Add to Phase 1 Checklist:
- [ ] Example 1 matches plan/tbta-analysis.md lines 146-200 (clusivity)
- [ ] Example 2 matches plan/tbta-analysis.md lines 201-280 (participant)
- [ ] Example 3 matches plan/tbta-analysis.md lines 281-375 (time granularity)
- [ ] All examples include: feature name, verse ref, language count, impact
```

### PHASE 2: Missing Checks

**4. ❌ Source file existence verification**
```yaml
Missing Check: Verify source files exist before creating documentation
Why Critical: Prevents fabrication if source is missing
How to Add:
- Pre-flight check for each task:
  Task 2.1: Verify plan/tbta-rebuild-with-llm/archive/features-analysis/data-coverage-analysis.md exists
  Task 2.2: Verify plan/tbta-comprehensive-review.md exists
  Task 2.3: Verify plan/tbta-analysis.md exists
  ... etc
- If source missing, FAIL task with error

Add to Pre-Phase 2 Checklist:
- [ ] All source files for Phase 2 tasks exist (8 files)
- [ ] Source files are readable and non-empty (>100 lines each)
```

**5. ❌ Citation format validation**
```yaml
Missing Check: Automated citation format and existence check
Why Critical: Prevents hallucinated sources, ensures consistency
How to Add:
- Script to extract all {citations} from created files
- Verify format matches {lang}-{version} or {llm-cs45}
- Cross-reference against ATTRIBUTION.md
- Flag any citations not in ATTRIBUTION.md

Add to Post-Phase 2 Checklist:
- [ ] All citations extracted and validated (script output: 0 errors)
- [ ] No {llm-*} citations for factual claims (only for summaries)
- [ ] All {lang}-{version} citations exist in ATTRIBUTION.md
```

**6. ❌ Content plagiarism check**
```yaml
Missing Check: Verify content is summarized, not copy-pasted
Why Critical: Respects source licenses, shows understanding
How to Add:
- Compare created files to source files
- Flag sections with >80% similarity (likely copy-paste)
- Require paraphrasing or proper block quotes

Add to Post-Phase 2 Checklist:
- [ ] No file has >80% verbatim overlap with source (plagiarism check)
- [ ] Block quotes are used for direct citations (marked with >)
```

**7. ❌ OT/NT structure documentation completion**
```yaml
Missing Check: Task 2.8 has no clear deliverable or verification
Why Critical: "To be determined" means it could be skipped
How to Add:
- Specify exact deliverable:
  - Create structure/OT-NT-ALIGNMENT.md
  - Include: How TBTA divides testaments, verse mapping strategy, migration path
- Require minimum sections

Add to Phase 2 Checklist (replace Task 2.8):
- [ ] structure/OT-NT-ALIGNMENT.md created
- [ ] Explains TBTA's OT/NT division approach
- [ ] Provides verse alignment algorithm
- [ ] Minimum 150 lines with examples
```

### PHASE 3: Missing Checks

**8. ❌ Automated link checking script**
```yaml
Missing Check: Actual executable script, not manual grep
Why Critical: Manual verification misses errors
How to Add:
- Create scripts/check-links.sh:
  #!/bin/bash
  find bible-study-tools/tbta -name "*.md" | while read file; do
    grep -o '\[.*\](.*)' "$file" | sed 's/.*(\(.*\))/\1/' | while read link; do
      if [[ ! "$link" =~ ^http ]]; then
        target="bible-study-tools/tbta/$(dirname $file)/$link"
        if [[ ! -f "$target" ]]; then
          echo "BROKEN: $file -> $link"
        fi
      fi
    done
  done
- Require: Script exits 0 (no broken links)

Add to Phase 3 Checklist:
- [ ] scripts/check-links.sh executed with 0 broken links
- [ ] All relative paths resolve correctly
- [ ] No links to non-existent files
```

**9. ❌ Progressive disclosure exception documentation**
```yaml
Missing Check: Document WHY files exceed limits
Why Critical: Prevents future bloat, ensures intentional exceptions
How to Add:
- Create plan/tbta-migration/PROGRESSIVE-DISCLOSURE-EXCEPTIONS.md
- For each file >500 lines:
  File: bible-study-tools/tbta/features/STAGES.md
  Lines: 600
  Reason: Comprehensive 6-stage methodology, cannot be split without losing coherence
  Approval: Documented in features/README.md
  Mitigation: Extensive table of contents, clear headings

Add to Phase 3 Checklist:
- [ ] PROGRESSIVE-DISCLOSURE-EXCEPTIONS.md created
- [ ] All files >500 lines documented with justification
- [ ] Exceptions are referenced in parent README.md
```

**10. ❌ TEMPLATE.md content verification**
```yaml
Missing Check: Verify template has required sections
Why Critical: "Actionable" is subjective without concrete requirements
How to Add:
- Require checklist verification:
  ✓ References STAGES.md for methodology
  ✓ Includes 6-stage checklist
  ✓ References FEATURE-AUDIT-TEMPLATE.md
  ✓ Includes progressive disclosure guidance
  ✓ Examples of good feature structure
  ✓ Examples of bad patterns to avoid

Add to Phase 3 Checklist:
- [ ] features/TEMPLATE.md includes STAGES.md reference (exact link)
- [ ] Includes copy of 6-stage checklist from STAGES.md
- [ ] Includes progressive disclosure limits (500/400 lines)
- [ ] Minimum 200 lines with examples
```

### PHASE 4: Missing Checks

**11. ❌ Feature migration completion criteria**
```yaml
Missing Check: What "standardized" means for each tier
Why Critical: Vague criteria allow incomplete work to pass
How to Add:
- Tier A (19 features) - "Standardized" means:
  ✓ README.md exists and follows TEMPLATE.md structure
  ✓ experiments/ directory with train.yaml, test.yaml, validate.yaml
  ✓ experiments/LEARNINGS.md with 6-step error analysis
  ✓ experiments/VALIDATION-RESULTS.md with accuracy metrics
  ✓ All required sections from STAGES.md present
  ✓ Progressive disclosure compliance (≤500 lines)

- Tier B (20 features) - "Migrated or status documented" means:
  ✓ README.md created with current status section
  ✓ If incomplete, status clearly marked as "PARTIAL" with reason
  ✓ Missing files documented in README.md

- Tier C (20 features) - "Scaffolded" means:
  ✓ Directory created
  ✓ README.md with "NOT STARTED" status
  ✓ Placeholder for future work

Add to Phase 4 Checklist:
- [ ] All 19 Tier A features meet standardization criteria (6/6 files present)
- [ ] All 20 Tier B features have README.md with status section
- [ ] All 20 Tier C features have scaffolding (dir + README)
- [ ] Feature count verified: ls features/ | wc -l = 59 (+STAGES, +README, +TEMPLATE = 62 total)
```

---

## 🚨 High-Risk Areas (Quality Could Slip Through)

### Risk 1: Information Loss from Source Files

**Current Check**: "No information loss from plan files" (Success Criteria, Line 391)

**Problem**: Completely unverifiable
- No definition of "information loss"
- No baseline of what information exists in source
- No metric to measure preservation

**How to Game It**:
- Read source file, write completely different content
- Claim "it's a summary, not loss"
- No way to detect

**Mitigation Needed**:
```yaml
ADD TO AUDIT CHECKLIST:

Information Preservation Verification:
- [ ] For each tbta-source/*.md file, create mapping document:
  File: tbta-source/COVERAGE.md
  Source: plan/tbta-rebuild-with-llm/archive/features-analysis/data-coverage-analysis.md
  Key Facts Preserved:
    ✓ 11,649 verses (line 23 of source)
    ✓ 34 books listed (lines 45-67 of source)
    ✓ ~37% coverage (line 89 of source)
  Key Facts Omitted (intentional):
    - Technical TBTA encoding details (out of scope)
    - Implementation specifics (belongs in DATA-STRUCTURE.md)

- [ ] Spot-check 20% of statements against source files
- [ ] All statistics/numbers have source line references
- [ ] No new statistics invented (must be in source)
```

### Risk 2: Feature Migration Quality Degradation

**Current Check**: "All 19 Tier A features standardized" (Line 311)

**Problem**: No verification of WHAT standardized means
- Could create empty files
- Could have incomplete data
- "Standardized" is subjective

**How to Game It**:
- Create all 6 required files with 1 line each
- Mark as "standardized"
- Pass the count check

**Mitigation Needed**:
```yaml
ADD TO PHASE 4 CHECKLIST:

Tier A Feature Quality Gates:
- [ ] Each feature README.md has ALL sections:
  ✓ Feature definition (≥100 words)
  ✓ Theological/linguistic context (≥150 words)
  ✓ Language family analysis (≥5 families listed)
  ✓ STAGES.md checklist (6 stages)
  ✓ File size ≥300 lines OR justification for smaller

- [ ] Each train.yaml has:
  ✓ ≥100 verses total OR documented reason for smaller
  ✓ TBTA values present for verification
  ✓ Valid YAML syntax (yaml-lint passes)

- [ ] Each LEARNINGS.md has:
  ✓ Iterative prompts documented (≥3 iterations)
  ✓ 6-step error analysis present
  ✓ File size ≥200 lines

- [ ] Random sample validation:
  - Select 5 random Tier A features
  - Deep audit against FEATURE-AUDIT-TEMPLATE.md
  - Require 5/5 to pass full audit
```

### Risk 3: Cross-Reference Integrity

**Current Check**: "All markdown links verified (no 404s)" (Line 303)

**Problem**: Manual grep is insufficient
- Won't catch relative path errors
- Won't catch anchor link issues
- Won't catch circular references

**How to Game It**:
- Run grep once, miss broken links in subdirectories
- Claim "verified"
- Links break later

**Mitigation Needed**:
```yaml
ADD TO PHASE 3 CHECKLIST:

Link Integrity Verification:
- [ ] Create scripts/verify-links.sh with:
  #!/bin/bash
  set -e

  # Find all markdown files
  FILES=$(find bible-study-tools/tbta -name "*.md")

  # Extract and verify each link
  for file in $FILES; do
    echo "Checking $file..."

    # Extract markdown links [text](path)
    grep -o '\[.*\](.*)' "$file" | sed 's/.*(\(.*\))/\1/' | while read link; do
      # Skip external URLs
      if [[ "$link" =~ ^https?:// ]]; then
        continue
      fi

      # Resolve relative path
      dir=$(dirname "$file")
      target="$dir/$link"

      # Remove anchor if present
      target="${target%%#*}"

      # Check if file exists
      if [[ ! -f "$target" && ! -d "$target" ]]; then
        echo "ERROR: Broken link in $file -> $link (resolved to $target)"
        exit 1
      fi
    done
  done

  echo "All links verified successfully"

- [ ] scripts/verify-links.sh executed and passed
- [ ] No broken links found (exit code 0)
- [ ] Script added to git pre-commit hook for future protection
```

---

## 📊 Quantitative Audit Metrics

To make the audit objectively measurable, add these metrics:

### Pre-Execution Baseline

```bash
# Capture current state
TODO_COUNT=$(grep -r "TODO" bible-study-tools/tbta --include="*.md" | wc -l)
FILE_COUNT=$(find bible-study-tools/tbta -name "*.md" | wc -l)
LINE_COUNT=$(find bible-study-tools/tbta -name "*.md" -exec wc -l {} \; | awk '{sum+=$1} END {print sum}')

echo "Baseline: $TODO_COUNT TODOs, $FILE_COUNT files, $LINE_COUNT total lines"
```

### Post-Execution Verification

```yaml
Quantitative Success Criteria:

MUST PASS ALL:
- [ ] TODO count decreased by exactly 26: $(grep -r "TODO" ... | wc -l) = BASELINE - 26
- [ ] File count increased by exactly 8: $(find tbta-source -name "*.md" | wc -l) = 8
- [ ] STAGES.md increased by 500-600 lines: wc -l < features/STAGES.md ≈ 600
- [ ] Zero broken links: scripts/verify-links.sh exits 0
- [ ] Zero git uncommitted changes: git status --porcelain | wc -l = 0
- [ ] Progressive disclosure: $(find . -name "*.md" -exec wc -l {} \; | awk '$1 > 500' | wc -l) ≤ documented exceptions
- [ ] All citations valid: scripts/verify-citations.sh exits 0

TIER A FEATURES (19 features):
- [ ] Feature count: ls features/ | grep -v STAGES | grep -v README | grep -v TEMPLATE | wc -l = 59
- [ ] README count: find features/*/README.md | wc -l ≥ 19 (Tier A minimum)
- [ ] train.yaml count: find features/*/experiments/train.yaml | wc -l ≥ 19
- [ ] LEARNINGS.md count: find features/*/experiments/LEARNINGS.md | wc -l ≥ 19
```

---

## 📋 Additional Checklist Items Needed

### Pre-Execution Checklist (ADD)

```yaml
- [ ] Git branch created: tbta-migration-complete
- [ ] Branch pushed to remote: git push -u origin tbta-migration-complete
- [ ] Baseline captured: plan/tbta-migration/BASELINE-METRICS.txt created with:
  - TODO count: {count}
  - File count: {count}
  - Current STAGES.md line count: {count}
  - List of all 26 TODOs with file:line
- [ ] All source files verified to exist (8 source files for Phase 2)
- [ ] Hive memory session initialized: swarm-{session-id}
- [ ] Time estimate confirmed: 6-8 hours available
```

### Phase 1 Checklist (ADD)

```yaml
After Task 1.1:
- [ ] STAGES.md diff shows Stage 4 content added (Dataset Requirements section)
- [ ] STAGES.md diff shows Stage 5 content added (Locked Predictions section)
- [ ] STAGES.md diff shows Stage 6 content added (Subagent Validation section)
- [ ] STAGES.md line count: 550-650 lines (was ~150 before)
- [ ] All 6 TODOs removed (if they existed): git diff shows "- TODO" lines removed

After Task 1.2:
- [ ] grep "11,649" README.md succeeds
- [ ] grep "31,102" README.md fails (old number removed)
- [ ] Intentional focus explanation added (≥50 words)

After Task 1.3:
- [ ] Genesis 1:26 example present with "clusivity" mention
- [ ] Genesis 4:8 example present with "participant tracking" mention
- [ ] Time granularity example present with "20+ values" mention
- [ ] Each example ≥100 words with concrete translation impact
```

### Phase 2 Checklist (ADD)

```yaml
Before Starting Phase 2:
- [ ] All 8 source files exist and are readable
- [ ] plan/tbta-comprehensive-review.md exists
- [ ] plan/tbta-analysis.md exists
- [ ] plan/tbta-rebuild-with-llm/archive/features-analysis/data-coverage-analysis.md exists

After Each File Creation:
- [ ] File has ≥100 lines (not a stub)
- [ ] File has ≥3 citations in {source} format
- [ ] All citations extracted and verified against ATTRIBUTION.md
- [ ] No {llm-*} citations for factual claims
- [ ] File follows progressive disclosure (≤400 lines for topic files)

After Task 2.8:
- [ ] structure/OT-NT-ALIGNMENT.md created (not "to be determined")
- [ ] File explains TBTA testament division
- [ ] File provides verse mapping examples
- [ ] File ≥150 lines
```

### Phase 3 Checklist (ADD)

```yaml
Before Task 3.1:
- [ ] scripts/verify-links.sh created and executable
- [ ] Script tested on one file successfully

After Task 3.1:
- [ ] scripts/verify-links.sh passed with exit code 0
- [ ] Link verification output saved: plan/tbta-migration/LINK-VERIFICATION.txt
- [ ] Zero broken links reported

After Task 3.2:
- [ ] All files measured: find . -name "*.md" -exec wc -l {} \; > DISCLOSURE-AUDIT.txt
- [ ] Exceptions documented: plan/tbta-migration/PROGRESSIVE-DISCLOSURE-EXCEPTIONS.md
- [ ] All exceptions ≤10 files
- [ ] All exceptions have justification in parent README

After Task 3.3:
- [ ] features/TEMPLATE.md has ≥200 lines
- [ ] Template references STAGES.md with exact link
- [ ] Template includes 6-stage checklist
- [ ] Template includes progressive disclosure guidance
- [ ] Template has ≥2 examples (good vs bad)
```

### Phase 4 Checklist (ADD)

```yaml
Before Task 4.1:
- [ ] FEATURE-AUDIT-TEMPLATE.md reviewed and understood
- [ ] Sample feature audited to test template

After Task 4.1:
- [ ] All 59 features inventoried
- [ ] Features categorized into Tiers A/B/C
- [ ] Migration priority list created

After Task 4.2 (Tier A):
- [ ] All 19 Tier A features have required files (6 files each)
- [ ] Random sample of 5 features deep-audited
- [ ] All 5 samples passed FEATURE-AUDIT-TEMPLATE.md
- [ ] Total file count: find features/*/experiments/ | wc -l ≥ 57 (19 × 3)

After Task 4.3 (Tier B):
- [ ] All 20 Tier B features have README.md
- [ ] Each README has status section ("COMPLETE" or "PARTIAL" or "INCOMPLETE")
- [ ] Incomplete features documented with reason

After Task 4.4 (Tier C):
- [ ] All 20 Tier C features have directory
- [ ] All 20 have scaffolding README.md
- [ ] All marked "NOT STARTED" in status
```

### Final Audit Checklist (ADD)

```yaml
Quantitative Verification:
- [ ] TODO count: grep -r "TODO" | wc -l = BASELINE - 26 ✅
- [ ] File count: find tbta-source/*.md | wc -l = 8 ✅
- [ ] Feature count: ls features/ | wc -l ≥ 62 ✅
- [ ] Git status clean: git status --porcelain | wc -l = 0 ✅
- [ ] All tests pass: npm test (if applicable) ✅

Qualitative Verification (Spot Checks):
- [ ] 10 random files checked for citation validity ✅
- [ ] 5 random Tier A features deep-audited ✅
- [ ] 3 random cross-references manually verified ✅
- [ ] Progressive disclosure exceptions all justified ✅

Documentation Verification:
- [ ] README.md approach checklist updated ✅
- [ ] Migration plan marked complete ✅
- [ ] All peer review feedback addressed ✅
- [ ] Lessons learned documented ✅

Git Verification:
- [ ] All commits have meaningful messages ✅
- [ ] Each phase has separate commit ✅
- [ ] No large files committed (≥1MB) ✅
- [ ] Git history is linear (no merge conflicts) ✅
```

---

## 🎯 Recommended Audit Process

### Pre-Flight (Before Any Work)

```bash
# 1. Create baseline snapshot
mkdir -p plan/tbta-migration/audit
grep -rn "TODO" bible-study-tools/tbta --include="*.md" > plan/tbta-migration/audit/BASELINE-TODOS.txt
find bible-study-tools/tbta -name "*.md" -exec wc -l {} \; > plan/tbta-migration/audit/BASELINE-LINES.txt
ls -R bible-study-tools/tbta > plan/tbta-migration/audit/BASELINE-FILES.txt

# 2. Verify all source files exist
./scripts/verify-source-files.sh

# 3. Create verification scripts
./scripts/create-audit-tools.sh
```

### During Execution (After Each Phase)

```bash
# 1. Phase-specific verification
./scripts/verify-phase-1.sh  # or 2, 3, 4

# 2. Git commit with verification
git add bible-study-tools/tbta/
git commit -m "feat(tbta): complete Phase {N} - {description}

Verification:
- TODOs resolved: {count}
- Files created: {count}
- Links verified: {pass/fail}
- Citations validated: {pass/fail}
"
git push

# 3. Update migration plan
# Mark phase complete with timestamp
```

### Post-Completion (Final Audit)

```bash
# 1. Run all verification scripts
./scripts/verify-all.sh

# 2. Generate audit report
./scripts/generate-audit-report.sh > plan/tbta-migration/AUDIT-REPORT.md

# 3. Quantitative comparison
./scripts/compare-baseline.sh plan/tbta-migration/audit/BASELINE-*.txt

# 4. Peer review
# Send to 3 reviewers for final check
```

---

## 🚩 Red Flags to Watch For

During execution, STOP and investigate if you see:

1. **Any task completes in <5 minutes** (except simple renames)
   - Likely rushing, quality suffering

2. **Git commits with >500 files changed**
   - Likely bulk operation without verification

3. **Any file with 0 citations**
   - Likely fabricated content

4. **Any README.md <100 lines**
   - Likely insufficient documentation

5. **scripts/verify-*.sh failing but work continues**
   - Ignoring quality gates

6. **"Partially complete" status without detailed explanation**
   - Hiding incomplete work

7. **Phase 2 completes in <1 hour**
   - Impossible to properly source 8 files in that time

8. **Phase 4 Tier A "complete" but missing files**
   - Gaming the checklist

---

## 📝 Summary of Required Changes

### CRITICAL (Must Add Before Execution)

1. ✅ Add baseline TODO snapshot requirement
2. ✅ Add source file diff verification for STAGES.md
3. ✅ Add automated link checking script
4. ✅ Add citation format validation script
5. ✅ Add feature migration quality gates with file count
6. ✅ Add information preservation verification
7. ✅ Add quantitative metrics to success criteria

### IMPORTANT (Strongly Recommended)

8. ⚠️ Add progressive disclosure exception documentation
9. ⚠️ Add TEMPLATE.md content requirements
10. ⚠️ Add OT/NT structure documentation deliverable
11. ⚠️ Add plagiarism check (80% similarity threshold)

### NICE-TO-HAVE (Quality Improvements)

12. 📋 Add git pre-commit hooks for link verification
13. 📋 Add random sampling verification (5 features deep audit)
14. 📋 Add peer review checklist template

---

## ✅ Conclusion

**Current Risk Level**: ⚠️ MODERATE → HIGH

**Recommendation**: **DO NOT PROCEED** with execution until:

1. All CRITICAL items added to checklist (7 items)
2. Verification scripts created and tested (3 scripts minimum)
3. Baseline snapshot captured
4. Peer review of updated checklist

**Estimated Time to Fix**: 1-2 hours to update plan

**Expected Outcome After Fixes**: ✅ LOW RISK - Audit will be objective and comprehensive

---

**Audit Complete**: ✅ YES
**Requires Follow-up**: ❌ YES - Plan must be updated before execution
**Approval Status**: ⛔ BLOCKED - Do not proceed without addressing critical gaps
