Ever wanted to create a conversation with full validation of entries and control over the flow of the dialogue, looping back to change previously entered values and finally being able to execute logic based on what the user is happy with. Well, BotFlow is here. BotFlow is a new dialogue flow generator, which from a simple CSV file, will generate all the required AIML files.

A new feature in v1.8.0 ( released today 16th Jan 2018 ) is Bot Dialog ( or Flow ) Generator. AIML can be a tough learning curve at times, and trying to learn the various mechanisms for controlling flow, validating input and handling execution requires some effort.

As an example, imagine a basic flight booking system, that asks you were from and where do you want to fly, on what date, how many passengers and what class you want to fly. This can be defined in a basic CSV file as follows
```csv
Step,Prompt,Variable,Type, Next, Condition
SOURCE,Where would you like to fly from,City,"Select(London, Edinburgh, Glasgow, Manchester)", DEST, =*, LONDON, =London
LONDON,Where from in London are you flying from,London,"Select(Stanstead, Heathrow, Gatwick)", DEST, =*
DEST,Where would you  like to fly to,Destination,"Select(New York, Washington, San Francisco)",DATE, =*
DATE,When would you like to fly,Date,Date(DD/MM/YYYY),PASSENGERS, =*
PASSENGERS,How many people are flying,Passengers,"Int(1,5)", CLASS, =*
CLASS,What class do you want to fly,Class,"Select(Economy, Premium Economy, Business, First)",
```
The steps are as follows
* SOURCE - Ask the user which city they want to fly from
* LONDON - If the user says London, an optional additional step that asks which airport in London to fly from
* DEST - Where do they want to fly to
* DATE - When do they want to fly
* PASSENGERS - How many are flying ( between 1 and 5 allowed )
* CLASS - Which class do they want to fly

Imagine running this through a simple command line which is able to create the following fully complete AIML File
```xml
<?xml version="1" encoding="UTF-8" ?>
<aiml>

	<category>
		<pattern>START FLIGHTBOOK</pattern>
		<template>
			<think>
				<set name="topic">FLIGHTBOOK</set>
				<set name="City" />
				<set name="London" />
				<set name="Destination" />
				<set name="Date" />
				<set name="Passengers" />
				<set name="Class" />
			</think>
			<srai>FLIGHTBOOK STEP SOURCE</srai>
		</template>
	</category>

	<topic name="FLIGHTBOOK">

		<category>
			<pattern>
				FLIGHTBOOK STEP SOURCE
			</pattern>
			<template>
				Where would you like to fly from - (London, Edinburgh, Glasgow, Manchester or exit)
			</template>
		</category>

		<category>
			<pattern>*</pattern>
			<that>Where would you like to fly from *</that>
			<template>
				<think><set name="City"><star /></set></think>
				<condition name="City">
					<li value="London"><srai>FLIGHTBOOK STEP  LONDON</srai></li>
					<li value="Edinburgh"><srai>FLIGHTBOOK STEP  DEST</srai></li>
					<li value="Glasgow"><srai>FLIGHTBOOK STEP  DEST</srai></li>
					<li value="Manchester"><srai>FLIGHTBOOK STEP  DEST</srai></li>
					<li><srai>FLIGHTBOOK STEP SOURCE</srai></li>
				</condition>
			</template>
		</category>

		<category>
			<pattern>EXIT</pattern>
			<that>Where would you like to fly from *</that>
			<template>
				<srai>EXIT FLIGHTBOOK</srai>
			</template>
		</category>

		<category>
			<pattern>
				FLIGHTBOOK STEP LONDON
			</pattern>
			<template>
				Where from in London are you flying from - (Stanstead, Heathrow, Gatwick or exit)
			</template>
		</category>

		<category>
			<pattern>*</pattern>
			<that>Where from in London are you flying from *</that>
			<template>
				<think><set name="London"><star /></set></think>
				<condition name="London">
					<li value="Stanstead"><srai>FLIGHTBOOK STEP  DEST</srai></li>
					<li value="Heathrow"><srai>FLIGHTBOOK STEP  DEST</srai></li>
					<li value="Gatwick"><srai>FLIGHTBOOK STEP  DEST</srai></li>
					<li><srai>FLIGHTBOOK STEP LONDON</srai></li>
				</condition>
			</template>
		</category>

		<category>
			<pattern>EXIT</pattern>
			<that>Where from in London are you flying from *</that>
			<template>
				<srai>EXIT FLIGHTBOOK</srai>
			</template>
		</category>

		<category>
			<pattern>
				FLIGHTBOOK STEP DEST
			</pattern>
			<template>
				Where would you  like to fly to - (New York, Washington, San Francisco or exit)
			</template>
		</category>

		<category>
			<pattern>*</pattern>
			<that>Where would you  like to fly to *</that>
			<template>
				<think><set name="Destination"><star /></set></think>
				<condition name="Destination">
					<li value="New York"><srai>FLIGHTBOOK STEP DATE</srai></li>
					<li value="Washington"><srai>FLIGHTBOOK STEP DATE</srai></li>
					<li value="San Francisco"><srai>FLIGHTBOOK STEP DATE</srai></li>
					<li><srai>FLIGHTBOOK STEP DEST</srai></li>
				</condition>
			</template>
		</category>

		<category>
			<pattern>EXIT</pattern>
			<that>Where would you  like to fly to *</that>
			<template>
				<srai>EXIT FLIGHTBOOK</srai>
			</template>
		</category>

		<category>
			<pattern>
				FLIGHTBOOK STEP DATE
			</pattern>
			<template>
				When would you like to fly - (DD/MM/YYYY or exit)
			</template>
		</category>

		<category>
			<pattern>*</pattern>
			<that>When would you like to fly *</that>
			<template>
				<think><set name="Date"><star /></set></think>
				<think><set name="Valid"><srai>VALID DATE <star /></srai></set></think>
				<condition name="Valid">
					<li value="TRUE"><srai>FLIGHTBOOK STEP PASSENGERS</srai></li>
					<li><srai>FLIGHTBOOK STEP DATE</srai></li>
				</condition>
			</template>
		</category>

		<category>
			<pattern>EXIT</pattern>
			<that>When would you like to fly *</that>
			<template>
				<srai>EXIT FLIGHTBOOK</srai>
			</template>
		</category>

		<category>
			<pattern>
				FLIGHTBOOK STEP PASSENGERS
			</pattern>
			<template>
				How many people are flying - (1 to 5 or exit)
			</template>
		</category>

		<category>
			<pattern>*</pattern>
			<that>How many people are flying *</that>
			<template>
				<think><set name="Passengers"><star /></set></think>
				<think><set name="Valid"><srai>VALID INT <star /> 1 5</srai></set></think>
				<condition name="Valid">
					<li value="TRUE"><srai>FLIGHTBOOK STEP  CLASS</srai></li>
					<li><srai>FLIGHTBOOK STEP PASSENGERS</srai></li>
				</condition>
			</template>
		</category>

		<category>
			<pattern>EXIT</pattern>
			<that>How many people are flying *</that>
			<template>
				<srai>EXIT FLIGHTBOOK</srai>
			</template>
		</category>

		<category>
			<pattern>
				FLIGHTBOOK STEP CLASS
			</pattern>
			<template>
				What class do you want to fly - (Economy, Premium Economy, Business, First or exit)
			</template>
		</category>

		<category>
			<pattern>*</pattern>
			<that>What class do you want to fly *</that>
			<template>
				<think><set name="Class"><star /></set></think>
				<condition name="Class">
					<li value="Economy"><srai>EXECUTE FLIGHTBOOK</srai></li>
					<li value="Premium Economy"><srai>EXECUTE FLIGHTBOOK</srai></li>
					<li value="Business"><srai>EXECUTE FLIGHTBOOK</srai></li>
					<li value="First"><srai>EXECUTE FLIGHTBOOK</srai></li>
					<li><srai>FLIGHTBOOK STEP CLASS</srai></li>
				</condition>
			</template>
		</category>

		<category>
			<pattern>EXIT</pattern>
			<that>What class do you want to fly *</that>
			<template>
				<srai>EXIT FLIGHTBOOK</srai>
			</template>
		</category>

	</topic>

</aiml>
```

