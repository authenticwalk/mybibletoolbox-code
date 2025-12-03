# How to Run a Fair Test

## Test Setup

Pick a verse that is **NOT** in any examples:
- NOT Ruth 1:1-3 (in V1 examples)
- NOT Genesis 22:2 (in examples.md)
- NOT Ruth 2:4 (in examples.md)
- NOT Romans 8:31 (in examples.md)

**Suggested test verses:**
- Exodus 3:4 (God calls Moses)
- 1 Samuel 17:4 (Goliath introduction)
- Matthew 5:3 (Beatitudes)
- John 1:1 (In the beginning)

---

## Run Each Version

### Test V1 (Examples-First)

```bash
cd /Users/chrispriebe/projects/mybibletoolbox/mybibletoolbox-code

claude --print "Read bible-study-tools/tbta/phase1/policies/SKILL-v1-examples.md

Convert Exodus 3:4 to He1. 
Follow the output format exactly - create ./output/EXO-003-004.md with step-by-step work.
Show text = \"...\" after each step.
Do NOT look at sources.tabitha.bible until after Step 5." > bible-study-tools/tbta/phase1/policies/test-comparison/v1-exo-3-4.md
```

### Test V2 (Rules-First)

```bash
claude --print "Read bible-study-tools/tbta/phase1/policies/SKILL-v2-rules.md

Convert Exodus 3:4 to He1. 
Follow the output format exactly - create ./output/EXO-003-004.md with step-by-step work.
Show text = \"...\" after each step.
Do NOT look at sources.tabitha.bible until after Step 5." > bible-study-tools/tbta/phase1/policies/test-comparison/v2-exo-3-4.md
```

### Test V3 (Progressive)

```bash
claude --print "Read bible-study-tools/tbta/phase1/policies/SKILL-v3-progressive.md
Also read the rules/*.md files as needed.

Convert Exodus 3:4 to He1. 
Follow the output format exactly - create ./output/EXO-003-004.md with step-by-step work.
Show text = \"...\" after each step.
Do NOT look at sources.tabitha.bible until after Step 5." > bible-study-tools/tbta/phase1/policies/test-comparison/v3-exo-3-4.md
```

---

## Get Ground Truth

```bash
curl -H "Accept: application/json" "https://sources.tabitha.bible/Bible/Exodus/3/4" | jq '.phase_1_encoding'
```

---

## Score Each Version

After running all three, compare:

1. **Did they follow the format?** (step-by-step with text = "...")
2. **Pronoun resolution** — all 3rd person pronouns resolved?
3. **Vocabulary** — L2 words paired?
4. **Clauses** — brackets correct?
5. **Match reference** — how close to sources.tabitha.bible?

---

## Scoring Rubric

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Format followed | No steps shown | Partial | Full step-by-step |
| Pronouns resolved | Many missed | Some missed | All resolved |
| Vocabulary correct | Wrong words | Partial pairings | All L2 paired |
| Clauses correct | Wrong brackets | Minor issues | All correct |
| Matches reference | Very different | Close | Exact match |

**Total: /10 per version**

