---
name: progressive-disclosure
description: Organize complex research, planning, and learning documentation using progressive disclosure - a hierarchical pattern where high-level READMEs summarize details in subfiles, which expand into nested directories when they grow beyond limits. Use for TBTA features, language research, tool creation, or any multi-layered knowledge work.
---

# Progressive Disclosure Documentation

## Overview

Progressive disclosure is an industry-standard documentation pattern that organizes information hierarchically, revealing detail on demand. This skill helps you structure complex research, experiments, and learnings so they remain token-efficient and navigable at any depth.

**Core Principle:** Every level contains all essential information (README.md), with optional deeper detail in subfiles/subdirectories. You can stop reading at any level and have complete knowledge at that depth.

## When to Use This Skill

Use progressive disclosure for:
- **TBTA feature research** - Features → experiments → individual test cases
- **Language research** - Language families → individual languages → specific grammatical features
- **Bible study tool creation** - Tool overview → experiments → revisions → learnings
- **Planning complex tasks** - High-level plan → task breakdowns → implementation details
- **Any growing knowledge base** - When documentation exceeds token-efficient sizes

## Documentation Structure Rules

### The 200/400 Rule

**Rule:** Files grow until they hit limits, then split into directories with their own README.

| Level | Type | Max Lines | Content |
|-------|------|-----------|---------|
| Top | README.md | 200 lines | Overview of entire domain, list of all subfiles with 1-2 line descriptions |
| Sub | {topic}.md | 400 lines | Detailed content on one topic, references to parent README summary |
| Deep | {topic}/README.md | 200 lines | Overview when topic.md exceeded 400 lines |
| Deeper | {topic}/{subtopic}.md | 400 lines | Specific details of subtopic |

### File Naming Conventions

```
./{domain}/
├── README.md                           # 200 lines max - overview of domain
├── {topic-1}.md                        # 400 lines max - details on topic 1
├── {topic-2}.md                        # 400 lines max - details on topic 2
└── {topic-3}/                          # Created when topic-3.md hit 400 lines
    ├── README.md                       # 200 lines max - overview of topic 3
    ├── {subtopic-3a}.md               # 400 lines max - details on subtopic
    ├── {subtopic-3b}.md               # 400 lines max - details on subtopic
    └── {subtopic-3c}/                 # Created when 3c.md hit 400 lines
        ├── README.md                   # 200 lines max - overview of subtopic 3c
        └── {detail-3c-i}.md           # 400 lines max - specific detail
```

### Real Examples from This Project

#### TBTA Feature: Person Systems
```
plan/tbta-project-local/features/person-systems/
├── README.md                          # Overview of person systems in translation
├── LEARNINGS.md                       # Key discoveries (could become dir if >400)
├── QUICK-REFERENCE.md                 # Practical guide
├── BIBLE-EXAMPLES.md                  # Annotated examples
└── ebible-analysis.md                 # Analysis of specific corpus
```

#### When person-systems grows further:
```
plan/tbta-project-local/features/person-systems/
├── README.md                          # Still 200 lines - updated overview
├── clusivity/                         # LEARNINGS.md hit 400 lines, became dir
│   ├── README.md                      # Summary of clusivity findings
│   ├── GEN-001-026.md                # Detailed analysis of Genesis 1:26
│   ├── MAT-006-009.md                # Lord's Prayer clusivity analysis
│   └── language-patterns.md          # Patterns by language family
├── obviation/                         # Similarly expanded
│   └── README.md
└── QUICK-REFERENCE.md                # Still a file, under 400 lines
```

## Core Principles

### 1. Upward Propagation

**Rule:** Changes in subfiles must update parent READMEs.

When you:
- Complete an experiment in `experiments/clusivity/GEN-001-026.md`
- Must update `experiments/clusivity/README.md` to reflect findings
- Must update `experiments/README.md` to note completion status
- May update `features/person-systems/README.md` if findings are significant

**Implementation:**
- Track which files changed in your session
- Before committing, check parent README(s)
- Update summary sections to reflect new learnings
- Keep parent README line count under 200

### 2. Executive Summaries

**Rule:** When a file becomes a directory, its original summary moves to the new README.md and becomes the "executive summary" section.

**Before (file growing too large):**
```markdown
# person-systems.md (450 lines - too long!)

Person systems vary across languages with features like clusivity...

## Detailed Analysis
[300 lines of details]
```

**After (converted to directory):**
```markdown
# person-systems/README.md (180 lines)

## Executive Summary
Person systems vary across languages with features like clusivity...
[This matches what was in parent README]

## Overview
This directory contains research on person systems in Bible translation.

## Subfiles
- clusivity.md - Inclusive/exclusive distinctions
- obviation.md - Fourth person systems
- number-systems.md - Dual, trial, plural distinctions

## Key Findings
[Summary of discoveries across all subfiles]
```

