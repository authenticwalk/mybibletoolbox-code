# Wizard Architecture - Bible Study Tool Creator Enhancement

**Architecture Date:** 2025-11-14
**Architect:** System Architecture Designer
**Status:** Design Complete - Ready for Implementation
**Project:** myBibleToolbox - Interactive Tool Creation System

---

## Executive Summary

### Strategic Decision: Enhance, Not Rebuild

**Recommendation:** Enhance the existing `bible-study-tool-creator` skill rather than building new.

**Rationale:**
1. **Proven Pattern**: Existing wizard successfully uses AskUserQuestion for progressive disclosure
2. **Complete Infrastructure**: File generation, validation, and registration already implemented
3. **Integration Ready**: Already integrated with TEMPLATE.md, STANDARDIZATION.md, tool-registry.yaml
4. **Risk Mitigation**: Enhancement leverages battle-tested code vs. new development risk
5. **Time Efficiency**: 80% of needed functionality already exists and working

**Enhancement Focus Areas:**
- Improved validation and duplicate detection
- Better example generation and quality assessment
- Enhanced schema definition workflow
- Streamlined integration with tool-experimenter skill
- Clearer decision flow for similar tools

---

## Architecture Decision Records (ADRs)

### ADR-001: Enhance Existing Wizard vs. Build New

**Status:** Accepted

**Context:**
- Existing wizard at `.claude/skills/bible-study-tool-creator/SKILL.md` implements full tool creation workflow
- Research shows wizard is functional but could benefit from refinement
- Project follows "prefer editing over creating new files" principle

**Decision:** Enhance existing wizard with focused improvements

**Consequences:**
- ✅ Faster implementation (weeks vs. months)
- ✅ Preserves institutional knowledge in existing code
- ✅ Maintains consistency with established patterns
- ✅ Reduces testing burden
- ❌ Constrained by existing architecture (acceptable trade-off)

---

### ADR-002: Progressive Questioning Pattern

**Status:** Accepted

**Context:**
- Claude Code has AskUserQuestion tool for interactive workflows
- Project emphasizes progressive disclosure (README ≤200 lines, topics ≤400 lines)
- Users need guidance without overwhelming context

**Decision:** Maintain one-question-at-a-time flow with AskUserQuestion tool

**Consequences:**
- ✅ Clear user experience
- ✅ Manageable context windows
- ✅ Natural conversation flow
- ✅ Easy to interrupt and resume
- ❌ Slightly longer total time (acceptable for quality)

---

### ADR-003: File Generation via Python Script

**Status:** Accepted

**Context:**
- Existing `init-tool.py` script generates complete tool structure
- YAML definition file (`/tmp/tool-definition.yaml`) serves as single source of truth
- Template-based generation ensures consistency

**Decision:** Maintain Python script approach with enhanced templates

**Consequences:**
- ✅ Consistent file structure across all tools
- ✅ Single source of truth (YAML definition)
- ✅ Easy to version and test templates
- ✅ Clear separation: data gathering (wizard) → file generation (script)
- ⚠️ Requires Python in environment (already present)

---

### ADR-004: Tool Registry Integration

**Status:** Accepted

**Context:**
- `tool-registry.yaml` serves as central registry for all tools
- `scripture-study` skill uses registry to determine file inclusion
- Scope (core/standard/comprehensive) determines query depth inclusion

**Decision:** Make registry registration mandatory step in wizard

**Consequences:**
- ✅ All tools automatically discoverable
- ✅ Clear categorization (scope + category)
- ✅ Integration with scripture-study skill
- ✅ Prevents orphaned tools
- ⚠️ Registry must be kept in sync (validation needed)

---

## System Architecture

