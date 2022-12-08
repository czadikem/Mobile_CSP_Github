## Variables
Variables provide a way to retain values during the execution of a conversation. There are 2 types of variables
* Global - Retain the value for the duration of the conversation and are persistent between bot execution
* Local - Only relevant to the current question and answer. Not persisted between not executions.
Varaibles are accessed by using the `get` and `set` aiml tags

### Global
Global variables are typically used to save long-running state such as the name of the user asking the questions or information that the bot would use later on in the conversation. The are defined by using the `name` attribute of the `get` and `set` AIML tags
```xml
    <category>
        <pattern>MY NAME IS *</pattern>
        <template>
            Hello <star />, nice to meet you.
            <think><set name="username"><star /></set></think>
        </template>
    </category>
    <get name="someproperty" />
```
Some time later during another part of the conversation
```xml
    <category>
        <pattern>HOW ARE YOU</pattern>
        <template>
            I am very well <get name="username" />, how are you.
        </template>
    </category>
```

### Local
Local variables differ from Global variables in that they are not persisted for the entire conversation, instead, they are only relevant for the specific question they are contained within. They can be used to store temporary data that is passed between various elements of the template processing.
```xml
    <category>
        <pattern>MY NAME IS *</pattern>
        <template>
            <think>
                <set var="firstname"><first><star/></first></set>
                <set var="remaining"><rest><star/></rest></set>
            </think>
            Hello <get var="firstname" />, how are you. I like your name,
            I think <get var="firstname" /> is a great first name
        </template>
    </category>
```
In this example we parse the entered string into local variables firstname and remaining, so that we can use firstname multiples times without each time having to parse the string.

Local variables are useful when used in Conditional statements as defined in the next statement

For more information on using variables see [set](./Template-Tags#set) and [get](.//Template-Tags#get) and for more information on how to use properties see [bot](./Template-Tags#bot)

***
[Back to Tutorial](./AIML-Tutorial) | [Back - Properties](./Tutorial-Properties) | [Next - Conditions](./Tutorial-Conditions)