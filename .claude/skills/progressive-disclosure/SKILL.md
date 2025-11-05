---
name: progressive-disclosure
description: Use for all .md file creation/editing. README ≤200 lines (self-contained overview), topic files ≤400 lines. Plan ahead - if content will exceed limits, create directory structure from start.
---

# Progressive Disclosure for Markdown Documentation

## Core Principle

**README is self-contained** - Contains all essential information, with optional links to details.

Not an index. Not a table of contents. A complete overview where you can stop reading and understand everything at that level.

## The Rules

### 1. File Limits
- README.md: **≤200 lines** - Complete overview
- {topic}.md: **≤400 lines** - Detailed content on ONE topic
- **Plan ahead:** If content will exceed limits, create directory structure from start

### 2. Anti-Spam Rule
**Before creating new file, ask:**
1. Does this belong in existing file? → **Update it**
2. Is this results of work already started? → **Append to that file**
3. Only create new file for **distinct new topic**

### 3. README Structure Rule
**Use topic sections with key findings + links** (NOT generic "Subfiles:" lists)

✅ Do this:
```markdown
## Clusivity

Inclusive/exclusive "we" distinctions affect 200+ languages. Austronesian languages
almost universally exhibit clusivity (kita/kami pattern). Validated: 100% accuracy.

[Read detailed analysis →](clusivity.md)
```

❌ Not this:
```markdown
## Subfiles
- clusivity.md
- obviation.md
```

### 4. Link Format Rule
Use `[text](file.md)` - NOT aliases (aliases auto-import, breaking token efficiency)

## Decision Tree: Creating Files

```
New content to add
    ↓
Can this go in existing file?
    ↓ YES → UPDATE that file
    ↓ NO
    ↓
Can this go in README?
    ↓ YES (README < 150 lines) → ADD to README
    ↓ NO
    ↓
Estimate content size
    ↓
Will this exceed 400 lines?
    ↓ YES → CREATE directory structure:
    |       mkdir {topic}/
    |       Create {topic}/README.md (overview)
    |       Create {topic}/{subtopic}.md files
    ↓ NO
    ↓
CREATE {topic}.md file
```

**Key:** Estimate BEFORE creating. Never create file knowing it will exceed 400 lines.

## Templates

### README.md Template

```markdown
# {Topic Name}

{2-3 sentence overview}

## {Subtopic 1}

{KEY FINDINGS - 2-4 sentences with actual insights, not just "see file"}

**Status:** {done/in progress}

[Read detailed analysis →]({subtopic-1}.md)

## {Subtopic 2}

{KEY FINDINGS}

**Status:** {status}

[Read detailed analysis →]({subtopic-2}.md)
```

