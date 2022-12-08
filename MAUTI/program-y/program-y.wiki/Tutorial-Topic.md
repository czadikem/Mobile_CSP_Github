The topic tag is used as a way to group categories into related 'topics' typically to allow conversations to maintain a context of the topic being discussed and therefore to allow duplicates patterns with different responses depending upon the topic under discussions.

You set the `topic` that using a `set` tag as follows
```
    <category>
        <pattern>HELLO</pattern>
        <template>
            <think>
                <set name="topic">GREETINGS</set>
            </think>
            Hello there!
        </template>
    <category>
```

And you can retrieve the current topic using `get`
```
    <category>
        <pattern>SHOW TOPIC</pattern>
        <template>
            The current topic is <get name="topic" />
        </template>
    <category>
```

However, the primary use of `topic` is as a tag to group cateegories together.

```
<category>
    <pattern>I AM BORED</pattern>
    <template>
        OK, do you want to talk about sport?
        <think><set name="topic">SPORT</set></think>
    </template>
</category>

<topic name="SPORT">
    <pattern>YES</pattern>
    <template>
        What kind of sports do you like to play?
    </template>

    <pattern>NO</pattern>
    <template>
        OK, how about you choose a topic to talk about
    </template>

    <pattern>*</pattern>
    <template>
        Is there something else you'd like to talk about?
    </template>
</topic>
```

***
[Back to Tutorial](./AIML-Tutorial) | [Back - That](./Tutorial-That) | [Next - Conversations](./Tutorial-Conversations)