# Dynamic Sets<a name="dsets">
Dynamic Sets are sets which, instead of loading their content from a text file, are instead a Python object. 

Dynamic Sets are loaded through config as defined below, which is a simple name value pair, consisting of the name of the set and the full Python class.
```yaml
   dynamic:
        sets:
            number: programy.parser.pattern.nodes.dynamic.sets.numeric.IsNumeric
            roman:   programy.parser.pattern.nodes.dynamic.sets.roman.IsRomanNumeral
```
The name is then used in the 'set' tag as follows
```xml
    <pattern>I like the number <set name="number" /> </pattern
````
Each object is an instantiation of the interface programy.dynamic.sets.set.DynamicSet. The method 'is_member' is called by the bot with the value to be checked for membership of the set. At this point the developer has the option to implement the check anyway they feel free. It could be algorithmic, a call to a database or a call to an external service.
```python
from abc import ABCMeta, abstractmethod

class DynamicSet(object):
    __metaclass__ = ABCMeta

    def __init__(self, config):
        self._config = config

    @property
    def config(self):
        return self._config

    @abstractmethod
    def is_member(self, bot, clientid, value):
        raise NotImplemented()
```

# Dynamic Maps<a name="dmaps">
Dynamic Maps are maps which, instead of loading their content from a text file, are instead a Python object. 

Dynamic Maps are loaded through config as defined below, which is a simple name value pair, consisting of the name of the set and the full Python class.
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

# Dynamic Variables<a name="dvars">
Dynamic variables are variables which, instead of loading static content from the bot, are instead a Python object. 

Dynamic variables are loaded through config as defined below, which is a simple name value pair, consisting of the name of the set and the full Python class.

```yaml
   dynamic:
        variables:
            gettime: programy.parser.template.nodes.dynamic.variables.datetime.GetTime
```

The name is then used in the template 'map' tag as follows

```xml
    <template>
       The time now is <get name="gettime" />
    </template
````

Each object is an instantiation of the interface programy.dynamic.vars.var.DynamicVariable. The method 'get_value' is called by the bot with the name of the variable to retrieve the value of. At this point the developer has the the option to implement the variable anyway they feel free. It could be algorithmic, a call to a database or a call to an external service.

```python
from abc import ABCMeta, abstractmethod


class DynamicVariable(object):
    __metaclass__ = ABCMeta

    def __init__(self, config):
        self._config = config

    @property
    def config(self):
        return self._config

    @abstractmethod
    def get_value(self, bot, clientid, value):
        raise NotImplemented()
```