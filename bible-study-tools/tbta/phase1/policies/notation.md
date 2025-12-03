Information relevant to the final phase 1 (with brackets and such) that is not as relevant for drafting He1 will be shown with red type. Comments relevant to He1 will be shown with magenta type.

There is a lot of useful information in the document entitled “Analysis Conventions”. Please check that out. The conventions for pronouns and clause brackets are described there.

1. Relative Time

We use relative time in relative clauses and in patient (object complement) clauses, but not adverbial clauses.  So the Time feature on the verbs in relative clauses and patient clauses is set with respect to the main verb.  For example, the time of the going in “John thought \[John will go to the store on the next day\]” means tomorrow on the day that he did the thinking. In other words, if he was thinking about this 7 days ago, tomorrow would be 6 days ago.

2. No Discourse Time in Quotes

For quotes, the main difference is that the main verb should have a Time value other than Discourse.  But we still use relative time in relative clauses and patient clauses in quotes.

**A Note about the Perfect Tense**  
In English and in a number of other languages you can use the perfect tense, "X HAS DONE something". The perfect represents a present state based on a past action, and therefore has a composite meaning of the present and past tense. In TBTA, if you write a phase 1 verb using the perfect, it will be analyzed in TBTA as the "flashback" feature. The perfect is used quite frequently in the Bible, but it is not always available for every target language. If it is available in the target language, it will be used if the verb is marked with the flashback feature. If it is not available in a target language, flashback will most likely be represented with something like "X did something previously" or "X did something recently". If both of these last representations are acceptable representations of the meaning, you can use the perfect in the phase 1\. For instance, Paul talking to new believers may say, "you have believed in Christ". Since that happened previously and from Paul's perspective was recent, it's okay to write it exactly that way for the phase 1, and it will be analyzed as flashback. On the other hand, consider, "God has chosen \[you to be his people\]" (for He1 we omit the square brackets). We don't know that that happened recently, and in some theological circles, it happened in the eternal past. Therefore in my opinion it would be best to use the simple past in this case, "God chose \[you to be his people\]".

# **Comments and poetry**

Use “ \_paragraph” for now (“(paragraph)” when TBTA is fixed so that it works) in the phase 1 to Indicate a new paragraph. Use “(paragraph)” in the English back translation or for He1.

Use “(comment-begin)” and “(comment-end)” for a parenthetical comment, that is, for a comment in parentheses. This will be generated as “(...)” in English. Use “(...) in He1. ('(begin-comment)' and '(end-comment)' are also OK.)

Use “(poetry-begin)” and “(poetry-end)” to delineate a section of poetry. The English generator will indent each sentence in between these markings. ('(begin-poetry)' and '(end-poetry)' are also okay.)

Please note that we do not use "\_indent" or "\\q" or "\\q1" or "\\q2", which all indicate some kind of indentation. Instead, we use "(begin-poetry)" and "(end-poetry)". Between those two notations, which may be many verses apart, all of the text will be indented. The NIV sometimes has a blank line marking off different sections of poetry. At those locations, you should add "(blank-line)"."

Note that comments, poetry sections and quotations may extend over multiple verses.

## **Marking quotes**

Quotes were also described in the Analysis Conventions, but I have some comments about them here. 

Single sentence direct quotes:    
John said, \["Mary read that book"\].    
John asked, \["Did Mary read that book?"\]    
John shouted, \["Mary read this book\!"\]  
In He1, you write these as above, but without the square brackets.

Multi-sentence direct quotes:  John said, \[“Mary read that book\]. Then Peter read this book".  
In He1, you write this as above, but without the square brackets.