## Configuration

The first line of the csv should have the follow headers
```csv
Step,Prompt,Variable,Type,Next,Condition
```

Each preceeding line should then match these columns headers as follows

* Step - The name of the step, used to direct the flow
* Prompt - Text to display as the question ( template )
* Variable - The name of the variable capturing the user input
* Type - The type of the variable ( see below )
* Next - Next Step ( repeats see below )
* Condition - The condition that would move the flow to the Next Step ( repeats see below )

### Type

BotFlow currently supports the follow types of variable

#### Int. 
An integer value that can have optional min and max restrictors
* Int         - Int no min or max value
* Int(m)      - Int with a max value
* Int(n,m)    - Int with a min n, and max m value
* If the validation fails then the same question is asked for again

#### Select. 
A list of items for the user to select from.
* Select(Item1, Item2, ... ItemN)  
* If the validation fails then the same question is asked for again

#### Date. 
A date value in the format dd/mm/yyyy
* A future release will allow the developer to set the date validation format
* If the validation fails then the same question is asked for again

### Entry/Exit
Flowbot creates a single entry step called START 'FLOWNAME', which you can call from outside of the flowbot grammar. Typically you would include in your grammar the following

```xml
    <category>
        <pattern>I WANT TO BOOK A FLIGHT</pattern>
        <template>
            <srai>START FLIGHTBOOK</srai>
        </template>
    </category>
```

When the conversation finishes, the bot calls EXECUTE 'FLOWNAME', This grammar is not included and you should create your own static grammar to pick up the variables and process them. An example would be

```xml
    <category>
        <pattern>EXECUTE FLIGHTBOOK</pattern>
        <template>
            Ok, I'll book a flight matching the following:
            flying from <get name="City" />,
            <get name="London" />,
            to <get name="Destination" />,
            on <get name="Date" />,
            with <get name="Passengers" /> passengers,
            in <get name="Class" /> Class,
        </template>
    </category>
```

### Next/Condition

A list of pairs consisting of a Destination tag which should be a valid step in a subsequent item and a condition for which the step should be moved to. Typically this is one of the items from a Select statement. The first of the pairs should be =* which is the default Step if no other validation succeeds or exists.

## Execution

Botflow is contained within the src\utils\botflow, there is a basic shell script for running the util
```bash
#!/usr/bin/env bash

clear

export PYTHONPATH=./src:.

python3 src/botflow.py -flow "../../../bots/botflow/flow/flightbook.csv" -topic flightbook -aiml "../../../bots/botflow/aiml"
```
This will execute the neccassary flow generator for a flight booking bot contained within bots\botflow folder.

The script takes 4 parameters
* -flow - CSV Flow file to load and process
* -topic - Topic name
* -lib - Library of aiml files. Flowbot uses prewritten aiml files for validation, these are copied into your aiml folder during the generation process
* -aiml - Directory to create aiml files in