**Rules:**
- Essential findings IN readme (don't force clicking)
- Links for DETAILS, not basic understanding
- Under 200 lines total

### Topic File Template

```markdown
# {Topic}

> **Parent Context:** {1 sentence from parent README}

{Introduction}

## {Section 1}

{Content}

## Summary

{Key takeaways}
```

### Experiment Template (All in ONE file)

```markdown
# Experiment 001: {Title}

## Hypothesis
{What you think}

## Method
{How you test}

## Results
{What happened} ← APPEND after running

## Learnings
{What you learned} ← APPEND after analyzing

## Next Steps
{What's next} ← APPEND after reflecting
```

**Do NOT create:** hypothesis.md, method.md, results.md separately!

## Common Patterns

### Pattern 1: Simple Feature Research

```
features/person-systems/
├── README.md (overview + findings for each topic)
├── clusivity.md
└── obviation.md
```

**README.md:**
```markdown
# Person Systems

Person systems (clusivity, obviation, number) affect 200+ languages.

## Clusivity

Inclusive/exclusive "we" distinctions. Universal in Austronesian languages.
Validated: 100% accuracy on 12 verses.

[Read detailed analysis →](clusivity.md)

## Obviation

Fourth person systems. Common in Algic languages.
Framework complete, needs validation.

[Read detailed analysis →](obviation.md)
```

### Pattern 2: Nested (when clusivity.md would exceed 400 lines)

```
features/person-systems/
├── README.md
├── clusivity/              # Started as directory (content >400 lines)
│   ├── README.md           # Clusivity overview
│   ├── validation.md       # All validation experiments
│   └── patterns.md         # Language patterns
└── obviation.md            # Still under 400 lines
```

**clusivity/validation.md** - NOT individual verse files!
```markdown
# Clusivity Validation

## Divine Speaker Verses

### Genesis 1:26 "Let us make mankind"
Prediction: Exclusive
Results: Indonesian kami ✓, Tagalog kami ✓

### Genesis 3:22 "Man has become like us"
[same format]

## Apostolic Authority Verses
[grouped verses]

## Summary
84 predictions, 84 correct (100%)
```

### Pattern 3: Experiments

```
experiments/aspect/
├── README.md
├── experiment-001.md  # Hypothesis → Method → Results → Learnings (all in one)
└── experiment-002.md
```

**experiment-001.md:**
```markdown
# Experiment 001: Basic Aspect

## Hypothesis
Aspect predictable from morphology

## Method
20 verbs from John 1

## Results
70% accuracy. Failed on perfect aspect.

## Learnings
- Aorist: 100% accurate
- Perfect needs semantic context
- Changes for 002: add context window
```

### Pattern 4: Bible Study Tools

```
bible-study-tools/cultural-context/
├── README.md (≤200 lines)
│   ## Purpose
│   ## Experiments
│   {Summary with findings}
│   [Read experiments →](experiments.md)
│   ## Schema
└── experiments.md (≤400 lines)
    ## Experiment 001
    {Hypothesis → Method → Results → Learnings}
```

Only create `experiments/` directory if experiments.md exceeds 400 lines.

## Anti-Patterns

### ❌ File Spam
```
experiments/
├── experiment-001-hypothesis.md
├── experiment-001-results.md
└── experiment-001-learnings.md
```
✅ Correct: `experiment-001.md` (all sections in one file)

### ❌ Random Verse Files
```
clusivity/
├── GEN-001-026.md
├── MAT-006-009.md
```
✅ Correct: `validation.md` (organized verse sections)

### ❌ Generic Subfile Lists
```markdown
## Subfiles
- file1.md
- file2.md
```
✅ Correct: Topic sections with findings + links

### ❌ QUICK-REFERENCE.md
```
├── README.md (long)
└── QUICK-REFERENCE.md (short)
```
✅ Correct: README IS the quick reference (≤200 lines)

### ❌ Creating Oversized Files
```
Agent: "I'll create validation.md with 622 lines, then note it should be a directory"
```
✅ Correct: Estimate first. If >400 lines, create `validation/` directory from start

## Workflow

### Creating New Documentation

1. **Start simple:** Create directory with minimal README.md
2. **Grow README:** Add content directly as you learn
3. **Before adding more:** Will README exceed 200 lines?
   - YES → Extract to topic file, summarize in README with link
   - NO → Keep adding to README
4. **Before creating topic file:** Will it exceed 400 lines?
   - YES → Create directory structure instead
   - NO → Create topic.md file

### Estimating File Size

**Before creating topic file:**
- Count major sections planned
- Estimate lines per section
- Add 20% buffer for growth

**Examples:**
- 3 sections × 100 lines = 300 lines → Create file ✓
- 5 sections × 100 lines = 500 lines → Create directory ✗
- Unsure? → Create file, watch line count, convert if approaching 400

### Converting File to Directory

If topic.md approaches 400 lines:

1. Create `topic/` directory
2. Create `topic/README.md` with overview
3. Split content into `topic/{subtopic}.md` files
4. Update parent README link

## Quick Reference

**Creating markdown? Ask:**

1. Can this go in existing file? → **UPDATE** it
2. Is README under 150 lines? → **ADD** to README
3. Is related file under 300 lines? → **ADD** to that file
4. Creating new topic file - will it exceed 400 lines? → **CREATE DIRECTORY** instead
5. Otherwise → **CREATE FILE**

**README must have:**
- ✅ Essential findings (not just links)
- ✅ Topic sections with key info + links
- ✅ Under 200 lines
- ❌ NOT just a file list
- ❌ NO "Subfiles:" section

**File creation:**
- ✅ Plan ahead - estimate size first
- ✅ One distinct topic = one file
- ✅ Append sections as work progresses
- ✅ Update existing before creating new
- ❌ NO oversized files (>400 lines)
- ❌ NO separate files for parts of same work
- ❌ NO file spam