For the first sentence (whether in a single sentence quote or the first sentence of the multi-sentence quote), the quote is a patient clause for the verb “said” (in the cases above). So it makes sense that that clause would be marked with brackets, and that the initial quotation marks would be within the brackets (since it is part of the content of that patient clause). If it is a single sentence quote, it makes sense that the final quote mark should be within the patient clause of “said”, and so also within the brackets of that clause. But note that the initial left bracket after “said” is not to indicate the start of a quotation, but rather to start the patient clause. It just so happens that “ \[“ “ occur together after verbs like “say”.

If there is a question mark or exclamation mark, it makes sense that that would be within the quotes, because that was describing how the statement was said. The period could perhaps be interpreted as either part of the quote or as for the entire sentence. We would prefer that you put the period at the end of the entire sentence, which makes it clearer where the sentence ends. (It does actually work in the analyzer if you use “John said, \["Mary read that book."\]”. It would not work in the analyzer to put the period within another subordinate clause embedded within the clause of the argument of “said”.) Note that we always use double quotes for quoted statements, regardless of how many levels of embedded quotes. 

Note that in long quotations that cross paragraph boundaries, we do not begin each paragraph with an open quote mark, as is standard practice for English. We only put the open quote at the very beginning of the quotation, and the end quote at the very end of the quotation.

Single quotes are automatically inserted in certain constructions like, “X means Y”. Do not put quotation marks around “Y” for these constructions.

Titles and footnotes  
Use “(title)” at the beginning of a title. Normally try to use one sentence for a title. If it is necessary to have more than one sentence, put “(title)” at the beginning of each sentence, but since you have total freedom to choose what to put in titles, try to limit it to one sentence. Use the present tense in titles. The title should be independent. Don’t assume knowledge of information in the text, and when you write the text, don’t assume knowledge of information in the title.

“(footnote)” should precede footnotes. Note that everything following a footnote is part of that footnote, unless a new footnote is started. In other words, you can’t put a footnote in the middle of a verse. It has to go at the end. If you start a new footnote after the first footnote, everything following that is part of the footnote unless you start another footnote.

## **Proposition arguments**

If a verb has a proposition argument, and the subject of the proposition argument is the same   
as either the subject or patient of the main clause, the repeated noun is deleted. We never need to repeat a noun for the sake of the analyzer; the sentences are supposed to sound like normal English.  
**Examples:**  
(1) sentence where the subject of the subordinate clause is the same as the subject of the main clause; write as "John wanted \[to eat food\]"  
(2) sentence where the subject of the subordinate clause is the patient of the main clause: write as "John wanted \[Paul to eat food\]"  
(3) sentence where the subject of the subordinate clause is unrelated to arguments of the main clause; write as "John knew \[Paul was eating food\]"  
In all of these cases, we put the opening bracket after the verb in the main clause. No brackets needed in He1.

We omit the complementizer "that" in patient clauses. That is, write "John knew \[Mary was in the house\]" rather than "John knew \[that Mary was in the house\]". The reason is that "that" is also used as a demonstrative determiner, the analyzer can be confused and interpret it that way, and "that" is not needed in those clauses. But you need a complementizer for a relative clause, like "the person \[that John knew\]", although you can use "who" here, which would be preferred.

## 

## **Indicating senses**

You can indicate the sense of a word by tacking on “-L” where “L” is a letter like “A” or “B”. But only do this when you know the correct sense and think that P2 might get it wrong. For instance, there are five senses of the conjunction “then”. By far the most common one is “then-A”, which means temporal succession. If you want “then-D” (consequence), it might be a good idea to indicate that. You don’t necessarily need to indicate the sense of “thing”, because there are four senses of this very common word, and P2 will know that he always needs to be checking that, but you can indicate it if you think it would be helpful. And many of the senses are determined by the argument structure. If sense A does not have a patient clause argument, but sense B does, the analyzer will know that the correct sense is B. Currently the analyzer will not automatically interpret “-B” to get the right sense, but P2 will see the notation and make a manual adjustment if necessary. In the future, this should be done automatically.

## **Simple/complex pairing**

Use the notation “X/Y” to indicate that “X” is a simple (level 0 or 1\) word and that the complex (level 2 or 3\) word “Y” is paired with it. This means that if Y is available in the target language, it will be used, but if not, X. Currently the analyzer just ignores “/Y”, but P2 will see it and manually set the pairing. In the future, this should be done automatically. For He1, you can write complex words without a pairing. But if it’s a level 3 word for which a pairing or explication is not appropriate, you should put it in a complex alternate.

## **Marking implicit information**

Use the underscore character followed by any number of letters and numbers to indicate miscellaneous information, like “ \_implicit \_dual”. It has to be separated from the word by a space. The comment will apply to the word preceding the comment. Think of the underscore character as pointing toward the word on the left. Everything following the underscore will be ignored by the analyzer, but P2 will see it and be able to use the information to make sure that the word’s features are correct. In this case, nothing may ever be automatically done with this text since it can be anything. Use “ \_implicitNecessary” for something that is required by the grammar or for the sentence to make sense.  
By including “implicit” within the text, we can mark that a noun phrase, adjective phrase, or adverb phrase is implicit. Clauses are marked implicit through another notation as discussed in the next paragraph. For He1, Surround text with “\<\<...\>\>”  for regular implicit information, and with “\<...\>”  for necessary implicit information.

The following types of notation mark that an optional clause (whole sentence or event clause) is implicit. If this notation is within the main clause of the sentence or in front of the sentence, the entire sentence will be marked as implicit. If the notation is within a subordinate clause, then only that subordinate clause (along with any embedded clauses subordinate to that clause) will be marked as implicit. If you know which kind of implicit marking it is, cultural, situational, etc, please indicate that.

“(implicit)” OR “(implicit-info)” \- generic indicator that the clause is implicit  
“(implicit-cultural)” \- implicit information relating to the ancient culture  
“(implicit-situational)” \- implicit information relating to the particular situation  
“(implicit-historical)” – implicit information related to the historical situation  
“(implicit-background)” \- background information  
“(implicit-subaction)” – these are actions that the original text didn’t mention, but from the context we know they had to have happened  
“(implicit-argument)” \-  for an implicit patient proposition of a verb

Don’t be overly concerned with choosing which category an implicit clause should be assigned to. The most common marking is "(implicit-situational)".

For He1, Surround text with “\<\<...\>\>”  for regular implicit information, and with “\<...\>”  for necessary implicit information.

**Regarding Historical and Background info,** 'Historical' generally refers to some event that happened earlier, while  'Background' generally refers to information rather than a historical event.  A good example of Background implicit info is in Matt. 1:16 'People call Jesus 'Christ' because God chose Jesus to save His people.'  That's  background info  rather than a historical event.  A good example of  Historical implicit info is in Ruth 4:17 'And David became the king of Israel.'  That's a historical event, so we tagged it as historical.  But again, distinguishing between these different categories is often subjective.

**Imperatives**  
“You(person) (imp) go now\!” is generated as “Go now\!” In He1, you can write “go now\!”

**First and second person pronouns**  
Indicate the referent for a first or second person pronoun in parentheses, like  
    “you(followers)”  
If a complex pairing has been used previously in the verse, you should use the simple term in parentheses: “Jesus said to Jesus’s followers/disciples, \[“You(followers) are my(Jesus’s) followers/disciples”\].”  
For third person plural, indicate inclusive or exclusive first person using "\_incl" or "\_excl" following the expression of the plural:  
   					"we(Jesus) \_incl"

Note **if there are multiple people listed**, like "Jesus, Peter, and John", **just list one person in parentheses ("we(Jesus)" above)**.

Note that we **never use third person pronouns,** “he”, “it”, etc. You **have to use the noun that the person pronoun would mean**. The program automatically determines when to use pronouns.

For He1, It could be helpful to use the notation above (red type) once per verse  so that the AI program could know who we are talking about. After that, just use the pronoun.

The function of relations  
In the list of relations, there are two relations at the top that have a specialized function, "Begin Episode" and "Begin Scene". "Title", the 19th item, also has a specialized function. We use "Began Scene" by writing "One day", and we use "Title" by writing "(title)". Preceding "Title" in the list are a number of relations which have a noun argument and modify a noun, like "made of" in "a box made of wood". (See the "Special relations" below concerning these.) And the relation 'Subgroup' modifies adjectives that modify nouns (e.g., '(np (adjp 2 Subgroup) book))' produces something like 'two of those books'). But the vast number of relations, almost all of those starting with "about" and also the "Iteration" relation near the top of the list function adverbially. They modify the verb in the clause. In the sentence "The mouse in the house was afraid", the phrase "in the house" modifies the verb "was", meaning that the mouse was afraid when he was in the house. If you want "in the house" to act like it modifies mouse, you need to put it in a relative clause, "the mouse \[that is in the house\] was afraid".  In that case, "in the house" actually modifies the verb "is" inside the relative clause, but now the entire relative clause modifies the noun "mouse". So "mouse \[that is in the house\]" functions similarly to "the mouse in the house" of natural English. 

**Specialized implicit descriptions of nouns**  
We have two specialized ways of specifying implicit descriptions of nouns. The first one, "\_implicitExplainName", is currently used only with the "named" adposition. It is used to indicate the type of a name (level 4, or brown, in the ontology). **(Let Richard know if there is a circumstance where it looks like we need this for a different relation.)** As a feature in the phase 2, this is "explanation of a name", but it is associated with this implicit type of notation in the phase 1\. Usually the first time in a book that we introduce a place or nation, we introduce it using notation like "Cana named the city \_implicitExplainName". We write this with "Cana" as the head noun of the phrase (see the “Intro to TBTA grammar”), so it won't be removed if the implicit type information is not included. But in the English grammar, if the audience option selected is to include these explanations, it will be generated with the nouns reversed, "\<\<the city named\>\> Cana". Our policy is to only use this explanation the first time the name is introduced in a particular book. This also could be used to introduce other types of nouns, like a person, "Jeremiah named a man \_implicitExplainName".

We handle metonymy in a similar way. Metonymy is when you say that someone or something did something, but the action was really done by someone or something else. An example would be "Herod searched for Jesus". Since Herod didn't actually go searching for Jesus, but rather was responsible for soldiers going to search for Jesus, we write for the phase 1 "Herod of the soldiers \_dynamicexpansion (previously \_explainMetonymy) searched for Jesus". Just like for the implicit explanation of the name, when generated in English, the nouns will be reversed, "\<\<The soldiers of\>\> Herod searched for Jesus". Again, the reason we write it reversed in the semantic representations is so that "Herod" will not be removed if "the soldiers" are removed.  Remember that if an implicit head noun is removed, subordinate modifiers, like a prepositional phrase will also be removed (see the extensive discussion in the “Intro to TBTA grammar”). So if we wrote it as "the soldiers \_implicit of Herod searched for Jesus", and if "the soldiers" were removed as implicit information, "of Herod" would also be removed, since the syntactic structure would be "\[NP the soldiers \[NP of Herod\]\]" with "of Herod" included in the "soldiers" noun phrase.  
We also can mark a "literal expansion", when there is a word that is literal, but the translator might prefer a more dynamic translation. Consider "The Lord of the eyes \_literalExpansion search for a good-B/righteous person". Unless the translator chooses to turn off the literal expansion, it will be generated as "The eyes of the Lord search for a righteous person", in other words, with the nouns "Lord" and "eyes" reversed, similar to the explanation of a name and dynamic expansion. The difference here is that the expansion is used if a more literal version is desired, whereas for a dynamic expansion, the expansion is not used if a literal translation is desired.

**Necessary Implicit**  
Our notation **“\_implicitNecessary” (“\<...\>” in He1) is used for any syntactic category that is implicit but necessary for the grammar**. It is not ordinarily used for optional items. Verbs or non-passive subjects need to be marked this way to be considered implicit. The generator will always generate these, but will be marked with “\<...\>”, italics or some other type of formatting.

**The word ‘X’**  
For “the word X”, we write it exactly that way, like “the word gods”.   Schematically, the structure is (np gods (np GenericGenitive word)).  You can see an example in the footnote for Matt. 1:1 "The Greek word Christ is like the Hebrew word Messiah."  The first NP is (np Christ (np GenericGenitive word (np GenericGenitive Greek)))'.

# **Using alternates**

 We have several different kinds of alternates. Whenever we have a very literal sentence that might be misunderstood, we use (literal) at the front of that sentence, and then normally add an alternate sentence with “(dynamic)” at the front of the alternate sentence. Literal or dynamic sentences can be allowed or disallowed by a switch for a particular audience (like churched adult or unchurched children).  Either or both of the translations can be generated. It’s also possible to have one without the other.

## **Meaning alternates**

Meaning alternates (our original kind of alternate) present a different interpretation where the meaning of the text is questionable, or a different wording if expressing a particular idea is difficult. Notation for meaning alternates:  
“(primary)” \- for primary text, the default choice  
“(alternate-1)” \- First alternate reading  
 “(alternate-2)” \- second alternate reading  
 “(alternate-3)” \- third alternate reading  
… Currently up to five alternates

Although our system allows for this number of alternates, generally we should try to use as few as possible. Alternates will necessitate a choice by the translator, and we would like to make the process as automatic as possible. So the fewer number of alternates the better, where zero is optimal. But when you need them, they can be used.

## **Metaphor**

Note that we allow metaphor if we think that the meaning would probably be understood. If we think that the metaphorical meaning would probably be understood, but might not be, then we would also include an alternate. In many cases, this would be a literal/dynamic combination.

**Note that we don’t use idioms. Idioms are sayings that would ONLY be understood by a particular culture.**  

Where we are quoting someone who says that something IS something metaphorically, like when Jesus says that he is the light, we should use the new version of "be-X" (metaphorical “be”). But in a footnote or title, where we are trying to explain the meaning, it is more appropriate to use "be-U \= be like".

## **Rhetorical questions**

We include rhetorical questions, but they must always have an alternate in the form of a statement. Use this notation within or at the beginning of the sentence:  
(yesrhetorical) \= for a yes or no question with an expected answer of yes (from Greek οὐχ)  
(norhetorical) \=  for a yes or no question with an expected answer of no (from Greek μή)  
(rhetorical) \= for cases that are debatable as to how they should be answered.  
“(statement)” \- for statement form

**\*Whenever you use one of the first three options (including the word “rhetorical”), you normally follow it by a statement version.**

Like literal and dynamic alternates, whether or not the rhetorical statement versions are generated can be determined by a switch for the audience.  

### **Rhetorical questions in the Back Translation:** 

Use the same also down "(yesrhetorical)" and "(norhetorical)" notation for the English. Explain about the expected answer  to the consultant in a comment where it first appears.

### **Biblical Units**

Used for time, currency, etc.  
You can write it like this: ‘Bethany was about 3/15 kilometers/stadia from Jerusalem.’  
Or  
**Notation:**	Mark biblical units with (literalunits) and contemporary units with (modernunits).   
**Example:**	(literalunits) The time was the third hour \[when those soldiers crucified Jesus.\]  
(modernunits) The time was 9AM \[when those soldi ers crucified Jesus\].

Certain units can't be expressed with pairings because they have different structures, so those have to be done with a 'literal units' alternate and a 'modern units' alternate.  For example, Matt. 20:3,5,6,9 talk about 'the third hour/9am,' 'the sixth hour/12pm,' etc.  And Matt. 25:15,16,17,18,20 talk about 'talents/bags of gold'.  Since the units have different structures, we can't use a pairing, so we use alternates.  But if the biblical units and contemporary units have the same  structure and simple arithmetic can convert one to the other (e.g., 'kilometer/stadia', 'kilogram/shekel', etc.), we use a pairing.

## **Vocabulary (level 3 word) alternates**

Another form of alternates is what we call the vocabulary alternate. **Currently vocabulary alternates are only used for level 3 words (dark green in the TBTA ontology or dark green box with L3 In the ontology app).**   
Level 3 words use abstract concepts that are usually expressed in a different way **when** there is not a satisfactory explication. Often they require a vocabulary alternate, *but they may appear as a complex term in a complex pairing.* **An example of a level 3 word is “glory”. A complex sentence with “glory” is often paired with an alternate that uses “wonderful/glorious”.** 

*The vocabulary alternate is currently the only kind of alternate that allows for multiple sentences.* Use this notation to indicate the primary text using the level 3 word and the alternate text using the simple vocabulary:  
“(complex)” – for the sentence using the level 3 word  
“(simple)” \- for the sentence using simple vocabulary  
if you have multiple sentences, for the time being just use this notation in each of the sentences.   
If the level 3 word is available in the target language, the complex vocabulary representation will be generated. If not, the simple vocabulary representation will be generated.

## **Special relations**

There are some special relations listed in the ontology at “Ontology and Lexicon/Ontology/Relations”. Generally, you should just use normal English to express these. **So here are ways to express these concepts:**  
Begin scene – “One day”  
body part – “Mary’s hand”  
composed of – “lake of fire”  
generic genitive – “Mary’s friends” or “friends of Mary”   
group \- “group of sheep”  
iteration – “X does something three times”  
kind-of \- kinds of animals  
kinship – “Mary’s sister”  
made-of – “house of bricks”  
named – “town named Bethlehem”  
nationality – “Hebrew man”  
owner – “John’s house”  
part whole – “the front of the boat”  
quantity – 10 kilograms of wheat  
realm of authority – “king of the Israelites”  
region of authority – “ruler of Israel”  
subgroup – “some of the apples”  
title – “king Herod”

You could optionally add a notation for the phase 2 person like “ \_ regionOfAuthority”. 

(You can write them as above, but currently “-quantity” is more reliable. For instance, “30 kilograms of wheat” is not correctly analyzed by the analyzer, but “wheat \-30 kilograms” is. Things like this may eventually get fixed.)

# **Writing Bible references**

# **Tod says to go ahead and write Bible references like “Isaiah 53:3” just like that, and the phase 2 person will fix it up. (That won’t be automatically analyzed correctly.)**

# **Marking Questionable Texts**

P1P should decide how to handle these as they come up because there are gradations in how questionable the text is. Refer to what modern translations do for guidance. The choices are:

* treat the text as regular text (Example: John 7:53-8:11)  
* include it but mark it as questionable text  
  * We have a feature for clauses called Location, and it has a value called Questionable Text.  A clause marked as Questionable Text can be anywhere in a verse.  
* mention it in a footnote (Example: Mark 9:29)  
  * And Jesus said to those followers/disciples, \["This kind of spirit will only leave a person \[if you(followers) pray\]"\]. (footnote) Some copies/manuscripts \_copyinLDV of this part of the Scriptures say, \["This kind of spirit will only leave a person \[if you(followers) pray\] \[and if you(followers) do not eat food \[so that you(followers) could pray\]\]"\]. (no brackets in He1 and  pronouns are okay)  
* not to mention it at all. (Example: KJV 1 John 5:7-8 vs. all other modern translations)

# **Using complex words**

A lot of the ideas in this document relate to the semantic complexity level of the words. For instance, you don’t have to worry about how to express a level 1 word. You just use it as a basic term. The semantic complexity level of words is shown in the ontology. You can find the numerical value in the TBTA ontology by doing a right-click in the row of a word and clicking on “Edit this concept’s semantic complexity level”. But you can also just see it from the color in the “Senses” column. More easily, you can see it in the TBTA ontology app. The notation “L\#” with “\#” having values between zero and four  will be surrounded by a box with the appropriate color listed below.

Words with blue background are supposed to be level 0, “semantic primitives” (very basic concepts).   
Words with a cream-colored background are level 1, simple.   
Words with magenta color are level 2, complex.   
And words with a green background are level 3 (concepts that are often expressed in a different way, like a noun that is more simply expressed with an adjective).   
Words with a brown background are proper names.   
**But keep in mind that there may be errors. Sometimes a word has a blue background because nobody set the complexity level of the word, and it defaulted to zero.** 

## **Using the Longman Defining Vocabulary**

Generally, we regard words in the Longman Defining Vocabulary (LDV) as simple. But there can be exceptions. You can see definitions of words in the online Longman Dictionary (https://www.ldoceonline.com/). Just like for our words, there can sometimes be several senses, which in the dictionary are numbered. The most commonly used sense is number 1\. If the word is in the LDV and the sense that you want to use is the first one, then you can probably start using that term and we will add it to the ontology. But if there is a long list of senses, and the sense that you want is far down on the list, that may be an indication that that sense of the word is uncommon, and we might need to consider whether we want to add it. So some discretion may be necessary here. But generally if I see a word in the LDV, and the sense that I want is the first or second sense in the Longman Dictionary, I assume that that word can be added to the ontology. 

**Adding complex words**  
**We can always add complex words if two conditions are met**.   
**First**, if that word occurs many times in the Bible (like 20 or over). We don’t want to bother the translator with having to deal with a special word that is only used once.   
**Second**, if you can pair it with a simpler word using the complex pairing, or if there is a straightforward explication in terms of simple words. An example is “consider”. That occurs many times in the New Testament epistles, and can be paired with “think”.

# **Special Notation**

## **Metonymy**

**Notation:** 	X of Y \_dynamicExpansion  
**Example:**	“Herod of the soldiers \_dynamicExpansion searched all of the boys.”   
(English BT (back translation)):   
\<\<The soldiers of\>\> Herod searched for all of the boys.”)

## **Using 3rd person for 1st or 2nd person**

**Notation:** 	X \_1stAs3rd  
**Example:** 	*P1* (phase 1): the Son-of-Man \_1stAs3rd  
		*BT* (English back translation): \<\<I, who am the\>\> Son of Man  
**Notation:** 	X \_2ndAs3rd  
**Example:** 	*P1:* my(David’s) Lord \_2ndAs3rd  
		*BT:* \<\<you,\>\> my Lord

## **Hyperbolic ‘all’**

**Notation:	“**all-B” (or “all \_hyperbolic”, meaning many)  
**Example:**	*P1: “*All-B the people \[who lived in Judea\] came \[in-order-to hear Jesus\].”  
*BT*: Use just “all”, and you can explain to the consultant if necessary that there is an option for that to be translated some other way, like with “many”

## **Language-specific words**

**Notation:**	The word of XLang named XWord means “Y”.  
**Example:**	The word of Aramaic named Abba means "father".

## 

# **Notes for P2**

Notes for P2 should be left in the P1 text (preferably) or as a comment below the text so that they can also be seen in Paratext. Here are some possible notations. But keep in mind that anything after “\_” is not interpreted by the program, so as long as you make it clear to P2, it  should be okay.  
instrument

| P1 In-text Notation | Meaning |
| :---- | :---- |
| \_addArg,  \_addInstrumentArg, etc | Marks a verb that requires an additional argument.**Example \- Mark 7:2**Those Pharisees and those people/scribes noticed \[some of Jesus's disciples eating food with religiously/ritually \_implicit dirty/unclean hands \_addArg\]. Those people's/disciple hands were not washed correctly \_implicit by those people/disciples \_implicitActiveAgent. This is a note to P2 to add an instrument argument to "eat". |
| \_addSense, \_addSenseDirectSpeechToSwear, etc | Marks a word that requires a new sense in the ontology.. **Example \- Mark 6:23** And Herod promised/swear \_addSense,   \["I(Herod) will give the thing \[that you(girl) ask-B to me(Herod) \_implicit \] to you(girl)\]. This is a note to P2 to add a sense of "swear" with direct speech. |
| \_Adj | Notifies P2 to choose the Adjective form of the marked word. |
| \_Adp | Notifies P2 to choose the Adposition form of the marked word. |
| \_Adv | Notifies P2 to choose the Adverb form of the marked word. |
| \_descriptive | Marks a relative clause as non-restrictive. |
| \_excl, \_incl | Marks a first person plural pronoun as exclusive or inclusive |
| \_inLDV | Marks a word that is in the Longman’s Defining Vocabulary and may be added to the ontology. **Example \- Matthew 7:2**And the measure  \_inLDV \[that you(people) use \[(implicit-situational) when you(person) judge other people\]\] will be the measure \[that you(people) will receive from God \_implicit\]. |
| \_1, \_2, \_3, …\_newNounIndex Note: The preferred notation is \_1, \_2, \_3, etc  | Indicates that a previously used noun is now used to refer to another person or thing **Example \- Mark 13:22**For false-B Christs and people \[who tell false-B messages \[that do not come from God\] to people\]  will come. Those people \_newNounIndex will do signs-B and actions \[that will surprise/amaze people\] But a more compact (and preferred) notation is For false-B Christs and people \_1 \[who tell false-B messages \[that do not come from God\] to people \_2\]  will come. Those people \_3 will do signs-B and actions \[that will surprise/amaze people \_4\] In the example, the marked “people” now includes both the false Christs and the false prophets. |
| \_plural | Notifies P2 that features should be marked plural. Used esp. with mass nouns, e.g., “money \_plural” |
| \_suggestiveLets | Marks a verb in a clause that requires the feature “Suggestive Let’s” (under “Illocutionary Force”). |
| \_jussive | Marks a verb to be jussive,  or third person imperative |

