# Sentiment Analysis

If enabled Program-Y calculates the positivity an the subjectivity of each sentence you ask it, and also keeps 
a running score of the overall conversation. The more you converse with it in a specific tone, the more it will start 
to respond to that tone.

The sentiment analyser keeps 2 scores

* Positivity
* Subjectivity

## Positivity
Polirity, as the name suggests refers to how positive the question and/or the running conversation is.
The more positive the questions, the higher the score, the more negative the lower the score.

The positivity score is a floating point numerical value between -1.0 and 1.0. The bot returns a textual value
to support grammar processing with the following values

* < -0.9 - EXTREMELY NEGATIVE
* \> -0.9 and score <= -0.7 - VERY NEGATIVE
* \> -0.7 and score <= -0.5 - QUITE NEGATIVE
* \> -0.5 and score <= -0.3 - NEGATIVE
* \> -0.3 and score <= -0.1 - SOMEWHAT NEGATIVE
* \> -0.1 and score <= 0.1 - NEUTRAL
* \> 0.1 and score <= 0.3 - SOMEWHAT POSITIVE
* \> 0.3 and score <= 0.5 - POSITIVE
* \> 0.5 and score <= 0.7 - QUITE POSITIVE
* \> 0.7 and score <= 0.9 - VERY POSITIVE
* \> 0.9 - EXTREMELY POSITIVE

#Subjectivity
A subjectivity score refers to how subjectivity or objective is the question and/or conversation. Objective refers to the fact
the questions reference actual people, places objects, where as a more subjective conversations are more based on feeling and mood.

Subjectivity is a numerical floating point value between 0.0 and 1.0. The bot returns a textual value
to support grammar processing with the following values

* score == 0.0 - COMPLETELY OBJECTIVE
* score > 0.0 and score <= 0.2 - MOSTLY OBJECTIVE
* score > 0.2 and score <= 0.4 - SOMEWHAT OBJECTIVE
* score > 0.4 and score <= 0.6 - NEUTRAL
* score > 0.6 and score <= 0.8 - SOMEWHAT SUBJECTIVE
* score > 0.8 and score < 1.0 - MOSTLY SUBJECTIVE
* score == 1.0 - COMPLETELY SUBJECTIVE

## Available Grammars

### Variables
At anytime during the conversation you can get the current positivity and subjectivity scores. 
These are stored in 2 variables which can be accessed via the 'get' template tag. As an example in AIML
```xml
	<category>
		<pattern>CONVERSATION SENTIMENT</pattern>
		<template>
			Current positivity is <get name="positivity" />, and subjectivity is
			<get name="subjectivity" />.
		</template>
	</category>
```

## Sentiment Extension

### Enabled
You can check if sentiment is enabled using the following 'SENTIMENT ENABLED' grammar. 
This will return either 'SENTIMENT ENABLED' or 'SENTIMENT DIABLED'. For example
```xml
	<category>
		<pattern>IS SENTIMENT ENABLED</pattern>
		<template>
			<extension path="programy.sentiment.extension.SentimentExtension" >SENTIMENT ENABLED</extension>
		</template>
	</category>
```

### Current Text Values

To get the textual version of sentiment scores, use the extention as follows
```xml
	<category>
		<pattern>CURRENT SENTIMENT TEXT</pattern>
		<template>
			<extension path="programy.sentiment.extension.SentimentExtension" >SENTIMENT CURRENT TEXT</extension>
		</template>
	</category>
```
This will return the following text

SENTIMENT SCORES POSITIVITY <positivity text> SUBJECTIVITY <subjectivity text>.

E.g.

SENTIMENT SCORES POSITIVITY SOMEWHAT POSITIVE SUBJECTIVITY NEUTRAL.

### Current Numberic Values
To get the numeric version of sentiment scores, use the extention as follows
```xml
	<category>
		<pattern>CURRENT SENTIMENT NUMERIC</pattern>
		<template>
			<extension path="programy.sentiment.extension.SentimentExtension" >SENTIMENT CURRENT NUMERIC</extension>
		</template>
	</category>
```

SENTIMENT SCORES POSITIVITY <positivity score> SUBJECTIVITY <subjectivity score>.

E.g.

SENTIMENT SCORES POSITIVITY 0.5 SUBJECTIVITY 0.6.

###Previous 
We can extract the sentiment of previous parts of the conversation. The following call to the extension
gives us the sentiment for the current conversation
```xml
	<category>
		<pattern>CALCULATE SENTIMENT FEELING OVERALL</pattern>
		<template>
			<extension path="programy.sentiment.extension.SentimentExtension" >SENTIMENT FEELING OVERALL</extension>
		</template>
	</category>

```
Where as the following call to the extension will extract the sentiment score for the last nth sentence 
```xml
	<category>
		<pattern>CALCULATE SENTIMENT FEELING LAST *</pattern>
		<template>
			<extension path="programy.sentiment.extension.SentimentExtension" >SENTIMENT FEELING LAST <star /></extension>
		</template>
	</category>
```

##Adhoc Sentiment Score
You can get the sentiment for a specific sentence using the following call to the extension
```xml
	<category>
		<pattern>CALCULATE SENTIMENT SCORE *</pattern>
		<template>
			<extension path="programy.sentiment.extension.SentimentExtension" >SENTIMENT SCORE <star /></extension>
		</template>
	</category>
```
This will return the following text string

SENTIMENT SCORES POSITIVITY <postivity text> SUBJECTIVITY <subjectivity text>.

E.g.

SENTIMENT SCORES POSITIVITY VERY NEGATIVE SUBJECTIVITY MOSTLY SUBJECTIVE.


###Numeric to Text Values
If you have the raw numeric values for positivity and/or subjectivity you can pull the text value
through a call to the extension with the following grammars. The numeric value should be 
denormalised first so 0.1 should 0 dot 1.

```xml
	<category>
		<pattern>GET SENTIMENT POSITIVITY *</pattern>
		<template>
			<extension path="programy.sentiment.extension.SentimentExtension" >SENTIMENT POSITIVITY <star /></extension>
		</template>
	</category>


	<category>
		<pattern>GET SENTIMENT SUBJECTIVITY *</pattern>
		<template>
			<extension path="programy.sentiment.extension.SentimentExtension" >SENTIMENT POSITIVITY <star /></extension>
		</template>
	</category>

```