### High-Level Component Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│                    (Claude Code + Terminal)                     │
└───────────────────────┬─────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                  BIBLE STUDY TOOL CREATOR                       │
│                    (Enhanced Wizard Skill)                      │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐      │
│  │ Intent       │  │ Validation   │  │ Example         │      │
│  │ Discovery    │──│ & Duplicate  │──│ Generation      │      │
│  │              │  │ Detection    │  │                 │      │
│  └──────────────┘  └──────────────┘  └─────────────────┘      │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐      │
│  │ Schema       │  │ Tool         │  │ Registry        │      │
│  │ Definition   │──│ Generation   │──│ Registration    │      │
│  │              │  │              │  │                 │      │
│  └──────────────┘  └──────────────┘  └─────────────────┘      │
└───────────────────────┬─────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                    TOOL DEFINITION BUILDER                      │
│                  (Assembles /tmp/tool-definition.yaml)          │
└───────────────────────┬─────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                     FILE GENERATION ENGINE                      │
│                        (init-tool.py)                           │
│                                                                 │
│  Input: /tmp/tool-definition.yaml                              │
│  Output: Complete tool directory structure                     │
└───────────────────────┬─────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                      PROJECT INTEGRATION                        │
│                                                                 │
│  • bible-study-tools/{tool-name}/                              │
│  • tool-registry.yaml (updated)                                │
│  • Integration with tool-experimenter skill                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Component Architecture

### 1. Intent Discovery Component

**Purpose:** Understand what tool the user wants to create

**Inputs:**
- User's initial description (may be empty)
- Existing tool directory listing
- Related tool README files

**Process:**
1. Check if user provided intent when invoking skill
2. If not, brainstorm 3-4 valuable tool ideas
3. Present options via AskUserQuestion
4. Capture user's response
5. Search for existing similar tools
6. If similar tools found, offer choice: edit existing or create new

**Outputs:**
- Clear tool intent description
- Confirmation that this is a new tool (not duplicate)
- Decision on whether to proceed or enhance existing

**Key Files:**
- `.claude/skills/bible-study-tool-creator/steps/step-discover-intent.md`

**Enhancement Opportunities:**
- Better duplicate detection (semantic similarity, not just name matching)
- Suggest related tools even if not exact duplicates
- Provide examples of successful similar tools

---

### 2. Validation & Duplicate Detection Component

**Purpose:** Prevent duplicate work and ensure tool meets quality bar

**Inputs:**
- Tool intent description
- List of existing tools in `bible-study-tools/`
- Each existing tool's README.md

**Process:**
1. List all directories in `bible-study-tools/`
2. For potential matches, read README.md
3. Compare goals, purpose, and scope
4. If match found, present options:
   - Work on existing tool
   - Explain how new tool is unique
   - Cancel and rethink

**Outputs:**
- Validation pass/fail
- List of similar tools (if any)
- User decision on how to proceed

**Validation Criteria:**
- Not a duplicate of existing tool
- Singular focus (not trying to do too much)
- Clear foreach scope (verse/chapter/book/word/topic)
- Grouped by purpose, not by source
- Specific enough to be actionable
- Broad enough to be useful

**Enhancement Opportunities:**
- Automated similarity scoring (keyword matching)
- Show tool relationship graph
- Suggest tool composition (combine existing tools vs. create new)

---

### 3. Example Generation Component

**Purpose:** Create 5 concrete examples that justify the tool's existence

**Inputs:**
- Tool intent description
- Access to web resources (WebSearch, WebFetch)
- ATTRIBUTION.md for source URLs

**Process:**
1. Research and generate 5 high-value examples
2. Present each example ONE AT A TIME via AskUserQuestion
3. Ask user to rate each example
4. Collect feedback and refine if needed
5. Append validated examples to tool YAML

**Outputs:**
- 5 validated examples with:
  - Context (what verse/scenario)
  - Insight (what was discovered)
  - Value (why it matters for target audience)
- User rating for each example

**Quality Criteria:**
- Specific and concrete (not generic)
- Shows clear practical value
- Demonstrates how tool helps translators/pastors/students
- Covers diverse verse types (narrative, poetry, doctrine, etc.)

**Enhancement Opportunities:**
- Use WebSearch to find real-world examples
- Check ATTRIBUTION.md for optimized URL patterns
- Suggest example refinements based on quality metrics
- Auto-validate examples against REVIEW-GUIDELINES.md Level 1

---

### 4. Schema Definition Component

