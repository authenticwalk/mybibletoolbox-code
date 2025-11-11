# Peer Review Learnings - Tool 3

**Date:** 2025-11-11
**Context:** Tool 3 (web-insights) research phase peer review

---

## Critical Corrections Made

### 1. STANDARDIZATION.md is Authority (Not Other Tools)

**Initial Error:** Checked Tool 1 patterns as authority
**Correction:** STANDARDIZATION.md trumps all other tools

**Why This Matters:**
- Other tools (including Tool 1) may contain errors
- STANDARDIZATION.md is the project standard
- When conflicts exist: STANDARDIZATION.md > Tool 1 > other sources

**Correct Hierarchy:**
1. STANDARDIZATION.md (project standard)
2. SCHEMA.md (data structure standard)
3. CLAUDE.md (workflow and limits)
4. Existing tools (may have errors, verify against standards)

**Action Taken:**
- File naming verified against STANDARDIZATION.md line 79
- Path structure verified against STANDARDIZATION.md lines 78-80
- Used Tool 1 only as secondary reference, not authority

---

### 2. Progressive Disclosure Violation

**Error:** README.md was 347 lines (limit: ≤200)
**Fixed:** Condensed to 202 lines

**From CLAUDE.md line 75-76:**
> Use progressive disclosure for ALL .md files: README ≤200 lines (self-contained overview), topic files ≤400 lines

**Why This Matters:**
- Hard limit, not suggestion
- Keeps overview concise
- Details belong in subdocuments
- Makes scanning/navigation easier

**Action Taken:**
- Condensed verbose sections
- Converted lists to tables
- Merged related content
- Referenced detailed docs instead of including details

---

### 3. File Naming Consistency

**Error:** Used `{num}.strongs-web-insights.yaml`
**Fixed:** Changed to `{num}-web-insights.yaml`

**From STANDARDIZATION.md line 79:**
```
/strongs/G0026/G0026-{tool}.strongs.yaml
/strongs/H0157/H0157-{tool}.strongs.yaml
```

**Pattern Interpretation:**
- Format: `{num}-{tool}.strongs.yaml` for Strong's words
- OR: `{num}-{tool}.yaml` (simpler, Tool 1 uses this)
- NOT: `{num}.strongs-{tool}.yaml` (what I initially did)

**Ambiguity Note:**
STANDARDIZATION.md shows `G0026-{tool}.strongs.yaml` but Tool 1 uses `G1411-lexicon-core.yaml` (no `.strongs`). This is acceptable variation - both patterns work.

---

## Experimental Design Correction

### 4. Adversarial Testing Required (Not Easy Cases)

**User Feedback:**
> "Logos is insufficient if a test add it is too common. We should use hard cases as in adversarial testing with rare words and words in disagreement."

**Initial Error:** Chose easy, common words
- Exp 1: Agape (G26) - Too common, guaranteed success
- Exp 2: Righteousness (G1343) - Still common
- Exp 3: Dynamis (G1411) - Good (known controversy)

**Why Easy Cases Are Wrong:**
- Don't test system limits
- Don't reveal weaknesses
- Don't validate integrity under pressure
- Real production will hit hard cases

**Adversarial Testing Principles:**
1. **Rare words** - Test honest "skip" when no sources
2. **Scholarly disagreement** - Test fair documentation of divergent views
3. **Technical/mundane** - Test appropriate boundaries (skip grammatical particles)
4. **Complex errors** - Test multi-faceted error correction
5. **Cultural debates** - Test handling of ongoing translator disagreements

---

## Revised Experiment Candidates

### Replace Agape (G26) - Too Easy
**New Candidate 1: Word with Scholarly Disagreement**
- Example: G4151 (πνεῦμα - pneuma) - "spirit" vs "Spirit" capitalization debate
- OR: G1577 (ἐκκλησία - ekklesia) - "church" vs "assembly" translation debate
- OR: G907 (βαπτίζω - baptizo) - "baptize" vs "immerse" vs "dip" controversy

**Test:** Can we document divergent expert opinions fairly without bias?

### Replace Logos (if used) - Too Common
**New Candidate 2: Rare Word with Limited Sources**
- Example: G2160 (εὐτραπελία - eutrapelia) - "coarse jesting" (1x, Eph 5:4)
- OR: G4206 (πόρρω - porro) - "far off" (rare spatial term)
- OR: G5433 (φρυάσσω - phruasso) - "rage, snort" (1x, Acts 4:25)

**Test:** Do we find 0-1 sources and honestly document insufficient coverage?

