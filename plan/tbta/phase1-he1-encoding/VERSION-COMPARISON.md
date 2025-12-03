# Subagent Skill Version Comparison

Three versions of the subagent skill, each with a different approach to deriving rules.

## Summary

| Version | Approach | Rules Source | File |
|---------|----------|--------------|------|
| **V1** | Policy-first | Official TBTA checklist.md | `SUBAGENT-SKILL.md` |
| **V2** | Reverse-engineering | Pattern analysis of 6,963 encoded verses | `SUBAGENT-SKILL-V2.md` |
| **V3** | Blended | Policy + reverse-engineering with evidence | `SUBAGENT-SKILL-V3.md` |

---

## V1: Policy-First

**Source**: `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL.md`

**Philosophy**: Follow the official TBTA documentation exactly as written.

**Rules derived from**:
- `checklist.md` - Official TBTA encoding checklist
- `notation.md` - TBTA notation guide
- Direct interpretation of policy documents

**Strengths**:
- Faithful to official documentation
- Clear policy citations (§ references)
- Predictable behavior

**Weaknesses**:
- Some policies not consistently applied in actual encoded verses
- May conflict with patterns found in real data
- Doesn't account for undocumented conventions

**Process**: 5-step transformation + checklist pass

---

## V2: Reverse-Engineering

**Source**: `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL-V2.md`

**Philosophy**: Derive rules from patterns observed in actual encoded verses.

**Rules derived from**:
- Analysis of 6,963 verses across 15 books
- Pattern extraction from `semantic_encoding` and `phase_1_encoding` columns
- Statistical consistency analysis (⭐ ratings)

**Strengths**:
- Evidence-based with verse references
- Confidence levels (🟢🟡🔴) based on actual consistency
- Documents exceptions and edge cases

**Weaknesses**:
- May capture encoding errors as "patterns"
- Some rules inconsistent because original encoding was inconsistent
- Missing policy rationale

**Process**: 10-step transformation with rules file reference

---

## V3: Blended (Policy + Evidence)

**Source**: `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL-V3.md`

**Philosophy**: Combine official policy with evidence from encoded verses, using each to validate and clarify the other.

**Rules derived from**:
- Official TBTA policy (📘 markers)
- Reverse-engineered patterns (🟢🟡🔴 confidence)
- Reconciliation of conflicts between policy and practice

**Key reconciliations**:

| Topic | Policy Says | Data Shows | V3 Resolution |
|-------|-------------|------------|---------------|
| Passive voice | Keep passive | Passives kept | ✅ Aligned - mark agent with "by" |
| Numbers | Use digits | Mixed rendering | Semantic layer correct; text varies |
| "can" | Use "is able" | 14% converted | 📘 Follow policy despite low adoption |
| Aspect verbs | No bracket | Consistently followed | 📘 Policy confirmed by data |

**Strengths**:
- Best of both worlds
- Policy rules validated by evidence where possible
- Clear distinction between policy (📘) and empirical (🟢🟡🔴)
- Corrections to previous misunderstandings

**Weaknesses**:
- More complex to understand
- Requires reading larger rules file

**Process**: 10-step transformation with blended rules

---

## When to Use Each

| Scenario | Recommended |
|----------|-------------|
| Quick encoding, simple verse | V1 |
| Need evidence for decisions | V2 |
| Production encoding, accuracy critical | V3 |
| Debugging encoding issues | V3 (check policy vs evidence) |
| Training new encoders | V1 (start simple) → V3 (advanced) |

---

## File Locations

```
bible-study-tools/tbta/phase1/policies/
├── SUBAGENT-SKILL.md      # V1 - Policy-first (reads checklist.md)
├── SUBAGENT-SKILL-V2.md   # V2 - Reverse-engineering (rules embedded)
├── SUBAGENT-SKILL-V3.md   # V3 - Blended (rules embedded)
└── learnings.md           # Shared by all versions

plan/tbta/phase1-he1-encoding/
├── RULES.md               # Reference copy of blended rules
├── SKILL.md               # Orchestrator reference
└── ORCHESTRATOR.md        # Parallel subagent workflow
```

**Note**: V2 and V3 have rules fully embedded in the skill file itself. No external file reads needed (except learnings.md).

---

## Evolution

```
V1 (Policy)          V2 (Evidence)
     │                    │
     │  "What does        │  "What do the
     │   policy say?"     │   verses show?"
     │                    │
     └────────┬───────────┘
              │
              ▼
         V3 (Blended)
              │
     "Policy + evidence,
      reconciled where
      they conflict"
```
