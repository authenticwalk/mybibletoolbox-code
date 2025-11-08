# Improve Strong's - Skill Documentation

## Quick Start

**Invoke this skill by saying:** "Let's improve strongs"

## What This Skill Does

Manages systematic implementation of Strong's word enrichment across three complementary initiatives:

1. **Lexical Research** - Etymology, scholarly analysis (7 tools)
2. **TBTA Hints** - Grammatical patterns from 900+ translations
3. **Cultural Translation** - Handling non-existent concepts

## How It Works

### Focused Grouping Approach

Instead of loading all tasks at once (which would fill your context), this skill:
- **Identifies** the next logical grouping of work
- **Loads** only that grouping's todos
- **Guides** systematic execution
- **Archives** completed work to plan files
- **Moves** to the next grouping when ready

### Example Groupings

**Lexical Research - Tool 1:**
- Grouping A: Research phase (3 documents)
- Grouping B: Experimentation phase (5 test cases) ← **Current suggested focus**
- Grouping C: Validation phase
- Grouping D: Production phase (scale to 50 words)

**TBTA Hints:**
- Grouping A: Proof-of-concept (3 pronouns, 20 verses)
- Grouping B: Measure accuracy improvement
- Grouping C: Scale to high-value words

**Cultural Translation:**
- Grouping A: Tool creation
- Grouping B: Data access setup
- Grouping C: Pilot expansion (10-20 words)

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

**Suggested Next Grouping:** Tool 1 Experimentation
1. Run Experiment 1: High-frequency word (G846 αὐτός)
2. Run Experiment 2: Medium-frequency theological (G1411 δύναμις)
3. Run Experiment 3: Rare word (<10 occurrences)
4. Run Experiment 4: Hebrew word (H430 Elohim)
5. Run Experiment 5: Word family (agape/phileo)
6. Validate results against quality checklist
7. Document learnings

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
1. Check current status
2. Load Tool 1 experiment todos (suggested next grouping)
3. Guide you through experiments

### Continue after a break:
```
You: "Continue improving strongs"
```

The skill will:
1. Check active todos
2. Resume where you left off
3. Or offer to switch groupings if complete

### Switch to different initiative:
```
You: "Let's work on TBTA hints for strongs"
```

The skill will:
1. Archive current lexical todos
2. Load TBTA hints proof-of-concept todos
3. Guide implementation

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

**Remember:** This skill keeps you focused on ONE grouping at a time, preventing context overload while systematically working through the comprehensive Strong's enrichment strategy.
