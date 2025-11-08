---
name: improve-strongs
description: Systematically implement Strong's word enrichment following the comprehensive strategy. Manages focused work on lexical research, TBTA hints, and cultural translation without context overload. Use when user wants to work on Strong's enrichment tasks.
---

# Improve Strong's Words

## Overview

This skill guides systematic implementation of the Strong's Word Enhancement comprehensive strategy, which enriches all 14,197 Strong's words with three complementary data types:

1. **Lexical Research** (what it means) - Etymology, scholarly analysis, controversies
2. **TBTA Hints** (how to say it) - Grammatical patterns from 900+ translations
3. **Cultural Translation** (what to say) - Handling non-existent concepts and cultural gaps

The skill maintains a master todo list and breaks work into focused groupings to prevent context overload.

## Master Plan Reference

**Primary Strategy Document:** `/plan/strongs-comprehensive-strategy.md`

### The Three Initiatives

```
┌─────────────────────────────────────────────────────────────┐
│                    Strong's Word Entry                       │
│                   (e.g., G26 ἀγάπη "love")                   │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼

┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  Lexical Data    │  │  TBTA Hints      │  │ Cultural Adapt   │
│  (What it means) │  │  (How to say it) │  │ (What to say)    │
└──────────────────┘  └──────────────────┘  └──────────────────┘
```

**Related Planning Documents:**
- `/plan/strongs-enrichment-tools/` - 7 lexical enrichment tools (Tool 1 complete)
- `/plan/strongs-enrichment-sources/` - Source discovery strategies
- `/plan/tbta-strongs-hints-summary.md` - TBTA hints overview
- `/plan/strongs-cultural-translation/` - Cultural translation challenges

## When to Use

Use this skill when:
- User says "let's improve strongs" or similar
- User wants to work on Strong's word enrichment
- User needs guidance on next steps for Strong's implementation
- User asks about Strong's enrichment progress or status

Do NOT use when:
- User just wants to look up a Strong's number (use get-source-languages skill)
- User is quoting Bible verses (use quote-bible skill)
- User is studying specific verses (use scripture-study skill)

## How This Skill Works

### Step 1: Read Current Plan and Context

First, load the comprehensive strategy to understand the current state:

```bash
# Read the master strategy
cat plan/strongs-comprehensive-strategy.md
```

Also check current implementation status:
- Tool 1 (lexicon-core) documentation: `/plan/strongs-enrichment-tools/01-lexicon-core/`
- TBTA hints status (analysis complete, proof-of-concept ready)
- Cultural translation status (planning complete, pilot samples done)

### Step 2: Present Current Status

Show the user:
- What's been completed
- What's in progress
- What's next in the queue
- Current focus area

### Step 3: Identify Focus Grouping

Break work into focused groupings to avoid context overload:

