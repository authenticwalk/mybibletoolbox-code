# Experiments Directory - Organization Note

**Date:** 2025-11-15
**Status:** Planning examples only, no actual experiments run

---

## Current Situation

**Location:** `/plan/strongs-cultural-translation/experiments/`

**Contents:**
- `pilot-samples.md` (1011 lines) - 3 planning examples (G26, H7950, G721)

**Nature:** These are **planning examples** demonstrating the output schema, NOT actual experiment runs against a test set.

---

## Clarification

The file `pilot-samples.md` contains:
- Comprehensive planning examples
- Schema validation
- Methodology demonstration
- Output format examples

**NOT actual experiments because:**
- No test set exists (Stage 1.3 requirement)
- No multiple approaches tested (Stage 1.4 requirement)
- No review committee evaluation (Stage 2.3 requirement)
- No validation metrics collected (Stage 2.4 requirement)
- No cross-approach comparison (Stage 2.5 requirement)

---

## Recommended Organization

### Current (Planning Phase):
```
/plan/strongs-cultural-translation/
├── README.md (planning overview)
├── research/
│   └── challenges.md (834 lines - methodology design)
└── experiments/
    └── pilot-samples.md (1011 lines - planning examples)
```

**Action:** Rename `pilot-samples.md` → `planning-examples.md` for clarity

### Future (When Experiments Begin):
```
/bible-study-tools/strongs-extended/tools/cultural-translation/
├── TEST-SET.md (30-50 words, stratified)
├── APPROACHES.md (3 approaches with hypotheses)
├── experiments/
│   ├── planning-examples/ (from /plan)
│   │   ├── G26-agape-example.yaml
│   │   ├── H7950-snow-example.yaml
│   │   └── G721-lamb-example.yaml
│   ├── round-1/
│   │   ├── approach-a/ (corpus-based)
│   │   ├── approach-b/ (case-study)
│   │   └── approach-c/ (anthropological)
│   ├── round-2/ (refinement)
│   ├── round-3/ (context engineering)
│   └── results-summary.md
└── docs/
    ├── README.md
    └── METRICS.md
```

---

## Migration Plan

**When experimentation begins (Phase 2):**

1. **Create experiments/ directory** in tool location
2. **Copy planning examples** from /plan to experiments/planning-examples/
3. **Create round-1/ structure** with 3 approach subdirectories
4. **Execute actual experiments** (9-15 runs)
5. **Keep /plan directory** for historical reference

**Rationale:**
- Planning examples valuable for schema reference
- Actual experiments belong in tool directory
- Clear separation: planning vs. execution

---

## Current Action: None Required

**Reason:** No actual experiments have been run yet

**Next Step:** Complete Stage 1 (TEST-SET.md + APPROACHES.md) before creating experiment structure

**See:** ACTION-PLAN.md for full execution roadmap

---

**Report Generated:** 2025-11-15
