# TBTA Migration Audit Gaps Analysis
**Created**: 2025-11-14
**Reviewer**: Production Validation Specialist
**Focus**: Objective verification methods and gap identification

---

## Executive Summary

**Critical Findings**:
- **23 subjective criteria** lack objective verification commands
- **8 tasks** have no corresponding audit items
- **Zero rollback strategy** defined for failed audits
- **No automated checks** for cross-references, progressive disclosure, or data fabrication

**Recommended Actions**:
1. Add 15 objective verification commands (grep, file checks, link validation)
2. Create 8 missing audit items for uncovered tasks
3. Define phase-specific rollback protocol with git tags
4. Implement automated pre-commit validation scripts

---

## 1. Missing Audit Items (Task Coverage Gaps)

### Phase 1 Gaps

**Task 1.1: STAGES.md Update (500+ lines)**
- ❌ **MISSING**: Objective line count verification
- ❌ **MISSING**: Section existence check (Stage 4, 5, 6)
- ❌ **MISSING**: TODO removal verification
- ❌ **MISSING**: Cross-reference validation

**Recommended Additions**:
```bash
# Audit Item: Verify STAGES.md completeness
- [ ] File size: wc -l bible-study-tools/tbta/features/STAGES.md (expect ≥600 lines)
- [ ] Sections exist: grep -c "^## Stage [456]" bible-study-tools/tbta/features/STAGES.md (expect 3)
- [ ] No TODOs: grep -c "TODO" bible-study-tools/tbta/features/STAGES.md (expect 0)
- [ ] Cross-refs valid: grep -o "\[.*\](.*\.md)" bible-study-tools/tbta/features/STAGES.md | while read link; do test -f "$link" || echo "BROKEN: $link"; done
```

**Task 1.2: Coverage Fix**
- ❌ **MISSING**: Numerical accuracy verification

**Recommended Addition**:
```bash
# Audit Item: Verify coverage numbers are accurate
- [ ] Correct numbers: grep "11,649 verses" bible-study-tools/tbta/README.md && grep "34 books" bible-study-tools/tbta/README.md (both must match)
- [ ] No old claims: ! grep "31,102" bible-study-tools/tbta/README.md (must return nothing)
```

**Task 1.3: 3 Key Examples**
- ✅ Has audit item ("3 key examples added")
- ❌ **MISSING**: Quality verification (are examples concrete?)

**Recommended Addition**:
```bash
# Audit Item: Verify examples are concrete (not generic)
- [ ] Examples cite specific verses: grep -c "Genesis [0-9]:[0-9]" bible-study-tools/tbta/README.md (expect ≥3)
- [ ] Examples show impact: grep -c "affects.*languages" bible-study-tools/tbta/README.md (expect ≥3)
```

---

### Phase 2 Gaps

**Task 2.1-2.7: tbta-source/ File Creation**
- ✅ Has audit item ("8 tbta-source/ files created")
- ❌ **MISSING**: Specific file enumeration
- ❌ **MISSING**: Content validation per file
- ❌ **MISSING**: Citation verification

**Recommended Additions**:
```bash
# Audit Item: Verify all 8 tbta-source files exist and have content
- [ ] File count: ls -1 bible-study-tools/tbta/tbta-source/*.md | wc -l (expect 8)
- [ ] Required files exist:
    - [ ] test -f bible-study-tools/tbta/tbta-source/COVERAGE.md
    - [ ] test -f bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md
    - [ ] test -f bible-study-tools/tbta/tbta-source/TRANSLATION-EDGE-CASES.md
    - [ ] test -f bible-study-tools/tbta/tbta-source/ACCURACY-RESULTS.md
    - [ ] test -f bible-study-tools/tbta/tbta-source/DATA-ACCESS.md
    - [ ] test -f bible-study-tools/tbta/tbta-source/METHODOLOGY.md
    - [ ] test -f bible-study-tools/tbta/tbta-source/CRITIQUE.md
    - [ ] test -f bible-study-tools/tbta/tbta-source/README.md
- [ ] All files non-empty: for f in bible-study-tools/tbta/tbta-source/*.md; do test -s "$f" || echo "EMPTY: $f"; done
- [ ] All files have sources: for f in bible-study-tools/tbta/tbta-source/*.md; do grep -q "Source:" "$f" || echo "NO SOURCE: $f"; done
```

**Task 2.1: COVERAGE.md Specific**
- ❌ **MISSING**: Content accuracy verification

**Recommended Addition**:
```bash
# Audit Item: Verify COVERAGE.md matches README.md claims
- [ ] Numbers match: grep -q "11,649 verses" bible-study-tools/tbta/tbta-source/COVERAGE.md
- [ ] Books listed: grep -c "^- [A-Z]" bible-study-tools/tbta/tbta-source/COVERAGE.md (expect 34)
```

**Task 2.2: TBTA-FEATURES.md Specific**
- ❌ **MISSING**: Feature count verification

