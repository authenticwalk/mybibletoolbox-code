# TBTA Feature Reproduction with LLM

**Objective**: Reproduce TBTA's 59 linguistic features using LLM-based prediction instead of manual annotation.

**Approach**: Adversarial validation methodology with hierarchical prompting (Theology → Grammar).

---

## What is TBTA?

TBTA (The Bible Translator's Assistant) annotates 31,102 Bible verses with 59 linguistic features needed for translation into 1,000+ languages. Features include clusivity, number systems, participant tracking, discourse genre, and theological patterns.

**Why reproduce it?**: Manual annotation is slow and opaque. LLM-based reproduction enables systematic prediction, validation, and extension to new features.

**Key studies**:
- [Number Systems Analysis](features/number-systems/) - Semantic vs morphological encoding
- [Degree Feature Analysis](features/degree/) - Comparative/superlative prediction
- [Cross-Feature Learnings](features/CROSS-FEATURE-LEARNINGS.md) - Universal patterns across features
- [Person Systems](features/person-systems/) - Clusivity and theological context

---

## Methodology

**Core Approach**: Hierarchical prompting using theological context to improve grammatical predictions.

### Adversarial Testing Protocol
Rather than large random samples, we use targeted edge cases to find weaknesses faster. Training phase allows free TBTA access; validation phase requires predictions locked before checking TBTA.

**Full methodology**: [methodology/ADVERSARIAL-TESTING.md](methodology/ADVERSARIAL-TESTING.md)

### Progressive Disclosure Standard
All documentation follows the ≤200 line README, ≤400 line topic file structure for navigability.

**Documentation standard**: [methodology/PROGRESSIVE-DISCLOSURE.md](methodology/PROGRESSIVE-DISCLOSURE.md)

### Feature Implementation Template
**Template guide**: [GENERIC-FEATURE-TEMPLATE.md](GENERIC-FEATURE-TEMPLATE.md) - Standard structure for documenting new feature implementations

---

## Key Learnings

Our experiments across features have identified transferable patterns that improve prediction accuracy:

**Pattern Overview**: [learnings/OVERVIEW.md](learnings/OVERVIEW.md) - Top 10 patterns summary

**Core Patterns**:
- [Hierarchical Prompts](learnings/HIERARCHICAL-PROMPTS.md) - Theology → Grammar hierarchy
- [Rarity Principle](learnings/RARITY-PRINCIPLE.md) - Default to common, prove rare
- [Multi-Factor Convergence](learnings/MULTI-FACTOR-CONVERGENCE.md) - Agreement-based confidence
- [Advanced Patterns](learnings/ADVANCED-PATTERNS.md) - Edge cases and failure modes

**Cross-Feature Analysis**: [features/CROSS-FEATURE-LEARNINGS.md](features/CROSS-FEATURE-LEARNINGS.md) - Universal patterns from completed experiments

---

## Discourse Context Strategies

For features requiring discourse-level context (participant tracking, discourse genre, register), three approaches are being evaluated:

**Approach Overview**: [discourse/OVERVIEW.md](discourse/OVERVIEW.md) - Comparison of three strategies

**Detailed Strategies**:
- [Approach 1: LLM Conversation Memory](discourse/APPROACH-1-LLM-MEMORY.md)
- [Approach 2: Expanded Context Window](discourse/APPROACH-2-EXPANDED-CONTEXT.md)
- [Approach 3: Two-Pass Processing](discourse/APPROACH-3-TWO-PASS.md)

---

## Workflows

**Feature Checklist**: [workflows/FEATURE-CHECKLIST.md](workflows/FEATURE-CHECKLIST.md) - All 59 features with completion status

**Local Analysis Workflow**: [LOCAL-ANALYSIS-WORKFLOW.md](LOCAL-ANALYSIS-WORKFLOW.md) - Detailed guide for analyzing TBTA features locally with Macula data integration. Covers verse selection, data extraction, pattern analysis, and validation methodology.

---

## Current Status

**Feature Progress**: See [workflows/FEATURE-CHECKLIST.md](workflows/FEATURE-CHECKLIST.md) for complete status of all 59 features.

**Completed Features**:
- Person Systems: Clusivity, Trinity trial number, theological patterns
- Number Systems: Semantic encoding, dual morphology analysis
- Degree: Comparative/superlative, implicit semantics
- Polarity: Affirmative/negative, scope analysis

**Active Development**:
- Participant Tracking: Discourse-level analysis
- Discourse Genre: Chapter-level context
- Illocutionary Force: Speech act classification
- Time Granularity: Temporal precision

---

## Feature Categories

TBTA provides 59 features organized by translation priority:

**Tier A - Critical** (12 features): Person, Number, Gender, Tense, Aspect, Mood, Clause Types, Illocutionary Force, Polarity, Participant Reference, Discourse Genre, Register

**Tier B - Important** (20 features): Evidentiality, Reflexivity, Honorifics, Proximity, Deixis, Time Granularity, Lexical Sense, Surface Realization

**Tier C - Enhanced** (27 features): Noun Classifier, Directionals, Inclusiveness, Distributivity, Associated Motion, and others

**Complete breakdown**: [FEATURE-SUMMARY.md](FEATURE-SUMMARY.md) - Detailed tier descriptions and translation impact
**Feature specifications**: [features/](features/) directory (59 subdirectories)

---

## Integration Examples

**Master Prompts**: Combined prompts for production use
- [Part 1: Core Prompts](combined/TBTA-MASTER-PROMPT-PART1.md)
- [Part 2: Feature-Specific](combined/TBTA-MASTER-PROMPT-PART2.md)
- [Part 3: Advanced Techniques](combined/TBTA-MASTER-PROMPT-PART3.md)

**Worked Examples**:
- [Genesis 1:4 Complete Analysis](combined/worked-example-genesis-1-4.md)
- [Language Adaptation Guide](combined/language-adaptation-guide.md)
- [TBTA Predictor Skill](combined/tbta-predictor-skill.md)

---

## File Organization

```
plan/tbta-rebuild-with-llm/
├── README.md                      # This file - navigation hub
├── methodology/                   # Testing and documentation standards
├── learnings/                     # Transferable patterns across features
├── discourse/                     # Context strategy approaches
├── workflows/                     # Practical analysis guides
├── features/                      # 59 TBTA feature specifications
├── combined/                      # Integration examples and master prompts
└── archive/                       # Historical analysis documents
```

---

**Documentation Navigation**: All documents follow progressive disclosure (README ≤200 lines, topics ≤400 lines) for AI agent accessibility.