**Purpose:** Define the YAML structure for tool output

**Inputs:**
- User description of desired data structure
- SCHEMA.md standard patterns
- Examples from similar tools

**Process:**
1. Ask user to describe YAML structure
2. Provide guidance with examples from SCHEMA.md
3. Create two versions:
   - `data_structure`: Complete example with sample data
   - `yaml_structure_inline`: Concise field hierarchy
4. Validate against SCHEMA.md standards
5. Ensure inline citation format `{source-id}`

**Outputs:**
- Complete YAML schema example
- Concise field hierarchy
- Validation that schema follows standards

**Standard Sections (from SCHEMA.md):**
- Required: `verse` field in `BOOK.chapter.verse` format
- Optional: `source`, `words`, `clusters`, `patterns`, `theological`, `grammatical`
- Citation format: `"content {source-id}"`

**Enhancement Opportunities:**
- Schema validation against SCHEMA.md
- Auto-suggest standard fields based on tool category
- Show examples from similar tools
- Validate citation format compliance

---

### 5. Tool Generation Component

**Purpose:** Generate complete tool directory structure

**Inputs:**
- Consolidated tool definition YAML (`/tmp/tool-definition.yaml`)
- Templates from skill directory

**Process:**
1. Build tool definition YAML with all collected data
2. Execute `init-tool.py` script
3. Generate files:
   - README.md (tool overview, goals, examples)
   - LEARNING.md (experiment log)
   - {tool-name}-template.md (agent prompt template)
   - tests/README.md (test framework)

**Outputs:**
- Complete tool directory at `bible-study-tools/{tool-name}/`
- All required files populated with collected data
- Proper file structure per project standards

**File Structure:**
```
bible-study-tools/{tool-name}/
├── README.md                    # Tool overview
├── LEARNING.md                  # Experiment log
├── {tool-name}-template.md      # Agent prompt
└── tests/
    └── README.md                # Test framework
```

**Enhancement Opportunities:**
- Template validation before generation
- Pre-flight check for directory conflicts
- Generate initial test cases
- Create example output YAML

---

### 6. Registry Registration Component

**Purpose:** Register tool in central tool-registry.yaml

**Inputs:**
- Tool name and description
- User input on scope and category

**Process:**
1. Ask user about scope (core/standard/comprehensive)
2. Ask user about category (lexical/theological/practical/historical/linguistic/topical)
3. Add entry to `tool-registry.yaml`
4. Validate YAML syntax
5. Confirm registration

**Outputs:**
- Updated `tool-registry.yaml` with new tool entry
- Validation that file is valid YAML
- Integration confirmation

**Registry Entry Format:**
```yaml
{tool-suffix}:
  name: {Tool Name}
  summary: {Brief description - max 20 words}
  scope: {core|standard|comprehensive}
  category: {lexical|theological|practical|historical|linguistic|topical}
```

**Scope Definitions:**
- **core**: Essential data, small files (~1-50 KB), always included
- **standard**: Standard research, moderate files (~50-500 KB), medium+ queries
- **comprehensive**: Exhaustive data, large files (>500 KB), full queries only

**Enhancement Opportunities:**
- Auto-suggest scope based on expected data size
- Auto-suggest category based on tool intent
- Validate summary length (≤20 words)
- Check for naming conflicts

---

## Data Flow