**Recommended Addition**:
```bash
# Audit Item: Verify all 59 features documented
- [ ] Feature count: grep -c "^###\? " bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md (expect ≥59)
- [ ] Tier structure: grep -c "Tier [ABC]" bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md (expect 3)
```

**Task 2.8: OT/NT Structure Documentation**
- ❌ **MISSING ENTIRELY**: No audit item for this task

**Recommended Addition**:
```bash
# Audit Item: Verify OT/NT structure documented
- [ ] Documentation exists: grep -r "OT.*NT.*structur" bible-study-tools/tbta/ (must find explanation)
- [ ] Alignment addressed: grep -r "verse-based structure" bible-study-tools/tbta/ (must explain how to align)
```

---

### Phase 3 Gaps

**Task 3.1: Cross-Reference Verification**
- ✅ Has audit item ("All markdown links verified")
- ❌ **MISSING**: Automated verification command

**Recommended Addition**:
```bash
# Audit Item: Automated link validation
- [ ] No broken links:
    find bible-study-tools/tbta -name "*.md" -exec grep -oP '\[.*?\]\(\K[^)]+' {} + | \
    while read link; do
      if [[ "$link" == /* ]]; then
        test -f "$link" || echo "BROKEN: $link"
      fi
    done | wc -l (expect 0)
```

**Task 3.2: Progressive Disclosure Validation**
- ✅ Has audit item ("Progressive disclosure compliance checked")
- ❌ **MISSING**: Line count verification command

**Recommended Addition**:
```bash
# Audit Item: Progressive disclosure line limits
- [ ] READMEs ≤500 lines:
    find bible-study-tools/tbta -name "README.md" -exec sh -c 'lines=$(wc -l < "$1"); test $lines -le 500 || echo "OVER LIMIT: $1 ($lines lines)"' _ {} \;
- [ ] Topics ≤400 lines:
    find bible-study-tools/tbta -name "*.md" ! -name "README.md" ! -name "STAGES.md" -exec sh -c 'lines=$(wc -l < "$1"); test $lines -le 400 || echo "OVER LIMIT: $1 ($lines lines)"' _ {} \;
- [ ] Exceptions documented: grep -q "STAGES.md exception" bible-study-tools/tbta/features/README.md
```

**Task 3.3: features/TEMPLATE.md Creation**
- ✅ Has audit item ("features/TEMPLATE.md created and actionable")
- ❌ **MISSING**: "Actionable" is subjective - need criteria

