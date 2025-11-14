# TBTA Migration - Executable Plan v2.0

**Status**: ✅ Peer Reviewed & Revised
**Scope**: Documentation Foundation (Phases 1-3)
**Feature Migration**: Deferred to separate epic

---

## Mission

Complete all TODOs in `bible-study-tools/tbta/` through systematic migration of content from `plan/tbta-rebuild-with-llm/` into standardized structure.

**Key Changes from v1.0**:
- ✅ Fixed 6 critical dependency issues
- ✅ Added 3 verification scripts
- ✅ Added baseline capture
- ✅ Removed Phase 4 (separate epic)
- ✅ Replaced hour estimates with t-shirt sizing

---

## Complexity Sizing (T-Shirt)

| Size | Description | Agent Effort |
|------|-------------|--------------|
| **XS** | Trivial - few minutes | Quick edit, single file |
| **S** | Small - straightforward | Simple migration, clear source |
| **M** | Medium - moderate complexity | Analysis + synthesis required |
| **L** | Large - significant effort | Multiple sources, careful integration |
| **XL** | Extra large - substantial | Complex analysis, iteration needed |

**Total Effort**: ~**3L + 5M + 6S + 2XS** = Substantial but achievable

---

## Pre-Flight Checklist (MUST RUN FIRST)

### Verification Scripts

Create these scripts before starting any work:

#### Script 1: verify-links.sh (Size: **S**)
```bash
#!/bin/bash
# Verify all markdown links point to existing files
cd bible-study-tools/tbta
errors=0

while IFS= read -r file; do
  while IFS= read -r link; do
    # Extract path from [text](path) format
    path=$(echo "$link" | sed 's/.*(\(.*\)).*/\1/')

    # Skip URLs and anchors
    [[ "$path" =~ ^http ]] && continue
    [[ "$path" =~ ^# ]] && continue

    # Check if file exists (relative to current file's directory)
    dir=$(dirname "$file")
    if [[ ! -f "$dir/$path" && ! -f "$path" ]]; then
      echo "❌ Broken link in $file: $path"
      ((errors++))
    fi
  done < <(grep -o '\[.*\](.*[^)])' "$file")
done < <(find . -name "*.md")

if [ $errors -eq 0 ]; then
  echo "✅ All links valid"
  exit 0
else
  echo "❌ Found $errors broken links"
  exit 1
fi
```

#### Script 2: verify-citations.sh (Size: **S**)
```bash
#!/bin/bash
# Verify all {citations} exist in ATTRIBUTION.md
cd bible-study-tools/tbta
attribution_file="../../ATTRIBUTION.md"
errors=0

# Extract all citations from markdown files
while IFS= read -r file; do
  while IFS= read -r citation; do
    # Extract citation code from {code} format
    code=$(echo "$citation" | sed 's/.*{\(.*\)}.*/\1/')

    # Check if citation exists in ATTRIBUTION.md
    if ! grep -q "$code" "$attribution_file"; then
      echo "❌ Unknown citation in $file: {$code}"
      ((errors++))
    fi
  done < <(grep -o '{[a-zA-Z0-9-]*}' "$file")
done < <(find . -name "*.md")

if [ $errors -eq 0 ]; then
  echo "✅ All citations valid"
  exit 0
else
  echo "❌ Found $errors unknown citations"
  exit 1
fi
```

#### Script 3: verify-content-diff.sh (Size: **S**)
```bash
#!/bin/bash
# Verify migrated content matches source (95%+ similarity)
source_file="$1"
target_file="$2"
threshold=95

if [[ ! -f "$source_file" || ! -f "$target_file" ]]; then
  echo "❌ Files not found: $source_file, $target_file"
  exit 1
fi

# Calculate similarity using diff
total_lines=$(wc -l < "$source_file")
diff_lines=$(diff -u "$source_file" "$target_file" | grep -c "^[-+]")
similarity=$((100 - (diff_lines * 100 / total_lines)))

if [ $similarity -ge $threshold ]; then
  echo "✅ Content verified: ${similarity}% similarity"
  exit 0
else
  echo "❌ Content mismatch: ${similarity}% similarity (need ${threshold}%)"
  exit 1
fi
```

### Baseline Capture (Size: **XS**)

