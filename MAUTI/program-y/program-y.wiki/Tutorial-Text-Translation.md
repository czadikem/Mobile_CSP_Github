There are a number of AIML tags which allow you to control the formatting of the text within the template before it is displayed. 

* lowercase - Converts all text within the tags to lowercase
* uppercase - Converts all text within the tags to uppercase
* sentence - Converts all text to lower case, apart from the first letter of the first word which is converted to upper case
* formal - Converts all text to lowercase apart from the first letter of each word which is converted to upper case

## Lowercase
Converts all text within the tags to lowercase

```xml
<category>
    <pattern>CONVERT * TO LOWERCASE</pattern>
    <template>
        <lowercase><star /></lowercase>
    </template>
</category>
```

Running this through the Bot shows the lowercase in action

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> CONVERT AIML RULES TO LOWERCASE
aiml rules
```

## Uppercase
Converts all text between the start and end tags to uppercase

```xml
<category>
    <pattern>CHANGE * TO ALL UPPERCASE LETTERS</pattern>
    <template>
       <star/> in upper case is <uppercase><star /></uppercase>
    </template>
</category>
```

Executing this shows how text is converted to uppercase

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> CHANGE program-y TO ALL UPPERCASE LETTERS
programy in upper case is PROGRAM-Y
```

## Sentence
Converts all text between the start and end tags to lowercase, apart from the first letter of the first word which is converted to uppercase.

```xml
<category>
    <pattern>MAKE A SENTENCE OUT OF *</pattern>
    <template>
        <sentence><star/></sentence>
    </template>
</category>
```

If we add this grammar and start the bot we can see a sentence format created by the tag

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> MAKE A SENTENCE OUT OF i LiKE Programming
I like programming
```

## Formal
Converts all text to lower case, apart from the first letter of each word which is converted to upper case.

```xml
<category>
    <pattern>MY NAME IS * * </pattern>
    <template>
        Hello Mr <formal><star /></formal> <formal><star index="2"/></formal>
    </template>
</category>
```

Lets add this grammar and start the bot to see the tag in action

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> MY NAME IS KEITH STERLING
 Hello Mr Keith Sterling
```

***
[Back to Tutorial](./AIML-Tutorial) | [Back - Conversations](./Tutorial-Conversations) | [Next - Grammar Manipulation](./Tutorial-Langauge-Grammar-Manipulation)