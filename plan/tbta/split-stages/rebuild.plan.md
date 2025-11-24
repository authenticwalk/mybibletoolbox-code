I want to rebuild @STAGES.md by breaking it into parts, imagine that each part is assigned to it's own agent to keep context low and each agent will need all the core information it needs to achieve it's goals.  Thus there should be an overachieving file (better name than STAGES.md) (filename-{yourModelName}.md and a directory (prefixed with dot so we know it is a system file not an output) ex (.directory-{yourModelName}) Following @PROGRESSIVE-DISCLOSURE.md 

As you work on each section review how the cursor and claudeFlow did (good and bad) and use that to inform you how to make this better.  Don't add any comments about your evaluation of how they did or what should be changed only make the changes; thus your result is the end product.  If you need to record your thoughts do so in /plan/tbta/split-stages-{yourModelName}

Here is what I'm thinking the new system will look like

 - .instructions-to-build-feature/
  - README.md
    - Short Intro to TBTA (links to key TBTA files) from ../README.md 
    - Features, what it is, why it matters
    - Goals for building this (want to rebuild TBTA using an LLM only)
    - Rules (predict with LLM, no looking at answers, must peer review, smaller is better, must genearlize - don't make an expert system with just hardcoded values)
    - Stages - list of all stage documents
    - Don't list all the features here, link to the features/README.md 
    - Don't add progress updates here or planning here, tell to put planning files into /plan/tbta/features/{feature-name}/
 - research/
   - tbta - read their documentation, our notes, frequency analysis (coverage per value)
   - languages - must determine which languages use this feature, unique needs between them, do an anlaysis of which languages we have
   - scholarly
  - analysis 
   - foreach tbta entry output in jsonl verse, label, some field that indicates what word it is (write as python code)
   - select 100+ values for each value using criteria in current STAGES.md (advsarerial, non-arbitrary, arbitrary, balanced, covering all edge cases) output as jsonl as reference, tbta word used, tbta value, strongs number, strongs word) (you will need to use a smart LLM agent for this as strongs number is not in the TBTA source)
   - Using the quote Bible skill lookup one of the verses in the NT and one in the OT and discover which langauges we have (you should get about 1000 languages back in NT, less in OT; if not you did it wrong, debug and fix).  
   - foreach record in the above consider which languages from above use or require this feature and guess which words they would use that would translate this strongs word to their language using the tbta feature.  Also guess which words they would use if TBTA was wrong and they chose another value
   - use a script (create if this is your first feature but make it reusable for all features) that will use the bible lookup function (already written) to get all the verses that have a TBTA value for this feature and using the guessed words check if any of those words are present in each verse.  Create a score card for each language and overall for how often they agree with TBTA. Also store the raw results as a jsonl file 

 [ I need to step out for a moment, do as much as I have written, if you have time left over you can continue down this train of thought ]