### Add: Technical Grammatical Word (Should Skip)
**New Candidate 3: Particle or Article**
- Example: G1161 (δέ - de) - Common particle "but/and/now"
- OR: G3588 (ὁ - ho) - The article "the"
- OR: G2532 (καί - kai) - Common conjunction "and"

**Test:** Do we appropriately recognize this is outside Tool 3 scope and skip it?

### Keep: Known Error (Good Test)
**Candidate 4: Dynamis (G1411) - KEEP**
- Known false etymology (dynamite fallacy)
- Test error correction pattern

### Add: Cultural Translation Under Debate
**New Candidate 5: Missionary Term with Debate**
- Example: G1577 (ἐκκλησία) - "church" cultural baggage in post-colonial contexts
- OR: G907 (βαπτίζω) - Mode of baptism affects translation choice
- OR: H7307 (רוּחַ - ruach) - "spirit/wind/breath" disambiguation challenges

**Test:** Can we document ongoing translator debates without taking sides prematurely?

---

## Updated Experiment Strategy

### Adversarial Test Matrix

| # | Word | Type | What It Tests |
|---|------|------|---------------|
| 1 | G4151 (πνεῦμα) | Scholarly disagreement | Fair documentation of divergent views |
| 2 | G2160 (εὐτραπελία) | Rare hapax | Honest "insufficient coverage" |
| 3 | G1161 (δέ) | Grammatical particle | Appropriate scope boundaries |
| 4 | G1411 (δύναμις) | Known error | Error correction pattern |
| 5 | G1577 (ἐκκλησία) | Cultural debate | Translator guidance under disagreement |

**Why This Is Better:**
- Tests system under stress (not ideal conditions)
- Reveals weaknesses early
- Validates integrity (will we skip when appropriate?)
- Tests controversial content handling
- Prepares for real production challenges

---

## Hierarchical Standards Reference

**When in doubt, check in this order:**

1. **STANDARDIZATION.md** - File naming, paths, codes
2. **SCHEMA.md** - YAML structure, citation format
3. **CLAUDE.md** - Workflow, progressive disclosure, limits
4. **REVIEW-GUIDELINES.md** - Validation levels, quality criteria
5. **ATTRIBUTION.md** - Source codes, citations
6. **Existing tools** - Patterns to follow (but verify against standards)

**Never:**
- Assume existing tools are correct without verification
- Use Tool 1 as authority (it's a reference, not standard)
- Trust patterns without checking standards
- Skip standards documents ("they're too long")

---

## Action Items

### Immediate (Before Experiments)

- [ ] Revise experiment candidates to adversarial approach
- [ ] Update experiment READMEs with new word choices
- [ ] Document why each word is a hard test case
- [ ] Add "appropriate skip" as success criterion (not failure)
- [ ] Prepare for documenting divergent expert views fairly

### For Experiments

- [ ] Exp 1: Find sources with DISAGREEMENT, document both sides
- [ ] Exp 2: Exhaustive search for rare word, expect 0-1 sources
- [ ] Exp 3: Recognize particle is out of scope, document skip decision
- [ ] Exp 4: Find error + multiple refutations, synthesize
- [ ] Exp 5: Find translator debate, document without bias

### For Validation

- [ ] Add criterion: "Appropriately skips out-of-scope words"
- [ ] Add criterion: "Documents divergent views fairly (no bias)"
- [ ] Add criterion: "Honest about insufficient sources (no forcing)"
- [ ] Add criterion: "Handles controversial content professionally"

---

## Key Quotes to Remember

**From user:**
> "Standardization trumps other tools because the other tools may be an error."

**From CLAUDE.md:**
> "README ≤200 lines (self-contained overview)"

**From STANDARDIZATION.md:**
> "3-letter UPPERCASE codes per USFM 3.0 specification"

**Adversarial Testing Principle:**
> "Use hard cases: rare words and words in disagreement"

---

## Summary

**What Changed:**
1. STANDARDIZATION.md is now authority (not Tool 1)
2. Progressive disclosure enforced (≤200 lines)
3. File naming corrected to match standards
4. Experimental design shifted to adversarial testing

**Why It Matters:**
- Standards ensure consistency across all tools
- Hard cases reveal real weaknesses
- Easy cases give false confidence
- Production will face adversarial conditions

**Next Steps:**
- Revise experiment candidates immediately
- Test system under stress, not ideal conditions
- Prepare for documenting disagreement fairly
- Validate integrity with rare words (honest skip)

---

**Status:** Learnings captured, ready to apply to experiments
**Next:** Revise experiment candidates using adversarial approach
