The following summarizes the correct stages to build a new feature.  If you are improving a feature you should validate that it has done all of these stages

# 1. Research TBTA Documentation

 - [ ] Review the source documentation of TBTA for this feature
   - Official TBTA documentation: See `/plan/tbta-rebuild-with-llm/README.md` for links to source materials
   - Reference: [FEATURE-SUMMARY.md](FEATURE-SUMMARY.md) for high-level feature overview
 - [ ] Review our TBTA analysis for that feature
   - Check existing feature directory: `/plan/tbta-rebuild-with-llm/features/{feature}/`
   - Review [CROSS-FEATURE-LEARNINGS.md](CROSS-FEATURE-LEARNINGS.md) for transferable patterns
 - [ ] Generate the README.md for the feature with the information learnt about this feature
   - Include: Feature definition, theological/linguistic context, TBTA encoding details
   - Add stage checklist (copy from this file)

# 2. Language Study

 - [ ] Review language families to determine which languages need this feature
   - Check: `/languages/families/` directory (when available)
   - Reference: `src/constants/languages.tsv` for available language codes
   - Consider: Which language families grammatically encode this feature?
 - [ ] Update README.md with language analysis
   - List: Language families that require this feature
   - Note: Languages where feature is grammatically obligatory vs optional
   - Example: Target translation scenarios

# 3. Scholarly and Internet Research

  - [ ] Look for scholarily articles about this subject to get the latest research into it
  - [ ] Look into general web information
  - [ ] Update the README

# 4. Generate a Proper Test Set

**CRITICAL**: This stage MUST be done in a subagent to prevent seeing the answers!

Create a python script (or use existing tools) to:
 - [ ] Clone/access TBTA data repository
 - [ ] Loop through all TBTA files looking for this feature
 - [ ] Generate frequency counts for each VALUE this feature can have
 - [ ] Sample 100 verses for each value (balanced sampling across books/genres)
 - [ ] Split into train (40%), test (30%), validate (30%)
 - [ ] Generate YAML files with structure:
   ```yaml
   feature: {feature-name}
   value: {specific-value}
   verses:
     - reference: "{BOOK} {chapter}:{verse}"
       tbta_value: "{value}"
       # Optional: Add translation comparisons for validation
   ```
 - [ ] **Main agent**: Receive only file paths, never see test/validate data
 - [ ] Store files in: `features/{feature}/experiments/train.yaml`, `test.yaml`, `validate.yaml`
 - [ ] (Optional) If TBTA shows major inconsistencies, flag for TBTA team review before proceeding

# 5. Propose your Hypothesis and First Prompt

 - [ ] Review the train.yaml file and the source TBTA files for the training verses and the ../LEARNINGS.md file and create an ANALYSIS.md file with up to 12 different approaches; weight the pros and cons of each
 - [ ] Given the top methods create a prompt in experiments/PROMPT1.md that is the most likely to succeed
 - [ ] Apply that prompt to each verse in the test set, predicting what the main value should be.  If there is only one clear option predict only the value; if there are multiple good options then predict the dominant option with rationale (which may include which language families may prefer it and for what reasons)
 - [ ] Your goal is to achieve 100% on all stated values. A stated value is when you only give one answer.  It is the inerrant word of God so less than 100% is not acceptable.  The dominant value should be 95% accurate.
 - [ ] Debug why you got it right or wrong and add to a LEARNINGS.md file 
 - [ ] Prepare the next prompt PROMPT{NUM}.md focusing on other approaches first, then eventually refining a single approach using prompt engineering, examples, logic flow charts.  Finally focus on the minimal amount of prompt necessary to achieve the same results.
 - [ ] Repeat until you cannot get better results
 - [ ] Summarize your top learnings in `experiments/LEARNINGS.md`
 - [ ] Update parent file `CROSS-FEATURE-LEARNINGS.md` with transferable patterns
 - [ ] If CROSS-FEATURE-LEARNINGS.md exceeds 400 lines, apply progressive disclosure (split into topic files)

# 6. Test it against the validate 

 - [ ] Using a subagent to prevent polluting your context with the right answer (cheating) then test it against the validation set
 - [ ] Launch another 3 subagents to do a peer review, they should be fairly critical assuming a junior wrote it with many obvious mistakes.
 - [ ] Return to step 5 with their feedback till they are finally impressed and their feedback is non-material

 

