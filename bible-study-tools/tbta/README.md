# TBTA Feature Reproduction with LLM

## What is TBTA?

TBTA (The Bible Translator's Assistant) annotates 11,649 verses across 34 books (~37% of Bible) ([tbta-source/COVERAGE.md](tbta-source/COVERAGE.md)) with 59 linguistic features ([tbta-source/TBTA-FEATURES.md](tbta-source/TBTA-FEATURES.md)) needed for translation into 1,000+ languages. TBTA intentionally focuses on narrative and discourse-heavy books where cross-linguistic features matter most.

Features include clusivity, number systems, participant tracking, discourse genre, and theological patterns.

**Why This Matters - 3 Key Examples**:

1. **Clusivity (Genesis 1:26)**: "Let us make man in our image"
   - Languages: 172 Austronesian languages grammatically distinguish trial number (exactly 3 persons)
   - Without TBTA: Translators might use dual (2 persons) or plural (3+), missing the Trinity reference
   - Impact: Affects theological understanding of God's nature in translation

2. **Participant Tracking (Genesis 4:8)**: "Cain spoke to Abel his brother. And when they were in the field, Cain rose up against his brother Abel and killed him."
   - Challenge: Ambiguous referent - who initiated dialogue? Was "killed him" premeditated or spontaneous?
   - Languages: Affects pronoun choice and discourse flow in 468 Native American languages
   - Without TBTA: Translators might obscure or clarify ambiguity differently than intended

3. **Time Granularity (Genesis narratives)**: Creation account timing
   - Values: 20+ distinct temporal markers (immediate, same day, next day, same week, etc.)
   - Languages: East Asian languages (Japanese, Korean, Chinese) require explicit temporal sequencing
   - Without TBTA: Translators might impose chronological precision or vagueness not present in Hebrew
   - Impact: Affects interpretation of creation timeline, prophetic fulfillment, narrative flow

## Our Approach to TBTA Reproduction

**Objective**: Reproduce and improve TBTA's linguistic features using LLM-based prediction instead of manual annotation.

**Why LLM-based?**: Manual annotation is slow and opaque. LLM-based reproduction enables systematic prediction, validation, and extension to new features while leveraging extensive language and Biblical knowledge.

**Key Resources**:
- **TBTA Source Analysis**: [tbta-source/](tbta-source/) - Comprehensive documentation of original TBTA system
- **Feature Methodology**: [features/STAGES.md](features/STAGES.md) - 6-stage development workflow
- **Consolidated Learnings**: [learnings/README.md](learnings/README.md) - Validated prompt engineering patterns
- **Language Resources**: [languages/README.md](languages/README.md) - Cross-linguistic guidance
- **Feature Catalog**: [features/README.md](features/README.md) - Progress tracking for all 82 features

**Improvements Over Original TBTA**:
 - Add rationale to answers. The why we reach a conclusion on a label can be invaluable for applying it in each use case.
 - Allow primary and secondary answers. When the choice is arbitrary seek consistency among language families.
 - Omit default values. It is better to have no answer than the wrong answer.
 - Divide New Testament by verses to maintain consistency with myBibleToolbox structure, allowing overlapping thoughts/words from neighboring verses to maintain relationships. (Note: TBTA's OT/NT division strategy documented in [tbta-source/DATA-STRUCTURE.md](tbta-source/DATA-STRUCTURE.md))

## Thesis

In the Bible it says, "there is nothing new under the sun".  The problem we are solving is how does a new translation deal with unique linguistical features not present in the original text.  We have access to about 1000 translations so likely several of them have already dealt with this.  The key is to analyze those translations and figure out which ones are the clue that reveals the answer.  Say your language requires not just (he, they) but (1,2,3,4,5,more) people.  You would not be alone.  Find another language that does that and see what they did for this verse and do the same.  Prefer languages of the same family or translations derived from the source text (since local translators are hard to find often they use what they know like Indonesian, Swahali, French, German, etc).  When multiple languages have that feature and disagree on your verse then understand the cultural, linguistic, translation source lineage and other reasons to help you make your decision.

## AI Rules

**Documentation Navigation**: All documents **must** follow progressive disclosure for AI agent accessibility:
- Feature READMEs: ≤500 lines (technical complexity requires inline methodology)
- General READMEs: ≤200 lines (self-contained overview)
- Topic files: ≤400 lines
- See [/.claude/skills/progressive-disclosure/SKILL.md](/.claude/skills/progressive-disclosure/SKILL.md) for general standards

**Don't write code to predict**: This is a prompt and context engineering task only, never write code that will try to predict the values as that will be too limited.

**Follow proper train/test/validate data hygiene**: Never look at the answer before predicting, that is cheating and will be severely punished by the removal of all your results. When checking the results always use a subagent so it has clean context and return only the results not the correct answer so you don't pollute your context.

**Don't pollute/spam this folder**: Never put session summary files in this folder or subdirectories, put them in /plan/tbta/{SESSION-TASK-SLUG}. Clean up old files, keep all documents current. If you edit a file always check its README.md in the same directory and the parent directory to ensure changes are propagated.
