# Stage 2: Analysis & Hypothesis Validation

**Role**: Data Scientist / Polyglot / QA
**Input**: Feature Definition (Stage 1)
**Output**: `analysis/` (Data dumps, scripts, Scorecards)

## Goal

Quantitatively validate the feature against real-world translations _before_ writing prompts. Shift from "looking for patterns" to "testing hypotheses".

## SETUP

- $CURRENT-FEATURE-DIR: `/bible-study-tools/tbta/features/{feature}/`
- $ANALYSIS-DIR: $CURRENT-FEATURE-DIR/analysis
- Check that your CWD is `/bible-study-tools/tbta/features` if not warn user then load `/bible-study-tools/tbta/features/CLAUDE.md`

## Quick Reference

```
analysis/
├── data/
│   ├── train.jsonl      # max 300 entries
│   ├── validate.jsonl   # max 100 entries
│   ├── test.jsonl       # max 100 entries (DO NOT TOUCH until final eval)
│   └── leftovers.jsonl  # remaining entries not in train/validate/test
├── tbta-extract.jsonl   # full extraction
├── README.md            # results summary
└── logical.py           # optional rules script
```

## Step 3: Analyze Patterns (Parallel Tasks)

Run these analyses in parallel using subagents:

### 3A: Dominant Value Analysis

Run as: 1 Subagents
Parallel: Yes
Models: Opus

**Datasource** $ANALYSIS-DIR/data/train.secret.jsonl and $ANALYSIS-DIR/data/leftovers.secret.jsonl

**Output** $ANALYSIS-DIR/EDGE-CASES.md

When one value dominates (e.g., Singular 66%):
1. Focus on: "When is it NOT the dominant value?"
2. List all conditions where the minority value applies; trying to group them into most common to least common with examples for each

### 3B: TBTA label quality

Run as: 1 Subagents
Parallel: Yes
Models: Opus

**Datasource** 
 - $ANALYSIS-DIR/data/train.secret.jsonl
 - $ANALYSIS-DIR/data/leftovers.secret.jsonl
 - $ANALYSIS-DIR/HIGH-LEVEL-REVIEW.md
 - $CURRENT-FEATURE-DIR/README.md (and potentially the subfiles)

**Output** $ANALYSIS-DIR/TBTA-QUALITY.md

Do a critical review of the TBTA labels.  Verify your work don't just theorize they are wrong.  

Be careful of broad assumptions like in research there is no FOUR person number system but TBTA has it; consider instead why they may have done it such as for translating the remaining 4000 langauges that are not yet documented they may encounter a langauge that does require it, labelling it as four is harmless in that langauges with only 3 will just call it plural.

Be sure to include qualifying questions asked very respectfully for the TBTA team to clear up confusion; providing examples for each.

### 3C: Word Patterns

#### Phase 1: Script Analysis (frequency patterns)

Run as: 4 Subagents
Parallel: Yes 
  1. `python src/ingest_data/tbta/group_by_strongs.py --input $ANALYSIS-DIR/data/train.jsonl --group-by strongs_number --min-support 3 --output $ANALYSIS-DIR/strongs-analysis.jsonl`
  2. `python src/ingest_data/tbta/group_by_strongs.py --input $ANALYSIS-DIR/data/leftovers.jsonl --group-by constituent --min-support 10 --output $ANALYSIS-DIR/constituent-leftovers-analysis.jsonl`
  3. `python src/ingest_data/tbta/group_by_strongs.py --input $ANALYSIS-DIR/data/train.jsonl --group-by constituent --min-support 3 --output $ANALYSIS-DIR/constituent-train-analysis.jsonl`
  4. `python src/ingest_data/tbta/group_by_strongs.py --input $ANALYSIS-DIR/data/train.jsonl --min-support 10 --output $ANALYSIS-DIR/translations-train-analysis.jsonl`
Models: Opus

