# TBTA Phase 1 (He1) — Orchestrator Skill

> **Mission**: Run parallel subagents to encode NIV verses to He1, select best result, debug failures.

## Input Handling

**Required**: Verse reference — any format: `Ruth 4:1`, `RUT 4:1`, `Ruth 4:1-5`, `Matthew 2:1-10`
**Optional**: Verse text — if not provided, will be fetched

| Input | Action |
|-------|--------|
| Reference + text | Use provided text |
| Reference only | Fetch text from sources |
| No reference | Return error |

```
# Examples
Ruth 4:1  Boaz went up to the town gate...   # uses provided text
Matthew 2:1-10                                 # fetches text
```

---

## Workflow

```
INPUT: Verse reference (text optional)
    │
    ├──► Subagent V1 (Policy)
    ├──► Subagent V2 (Evidence)
    └──► Subagent V3 (Blended)
           │
           ▼
    FETCH REFERENCE (sources.tabitha.bible)
           │
           ▼
    COMPARE & SELECT (match phase_1_encoding)
           │
           ▼
    DEBUG FAILURES (analyze what went wrong)
           │
           ▼
    UPDATE LEARNINGS (wrong version's learnings-{v}.md)
```

## Process

1. **Get NIV** → Validate input OR fetch verse
   - Single verse: `src/tools/fetch_verse.py`
   - Chapter: `https://www.biblestudytools.com/{book}/{chapter}.html`
2. **Launch subagents** → Run V1, V2, V3 in parallel (see prompt below)
3. **Collect results** → Each returns: He1 encoding (linter-validated) + issues
4. **Fetch reference** → `curl -H "Accept: application/json" "https://sources.tabitha.bible/Bible/{Book}/{ch}/{vs}"`
5. **Compare & select** → Match against `phase_1_encoding` field
6. **Debug failures** → Analyze what went wrong, update learnings

---

## Subagent Prompt

**For V1/V2/V3** — adjust file names accordingly:
```
Read: ./SUBAGENT-SKILL{-V2|-V3}.md + learnings-v{1|2|3}.md
Input: "{verse_ref}: {niv_text}"
File Ouput: "Write to `${OUTPUT}`" OR Don't save to files
Return: He1 encoding (linter-validated), issues
NOTE: Run linter until clean (max 12 iterations) BEFORE returning


```

Note: only write to ${OUTPUT} if you where told what your subagent outdir was otherwise the subagent is not allowed to save to files (default)

| Version | Skill File | Learnings |
|---------|------------|-----------|
| V1 | `SUBAGENT-SKILL.md` | `learnings-v1.md` |
| V2 | `SUBAGENT-SKILL-V2.md` | `learnings-v2.md` |
| V3 | `SUBAGENT-SKILL-V3.md` | `learnings-v3.md` |

---

## Selection Criteria

**Primary**: Match reference `phase_1_encoding` from Sources API.

**Exception**: If difference exists in both `phase_1_encoding` AND `semantic_encoding`, consider it acceptable — Phase 2 doesn't fix Phase 1 errors (e.g., "two" vs "2").

**Tiebreakers** (if all match reference equally):
1. Linter passes (zero errors)
2. Pronoun resolution complete
3. Prefer V3 > V2 > V1

---

## Learnings Update Protocol

**Key principle**: Update the version(s) that got it WRONG, not the one that got it right.

| Scenario | Action |
|----------|--------|
| All match reference | No update needed |
| Some wrong, some right | Update WRONG version's `learnings-{v}.md` |
| All wrong, same mistake | Add to ALL learnings files |

### Debug Process

1. **Identify** — what's wrong vs. reference?
2. **Diagnose** — which rule/pattern was missed?
3. **Consider fixes** — missing pattern? rule misinterpretation? vocabulary?
4. **Update** the appropriate learnings file

### Learnings Format

**CRITICAL**: Learnings must be GENERIC patterns applicable to ANY verse.

```markdown
## {Generic Category}
- {pattern} → `{solution}` (Mt 2:1, Ac 10:3)
```

**Rules**:
1. **Headers = Generic categories** — "L2 Word Pairings", "Verb Case Frames", "Quote Structure" — NEVER verse-specific ("Matthew 2:1-10 Learnings")
2. **Verse refs = Suffix only** — Add `(Mt 2:1)` at END to show evidence, not as headers
3. **No metadata** — Never add "(V1 Winner)", error counts, iteration counts
4. **Merge into existing sections** — Find the right category, don't create new verse-specific sections

### Rule Aggregation

**Before adding**, check for similar rules → merge into existing section with combined refs.

```markdown
# BAD (verse-specific section):
## Matthew 2:1-10 Learnings
- "Magi" → "wise men"

# GOOD (merged into generic section):
## L2 Word Substitutions
- "Magi" → "wise men" (Mt 2:1)
- "centurion" → "officer/centurion" (Ac 10:1)
```

**Aggregate when**: Same category, same pattern, only specific word differs.
**Keep separate when**: Different logic or exception to pattern.

---

## APIs

| Tool | URL |
|------|-----|
| Linter | `https://editor.tabitha.bible/check?text={urlencoded}` |
| Sources | `https://sources.tabitha.bible/Bible/{Book}/{ch}/{vs}` (use `Accept: application/json`) |