### Step-by-Step Data Flow Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│ START: User invokes bible-study-tool-creator skill              │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│ Step 1: Discover Intent                                         │
│                                                                  │
│ Input:  User description (may be empty)                         │
│ Check:  Did user provide intent?                                │
│   YES → Capture intent                                          │
│   NO  → Brainstorm ideas, AskUserQuestion                       │
│ Output: Clear tool intent                                       │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│ Step 2: Check for Duplicates                                    │
│                                                                  │
│ Action: ls -la bible-study-tools/                               │
│ For each existing tool:                                         │
│   - Read README.md                                              │
│   - Compare goals/purpose                                       │
│ If similar found:                                               │
│   AskUserQuestion: Edit existing or explain uniqueness?         │
│ Output: Validation pass + decision to proceed                   │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│ Step 3: Suggest Tool Name                                       │
│                                                                  │
│ Input:  Tool intent                                             │
│ Generate: 2-3 name suggestions (kebab-case)                     │
│ Ask:    AskUserQuestion with name options                       │
│ Create: bible-study-tools/{tool-name}/{tool-name}.yaml          │
│ Output: Tool name confirmed, initial YAML created               │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│ Step 4: Create 5 Examples (ONE AT A TIME)                       │
│                                                                  │
│ For i = 1 to 5:                                                 │
│   Research → Generate example                                   │
│   AskUserQuestion: Present example, request rating              │
│   Collect feedback                                              │
│   Append to {tool-name}.yaml                                    │
│ Output: 5 validated examples with ratings                       │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│ Step 5: Define Output Structure                                 │
│                                                                  │
│ Ask: Describe YAML structure (with guidance)                    │
│ Create:                                                          │
│   - data_structure (complete example with sample data)          │
│   - yaml_structure_inline (concise field hierarchy)             │
│ Validate: Against SCHEMA.md standards                           │
│ Output: Complete schema definition                              │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│ Step 6: Select Test Verse                                       │
│                                                                  │
│ Ask: AskUserQuestion with verse options                         │
│   - JHN 3:16 (familiar baseline)                                │
│   - MAT 5:3 (theological depth)                                 │
│   - GEN 1:1 (ancient context)                                   │
│   - PSA 23:1 (poetry)                                           │
│   - Other (specify)                                             │
│ Output: Test verse reference                                    │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│ Step 7: Build Tool Definition YAML                              │
│                                                                  │
│ Consolidate all data into /tmp/tool-definition.yaml:            │
│   - tool_name, tool_name_kebab, task_name                       │
│   - description                                                  │
│   - test_verse                                                   │
│   - goals_formatted                                              │
│   - examples_formatted                                           │
│   - data_structure                                               │
│   - yaml_structure_inline                                        │
│ Output: Complete YAML definition file                           │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│ Step 8: Run Initialization Script                               │
│                                                                  │
│ Execute: python3 init-tool.py /tmp/tool-definition.yaml         │
│ Creates:                                                         │
│   - bible-study-tools/{tool-name}/README.md                     │
│   - bible-study-tools/{tool-name}/LEARNING.md                   │
│   - bible-study-tools/{tool-name}/{tool-name}-template.md       │
│   - bible-study-tools/{tool-name}/tests/README.md               │
│ Output: Complete tool directory structure                       │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│ Step 9: Register in Tool Registry                               │
│                                                                  │
│ Ask: Scope (core/standard/comprehensive)                        │
│ Ask: Category (lexical/theological/practical/etc.)              │
│ Edit: bible-study-tools/tool-registry.yaml                      │
│ Add entry:                                                       │
│   {tool-suffix}:                                                │
│     name: {Tool Name}                                           │
│     summary: {Brief description}                                │
│     scope: {scope}                                              │
│     category: {category}                                        │
│ Output: Updated registry                                        │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│ Step 10: Update Related Tools (if applicable)                   │
│                                                                  │
│ If related tools exist:                                         │
│   - Update their README.md to cross-reference new tool          │
│   - Summarize learnings from related tools' LEARNING.md         │
│ Output: Cross-references established                            │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│ Step 11: Confirm Creation                                       │
│                                                                  │
│ Display summary:                                                 │
│   ✅ Tool created: {tool-name}                                  │
│   ✅ Files created (list)                                       │
│   ✅ Registry updated                                           │
│   Next steps:                                                    │
│     1. Review generated files                                   │
│     2. Customize template                                       │
│     3. Run first test                                           │
│     4. Document learnings                                       │
│     5. Test integration with scripture-study                    │
│ Output: Confirmation message                                    │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│ END: Tool ready for experimentation with tool-experimenter      │
└──────────────────────────────────────────────────────────────────┘
```

---

## Integration Points

### 1. TEMPLATE.md Integration

**Purpose:** Ensure generated tools follow project template structure

**Integration Method:**
- `init-tool.py` uses TEMPLATE.md as blueprint for README.md generation
- All standard sections from TEMPLATE.md included in generated README
- Custom sections populated with wizard-collected data

**Key Sections:**
- Purpose, Research Methodology, Output Schema
- Output Validation (Level 1-3 requirements)
- Quality Metrics, Examples, Challenges

**Validation:**
- Generated README must be ≤500 lines (per progressive-disclosure)
- All required sections present
- Schema matches STANDARDIZATION.md conventions

---

### 2. STANDARDIZATION.md Integration

**Purpose:** Ensure naming conventions and formats are correct

**Integration Method:**
- Tool name must be kebab-case
- Book codes follow USFM 3.0 (MAT, JHN, GEN)
- Language codes follow ISO-639-3 (eng, grc, heb)
- File paths follow directory structure standards

**Validation Points:**
- Tool name format validation
- Test verse reference format (BOOK.chapter.verse, zero-padded)
- Citation format (`{source-id}`)
- Directory structure compliance

---

### 3. SCHEMA.md Integration

**Purpose:** Ensure YAML output structure follows project standards

**Integration Method:**
- Schema definition step references SCHEMA.md patterns
- Inline citation format enforced: `"content {source-id}"`
- Required field: `verse: BOOK.chapter.verse`
- Optional standard sections suggested based on tool category

**Validation Points:**
- `verse` field present and properly formatted
- Citations use inline format (not separate fields)
- Standard sections used when applicable
- Custom fields don't conflict with standard names

---

### 4. tool-registry.yaml Integration

**Purpose:** Make tool discoverable by scripture-study skill

**Integration Method:**
- Mandatory registration step in wizard
- User provides scope and category
- Entry added to `tools:` section
- YAML syntax validated

**Registry Structure:**
```yaml
tools:
  {tool-suffix}:
    name: {Tool Name}
    summary: {Brief description - max 20 words}
    scope: {core|standard|comprehensive}
    category: {lexical|theological|practical|historical|linguistic|topical}
