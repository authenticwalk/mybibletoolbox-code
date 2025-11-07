# Language Families Restructuring Plan

## Objective

Convert language family documentation to progressive disclosure format with full fact-checking and source verification.

## Current State

| File | Lines | Status | Action Needed |
|------|-------|--------|---------------|
| README.md | 189 | ✓ | Minor updates for new structure |
| austronesian.md | 1208 | ✗ | Convert to directory (>400 lines) |
| indo-european.md | 1013 | ✗ | Convert to directory |
| niger-congo.md | 913 | ✗ | Convert to directory |
| trans-new-guinea.md | 1008 | ✗ | Convert to directory |
| other-families.md | 1489 | ✗ | Convert to directory |
| mayan.md | 398 | ⚠ | Fact-check + verify sources |
| otomanguean.md | 324 | ⚠ | Fact-check + verify sources |

## Progressive Disclosure Requirements

1. **README.md**: ≤200 lines, self-contained overview
2. **Topic directories**: When content >400 lines
3. **All claims**: Must have inline sources OR be common knowledge
4. **Source verification**: Open cited sources, verify they support claims and are authoritative
5. **Unsourced claims**: Remove if no supporting source can be found

## Work Breakdown

### Phase 1: Restructure Large Files (Parallel)

Each large file needs:
1. Create directory: `{family}/`
2. Create `{family}/README.md` (≤200 lines) - overview + key findings
3. Split content into logical topic files (≤400 lines each)
4. Extract all sources to verify

**Files to restructure:**
- [ ] austronesian.md → austronesian/
- [ ] indo-european.md → indo-european/
- [ ] niger-congo.md → niger-congo/
- [ ] trans-new-guinea.md → trans-new-guinea/
- [ ] other-families.md → other-families/

### Phase 2: Fact-Check Files (Parallel)

For each file/directory:
1. Extract all factual claims
2. Identify which claims need sources (not common knowledge)
3. For existing sources:
   - Verify source is authoritative
   - Verify claim is accurately represented
4. For missing sources:
   - Search for authoritative source
   - If found: add inline citation
   - If not found: **remove claim as noise**

### Phase 3: Update Structure

- [ ] Update families/README.md with new directory links
- [ ] Ensure all files follow progressive disclosure format
- [ ] Commit changes with clear message

## Parallel Execution Strategy

Launch 6 subagents in parallel to handle restructuring and fact-checking simultaneously:
1. Agent 1: Austronesian restructure + fact-check
2. Agent 2: Indo-European restructure + fact-check
3. Agent 3: Niger-Congo restructure + fact-check
4. Agent 4: Trans-New Guinea restructure + fact-check
5. Agent 5: Other-families restructure + fact-check
6. Agent 6: Mayan + Otomanguean fact-check only

## Source Verification Criteria

**Authoritative sources:**
- ✓ Academic publishers (Oxford, Cambridge, MIT Press, etc.)
- ✓ Peer-reviewed journals (*Language*, *Linguistic Typology*, etc.)
- ✓ University dissertations
- ✓ SIL International, Ethnologue (for language classification/demographics)
- ✓ WALS (World Atlas of Language Structures)

**Non-authoritative sources:**
- ✗ Wikipedia (can use as starting point to find primary sources)
- ✗ Personal blogs without citations
- ✗ Unverified websites

## Progress Tracking

- **Started**: 2025-11-07
- **Estimated completion**: This session (parallel execution)
- **Files processed**: 0/8
- **Sources verified**: 0
