There are a number of tags which can be used to support contextual conversations, providing access to that which was asked and responded to, so that it can then be used in further stages of the conversation. These tags are

* input - Returns the entire user input
* request - Indexed element which provides access to the historical inputs from the user. 
* response - Indexed element which provides access to the historical responses from the bot.
* star - Indexed element which provides access to those words or phrases which matched one or more wildcards
* topicstar - Similar star but returns the wildcard matches for topic
* thatstar - Similar to star but returns the wildcard matches for that

## input
Returns the entire question asked by the user. This is different to 'star' tag which only returns those values that match one of the wild cards in the pattern.
```
    <category>
        <pattern>Patriots Rock</pattern>
        <template>
            You said <input />, but I disagree, for me its the Jaguars all the way!
        </template>
    </category>
```

## request
Returns the users input specified by the number index. This returns all sentences if a multi sentence question is asked.
```
    <category>
        <pattern>WHAT DID I JUST SAY</pattern>
        <template>
            You said <request index="1" />
        </template>
    </category>

    <category>
        <pattern>WHAT DID I SAY BEFORE THAT</pattern>
        <template>
            You said <request index="2" />
        </template>
    </category>
```

## response
Returns the users input specified by the number index. This returns all sentences if a multi sentence question is asked.
```
    <category>
        <pattern>WHAT DID YOU JUST SAY</pattern>
        <template>
            You said <response index="1" />
        </template>
    </category>

    <category>
        <pattern>WHAT DID YOU SAY BEFORE THAT</pattern>
        <template>
            You said <response index="2" />
        </template>
    </category>
```

## star
The star element is used to echo portions of the user’s input that were captured by wildcards. The index attribute provides the ability to access each individual match in the sentence. Wildcards include the one or more characters * and _, the zero or more characters ^ and #, maps, sets, isets and bot tags.
```
    <category>
        <pattern>I LIKE *</pattern>
        <template>
            I also like <star />
        </template>
    </category>

    <category>
        <pattern>I LIKE * AND *</pattern>
        <template>
            I like <star index="1" /> but I do not like <star index="2" />
        </template>
    </category>
```

## topicstar
The topic tag can use the full set of wildcard matching that is available in the pattern tag. These matches are accessed in the same way as using <star/>, but for the topic tag, we use <topicstar/>
```
    <topic name="* APPLES">
      <category>
        <pattern>I LIKE TO EAT THEM</pattern>
        <template>
            Why do you like eating <topicstar /> apples ?
        </template>
      </category>
    </topic>
```

## thatstar
The that tag can use the full set of wildcard matching that is available in the pattern tag. These matches are accessed in the same way as using <star/>, but for that tag, we use <thatstar/>
```
    <category>
        <pattern>I LIKE IT TOO</pattern>
            <that>I LIKE *</that>
            <template>
                What do you like best about <thatstar />
            </template>
    </category>
```

***
[Back to Tutorial](./AIML-Tutorial) | [Back - Topic](./Tutorial-Topic) | [Next - Text Translation](./Tutorial-Text-Translation)