```

**Query Depth Mapping:**
- Light queries → Include `core` tools only
- Medium queries → Include `core` + `standard` tools
- Full queries → Include `core` + `standard` + `comprehensive` tools

---

### 5. tool-experimenter Skill Integration

**Purpose:** Enable rapid iteration after tool creation

**Integration Method:**
- Tool created by wizard → Passed to tool-experimenter for 50+ experiments
- LEARNING.md populated with experiment results
- Successful patterns identified and documented
- Tool refined based on learnings

**Workflow:**
```
wizard → tool creation → tool-experimenter → 50+ experiments →
production-ready tool
```

**Data Flow:**
- Wizard creates initial structure
- Tool-experimenter populates LEARNING.md
- Patterns documented in README.md
- Quality metrics refined through iteration

---

## File Structure

### Generated Tool Directory

```
bible-study-tools/{tool-name}/
│
├── README.md                        # Main tool documentation (≤500 lines)
│   ├── Purpose
│   ├── Research Methodology
│   │   ├── Phase 1: Data Extraction
│   │   ├── Phase 2: Analysis and Synthesis
│   │   └── Phase 3: Citation and Verification
│   ├── Output Schema
│   │   ├── Filename Format
│   │   └── YAML Structure
│   ├── Output Validation
│   │   ├── Level 1: CRITICAL (100%)
│   │   ├── Level 2: HIGH PRIORITY (80%+)
│   │   └── Level 3: MEDIUM PRIORITY (60%+)
│   ├── Quality Metrics
│   ├── Examples of Stellar Outputs (5 examples)
│   ├── Common Challenges and Solutions
│   └── Research Guidelines for Bible-Researcher Agent
│
├── LEARNING.md                      # Experiment log (populated by tool-experimenter)
│   ├── Experiment tracking
│   ├── Pattern discoveries
│   ├── Quality improvements
│   └── Integration learnings
│
├── {tool-name}-template.md          # Agent prompt template
│   ├── System prompt for Bible-Researcher agent
│   ├── Research methodology instructions
│   ├── Output format requirements
│   └── Validation checklist
│
└── tests/
    └── README.md                    # Test framework documentation
        ├── Test case structure
        ├── Validation criteria
        └── Expected outputs
