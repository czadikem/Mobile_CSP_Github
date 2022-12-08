## AIML XML Files
All AIML files start the same way, with an XML declaration and a root level tag

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
</aiml>
```

## Basic Question and Answer
When you boil it down to the basics, all AIML interactions are made up of 2 parts, a question and an answer. Each interaction is called a 'category', the question is a 'pattern' and the 'answer' is a template. These take the form like 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>HELLO</pattern>
        <template>Hi there!</template>
    </category>
</aiml>
```

Create a file in the \storage\categories folder called `hello.aiml` and xml from above into the file, then save it.

AIML uses the pattern to match the incoming text you type into Y-Bot, and if it finds a match it executes and prints out the template. 

To run the bot, use the .sh or .cmd script from the previous section depending upon whether you are on Linux, Mac or Windows.

Running the bot with the above grammar and entering Hello as a question will show the following response.

```
Loading, please wait...
No bot root argument set, defaulting to [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/y-bot]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> Hello
Hi there!
>>> 
```
Congratulations you have created your first AIML Chatbot and given it enough knowledge to answer a basic question.
Next we'll look at pattern matching in more details.
 
***
[Back to Tutorial](./AIML-Tutorial) | [Back - Bot Template](./Tutorial-Bot-Template) | [Next - Pattern Matching](./Tutorial-Pattern-Matching)