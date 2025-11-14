# TBTA Feature Reproduction with LLM

## What is TBTA?

TBTA (The Bible Translator's Assistant) annotates 31,102 Bible verses [tbta-source/COVERAGE.nd] with 59 linguistic features [tbta-source/TBTA-FEATURES.md] needed for translation into 1,000+ languages. Features include clusivity, number systems, participant tracking, discourse genre, and theological patterns. [TODO: confirm this claim, I thought they did not do all verses yet, confirm number of features, populate those research files ]

[TODO: need to add a 3 key examples of why this is important using 3 different features]

## Creating a workflow that will Reproduce and Extend TBTA

**Objective**: Reproduce and improve TBTA's linguistic features using LLM-based prediction instead of manual annotation.

**Why reproduce it?**: Manual annotation is slow and opaque. LLM-based reproduction enables systematic prediction, validation, and extension to new features. It allows [learnings/LLM-MEMORY.md](LLM memory) [TODO: move that file over] to draw from extensive language and Biblical knowledge.

**Approach**:
[TODO: this is intented as a high level task list and should be checked off when done] 
 - [ ] Extensively research TBTA and it's goals [tbta-source/][TODO: analyze all files for where we researched tbta and it's git repo and populate that into ./tbta-source]
 - [ ] Extenstively research linguistical theory and languages [languages/README.md]
 - [ ] Extensively research each feature[features/README.md] indepentently then use prompt engineering to correctly predict it [features/STAGES.md] sharings [learnings/README.md]
 - [ ] Discover the rules to structure the data in nested relationships [structure/README.md] [TODO: or could we present it as a list of words with pointers to it's parent(s) thus allowing it more graph like showing relationship to multiple fields instead of just one]

**Improvements**:
 - Add rational to answers.  The why we reach a conclusion on a label can be invaluable for applying it in each use case.
 - Allow primary and secondary answers.  When the choice is arbitrary seek consistency among language families.
 - Omit default values.  It is better to have no answer than the wrong answer.
 - Divide New Testament by verses so keep consistency with myBibleToolbox structure, allowing overlapping thoughts/words from neighboring verses to maintain the relationship. [TODO: improve this wording; TBTA divides OT and NT differently; what is NT divided into and how can we make it work.]

## AI Rules

**Documentation Navigation**: All documents **must** follow progressive disclosure (README ≤200 lines, topics ≤400 lines) for AI agent accessibility. [/.claude/skills/progressive-disclosure/SKILL.md]

**Don't write code to predict**: This is a prompt and context engineering task only, never write code that will try to predict the values as that will be too limited. 

**Follow proper train/test/valide data hygene**: Never look at the answer before predicting, that is cheating and will be severely punished by the removal of all your results.  When checking the results always use a subagent so it has clean context and return only the results not the correct answer so you don't polute your context.

**Don't pollute/spam this folder** Never put session summary files in this folder or subdirectories, put them in /plan/tbta/{SESSION-TASK-SLUG}.  Clean up old files, keep all documents current. If you edit a file always check its README.md in the same directory and the parent directory to ensure changes are propogated.