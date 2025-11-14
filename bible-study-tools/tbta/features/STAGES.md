The following summarizes the correct stages to build a new feature.  If you are improving a feature you should validate that it has done all of these stages

# 1. Research TBTA documentation

 - [ ] Review the source documentation of TBTA for this feature from this git repo [ TODO: add link to get to their pdf ]
 - [ ] Review our TBTA analsyis for that feature [ TODO: provide all our links to places where we did that analsyis ]
 - [ ] Generate the README.md for the feature with the information learnt about this feature

# 2. Language Study

 - [ ] Given our notes in languages [ TODO: provide entry level README.md link ] determine for who this feature is important
 - [ ] Update README.md

# 3. Scholarly and Internet Research

  - [ ] Look for scholarily articles about this subject to get the latest research into it
  - [ ] Look into general web information
  - [ ] Update the README

# 4. Generate a proper test set

The following *must* be done in a subagent or new agent so that you don't see what the answers are.  You are not allowed to read the test or validate files till given permission and then only with a subagent to prevent it creeping into your context/memory.

 - [ ] Using the python script analyze tbta [TODO: create and test this script which will clone the TBTA data into a tmp file, loop through all files looking for this feature generating frequency counts and random samples of verses for each] get 100 verses for each VALUE this feature could be.
 - [ ] break those verses into train (40%), test (30%), validate (30%) YAML files as feature: {feature} value: {value: foreach -> verses: {list of verses}}
 - [ ] Use the python3 ~/projects/mcp/bible/fetch_verse.py "<references>" "<languages>" [TODO: upgrade it to accept a list of languages and verses] on each of the verses for each YAML file and your research into languages and language families to get all the verses.  Foreach verse in the YAML file add which languages agree and disagree with the TBTA marked field and the word(s) to support it and any commentary on cultural or debugging reason
 - [ ] Determine if TBTA appears highly consistent with itself and with the translations.  If there is significant concern create a list of questions and examples for the TBTA team to answer before proceeding further.  Do this very rarely.

# 5. Propose your Hypothesis and First Prompt

 - [ ] Review the train.yaml file and the source TBTA files for the training verses and the ../LEARNINGS.md file and create an ANALYSIS.md file with up to 12 different approaches; weight the pros and cons of each
 - [ ] Given the top methods create a prompt in experiments/PROMPT1.md that is the most likely to succeed
 - [ ] Apply that prompt to each verse in the test set, predicting what the main value should be.  If there is only one clear option predict only the value; if there are multiple good options then predict the dominant option with rationale (which may include which language families may prefer it and for what reasons)
 - [ ] Your goal is to achieve 100% on all stated values. A stated value is when you only give one answer.  It is the inerrant word of God so less than 100% is not acceptable.  The dominant value should be 95% accurate.
 - [ ] Debug why you got it right or wrong and add to a LEARNINGS.md file 
 - [ ] Prepare the next prompt PROMPT{NUM}.md focusing on other approaches first, then eventually refining a single approach using prompt engineering, examples, logic flow charts.  Finally focus on the minimal amount of prompt necessary to achieve the same results.
 - [ ] Repeat until you cannot get better results
 - [ ] Summarize your top learnings in the parent learnings file at ../LEARNINGS.md; if it gets over 400 lines then aggregate that file based on our progressive disclosure documentation skill

# 6. Test it against the validate 

 - [ ] Using a subagent to prevent polluting your context with the right answer (cheating) then test it against the validation set
 - [ ] Launch another 3 subagents to do a peer review, they should be fairly critical assuming a junior wrote it with many obvious mistakes.
 - [ ] Return to step 5 with their feedback till they are finally impressed and their feedback is non-material

 

