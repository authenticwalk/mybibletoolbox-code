# TBTA Phase 1 (He1) — Orchestrator Skill

> **Mission**: Run parallel subagents to encode NIV verses to He1, select best result, debug failures.

## Input Handling

**Accepts**: Text file or direct input with verse reference(s), optionally with text.

### Validation

**Required**: Verse reference — any format: `Ruth 4:1`, `RUT 4:1`, `Ruth 4:1-5`, `Matthew 2:1-10`
**Optional**: Verse text — if not provided, will be fetched

| Input | Action |
|-------|--------|
| Reference + text | Use provided text |
| Reference only | Fetch text from sources |
| No reference | Return error (see below) |

**If no verse reference found** → Return error:
```
ERROR: Input must contain a verse reference.
Expected format: "{Book} {ch}:{vs}" (e.g., Ruth 4:1, Matthew 2:1-10)
```

### Input Examples

```
# Reference + text (uses provided text)
Ruth 4:1  Boaz went up to the town gate and sat down there...

# Reference only (will fetch text)
Matthew 2:1-10

# Multiple verses with text
Matthew 2:1-3
v1: After Jesus was born in Bethlehem...
v2: and asked, "Where is the one..."
v3: When King Herod heard this...

# Minimal format
GEN 1:1
```

---

## Workflow

```
INPUT: Verse reference (text optional, fetched if missing)
    │
    ├──► Subagent V1 (Policy)
    ├──► Subagent V2 (Evidence)
    └──► Subagent V3 (Blended)
           │
           ▼
    FETCH REFERENCE (sources.tabitha.bible)
           │
           ▼
    COMPARE & SELECT (5 criteria)
           │
           ▼
    DEBUG FAILURES (analyze what went wrong)
           │
           ▼
    UPDATE LEARNINGS (wrong version's learnings-{v}.md)
```

## Process

1. **Get NIV** → Validate input OR fetch verse
   - If input provided: validate has reference + text (see Input Handling)
   - Single verse fetch: `src/tools/fetch_verse.py`
   - Chapter fetch: `https://www.biblestudytools.com/{book}/{chapter}.html`
2. **Launch subagents** → Run V1, V2, V3 in parallel with NIV text
3. **Collect results** → Each returns: He1 encoding (linter-validated) + issues
4. **Fetch reference** → `curl -H "Accept: application/json" "https://sources.tabitha.bible/Bible/{Book}/{ch}/{vs}"`
5. **Compare & select** → Apply selection criteria (see below)
6. **Debug failures** → Analyze what went wrong, update learnings

---

## Subagent Prompts

### V1 (Policy-First)
```
Read: ./SUBAGENT-SKILL.md (rules + learnings-v1.md)
Input: "{niv_text}"
Return: He1 encoding (linter-validated), issues
NOTE: Run linter until clean (max 12 iterations) BEFORE returning
```

### V2 (Evidence-Based)
```
Read: ./SUBAGENT-SKILL-V2.md (rules + learnings-v2.md)
Input: "{niv_text}"
Return: He1 encoding (linter-validated), issues
NOTE: Run linter until clean (max 12 iterations) BEFORE returning
```

### V3 (Blended)
```
Read: ./SUBAGENT-SKILL-V3.md (rules + learnings-v3.md)
Input: "{niv_text}"
Return: He1 encoding (linter-validated), issues
NOTE: Run linter until clean (max 12 iterations) BEFORE returning
```

---

## Selection Criteria

| Priority | Criterion | How to Check |
|----------|-----------|--------------|
| **1** | **Match reference `phase_1_encoding`** | Compare against Sources API (see below) |
| 2 | Linter passes | Zero blocking errors |
| 3 | Rule compliance | Matches HIGH confidence rules |
| 4 | Pronoun resolution | All 3rd person → nouns |
| 5 | Bracket correctness | Subordinate clauses bracketed |

### Comparing Against Reference

**Get reference encoding:**
```bash
curl -H "Accept: application/json" "https://sources.tabitha.bible/Bible/{Book}/{ch}/{vs}"
```

**Compare your output against `phase_1_encoding` field.**

**IMPORTANT EXCEPTION**: When Phase 2 encoding (`semantic_encoding`) was created, they didn't fix Phase 1 errors they found. Common example: numbers written as words ("two") instead of digits ("2"). 

**If a "difference" exists in both `phase_1_encoding` AND `semantic_encoding`, consider it acceptable** — the semantic layer preserved it, meaning it's functionally correct.

### If Tie

Prefer V3 (most comprehensive) > V2 (evidence-based) > V1 (policy-only)

---

## Learnings Update Protocol

**Key principle**: Update the version(s) that got it WRONG, not the one that got it right.

| Scenario | Action |
|----------|--------|
| All match reference | No update needed |
| Some wrong, some right | Update WRONG version's `learnings-{v}.md` with what they missed |
| All wrong, same mistake | Add to ALL learnings files |
| Right version learned something new | Note in learnings if a novel pattern was discovered |

### Debug Process for Failed Encodings

When a subagent produces incorrect output:

1. **Identify the specific difference** — what's wrong vs. reference?
2. **Diagnose root cause** — which rule/pattern was missed or misapplied?
3. **Consider multiple fixes**:
   - Is it a missing pattern in learnings?
   - Is it a rule misinterpretation?
   - Is it a vocabulary issue?
4. **Update the appropriate learnings file** with the fix

### Learnings Format
```markdown
## {Category}
- {pattern} → `{solution}` — {verse reference}
```

---

## Step Comparison

| Step | V1 (Policy) | V2 (Evidence) | V3 (Blended) |
|------|-------------|---------------|--------------|
| 1 | Copy NIV | Resolve Coreference | Resolve Coreference |
| 2 | Fix Pronouns | Segment Clauses | Segment Clauses (+aspect) |
| 3 | Simplify Vocab | Add Brackets | Add Brackets (+after) |
| 4 | Group Participants | Named Formula | Named Formula |
| 5 | Fix Clauses | Mark Speech | Mark Speech (+rhetorical) |
| 6 | Checklist Pass | Simplify Vocab | Simplify Vocab (+forbidden) |
| 7 | — | Discourse Markers | Discourse Markers |
| 8 | — | Mark Implicit | Mark Implicit (He1/He2) |
| 9 | — | Apply Learnings | Grammar Constraints |
| 10 | — | **Linter (must pass)** | **Linter (must pass)** |

### Key Differences

| Aspect | V1 | V2 | V3 |
|--------|----|----|-----|
| Steps | 5+1 | 10 | 10 |
| Rules | Policy docs | 6,963 verse corpus | Policy + corpus |
| Confidence | None | 🟢🟡🔴 | 🟢🟡🔴 + 📘 |
| Self-contained | Mostly | Yes | Yes |

---

## APIs

| Tool | URL | Notes |
|------|-----|-------|
| Linter | `https://editor.tabitha.bible/check?text={urlencoded}` | Run until clean |
| Sources | `https://sources.tabitha.bible/Bible/{Book}/{ch}/{vs}` | Use `Accept: application/json` header |
| Ontology | `https://ontology.tabitha.bible/?q={word}` | Check word levels |

---

## Files

| File | Purpose |
|------|---------|
| `SUBAGENT-SKILL.md` | V1 policy-first rules |
| `SUBAGENT-SKILL-V2.md` | V2 evidence-based rules |
| `SUBAGENT-SKILL-V3.md` | V3 blended rules |
| `learnings-v1.md` | V1 patterns (update when V1 fails) |
| `learnings-v2.md` | V2 patterns (update when V2 fails) |
| `learnings-v3.md` | V3 patterns (update when V3 fails) |
