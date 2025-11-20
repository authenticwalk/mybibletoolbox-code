# Outstanding TODOs from TBTA Migration

**Purpose**: Track unresolved TODOs extracted from TBTA files during cleanup to make them look like final documentation rather than work-in-progress.

**Date Extracted**: 2025-11-14

---

## From features/STAGES.md

### Stage 4: Generate a Proper Test Set

**Line 37**: Script Integration for Data Extraction
- TODO: In initial notes, mentioned need to call a script for data extraction
- Requirement: LLM should NOT do data extraction work
- LLM should: Select verses and assign to train/test/validate based on adversarial criteria
- Script should: Handle actual data extraction from TBTA repository

**Line 65**: Missing Script Name
- TODO: Script name for getting verses was removed, need to restore it
- Context: External validation preparation section
- Action: Document the existing script name/path for verse extraction

**Lines 100-109**: LLM vs Script Role Clarity
- TODO: Clarify which tasks are LLM vs script responsibilities
- Current confusion: Some values like languages, families, difficulty, notes must be done by LLM not script
- Need: Clear delineation of roles
  - Script: Data extraction, filtering, counting
  - LLM: Verse selection, adversarial identification, linguistic analysis

### Stage 5: Test Hypothesis

**Line ~200+**: State Values Documentation Missing
- TODO: Lost notes on what "state values" are
- TODO: Lost explanation of "dominant", "secondary", "linguistic rationale" and why they matter
- Action: Go back in git history to recover these notes and improve documentation

### Stage 6: Validation

**Theological Soundness Over-emphasis**
- TODO: Section overly focused on theological soundness (may not be transferable)
- Better focus: How translators may accidentally create theological issues
- Reframe: Preventative guidance rather than correctness validation

**Validation Summary Length**
- TODO: Validation summary section is too long
- Should be: Shorter form that is humanly manageable
- Only include: Details when there is confusion

**AI Transparency**
- TODO: Need to be transparent this is AI roleplay
- Add: AI model and version number to avoid confusing future readers
- Example: "This validation was performed using Claude Sonnet 4.5 (2025-09-29)"

---

## From learnings/README.md

### Prompt Engineering Pattern: Default Value Handling

**Line ~105+**: Clarification on "Read TBTA Files"
- TODO: Ambiguous statement "do you mean read the tbta files for the answer"
- Concern: That would be cheating and won't work for books TBTA hasn't annotated yet
- Alternative interpretation: Certain words are always certain values (lexical lookup)
- Need: Clarify whether this is about:
  - Lexical defaults (e.g., "οὐ" is always negative)
  - Contextual inference without peeking at answers
  - Or something else entirely

### Theological Cautions

**Line ~150+**: Isogesis Warning Missing
- TODO: Add caution and need for footnote
- Issue: If theological concept is NOT in source language and we're adding it
- Requirement: Must be clear it was not in the source
- Risk: Eisogesis (reading meaning into text rather than extracting from it)
- Solution: Metadata flag when theological interpretation goes beyond source morphology

---

## Migration Priority

**HIGH PRIORITY** (Blocks feature development):
1. ✅ Document script name/path for verse extraction - COMPLETE (see HIGH-PRIORITY-TODO-SOLUTIONS.md)
2. ✅ Clarify LLM vs script role separation - COMPLETE (documented in STAGES.md)
3. ✅ Restore "state values" documentation from git history - COMPLETE (accuracy targets table added to STAGES.md)

**MEDIUM PRIORITY** (Improves quality):
4. Add AI transparency disclaimers with model versions
5. Reframe theological validation to be preventative
6. Clarify default value lookup strategy

**LOW PRIORITY** (Documentation polish):
7. Shorten validation summary guidelines
8. Add eisogesis warning with metadata solution

---

## Actions Taken

- [x] Extracted all TODOs from features/STAGES.md
- [x] Extracted all TODOs from learnings/README.md
- [x] Removed TODOs from languages/README.md (migration plan removed entirely)
- [x] Created this tracking document in /plan/tbta-migration/

## Next Steps

1. Clean up all [TODO] markers from TBTA files
2. Remove all migration-related checkboxes from STAGES.md and other files
3. Make TBTA directory look like final reference documentation
4. Keep this file in /plan for future resolution

---

**Last Updated**: 2025-11-14
