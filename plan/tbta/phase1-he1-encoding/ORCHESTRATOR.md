# He1 Encoding Orchestrator

Run three subagents in parallel with different skill versions, then select the best result.

## Version Summary

| Version | Approach | Source |
|---------|----------|--------|
| V1 | Policy-first | Official TBTA checklist |
| V2 | Reverse-engineering | Pattern analysis of 6,963 verses |
| V3 | Blended | Policy + evidence reconciled |

See `VERSION-COMPARISON.md` for detailed differences.

## Workflow

```
                              ORCHESTRATOR
                         (SKILL.md, RULES.md)
                                  │
            ┌─────────────────────┼─────────────────────┐
            │                     │                     │
            ▼                     ▼                     ▼
    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │ Subagent V1  │     │ Subagent V2  │     │ Subagent V3  │
    │  (policy)    │     │ (evidence)   │     │  (blended)   │
    └──────┬───────┘     └──────┬───────┘     └──────┬───────┘
           │                    │                    │
           ▼                    ▼                    ▼
       Result A             Result B             Result C
           │                    │                    │
           └────────────────────┼────────────────────┘
                                ▼
                        COMPARE & SELECT
                                │
                                ▼
                        UPDATE LEARNINGS
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

### Subagent V2 (Reverse-Engineering)

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

### Subagent V3 (Blended)

```markdown
# Task: Encode {BOOK} {ch}:{vs} to He1

Read and follow: `bible-study-tools/tbta/phase1/policies/SUBAGENT-SKILL-V3.md`

This skill tells you to also read:
- `plan/tbta/phase1-he1-encoding/RULES.md` (blended policy + evidence)
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

1. **If all three similar**: No update needed
2. **If V3 was best**: Blended approach validated
3. **If V1/V2 beat V3**: Investigate why blending failed
4. **If all had same issue**: Add to `learnings.md`
5. **If V1 vs V2 disagree**: Policy vs evidence conflict - document in `CONTRADICTION-REPORT.md`

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

# 1. Call all three subagents in parallel
results = parallel_call([
    Task(subagent="haiku", prompt=v1_prompt(verse, niv)),  # Policy
    Task(subagent="haiku", prompt=v2_prompt(verse, niv)),  # Evidence
    Task(subagent="haiku", prompt=v3_prompt(verse, niv))   # Blended
])

# 2. Parse results
result_v1 = parse_encoding(results[0])
result_v2 = parse_encoding(results[1])
result_v3 = parse_encoding(results[2])

# 3. Compare all three
winner = select_best(result_v1, result_v2, result_v3)

# 4. Document conflicts between V1 and V2
if result_v1.encoding != result_v2.encoding:
    log_conflict(verse, result_v1, result_v2)  # → CONTRADICTION-REPORT.md

# 5. Update learnings if needed
if new_patterns_discovered(results):
    update_learnings(verse, results, winner)

# 6. Return best encoding
return winner.encoding
```

## File References

| File | Role |
|------|------|
| `SKILL.md` | Orchestrator reference (10-step process) |
| `RULES.md` | Blended rules (policy + evidence) |
| `VERSION-COMPARISON.md` | Explains V1 vs V2 vs V3 differences |
| `SUBAGENT-SKILL.md` | V1 subagent - policy-first |
| `SUBAGENT-SKILL-V2.md` | V2 subagent - reverse-engineering |
| `SUBAGENT-SKILL-V3.md` | V3 subagent - blended |
| `learnings.md` | Accumulated patterns (all versions read) |
| `CONTRADICTION-REPORT.md` | Policy vs evidence conflicts |
