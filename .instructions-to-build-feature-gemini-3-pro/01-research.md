# Stage 1: Research & Definition

**Role**: Researcher / Linguist / Theologian
**Input**: Feature Name (e.g., "Number", "Allocution", "Mood")
**Output**: `features/{feature}/README.md` and `experiments/ARBITRARITY-CLASSIFICATION.md`

## Goal

Define the feature comprehensively: what it is, who needs it, and why it matters theologically. You are laying the foundation for the data scientists.

## Tasks

### 1. TBTA Documentation Review

- **Source**: Read files in `../../tbta-source/` (look for `DATA-STRUCTURE.md`, feature lists, etc.).
- **Action**:
  - Identify the "Concept" (e.g., Number = count of entities).
  - Identify the "Values" (e.g., Singular, Dual, Trial, Paucal, Plural, Quadrial).
  - Identify the Encoding (Where is it in the JSON? Noun Position 2?).

### 2. Language Family Analysis

- **Source**: `../../languages/` directory.
- **Action**: Determine which language families _grammatically require_ this feature.
  - _Example_: Dual number is required by Austronesian (Oceanic) and some Trans-New Guinea languages.
  - _Constraint_: Be specific. Don't just say "Many languages". List families and count estimate.

### 3. Scholarly Research

- **Source**: General knowledge / Web Search (if enabled).
- **Action**: Find 1-2 scholarly references confirming the linguistic typology.
- **Check**: Are there cultural sensitivities? (e.g., "Brothers" vs "Brothers and Sisters").

### 4. Arbitrarity Classification (Theological Analysis)

**Critical Step**: Not all choices matter. Some are arbitrary (style); some are non-arbitrary (doctrine).

- **Create**: `experiments/ARBITRARITY-CLASSIFICATION.md`
- **Format**:
  ```yaml
  feature: { feature }
  default_classification: arbitrary
  non_arbitrary_contexts:
    - pattern: 'Gen 1:26 (Trinity)'
      affected_values: [Trial, Plural]
      theological_stakes: High (Nature of God)
      denominational_implications: True
  ```
- **Rule**: If a choice affects Doctrine (Trinity), Divine Speech, or Ethics, it is **Non-Arbitrary**.

## Deliverable: The Feature README.md

Create `features/{feature}/README.md` following **Progressive Disclosure** (≤500 lines).

**Structure**:

1.  **Feature Name & Description**: One sentence summary.
2.  **Target Audience**: Which language families need this?
3.  **Theological Context**: Why does this matter? (Link to Arbitrarity).
4.  **TBTA Encoding**: Technical details (values, JSON path).
5.  **Stage Checklist**: Copy the checklist of stages so we can track progress.

_Do not add implementation details yet. Focus on Definition._
