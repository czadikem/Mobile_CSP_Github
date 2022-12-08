
Program-y uses a customer process to split sentences. This works in nearly every case by splitting the text you enter
across boundaries defined by English sentences terminators such as full stop, colon, semi colon and brackets.

Once a sentence is split, Program-y parses each sentence and then combines all of the responses back into a single text output

However there is a time when you need to take the entire input and not have it split such as if a text block make have fullstop

You can control sentence splitting using System variable as defined using the process below

## System Variable

If its not added already to your config you need to add the dynamic variable called 'splitter' as follows

```yaml
dynamic:
    variables:
        gettime: programy.dynamic.variables.datetime.GetTime
        splitter: programy.dynamic.variables.system.splitter.SentenceSplitter
    sets:
        numeric: programy.dynamic.sets.numeric.IsNumeric
        roman:   programy.dynamic.sets.roman.IsRomanNumeral
    maps:
        romantodec: programy.dynamic.maps.roman.MapRomanToDecimal
        dectoroman: programy.dynamic.maps.roman.MapDecimalToRoman
```

## Example Grammar
Once you have restarted your bot you can use the following grammars to switch sentence splitting 'ON' and 'OFF'

```xml
<aiml>

	<category>
		<pattern>START USERNAME WITH SPLITTER ON</pattern>
		<template>
		    What is your username?
			<think>
				<set name="topic">ENTERUSERNAME</set>
				<set name="splitter">ON</set>
			</think>
		</template>
	</category>

	<category>
		<pattern>START USERNAME WITH SPLITTER OFF</pattern>
		<template>
		    What is your username?
			<think>
				<set name="topic">ENTERUSERNAME</set>
				<set name="splitter">OFF</set>
			</think>
		</template>
	</category>

	<topic>ENTERUSERNAME</topic>
	<category>
		<pattern>*</pattern>
		<template>Thanks, you entered <star /></template>
	</category>
```

## Example Output

If you used the above grammar you would see the following output when the splitter is switched on

```bash
START USERNAME WITH SPLITTER ON
fred.smith
Thanks, you entered fred. Thanks, you entered smith.
```

You would see the following output when the splitter is switched off

```bash
START USERNAME WITH SPLITTER OFF
fred.smith
Thanks, you entered fred.smith.
```


