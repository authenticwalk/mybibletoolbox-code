# TODO Investigation Report

## TODOs Resolved

### TODO #1 (Line 157): ATTRIBUTION.md Usage
**Status**: ✅ RESOLVED

**Original Issue**: ATTRIBUTION.md was being used as a dumping ground instead of strategic source documentation.

**Solution Implemented**:
- Added clarification in STAGES.md Step 4
- **URL-templatable sources** → ATTRIBUTION.md (BibleHub, StudyLight, Blue Letter Bible, etc.)
- **One-off sources** → Bottom of individual YAML file (specific articles, blog posts)

**Location**: `/workspaces/mybibletoolbox-code/bible-study-tools/tbta/features/STAGES.md` lines 169-170

### TODO #2 (Line 541): Timeline Estimates
**Status**: ✅ RESOLVED (Prevention)

**Original Issue**: User reported unwanted timeline estimates appearing in documentation.

**Investigation Results**:

**GOOD NEWS**: STAGES.md has ZERO timeline content!
- File line count: 476 lines (under 600 limit)
- No "timeline", "time estimate", "hours", "weeks", "months" found in file

**Source of Timeline Instructions Found**:

1. **`.claude/agents/core/planner.md`**
   - Line 10: `timeline_estimation` capability
   - Line 31: "Timeline Creation: Estimate realistic timeframes for task completion"
   - This is a PLANNER agent - appropriate for project planning contexts

2. **`.claude/skills/tool-experimenter/SKILL.md`**
   - Line 689: "## Expected Timeline" section
   - Lines 692+: Detailed time estimates (1-2 hours, etc.)
   - This skill is specifically for tool experimentation with time tracking

**Analysis**:
- Timeline instructions are NOT in CLAUDE.md or CLAUDE-FLOW.md (core project guidance)
- Timeline instructions are ONLY in agent/skill files for specific planning contexts
- These are appropriate for their use cases (project planning, experiment tracking)

**Recommendation**:
- NO CHANGES NEEDED to agent/skill files
- Timeline estimates are contextually appropriate in those specific roles
- User's STAGES.md file never had timeline content to remove
- Issue may have been from a different file or different context

**Prevention**:
- If timeline estimates appear in TBTA feature documentation in the future:
  - Check if planner agent was invoked unnecessarily
  - Verify tool-experimenter skill isn't being applied to wrong context
  - Remind agents that TBTA feature work ≠ time-tracked experiments

## Git Commit
- Commit: a7bb4bb - "docs(tbta): clarify ATTRIBUTION.md usage for templatable vs one-off sources"
- Pushed to: tbta-docs-foundation branch

## Summary
- TODO #1: RESOLVED with documentation clarification
- TODO #2: NO ACTION NEEDED (file already clean, sources identified)
- File quality: 476 lines, well under 600-line limit
