# Dynamic Sets
Dynamic Sets are sets which, instead of loading their content from a text file, are instead a Python object. Each object is an instantiation of the interface programy.dynamic.sets.set.DynamicSet.

Dynamic Sets are loaded through config as defined below, which is a simple name value pair, consisting of the name of the set and the full Python class.
```yaml
   dynamic:
        sets:
            number: programy.parser.pattern.nodes.dynamic.sets.numeric.IsNumeric
            roman:   programy.parser.pattern.nodes.dynamic.sets.roman.IsRomanNumeral
```
For more information on Dynamic Sets please see [Dynamic Sets, Maps & Variables](./Dynamics)

# Dynamic Maps
Dynamic Maps are maps which, instead of loading their content from a text file, are instead a Python object. Each object is an instantiation of the interface programy.dynamic.maps.map.DynamicMap.

Dynamic Maps are loaded through config as defined below, which is a simple name value pair, consisting of the name of the set and the full Python class.
```yaml
   dynamic:
        maps:
            romantodec: programy.parser.template.nodes.dynamic.maps.roman.MapRomanToDecimal
            dectoroman: programy.parser.template.nodes.dynamic.maps.roman.MapDecimalToRoman
```
For more information on Dynamic Maps please see [Dynamic Sets, Maps & Variables](./Dynamics)

# Dynamic Variables
Dynamic variables are variables which, instead of loading static content from the bot, are instead a Python object. Each object is an instantiation of the interface programy.dynamic.vars.var.DynamicVariable.

Dynamic variables are loaded through config as defined below, which is a simple name value pair, consisting of the name of the set and the full Python class.

```yaml
   dynamic:
        variables:
            gettime: programy.parser.template.nodes.dynamic.variables.datetime.GetTime
```
For more information on Dynamic Sets please see [Dynamic Sets, Maps & Variables](./Dynamics)
