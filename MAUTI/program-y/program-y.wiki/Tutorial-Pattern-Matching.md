## Pattern Matching

You can build a lot of simple questions and answers with this form, but it becomes unmanageable when you get to very large numbers. You end up repeating yourself and trying to guess every possible combination of a question someone might ask.

To solve this problem AIML comes with power pattern matching capabilities. Instead of including every possible world in every possible combination, an AIML developer uses special syntax which can be used to match one or more words. This allows the AIML developer to focus on the core aspects of the question. 

The purpose of this is to allow the developer to ignore the unimportant parts of the question and focus only on the core aspects. As with most languages there many different ways to ask the question, but most are just variations on a core theme. This is where pattern matching helps.

These matching operators are

* Priority. Matches the exact word specified by proceeding the word with a $
* 0 or more. Matches 0 or more words in a sequence. Can be either # or ^ depending upon precedence preference
* 1 or more. Matches 1 or more words in a sequence. Can be either _ or * depending upon precedence preference
* Sets. Matches a word as a member of a specific set. Sets are files of words, each file contains one set, such as colours or numbers.
* ISet. Similar to sets but, but the members are contained inline to the AIML
* Bot. Matches a word again a bot predicate, such as bot name, age, location etc
* Regex. Matches a one-word regular expression

For more information on pattern matching and operator, precedence see [Pattern Matching](./AIML-Pattern-Matching)

### 0 or More Matching
The special characters `#` or `^` where added in AIML 2.0 and mean matching zero or more words before either the next specific match or the end of the sentence.

For example `HELLO #` would match any sentence that starts with the word `HELLO` and has zero or more words.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>HELLO #</pattern>
        <template>Hi there!</template>
    <category>
</aiml>
```

### 1 or More Matching
The special characters `_` or `*` are used to match one of more words after the specified word before the next specific match or the end of the sentence. 

For example `HELLO *` will match any two word or more sentence starting with `HELLO`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>HELLO</pattern>
        <template>Hi there!</template>
    <category>
</aiml>
```

### Priority Matching
The priority special char `$` is normally used when a zero or more, or one or more special character is included and you want to seperate out a specific word, but allow all other zero or one or more combinations to pass through

In the example below we watch to match all sentences whic start `HELLO...` but if any sentence starts `HELLO FRIEND` we give a slightly different answer to every other combination. In this example we use zero or more match.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>HELLO $FRIEND #</pattern>
        <template>Hi there, friend!</template>
    <category>

    <category>
        <pattern>HELLO *</pattern>
        <template>Hi there!</template>
    <category>
</aiml>
```

### Set Matching
Sets are defined in a later section [Sets Tutorial](./Tutorial-Sets) and more info can be found in [Sets](./Pattern-Tags#set). Sets are essentially collections of common words. When matching, the system looks at the name of the set and then tries to match the given word by checking if it is a member of the set

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>I LIKE THE COLOR <set name="colors" /></pattern>
        <template>I LIKE THAT COLOR TOO!</template>
    <category>
</aiml>
```

### iSet Mactching
Sets are defined in a later section [Sets Tutorial](./Tutorial-Sets) and more info can be found in [iSets](./Pattern-Tags#iset). Similar to sets, isets are inline sets that rather than specify the collection of words in a file, you specify them in line to the XML. Matching is the same as for sets, the word is checked for membership of the iset words listed.

In the example below, the grammar will match either HELLO THERE, HI THERE and YO THERE, providing the same answer for each sentenec.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern><iset words="HELLO, HI, YO" /> THERE</pattern>
        <template>Hi there!</template>
    <category>
</aiml>
```

### Bot Matching
Bots are defined in a later section [Properties Tutorial](./Tutorial-Properties) and more info can be found in [Sets](.//Pattern-Tags#bot). Bots are aware to access a specific bot defined property.

In tbe example below, if the bot has a property called `location` and its value is `Scotland` and the user enters the statement `I LIVE IN SCOTLAND`, the bot will reply `Hey I live there too.`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>I LIVE IN <bot name="location" /></pattern>
        <template>Hey, I live there too!</template>
    <category>
</aiml>
```

### Regex Matching
Bots are defined in a later section [Properties Regular Expressions](./Tutorial-Regular-Expressions) and more info can be found in [Regular Expressions](.//Pattern-Tags#regex). A regex is useful to allow a grammar developer to create matches that match against regular expressions.

In the example below, a regular expression is used to match either `COLOR` or COLOUR` this dealing with the difference in English spellings of that word.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>I LIKE THE <regex pattern="COL[O|OU]R" /> RED</pattern>
        <template>I like the colour red too!</template>
    <category>
</aiml>
```

### Multiple Wild Card Matching
```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>HELLO * *</pattern>
        <template>Hi there!</template>
    <category>
</aiml>
```

### Operator Precedence 
In terms of precedence, the parser checks for each type of matching in a specific order defined by the following rules

```
	Precedence
		$	Priority
		#	0 or more
		_ 	1 or more
		word
		set
		iset		
		bot
		regex
                word
		^	0 or more
		*	1 or more
```

## Star matching
For every type of wildcard matching defined above, the system provides access to the word or words which match the wild card. This is provided through the use of the `<star>` tag.

In the example below, we extend the question we defined earlier about liking the colour red to like any colour.
Here the tag `star` will contain all of the words that matched after COLOR. This is a simplistic example and will match anything after COLOR and therefore as well as matching colours will match anything else after the colour in the sentence.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>I LIKE THE COLOR *</pattern>
        <template>I LIKE <star /> TOO </template>
    <category>
</aiml>
```

The `star` tag also provides an index to allow you to specifiy which star in the sentence was matched against which word or words.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>MY FIRST NAME IS * AND MY SURNAME IS *</pattern>
        <template>NICE TO MEET YOU <star index="1"/> <star index="2" /></template>
    <category>
</aiml>
```
The index is one based and therefore `<star/>` is identical to `<star index="1" />`

The star matches are as follows

* 0 or more. The word or words that matched, this can be empty string or zero words match.
* 1 or more. The word or words that matched the wildcard.
* Sets. The word that matched, as was proven to be a member of the set.
* ISet. The word that matched, as was proven to be a member of the set.
* Bot. The value of the bot property that matched.
* Regex. The value of the word which matched the regular expression.

### Multiple Wildcards
When multiple wild cards are combined, there are a number of rules the system uses to match zero or more words to each wild card. 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>HELLO * #</pattern>
        <template></template>
    <category>
</aiml>
```

In the example above, the first word after HELLO is matched to the `*` and then any more words after that are matched to `#`

***
[Back to Tutorial](./AIML-Tutorial) | [Back - Getting Started](./Tutorial-Getting-Started) | [Next - Sets](./Tutorial-Sets)