# Natural Language Processing
This version of program-y introduces significant enhancements in the area of Natural Language Processing. 
Build on the translations and sentinment analysis introduced in v3.9, v3.10 introduces the following NLP features

* Stop Words
  * Pre Processor
  * Dynamic Set
  * Post Question Processor
* Lemmatization
  * Dynmaic Map
  * Pre Processor
  * Post Question Processor
* Stemming
  * Dynamic Map
  * Post Question Processor
* Synsets
  * Dynamic Set
  * Extension
* Part of Speech (POS) Tagging
  * Post Question Processor
* NGrams
  * Post Question Processor
* Wordnet
  * Extension
 
For more details of Stemming and Lemmatization see the following link
* [Stanford](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html)
* [Wikipedia - Stemming](https://en.wikipedia.org/wiki/Stemming)
* [Wikipedia - Lemmatisation](https://en.wikipedia.org/wiki/Lemmatisation)
 
## Stop Words
The process of converting data to something a computer can understand is referred to as pre-processing. 
One of the major forms of pre-processing is to filter out useless data. In natural language processing, 
useless words (data), are referred to as stop words.

The full list of stop words which will be removed are the following
```json
{"ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", 
"very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", 
"of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", 
"themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", 
"her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", 
"ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", 
"in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", 
"did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", 
"which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", 
"doing", "it", "how", "further", "was", "here", "than"}
```

### Stop Word Pre Processing
There is now a pre processor you can use to remove stop words from your input text

To use this processor, add the following lines to preprocessing.conf
```ini
programy.processors.pre.stopwords.StopWordsPreProcessor
```

### Stop Word Post Question Processor
To use this processor, add the following lines to postquestionprocessing.conf
```ini
programy.processors.postquestion.stopwords.StopWordsPostQuestionProcessor
```
 
### Stop Word Set
You can also include a new dynamic set in your grammars which will tell you if a word is a stop word.
A typical category patter would be as follows. 
```xml
<category>
    <pattern>
        IS <set name="stopwords">*</set> A STOP WORD
    </pattern>
    <template>
        Yes <star /> is a stop word
    </template>
</category>
``` 
In the above example will the pattern matches if the single word matched by '*' is a stop word.

## Lemmatization
Reduduces a word to its base word, turning plurals etc into singulars, such as octopi to octopus or mice to mouse

### Dynmaic Map
The dynamic map will conver the word passed to it into its singlar form by using the maps as follows
```xml
<category>
    <pattern>
        WHAT IS THE SINGULAR NAME OF A *
    </pattern>
    <template>
        A singlular <star /> is called a <map name="lemmatizer" ><star /></map>
    </template>
</category>
```
This will only match if the lemmatize finds a value lemma, otherwise no match will occur

### Pre Processor
The preprocessor will attempt to lemmatize every word in the sentence passed in. This reducing all 
multiple terms to their singular version. To use this processor, add the following lines to preprocessing.conf
```ini
programy.processors.pre.lemmatize.LemmatizePreProcessor
```

### Post Question Processor
The post question processor, is called ( if configured ) when a sentence fails to match. The sentnce is lemmatized 
and the question asked again. To use this processor, add the following lines to postquestionprocessing.conf
 ```ini
programy.processors.postquestion.lemmatize.LemmatizePostQuestionProcessor
```
 
## Stemming
Stemming reduces all variants of a specific work down to the base word, e.g troubles, troubled and troubling
are all reduced to troubl. Note the 'e' is missing as the word 'troubl' is considered the base term in NLP.

### Dynamic Map
```xml
<category>
    <pattern>
        The base term of * is
    </pattern>
    <template>
        <map name="stemmer" ><star /></map>
    </template>
</category>
```

### Pre Processor
The pre process will apply stemming rules to all words of the sentence before it is parsed. 
To use this processor, add the following lines to preprocessing.conf
```ini
programy.processors.pre.stemming.StemmingPreProcessor
```

### Post Question Processor
The post question processor will stem the sentence after it failed to match a response, and then
ask the question again with stemming applied. To use this processor, add the following lines to postquestionprocessing.conf
```ini
programy.processors.postquestion.stemming.StemmingPostQuestionProcessor
```

## Synsets
Synsets are considered words which are similar to the original word, 
e.g the synsets of 'red' are the words 'red' and 'crimson', like wise
the synsets of 'hack' are 'hack', 'machine_politician', 'cab', 'chop'

### Dynamic Set
You can use a dynamic set, to check if a word is similar in you pattern match. This provides
a greater degree of flexibility in matching clauses
```xml
<category>
    <pattern>
       I WOULD LIKE A <set name="synsets" similar="dog">*</set>
    </pattern>
    <template>
        Me too, although I would like a cat too
    </template>
</category>
```
This pattern will now match to 'I WOULD LIKE A DOG', 'I WOULD LIKE A POUCH', 'I WOULD LIKE LIKE A PUPPY'
 
### Extension
You can use the extension provided to check if 2 words are similar as follows
```xml
<category>
    <pattern>
      SYNSETS SIMILAR * *
    </pattern>
    <template>
        <extension path="programy.nlp.synsets.extension.SynsetsExtension">
            SIMILAR <star index="1"/> <star index="2"/>
        </extension>
    </template>
</category>
```
 
## Part of Speech (POS) Tagging
Parts of Speech Tagging or POS Tagging carries out textual analysis on the text string and adds in 
identifiers for each work. Each identifier correlating to a part of speech such as noun, verb, adjective etc

For example the sentence 'Python is a high-level, general-purpose programming language.' will be converted into
the sentence ''Python NNP is VBZ a DT high-level JJ general-purpose JJ programming NN language NN'.

Note none of the meaning is lost, just additional identifiers are added to the text to help with parsing. 

You can now constructu a pattern grammar which looks for specific POS terms and matches the words as '*'s

### Pre Processor
The POS pre processor will convert the sentence into one in which all the words have had a POS tag associated with them. 
To use this processor, add the following lines to preprocessing.conf
```ini
programy.processors.pre.wordtagger.WordTaggerPreProcessor
```
 
## NGrams
NGrams are smaller sub sentences created from the original sentence, 
For example the sentence 'Now is better than never.', would produce the ngrams 
'Now is better', 'is better than' and 'better than never'

The default size is 3 words, but a future version of the NGrammer will allow this to be configured programmatically.

### Post Question Processor
The post question ngram processor will split the sentence into 3 word ngrams and ask each of the sentences. 
If it gets a result then that response will be returned. To use this processor, add the following lines to preprocessing.conf
```ini 
programy.processors.postquestion.ngrams.NGramsPostQuestionProcessor 
```
 
## WordNet Integration
WordNet is a database of 1000's of definitions of words. You can query the database and have it return the defintion
in you template grammar

### Extension
You can use the WordNet functionality as an extension as follows. This example will display the WordNet defintion
of any word the is matched to the '*'

```xml
<category>
    <pattern>
      WORDNET *
    </pattern>
    <template>
        <extension path="programy.nlp.wordnet.extension.WordNetExtension">
            <star />
        </extension>
    </template>
</category>
```
 
### Future Versions
Building on top of NLP capbilities, a future version will introduce Natural Langauge Understanding (NLU) enhancements in the form
of intent analysis. This will allow direct sentence to canonical form mapping of a category.
The NLU engine can be used in multiple places, either
* Pre Processor
* Sentence Repeat Processor
Converts you input sentence into intent, object, descriptors, e.g any combination of the following

        I want to book a flight from edinburgh to san francisco next wednesday at 3:00pm

maps directly to

        BOOK FLIGHT * FROM * TO * DATE *