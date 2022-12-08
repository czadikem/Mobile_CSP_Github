The ability to process a string of words individually is a key component of any language parsing tool and AIML is no different. AIML provides 2 tags to split and combine single words into a string of individual letters separated by spaces, and then 2 functions which operate on any string of words or letters separated by strings.

* explode - Convert a single word into a string of individual letters separated by spaces.
* implode - Take a string of letters or words separated by spaces and combine into a single string with no spaces.
* first - Return the first element of a string of space-separated words.
* rest - Return all but the first element of a string of space-separated words.

## Explode
Convert a single word into a string of individual letters separated by spaces.

```xml
<category>
    <pattern>WHAT ARE THE LETTERS OF *</pattern>
    <template>
        <explode><star /></explode>
    </template>
</category>
```
	
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> WHAT ARE THE LETTERS OF IBM
I B M
```

## Implode
Take a string of letters or words separated by spaces and combine into a single string with no spaces.

```xml
<category>
    <pattern>IMPLODE </pattern>
    <template>
        <implode><star /></implode>
    </template>
</category>
```
	
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> IMPLODE I B M
IBM
```

## First
Return the first element of a string of space-separated words.

```xml
<category>
    <pattern>FIRST WORD OF *</pattern>
    <template>
        <first><star /></first>
    </template>
</category>
```
	
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> FIRST WORD OF THE QUICK BROWN FOX
THE
```

## Rest
Return all but the first element of a string of space-separated words.

```xml
<category>
    <pattern>EVERYTHING BUT THE FIRST WORD OF * </pattern>
    <template>
        <rest><star /></rest>
    </template>
</category>
```
	
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> Everything but the first word of the quick brown fox
quick brown fox
```

***
[Back to Tutorial](./AIML-Tutorial) | [Back - Grammar Manipulation)](./Tutorial-Langauge-Grammar-Manipulation) | [Next - Knowledge Management](./Tutorial-Knowledge)