**Subfiles start with parent context:**
```markdown
# person-systems/clusivity.md

> **Parent Context:** Person systems vary across languages with features like
> clusivity, obviation, and complex number systems.

## Focus: Clusivity in Bible Translation

[400 lines of detailed analysis]
```

### 3. Token Efficiency

**Rule:** Users should be able to load just what they need.

**Levels of detail:**
1. **Scan level** - Top README.md (200 lines) - "What exists here?"
2. **Working level** - Specific topic file (400 lines) - "What do I need to know?"
3. **Deep dive level** - Subdirectory (multiple files) - "What are all the details?"

**For AI agents:**
- Load parent README first
- Determine which subfiles are relevant
- Load only those subfiles
- Never load entire tree unless explicitly needed

### 4. Self-Contained Context

**Rule:** Every file must make sense on its own.

**Bad:**
```markdown
# experiment-002.md
We tried the same approach but with 10 verses.
Results were better than before.
```

**Good:**
```markdown
# experiment-002.md

> **Parent Context:** Testing clusivity prediction in Genesis using LLM analysis
> of Greek source text. Previous experiment (001) achieved 70% accuracy on 5 verses.

## Experiment: Expanded verse set (10 verses)

**Hypothesis:** More context improves accuracy
**Method:** Same prompt structure, expanded to 10 consecutive verses
**Result:** 85% accuracy (improved from 70%)

[Detailed analysis]
```

## Workflow

### Creating New Documentation Structure

#### Step 1: Start with README.md
```markdown
# {domain}/README.md

## Overview
[2-3 sentences on what this domain covers]

## Scope
[What's included, what's not]

## Current Status
[Empty, in progress, completed]

## Subfiles
[None yet]
```

#### Step 2: Add First Details
Create `{topic}.md` files as you research:
- Keep focused on one topic
- Start simple, grow organically
- Don't pre-create empty files

#### Step 3: Monitor Line Counts
As files approach limits:
- **Approaching 200 (README)** - Consider if any topics can be extracted to subfiles
- **Approaching 400 (topic file)** - Plan to convert to directory structure

#### Step 4: Convert File → Directory
When `topic.md` exceeds 400 lines:

```bash
# 1. Create directory
mkdir {topic}

# 2. Extract sections to subfiles
# Split content into logical subtopics

# 3. Create new README
# Move high-level summary from topic.md to topic/README.md

# 4. Update parent README
# Reflect that {topic} is now a directory
```

#### Step 5: Update Parents
After any significant change:
```markdown
# Parent README update checklist:
- [ ] Updated subfile list with new files
- [ ] Updated key findings with discoveries
- [ ] Updated status if work completed
- [ ] Kept under 200 lines
```

### Working Within Existing Structure

#### Step 1: Read Parent README
```markdown
# Understand context:
- What is the scope of this domain?
- What subfiles exist?
- What has been learned so far?
```

#### Step 2: Navigate to Relevant Subfile
```markdown
# Load only what you need:
- For specific topic: Read {topic}.md
- For subtopic: Read {topic}/{subtopic}.md
- For overview: Stay at parent README
```

#### Step 3: Make Changes
```markdown
# Add content to appropriate level:
- New experiment results → experiments/{feature}/experiment-00X.md
- New learning → features/{feature}/LEARNINGS.md
- New subtopic → create new {subtopic}.md file
```

#### Step 4: Propagate Upward
```markdown
# Update chain:
1. Complete work in deepest file
2. Update immediate parent README
3. Update grandparent README if significant
4. Stop when change is no longer significant to parent
```

## Integration with Existing Patterns

### Replacing/Updating Old Patterns

This progressive disclosure pattern **replaces** the following in this project:
- ❌ Creating `LEARNINGS.md` at root of tool directories (keep them, but follow 400-line rule)
- ❌ Experiment files without clear parent structure
- ❌ Massive single-file documentation (>400 lines)
- ❌ Summary files in project root (use `/plan/{task-name}/README.md`)

This pattern **incorporates and improves**:
- ✅ Learning loops from tool-experimenter (learnings propagate up)
- ✅ Experiment tracking (experiments are subfiles with clear structure)
- ✅ Self-improvement systems (findings update parent READMEs)

### Bible Study Tools Integration