```

### Wizard Working Files

```
.claude/skills/bible-study-tool-creator/
│
├── SKILL.md                         # Main skill definition
│
├── steps/                           # Step-by-step guides
│   ├── step-discover-intent.md
│   ├── step-suggest-tool-name.md
│   ├── step-create-examples.md
│   └── [other steps]
│
├── templates/                       # File templates
│   ├── README.template.md
│   ├── LEARNING.template.md
│   ├── tool-template.template.md
│   └── test-README.template.md
│
└── init-tool.py                     # File generation script
```

### Temporary Working Files

```
/tmp/
└── tool-definition.yaml             # Consolidated tool definition
    ├── tool_name
    ├── tool_name_kebab
    ├── task_name
    ├── description
    ├── test_verse
    ├── goals_formatted
    ├── examples_formatted
    ├── data_structure
    └── yaml_structure_inline
```

---

## Key Design Decisions

### 1. One Question at a Time

**Decision:** Use AskUserQuestion for every user input, one question at a time

**Rationale:**
- Prevents overwhelming user with multiple questions
- Allows for natural conversation flow
- Easy to interrupt and resume
- Aligns with progressive disclosure principle
- Reduces cognitive load

**Implementation:**
- Each step explicitly uses AskUserQuestion
- No free-text questions in wizard dialogue
- Options always provided when possible
- "Other" option for custom input

---

### 2. Search-First Approach

**Decision:** Always search for existing tools before creating new

**Rationale:**
- Prevents duplicate work
- Surfaces opportunities to enhance existing tools
- Encourages composition over creation
- Maintains tool ecosystem coherence

**Implementation:**
- Directory listing of `bible-study-tools/`
- README.md reading for potential matches
- User decision on proceed/edit/cancel
- Suggestions for related tools

---

### 3. Example-Driven Validation

**Decision:** Require 5 concrete examples before proceeding

**Rationale:**
- Examples justify the tool's existence
- Demonstrates practical value for target audience
- Provides clarity on tool scope and output
- Prevents vague or low-value tools

**Implementation:**
- Each example presented individually
- User rating/feedback collected
- Examples appended to tool YAML
- Quality criteria validated

---

### 4. Schema-First Design

**Decision:** Define YAML schema before generating tool structure

**Rationale:**
- Clear output contract established early
- Prevents scope creep during implementation
- Enables validation against SCHEMA.md
- Provides concrete target for researchers

**Implementation:**
- User describes desired structure
- Wizard validates against SCHEMA.md
- Both complete and concise versions created
- Schema embedded in README.md

---

### 5. Mandatory Registry Integration

**Decision:** Make tool-registry.yaml registration a required step

**Rationale:**
- Ensures all tools are discoverable
- Enables scripture-study integration
- Enforces categorization discipline
- Prevents orphaned tools

**Implementation:**
- Scope and category questions
- Automated YAML entry generation
- Syntax validation
- Immediate integration with scripture-study

---

## Enhancement Opportunities

### High Priority Enhancements

#### 1. Improved Duplicate Detection

**Current State:** Simple directory listing and README comparison

**Enhancement:**
- Semantic similarity scoring (keyword matching)
- Automatic suggestion of related tools
- Relationship graph visualization
- Composition vs. creation guidance

**Implementation Approach:**
- Extract keywords from tool descriptions
- Calculate similarity scores
- Rank by relevance
- Present as "Related Tools" section

---

#### 2. Schema Validation

**Current State:** Manual schema definition with examples

**Enhancement:**
- Real-time validation against SCHEMA.md
- Auto-suggest standard fields by category
- Citation format validation
- Example schema from similar tools

**Implementation Approach:**
- Parse SCHEMA.md to extract standard patterns
- Validate user-provided schema
- Highlight violations
- Suggest corrections

---

#### 3. Quality Metrics

**Current State:** User provides examples, no automated quality check

**Enhancement:**
- Automated quality scoring for examples
- Validation against REVIEW-GUIDELINES.md Level 1
- Citation format checking
- Token estimation for file size

**Implementation Approach:**
- Parse examples for required elements
- Check citation format compliance
- Estimate tokens using rough heuristics
- Flag potential issues before generation

---

### Medium Priority Enhancements

#### 4. Tool Composition Guidance

**Current State:** Binary choice: create new or edit existing

**Enhancement:**
- Suggest composing multiple existing tools
- Identify tool chains (output → input)
- Recommend tool combinations
- Show integration examples

---

#### 5. Test Case Generation

**Current State:** Empty tests/README.md generated

**Enhancement:**
- Auto-generate test cases based on examples
- Create expected output YAML
- Define validation criteria
- Provide test verse coverage guidance

---

#### 6. Integration with WebSearch

**Current State:** Manual example creation

**Enhancement:**
- Auto-search for real-world examples
- Check ATTRIBUTION.md for optimized URLs
- Suggest sources based on tool category
- Validate source authority levels

---

## Risk Analysis and Mitigation

### Risk 1: User Abandons Wizard Mid-Flow

**Likelihood:** Medium
**Impact:** Medium
**Mitigation:**
- Save progress to `/tmp/tool-definition.yaml` after each step
- Provide resume capability
- Clear progress indicators
- Allow skip/come-back-later for non-critical steps

---

### Risk 2: Generated Files Don't Match TEMPLATE.md

**Likelihood:** Low
**Impact:** High
**Mitigation:**
- Template-based generation ensures consistency
- Validation against TEMPLATE.md structure
- Progressive disclosure enforcement (≤500 lines)
- Automated section presence checks

---

### Risk 3: Tool Registry Gets Out of Sync

**Likelihood:** Medium
**Impact:** Medium
**Mitigation:**
- Mandatory registration step (can't skip)
- YAML syntax validation before commit
- Periodic registry audit
- Clear scope/category definitions

---

### Risk 4: Duplicate Tools Created Despite Checks

**Likelihood:** Low
**Impact:** Medium
**Mitigation:**
- Enhanced duplicate detection
- Semantic similarity scoring
- Explicit user confirmation of uniqueness
- Related tools visibility

---

### Risk 5: Schema Doesn't Follow SCHEMA.md Standards

**Likelihood:** Medium
**Impact:** Medium
**Mitigation:**
- Schema validation step
- Auto-suggest standard fields
- Citation format checking
- Examples from similar tools

---

## Success Metrics

### Functional Metrics

✅ **Tool Creation Time:** <10 minutes for basic tool (current: ~15-20 min)
✅ **Zero Manual Editing:** 95%+ of tools require no manual file editing
✅ **Template Compliance:** 100% of generated tools match TEMPLATE.md structure
✅ **Registry Integration:** 100% of tools registered in tool-registry.yaml
✅ **Duplicate Prevention:** 90%+ reduction in duplicate tool creation

### Quality Metrics

✅ **Progressive Disclosure:** 100% of READMEs ≤500 lines
✅ **Schema Compliance:** 100% validation against SCHEMA.md
✅ **Example Quality:** Average rating ≥4/5 for generated examples
✅ **Citation Format:** 95%+ compliance with inline `{source-id}` format
✅ **Test Coverage:** All Level 1-3 validation defined per REVIEW-GUIDELINES.md

### User Experience Metrics

✅ **Clear Questions:** 95%+ questions answered without clarification needed
✅ **Helpful Examples:** 90%+ users find suggested examples valuable
✅ **Quick Validation:** <30 seconds average per validation check
✅ **Easy Restart:** Users can restart wizard without data loss

---

## Implementation Roadmap

### Phase 1: Core Enhancement (Week 1-2)

**Goals:**
- Improve duplicate detection
- Add schema validation
- Enhance example generation

**Deliverables:**
- Enhanced `step-discover-intent.md` with semantic similarity
- Schema validation against SCHEMA.md
- Improved example quality checks

---

### Phase 2: Integration Enhancement (Week 3-4)

**Goals:**
- Strengthen tool-registry integration
- Add test case generation
- Improve template quality

**Deliverables:**
- Mandatory registry registration with validation
- Auto-generated test cases
- Enhanced README.md templates

---

### Phase 3: Advanced Features (Week 5-6)

**Goals:**
- Tool composition guidance
- WebSearch integration for examples
- Quality metrics dashboard

**Deliverables:**
- Tool relationship graph
- Automated example sourcing
- Quality score calculator

---

## Technical Specifications

### AskUserQuestion Usage Pattern

```javascript
// Standard question format
{
  "question": "Clear, concise question text?",
  "options": [
    "Option 1 (with context)",
    "Option 2 (with context)",
    "Option 3 (with context)",
    "Other (provide custom input)"
  ],
  "multiSelect": false  // true for multiple answers
}
```

### Tool Definition YAML Schema

```yaml
# Required fields
tool_name: "Proper Case Tool Name"
tool_name_kebab: "kebab-case-identifier"
task_name: "kebab-case-identifier"  # Must match tool_name_kebab
description: "One sentence description"
test_verse: "BOOK.chapter.verse"

