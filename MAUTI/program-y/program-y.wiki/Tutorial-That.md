The `that` tag allows you to create conversations, along with `topic` you can create multi-part questions and answers, where follow-on questions can use the context of the previous response to influence the context of the next response/question.

Imagine a conversation in which you asked the bot a question, "What other AIs do you know" and it responded with "I have spoken to HAL before". If you then asked "Was he friendly" the conversation needs to know how to respond in the context of referring to the previous question about HAL. 

```
    <category>
        <pattern>WHAT OTHER AIS DO YOU KNOW</pattern>
        <template>I have spoken to HAL before</template>
    <category>

    <category>
        <pattern>* FRIENDLY</pattern>
        <that>I have spoken to HAL before</that>
        <template>No, he seemed a little unhinged actually!</template>
    <category>
```

Another example is to use `that` when you need to handle basic responses that may be repeated multiple times such as Yes and No responses.

```
    <category>
        <pattern>COMEDY SCI FI</pattern>
        <template>Do you like Red Dwarf?</template>
    <category>

    <category>
        <pattern>YES</pattern>
        <that>Do you like Red Dwarf</that>
        <template>Awesome, my favourite character is Kryten</template>
    <category>

    <category>
        <pattern>NO</pattern>
        <that>Do you like Red Dwarf</that>
        <template>Thats a shame, you should give it a second change.</template>
    <category>
```
In this instance no matter how many YES/NO patterns you have, if the bot responds with 'Do you like Red Dwarf?', then if the next response is YES or NO, it will first be matched against the patterns above

***
[Back to Tutorial](./AIML-Tutorial) | [Back - System Information](./Tutorial-System-Information) | [Next - Topic](./Tutorial-Topic)