For tool creation, structure becomes:
```
bible-study-tools/{tool-name}/
├── README.md                          # 200 lines - tool overview, schema, sources
├── experiments/                       # All experimental work
│   ├── README.md                      # Experiment overview, results summary
│   ├── experiment-001/                # First major experiment
│   │   ├── README.md                  # Experiment goals, findings
│   │   ├── method.md                  # Detailed methodology
│   │   ├── results.md                 # Raw results and analysis
│   │   └── learnings.md               # What we learned, what to change
│   └── experiment-002/                # Second experiment incorporating learnings
│       └── ...
└── LEARNINGS.md                       # Cumulative learnings (→ dir if >400 lines)
```

**Key change:** Experiments directory has its own README showing experiment history and cumulative results, making it easy to see evolution without loading everything.

### TBTA Features Integration

Already well-aligned! The merged code follows this pattern:
```
plan/tbta-project-local/
├── README.md                          # Project overview, status, key results
├── features/                          # All feature research
│   ├── FEATURE-SUMMARY.md            # Quick reference across features
│   └── person-systems/                # One feature
│       ├── README.md                  # Feature overview
│       └── LEARNINGS.md              # Discoveries (could become dir)
└── experiments/                       # All experiments
    ├── FRAMEWORK.md                   # How experiments work
    └── person-systems/                # Experiments for one feature
        └── experiment-001.md          # Specific test
```

## Common Patterns

### Pattern 1: Research → Discovery → Integration

**Stage 1: Initial Research**
```
research-topic/
└── README.md (50 lines) - "Started researching X"
```

**Stage 2: Growing Knowledge**
```
research-topic/
├── README.md (150 lines) - Updated with initial findings
├── source-analysis.md (200 lines) - Analysis of key sources
└── initial-patterns.md (180 lines) - Patterns discovered
```

**Stage 3: Deep Investigation**
```
research-topic/
├── README.md (200 lines) - Comprehensive overview
├── source-analysis/                   # source-analysis.md hit 400 lines
│   ├── README.md
│   ├── source-type-1.md
│   └── source-type-2.md
├── patterns/                          # initial-patterns.md hit 400 lines
│   ├── README.md
│   ├── pattern-family-1.md
│   └── pattern-family-2.md
└── applications.md (300 lines) - How to use findings
```

### Pattern 2: Experiment Series

**Structure:**
```
experiments/{feature-name}/
├── README.md                          # Experiment history, best methods
├── experiment-001.md                  # First attempt
├── experiment-002.md                  # Refinement based on 001 learnings
├── experiment-003.md                  # Further refinement
└── FINAL-METHOD.md                    # Production-ready approach
```

**experiment-001.md format:**
```markdown
# Experiment 001: [Short description]

> **Parent Context:** [Feature being tested, project goals]

## Hypothesis
[What we think will happen]

## Method
[What we're testing]

## Results
[What happened]

## Learnings
[What we discovered, what to change next]

## Next Steps
[What experiment-002 should try]
```

### Pattern 3: Language Family Research

**Structure:**
```
languages/{family-name}/
├── README.md                          # Family overview, key characteristics
├── {language-code}.md                 # Individual language details (max 400)
└── {language-code}/                   # If language details >400 lines
    ├── README.md                      # Language overview
    ├── phonology.md                   # Detailed phonology
    ├── grammar.md                     # Detailed grammar
    └── bible-translation.md           # Translation-specific notes
```

## Best Practices

### Do:
- ✅ Create files organically as content emerges
- ✅ Keep README files under 200 lines strictly
- ✅ Keep subfiles under 400 lines strictly
- ✅ Update parent READMEs when subfiles change significantly
- ✅ Include parent context at start of subfiles
- ✅ Use descriptive filenames (not file1.md, file2.md)
- ✅ Add subfile descriptions to parent README
- ✅ Keep directory depths reasonable (usually max 3-4 levels)

### Don't:
- ❌ Pre-create empty files "for later"
- ❌ Let files exceed line limits
- ❌ Create files without updating parent README
- ❌ Duplicate content across multiple files
- ❌ Write content assuming reader has loaded all previous files
- ❌ Create deeply nested structures (>5 levels) unless truly necessary
- ❌ Use this pattern for simple, single-file documentation

## Line Count Guidelines

### How to Count Lines

```bash
# Count lines in a file
wc -l {file}.md

# Check all markdown files in directory
wc -l *.md

# Find files over limit
find . -name "*.md" -exec wc -l {} \; | awk '$1 > 400 {print $2, $1}'
```

### What Counts as Lines

- ✅ All content lines (text, headers, lists)
- ✅ Code blocks and examples
- ✅ Blank lines for spacing
- ❌ YAML frontmatter (--- delimited)
- ❌ Commented-out sections for AI only