**prompt**
`
Analyze ${filename} to find patterns for predicting ${feature} labels. Be critical and think deeply—watch for undersampling or overfitting.

**Theory**: Other languages encode ${feature} grammatically. If certain translation words consistently appear when a Hebrew/Greek word has a specific label, we can use those patterns as prediction rules.

**Data structure**:
- `entry.group`: The word we are trying to label for ${feature}
- `entry.top_patterns.pattern.translation`: The language giving us a clue
- `entry.top_patterns.pattern.word`: The word from that language that signals the label
- `--GROUP-BY-ITSELF--`: The value in `entry.group` alone is sufficient to predict the label

**Key insight**: For words with VARIABLE labels, find CONTEXTUAL patterns that explain the variation:
- Preceding word context: "two **men**" → Dual, "three **men**" → Trial
- Named entities in context: "**sons** of Zebedee" (we know there are 2) → Dual
- Translation morphology: Arabic dual suffix (-ān), Hebrew suffix (-ayim) → Dual
- Verse context you know from memory

Good hints:
- ✅ "For H0376 (man), look at the preceding numeral to determine number"
- ✅ "For G5207 (son), check if named entity follows with known count"

Bad hints (just memorization):
- ❌ "H0376 is always Dual" (wrong—it varies by context)

Exceptions are just as important: a pattern might be "usually X except when Y". Use your internal memory to reason about verse references and why some would differ.

**Output format** (provide a few examples with verse refs for each):

# Major Patterns
Large sweeping consistencies we can make rules from:
1. When the word we are labelling is a name it will be singular

# Exceptions
What are exceptions to the above?
- Do you estimate there are <50 Strong's codes that would cover all exceptions? These are one-offs we'll solve later by adding hints on those specific Strong's words.
1. `heavens` while it looks plural in some languages is singular

# One-offs
Patterns not worth making a rule for (too complex, <50 Strong's words would cover it)

# Potentially Data Labelling Issues
Clear patterns where data labelling is inconsistent or confusing. Group by common issues, provide examples with verses and their labels.

`

Now create a file in jsonl format with the schema of each entry as
```
group: str: the name of your group. Not entry.group from above but how you grouped all those entries together
rule: str: max 200 words; a long form description written to a human labeller about the policy of when to label a feature this value
exceptions: []{
  group: str: group the exceptions into logical similar units and give it a name
  exception: str: max 200 words; explain when you would break the rule and label as another value
  strongs: str[] exhaustive list of all strongs numbers in format of (G|H)${strongs_number:fd4}
}
```

### 3D Logical Reason Analysis

Run as: 4 Subagents
Parallel: Yes (with 3C)
Models: Opus

**Goal**: Identify theological/grammatical reasons why verses get specific labels, then add hints to edge cases.

**Rationale**: Writing prompts with endless edge cases is confusing. Instead, add verse-specific hints for rare patterns (<500 occurrences).

**Notes**:
- You have memorized the entire Bible and can mostly rely on your accuracy
- Limit each reason group to maximum 500 verses

**Phase 1: Group verses by reason**

```bash
python src/ingest_data/tbta/group_by_reasons.py \
  --input $ANALYSIS-DIR/data/train.jsonl \
  --output $ANALYSIS-DIR/reason-groupings.jsonl
```

The script outputs groups WITHOUT hints:
```json
{"reason": "TRINITY", "count": 45, "verses": ["GEN.001.026", "GEN.003.022", ...]}
{"reason": "UNSET", "count": 120, "verses": [...]}
```

**Phase 2: Add hints (LLM task)**

- [ ] Read `features/${feature}/research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml` for context
- [ ] Review each group in `reason-groupings.jsonl`
- [ ] For reason NONE verses: determine which reason group they belong to, or create new groups, or ignore
- [ ] Add a `"hint"` field to each group (max 250 words)
- [ ] Save as `$ANALYSIS-DIR/reason-groupings-with-hints.jsonl`

**Required transformation** - add `hint` field to each group:
Example)
```json
{"reason": "TRINITY", "hint": "Trinitarian context often uses plural forms...", "description": "...", "count": 45, "verses": [...]}
{"reason": "DIVINE_SPEECH", "hint": "Direct divine speech typically uses...", "description": "...", "count": 30, "verses": [...]}
```

**Hint guidelines**:
- Generic enough to apply to all verses in the group (not verse-specific)
- Explains the theological/grammatical principle (e.g., "Trinitarian verses often use plural because...")
- Avoid absolute language like "must" - these are hints, not rules
- Include edge case considerations where relevant

**Validation checklist**:
- [ ] Do you agree with TBTA's labels? Note disagreements in `$ANALYSIS-DIR/TBTA-QUALITY.md`
- [ ] Are there verses missing from groups that should be included?
- [ ] Are there verses in groups where the hint doesn't apply?


## Step 7: Document Results

**Input**:
 - review all the markdown files in the analysis director
 - `$ANALYSIS-DIR/reason-groupings-with-hints.jsonl`
  
Create `$ANALYSIS-DIR/README.md` linking to the subfiles for more details:

```markdown
# {Feature} Analysis

## Distribution
- Value A: X% (N entries)
- Value B: Y% (N entries)

## Dataset Sizes
- Train: N | Validate: N | Test: N

## Key Findings
1. [Pattern 1]: [accuracy]% confidence
2. [Pattern 2]: [accuracy]% confidence
...

## Suspicious Data
- [Any TBTA labeling concerns]

## Recommended Approach
- [ ] Simple rules (logical.py)
- [ ] LLM with hints
- [ ] Hybrid approach
```

Update `features/{feature}/README.md` with summary linking to analysis.


