# TBTA Verse Column - Rebuild Instructions

## Objective
Reverse engineer TBTA's "Verse" column to create rules an LLM can follow to reproduce the transformation from NIV → CNL (Controlled Natural Language).

## Scope
**Books**: Genesis, Joshua, Ruth, 1-2 Samuel, Nehemiah, Esther, Daniel, Jonah, Nahum, Matthew, Mark, Acts, Titus, Philemon, 2 John

**Data Source**: https://github.com/AllTheWord/tbta_db_export/blob/main/csv/Bible/

## Deliverables
- `RULES.md` - Transformation rules using pregnant phrases (done)
- `SKILL.md` - LLM prompt for verse generation (done)
- `RULES.md` needs: 5 supporting refs + 3 contradicting refs per rule

## Requirements

### 1. Use Pregnant Phrases
Compress rules using established terminology:
- **Coreference resolution** (not "replace pronouns with nouns")
- **Clause segmentation** (not "one verb per sentence")
- **Explicit relativization** (not "appositive to relative clause")
- **Deixis marking** (not "mark speaker/hearer")
- **LDV substitution** (Longman Defining Vocabulary L0-L3)
- **CNL** (Controlled Natural Language)

### 2. Evidence-Based Rules
Each rule must have:
- **Up to 5 supporting references** (best examples first)
- **Up to 3 contradicting references** (inconsistencies)

Format: `**Rule Name** (Ruth 1:3, Gen 1:4, Jonah 1:2; NOT Ruth 1:13, Matt 5:3)`

### 3. Source Strategy
Document as: "Copy NIV EXCEPT [list] AND INCORPORATE [list from Hebrew/Greek/scholarship]"

## Process to Rebuild

1. **Download CSVs** for all 15 books from GitHub
2. **Analyze patterns** - search for rule violations and confirmations
3. **Update RULES.md** - add real verse references per rule
4. **Discover He1/He2 differences** - Ruth=He1 (natural), Matthew=He2 (strict)
5. **Validate** - test rules against held-out verses, measure accuracy

## Current State
- `RULES.md` - 142 lines, 12 rules with pregnant phrases, NO references yet
- `SKILL.md` - 66 lines, 7-step process
- `RULES-VERBOSE.md` - 213 lines, full explanations (reference only)
- `SKILL-VERBOSE.md` - 133 lines, full examples (reference only)
- `TEST-RESULTS.md` - 112 lines, 95-100% accuracy on Ruth samples

## Next Steps
1. Download all 15 book CSVs
2. For each rule in RULES.md, grep for supporting/contradicting examples
3. Update RULES.md with format: `Rule (ref, ref, ref; NOT ref, ref)`
4. Prioritize references by clarity (best examples first)
