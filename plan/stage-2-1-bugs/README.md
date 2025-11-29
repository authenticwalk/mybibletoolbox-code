# Stage 2.1 Bug Analysis

**Date**: 2025-11-28
**Context**: Running Stage 2.1 for number-systems and mood features

## Bugs Found

### Bug 1: Subagent Created Script Instead of Manual LLM Work

**Severity**: HIGH
**Location**: STAGE-2-1-ANALYSIS-DATASET.md Step 1B

**Problem**: Instructions say "This is an LLM task" but subagent wrote `enrich_dataset.py` script instead of manually enriching entries.

**Evidence**:
- Created `/workspace/bible-study-tools/tbta/features/mood/analysis/enrich_dataset.py`
- All `strongs_number` fields are empty

**Root Cause**: Ambiguous instruction phrasing. "LLM task" was meant to say "you the LLM should do this manually" but was interpreted as "create automation".

**Fix**:
```markdown
# Change from:
**This is an LLM task** - requires judgment about theological/literary diversity.

# To:
**MANUAL LLM WORK** - Do NOT write a script. YOU must manually edit each entry
using Write/Edit tools to add strongs_number and reason_group based on your judgment.
```

---

### Bug 2: `strongs` Field Not Added When Empty

**Severity**: MEDIUM
**Location**: `extract_feature.py` lines 491-496

**Problem**: When macula lookup returns empty string, the `strongs` field is not added to output at all.

**Code**:
```python
# Current (line 495-496):
if with_strongs and strongs_codes:
    result['strongs'] = strongs_codes
```

**Expected**: Field should be added even when empty so downstream knows extraction was attempted.

**Fix**:
```python
# Always add strongs field if requested, even if empty
if with_strongs:
    result['strongs'] = strongs_codes or ""
```

---

### Bug 3: Translation Codes Don't Match Reality

**Severity**: HIGH
**Location**: STAGE-2-1-ANALYSIS-DATASET.md Step 1C

**Problem**: Instructions list translation codes that don't match available data.

| Instruction Says | Actual OT Code | Actual NT Code |
|------------------|----------------|----------------|
| grc-BYZ | grc-BRENT | grc-BYZ ✓ |
| jpn-1965 | (not found) | (not found) |
| lat-VUC | lat-VUC ✓ | lat-VUC ✓ |
| heb-heb | heb-heb ✓ | (Hebrew not in NT) |

**Root Cause**: Instructions written without verifying actual code availability.

**Fix**:
1. Change Step 1Ci to require running `fetch_verse.py` to discover available codes BEFORE enrichment
2. Update default code list or note that OT/NT have different codes
3. Add note: "Use codes exactly as shown in fetch_verse.py output"

---

### Bug 4: Cache Miss When File Exists

**Severity**: MEDIUM
**Location**: `enrich_extract_with_verses.py` / `cache.py`

**Problem**: Subagent reported "Cache miss" but files exist on disk.

**Investigation**:
```bash
# File exists:
/workspace/.data/commentary/EXO/020/013/EXO-020-013-translations-ebible.yaml

# Path construction is correct (verified)
```

**Possible Causes**:
1. Translation code filter in `filter_translations_by_codes()` returns empty dict
2. Script was called with codes like `eng-YLT` but file has slightly different key

**Fix**: Add debug logging to show:
- Requested codes
- Available codes in file
- Which codes matched

---

### Bug 5: Instructions Don't Match Script Capabilities

**Severity**: LOW
**Location**: STAGE-2-1-ANALYSIS-DATASET.md

**Problem**: Instructions reference translation codes format without clarifying ebible vs biblehub differences.

**Evidence**: eBible has codes like `eng-YLT`, `spa-BLM` while biblehub might have different formats.

**Fix**: Clarify in instructions that codes must come from `translations-ebible.yaml` files in `.data/commentary/`.

---

## Proposed Instruction Changes

### Step 1B: Clarify Manual Work

**Before**:
```markdown
**This is an LLM task** - requires judgment about theological/literary diversity.
```

**After**:
```markdown
**MANUAL LLM WORK REQUIRED** - Do NOT write automation scripts for this step.

For EACH entry in the draft dataset:
1. Open the entry in your context
2. Look at the `strongs` field (e.g., "H0430-God H1254-created H0853-the H8064-heavens")
3. Find the code matching `constituent` (e.g., constituent="God" → strongs_number="H0430")
4. Assign `reason_group` based on THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml
5. Write the modified entry back

Example:
- Entry has: constituent="us", strongs="H0430-God H0559-said H6213-let_us H0120-man"
- Match "us" to "let_us" → strongs_number = "H6213"
- Genesis 1:26 is Trinity context → reason_group = "TRINITY"
```

### Step 1Ci: Verify Codes Before Use

**Before**:
```markdown
Use `src/tools/fetch_verse.py` to get 2 verses (1 OT, 1 NT)
```

**After**:
```markdown
Use `src/tools/fetch_verse.py` to discover EXACT translation codes available:

```bash
python src/tools/fetch_verse.py GEN.001.026 2>&1 | head -100
```

Copy the EXACT codes from output (e.g., "eng-YLT", "arb-NAV", "grc-BRENT")
Note: OT uses grc-BRENT (Septuagint), NT uses grc-BYZ (Byzantine)
```

---

## Action Items

1. [ ] Update STAGE-2-1-ANALYSIS-DATASET.md with clearer instructions
2. [ ] Fix `extract_feature.py` to always add strongs field
3. [ ] Add debug output to `enrich_extract_with_verses.py`
4. [ ] Re-run Stage 2.1 for both features with corrected instructions
5. [ ] Validate that strongs_number is populated correctly
