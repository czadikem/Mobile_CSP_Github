## Properties
Properties provide a way to preload the bot with a set of name-value pairs, that you can then refer to during AIML execution. These 'bot' properties are stored in a configuration file as defined below
```yaml
brain:
    files:
        properties: $BOT_ROOT/config/properties.txt
```
The bot loads these properties are starting up. Each property is a name-value pair separated by a colon ':' as below. The bot treats the first colon as a separator and any other colons as part of the value element, so your value can contain URLS for example.
```text
name:Y-Bot
firstname:Y
middlename:AIML
lastname:BoT
fullname:Y-Bot

nationality:Scottish
ethnicity:Electronic
gender:male
species:robot
personality:helpful and fun
```
You can have any number of name-value pairs. However they should be unique, duplicates will result in the last value in the list overriding the preceding values.

To reference a property, you use the `bot` element as follows
```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">
    <category>
        <pattern>WHAT IS YOUR NAME</pattern>
        <template>My name is <bot name="name" /></template>
    <category>
    <category>
        <pattern>ARE YOU A MAN OR A WOMAN</pattern>
        <template>I am considered <bot name="gender" /> by many</template>
    <category>
</aiml>
```
Running this through the bot, you can then the properties in action as follows
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> What is your name
My name is Y-Bot
>>> Are you a man or a woman
I am considered male by many
```


***
[Back to Tutorial](./AIML-Tutorial) | [Back - Maps](./Tutorial-Maps) | [Next - Variables](./Tutorial-Variables)