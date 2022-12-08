# Maps
A map is a way to map the value of something to a different value. It provides the ability to carry out a number of lookups or conversions
* Convert the tense of a word, e.g be -> been
* Generalise the gender of a word, e.g man -> male, bot -> male, girl -> female
* Lookup the capital city, e.g Afghanistan -> Kabul, UK -> London
* Convert number to and from numeric and number, e.g 1 -> one, three -> 3

Program-Y supports 3 different types of maps
* File-based. Each mapping is stored in a single file in the maps folder
* Inbuilt. The system ships with a number of inbuilt mappings, e.g. Singular, Plural, Successor, Predecessor
* Dynamic. User-defined maps that programmatically map the value given to a new value

## File Based Maps

The location of each map file is configured using the maps section of the file seciton of the brain configuration in your configuration file

```yaml
  storage:
    entities:
      maps: file

    stores:

      file:
        type:   file
        config:
          maps_storage:
            dirs: ../../storage/maps
            extension: txt
```

Each map value consists of a number of name and value pairs separated by a ':'. As an example, the follows shows a snippet from the nation2capitol.txt mapping value which takes the name of a country and returns its capital city

```text
Uganda:Kampala
Ukraine:Kiev
United Arab Emirates:Abu Dhabi
United Kingdom:London
United States:Washington, D.C.
```
To use this in a grammar we use the `<map>` tag

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>I AM FROM THE *</pattern>
        <template>
             Cool, have you been to the capital city <map name="nation2capitol"><star /></map>
        </template>
    </category>
</aiml>
```

Running the bot with this grammar, allows us to answer the question about living in any country has an entry in the file

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> I live in the United Kingdom
Cool, have you been to the capital city London
>>> 
```

## Inbuilt Maps
AIML 2.0 defines a number of inbuilt maps which use code to map the value from one value to the next. Currently, AIML defines 4 such in-built maps
* Singular. Given a word attempts to create the singular version of the word by removing 's', 'es', or 'ies' from the word.Can also deal with words such as sheep -> sheep, and foot -> feet.
* Plural. Given a word attempts to create the plural by appending 's', 'es', or 'ies' to the word. Can also deal with words such as sheep -> sheep, and foot -> feet.
* Successor. Given a numeric value adds one to the value. E.g 99 -> 100
* Predecessor. Given a numeric value subtracts one from the value E.g 100 -> 99

### Singlular and Plural
Lets use an interested in animals to show how these grammars can be used

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>I WOULD LIKE A * AS A PET</pattern>
        <template>
             OK, how many <map name="plural"><star/></map> would you like?
        </template>
    <category>
    <category>
        <pattern>I HAVE * * AS PETS</pattern>
        <template>
             OK, whats the best thing about a <map name="singular"><star/></map>?
        </template>
    <category>
</aiml>
```
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> 
```

### Successor and Predecessor
Some very basic maths to demonstrate the us eof successor and predecessor
```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>WHAT IS ONE MORE THAN *</pattern>
        <template>
             That would be <map name="successor"><star/></map>
        </template>
    <category>
    <category>
        <pattern>WHAT IS ONE LESS THAN *</pattern>
        <template>
             That would be <map name="predecessor"><star/></map>
        </template>
    <category>
</aiml>
```
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> 
```

## Dynamic Maps
A more generalised version of the inbuilt maps is dynamic maps. Dynamic Maps are maps which, instead of loading their content from a text file, are instead a Python object. 

Dynamic Maps are loaded through config as defined below, which is a simple name-value pair, consisting of the name of the set and the full Python class.

```yaml
   dynamic:
        maps:
            romantodec: programy.parser.template.nodes.dynamic.maps.roman.MapRomanToDecimal
            dectoroman: programy.parser.template.nodes.dynamic.maps.roman.MapDecimalToRoman
```

The name is then used in the template 'map' tag as follows

```xml
    <template>
       <star /> is <map name="dectoroman"><star /></map> in Roman Numerals
    </template
````

Each object is an instantiation of the interface programy.dynamic.maps.map.DynamicMap. The method 'map_value' is called by the bot with the value to be mapped to a new value. At this point the developer has the the option to implement the mapping anyway they feel free. It could be algorithmic, a call to a database or a call to an external service.

```python
from abc import ABCMeta, abstractmethod

class DynamicMap(object):
    __metaclass__ = ABCMeta

    def __init__(self, config):
        self._config = config

    @property
    def config(self):
        return self._config

    @abstractmethod
    def map_value(self, bot, clientid, value):
        raise NotImplemented()
```

It's worth noting that all inbuilt maps are built using dynamic values, but they are loaded automatically and no not need to be specified in the dynamics section.

For more information on these tags, see the page [Dynamic Maps](./Dynamics#dmaps) and for more information on maps in general see the wiki page [Maps](./Template-Tags#map)

***
[Back to Tutorial](./AIML-Tutorial) | [Back - Random Selection](./Tutorial-Random-Selection) | [Next - Properties](./Tutorial-Properties)