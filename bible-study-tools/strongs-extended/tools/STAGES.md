[TODO: I stubbed this in from other places, I need you to go though and research all our strongs data in /plan and find all the best work we did on process and what processes we developed that made great results]
[TODO: I need you to look at ../tbta/features/STAGES.md and see if there are any useful techniques we can use from there, not all will be relevant but that may really help us]

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