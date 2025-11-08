# Improve Strong's - Skill Documentation

## Quick Start

**Invoke this skill by saying:** "Let's improve strongs"

## What This Skill Does

Manages systematic implementation of Strong's word enrichment across three complementary initiatives:

1. **Lexical Research** - Etymology, scholarly analysis (7 tools)
2. **TBTA Hints** - Grammatical patterns from 900+ translations
3. **Cultural Translation** - Handling non-existent concepts

## How It Works

### Single-Tool-to-Completion Methodology

**CRITICAL PRINCIPLE:** Take ONE tool to full production readiness before starting the next.

Instead of spreading effort across multiple tools, this skill:
- **Focuses** on a single tool until it reaches production quality
- **Iterates** through at least 7 improvement cycles (or until diminishing returns)
- **Refines** prompts and context engineering systematically
- **Validates** through peer review and quality checks
- **Documents** all learnings before moving to next tool

### The 7+ Cycle Improvement Process

For each tool (e.g., lexicon-core):

**Cycle 1: Initial Implementation**
- Run 5 diverse experiments (high-freq, medium-freq, rare, Hebrew, word family)
- Generate initial outputs following schema
- Document what works and what fails

**Cycle 2: Prompt Refinement**
- Identify common failure patterns from Cycle 1
- Refine extraction prompts for better accuracy
- Test on same 5 words, compare results
- Measure improvement

**Cycle 3: Context Engineering**
- Optimize information passed to extraction prompts
- Add/remove context based on Cycle 2 learnings
- Test again, measure improvement

**Cycle 4: Edge Case Handling**
- Focus on specific failure modes (rare words, controversies, etc.)
- Create targeted improvements
- Validate edge case handling

**Cycle 5: Schema Refinement**
- Adjust output structure based on what worked
- Ensure fair use compliance
- Optimize for downstream consumption

**Cycle 6: Peer Review**
- Use subagent to review outputs as an external evaluator
- Identify subtle issues (fabrication, citation gaps, theological errors)
- Implement feedback

**Cycle 7: Production Validation**
- Run validation checklist (Level 1/2/3)
- Measure success metrics
- Document final methodology

**Cycle 8+: Continue if significant improvement possible**
- Stop when improvements <5% per cycle
- Diminishing returns = ready for production

### Current Focus: Tool 1 (Lexicon-Core)

**Status:** Experimentation phase (Cycle 1) ready to begin

**Next Steps:**
1. Run 5 initial experiments
2. Document learnings
3. Begin improvement cycles 2-7+
4. Reach production readiness
5. ONLY THEN move to Tool 2

## Current Status

As of 2025-11-08:

**Completed:**
- ✅ Comprehensive strategy document
- ✅ Source discovery strategies (10 methods)
- ✅ Implementation plan for 7 lexical tools
- ✅ Tool 1 (lexicon-core) complete documentation
  - Research phase (3 documents)
  - Experiment designs (5 test cases)
  - Output schema
  - Validation criteria
- ✅ Cultural translation planning
  - Comprehensive methodology
  - Pilot samples (3 words: agape, snow, lamb)

**Current Tool:** lexicon-core (Tool 1 of 7)
**Current Cycle:** 1 (Initial Implementation)

**This Cycle's Tasks:**
1. Run Experiment 1: High-frequency word (G846 αὐτός)
2. Run Experiment 2: Medium-frequency theological (G1411 δύναμις)
3. Run Experiment 3: Rare word (<10 occurrences)
4. Run Experiment 4: Hebrew word (H430 Elohim)
5. Run Experiment 5: Word family (agape/phileo)
6. Document learnings and failure patterns
7. Prepare for Cycle 2 (Prompt Refinement)

## Key Planning Documents

The skill references these files:
- `/plan/strongs-comprehensive-strategy.md` - Master overview
- `/plan/strongs-enrichment-tools/` - 7 lexical tools (Tool 1 complete)
- `/plan/strongs-enrichment-sources/` - Source discovery methods
- `/plan/strongs-cultural-translation/` - Cultural challenges
- `/plan/tbta-strongs-hints-summary.md` - TBTA hints overview

## Quality Standards

The skill enforces:
- **No fabrication** - All data from documented sources
- **Inline citations** - Every claim cited (e.g., {thayer} {bdag})
- **Fair use compliance** - Convergence grouping, divergence in context
- **3-level validation** - CRITICAL (100%), HIGH (80%+), MEDIUM (60%+)

## Integration with Other Skills

**Creates production tools using:**
- `bible-study-tool-creator` - When experiments are validated

**Works alongside:**
- `get-source-languages` - Access Strong's data
- `tool-experimenter` - Refine existing tools
- `quote-bible` - Get verse context

## Usage Examples

### Start working on Strong's enrichment:
```
You: "Let's improve strongs"
```

The skill will:
1. Check current tool and cycle status
2. Load current cycle's todos
3. Execute experiments/improvements systematically
4. Document learnings
5. Iterate through 7+ cycles until production ready

### Continue after a break:
```
You: "Continue improving strongs"
```

The skill will:
1. Check which cycle you're on
2. Resume current cycle's work
3. Show progress through the 7+ cycle improvement process

### See improvement metrics:
```
You: "Show me the improvement metrics for lexicon-core"
```

The skill will:
1. Compare outputs across cycles
2. Show quality score trends
3. Identify if diminishing returns reached (ready for production)

## The Single-Tool Focus

**Important:** This skill will NOT move to Tool 2 (lexicon-expert), TBTA hints, or cultural translation until Tool 1 (lexicon-core) reaches production quality through 7+ improvement cycles.

**Why this approach:**
- Prevents spreading effort too thin
- Allows deep learning from one tool before applying to next
- Ensures production-quality output before scaling
- Each tool's learnings inform the next tool's design

## Success Metrics

### Lexical Research
- ✅ 5+ lexicons consulted per word
- ✅ No fabrication/hallucination
- ✅ Fair use compliance

### TBTA Hints
- ✅ +7% overall accuracy
- ✅ +25% edge case accuracy
- ✅ Patterns validated across 50+ languages

### Cultural Translation
- ✅ Real solutions from documented translations
- ✅ Multiple language families represented
- ✅ Theological impact assessed

## Timeline

- **Immediate (Weeks 1-4):** Tool 1 experiments, TBTA proof-of-concept
- **Short-term (Months 2-3):** Expand to top 50 words
- **Medium-term (Months 4-6):** Scale to top 300 words
- **Long-term (Months 7-12):** Continue based on priority

---

**Remember:** This skill focuses on ONE tool at a time, taking it through 7+ improvement cycles to production quality before moving to the next tool. This prevents spreading effort too thin and ensures each tool reaches excellence through systematic iteration and refinement.
