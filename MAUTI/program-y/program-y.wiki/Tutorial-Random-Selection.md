# Randomness

The `<random>` tag allows the AIML developer to add a level of 'humanness' to the response to any question. It provides the ability to respond in multiple different ways to the same question. A random tag is made up of one or more 'list items'  or `<li>` tags. Each list tag can contain anything that you would normally place within a template tag.

If the example below we have decided to provide a random response to the question HELLO. 
```xml
<category>
    <pattern>HELLO</pattern>
    <template>
        <random>
            <li>Hi there!</li>
            <li>Hiya</li>
            <li>Hello there</li>
            <li>Yo!</li>
        </random>
    </template>
</category>
```
Adding this grammat to your bot and running the console, you can now ask Hello and receive a random response as follows.
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> Hello
Hiya
>>> Hello
Hi there!
>>> Hello
Yo
>>> Hello
Hi there!
```

## Complex Conditional Statements
The `<li>` tag can contain any other template tags, which provides the option to build complex conditional and logic statements. In the example below HELLO is expanded to add a little more variance and humanism to the response.
```xml
<category>
    <pattern>
        HELLO
    </pattern>
    <template>
        <random>
            <li>Hello!</li>
            <li>Hi there!</li>
            <li>Greetings!</li>
            <li>Hiya!</li>
            <li>
                <think><set name="dayphase"><srai>DAY PHASE</srai></set></think>
                <condition name="dayphase">
                    <li value="Morning">Good morning.</li>
                    <li value="Noon">Good afternoon.</li>
                    <li value="Afternoon">Good afternoon.</li>
                    <li value="Night">Good evening.</li>
                    <li>Hello!</li>
                </condition>
            </li>
        </random>
    </template>
</category>
```

For a detailed description of the random tag, see the Wiki page [Random](./Template-Tags#random)
***
[Back to Tutorial](./AIML-Tutorial) | [Back - Symbolic Reduction](./Tutorial-Symbolic-Reduction) | [Next - Maps](./Tutorial-Maps)