**Why these limits?**
- 200 lines ≈ 3000-4000 tokens (efficient for overview)
- 400 lines ≈ 6000-8000 tokens (comprehensive detail without overload)
- Humans can read 200 lines in 5-10 minutes
- AI agents can load 400 lines with plenty of token budget remaining

## Migration Guide

### Converting Existing Documentation

If you have existing documentation that doesn't follow this pattern:

#### Step 1: Assess Current Structure
```bash
# Find all markdown files
find . -name "*.md" -type f

# Check line counts
find . -name "*.md" -exec wc -l {} \; | sort -n
```

#### Step 2: Identify Violations
- Files >400 lines → Need to become directories
- Directories without README.md → Need README creation
- Parent READMEs >200 lines → Need compression/extraction

#### Step 3: Prioritize Conversions
Focus on:
1. Most-used documentation first
2. Actively growing areas
3. Areas with >500 line files (severe violations)

#### Step 4: Convert Systematically
For each oversized file:
1. Create directory with same name
2. Create README.md with overview (extract from original)
3. Split content into logical subfiles
4. Update parent README to reflect new structure
5. Commit with message: "refactor: convert {name} to progressive disclosure structure"

## Examples from Project

### Example 1: TBTA Person Systems (Already Good!)

```
plan/tbta-project-local/features/person-systems/
├── README.md (237 lines) - ⚠️ Slightly over, but acceptable
├── LEARNINGS.md (164 lines) - ✅ Good
├── QUICK-REFERENCE.md (164 lines) - ✅ Good
└── BIBLE-EXAMPLES.md (186 lines) - ✅ Good
```

**Status:** Well-structured! Each file is self-contained. If README.md grows past 250 lines or BIBLE-EXAMPLES grows past 400, consider splitting.

### Example 2: Converting Large File

**Before:**
```
plan/research/language-systems.md (850 lines) - ❌ Too large!
```

**After:**
```
plan/research/language-systems/
├── README.md (180 lines)              # Overview + findings summary
├── clusivity-systems.md (350 lines)   # One major topic
├── number-systems.md (280 lines)      # Another major topic
└── case-systems.md (240 lines)        # Third major topic
```

### Example 3: Growing Organically

**Week 1:**
```
plan/new-feature/
└── README.md (80 lines) - Initial exploration
```

**Week 2:**
```
plan/new-feature/
├── README.md (120 lines) - Updated with findings
└── initial-experiment.md (200 lines) - First test
```

**Week 3:**
```
plan/new-feature/
├── README.md (180 lines) - Comprehensive overview
├── experiments/
│   ├── README.md (60 lines) - Experiment tracking
│   ├── experiment-001.md (200 lines)
│   └── experiment-002.md (250 lines)
└── findings.md (180 lines) - Key discoveries
```

## Troubleshooting

### "My README is at 195 lines and I need to add more!"

**Options:**
1. Compress existing content (use bullet points, remove redundancy)
2. Extract details to new subfile
3. Move less critical info to subfile, keep summary in README
4. Accept 205 lines if truly necessary (guidelines, not prison)

### "I have 10 subfiles and the parent README list is huge!"

**Solution:** Use categorization:
```markdown
## Subfiles

### Core Documentation
- overview.md - Project scope and goals
- methodology.md - How we do this work

### Experiments (5 files)
- experiments/ - See experiments/README.md for full list

### Reference (3 files)
- See reference/README.md for detailed source materials
```

### "My topic needs 600 lines of detailed explanation!"

**Solution:** It's a directory, not a file:
```
topic/
├── README.md (200 lines) - Overview with key points
├── part-1.md (400 lines) - First major section
└── part-2.md (200 lines) - Second major section
```

### "Changes in deep files require updating 4 parent READMEs!"

**Solution:** Only propagate significant changes:
- Small bug fix in deep file → Update immediate parent only
- New discovery → Update 2 levels up
- Major breakthrough → Update to top level

Use judgment on what's "significant enough" to propagate.

## Summary

Progressive disclosure documentation:
- **Organizes knowledge hierarchically** - README → subfiles → subdirectories
- **Keeps content token-efficient** - 200/400 line limits
- **Makes information findable** - Clear structure, descriptive names
- **Propagates learnings upward** - Changes update parent summaries
- **Grows organically** - Start simple, expand as needed
- **Works across domains** - TBTA, languages, tools, planning

**Remember:** This is about making complex knowledge navigable and maintainable, not about rigid rules. Use judgment, prioritize clarity, and adjust as needed.

---

**When in doubt:**
1. Can someone understand the domain by reading just the README? (If no, improve README)
2. Can someone find specific details easily? (If no, improve structure)
3. Is any file over 400 lines? (If yes, split it)
4. Is any README over 200 lines? (If yes, extract to subfiles)
