# intern_work
The work done during my tenure of six months at IIIT Hyderabad in Natural Language Programming.
    Synopsis on
Mutual Bootstrapping in Alignment

INTRODUCTION
1.1. ORGANIZATION
Language Technologies Research Centre (LTRC), IIIT-H
The MT-NLP Lab at LTRC, IIIT-H, works in many different sub-areas of NLP including syntax and parsing, semantics and word sense disambiguation, discourse and treebanking, machine translation, etc. Computational models are built from linguistics, which is combined with machine learning techniques. The Lab and the Centre in general works on developing Computational Paninian Grammar (CPG) framework for Indian languages. By using such a framework, Treebank for Indian languages have been developed. These provide a rich testbed for studying and understanding the language in actual use and are also used for developing parsers using machine learning. This has given rise to full sentence parsers with broad coverage for Indian languages. 
Natural Language Processing or Computational Linguistics (NLP/CL) deals with understanding and developing computational theories of human language. These theories enable us to understand the structure of language and build computer software that can process language.NLP/CL is assumed to play a major role in facilitating man-machine communication as well as man-man communication. The objective is to create computer systems that can speak and listen to users, machines that can translate from one language to another, thus bringing about a virtual revolution in access to information. 
Creating a semantic PurposeNet, semantic category assigners, identifying semantic relations in nominals, etc are involved in Semantic processing. Machine translation (MT) has been a driving application in which intense research is being done. Work is going on for English to Hindi MT and MT from one Indian language to another.



Anusaaraka
Anusaaraka is:
A tool for overcoming language barriers
A better approach for building Machine Translation Systems.
Practical demonstration of the application of traditional ‘Shastras’ to solve contemporary problems.
Anusaaraka is an English-Hindi Language Translator Software. A machine translation tool with insights from Panini's Ashtadhyayi (Grammar rules). It is being developed by Chinmaya International Foundation (CIF), IIIT-H, and University of Hyderabad.
Anusaaraka is about the combination of traditional Indian shastras and advanced model technology. Anusaaraka is named from the Sanskrit word 'Anusaran' which means 'to follow'. It allows users to access text in any Indian language after translation from English language (source language).
Anusaaraka is a Natural Language Processing (NLP) Research and Development project undertaken by CIF. A machine translation system as it commits to provide the  users an output which gives them 100% faithful original text. This is accomplished by giving a layered output that shows how the given English text is translated into Hindi.
It aims to bridge the language barrier by allowing a user to enter an English text into Anusaaaraka and get the translation of a given text in any Indian language. English is being referred to as the source language and Hindi as a target language. In the distinct spirit of Chinmaya MissionAnusaaraka will be accessible for free under the General Public Licence (GPL). The approach for developing tools forAnusaaraka is Mutual Bootstrapping of NLP tools and language resources.
Anusaaraka follows the Rule-based approach in translations of the source language to the target language. It uses Stanford Parser which is statistical in nature. Anusaaraka provides the option of post editing by a skilled user. It considers language as an information encoding system wherein, information can be encoded at word, sentence or discourse level.
The idea behind the development of Anusaaraka is to build a Language Accessor tool and a state of the art Machine Translation System, work is in progress at many levels for all the available resources and methodologies such as Semantic Vectors, Alignment, Parallel Corpus, decision support tools, etc.
Machine Translation performs the substitution of words in one language for the corresponding words of another language; however the single substitution of the word usually cannot produce a reliable translation of the text, therefore for performing Machine Translation various tools are required.

1.2. PROBLEM DEFINITION

Bootstrapping or mutual bootstrapping in Anusaaraka is done using the Sentence Alignment module which facilitates comparison of all resources as placed next to each other for each sentence of the corpus. 
Parallel text alignment is important because during the translation process sentences are split, merged, deleted, inserted or reordered by the translator in order to create a natural translation in the target language. 
Due to lack of resources and inaccuracy of the ones available,the output of this module and hence,Anusaaraka isn’t robust. 
To improve translation there is a need to test and introduce more resources in order to make the system robust. There is also a need to improve the accuracy of Anusaaraka to get better translation. 





LITERATURE REVIEW
while there has been much research on x, few researchers have taken y into consideration

Disambiguating different senses of the word based on the context.(Literature Review : We did it to get a hand on CLIPS)

PROPOSED STUDY
AIMS AND OBJECTIVES
The major goal outlined in the report is to achieve a better translated output of Anusaaraka by mutualing bootstrapping multiple resources. The objectives leading upto the said goal are:
Integrating Transliteration of words from source language to desired language in mutual bootstrapping module
Disambiguating different senses of the word  in Anusaaraka
 based on the context
Aligning technical word substitution using Bharatvani domain specific dictionary in mutual bootstrapping module
Generating CLIP rules from the mutual bootstrapping  