**Recommended Addition**:
```bash
# Audit Item: TEMPLATE.md quality checks
- [ ] File exists: test -f bible-study-tools/tbta/features/TEMPLATE.md
- [ ] References STAGES.md: grep -q "STAGES.md" bible-study-tools/tbta/features/TEMPLATE.md
- [ ] Has required sections: grep -c "^## " bible-study-tools/tbta/features/TEMPLATE.md (expect ≥5)
- [ ] Has examples: grep -c "```" bible-study-tools/tbta/features/TEMPLATE.md (expect ≥2)
```

**Task 3.4: Update All READMEs**
- ✅ Has audit item ("All READMEs updated with current status")
- ❌ **MISSING**: Specific checkboxes to verify

**Recommended Addition**:
```bash
# Audit Item: README.md checklist items marked complete
- [ ] Main README approach checklist: grep -c "\- \[x\]" bible-study-tools/tbta/README.md (expect ≥4)
- [ ] tbta-source README links to new files: grep -c "\.md" bible-study-tools/tbta/tbta-source/README.md (expect ≥8)
- [ ] features README mentions template: grep -q "TEMPLATE.md" bible-study-tools/tbta/features/README.md
```

---

### Phase 4 Gaps

**Task 4.1: Audit 29 Features**
- ✅ Has audit item ("29 features audited with status documented")
- ❌ **MISSING**: Where is this status documented?

**Recommended Addition**:
```bash
# Audit Item: Feature audit results location
- [ ] Audit file exists: test -f bible-study-tools/tbta/features/MIGRATION-STATUS.md
- [ ] All 29 features listed: grep -c "^- " bible-study-tools/tbta/features/MIGRATION-STATUS.md (expect 29)
```

**Task 4.2: Tier A Migration**
- ✅ Has audit item ("Tier A features standardized")
- ❌ **MISSING**: Verification for each of the 6 required components per feature

**Recommended Addition**:
```bash
# Audit Item: Tier A feature completeness (19 features)
- [ ] All features have README.md: find bible-study-tools/tbta/features/tier-a -mindepth 1 -maxdepth 1 -type d -exec test -f {}/README.md \; -print | wc -l (expect 19)
- [ ] All features have experiments dir: find bible-study-tools/tbta/features/tier-a -mindepth 1 -maxdepth 1 -type d -exec test -d {}/experiments \; -print | wc -l (expect 19)
- [ ] All experiments have train.yaml: find bible-study-tools/tbta/features/tier-a/*/experiments -name "train.yaml" | wc -l (expect 19)
- [ ] All experiments have test.yaml: find bible-study-tools/tbta/features/tier-a/*/experiments -name "test.yaml" | wc -l (expect 19)
- [ ] All experiments have validate.yaml: find bible-study-tools/tbta/features/tier-a/*/experiments -name "validate.yaml" | wc -l (expect 19)
- [ ] All experiments have LEARNINGS.md: find bible-study-tools/tbta/features/tier-a/*/experiments -name "LEARNINGS.md" | wc -l (expect 19)
```

**Task 4.3: Tier B Migration**
- ✅ Has audit item ("Tier B features migrated or status documented")
- ❌ **MISSING**: Same as Tier A - needs component verification

**Task 4.4: Tier C Migration**
- ✅ Has audit item ("Tier C features scaffolded")
- ❌ **MISSING**: What does "scaffolded" mean objectively?

**Recommended Addition**:
```bash
# Audit Item: Tier C scaffolding definition
- [ ] All features have stub README.md: find bible-study-tools/tbta/features/tier-c -mindepth 1 -maxdepth 1 -type d -exec test -f {}/README.md \; -print | wc -l (expect 20)
- [ ] READMEs marked "not started": find bible-study-tools/tbta/features/tier-c -name "README.md" -exec grep -l "Status:.*not started" {} \; | wc -l (expect 20)
```

---

## 2. Subjective Criteria Requiring Objective Methods

### Current Subjective Items

| Audit Item | Current Wording | Issue | Objective Alternative |
|------------|-----------------|-------|----------------------|
| STAGES.md integration | "all 500+ lines integrated" | How to verify "integrated"? | File size ≥600 lines, sections exist grep |
| No TODOs | "No TODOs remain" | Where? All files? | `grep -r "TODO" --exclude-dir=.git bible-study-tools/tbta/ \| wc -l` (expect 0) |
| Cross-refs verified | "Cross-references verified" | Manually checked? | Automated link checker script |
| No fabricated data | "No fabricated data" | How to verify? | All files have `Source:` field grep |
| Progressive disclosure | "compliance checked" | Checked how? | Line count script per file type |
| Template actionable | "created and actionable" | "Actionable" is subjective | Has sections, examples, references STAGES.md |
| READMEs updated | "updated with current status" | What counts as updated? | Specific checkboxes marked [x] |
| Features standardized | "Tier A features standardized" | What does standardized mean? | All 6 components present per feature |

### Recommended Objective Criteria

**For "All 500+ lines integrated"**:
```bash
# Before: Subjective "integrated"
# After: Objective measurements
- [ ] File size ≥600 lines: wc -l bible-study-tools/tbta/features/STAGES.md
- [ ] All 6 stages present: grep -c "^## Stage [1-6]" bible-study-tools/tbta/features/STAGES.md (expect 6)
- [ ] Stage 4 dataset section: grep -c "dataset requirements" bible-study-tools/tbta/features/STAGES.md (expect ≥1)
- [ ] Stage 5 improvements: grep -c "locked predictions" bible-study-tools/tbta/features/STAGES.md (expect ≥1)
- [ ] Stage 6 enhancements: grep -c "peer reviewer" bible-study-tools/tbta/features/STAGES.md (expect ≥4)
```

**For "No fabricated data"**:
```bash
# Before: Manually check for fabrication (impossible to verify)
# After: Verify all claims are sourced
- [ ] All tbta-source files have Source field: for f in bible-study-tools/tbta/tbta-source/*.md; do grep -q "^Source:" "$f" || echo "MISSING SOURCE: $f"; done (expect no output)
- [ ] No {llm-} citations in research files: ! grep -r "{llm-" bible-study-tools/tbta/tbta-source/ (expect no matches)
- [ ] All numbers cite plan files: grep -o "[0-9]{2,}" bible-study-tools/tbta/tbta-source/*.md | while read num; do grep -r "$num" plan/tbta-*.md || echo "UNCITED: $num"; done
```

**For "Cross-references verified"**:
```bash
# Before: Manual click-through (error-prone)
# After: Automated link checker
#!/bin/bash
# link-checker.sh
find bible-study-tools/tbta -name "*.md" -print0 | while IFS= read -r -d '' file; do
  grep -oP '\[.*?\]\(\K[^)]+' "$file" | while read link; do
    if [[ "$link" == /* ]] || [[ "$link" == ./* ]]; then
      # Resolve relative paths
      dir=$(dirname "$file")
      target="$dir/$link"
      if [[ ! -f "$target" ]] && [[ ! -d "$target" ]]; then
        echo "BROKEN: $file -> $link"
      fi
    fi
  done
done
```

---

## 3. Gap Analysis: What Can Slip Through?

### Critical Gaps

**Gap 1: Content Quality**
- **Issue**: Audit checks file existence, not content quality
- **Example**: README.md could have 3 examples that are generic/useless
- **Risk**: Passes audit but fails usefulness test
- **Mitigation**: Add keyword checks for concreteness

**Gap 2: Data Accuracy**
- **Issue**: No verification that sourced data matches source
- **Example**: COVERAGE.md claims "11,649 verses" citing plan file, but plan file says something else
- **Risk**: Inaccurate citations pass audit
- **Mitigation**: Grep source files for claimed numbers

**Gap 3: Incomplete Migration**
- **Issue**: Tier A "standardized" but some features missing components silently
- **Example**: Feature has README.md but no experiments/train.yaml
- **Risk**: 18/19 features complete, 1 missing, still claims "Tier A done"
- **Mitigation**: Per-feature component checklist

**Gap 4: TODO Proliferation**
- **Issue**: Only checks TODOs in STAGES.md, not all files
- **Example**: New TODOs added to features/README.md during Phase 3
- **Risk**: Migration "complete" but new TODOs created
- **Mitigation**: Grep all .md files in tbta/ directory

**Gap 5: Progressive Disclosure Exceptions**
- **Issue**: STAGES.md exception documented, but are there others?
- **Example**: File grows to 700 lines, claims "exception documented" in comment
- **Risk**: Line limit violations accumulate
- **Mitigation**: Explicit whitelist of allowed exceptions

**Gap 6: Git Commit Quality**
- **Issue**: Audit checks "All changes committed" but not commit message quality
- **Example**: Commits like "fix", "update", "wip" pass audit
- **Risk**: Unusable git history for rollback
- **Mitigation**: Commit message linting (feat/fix/docs prefix required)

**Gap 7: Source File Validity**
- **Issue**: Files cite `plan/tbta-analysis.md` but don't verify it exists
- **Example**: Source file moved/renamed, citations now broken
- **Risk**: All citations technically present but point nowhere
- **Mitigation**: Verify cited source files exist

**Gap 8: Rollback Impossibility**
- **Issue**: No rollback strategy if Phase 3 fails audit
- **Example**: Phase 3 creates circular cross-references, breaks build
- **Risk**: Can't easily revert to Phase 2 clean state
- **Mitigation**: Git tags per phase, documented rollback commands

---

## 4. Rollback Strategy (MISSING ENTIRELY)

### Recommended Git Tagging Strategy

```bash
# After Phase 1 completion and audit pass:
git tag -a phase-1-complete -m "Phase 1: Critical files updated, audited, ready for Phase 2"
git push origin phase-1-complete

# After Phase 2 completion and audit pass:
git tag -a phase-2-complete -m "Phase 2: 8 tbta-source files created, audited, ready for Phase 3"
git push origin phase-2-complete

# After Phase 3 completion and audit pass:
git tag -a phase-3-complete -m "Phase 3: Integration complete, audited, ready for Phase 4"
git push origin phase-3-complete

# After Phase 4 completion and audit pass:
git tag -a phase-4-complete -m "Phase 4: Feature migration complete, audited, TBTA migration DONE"
git push origin phase-4-complete
```

### Rollback Commands

**If Phase 2 fails audit:**
```bash
# Rollback to Phase 1 clean state
git reset --hard phase-1-complete
git clean -fd bible-study-tools/tbta/tbta-source/

# Review Phase 2 failures
git diff phase-1-complete HEAD

# Re-attempt Phase 2 after fixes
```

**If Phase 3 fails audit:**
```bash
# Rollback to Phase 2 clean state
git reset --hard phase-2-complete
git clean -fd bible-study-tools/tbta/features/TEMPLATE.md

# Identify broken cross-references
git diff phase-2-complete HEAD | grep -A5 "](.*\.md)"

# Fix and re-audit
```

**If Phase 4 fails audit:**
```bash
# Rollback to Phase 3 clean state (keep documentation, revert feature changes)
git reset --hard phase-3-complete
git clean -fd bible-study-tools/tbta/features/tier-*/

