There are a number of AIML tags which provide access to underlying system information, these include

* id - Gives the client id
* program - Gives the version of the Bot
* size - Returns the number of categories loaded
* vocabulary - Returns the total number of distinct words known by the bot

## ID

```xml
<category>
    <pattern>Tell me you client id</pattern>
    <template>
        My clent id is <id />
    </template>
</category>
```

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> Tell me you client id
My client id is Console
```

## Program

```xml
<category>
    <pattern>VERSION INFO</pattern>
    <template>
        I am currently at version <program />
    </template>
</category>
```

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> VERSION INFO
I am currently at version Y-Bot 0.0.1
```

## Size

```xml
<category>
    <pattern>WHAT DO YOU KNOW</pattern>
    <template>
        My brain contains<size /> categories.
    </template>
</category>
```

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> WHAT DO YOU KNOW
My brain contains 8268 categories.
```

## Vocabulary

```xml
<category>
    <pattern>HOW BIG IS YOUR BRAIN</pattern>
    <template>
        I am able to recognize
        <vocabulary/>
        individual words.
    </template>
</category>
```

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> HOW BIG IS YOUR BRAIN
I am able to recognize 35863 individual words
```

***
[Back to Tutorial](./AIML-Tutorial) | [Back - Date And Time](./Tutorial-Date-And-Time) | [Next - That](./Tutorial-That)