RESEARCH METHODOLOGY
METHODOLOGY
Transliteration
Machine Transliteration System accepts characters of source language and map to the characters of the target language. The process is performed into two parts –Improving
(i) Segmentation Phase - In which words of the source
language are segmented into units 
(ii) Assembly phase - In which segmented characters are mapped to the
characters of target language with the help of rules.
Transliteration is particularly used to translate proper names and technical terms from source language.  It is an active module in Anusaaraka but not yet integrated in Alignment module formulated via mutual bootstrapping. 
The idea is to integrate Transliteration in Alignment module to improve the overall translation of the sentence and hence improve outputs of individual resources.
This can be done by detecting if a capital letter occurs in English sentence,except for the first letter of the sentence, that word and it’s proposed meaning in Hindi should be passed through Transliteration module to check if the said word is transliterate or not.

Word Sense Disambiguation
Word sense disambiguation module determines the final Hindi meaning of an ambiguous English word. This module uses the information from morph Analyser, POS tagger and Paninian relations, position and semantic property of the word to disambiguate to a final Hindi meaning. This module consists of thousands of manually written rules in CLIPS environment. The rule data-base is made up of two types of rules. 
One is the generalised rule which comes with the Anusaaraka software package and the other one is provisional (user given) rules written by the team working at Anusaaraka. Higher priority is given to the provisional rule, than the system rule. If no rule is present for a word, the default Hindi meaning is chosen from the bilingual dictionary. Multi-words are also translated with the help of a multi-word dictionary. 
As the system lacks accuracy and precision,the target is to achieve precision by polishing provisional rule. This will be done by analyzing the Parallel Corpora in Alignment module and observing where the system falters and find alternate better translation for words as opposed by other resources. The next task is to establish a formulated connection using POS taggers or Paninian relations with other words of the sentence followed by writing a provisional rule using CLIPS.

Linguistic Domain Specific Dictionary
This module provides the dictionary of aligned phrases in a specific Domain.The basic idea of this module is inspired from the work of old intern with added perspective and new version.The old version was not in maintainable so new version is designed from scratch.
English Phrases with high frequency where aligned with corresponding hindi phrases.

Anchor Fact Generation
Anusaaraka is working to adapt a new methodology for assigning translation to the words during Sentence Alignment. The new methodology will give a demarcation to each word during its first run. The words for which Alignment module suggests only one translation are called Starting Anchors and the for the on’s having more than one translation are assigned as Potential Anchors. Hence, this module acts as an assistive tool to generate various anchors (alternatively markers) in the form of facts in CLIP format to process a new layer of Alignment module.

WORK PLAN
Transliteration
In order to prepare a workflow for integrating Transliteration module in Sentence Alignment module, the first step is to understand how it functions in Anusaaraka. Upon understanding,the idea is to detect if a capital letter occurs in English sentence,except for the first letter of the sentence, that word and it’s proposed meaning in Hindi should be passed through Transliteration module occuring in Anusaaraka to check if the said word is transliterate or not. If there is a capital letter in the English sentence,in the same sentence in Hindi Corpus we pass the English word paired once with every word from the Hindi sentence and pass the pair through Transliteration module which ever pair matches will automated to give a CLIP fact for the Hindi transliteration of the English word.

Word Sense Disambiguation
To improve the accuracy of various senses of word, it is required to understand the working of Anusaaraka. Further on, understanding the purpose and need of provisional WSD rules. In order to be able to write accurate rules, it is also required to analysis how to establish a relationship between the word and other words of the sentence also known as Paninian relations and from where can these be fetched. After complete analysis, each word in the Corpora requires special attention and through analysis.

Linguistic Domain Specific Dictionary
For incorporating steps to be followed are : 
Data Extraction : Using Selenium, Raw data is to be extracted from bharatvani.in.  
Data Processing and Preparation : Extracted data is to be processed in a usable format of the dictionary.
Feature Engineering : After Data Pruning as per the requirement of our domain new words are to be added in the processed data.
Model Selection : After the final data, for the specific corpora, Lookup Dictionary is to be created from Original Dictionary using a specific format.
CLIPS Facts Generation : CLIPS facts are to be generated for further integration in the CLIPS modules.
CSV Creation : CSV for this specific resource is to be created for mutual-bootstrapping of all the resources. 
Anchor Fact Generation
The information required to generate facts is stored in a CSV file. Information after been read from the CSV file, will be converted in a fact depending on its type. If the word is described as Starting anchor, starting fact will be generated. If the word will be described as a Potential anchor, a potential fact will be generated. For all other words, unknown facts will be generated. This facts are further passed on to create a new layer in the Alignment module which acts as a resource to improve grouping information in Anusaaraka. 

PROPOSED CONTENTS OF THE THESIS
Final thesis proposes to develop a better mutual bootstrapping using Sentence Alignment module using multiple resources. For the same,that one has to identify the pairs or sets of sentences, phrases, and words in the original text and their correspondences in other languages.  
	

