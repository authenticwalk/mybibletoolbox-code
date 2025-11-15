# Template Usage Guide

**Purpose:** Guide for using the minimal Tool 3 templates
**Status:** Production-ready
**Last Updated:** 2025-11-12

---

## Quick Start

1. **Choose Template:**
   - `error-correction.yaml` - For correcting common errors/fallacies
   - `multi-perspective.yaml` - For scholarly disagreements or cultural/translation debates
   - `skip-decision.yaml` - For documenting why a word is excluded from Tool 3

2. **Review Example:**
   - `examples/G1411-error-correction-EXAMPLE.yaml` - Error correction (dynamite fallacy)
   - `examples/G1577-multi-perspective-EXAMPLE.yaml` - Multi-perspective (church vs assembly)
   - `examples/G1161-skip-decision-EXAMPLE.yaml` - Skip decision (grammatical particle)

3. **Copy Template:**
   - Copy minimal template to your working directory
   - Fill in placeholders with real data
   - Validate against quality-checklist.md

4. **See Experiments for Detailed Examples:**
   - experiments/exp4-error-correction/ - Detailed error correction process
   - experiments/exp5-cultural-debate/ - Detailed multi-perspective process
   - experiments/exp3-scope-boundary/ - Detailed skip decision process

---

## Templates Overview

### error-correction.yaml (88 lines)

**When to Use:** Word has a common error or fallacy that needs correction

**5-Part Structure:**
1. Error Statement - Clear, non-mocking statement of the error
2. Classification - Name the fallacy type (etymological, totality transfer, etc.)
3. Multi-Layered Refutation - Minimum 4 evidence types (linguistic, diachronic, contextual, scholarly consensus)
4. Expert Validation - Authority pyramid (VERY HIGH → HIGH → MEDIUM), minimum 2 sources, at least 1 HIGH+
5. Correct Alternative - Principle + Methodology + Better Analogy + Biblical Usage

**Key Requirements:**
- Minimum 2 sources (MEDIUM-HIGH or higher)
- At least 1 HIGH or VERY HIGH authority
- Gracious, pedagogical tone (not mocking)
- 4+ evidence types in refutation

**Example:** See `examples/G1411-error-correction-EXAMPLE.yaml` (dynamis/dynamite fallacy)

**Validated On:** G1411 dynamis, G5485 charis, G4396 prophetes (3/3 pass)

---

### multi-perspective.yaml (101 lines)

**When to Use:** Word has scholarly disagreement, translation debate, or cultural sensitivity

**Key Components:**
- Positions - Minimum 2 major positions with advocates, arguments, strengths, considerations
- Cultural Considerations - Post-colonial, denominational, contemporary movement factors (if applicable)
- Translator Guidance - Decision framework (options, NOT mandates)
- Bias Detection - Reversal, Respect, Evidence tests (all must pass)

**Key Requirements:**
- Minimum 2 positions documented
- Each position has credentialed advocates
- Fair representation (bias tests passed)
- Guidance as options, not commands

**Example:** See `examples/G1577-multi-perspective-EXAMPLE.yaml` (ekklesia church/assembly debate)

**Validated On:** G4151 pneuma, G1577 ekklesia, G4983 soma, H2617 hesed, G4396 prophetes (5/5 pass)

---

### skip-decision.yaml (92 lines)

**When to Use:** Word should be excluded from Tool 3 (grammatical particle, function word, insufficient coverage, Tool 1 sufficient)

**Key Components:**
- Skip Reason - grammatical_particle | function_word | insufficient_coverage | tool_1_sufficient
- Skip Rationale - Detailed explanation
- Search Documentation - Prove exhaustive search (minimum 5 queries if insufficient_coverage)
- Scope Boundary Analysis - Tool 1 vs Tool 3 territory

**Key Requirements:**
- Clear skip reason with detailed rationale
- Exhaustive search documented (if insufficient_coverage)
- Scope boundaries explained
- Skip recognized as success (not failure)

**Example:** See `examples/G1161-skip-decision-EXAMPLE.yaml` (de particle)

**Validated On:** G1161 de, G235 alla, G1 alpha (3/3 pass)

---

## Detailed Guidance (OLD Templates)

For extensive guidance with detailed instructions and researcher notes, see the OLD template files:

- `error-correction-template-OLD.yaml` - 170 lines with comprehensive guidance
- `multi-perspective-template-OLD.yaml` - 269 lines with comprehensive guidance
- `skip-decision-template-OLD.yaml` - 244 lines with comprehensive guidance

**Note:** These OLD templates contain the same structure as minimal templates but with extensive inline comments and researcher notes. Use them as reference when you need detailed instructions.

---

## Validation

All outputs must pass quality-checklist.md:

**Level 1 (CRITICAL - 100%):**
- Verifiable credentials
- No fabrication
- Inline citations
- Authority marked
- 5-part error complete (if applicable)
- Scope boundaries respected

**Level 2 (HIGH - 80%+, 7 of 9):**
- Expert-based insights
- 5-part structure complete
- Gracious tone
- Multi-perspective fairness
- Bias tests passed

**Level 3 (MEDIUM - 60%+, 5 of 8):**
- Full documentation
- Discipline-specific noted
- Cultural sensitivity
- Scope clarity

---

## Common Pitfalls

1. ❌ **Using harsh tone in error corrections** → Use gracious, pedagogical tone
2. ❌ **Biased multi-perspective** → Run all 3 bias tests (Reversal, Respect, Evidence)
3. ❌ **Skipping without documentation** → Document search effort and rationale
4. ❌ **Insufficient authority for errors** → Need minimum 2 sources, 1 HIGH+
5. ❌ **Missing evidence types** → Need minimum 4 in error refutations

---

## Extended Validation

See `experiments/EXTENDED-VALIDATION-7-WORDS.md` for documentation of 7 additional adversarial test cases validating all templates across:

- Multiple fallacy types (etymological, totality transfer)
- Multiple controversy types (translation, theological, cultural)
- Multiple scope boundaries (particles, conjunctions, letters)
- Both Greek and Hebrew words
- Combined features (multiple templates on one word)

**Result:** 12/12 total adversarial tests passed (5 original experiments + 7 extended validation)

---

## Quick Reference

**Template Selection Decision Tree:**

```
Does word have a common error/fallacy?
├─ YES → Use error-correction.yaml
└─ NO ↓

Does word have scholarly disagreement/cultural debate?
├─ YES → Use multi-perspective.yaml
└─ NO ↓

Is word outside Tool 3 scope (particle, function word, etc.)?
├─ YES → Use skip-decision.yaml
└─ NO → Use standard schema.yaml (modern_insights + practical_applications)
```

**When to Combine Templates:**
- Word can have both error correction AND multi-perspective (e.g., G4396 prophetes)
- Use both templates, include both in final YAML output

---

**For Full Workflow:** See `workflow/README.md` (when created) or `RESEARCHER-WORKFLOW.md` (current comprehensive guide)
