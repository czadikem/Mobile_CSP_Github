# Sets

Sets are essentially a collection of similar words that you can use within a `<pattern>` tag to simplify the pattern matching capabilities. Instead of separate categories to capture every possible  grammar allowing the user to state that they like a color, we can have a single grammar that makes use of a set of colours, as follows

```xml
<category>
    <pattern> I LIKE THE COLOR <set name="colors"></pattern>
    <template>
        That is great, I like that color too.
    </template>
</category>
```

The set above references a name attribute with a value 'colors'. This references a file stored in the directory that is referenced by the configuration option
```yaml
console:
  storage:
    entities:
      sets: file

    stores:
      file:
        type: file
        config: 
          sets_storage:
             dirs: ..\..\storage\sets
             extension: txt
```

For more information on the settings, see the section [Brain File Configuration](./Config_Brain_Files)

If you were to add this grammar to your bot and execute. You can then ask any question about like a color, as long as that colors name is contained within the set file colors.txt
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> I like the color red
That is great, I like that color too.
>>> I like the color green
That is great, I like that color too.
```

## Creating your own Set
Lets create a new set for the types of cars.

1. Create a file and give it the name of the set you want to use. Don't worry about case, set name lookup is case insensitive, so cars.txt, CARS.txt and Cars.txt will all be considered the same set

2. Fill the set with names of all the cars you want in the set. Again don't worry about case, set contents lookup is case insensitive.
```txt
       Saab
       Ford
       Vauxhall
       Peugeot       
       Honda
       Nissan
       BMW
       Mercedes
```
3. Next, create a grammar that can make use of the set in the AIML folder of your bot.
```xml 
<category>
    <pattern> I DRIVE A <set name="cars"></pattern>
    <template>
        Hey, I have always wanted to drive one of them.
    </template>
</category>
```
4. Reload the bot, and check the log file to make sure that the new grammar has been loaded without any issues. 

5. You can now interact with your bot using the new grammar and set
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> I drive a Ford
Hey, I have always wanted to drive one of them.
>>> I drive a Saab
Hey, I have always wanted to drive one of them.
```

## Inbuilt Sets
Program-Y ships with a number of inbuilt sets that programmatically determine if a word is a member of a set. These are system-defined and hard-coded into the Brain. This is due to a number of sets being defined in the AIML 2.0 Draft Spec but not having a true implementation.

However, if you want to create your own programmatic sets, then I would suggest using Dynamic Sets as defined below. In fact, the inbuilt sets described in this section are all implemented as Dynamic Sets, just their implementation is hidden from the user.

Currently, the available inbuilt sets are 
* Numeric - Determines if a word is a numeric value
```xml 
<category>
    <pattern>PHONE <set name="numeric"></pattern>
    <template>
        OK, I am calling <star /> now for you.
    </template>
</category>
```

## Dynamic Sets
Dynamic sets allow the developer to add a programmatically verified set. By implementing a Python class based on a specific interface, the dynamic set can be included in the grammar. When the set tag is parsed as part of the matching process, the class is loaded and the interface is called. At this point, the developer can take the word passed in and implement any logic they feel necessary to determine if the word is part of the specific set.

Dynamic sets are configured in the following section of the config.yaml
```yaml
brain:
    dynamic:
        sets:
            numeric: programy.dynamic.sets.numeric.IsNumeric
            roman:   programy.dynamic.sets.roman.IsRomanNumeral
```
To read more about dynamic sets and to create them, see the wiki page [Dynamic Sets](./Dynamics#dsets)

See also [Dynamic Maps](./Dynamics#dmaps) and [Dynamic Variables](./Dynamics#dvars)

For more information about the template set tag, see the wiki page [Sets](./Pattern-Tags#set)
***
[Back to Tutorial](./AIML-Tutorial) | [Back - Pattern Matching](./Tutorial-Pattern-Matching) | [Next - Regular Expressions](./Tutorial-Regular-Expressions)