```bash
cd /workspaces/mybibletoolbox-code

# Capture TODO baseline
grep -rn "TODO\|FIXME\|XXX" bible-study-tools/tbta/ > plan/tbta-migration/baseline-todos.txt

# Capture file tree
find bible-study-tools/tbta -type f > plan/tbta-migration/baseline-files.txt

# Count actual TODOs
echo "Total TODOs: $(grep -c "TODO" plan/tbta-migration/baseline-todos.txt)"

# Verify source files exist
echo "Verifying source files..."
[ -f plan/tbta-rebuild-with-llm/features/STAGES.md ] && echo "✅ STAGES.md source exists"
[ -f plan/tbta-analysis.md ] && echo "✅ tbta-analysis.md exists"
[ -f plan/tbta-comprehensive-review.md ] && echo "✅ tbta-comprehensive-review.md exists"
```

---

## Phase 1: Critical Updates (SEQUENTIAL)

**Complexity**: **L** (large - blocking all other work)
**Dependencies**: None (but blocks everything)

### Task 1.1: Update STAGES.md with methodology improvements
**Size**: **M**
**File**: `bible-study-tools/tbta/features/STAGES.md`
**Source**: `plan/tbta-rebuild-with-llm/features/STAGES.md`

**Action**:
1. Read both files, identify differences
2. Integrate 500+ lines of improvements (dataset requirements, 6-step analysis, peer review templates)
3. Remove resolved TODOs
4. Verify with: `./verify-content-diff.sh plan/tbta-rebuild-with-llm/features/STAGES.md bible-study-tools/tbta/features/STAGES.md`

**Success Criteria**:
- [ ] All methodology sections integrated
- [ ] All TODOs removed from STAGES.md
- [ ] Content diff shows 95%+ similarity

---

### Task 1.2: Fix coverage claim in README.md
**Size**: **XS**
**File**: `bible-study-tools/tbta/README.md`

**Changes**:
- Line 5: "31,102 verses" → "11,649 verses across 34 books (~37% of Bible)"
- Add: "TBTA intentionally focuses on narrative and discourse-heavy books"
- Add reference: See [tbta-source/COVERAGE.md](tbta-source/COVERAGE.md)

**Success Criteria**:
- [ ] Coverage numbers accurate (11,649 verses)
- [ ] Reference to COVERAGE.md added
- [ ] Git commit: "fix(tbta): correct coverage claim to 11,649 verses"

---

### Task 1.3: Add 3 key examples to README.md
**Size**: **S**
**File**: `bible-study-tools/tbta/README.md`
**Dependencies**: Task 1.2 (sequential - same file)

**Content**: Add after "What is TBTA?" section (line 7):
```markdown
**Why This Matters - 3 Key Examples**:

1. **Clusivity (Genesis 1:26)**: "Let us make man in our image"
   - Languages: 172 Austronesian languages grammatically distinguish trial number (exactly 3 persons)
   - Without TBTA: Translators might use dual (2 persons) or plural (3+), missing the Trinity reference
   - Impact: Affects theological understanding of God's nature in translation

2. **Participant Tracking (Genesis 4:8)**: "Cain spoke to Abel... and killed him"
   - Challenge: Ambiguous referent - which "he" is which?
   - Languages: Affects pronoun choice in 468 Native American languages
   - Without TBTA: Translators might obscure or clarify ambiguity differently than intended

3. **Time Granularity (Genesis narratives)**: Creation account timing
   - Values: 20+ distinct temporal markers (immediate, same day, next day, etc.)
   - Languages: East Asian languages require explicit temporal sequencing
   - Without TBTA: Translators might impose precision or vagueness not present in Hebrew
```

**Source**: `plan/tbta-analysis.md` lines 146-375
**Success Criteria**:
- [ ] 3 examples added with concrete language impact
- [ ] Git commit: "docs(tbta): add 3 translation impact examples"

---

## Phase 2: Independent Documentation (PARALLEL)

**Complexity**: **2L + 4M** (can run 7 tasks simultaneously)
**Dependencies**: Only Task 2.1 waits for 1.2, others start immediately

### Task 2.1: Create tbta-source/COVERAGE.md
**Size**: **S**
**Dependencies**: Task 1.2 (uses coverage numbers)
**Source**: `plan/tbta-rebuild-with-llm/archive/features-analysis/data-coverage-analysis.md`