TOOLS AND TECHNIQUES
Sentence Alignment Tool
The tool does the sentence alignment using lexical information of the target language. The algorithm first passes the source language paragraph through Anusaaraka (Machine Translation system from English to Hindi). The source paragraph is broken into sentences and translated to target languages. The target language paragraph is also broken into sentences. Finally we will get both source and target languages in the form of sentences in the target language. The proposed algorithm uses shallow parser to extract the root words from translated source language and target language text for comparison. Scores were assigned according to number of matched possible words between translated source language and target language for each comparison. The algorithm then carries out the alignment of sentences using these scores. 

Word Sense Disambiguation (WSD)
English has a very rich source of systematic ambiguity. Majority of nouns in English can potentially be used as verbs. Therefore, the WSD task in case of English can be split into two classes: 
(i) WSD across POS 
(ii) WSD within POS 
The POS taggers can help in WSD when the ambiguity is across POSs. For example: Consider the two sentences 
‘He chairs the session’. 
‘The chairs in this room are comfortable’. 
The POS taggers mark the words with appropriate POS tags. These taggers use certain heuristic rules, and hence may sometimes go wrong. The reported performances of these POS taggers vary between 95% to 97%. However, they are still useful, since they reduce the search space for meanings substantially. 
However, disambiguation in the case of Polysemous words requires disambiguation rules. It is not an easy task to frame such rules. It is the context, which plays a crucial role in disambiguation. The context may be 
(i) The words in proximity, 
(ii) Other words in the sentence that are related to the word to be disambiguated. 
Based on the context,rules are written for peculiar senses.



CLIPS
CLIPS is designed to facilitate the development of software to model human knowledge or expertise. There are three ways to represent knowledge in CLIPS :
Rules, which are primarily intended for heuristic knowledge based on experience.
 Deffunctions and generic functions, which are primarily intended for procedural knowledge. 
 Object-oriented programming, also primarily intended for procedural knowledge. The five generally accepted features of object-oriented programming are supported: classes, message-handlers, abstraction, encapsulation, inheritance, and polymorphism. Rules may pattern match on objects and facts. 
We can develop software using only rules, only objects or a mixture of rules and objects. CLIPS is an excellent tool for word sense disambiguation . Based on the context, CLIP rules are written for different senses of the same word.
Bharatvani
Bharatvani is a project with the objective of delivering knowledge in and about all languages in India using multimedia (ie text, audio, video, images) formats through a portal (website).Bharatvani contain various subjects from agriculture to economics to sciences in 22 Indian languages.


Selenium
Selenium automates browsers. Primarily, it is for automating web applications for testing purposes, but is certainly not limited to just that. Selenium is a free (open source) automated testing suite for web applications across different browsers and platforms. Selenium focuses on automating web-based applications. Testing done using Selenium tool is usually referred as Selenium Testing.
Selenium is not just a single tool but a suite of software, each catering to different testing needs of an organization. It has four components.
Selenium Integrated Development Environment (IDE)
Selenium Remote Control (RC)
WebDriver
Selenium Grid
 
NMT
Neural Machine Translation is a machine translation approach that applies a large artificial neural network toward predicting the likelihood of a sequence of words, often in the form of whole sentences. Unlike statistical machine translation, which consumes more memory and time, neural machine translation, NMT, trains its parts end-to-end to maximize performance. NMT systems are quickly moving to the forefront of machine translation, recently outcompeting traditional forms of translation systems.

Anchoring Technique
In NLP, “anchoring” refers to the process of associating an internal response with some external or internal trigger so that the response may be quickly, and sometimes covertly, re-accessed. Anchoring is a process that on the surface is similar to the “conditioning” technique used by Pavlov to create a link between the hearing of a bell and salivation in dogs. By associating the sound of a bell with the act of giving food to his dogs, Pavlov found he could eventually just ring the bell and the dogs would start salivating even though no food was given. In the behaviorist’s stimulus-response conditioning formula, however, the stimulus is always an environmental cue and the response is always a specific behavioural action. The association is considered reflexive and not a matter of choice.

REFERENCES

Anusaaraka: An Expert System based Machine Translation System  by Sriram Chaudhary, Ankitha Rao, Dipti M Sharma

Statistical Vs Rule Based Machine Translation; A Case Study on Indian Language Perspective by Sreelekha S.

Comparison, Selection and Use of Sentence Alignment Algorithms for New Language Pairs by Anil Kumar Singh, Samar Husain

Adapting Link Grammar Parser (LGP) to Paninian Framework Mapping of Parser Relations for Indian Languages by Akshar Bharati, Dipti Misra Sharma, Sukhada

https://ltrc.iiit.ac.in/Anusaaraka/anu_home.html

https://www.thehindu.com/sci-tech/technology/bharatavani-portal-offers-digital-dictionaries-of-vanishing-indian-languages/article21249663.ece

http://clipsrules.sourceforge.net/OnlineDocs.html