# Formatted sections
goals_formatted: |
  1. Goal 1
  2. Goal 2
  3. Goal 3

examples_formatted: |
  ### Example 1
  **Context**: [Context]
  **Insight**: [Insight]
  **Value**: [Value]

# Schema definitions
data_structure: |
  ```yaml
  [Complete YAML example with sample data]
  ```

yaml_structure_inline: |
  [Concise field hierarchy]

# Optional
related_tools: "Tool1, Tool2, or 'None yet'"
```

### File Generation Script Interface

```python
# init-tool.py usage
python3 init-tool.py /tmp/tool-definition.yaml

# Expected input: YAML file with tool definition
# Output: Complete tool directory structure
# Exit codes:
#   0 = Success
#   1 = YAML parse error
#   2 = Missing required fields
#   3 = Directory already exists
```

---

## Dependencies

### External Dependencies

- **Python 3:** For `init-tool.py` script execution
- **YAML Parser:** PyYAML or equivalent for tool definition parsing
- **Git:** For version control and repository operations

### Project Dependencies

- **TEMPLATE.md:** Blueprint for tool README structure
- **SCHEMA.md:** YAML output structure standards
- **STANDARDIZATION.md:** Naming and format conventions
- **REVIEW-GUIDELINES.md:** Validation criteria (Level 1-3)
- **ATTRIBUTION.md:** Source citation codes and authority levels
- **tool-registry.yaml:** Central tool registry

### Skill Dependencies

- **progressive-disclosure:** Ensures docs stay within line limits
- **tool-experimenter:** Post-creation iteration and refinement
- **scripture-study:** Consumes tools via registry

---

## Conclusion

### Architecture Summary

The Bible Study Tool Creator wizard architecture leverages the existing proven implementation while adding strategic enhancements for:

1. **Better Validation:** Improved duplicate detection and schema compliance
2. **Quality Assurance:** Automated quality checks and citation validation
3. **User Experience:** Clearer questions, better examples, faster workflow
4. **Integration:** Stronger connections with tool ecosystem

### Implementation Strategy

**Enhance, Don't Replace:** Build on existing `bible-study-tool-creator` skill foundation

**Key Principles:**
- One question at a time (progressive disclosure)
- Search-first (prevent duplicates)
- Example-driven (justify value)
- Schema-first (clear contract)
- Mandatory registration (ensure discoverability)

### Next Steps for Implementation

1. **Review existing wizard:** Identify specific enhancement points
2. **Prioritize enhancements:** Focus on high-impact, low-effort improvements
3. **Update step files:** Enhance step-*.md documentation
4. **Improve templates:** Refine README/LEARNING/template generation
5. **Add validation:** Schema and citation format checking
6. **Test thoroughly:** Create 3-5 diverse tools using enhanced wizard
7. **Document learnings:** Update LEARNING.md with enhancement results

---

**Architecture Version:** 1.0.0
**Last Updated:** 2025-11-14
**Maintained By:** myBibleToolbox Project
**Status:** ✅ Ready for Implementation
