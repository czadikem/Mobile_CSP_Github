# Symbolic Reduction
A symbolic reduction is about reducing multiple different grammars down to a single one. This allows you to capture multiple ways in which to ask a single question, but then to have it all funnelled into a single grammar that does the work. This greatly reduces complexity and duplication of effort when working with large grammars

Imagine all the different ways you can say hello to someone, but the answer is always going to be the same ( Later on we'll see how we can create multiple responses to the same question, but let's keep it simple for now ) 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">

    <category>
        <pattern>HELLO</pattern>
        <template>
            <srai>HELLO_RESPONSE</srai>
       </template>
    <category>

    <category>
        <pattern>HI</pattern>
        <template>
            <srai>HELLO_RESPONSE</srai>
       </template>
    <category>

    <category>
        <pattern>GOOD MORNING</pattern>
        <template>
            <srai>HELLO_RESPONSE</srai>
       </template>
    <category>

    <category>
        <pattern>HELLO_RESPONSE</pattern>
        <template>
            <srai>Hi there!</srai>
       </template>
    <category>

</aiml>
```
If we now run the bot with this new grammar, we can see we can ask it various versions of hello and get the same response back

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> Hello
Hi there!
>>> Hi
Hi there!
>>> Good morning
Hi there!
>>> 
```

# Pattern Matching
We can reduce the number of grammars required down further by using pattern matching we learnt about in the previous section

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">

    <category>
        <pattern>HELLO *</pattern>
        <template>
            <srai>HELLO_RESPONSE</srai>
       </template>
    <category>

    <category>
        <pattern>HI *</pattern>
        <template>
            <srai>HELLO_RESPONSE</srai>
       </template>
    <category>

    <category>
        <pattern>GOOD *</pattern>
        <template>
            <srai>HELLO_RESPONSE</srai>
       </template>
    <category>

    <category>
        <pattern>HELLO_RESPONSE</pattern>
        <template>
            <srai>Hi there!</srai>
       </template>
    <category>

</aiml>
```

Now when we run the bot with this new grammar, we can see we can ask it an even wider range of different ways to say hello and get the same response back

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> Hello
Hi there!
>>> Hello there
Hi there!
>>> Good morning
Hi there!
>>> Good afternoon friend
Hi there!
>>> 
```
For more details about this tag see [srai tag](./Template-Tags#srai)

## SRAI Shorthand
As we saw in the section on Pattern Matching, you can access the words which matched the wildcard using the `<star>` tag. Quite often when developing AIML grammars, you will use a combination of symbolic reduction and pattern matching. AIML provides a shorthand to help with this in the form of the `<sr/>` tag

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">

    <category>
        <pattern>GOOD *</pattern>
        <template>
            <srai><sr/></srai>
       </template>
    <category>

    <category>
        <pattern>MORNING</pattern>
        <template>
            <srai>Good morning, did you sleep well?</srai>
       </template>
    <category>

    <category>
        <pattern>AFTERNOON</pattern>
        <template>
            <srai>Good afternoon, time for lunch?</srai>
       </template>
    <category>

    <category>
        <pattern>EVENING</pattern>
        <template>
            <srai>Good evening, bedtime?</srai>
       </template>
    <category>

</aiml>
```

For more details on this tag see [sr tag](./Template-Tags#sr)

***
[Back to Tutorial](./AIML-Tutorial) | [Back - Regular Expressions](./Tutorial-Regular-Expressions) | [Next - Random Selection](./Tutorial-Random-Selection)