# Ruth 4 SKILL Comparison v2: Unchurched Adults Source

## Test Setup
- **Source**: Unchurched Adults (targets.tabitha.bible) - already simplified
- **Target**: He1 encoding (sources.tabitha.bible reference)
- **Verses**: Ruth 4:1, 4:5, 4:13

## Performance Results

| Approach | Ruth 4:1 | Ruth 4:5 | Ruth 4:13 | Average |
|----------|----------|----------|-----------|---------|
| V1 Examples | ~55% | ~45% | ~65% | **~55%** |
| V2 Rules | ~50% | ~55% | ~50% | **~52%** |
| V3 Progressive | ~55% | ~55% | ~70% | **~60%** |

**Note**: Starting from Unchurched Adults (already simplified) gave slightly better results than NIV.

---

## Common Errors Across All Approaches

| Error Type | What Happened | Should Be |
|------------|---------------|-----------|
| Missing `(title)` | No section title | "(title) Boaz marries Ruth" |
| Missing `(imp)` | "come here" | "you(man) (imp) come to this place" |
| Wrong verb | "slept with" / "had sex with" | "sexed" |
| Wrong causative | "made Ruth pregnant" | "caused [Ruth to become pregnant]" |
| Wrong birth phrase | "birthed" / kept "gave birth" | "gave birth to" (confirmed) |
| Missing pronoun refs | "you buy" | "you(man) buy" |
| Wrong deity name | "the LORD" | "Yahweh" |
| Implicit notation | `<< >>` or inline | `(implicit-info)` marker |

---

## Approach-Specific Issues

### V1 Examples-First
**Unique errors:**
- Changed vocabulary unnecessarily: "property" → "land"
- Over-simplified: "kinsman-redeemer" → "family-protector"
- Kept quotes instead of brackets for speech

**Root cause**: Examples show transforms but don't explain *boundaries* - agent felt free to simplify beyond specification.

### V2 Rules-First
**Unique errors:**
- **Critical**: Used pronouns (he/she/her) after first mention
- Rule §3 says "After first occurrence: can use natural pronouns" - **AMBIGUOUS**

**Root cause**: Rule is literally incorrect/misleading. Agent followed rule exactly but got wrong result.

### V3 Progressive
**Unique errors:**
- Wrongly hyphenated "sit-down" (should be "sat down")
- Used "birth" as verb per learnings.md (outdated)
- Used `<< >>` notation per rules (wrong version)

**Root cause**: Outdated learnings.md + notation version confusion between He1/Phase2.

---

## Maintainability Analysis

### Key Question: Which approach is easiest to fix and extend?

| Factor | V1 Examples | V2 Rules | V3 Progressive |
|--------|-------------|----------|----------------|
| **Adding new patterns** | Add example | Add rule to section | Add to specific rule file |
| **Fixing errors** | Find/update example | Find rule by § number | Update specific file |
| **Finding what to fix** | Hard (search examples) | Easy (§ references) | Medium (check file) |
| **Avoiding bloat** | Examples grow linearly | Single file grows | Distributed across files |
| **Version control** | Hard to track changes | Moderate | Easy (per-file diffs) |
| **Consistency** | Low (pattern matching) | High (explicit rules) | Medium (cross-file) |

### V2 Rules: Best for Long-Term Maintenance

**Why V2 wins for maintainability:**

1. **Explicit § references** - Agent V2 cited "§3 pronoun rules" making it trivial to find and fix
2. **Categorical organization** - Rules grouped by type (Pronouns, Words, Clauses, etc.)
3. **Easy to audit** - Can review each section systematically
4. **Clear fix locations** - When V2 agent made pronoun error, we know exactly where to fix: §3

**V2 Fix Example:**
```markdown
### Pronouns (§3)
- ❌ Third person pronouns (he/she/they) — ALWAYS resolve to nouns
- ✅ First/second person: `I(Paul)`, `you(people)`, `we(Peter) _excl`
- ⚠️ Note: "After first occurrence" ONLY applies to 1st/2nd person maintaining their form
- ❌ NEVER use he/she/they even after first mention
```

### V3 Progressive: Second Best

**Advantages:**
- Separate files = smaller diffs, easier code review
- Can update `learnings.md` without touching main skill
- Modular structure scales well

**Disadvantages:**
- Cross-file dependencies can cause version drift
- Agent V3 had notation confusion (He1 vs Phase2) because files weren't synced
- Need to update multiple files for single concept

### V1 Examples: Hardest to Maintain

**Problems:**
- No systematic categorization
- Adding examples doesn't prevent interpretation drift
- Hard to find where specific rule is taught
- Agent felt free to "interpret" beyond examples

---

## Recommendation: Hybrid V2+V3

**Proposed structure:**

```
SKILL.md (V2 style - complete rules with § references)
├── Quick reference table (80% cases)
├── §1 Vocabulary rules
├── §2 Pronoun rules
├── §3 Clause rules
├── §4 Quote/Speech rules
├── §5 Special markers ((imp), (title), (implicit-info))
├── §6 Approved vocabulary list
└── References to detail files for edge cases

rules/
├── vocabulary-levels.md (L0-L4 lookup)
├── notation-versions.md (He1 vs Phase2 differences)
└── worked-examples.md (V1-style examples organized by § reference)
```

**Why hybrid:**
1. V2's § structure for easy fixes and auditing
2. V3's separate files for vocabulary lookup and version clarity
3. V1's examples linked to specific § rules for pattern learning

---

## Action Items to Fix Current SKILLs

### V2-rules.md (Priority: HIGH)
1. Fix §3: Clarify "NEVER use 3rd person pronouns, even after first mention"
2. Add §X: Imperative markers `(imp)` with `you(addressee)` syntax
3. Add §X: Title markers `(title)` at section starts
4. Add §X: Implicit info using `(implicit-info)` notation
5. Add vocabulary table: "sexed", "caused [X]", "gave birth to"

### V3-progressive.md (Priority: MEDIUM)
1. Update learnings.md: Remove "birth as verb" (wrong)
2. Clarify notation: He1 uses `(implicit-info)` not `<< >>`
3. Add section on `(imp)` markers
4. Sync all rule files to same notation version

### V1-examples.md (Priority: LOW)
1. Add examples showing `(imp)` markers
2. Add examples showing `(title)` markers
3. Add vocabulary constraints section
4. (Consider deprecating in favor of V2 with linked examples)

---

## Conclusion

**For accuracy**: All approaches ~55-60% (source text matters less than skill completeness)

**For maintainability**: **V2 Rules-First** is best because:
- § references make errors traceable
- Single file to audit
- Clear categorical structure
- Easy to add rules without breaking existing content

**Recommended path forward:**
1. Fix V2 with identified gaps
2. Add vocabulary reference file (from V3 approach)
3. Link worked examples (from V1 approach)
4. Retest to validate improvements
