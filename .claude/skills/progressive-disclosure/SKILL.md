---
name: progressive-disclosure
description: Organize markdown documentation using progressive disclosure - README.md ≤200 lines (overview), subfiles ≤400 lines (details), nested directories when limits exceeded. Use whenever creating or updating .md files for research, planning, experiments, or learning documentation.
---

# Progressive Disclosure Documentation

## Core Principle

Organize information hierarchically where each level is self-contained:
- **README.md** (≤200 lines) - Complete overview with links to details
- **Topic files** (≤400 lines) - Deep detail on one topic
- **Nested directories** - When topic files exceed 400 lines

**Key:** README should be the quick reference. Load it and know everything at a glance.

## The 200/400 Rule

| File Type | Max Lines | Content |
|-----------|-----------|---------|
| README.md | 200 | Overview + links to all topics |
| {topic}.md | 400 | Detailed content on one topic |
| {topic}/README.md | 200 | Overview when topic.md exceeded 400 |
| {topic}/{subtopic}.md | 400 | Specific subtopic details |

## Anti-Spam Policy: Prefer Updates Over New Files

**Bad Pattern:**
```
experiments/
├── experiment-001.md
├── experiment-001-results.md
├── experiment-001-analysis.md
├── experiment-001-learnings.md
└── experiment-002.md
```

**Good Pattern:**
```
experiments/
├── experiment-001.md          # Hypothesis → Method → Results → Learnings (all in one)
└── experiment-002.md          # Next iteration
```

**Workflow for updating files:**
1. Write initial content (thesis, hypothesis, plan)
2. Do the work (experiment, research, analysis)
3. **Append results to same file** (add Results section)
4. **Append learnings to same file** (add Learnings section)
5. Only create new file for next iteration or distinct topic

**When to create new files:**
- ✅ Distinct topic that doesn't fit existing files
- ✅ File approaching 400-line limit
- ✅ Next iteration/experiment in a series
- ❌ Different sections of same work
- ❌ Results/analysis of same experiment
- ❌ "Part 2" of something that should be one file

## Structure Pattern: Topic Sections with Links