**Content**:
```markdown
# TBTA Coverage Analysis

**Total Coverage**: 11,649 verses across 34 books (~37% of Bible)

## Books Covered
**Old Testament** (20 books): Genesis, Exodus, Numbers, Deuteronomy, Joshua, Judges, Ruth, 1-2 Samuel, 1-2 Kings, Jonah, Haggai, Zechariah, Daniel, Ezra, Nehemiah, 1-2 Chronicles

**New Testament** (14 books): Matthew, Mark, Luke, John, Acts, Romans, 1-2 Corinthians, Galatians, Ephesians, Philippians, Colossians, 1 Thessalonians

## Intentional Focus

TBTA deliberately prioritizes narrative and discourse-heavy books where cross-linguistic features (participant tracking, discourse genre, speaker demographics) matter most for translation. Books like Leviticus or Psalms have less coverage because linguistic features are more uniform or less critical.

## Coverage by Genre
- **Narrative**: ~8,500 verses (73%)
- **Epistolary**: ~2,000 verses (17%)
- **Prophetic**: ~800 verses (7%)
- **Other**: ~350 verses (3%)

For detailed analysis, see [data-coverage-analysis.md](../../plan/tbta-rebuild-with-llm/archive/features-analysis/data-coverage-analysis.md)
```

**Success Criteria**:
- [ ] Numbers match README.md (11,649 verses)
- [ ] 34 books listed correctly
- [ ] Git commit with coverage data

---

### Task 2.2: Create tbta-source/TBTA-FEATURES.md
**Size**: **L** (59 features to catalog)
**Dependencies**: None
**Source**: `plan/tbta-comprehensive-review.md` lines 40-250

**Content Structure**:
```markdown
# TBTA Feature Catalog

**Total**: 59 features across 15 categories

## Three-Tier Structure

### Tier A: Essential (19 features - 68% complete)
Features affecting 1000+ languages, cannot be easily inferred

| # | Feature | Category | Values | Status |
|---|---------|----------|--------|--------|
| 1 | Number System | Noun | S/D/T/Q/p/P | ✅ Complete |
| 2 | Person System | Noun | 1/2/3/A/B/F/S/I/E | ✅ Complete |
...

### Tier B: Important (20 features - 15% complete)
Common features, sometimes inferable from context
...

### Tier C: Specialized (20 features - 0-70% documented)
Language-specific or rare features
...
```

**Success Criteria**:
- [ ] All 59 features enumerated
- [ ] Accurate status markers (✅/🟨/⬜)
- [ ] Values documented per feature
- [ ] File ≤500 lines or split into tiers

---

### Task 2.3: Create tbta-source/TRANSLATION-EDGE-CASES.md
**Size**: **M**
**Dependencies**: None
**Source**: `plan/tbta-analysis.md` lines 146-375

**Content**: 6 concrete examples showing real translation challenges with Genesis 1:26, 4:8, Acts 15:25, etc.

**Success Criteria**:
- [ ] Examples show real language impact
- [ ] Citations to source texts included
- [ ] File ≤400 lines

---

### Task 2.4: Create tbta-source/CRITIQUE.md
**Size**: **M**
**Dependencies**: None
**Source**: `plan/tbta-rebuild-with-llm/combined/IMPROVEMENTS.md` (validate first)

**Content**: Validated criticisms only, mark speculation
**Success Criteria**:
- [ ] No fabricated claims
- [ ] Evidence-based critiques only
- [ ] Verify citations: `./verify-citations.sh`

---

### Task 2.5: Create tbta-source/DATA-STRUCTURE.md
**Size**: **M**
**Dependencies**: None

**Content**:
- OT vs NT file splitting differences
- Character-based encoding format
- How to parse TBTA codes
- Examples from Genesis (OT) and John (NT)

**Success Criteria**:
- [ ] Clear explanation of OT/NT differences
- [ ] File ≤200 lines

---

### Task 2.6: Update tbta-source/README.md
**Size**: **S**
**Dependencies**: None
**Sources**: `plan/tbta-analysis.md`, `plan/tbta-comprehensive-review.md`

