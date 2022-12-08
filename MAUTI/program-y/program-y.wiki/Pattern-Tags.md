# Index
This is the list of all currently supported AIML Pattern Matching tags by Program-Y.

Program-Y comes with its own set of additional tags which are not part of the official AIML 2.x spec, but have been added to make my life easier creating grammars. Use them if you are only ever going to use Program-Y, otherwise stick to the AIML 2.x compliant tags above.

* [bot](#bot)
* [iset](#iset)
* [oneormore](#oneormore)
* [priority](#priority)
* [regex](#regex)
* [set](#set)
* [template](#template)
* [topic](#topic)
* [that](#that)
* [word](#word)
* [zeroormore](#oneormore)

# Descriptions

This section provides detailed descriptions and examples for all currently supported AIML pattern nodes. The number after the name in [] brackets indicates which version of AIML the tag first appeared.

For details on pattern matching precedence rules, see [AIML Pattern Matching](./AIML-Pattern-Matching)

## bot<a name="bot"> [1.0]
This tag allows you to match a word against a pre-loaded bot predicate. These predicates are stored in properties.txt in the config folder as name:value pairs

In the example below, there will be a match if the user enters a sentence "I LIVE IN LONDON", and the predicate value for location is also London.

```xml
<category>
    <pattern>I LIVE IN <bot name="location" /></pattern
    <template>
        Hey I live there too!
    </template>
</category>
```
See Also: [iset](#iset), [set](#set)

## iset<a name="iset"> [1.0]
The iset tag is shorthand version of set. You would use an iset when you have a small number of set members that may only be used once in the entire grammar and you don't want to create a set file and have the set loaded at start time.

```xml
<category>
    <pattern>I LIVE IN <iset words="ENGLAND, IRELAND, SCOTLAND, WALES" /></pattern
    <template>
        Thats great, I live in the UK too!
    </template>
</category>
```
See Also: [bot](#bot), [set](#set)

## oneormore<a name="oneormore"> [1.0]
Matches one or more words until either end of sentence or another match is made.

In the example below, the grammar will match any sentence that starts with 'HELLO' and 1 or more additional words

There are 2 one or more characters which are used to control matching precedence. '_' is matched before set, bot iset, regex and words, but * is matched after these. For more details see [AIML Pattern Matching](./AIML-Pattern-Matching)
 
```xml
<category>
    <pattern>HELLO _</pattern
    <template>
        Hi There
    </template>
</category>

<category>
    <pattern>Hello *</pattern
    <template>
        Ho There
    </template>
</category>
```
See Also: [zeroormore](#zeroormore), [Precedence](./AIML-Pattern-Matching)

## priority<a name="priority"> [1.0]
Sometimes there is an exact match there we want to process a head of any wild card, set, bot or regex mapping. The priority character provides this mechanism. By preceeding a word with '$' the parser will always check for this word before applying any other matching patterns

In the example below, if there existed additional patterns for HELLO *, HELLO * FRIEND, etc, the priority grammar below would guarantee that HELLO THERE would be captured by that grammar

```xml
<category>
    <pattern>HELLO $THERE</pattern
    <template>
        Hi there
    </template>
</category>
```
See Also: [word](#word)

## regex<a name="regex"> [Program-Y]
An Program-y specific extension to pattern matching which allows you to allow regular expressions instead of specific words. One area where this is useful is in handling the difference between UK-English and American-English spelling.

Regex is availble as 2 options, the first is by specifying the regular expression as the 'pattern' attribute as below 

```xml
<category>
    <pattern>I DID NOT <regex pattern="^REALI[Z|S]E$" /> IT WAS THAT</pattern
    <template>
        OK, what did you think it was?
    </template>
</category>
```
The second option is to specify the name of a template which is stored within regex.txt file in the config folder. This options allows you to reuse the same regular expression in multiple places without having to copy the actual expression to each location
```
<category>
    <pattern>I DID NOT <regex template="realise" /> IT WAS THAT</pattern
    <template>
        OK, what did you think it was?
    </template>
</category>
```

## set<a name="set"> [1.0]
Allows a match against a set of related words. Sets are defined as a list of words, and each stored in the /sets folder in config. The name of the set is the name of the file containing the set of works, minus the extension.

In the example below, the set file united_kindgom.txt contains the works England, Ireland, Scotland and Wales. Any of these at the end of the sentence "I live in ..." would therefore match.

```xml
<category>
    <pattern>I LIVE IN <set name="united_kingdom" /></pattern>
    <template>
        Thats great, I live in the UK too!
    </template>
</category>
```
See Also: [bot](#bot), [iset](#iset)

## topic<a name="topic"> [1.0]
A topic element in the grammar allows you to restrict the matching when the topic value also matches. A topic is defined using the set templat tag as follows
```
<think><set name="topic">FISHING</set></think>
```
A question matching applies the topic first before seeing if there is a more general match. This is useful when you want to match the same question, for different contexts each of which require a different answer.

In the example below, the match occurs if the user asks the question "How do you know that?" in the context of talking to the bot about fishing. Given that a previous answers has set the topic as part of its response

```xml
<category>
    <pattern>HOW DO YOU KNOW THAT</pattern>
    <topic>FISHING</topic>
    <template>
        My father taught me when I was young.
    </template>
</category>
```
See Also: [that](#that), [set](./Template-Tags#set), [think](./Template-Tags#think)

## that<a name="that"> [1.0]
A 'that' tag allows the bot to continue a conversation, by matching a response both the question asked, and the response given in the previous sentence.

That is always set by the bot and will also be the most recent response given by the bot.

In the example below, a previous question will have resulted in the response "Eliza for president", if the user then asks "Please go on", the bot can provide a more contextual response as part of a natural conversation with context.

```xml
<category>
    <pattern>PLEASE GO ON</pattern>
    <that>ELIZA FOR PRESIDENT</that>
    <template>
        She is old enough, because she was born in 1966. And she was born in the U.S.
    </template>
</category>
```
See Also: [topic](#topic)

## word<a name="word"> [1.0]
The most basic matching operator in AIML, as simple as it sounds, any word without any special character or definition will be matched like for like regardless of case. 

In the example below, this grammar would match HELLO, hello, Hello, and even HeLlO.

```xml
<category>
    <pattern>HELLO</pattern
    <template>
        Hi there!
    </template>
</category>
```
See Also: [priority](#priority)

## zeroormore<a name="zeroormore"> [1.0]
Matches zero or more words until either end of sentence or another match is made.

In the example below, the grammar will match any sentence that is either 'HELLO' or a sentence that starts with 'HELLO' and 1 or more additional words

There are 2 one or more characters which are used to control matching precedence. '^' is matched before set, bot iset, regex and words, but # is matched after these. For more details see [AIML Pattern Matching](./AIML-Pattern-Matching)

```xml
<category>
    <pattern>Hello ^</pattern
    <template>
        Hi there
    </template>
</category>

<category>
    <pattern>Hello #</pattern
    <template>
        Hi there
    </template>
</category>
```
See Also: [oneormore](#oneormore), [Precedence](./AIML-Pattern-Matching)
