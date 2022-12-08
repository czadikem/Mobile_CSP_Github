# Regular Expressions

Regular expressions are a Program-Y only feature added during the development of AIML 2.0 support. Therefore if you are looking to maintain pure AIML 2.0 support I would suggest not using regular expressions. However, this niche feature is useful when you are dealing with such things as language idiosyncracies e.g colour vs color.

Regular expression support is provided in 2 ways

* Patterns - A single regular expression inline to the regex tag
* Templates - A name of a pattern which is stored in the regex-template.txt file

## Patterns
Pattern regular expressions are in line regex patterns, which are defined using the `pattern` attribute of the regex tag.

Let's add a pattern regular expression to handle the difference between the UK and American spelling of colour. The correct spelling is colour, but our friends across the pond drop the 'u' and spell it color.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>I LIKE THE <regex pattern="COL[O|OU]R" /> RED</pattern>
        <template>Wow, I like red too!</template>
    <category>
</aiml>
```

Running the bot with this grammar as below, shows we can ask the question using either spelling and get the same answer

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> I like the colour red
Wow, I like red too!
>>> I like the color red
Wow, I like red too!
>>> 
```

## Templates
Regular expressions templates use a file to store a list of regular expressions each with a unique name. The pattern is then referenced via the `template` attribute 

The regex template file is defined in the following section of the bot configuration
```yaml
console:
  storage:
    entities:
      regex: file

    stores:
      file:
        type: file
        config: 
          rege_storage:
             file: ..\..\storage\regex\regex-templates.txt
             extension: txt       
```

Let's add the same regular expression we used in the pattern example to the template file. 
```text
colour-spelling:COL[O|OU]R
```
Now we use the template variant of the regex tag
```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>I LIKE THE <regex template="colour-spelling" /> RED</pattern>
        <template>Wow, I like red too!</template>
    <category>
</aiml>
```

Running the bot now we get the same response as follows

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> I like the colour red
Wow, I like red too!
>>> I like the color red
Wow, I like red too!
>>> 
```

### Duplicate Entries
Be careful not to have these 2 grammars active in the same brain otherwise when the AIML is loaded you will get a duplicate warning. For more information on how to debug your aiml, see [Debugging Your AIML](./Debugging-Your-AIML)

For more information on the regex pattern tag including a full description of how to use it, see the wiki page [Regular Expressions](./Pattern-Tags#regex)

***
[Back to Tutorial](./AIML-Tutorial) | [Back - Sets](./Tutorial-Sets) | [Next - Symbolic Reduction](./Tutorial-Symbolic-Reduction)