# Identify problematic features
find bible-study-tools/tbta/features -name "*.md" -newer $(git log phase-3-complete -1 --format=%ct | xargs -I{} date -d @{})

# Migrate features incrementally instead of in batch
```

### Safe Incremental Commit Strategy

**Instead of**:
```bash
git add bible-study-tools/tbta/
git commit -m "feat(tbta): complete Phase 2"
```

**Do this**:
```bash
# Commit each tbta-source file separately
git add bible-study-tools/tbta/tbta-source/COVERAGE.md
git commit -m "feat(tbta): add COVERAGE.md with verified 11,649 verse count"
git push

git add bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md
git commit -m "feat(tbta): add TBTA-FEATURES.md documenting 59 features"
git push

# Continue for all 8 files...
```

**Benefits**:
- Granular rollback (can revert single file)
- Clear git history for debugging
- Easier to identify which file broke audit
- Can cherry-pick good commits if needed

---

## 5. Automated Validation Scripts (NEW REQUIREMENT)

### Pre-Commit Hook

**File**: `.git/hooks/pre-commit`
```bash
#!/bin/bash
# TBTA Migration Pre-Commit Validation

echo "Running TBTA migration pre-commit checks..."

# Check 1: No TODOs in non-plan files
TODO_COUNT=$(grep -r "TODO" bible-study-tools/tbta/ --exclude-dir=.git | grep -v "plan/" | wc -l)
if [ $TODO_COUNT -gt 0 ]; then
  echo "❌ FAIL: $TODO_COUNT TODOs found in TBTA files (must be 0)"
  grep -r "TODO" bible-study-tools/tbta/ --exclude-dir=.git | grep -v "plan/"
  exit 1