**Bad (Don't do this):**
```markdown
# Feature Research

## Overview
Research on grammatical features.

## Subfiles
- clusivity.md - Inclusive/exclusive distinctions
- obviation.md - Fourth person systems
- number-systems.md - Dual and trial numbers
```

**Good (Do this):**
```markdown
# Feature Research

Brief overview paragraph explaining what this research covers.

## Clusivity

Inclusive/exclusive distinctions in first-person plural pronouns affect 200+ languages
in our dataset. Key finding: Austronesian languages almost universally exhibit clusivity.

**Status:** Validation complete (12 verses tested, 100% accuracy)

[Read detailed analysis →](clusivity.md)

## Obviation

Fourth person (obviative) systems rank discourse participants by prominence...

**Status:** Framework defined, needs validation

[Read detailed analysis →](obviation.md)

## Number Systems

Dual (2) and trial (3) number marking beyond singular/plural...

**Status:** In progress

[Read detailed analysis →](number-systems.md)
```

**Why this works:**
- Each section gives essential info (no need to click through)
- Links provide path to details without forcing load
- Status makes progress clear
- README stays under 200 lines even with many topics

## Ideal Directory Structures

### Example 1: Feature Research (Simple)

```
features/person-systems/
├── README.md                          # Overview of person systems
├── clusivity.md                       # Detailed analysis
├── obviation.md                       # Detailed analysis
└── number-systems.md                  # Detailed analysis
```

**README.md structure:**
```markdown
# Person Systems

Person systems vary across languages with features like clusivity, obviation,
and complex number marking that affect Bible translation accuracy.

## Clusivity
[2-3 sentences on key findings]
[Read detailed analysis →](clusivity.md)

## Obviation
[2-3 sentences on key findings]
[Read detailed analysis →](obviation.md)

## Number Systems
[2-3 sentences on key findings]
[Read detailed analysis →](number-systems.md)
```

### Example 2: Feature Research (Nested)

When `clusivity.md` exceeds 400 lines, split it:

```
features/person-systems/
├── README.md                          # Still 200 lines - overview
├── clusivity/                         # clusivity.md became directory
│   ├── README.md                      # Clusivity overview
│   ├── validation.md                  # Validation experiments
│   ├── language-patterns.md           # Patterns by language family
│   └── exceptions.md                  # Edge cases and exceptions
├── obviation.md                       # Still under 400 lines
└── number-systems.md                  # Still under 400 lines
```

**clusivity/README.md structure:**
```markdown
# Clusivity in Bible Translation

Inclusive/exclusive distinctions in 200+ languages force explicit theological
interpretation in verses where Greek/Hebrew leave "we" ambiguous.

## Validation

Tested 12 key verses across 7 language families. Achieved 100% accuracy in
predicting which languages require clusivity marking and whether inclusive or
exclusive is appropriate.

[Read validation details →](validation.md)

## Language Patterns

Austronesian: Nearly universal clusivity (kita/kami pattern)
Algic: Suppletive forms (completely different roots)
Mayan: Complex interaction with evidential systems

[Read detailed patterns →](language-patterns.md)

## Exceptions

Three cases where standard rules fail: creoles, language contact situations,
and honorific system interactions.

[Read exception analysis →](exceptions.md)
```

**validation.md structure:**
```markdown
# Clusivity Validation Experiments

Testing prediction accuracy for clusivity marking across verses and languages.

## Experiment Design

**Hypothesis:** Greek inclusive/exclusive distinctions predictable from context
**Method:** Analyze 12 verses in 7 language families
**Success Criteria:** >90% accuracy

## Verse Analysis

### Genesis 1:26 - "Let us make mankind"

**Context:** Divine plural
**Prediction:** Exclusive (God speaking, not including creation)
**Tested Languages:**
- Indonesian: kami (exclusive) ✓
- Tagalog: kami (exclusive) ✓
- Ojibwe: niinawind (exclusive) ✓

**Accuracy:** 3/3 (100%)

[Additional 11 verses analyzed in same format...]

## Results Summary

- Total predictions: 84 (12 verses × 7 languages)
- Correct: 84
- Accuracy: 100%

## Learnings

1. Divine speaker = exclusive (always)
2. Apostolic "we" context-dependent
3. Community "we" requires narrative analysis
```

### Example 3: Experiments with Learning Loop

```
experiments/aspect-marking/
├── README.md                          # Experiment series overview
├── experiment-001.md                  # First attempt (complete)
├── experiment-002.md                  # Refinement (complete)
└── experiment-003.md                  # Current work
```

**experiment-001.md structure (all in one file):**
```markdown
# Experiment 001: Basic Aspect Detection

## Hypothesis

Greek perfect/aorist/present aspect predictable from verb form alone.

## Method

- Analyzed 20 verbs from John 1
- Used morphology codes from Macula Greek
- Predicted aspect marking needed in target languages
- Validated against TBTA database

## Results

**Accuracy:** 70% (14/20 correct)

**Failures:**
- Perfect aspect: 3 wrong predictions
- Stative verbs: 2 wrong predictions

[Detailed results table...]

## Learnings

### What Worked
- Aorist detection: 100% accurate
- Present continuous: 95% accurate

### What Failed
- Perfect aspect needs semantic context, not just morphology
- Stative verbs follow different rules

### Changes for Experiment 002
1. Add semantic context window (±2 verses)
2. Separate stative verb handling
3. Include discourse type (narrative vs discourse)

## Next Steps

See [experiment-002.md](experiment-002.md) for refinements based on these learnings.
```

**Why this works:**
- Everything about experiment-001 is in ONE file
- Results appended after running experiment
- Learnings appended after analyzing results
- Clear link to next iteration
- No spam of separate results/analysis/learnings files

### Example 4: Bad vs Good Nested Structure

**Bad - Unstructured verse files:**
```
clusivity/
├── README.md
├── GEN-001-026.md                     # Random verse file
├── MAT-006-009.md                     # Another random verse file
├── ROM-015-005.md                     # Yet another random verse file
└── random-notes.md                    # Unorganized thoughts
```

**Good - Purposeful organization:**
```
clusivity/
├── README.md                          # Overview with links
├── validation.md                      # All validation work
├── language-patterns.md               # Pattern analysis
└── exceptions.md                      # Edge cases

# validation.md contains all verses in organized sections:
## Divine Speaker Verses (5 verses)
## Apostolic Authority Verses (4 verses)
## Community Identity Verses (3 verses)
```

## README Template

Use this template for all README.md files:

```markdown
# {Topic Name}

[2-3 sentence overview of what this topic covers and why it matters]

## {Subtopic 1 Name}

[2-4 sentences with key findings/status for this subtopic]

[Read detailed analysis →]({subtopic-1}.md)

## {Subtopic 2 Name}

[2-4 sentences with key findings/status for this subtopic]

[Read detailed analysis →]({subtopic-2}.md)

## Current Status

[Brief status: what's done, what's in progress, what's next]
```

**Rules:**
- No "Subfiles" section (use topic sections instead)
- Each section links to its subfile using `[text](path.md)` not aliases
- Keep under 200 lines total
- Include key findings IN the README (don't force clicking)

## Topic File Template

Use this for {topic}.md files:

```markdown
# {Topic Name}

> **Parent Context:** [1 sentence from parent README about larger domain]

[2-3 paragraph detailed introduction to this specific topic]

## {Section 1}

[Detailed content...]

## {Section 2}

[Detailed content...]

## Summary

[Key takeaways from this topic]
```

**Rules:**
- Include parent context at top
- Keep under 400 lines
- If approaching 400, plan conversion to directory
- Organize with clear sections

## Workflow: Creating New Documentation

### Step 1: Start Simple

```bash
mkdir research-topic
cd research-topic
```

Create minimal README.md:
```markdown
# Research Topic

Brief overview of what will be researched.

## Status

Initial exploration - no subfiles yet.
```

### Step 2: Add Content to README

As you learn, update README.md directly:
```markdown
# Research Topic

Overview paragraph.

## Initial Findings

[Add findings as you discover them]

## Questions

[Track questions that emerge]
```

### Step 3: Extract to Subfile When Needed

When README approaches 200 lines, extract details:

```markdown
# Research Topic

Overview paragraph stays.

## Initial Findings

Key findings: [2-3 sentences summary of what's in findings.md]

[Read detailed findings →](findings.md)
```

Create `findings.md` with extracted content.

### Step 4: Continue Growing

- Update existing files before creating new ones
- Create new topic file only when distinct topic emerges
- Convert file→directory only when exceeding 400 lines

## Workflow: Updating Existing Documentation

### Before Creating New File, Ask:

1. **Does this belong in existing file?** → Update that file
2. **Is this results/analysis of existing work?** → Append to existing file
3. **Is this truly a new distinct topic?** → Create new file
4. **Is existing file approaching 400 lines?** → Plan split

### Appending to Existing Files

**Good workflow:**
```markdown
# Initial file creation
## Hypothesis
[Written before experiment]

# After running experiment, append:
## Results
[Appended to same file]

# After analysis, append:
## Learnings
[Appended to same file]

# After insights, append:
## Next Steps
[Appended to same file]
```

### When to Split Files

Only split when:
- File exceeds 400 lines
- File has 3+ distinct major topics (each 100+ lines)
- Topics could be independently useful

## Integration with Project Patterns

### Bible Study Tools

```
bible-study-tools/{tool-name}/
├── README.md (≤200 lines)             # Tool overview, schema, sources
│   ## Purpose
│   ## Research Methodology
│   [Read detailed experiments →](experiments.md)
│   ## Output Schema
│   ## Validation
│
└── experiments.md (≤400 lines)        # All experimental work
    ## Experiment 001
    [Hypothesis → Method → Results → Learnings - all in one section]

    ## Experiment 002
    [Next iteration based on 001 learnings]
```

**Only create experiments/ directory if experiments.md exceeds 400 lines.**

### TBTA Features

```
plan/tbta/features/{feature}/
├── README.md                          # Feature overview with links
│   ## Definition
│   ## Language Distribution
│   [Read validation →](validation.md)
│   [Read patterns →](patterns.md)
│
├── validation.md                      # All validation experiments
└── patterns.md                        # Pattern analysis
```

### Language Research

```
plan/languages/{family}/
├── README.md                          # Family overview
│   ## Overview
│   ## Key Characteristics
│   ## Languages in This Family
│   [Read translation challenges →](translation-challenges.md)
│
├── translation-challenges.md          # Challenges analysis
└── {language-code}.md                 # Individual language (if needed)
```

## Common Mistakes to Avoid

### ❌ Mistake 1: Pre-creating Empty Files

**Don't:**
```bash
touch hypothesis.md method.md results.md analysis.md learnings.md
```

**Do:**
```markdown
# experiment-001.md

## Hypothesis
[Write this section]

[Later, append:]
## Method
[Write this section]

[Later, append:]
## Results
[Write this section]
```

### ❌ Mistake 2: File Spam

**Don't:**
```
notes-2024-01-15.md
notes-2024-01-16.md
notes-2024-01-17.md
random-thoughts.md
more-thoughts.md
```

**Do:**
```
research-notes.md (update daily with dated sections)
```

### ❌ Mistake 3: Generic Subfile Lists

**Don't:**
```markdown
## Subfiles
- file1.md
- file2.md
- file3.md
```

**Do:**
```markdown
## Clusivity
[Key findings...]
[Link to details]

## Obviation
[Key findings...]
[Link to details]
```

### ❌ Mistake 4: Breaking Single Work Across Files

**Don't:**
```
experiment-hypothesis.md
experiment-method.md
experiment-results.md
experiment-analysis.md
```

**Do:**
```
experiment.md (with all sections in one file)
```

### ❌ Mistake 5: QUICK-REFERENCE.md Separate File

**Don't:**
```
README.md (comprehensive)
QUICK-REFERENCE.md (short version)
```

**Do:**
```
README.md (make it the quick reference - ≤200 lines)
```

## Line Count Checks

```bash
# Check specific file
wc -l README.md

# Check all markdown in directory
wc -l *.md

# Find files over 400 lines
find . -name "*.md" -exec wc -l {} \; | awk '$1 > 400 {print $2 " has " $1 " lines (OVER LIMIT)"}'

# Find READMEs over 200 lines
find . -name "README.md" -exec wc -l {} \; | awk '$1 > 200 {print $2 " has " $1 " lines (OVER LIMIT)"}'
```

## When in Doubt

**Ask these questions:**

1. **Does README contain all essential info?**
   - If no → improve README
   - If yes → good!

2. **Can someone understand topic reading just README?**
   - If no → add more summary to README
   - If yes → good!

3. **Are subfiles truly necessary or just spam?**
   - Necessary → distinct topics, detailed analysis
   - Spam → results of same work, different days' notes

4. **Does each section in README link to details?**
   - If no → add links
   - If yes → good!

5. **Am I creating new file or updating existing?**
   - Default to updating
   - Create only if truly distinct

## Summary

Progressive disclosure for markdown docs:
- ✅ README.md ≤200 lines (the quick reference)
- ✅ Topic files ≤400 lines (detailed analysis)
- ✅ Topic sections in README with links (not "Subfiles" list)
- ✅ Nested directories only when needed
- ✅ Update existing files before creating new ones
- ✅ One file per distinct work (append sections, don't split)
- ✅ Use `[text](path.md)` links not aliases
- ❌ Don't spam directories with many small files
- ❌ Don't create QUICK-REFERENCE.md (README is the quick reference)
- ❌ Don't split single experiments across multiple files

**Goal:** Token-efficient, navigable documentation where README gives you everything you need, with optional deep dives available via links.