**Content**: Executive summary with links to all created files
**Success Criteria**:
- [ ] File ≤200 lines (progressive disclosure)
- [ ] Links to all tbta-source/*.md files

---

### Task 2.7: Migrate learnings/README.md
**Size**: **L** (57KB source to consolidate)
**Dependencies**: None
**Sources**:
- `plan/tbta-rebuild-with-llm/learnings/*.md` (5 files)
- `plan/tbta-rebuild-with-llm/methodology/ADVERSARIAL-TESTING.md`

**Action**: Consolidate transferable patterns, remove bloat
**Success Criteria**:
- [ ] File ≤400 lines or split into topic files
- [ ] No outdated learnings
- [ ] Mark unvalidated claims with "consider" language

---

## Phase 3: Integration & Templates (SEQUENTIAL)

**Complexity**: **2M + 2S**
**Dependencies**: Phase 1 & 2 complete

### Task 3.1: Verify all cross-references (PARALLEL with 3.2)
**Size**: **S**
**Action**: `./verify-links.sh`
**Success Criteria**:
- [ ] All markdown links resolve
- [ ] Zero broken references

---

### Task 3.2: Progressive disclosure validation (PARALLEL with 3.1)
**Size**: **S**
**Action**: Check line counts

```bash
find bible-study-tools/tbta -name "README.md" -exec wc -l {} \; | awk '$1 > 200 {print "❌", $2, "has", $1, "lines (max 200)"}'
find bible-study-tools/tbta -name "*.md" ! -name "README.md" ! -name "STAGES.md" -exec wc -l {} \; | awk '$1 > 400 {print "⚠️", $2, "has", $1, "lines (max 400)"}'
```

**Success Criteria**:
- [ ] All READMEs ≤200 lines (except STAGES.md ≤500)
- [ ] All topic files ≤400 lines
- [ ] Oversized files split or documented as exceptions

---

### Task 3.3: Create features/TEMPLATE.md
**Size**: **M**
**Dependencies**: Task 3.2 (needs progressive disclosure results)
**Sources**:
- STAGES.md (authoritative)
- FEATURE-AUDIT-TEMPLATE.md
- TEMPLATE-CONSOLIDATION-ANALYSIS.md

**Content**: Consolidated best practices for feature development
**Success Criteria**:
- [ ] References STAGES.md (don't duplicate)
- [ ] File ≤200 lines
- [ ] Actionable template for new features

---

### Task 3.4: Update all READMEs with completion status
**Size**: **M**
**Action**: Update 5 README files with current state

**Files**:
- `bible-study-tools/tbta/README.md` (mark approach checklist items)
- `bible-study-tools/tbta/tbta-source/README.md` (link to new files)
- `bible-study-tools/tbta/features/README.md` (update with template info)
- `bible-study-tools/tbta/languages/README.md` (mark migration status)
- `bible-study-tools/tbta/learnings/README.md` (mark migration status)

**Success Criteria**:
- [ ] All READMEs reflect current state
- [ ] No broken links to newly created files
- [ ] All checklist items updated

---

## Git Workflow

### Branch Strategy
```bash
# Start
git checkout -b tbta-docs-foundation
git push -u origin tbta-docs-foundation

# After each phase
git add bible-study-tools/tbta/ plan/tbta-migration/
git commit -m "feat(tbta): complete Phase {N} - {description}"
git push
```

### Commit Pattern
- Phase 1: "feat(tbta): update STAGES.md and README with corrections"
- Phase 2: "feat(tbta): create tbta-source documentation foundation"
- Phase 3: "feat(tbta): integrate templates and validate structure"

---

## Audit Checklist

### Pre-Execution
- [ ] All 3 verification scripts created and executable
- [ ] Baseline captured (todos.txt, files.txt)
- [ ] Source files verified to exist
- [ ] Git branch created

### Post-Phase 1
- [ ] STAGES.md content diff ≥95% similarity to source
- [ ] README.md has correct coverage (11,649 verses)
- [ ] 3 examples added to README.md
- [ ] All Phase 1 TODOs removed
- [ ] Git commit pushed

### Post-Phase 2
- [ ] 7 files created in tbta-source/
- [ ] `./verify-citations.sh` passes
- [ ] No fabricated statistics
- [ ] All numbers cross-checked against sources
- [ ] Git commit pushed

### Post-Phase 3
- [ ] `./verify-links.sh` passes (zero broken links)
- [ ] Progressive disclosure validated (line counts ≤ limits)
- [ ] features/TEMPLATE.md created
- [ ] All 5 READMEs updated
- [ ] Git commit pushed

### Final Validation
- [ ] All original TODOs from baseline resolved
- [ ] No new unjustified TODOs
- [ ] All files follow STANDARDIZATION.md conventions
- [ ] Git history is clean with meaningful commits
- [ ] Ready for production feature work

---

## Success Metrics

**Quantitative**:
- All baseline TODOs resolved ✅
- 0 broken links ✅
- 0 unknown citations ✅
- 7 new tbta-source/ files ✅
- 3 verification scripts ✅

**Qualitative**:
- Documentation is clear and actionable
- Subagents can navigate using READMEs
- Migration is repeatable (documented process)
- No information loss from source files
- Foundation ready for feature work

---

## Out of Scope (Future Epic)

**Feature Migration** (Phase 4 from v1.0):
- **Complexity**: ~**XL** (30+ feature directories)
- **Prerequisite**: Verify feature directories exist
- **Approach**: Feature-by-feature with quality gates
- **Timeline**: Separate planning required

---

**Plan Status**: ✅ READY FOR EXECUTION
**Version**: 2.0 (Peer Reviewed & Revised)
**Date**: 2025-11-14