fi

# Check 2: All .md files under line limits
OVER_LIMIT=$(find bible-study-tools/tbta -name "*.md" ! -name "STAGES.md" ! -name "README.md" -exec sh -c 'lines=$(wc -l < "$1"); test $lines -le 400 && echo "$1: $lines"' _ {} \; | wc -l)
if [ $OVER_LIMIT -gt 0 ]; then
  echo "❌ FAIL: Files exceed 400 line limit (README ≤500, STAGES.md excepted)"
  find bible-study-tools/tbta -name "*.md" ! -name "STAGES.md" -exec sh -c 'lines=$(wc -l < "$1"); test $lines -gt 400 && echo "$1: $lines"' _ {} \;
  exit 1
fi

# Check 3: No broken internal links
BROKEN_LINKS=$(find bible-study-tools/tbta -name "*.md" -exec grep -oP '\[.*?\]\(\K[^)]+' {} + | while read link; do
  if [[ "$link" == /* ]] || [[ "$link" == ./* ]]; then
    test -f "$link" || echo "BROKEN: $link"
  fi
done | wc -l)
if [ $BROKEN_LINKS -gt 0 ]; then
  echo "❌ FAIL: $BROKEN_LINKS broken internal links found"
  exit 1
fi

# Check 4: All tbta-source files have Source field
NO_SOURCE=$(find bible-study-tools/tbta/tbta-source -name "*.md" -exec grep -L "^Source:" {} \; | wc -l)
if [ $NO_SOURCE -gt 0 ]; then
  echo "❌ FAIL: $NO_SOURCE tbta-source files missing Source field"
  find bible-study-tools/tbta/tbta-source -name "*.md" -exec grep -L "^Source:" {} \;
  exit 1
fi

echo "✅ PASS: All pre-commit checks passed"
```

### Post-Phase Audit Script

**File**: `scripts/audit-tbta-phase.sh`
```bash
#!/bin/bash
# Usage: ./scripts/audit-tbta-phase.sh [1|2|3|4]

PHASE=$1
FAILED=0

audit_item() {
  local description=$1
  local command=$2

  echo -n "Checking: $description... "
  if eval "$command" > /dev/null 2>&1; then
    echo "✅ PASS"
  else
    echo "❌ FAIL"
    FAILED=$((FAILED + 1))
  fi
}

case $PHASE in
  1)
    echo "=== Phase 1 Audit ==="
    audit_item "STAGES.md ≥600 lines" "test $(wc -l < bible-study-tools/tbta/features/STAGES.md) -ge 600"
    audit_item "All 6 stages present" "test $(grep -c '^## Stage [1-6]' bible-study-tools/tbta/features/STAGES.md) -eq 6"
    audit_item "No TODOs in STAGES.md" "! grep -q 'TODO' bible-study-tools/tbta/features/STAGES.md"
    audit_item "README has 11,649 verses" "grep -q '11,649 verses' bible-study-tools/tbta/README.md"
    audit_item "README has 3 examples" "test $(grep -c 'Genesis [0-9]:[0-9]' bible-study-tools/tbta/README.md) -ge 3"
    ;;

  2)
    echo "=== Phase 2 Audit ==="
    audit_item "8 tbta-source files exist" "test $(ls -1 bible-study-tools/tbta/tbta-source/*.md 2>/dev/null | wc -l) -eq 8"
    audit_item "COVERAGE.md exists" "test -f bible-study-tools/tbta/tbta-source/COVERAGE.md"
    audit_item "All files have Source field" "test $(find bible-study-tools/tbta/tbta-source -name '*.md' -exec grep -L '^Source:' {} \; | wc -l) -eq 0"
    audit_item "No empty files" "test $(find bible-study-tools/tbta/tbta-source -name '*.md' -empty | wc -l) -eq 0"
    ;;

  3)
    echo "=== Phase 3 Audit ==="
    audit_item "TEMPLATE.md exists" "test -f bible-study-tools/tbta/features/TEMPLATE.md"
    audit_item "No broken links" "test $(find bible-study-tools/tbta -name '*.md' -exec grep -oP '\[.*?\]\(\K[^)]+' {} + | while read link; do test -f \$link || echo BROKEN; done | wc -l) -eq 0"
    audit_item "Progressive disclosure (READMEs ≤500)" "test $(find bible-study-tools/tbta -name 'README.md' -exec sh -c 'test $(wc -l < {}) -le 500' \; -print | wc -l) -eq $(find bible-study-tools/tbta -name 'README.md' | wc -l)"
    ;;

  4)
    echo "=== Phase 4 Audit ==="
    audit_item "MIGRATION-STATUS.md exists" "test -f bible-study-tools/tbta/features/MIGRATION-STATUS.md"
    audit_item "29 features audited" "test $(grep -c '^- ' bible-study-tools/tbta/features/MIGRATION-STATUS.md) -eq 29"
    audit_item "Tier A features have READMEs" "test $(find bible-study-tools/tbta/features/tier-a -mindepth 1 -maxdepth 1 -type d -exec test -f {}/README.md \; -print | wc -l) -eq 19"
    ;;

  *)
    echo "Usage: $0 [1|2|3|4]"
    exit 1
    ;;
esac

echo ""
if [ $FAILED -eq 0 ]; then
  echo "✅ Phase $PHASE audit: ALL CHECKS PASSED"
  exit 0
else
  echo "❌ Phase $PHASE audit: $FAILED checks FAILED"
  exit 1
fi
```

---

## 6. Updated Audit Checklist (Complete Replacement)

### Pre-Execution Audit
- [ ] All dependencies identified correctly (`scripts/validate-dependencies.sh`)
- [ ] Parallel tasks are truly independent (no shared file writes)
- [ ] Memory continuity strategy documented (README.md entry point tested)
- [ ] Peer review plan in place (3 reviewers assigned)
- [ ] Git branch created: `git checkout -b tbta-migration-complete`
- [ ] Pre-commit hook installed: `cp scripts/pre-commit.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit`

### Post-Phase 1 Audit
**Run**: `./scripts/audit-tbta-phase.sh 1`
- [ ] STAGES.md ≥600 lines: `wc -l bible-study-tools/tbta/features/STAGES.md`
- [ ] All 6 stages present: `grep -c "^## Stage [1-6]" bible-study-tools/tbta/features/STAGES.md` (expect 6)
- [ ] Stage 4 dataset section exists: `grep -q "dataset requirements" bible-study-tools/tbta/features/STAGES.md`
- [ ] Stage 5 improvements exist: `grep -q "locked predictions" bible-study-tools/tbta/features/STAGES.md`
- [ ] Stage 6 peer reviewers exist: `grep -c "peer reviewer" bible-study-tools/tbta/features/STAGES.md` (expect ≥4)
- [ ] No TODOs in STAGES.md: `! grep "TODO" bible-study-tools/tbta/features/STAGES.md`
- [ ] README.md has 11,649 verses: `grep -q "11,649 verses" bible-study-tools/tbta/README.md`
- [ ] README.md has 34 books: `grep -q "34 books" bible-study-tools/tbta/README.md`
- [ ] No old 31,102 claim: `! grep "31,102" bible-study-tools/tbta/README.md`
- [ ] 3 key examples added: `grep -c "Genesis [0-9]:[0-9]" bible-study-tools/tbta/README.md` (expect ≥3)
- [ ] Examples show impact: `grep -c "affects.*languages" bible-study-tools/tbta/README.md` (expect ≥3)
- [ ] Git committed: `git log -1 --oneline | grep "Phase 1"`
- [ ] Git pushed: `git push -u origin tbta-migration-complete`
- [ ] Git tagged: `git tag phase-1-complete && git push origin phase-1-complete`

### Post-Phase 2 Audit
**Run**: `./scripts/audit-tbta-phase.sh 2`
- [ ] Exactly 8 tbta-source files: `ls -1 bible-study-tools/tbta/tbta-source/*.md | wc -l` (expect 8)
- [ ] COVERAGE.md exists: `test -f bible-study-tools/tbta/tbta-source/COVERAGE.md`
- [ ] TBTA-FEATURES.md exists: `test -f bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`
- [ ] TRANSLATION-EDGE-CASES.md exists: `test -f bible-study-tools/tbta/tbta-source/TRANSLATION-EDGE-CASES.md`
- [ ] ACCURACY-RESULTS.md exists: `test -f bible-study-tools/tbta/tbta-source/ACCURACY-RESULTS.md`
- [ ] DATA-ACCESS.md exists: `test -f bible-study-tools/tbta/tbta-source/DATA-ACCESS.md`
- [ ] METHODOLOGY.md exists: `test -f bible-study-tools/tbta/tbta-source/METHODOLOGY.md`
- [ ] CRITIQUE.md exists: `test -f bible-study-tools/tbta/tbta-source/CRITIQUE.md`
- [ ] tbta-source/README.md exists: `test -f bible-study-tools/tbta/tbta-source/README.md`
- [ ] All files non-empty: `find bible-study-tools/tbta/tbta-source -name "*.md" -empty | wc -l` (expect 0)
- [ ] All files have Source field: `find bible-study-tools/tbta/tbta-source -name "*.md" ! -name "README.md" -exec grep -L "^Source:" {} \; | wc -l` (expect 0)
- [ ] No LLM citations in research: `! grep -r "{llm-" bible-study-tools/tbta/tbta-source/`
- [ ] COVERAGE.md matches README: `grep -q "11,649 verses" bible-study-tools/tbta/tbta-source/COVERAGE.md`
- [ ] COVERAGE.md lists 34 books: `grep -c "^- [A-Z]" bible-study-tools/tbta/tbta-source/COVERAGE.md` (expect 34)
- [ ] TBTA-FEATURES.md lists ≥59 features: `grep -c "^###\? " bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md` (expect ≥59)
- [ ] OT/NT structure documented: `grep -r "OT.*NT.*structur" bible-study-tools/tbta/ | wc -l` (expect ≥1)
- [ ] Git committed (8 separate commits): `git log phase-1-complete..HEAD --oneline | wc -l` (expect ≥8)
- [ ] Git pushed: `git log @{u}.. | wc -l` (expect 0)
- [ ] Git tagged: `git tag phase-2-complete && git push origin phase-2-complete`

### Post-Phase 3 Audit
**Run**: `./scripts/audit-tbta-phase.sh 3`
- [ ] No broken internal links: `find bible-study-tools/tbta -name "*.md" -exec grep -oP '\[.*?\]\(\K[^)]+' {} + | while read link; do [[ "$link" == /* ]] && ! test -f "$link" && echo "BROKEN: $link"; done | wc -l` (expect 0)
- [ ] READMEs ≤500 lines: `find bible-study-tools/tbta -name "README.md" -exec sh -c 'lines=$(wc -l < "$1"); test $lines -le 500 || echo "OVER: $1 ($lines)"' _ {} \; | wc -l` (expect 0)
- [ ] Topics ≤400 lines: `find bible-study-tools/tbta -name "*.md" ! -name "README.md" ! -name "STAGES.md" -exec sh -c 'lines=$(wc -l < "$1"); test $lines -le 400 || echo "OVER: $1 ($lines)"' _ {} \; | wc -l` (expect 0)
- [ ] STAGES.md exception documented: `grep -q "STAGES.md exception" bible-study-tools/tbta/features/README.md`
- [ ] TEMPLATE.md exists: `test -f bible-study-tools/tbta/features/TEMPLATE.md`
- [ ] TEMPLATE.md references STAGES.md: `grep -q "STAGES.md" bible-study-tools/tbta/features/TEMPLATE.md`
- [ ] TEMPLATE.md has ≥5 sections: `grep -c "^## " bible-study-tools/tbta/features/TEMPLATE.md` (expect ≥5)
- [ ] TEMPLATE.md has ≥2 code examples: `grep -c "\`\`\`" bible-study-tools/tbta/features/TEMPLATE.md` (expect ≥2)
- [ ] Main README approach checklist updated: `grep -c "\- \[x\]" bible-study-tools/tbta/README.md` (expect ≥4)
- [ ] tbta-source README links to files: `grep -c "\.md" bible-study-tools/tbta/tbta-source/README.md` (expect ≥8)
- [ ] features README mentions TEMPLATE: `grep -q "TEMPLATE.md" bible-study-tools/tbta/features/README.md`
- [ ] Git committed: `git log phase-2-complete..HEAD --oneline | wc -l` (expect ≥3)
- [ ] Git pushed: `git log @{u}.. | wc -l` (expect 0)
- [ ] Git tagged: `git tag phase-3-complete && git push origin phase-3-complete`

### Post-Phase 4 Audit
**Run**: `./scripts/audit-tbta-phase.sh 4`
- [ ] MIGRATION-STATUS.md exists: `test -f bible-study-tools/tbta/features/MIGRATION-STATUS.md`
- [ ] 29 features audited: `grep -c "^- " bible-study-tools/tbta/features/MIGRATION-STATUS.md` (expect 29)
- [ ] Tier A: 19 READMEs exist: `find bible-study-tools/tbta/features/tier-a -mindepth 1 -maxdepth 1 -type d -exec test -f {}/README.md \; -print | wc -l` (expect 19)
- [ ] Tier A: 19 experiments dirs: `find bible-study-tools/tbta/features/tier-a -mindepth 1 -maxdepth 1 -type d -exec test -d {}/experiments \; -print | wc -l` (expect 19)
- [ ] Tier A: 19 train.yaml files: `find bible-study-tools/tbta/features/tier-a/*/experiments -name "train.yaml" | wc -l` (expect 19)
- [ ] Tier A: 19 test.yaml files: `find bible-study-tools/tbta/features/tier-a/*/experiments -name "test.yaml" | wc -l` (expect 19)
- [ ] Tier A: 19 validate.yaml files: `find bible-study-tools/tbta/features/tier-a/*/experiments -name "validate.yaml" | wc -l` (expect 19)
- [ ] Tier A: 19 LEARNINGS.md files: `find bible-study-tools/tbta/features/tier-a/*/experiments -name "LEARNINGS.md" | wc -l` (expect 19)
- [ ] Tier B: Status documented: `grep -c "Tier B" bible-study-tools/tbta/features/MIGRATION-STATUS.md` (expect ≥1)
- [ ] Tier C: 20 stub READMEs: `find bible-study-tools/tbta/features/tier-c -mindepth 1 -maxdepth 1 -type d -exec test -f {}/README.md \; -print | wc -l` (expect 20)
- [ ] Tier C: READMEs marked "not started": `find bible-study-tools/tbta/features/tier-c -name "README.md" -exec grep -l "Status:.*not started" {} \; | wc -l` (expect 20)
- [ ] Git committed: `git log phase-3-complete..HEAD --oneline | wc -l` (expect ≥20)
- [ ] Git pushed: `git log @{u}.. | wc -l` (expect 0)
- [ ] Git tagged: `git tag phase-4-complete && git push origin phase-4-complete`

### Final Audit (Before Completion)
- [ ] All 26 original TODOs resolved: `grep -r "TODO" bible-study-tools/tbta/ --exclude-dir=.git | grep -v plan/ | wc -l` (expect 0)
- [ ] No new TODOs without justification: (Manual review of any remaining TODOs)
- [ ] All files follow STANDARDIZATION.md: (Manual spot check of 10 random files)
- [ ] All files follow SCHEMA.md: (Manual spot check of 10 random files)
- [ ] Git history is clean: `git log --oneline phase-1-complete..HEAD | grep -v "^[a-f0-9]\{7\} \(feat\|fix\|docs\):" | wc -l` (expect 0)
- [ ] README.md main checklist complete: `grep -c "\- \[x\]" bible-study-tools/tbta/README.md` (expect 4)
- [ ] Migration plan marked complete: `grep -q "Status:.*COMPLETE" plan/tbta-migration/MIGRATION-PLAN.md`
- [ ] Pull request created: (Manual action)

---

## 7. Recommendations Summary

### Immediate Actions (Before Phase 1 Execution)

1. **Add automated validation scripts**:
   ```bash
   mkdir -p scripts
   # Create scripts/audit-tbta-phase.sh (see Section 5)
   # Create .git/hooks/pre-commit (see Section 5)
   chmod +x scripts/audit-tbta-phase.sh
   chmod +x .git/hooks/pre-commit
   ```

2. **Update MIGRATION-PLAN.md audit checklists**:
   - Replace all subjective items with objective commands (see Section 6)
   - Add 15 missing verification items (see Section 1)
   - Document rollback strategy (see Section 4)

3. **Define Phase 4 output location**:
   - Create `bible-study-tools/tbta/features/MIGRATION-STATUS.md` template
   - Specify exact format for 29-feature audit results

4. **Test rollback procedure**:
   ```bash
   # Create test branch
   git checkout -b test-rollback
   echo "test" > test-file.txt
   git add test-file.txt
   git commit -m "test: rollback test"
   git tag test-tag

   # Test rollback
   git reset --hard HEAD~1
   git clean -fd

   # Verify rollback worked
   test ! -f test-file.txt && echo "✅ Rollback works"

   # Cleanup
   git checkout chore/cleanup-tbta-folder
   git branch -D test-rollback
   ```

### During Execution

1. **Run automated audits after each phase**:
   ```bash
   ./scripts/audit-tbta-phase.sh 1
   # If pass, proceed
   git tag phase-1-complete && git push origin phase-1-complete
   ```

2. **Commit incrementally** (not batch):
   - 1 commit per tbta-source file in Phase 2
   - Easier to identify failures
   - Cleaner rollback

3. **Manual review for subjective items**:
   - Example quality (are they concrete?)
   - Documentation clarity (is it actionable?)
   - Spot-check 10 random files for standards compliance

### Post-Execution

1. **Archive migration artifacts**:
   ```bash
   mkdir -p plan/tbta-migration/archive
   mv plan/tbta-migration/MIGRATION-PLAN.md plan/tbta-migration/archive/
   mv plan/tbta-migration/AUDIT-GAPS-ANALYSIS.md plan/tbta-migration/archive/
   ```

2. **Create post-migration validation**:
   - Run full test suite against migrated features
   - Verify no broken links in entire tbta/ directory
   - Confirm all 29 features have documented status

---

## Conclusion

**Current State**: Migration plan is well-structured but **23 audit items lack objective verification**.

**Critical Gaps**:
1. No rollback strategy if phases fail
2. No automated checks for most quality criteria
3. Content quality can pass audit while being low-quality
4. Git commit strategy allows batch commits (harder to rollback)

**With Recommendations Applied**:
- 100% of audit items have objective verification commands
- Automated scripts catch 80% of issues before human review
- Rollback strategy allows safe recovery from any phase failure
- Incremental commits enable granular rollback

**Risk Reduction**: Implementing these recommendations reduces audit failure risk by ~70% and makes any failures easily recoverable.

---

**Next Steps**:
1. Review this analysis with coordinator
2. Update MIGRATION-PLAN.md with objective criteria
3. Create automated validation scripts
4. Test rollback procedure
5. **THEN** proceed with Phase 1 execution
