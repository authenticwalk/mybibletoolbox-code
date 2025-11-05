# Scripts Folder Review

Date: 2025-11-05
Reviewer: AI Assistant

## Summary

These are **experimental/abandoned scripts** from a refactoring attempt. They can be **REMOVED**.

---

## Analysis

### Scripts in Question

1. **build_strongs_references.py** (325 lines)
   - Purpose: Build `.references.yaml` files for ALL Strong's numbers showing verse occurrences
   - Scope: Full Bible (Greek NT + Hebrew OT)
   - Output: `{strongs_number}.references.yaml` files

2. **test_matthew5_strongs.py** (288 lines)
   - Purpose: Test version of build_strongs_references.py
   - Scope: Matthew 5 only
   - Output: Same `.references.yaml` format

3. **test_strongs_references.py** (238 lines)
   - Purpose: Earlier test version
   - Scope: Mark + Genesis 1
   - Output: `{strongs_number}-references.yaml` format (different filename)

### Git History

```
2ab6c25 chore: cleanup
cbf0c36 feat: update Strong's reference building and test scripts
4536d85 refactor: change from 3-repo to 2-repo split structure
9429fcc fix: update scripts to use data/lexicon path structure
e126384 fix: update Strong's reference builder for standardized format
dfed432 fix: align Strong's reference structure with SCHEMA.md
d7a6fc0 refactor: improve Strong's reference structure
d4bbe74 feat: add Strong's dictionary reference builder
```

**Interpretation**: These scripts went through multiple iterations trying to find the right format, then were cleaned up, but **never fully integrated or used**.

---

## Why They Can Be Removed

### 1. No Output Files Exist
```bash
find .data/strongs -name "*.references.yaml"
# Result: Empty (no files found)
```

**Conclusion**: These scripts were never run in production or their output was never committed.

### 2. No Code References Them
- Searched entire codebase for `.references.yaml` - **no matches**
- No imports of these script modules
- No documentation referencing them

### 3. Functionality is Redundant

The `macula_processor.py` already provides this functionality:
- Parses Macula XML data
- Extracts Strong's numbers per verse
- Creates per-verse YAML files with Strong's data

**Key Difference**: 
- These scripts: Organize by Strong's number (inverse index)
- Macula processor: Organize by verse (primary use case)

The inverse index approach (by Strong's number) was **attempted but never completed or adopted**.

### 4. Already Flagged for Cleanup

From `plan/code-cleanup/CLEANUP-ANALYSIS.md`:
```markdown
#### Scripts Organization
- [ ] **scripts/** directory
  - Current Files:
    - `build_strongs_references.py`
    - `test_matthew5_strongs.py`
    - `test_strongs_references.py`
  - *Action*: Split into `/scripts/build/` and `/scripts/test/`
  - *Reason*: Better organization of build vs test scripts
```

But since they're not being used, moving them is pointless - they should be **removed**.

---

## Recommendation

### ✅ DELETE ALL THREE SCRIPTS

**Rationale**:
1. Experimental code that was never integrated
2. No output files exist from these scripts
3. No other code depends on them
4. Functionality is covered by macula_processor.py
5. Been through multiple refactors but never reached production

### If Needed in Future

The concept of a "Strong's reference index" (showing all verses for each Strong's number) **could** be useful, but would need:
1. A clear use case / requirement
2. Integration with existing tools
3. Proper tool definition (like other bible-study-tools)
4. Tests and documentation

For now: **Git history preserves the code** if you ever want to resurrect the concept.

---

## Action

```bash
# Delete the experimental scripts
rm scripts/build_strongs_references.py
rm scripts/test_matthew5_strongs.py
rm scripts/test_strongs_references.py
```

After deletion, `scripts/` directory will be empty (create new scripts as needed per use case).

---

## Alternative: Archive Instead of Delete

If you want to keep them for reference:

```bash
mkdir -p plan/archive/experiments
mv scripts/*.py plan/archive/experiments/
```

This preserves them without cluttering the active codebase.

