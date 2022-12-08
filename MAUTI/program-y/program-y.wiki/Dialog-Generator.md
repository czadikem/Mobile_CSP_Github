Ever wanted to create a conversation will validation of entries and control over the flow of the dialogue, looping back to change previously entered values and finally being able to execute logic based on what their user is happy with. Well, BotFlow is here. BotFlow is a new dialogue generator, which from a simple CSV file, it will generate all the required AIML files.

As an example, imagine a basic flight booking system, that asks you were from and where do you want to fly, on what date, how many passengers and what class you want to fly. This can be defined in a basic CSV file as follows
```csv
Step,Prompt,Variable,Type,Next,Condition
SOURCE,Where would you like to fly from,Source,"Select(London Stanstead, London Heathrow, London Gatwick, Edinburgh, Glasgow, Manchester)",DEST, *
DEST,Where would you  like to fly to,Destination,"Select(New York, Washington, San Francisco)",DATE, *
DATE,When would you like to fly,Date,Date(DD/MM/YYYY),PASSENGERS, *
PASSENGERS,How many people are flying,Passengers,"Int(1,5)",CLASS, *
CLASS,What class do you want to fly,Class,"Select(Economy, Premium Economy, Business, First)",
```

Imagine running this through a simple command line which is able to create the following fully complete AIML File
```xml
<?xml version="1" encoding="UTF-8" ?>
<aiml>

	<category>
		<pattern>START FLIGHTBOOK</pattern>
		<template>
			<think>
				<set name="topic">FLIGHTBOOK</set>
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
				Where would you like to fly from - (London Stanstead, London Heathrow, London Gatwick, Edinburgh, Glasgow, Manchester)
			</template>
		</category>

		<category>
			<pattern>*</pattern>
			<that>Where would you like to fly from *</that>
			<template>
				<think><set name="Source"><star /></set></think>
				<condition name="Source">
					<li value="London Stanstead"><srai>FLIGHTBOOK STEP DEST</srai></li>
					<li value="London Heathrow"><srai>FLIGHTBOOK STEP DEST</srai></li>
					<li value="London Gatwick"><srai>FLIGHTBOOK STEP DEST</srai></li>
					<li value="Edinburgh"><srai>FLIGHTBOOK STEP DEST</srai></li>
					<li value="Glasgow"><srai>FLIGHTBOOK STEP DEST</srai></li>
					<li value="Manchester"><srai>FLIGHTBOOK STEP DEST</srai></li>
					<li><srai>FLIGHTBOOK STEP SOURCE</srai></li>
				</condition>
			</template>
		</category>

		<category>
			<pattern>
				FLIGHTBOOK STEP DEST
			</pattern>
			<template>
				Where would you  like to fly to - (New York, Washington, San Francisco)
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
			<pattern>
				FLIGHTBOOK STEP DATE
			</pattern>
			<template>
				When would you like to fly - ()
			</template>
		</category>

		<category>
			<pattern>*</pattern>
			<that>When would you like to fly *</that>
			<template>
				<think><set name="Date"><star /></set></think>
				<think><set name="Valid"><srai>VALID DATE <star /></srai></set></think>
				<condition name="Valid">
					<li value="true"><srai>FLIGHTBOOK STEP PASSENGERS</srai></li>
					<li><srai>FLIGHTBOOK STEP DATE</srai></li>
				</condition>
			</template>
		</category>

		<category>
			<pattern>
				FLIGHTBOOK STEP PASSENGERS
			</pattern>
			<template>
				How many people are flying - (1 to 5)
			</template>
		</category>

		<category>
			<pattern>*</pattern>
			<that>How many people are flying *</that>
			<template>
				<think><set name="Passengers"><star /></set></think>
				<think><set name="Valid"><srai>VALID INT <star /> 1 5</srai></set></think>
				<condition name="Valid">
					<li value="true"><srai>FLIGHTBOOK STEP CLASS</srai></li>
					<li><srai>FLIGHTBOOK STEP PASSENGERS</srai></li>
				</condition>
			</template>
		</category>

		<category>
			<pattern>
				FLIGHTBOOK STEP CLASS
			</pattern>
			<template>
				What class do you want to fly - (Economy, Premium Economy, Business, First)
			</template>
		</category>

		<category>
			<pattern>*</pattern>
			<that>What class do you want to fly *</that>
			<template>
				<think><set name="Class"><star /></set></think>
				<condition name="Class">
					<li value="Economy"><srai>EXIT FLIGHTBOOK</srai></li>
					<li value="Premium Economy"><srai>EXIT FLIGHTBOOK</srai></li>
					<li value="Business"><srai>EXIT FLIGHTBOOK</srai></li>
					<li value="First"><srai>EXIT FLIGHTBOOK</srai></li>
					<li><srai>FLIGHTBOOK STEP CLASS</srai></li>
				</condition>
			</template>
		</category>

		<category>
			<pattern>EXIT FLIGHTBOOK</pattern>
			<template>
				<get name="Source" />, 
				<get name="Destination" />, 
				<get name="Date" />, 
				<get name="Passengers" />, 
				<get name="Class" />, 
			</template>
		</category>

	</topic>

	<!-- Utilities -->

	<!-- Date Validation -->
	<category>
		<pattern>VALID DATE *</pattern>
		<template>true</template>
	</category>

	<!-- Integer Validation -->
	<!-- No Min or Max Range -->
	<category>
		<pattern>VALID INT *</pattern>
		<template>true</template>
	</category>
	<category>
	<!-- Max Range -->
		<pattern>VALID INT * *</pattern>
		<template>true</template>
	</category>
	<category>
	<!-- Min and Max Range -->
		<pattern>VALID INT * * *</pattern>
		<template>true</template>
	</category>

</aiml>
```
Its still work in progress, specifically the validators and some looping logic, but I think this has the power to get you up to advanced AIML development and an increased pace than previously possible.

Watch this space as we move into a Beta test of the tool....