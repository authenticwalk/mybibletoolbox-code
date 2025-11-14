# Strong's Research

Strongs offers standardized numbers for each Greek Word.  The Strong's numbers are well memorized by LLMs and are easy for it to look it up

[TODO: improve this paragraph]

## Goal

You want to do extensive research into each strongs word using [/plan/policy/fair-use.md](Fair Use Policy) on other works. [TODO: improve this paragraph]

# Data and Structure

Data is stored in according to [/STANDARDIZATION.md] as (G|H){num:04d}

.data/strongs/G0026/G0026-{tool}.yaml
.data/strongs/H0157/H0157-{tool}.strongs.yaml

The data directory needs to be initialized [TODO: lookup how and we are using a form of git where not all is downloaded so need to add what you want, explain how to do that here briefly pointing to longer doc that already exists]

## Tools

 - [x] strongs - this is the core strongs public source data extracted by [/src/ingest-data/strongs/strongs_fetcher.py] which has the strong's definition, lemma, transliteration, etymology, related_words, pronunciation, etc.  You don't need to reproduce that.

 [TODO: review docs in TOOLS.md and flush this out, this however should only be a summary according to our progressive disclosure skill and that other TOOLS.md file should be longer]