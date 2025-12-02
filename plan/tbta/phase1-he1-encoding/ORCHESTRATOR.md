# He1 Encoding Orchestrator

Run two subagents in parallel with different skill versions, then select the best result.

## Workflow

```
                    ┌─────────────────────────────────┐
                    │         ORCHESTRATOR            │
                    │  (reads SKILL.md, RULES.md)     │
                    └───────────────┬─────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │         PARALLEL CALL          │
                    ▼                                ▼
        ┌───────────────────┐           ┌───────────────────┐
        │    Subagent V1    │           │    Subagent V2    │
        │ SUBAGENT-SKILL.md │           │ SUBAGENT-SKILL-V2 │
        └─────────┬─────────┘           └─────────┬─────────┘
                  │                               │
                  ▼                               ▼
        ┌───────────────────┐           ┌───────────────────┐
        │   Result A + Issues        │   Result B + Issues │
        └───────────────────┘           └───────────────────┘
                    │                               │
                    └───────────────┬───────────────┘
                                    ▼
                    ┌─────────────────────────────────┐
                    │     COMPARE & SELECT BEST       │
                    │  - Linter errors               │
                    │  - Rule compliance             │
                    │  - Naturalness                 │
                    └───────────────┬─────────────────┘
                                    │
                                    ▼
                    ┌─────────────────────────────────┐
                    │      UPDATE LEARNINGS           │
                    │  (if new patterns discovered)   │
                    └─────────────────────────────────┘
```

## Subagent Prompts

### Subagent V1 (Original)

```markdown
# Task: Encode {BOOK} {ch}:{vs} to He1

Read and follow: `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL.md`
Also read: `bible-study-tools/tbta/phase1/policies/learnings.md`

## NIV Input
"{niv_text}"

## Output Format
Return:
1. Final He1 encoding
2. Linter results (errors/warnings)
3. Issues encountered (for orchestrator)
```

### Subagent V2 (Enhanced)

```markdown
# Task: Encode {BOOK} {ch}:{vs} to He1

Read and follow: `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL-V2.md`

This skill tells you to also read:
- `plan/tbta/phase1-he1-encoding/RULES.md`
- `bible-study-tools/tbta/phase1/policies/learnings.md`

## NIV Input
"{niv_text}"

## Output Format
Return:
1. Final He1 encoding
2. Linter results (errors/warnings)
3. Issues encountered (for orchestrator)
```

## Selection Criteria

Pick the better result based on (in priority order):

| Priority | Criterion | How to Check |
|----------|-----------|--------------|
| 1 | Linter passes | Zero blocking errors |
| 2 | Rule compliance | Matches HIGH confidence rules in RULES.md |
| 3 | Pronoun resolution | All 3rd person pronouns → nouns |
| 4 | Bracket correctness | Subordinate clauses properly bracketed |
| 5 | Natural flow | Reads naturally while following rules |

**If both pass linter**: Prefer the one with fewer warnings and better rule compliance.

**If both have errors**: Pick the one with fewer/less severe errors, note issues for learnings.

## Learnings Update

After selecting the best result:

1. **If both succeeded similarly**: No update needed
2. **If V2 was clearly better**: Note which rules made the difference
3. **If V1 was better**: Investigate why V2 rules caused issues
4. **If both had same issue**: Add to `learnings.md`

### Update Process

```markdown
## In learnings/{verse-slug}.md:
- What went wrong
- Which version handled it better
- Root cause analysis
- Proposed policy statement

## In learnings.md:
- One-line policy under appropriate header
- Link to detailed diagnostic
```

## Example Orchestrator Flow

```python
# Pseudocode for orchestrator

verse = "Ruth 1:1"
niv = "In the days when the judges ruled..."

# 1. Call both subagents in parallel
results = parallel_call([
    Task(subagent="haiku", prompt=v1_prompt(verse, niv)),
    Task(subagent="haiku", prompt=v2_prompt(verse, niv))
])

# 2. Parse results
result_v1 = parse_encoding(results[0])
result_v2 = parse_encoding(results[1])

# 3. Compare
winner = select_best(result_v1, result_v2)

# 4. Update learnings if needed
if new_patterns_discovered(result_v1, result_v2):
    update_learnings(verse, result_v1, result_v2, winner)

# 5. Return best encoding
return winner.encoding
```

## File References

| File | Role |
|------|------|
| `SKILL.md` | Orchestrator reference (10-step process) |
| `RULES.md` | Full rules for V2 subagent |
| `SUBAGENT-SKILL.md` | V1 subagent instructions |
| `SUBAGENT-SKILL-V2.md` | V2 subagent instructions |
| `learnings.md` | Accumulated patterns (both versions read) |