#### Initiative 1: Lexical Research - 7 Tools
**Groupings:**
1. Tool 1: lexicon-core (HIGH authority - HELPS, Thayer's, BDB, BDAG, LSJ)
2. Tool 2: lexicon-expert (MEDIUM authority - StudyLight, expert blogs)
3. Tool 3: lexicon-community (LOW authority - forums, Reddit)
4. Tool 4: scholarly-papers (Academic research)
5. Tool 5: etymology-deep (Diachronic analysis)
6. Tool 6: translation-patterns (TBTA cross-linguistic)
7. Tool 7: synthesis (Merge all sources)

**For each tool, work through:**
- Research phase (source inventory, extraction methods, convergence patterns)
- Experimentation phase (5 test cases)
- Validation phase (quality checklist, theological review)
- Production phase (scale to high-value words)

#### Initiative 2: TBTA Hints
**Groupings:**
1. Proof-of-concept: 3 pronouns, 20 verses, measure accuracy
2. High-value pronouns: All personal pronouns (G/H)
3. Demonstratives: Near/far distinctions
4. High-frequency particles
5. Scale to top 300 words

#### Initiative 3: Cultural Translation
**Groupings:**
1. Tool creation (following TEMPLATE.md)
2. Data access setup (TBTA corpus)
3. Pilot expansion (10-20 high-challenge words)
4. Category development (animals, natural phenomena, abstracts)
5. Scale to top 300 words

### Step 4: Create/Update Master Todo List

Use the TodoWrite tool to maintain a focused todo list for the CURRENT GROUPING ONLY.

**Important:** Only include todos for one grouping at a time. When that grouping is complete, archive it and load the next grouping.

### Step 5: Execute Current Grouping

Work through the todos systematically:
- Mark each todo as in_progress before starting
- Complete work following established patterns
- Mark as completed immediately after finishing
- Update plan files with learnings

### Step 6: Archive and Move to Next

When a grouping is completed:
1. Update the comprehensive strategy with status
2. Document learnings in the tool's directory
3. Clear completed todos
4. Load next grouping's todos
5. Brief the user on what's next

## Master Todo List Structure

The full implementation has many phases. Break them into groupings:

### Current Status (as of last update)

**Completed:**
- ✅ Comprehensive strategy document
- ✅ Source discovery strategies (10 methods)
- ✅ Implementation plan for 7 tools
- ✅ Tool 1 (lexicon-core) complete documentation
  - Research phase documents (3 files)
  - Experiment designs (5 test cases)
  - Output schema
  - Validation criteria
- ✅ Cultural translation planning
  - Comprehensive methodology
  - Pilot samples (3 words)

**Current Focus: Tool 1 Experimentation Phase**

Suggested next grouping todos:
1. Run Experiment 1: High-frequency word (G846 αὐτός)
2. Run Experiment 2: Medium-frequency theological (G1411 δύναμις)
3. Run Experiment 3: Rare word (<10 occurrences)
4. Run Experiment 4: Hebrew word (H430 Elohim)
5. Run Experiment 5: Word family (agape/phileo)
6. Validate experimental results against quality checklist
7. Document learnings and refine methodology

### Future Groupings Queue

**Lexical Research:**
- Tool 1 validation phase
- Tool 1 production phase (top 50 words)
- Tool 2 (expert sources) research → experiments → validation
- Tools 3-7 following same pattern

**TBTA Hints:**
- Proof-of-concept implementation
- Accuracy measurement
- Decision point: proceed or stop
- Scale to high-value words

**Cultural Translation:**
- Create Bible study tool README
- Setup TBTA corpus access
- Expand pilot to 10-20 words
- Build extraction pipeline

## Working Principles

### Context Management
- **One grouping at a time** - Don't load all 7 tools' todos at once
- **Archive completed work** - Move to plan files, clear from active todos
- **Subagent decomposition** - Use Task tool for large operations
- **Progressive disclosure** - Keep READMEs <200 lines, topics <400 lines

### Quality Standards
- **No fabrication** - All data from documented sources
- **Inline citations** - Every claim cited (e.g., {thayer} {bdag})
- **Fair use compliance** - Convergence grouping, divergence in context
- **3-level validation** - CRITICAL (100%), HIGH (80%+), MEDIUM (60%+)

### Bible Study Tool Integration

When experiments are successful and ready for production, create proper Bible study tools:

1. Use the `bible-study-tool-creator` skill
2. Follow `/bible-study-tools/TEMPLATE.md`
3. 3-phase structure: data extraction → analysis → validation
4. Self-learning loops for continuous improvement

## Examples

### Example 1: Starting Strong's Enrichment Work

**User:** "Let's improve strongs"

**Skill Actions:**
1. Read `/plan/strongs-comprehensive-strategy.md`
2. Check status of all 3 initiatives
3. Identify that Tool 1 documentation is complete, experiments are next
4. Load Tool 1 experiment todos (5 experiments + validation)
5. Present status and ask which experiment to start with
6. Execute chosen experiment following methodology

### Example 2: Continuing After Break

**User:** "Let's continue improving strongs"

**Skill Actions:**
1. Check current todos (if any exist)
2. Read comprehensive strategy for context
3. Present what was last worked on
4. Offer to continue or switch groupings
5. Load appropriate todos and proceed

### Example 3: Switching Initiatives

**User:** "Let's work on TBTA hints instead"

**Skill Actions:**
1. Archive current lexical research todos to plan files
2. Read TBTA hints summary and status
3. Load TBTA hints proof-of-concept todos
4. Present the 3 pronouns + 20 verses approach
5. Guide implementation

## Error Handling

**If plan files are missing:**
- Alert user that comprehensive strategy is required
- Ask if they want to recreate it

**If context gets too full:**
- Archive current progress to plan files
- Create subagent for large operations
- Summarize status in comprehensive strategy

**If experiments fail:**
- Document failures in tool's experiments/ directory
- Update methodology based on learnings
- Revise validation criteria if needed

## Integration with Other Skills

**Works with:**
- `bible-study-tool-creator` - Create production tools from experiments
- `tool-experimenter` - Refine existing tools
- `get-source-languages` - Access Strong's data for experiments
- `quote-bible` - Get verse context for word studies

**Complements:**
- `scripture-study` - Enriched Strong's data improves verse commentary
- TBTA features - Strong's hints connect to linguistic features

## Technical Notes

### File Locations

**Plans:**
- `/plan/strongs-comprehensive-strategy.md` - Master overview
- `/plan/strongs-enrichment-tools/` - Lexical research (7 tools)
- `/plan/strongs-enrichment-sources/` - Source discovery
- `/plan/strongs-cultural-translation/` - Cultural challenges
- `/plan/tbta-strongs-hints-*.md` - TBTA hints analysis (5 files)

**Data:**
- `.data/bible/words/strongs/(H|G){num:04d}/` - Base Strong's files (14,197)
- Output pattern: `{num}.strongs-{tool}.yaml`

**Tools (when created):**
- `/bible-study-tools/strongs-*/` - Production tools

### Output Schema

Each tool produces YAML following this pattern:

```yaml
strongs_number: G1411
lemma: δύναμις
source: {tool-name}

# Tool-specific content
lexical_data:
  etymology: "..."
  semantic_range: [...]
  convergence: "..."

# Always include
metadata:
  generated_date: "2025-11-08"
  sources_consulted: [...]
  validation_level: "high"
```

## Success Metrics

### For Lexical Research
- ✅ 5+ lexicons consulted per word
- ✅ All claims cited with inline sources
- ✅ No fabrication/hallucination
- ✅ Fair use compliance verified

### For TBTA Hints
- ✅ +7% overall accuracy improvement
- ✅ +25% edge case accuracy
- ✅ Patterns validated across 50+ languages
- ✅ Confidence scores calibrated

### For Cultural Challenges
- ✅ Real solutions from documented translations
- ✅ Multiple language families per word
- ✅ Theological impact assessed
- ✅ Both successful AND unsuccessful approaches documented

## Next Steps Reference

See comprehensive strategy timeline:
- **Immediate (Weeks 1-4):** Tool 1 experiments, TBTA proof-of-concept, cultural tool creation
- **Short-term (Months 2-3):** Expand to top 50 words across all initiatives
- **Medium-term (Months 4-6):** Scale to top 300 words
- **Long-term (Months 7-12):** Continue based on priority, community contribution

---

**Remember:** Focus on ONE GROUPING at a time. Complete it fully before moving to the next. Document learnings. Maintain quality standards. Use subagents to protect context.
