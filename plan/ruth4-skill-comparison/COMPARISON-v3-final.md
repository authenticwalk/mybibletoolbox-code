# Ruth 4 SKILL Comparison v3: Final Test (4 Approaches)

## Test Setup
- **Source**: Unchurched Adults (targets.tabitha.bible)
- **Verses**: Ruth 4:1, 4:5, 4:13
- **Approaches**: SKILL.md (original), V1, V2 (fixed), V3

## Results Summary

| Approach | Est. Accuracy | Pronoun Fix | Brackets | (imp) markers | Verb choices |
|----------|---------------|-------------|----------|---------------|--------------|
| **SKILL.md** | 30-40% | ✅ | Partial | ✅ | ❌ birthed |
| **V1 Examples** | 60-70% | ✅ | ❌ Under-bracketed | ❌ Missing | ❌ slept with |
| **V2 Rules (fixed)** | 70-85% | ✅ | ✅ | ✅ | ⚠️ had sex with |
| **V3 Progressive** | ~65% | ✅ | ✅ | Partial | ❌ Multiple |

## Final He1 Comparisons (Ruth 4:13 - cleanest test)

| Approach | Output |
|----------|--------|
| **Reference** | `So Boaz married Ruth. [When Boaz sexed Ruth] Yahweh caused [Ruth to become pregnant]. Then Ruth gave birth to a son.` |
| **SKILL.md** | `So Boaz married Ruth. When Boaz slept with Ruth, Yahweh caused [Ruth to become pregnant]. Then Ruth birthed a son.` |
| **V1** | `So Boaz married Ruth. When Boaz slept with Ruth, Yahweh caused Ruth to become pregnant. Then Ruth birthed a son.` |
| **V2 (fixed)** | `So Boaz married Ruth. [When Boaz had sex with Ruth], Yahweh caused [Ruth to become pregnant]. Then Ruth birthed a son.` |
| **V3** | `So Boaz married Ruth. [When Boaz slept with Ruth], Yahweh caused [Ruth become pregnant]. Then Ruth birth a son.` |

## Key Findings

### V2 (Fixed) Won
- Best bracket placement
- Caught (imp) markers in Step 6 Checklist Pass
- Followed learnings.md correctly
- Only missed: "sexed" vs "had sex with", "gave birth" vs "birthed"

### What Each Approach Missed

| Approach | Critical Miss |
|----------|---------------|
| **SKILL.md** | No temporal bracket `[When...]` |
| **V1** | No brackets on patient clause `caused [Ruth...]` |
| **V2** | Verb form: "had sex with" → "sexed" |
| **V3** | Grammar errors: "Ruth birth" not "Ruth gave birth" |

### learnings.md Issue Confirmed
All approaches that read learnings.md used "birthed" because it says:
> "Use `birth` as verb instead of `give birth` (not in ontology)"

But reference uses "gave birth to" - **learnings.md is wrong**.

## Recommendation

**V2 Rules-First (fixed)** is the winner:
- 70-85% accuracy (highest)
- Step 6 Checklist Pass catches markers other approaches miss
- § references make debugging easy
- Only remaining issues are vocabulary choices

### One More Fix Needed

Update learnings.md:
```diff
- Use `birth` as verb instead of `give birth` (not in ontology)
+ Use `gave birth to` (NOT "birth" or "birthed" as standalone verb)
```

And add:
```
- "slept with" / "had sex with" → `sexed` (use verb form)
```
