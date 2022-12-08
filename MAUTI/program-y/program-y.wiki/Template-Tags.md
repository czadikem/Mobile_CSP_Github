# Index
This is the list of all currently supported AIML Templates by Program-Y

* [addtriple](#addtriple)
* [authorise](#authorise)
* [bot](#bot)
* [button](#button)
* [card](#card)
* [carousel](#carousel)
* [condition](#condition)
  * [Block Condition](#type1)
  * [Single-predicate Condition](#type2)
  * [Multi-predicate Condition](#type3)
  * [Looping](#looping)
* [date](#date)
* [delay](#delay)
* [deletetriple](#deletetriple)
* [denormalize](#denormalize)
* [eval](#eval)
* [explode](#explode)
* [first](#first)
* [extension](#extension)
* [formal](#formal)
* [gender](#gender)
* [get](#get)
* [id](#id)
* [image](#image)
* [implode](#implode)
* [input](#input)
* [interval](#interval)
* [learn](#learn)
* [learnf](#learnf)
* [link](#link)
* [list](#list)
* [log](#log)
* [lowercase](#lowercase)
* [map](#map)
* [normalize](#normalize)
* [oob](#oob)
* [olist](#olist)
* [person](#person)
* [person2](#person2)
* [program](#program)
* [random](#random)
* [reply](#reply)
* [request](#request)
* [resetlearn](#resetlearn)
* [resetlearnf](#resetlearnf)
* [response](#response)
* [rest](#rest)
* [set](#set)
* [search](#search)
* [sentence](#sentence)
* [select](#select)
* [size](#size)
* [split](#split)
* [sr](#sr)
* [srai](#srai)
* [sraix](#sraix)
* [star](#star)
* [system](#system)
* [that](#that)
* [thatstar](#thatstar)
* [think](#think)
* [topicstar](#topicstar)
* [uniq](#uniq)
* [uppercase](#uppercase)
* [video](#video)
* [vocabulary](#vocabulary)
* [word](#word)
* [xml](#xml)

# Descriptions
This section provides detailed descriptions and examples for all currently supported AIML Template nodes. The number after the name in [] brackets indicates which version of AIML the tag first appeared.

Most nodes take additional data either as attributes or xml child elements, where this occurs, the examples show all possible variations

## addtriple<a name="addtriple"> [2.0]
The 'addtriple' adds another element to the RDF knowledge base. RDF elements comprise of 3 items; subject, predicate and object. For more information see the section on [RDF Support](./RDF)

Description
```xml
<category>
    <pattern>* is a *</pattern>
    <template>
        <addtriple>
            <subj><star /></star>
            <pred>isA</pred>
            <obj><star index="2"/></obj>
        <addtriple>
    </template>
</category>
```
See Also: [deletetriple](#deletetriple), [select](#select), [uniq](#uniq), [RDF Support](./RDF)

## authorise<a name="authorise"> [1.0]
Allows a developer to wrap template tags in role authorization. If the user asking the question does not have the role specified role then they cannot execute the template. For more details see [Role Based Security](./Security-Role-Based)

In the example below, if the role 'root' then they cannot ask for the list of words the Bot knows.

```xml
<category>
    <pattern>LIST VOCABULARY</pattern>
    <template>
          <authorise role="root">
              <vocabulary />
          </authorise
    </template>
</category>
```
In addition, the tag can take an additional parameter to specify a specific srai to execute if authorization fails
```xml
<category>
    <pattern>LIST VOCABULARY</pattern>
    <template>
          <authorise role="root" denied_srai="ACCESS_DENIED">
              <vocabulary />
          </authorise
    </template>
</category>
```
See Also: [Role Based Security](./Security-Role-Based)

## bot<a name="bot"> [1.0]
Provides read-only access to a list of bot properties. These are typically loaded from the file properties.txt on system startup and are used to define bot personality characteristics

```xml
<category>
    <pattern>WHAT IS YOUR NAME</pattern>
    <template>
        My name is <bot name="botname" />
    </template>
</category>

<category>
    <pattern>WHAT IS YOUR NAME</pattern>
    <template>
        My name is <bot><name>botname</name></bot>
    </template>
</category>
```
Uses: properties.txt
See Also: [get](#get), [set](#set)

## button<a name="button"> [2.1]
TBD

## card<a name="card"> [2.1]
TBD

## carousel<a name="carousel"> [2.1]
TBD

## condition<a name="condition"> [1.0]
A condition allows you to control the flow within the processing of the template providing conditional logic around the resulting response that is generated. All conditions work on the value of predicates, either global ones controlled through get/set name or local ones controlled through get/ser var.

### Block Condition<a name="type1">
The first type of condition is a boolean statement that executes the included template tags if the value is true and does nothing if the value is false. There are a number of ways the tag can be defined in XML, all 4 of the following statements are syntactically equal returning the value 'X' if the value of the predicate property is 'v'

```xml
<condition name="property" value="v">X</condition>
<condition name="property"><value>v</value>X</condition>
<condition value="v"><name>property</name>X</condition>
<condition><name>property</name><value>v</value>X</condition>
```

### Single-predicate Condition<a name="type2">
The second type of condition acts like a case or a switch statement in some programming languages. Whereby a single predicate is checked in turn for specific values. As soon as one of the conditions is true, the contained value in then returned. If no value matches, then the parser checks if there is a default value and if so returns that, otherwise it returns no content.

In the example below, both conditions are syntactically equivalent and will return X if predicate called property has value a, and b if it has value Y, otherwise the statement will return the default value Z.

```xml
<condition name="property">
    <li value="a">X</li>
    <li value="b">Y</li>
    <li>Z</li>			<!-- Optional default value if no condition met -->
</condition>

<condition>
    <name>property</name>
    <li value="a">X</li>
    <li value="b">Y</li>
    <li>Z</li>			<!-- Optional default value if no condition met -->
</condition>
```

### Multi-predicate Condition<a name="type3">
The third form of a condition statement is very much like a nested set of if statements in most programming languages. Each condition to be checked defined as a 'li' tag is checked in turn. Each statement may have different predicate names and values. As soon as one of the conditions is true further processing of the li items stops.

```xml
<condition>
    <li name='1' value="a">X</li>
    <li value="b"><name>1</name>Y</li>
    <li name="1"><value>b</value>Z</li>
    <li><name>1</name><value>b</value>Z</li>
    <li>Z<l/i>			<!-- Optional default value if no condition met -->
</condition>
```

### Looping<a name="looping">
Type 2 and Type 3 only
It is possible to loop round in the conditions statement in both Type 2 and Type 3 condition statements. This is controlled through the use of <loop> tag. 

In Type 2, if no default value is specified and a loop tag is encountered at the end, then the parser will re-evaluate the entire condition again. Typically this is useful when the child elements of each li tag do more than just return text and instead may carry our operations that set the predicate under test to a different value.

```xml
<condition name="property">
    <li value="a">X</li>
    <li value="b">Y</li>
    <loop />		            <!-- Loop if no condition met -->
</condition>
```

In Type 3, the loop tag is embedded as one of the li child elements and acts like an else statement. If the condition containing the loop proves to be false, then the loop causes the entire condition to be evaluated from the start again.

```xml
<condition name="property">
    <li value="a">X</li>
    <li value="b">Y </loop></li>    <!-- Loop if condition met -->
    <li>Z</li>			
</condition>
```

## date<a name="date"> [1.0]
Provides a mechanism to automatically generate a range of date and time strings. The format attribute supports Python datetime string formatting. For further information see Python documentation for [datetime](https://docs.python.org/3.6/library/datetime.html)

```xml
<category>
    <pattern>WHAT IS THE DATE</pattern>
    <template>
        Today is <date format="%B %d, %Y" />
    </template>
</category>

<category>
    <pattern>WHAT IS THE DATE</pattern>
    <template>
        Today is <date><format>%B %d, %Y</format></date>
    </template>
</category>
```
See Also: [interval](#interval)

## delay<a name="delay"> [2.1]
TBD

## deletetriple<a name="deletetriple"> [2.0]
Removes an element of knowledge from the RDF data store. The element will either have been loaded at startup, or added via the [addtriple](#addtriple) tag.

```xml
<category>
    <pattern>REMOVE * IS A * </pattern>
    <template>
        <deletetriple>
            <subj><star /></star>
            <pred>isA</pred>
            <obj><star index="2"/></obj>
        <deletetriple>
    </template>
</category>
```
See Also: [addtriple](#addtriple), [select](#select), [uniq](#uniq), [RDF Support](./RDF)

## denormalize<a name="denormalize"> [1.0]
During pre processing of the input text, the parser converts various characters and combinations of characters into distinct words. For example 'github.com' will be converted to 'github dot com' by looking for matches in the mappings contained in dernormalize.txt

```xml
<category>
    <pattern>MY URL IS *</pattern>
    <template>
        OK, I have a look at <denormalize><star /></denormalize>
    </template>
</category>
```
An alternative form with no children implies the use of `<star />
```xml
<category>
    <pattern>MY URL IS *</pattern>
    <template>
        OK, I have a look at <denormalize />
    </template>
</category>
```
Uses: config/denormalize.txt
See Also: [normalize](#normalize)

## eval<a name="eval"> [1.0]
Typically used as part of learn or learnf tags. Eval evaluates the contained tags returning the textualised content.

In the example below, if a variable with name 'name' was set to TIMMY, and a variable 'animal' was set to dog, then evaluation of this learn node would then see a new category 'learnt' to match 'WHO IS TIMMY' with a response, 'YOUR DOG'

```xml
<category>
    <pattern>REMEMBER * IS MY PET *</pattern>
    <template>
    <learn>
      <think>
          <set var="name"><star /></set>
          <set var="animal"><star index="2" /></set>
      </think>
      <category>
        <pattern>WHO IS
            <eval>
                <get var="name"/>
            </eval>
        </pattern>
        <template>
            Your
            <eval>
                <get var="animal"/>
            </eval>.
        </template>
      </category>
    </learn>
  </template>
</category>
```
See Also: [learn](#learn), [learnf](#learnf)

## explode<a name="explode"> [1.0]
Turns the contents of each word contained within the talk into a series single character words separated by spaces.

So for example 'FRED' would explode to 'F R E D', and 'Hello There' would explode to 'H e l l o T h e r e'.

```xml
<category>
    <pattern>EXPLODE *</pattern>
    <template>
        <explode><star /></explode>
    </template>
</category>
```
An alternative form with no children implies the use of `<star />
```xml
<category>
    <pattern>EXPLODE *</pattern>
    <template>
        <explode />
    </template>
</category>
```
## image<a name="image"> [2.1]
TBD

See Also: [implode](#implode)

## first<a name="first"> [1.0]
Give a list of words returns the first word. The opposite of rest which returns all but the first word. Usefully for iterating through a series of words in conjunction with the rest tag. Return NIL if there are no more words to return.

```xml
<category>
    <pattern>MY NAME IS * </pattern>
    <template>
        Your first name is <first><star /></star>
    </template>
</category>
```
An alternative form with no children implies the use of `<star />
```xml
<category>
    <pattern>MY NAME IS * </pattern>
    <template>
        Your first name is <first />
    </template>
</category>
```

See Also: [rest](#rest)

## extension<a name="extension"> [Program-Y]
An extension provides the mechanism to call out to the underlying Python system Program-Y is developed in. An extension is essentially made up of a full Python module path to a Python class which implements the `programy.extensions.Extension` interface.

For more information on how to build your own extensions see the wiki page [Extensions](./Extensions).

```xml
<category>
    <pattern>
        BANK BALANCE *
    </pattern>
    <template>
        <srai>
            SHOW_BALANCE
            <extension path="programy.extensions.banking.balance.BankingBalanceExtension">
                <star />
            </extension>
        </srai>
    </template>
</category>
```

## formal<a name="formal"> [1.0]
The formal tag will capitialise every distinct word contained between its tags.

```xml
<category>
    <pattern>MY NAME IS * * </pattern>
    <template>
        Hello Mr <formal><star /></formal> <formal><star index="2"/></formal>
    </template>
</category>
```
An alternative form with no children implies the use of `<star />
```xml
<category>
    <pattern>MY NAME IS * * </pattern>
    <template>
        Hello Mr <formal /><formal><star index="2"/></formal>
    </template>
</category>
```

## gender<a name="gender"> [1.0]
The gender tags uses the contents of the `gender.txt` file to change gender of the text contained. The file is a set and a gender change is only actioned if there is match within the gender set.

```xml
<category>  
    <pattern>DOES IT BELONG TO *</pattern>  
    <template>
        No, it belongs to <gender><star/></gender>
    </template>  
</category>
```
Uses: config/gender.txt

## get<a name="get"> [1.0]
The get tag provides access to variables, of which there are 2 types
* Global. The same variable is accessible to all clients within the context of the same brain. Global variables accessed using the 'name' attribute. 
* Local. Local to the individual client and only relevant during the current conversation. Local variables are accessed using the 'var' attribute
Values are set either by the system at start up or as part of the conversation by the use of the [set](#set) tag.

```xml
<!-- Access Global Variable -->
<category>
    <pattern>USER COUNT</pattern>
    <template>
        Total active users is <get name="activeusers" />
    </template>
</category>

<!-- Access Local Variable -->
<category>
    <pattern>QUESTION COUNT</pattern>
    <template>
        You have asked <get var="questioncount" /> questions in this conversation.
    </template>
</category>
```
See Also: [bot](#bot), [set](#set)

## id<a name="id"> [1.0]
Returns the current system defined name of the bot. This is up to the bot developer to define what this string means.
```xml
<category>
    <pattern>Tell me you name</pattern>
    <template>
        <id />
    </template>
</category>
```

## implode<a name="implode"> [Program-Y]
Given a string of words, concatenates them all into a single string with no spaces.
```xml
<category>
    <pattern>Implode the acronym *</pattern>
    <template>
        <implode><star /></implode>
    </template>
</category>
```
An alternative form with no children implies the use of `<star />
```xml
<category>
    <pattern>Implode the acronym *</pattern>
    <template>
        <implode />
    </template>
</category>
```
See Also: [explode](#explode)

## input<a name="input"> [1.0]
Returns the entire question asked by the user. This is different to 'star' tag which only returns those values that match one of the wild cards in the pattern.
```xml
<category>
    <pattern>What was my question</pattern>
    <template>
        You question was <input />
    </template>
</category>
```

## interval<a name="interval"> [1.0]
Calculates the difference between 2 date and time entities. The value returned can be formatted using standard Python [datetime](https://docs.python.org/3.6/library/datetime.html) formatting information.
```xml
<category>
    <pattern>AGE IN YEARS</pattern>   
    <template>
        <interval format="%B %d, %Y">
            <style>years</style>
            <from><bot name="birthdate"/></from>
            <to><date format="%B %d, %Y" /></to>
        </interval>
    </template>
</category>
```
See Also: [date](#date)

## link<a name="link"> [2.1]
TBD

## list<a name="list"> [2.1]
TBD

## learn<a name="learn"> [2.0]
Allows the bot to learn new knowledge. Knowledge is held within the bot in the form of categories, when a learn template node is evaluated new categories are added to the braintree and become available to be queried during the context of the conversation. Unlike with learnf, when the bot is restarted, all learn categories are lost.

```xml
<category>
    <pattern>REMEMBER * IS MY PET *</pattern>
    <template>
    <learn>
      <think>
          <set var="name"><star /></set>
          <set var="animal"><star index="2" /></set>
      </think>
      <category>
        <pattern>WHO IS
            <eval>
                <get var="name"/>
            </eval>
        </pattern>
        <template>
            Your
            <eval>
                <get var="animal"/>
            </eval>.
        </template>
      </category>
    </learn>
  </template>
</category>
```
See Also; [eval](#eval), [learnf](#learnf)

## learnf<a name="learnf"> [2.0]
Allows the bot to learn new knowledge. Knowledge is held within the bot in the form of categories when a learn template node is evaluated new categories are added to the braintree and become available to be queried during the context of the conversation. Unlike with learn, when the bot is restarted, all learnf categories are retained and reloaded at startup.

```xml
<category>
    <pattern>REMEMBER * IS MY PET *</pattern>
    <template>
    <learnf>
      <think>
          <set var="name"><star /></set>
          <set var="animal"><star index="2" /></set>
      </think>
      <category>
        <pattern>WHO IS
            <eval>
                <get var="name"/>
            </eval>
        </pattern>
        <template>
            Your
            <eval>
                <get var="animal"/>
            </eval>.
        </template>
      </category>
    </learnf>
  </template>
</category>
```
See Also: [eval](#eval), [learn](#learn)

## log<a name="log"> [Program-Y]
Allows a AIML developer to embed logging statements into the AIML itself. These statements are then output into the bot log file. Logging levels are as follows, and are equivalent to [Python Logging](https://docs.python.org/3.6/library/logging.html)
* error
* warning
* debug
* info
For more information see how to configure and use [Program-Y Logging](/Config_Logging)

```xml
<category>
    <pattern>HELLO *</pattern>
    <template>
        <log>You said hello</log>
    </template>
</category>

<category>
    <pattern>Goodbye *</pattern>
    <template>
        <log level="error">You said goodbye</log>
    </template>
</category>
```

## lowercase<a name="lowercase"> [1.0]
Turns all text contained within the tag to lowercase.
```xml
<category>
    <pattern>HELLO *</pattern>
    <template>
        <lowercase><star /></lowercase>
    </template>
</category>
```
An alternative form with no children implies the use of `<star />
```xml
<category>
    <pattern>HELLO *</pattern>
    <template>
        <lowercase />
    </template>
</category>
```
See Also: [uppercase](#uppercase)

## map<a name="map"> [1.0]
The name of the maps refes to a map stored within the config/maps folder. Each map contains a series of name:value pairs. This node looks for a match of the test given and replaces that text with the value stored in the map. If no value is found then 'unknown' is returned.

```xml
<category>
    <pattern>WHAT NOISE DOES A * MAKE</pattern>
    <template>
       A <star/> says <map name="animalsounds" /></map>
    </template>
</category>
```

## normalize<a name="normalize"> [1.0]
Where denormalize reconstructs a series of words into the actual form, normalize can be used to in the opposite direction and breaks down a string containing special characters and substrings into a series of space seperated words

```xml
<category>
    <pattern>MY EMAIL ADDRESS IS *</pattern>
    <template>
        Your email address is stored as <normalize><star /><normalize>
    </template>
</category>
```
An alternative form with no children implies the use of `<star />
```xml
<category>
    <pattern>MY EMAIL ADDRESS IS *</pattern>
    <template>
        Your email address is stored as <normalize />
    </template>
</category>
```
See Also: [denormalize](#denormalize)

## olist<a name="olist"> [2.1]
TBD

## oob<a name="oob"> [1.0]
OOB refers to Out Of Band. When an oob tag is evaluated, the parser returns the content of the tag back to the client replacing any template tags with their relevant values. OOB is used to return control statements back to the client to allow it to perform additional tasks.

It is the responsibility of the Bot developer to build appropriate OOB functionality on how to handle and process the contents of the oob node returned. For more information see [OOB](./OOB)

```xml
<category>
    <pattern>DIAL *</pattern>
    <template>
        <oob><dial><star /><dial></oob>
    </template>
</category>
```
See Also: [xml](#xml)

## person<a name="person"> [1.0]
Uses the contents of the person.txt map file to transform a matched pronoun string from first to second person
```xml
<category>
    <pattern>I AM *</pattern>  
    <template>
        You are <person><star/></person>
    </template>  
</category>
```
An alternative form with no children implies the use of `<star />
```xml
<category>
    <pattern>I AM *</pattern>  
    <template>
        You are <person />
    </template>  
</category>
```
See Also: [person2](#person2)

## person2<a name="person2"> [1.0]
Uses the contents of the person2.txt map file to transform a matched pronoun string from first to third person
```xml
<category>  
    <pattern>GIVE THE * TO *</pattern>  
    <template>
        User has asked me to give the <star/> to <person2><star index="2"/></person2>
    </template>  
</category>
```
An alternative form with no children implies the use of `<star />
```xml
<category>  
    <pattern>GIVE THE * TO *</pattern>  
    <template>
        You have given it to <person2 />
    </template>  
</category>
```
See Also: [person](#person)

## program<a name="program"> [1.0]
Returns the name and version number of the Bot
```xml
<category>
    <pattern>VERSION INFO</pattern>
    <template>
        <program />
    </template>
</category>
```

## random<a name="random"> [1.0]
Randomly selects one of the child list elements. Useful to give the bot a more human non deterministic response quality
```xml
<category>
    <pattern>HELLO</pattern>
    <template>
        <random>
             <li>Hi there!</li>
             <li>Hello</li>
             <li>Greetings</li>
    </template>
</category>
```

## reply<a name="reply"> [2.1]
TBD

## request<a name="request"> [1.0]
Returns the users input specified by the number index. This returns all sentences if a multi sentence question is asked.
```xml
<category>
    <pattern>WHAT DID I SAY</pattern>
    <template>
          You said <request index="1" /> and before that
          you said <request index="2" /> and you just said
          <request index="0" />
    </template>
</category>
```
An alternative form with no attributes implies the use of index="1"
```xml
<category>
    <pattern>WHAT DID I SAY</pattern>
    <template>
          You said <request/>
    </template>
</category>
```
See Also: [response](#response)

## resetlearn<a name="resetlearn"> [2.x]
Clears all patterns that have been learnt using the `<learn>` tag
```xml
<category>
    <pattern>Forget what I said</pattern>
    <template>
         <think><resetlearn /></think>
         OK, I have forgotten what you taught me
    </template>
</category>
```

## resetlearnf<a name="resetlearnf"> [2.x]
Clears all patterns that have been learnt using the `<learnf>` tag. This differs from learn in that it deletes all the files that the tag created.
```xml
<category>
    <pattern>Forget what I said</pattern>
    <template>
         <think><resetlearnf /></think>
         OK, I have forgotten what you taught me
    </template>
</category>
```

## response<a name="response"> [1.0]
Returns the users input specified by the number index. This returns all sentences if a multi sentence question is asked.
```xml
<category>
    <pattern>WHAT DID YOU JUST SAY</pattern>
    <template>
          I said <response index="1" /> and before that
          I said <response index="2" /> and I just said
          <response index="0" />
    </template>
</category>
```
An alternative form with no attributes implies the use of index="1"
```xml
<category>
    <pattern>WHAT DID YOU SAY</pattern>
    <template>
          You said <response/>
    </template>
</category>
```
See Also: [request](#request)

## rest<a name="rest"> [2.0]
Given a series of words returns all but the first word. Provides the opposite functionality to the first tag.

For example given a list of words 'HELLO TO  YOU', will return 'TO YOU'. When used in conjunction with first, it allows the developer to iterate through an indefinite list of words. Return NIL if there are no more words to return.

```xml
<category>
    <pattern>MY NAME IS * </pattern>
    <template>
        Your middle and/or last names are <rest><star /></rest>
    </template>
</category>
```
See Also: [first](#first)

## set<a name="set"> [1.0]
Within the context of a template the set tag allows the setting of variables both global (name) and local (var)
```xml
<!-- Global variable -->
<category>
    <pattern>MY NAME IS *</pattern>
    <template>
        <set name="myname"><star /></set>
    </template>
</category>

<!-- Local Variables -->
<category>
    <pattern>MY NAME IS *</pattern>
    <template>
        <set var="myname"><star /></set>
    </template>
</category>
```
See Also: [bot](#bot), [get](#get)

## search<a name="search"> [Program-Y, Pandora]
Create a google search URL of the formats https://www.google.co.uk/search?q=XXXXXXX. Useful short hand for adding Google capabilities to your grammar now that Google does not provide access to its search API.

This node is found only within the context of PandoraBot, but has been added to Program-Y to provide compatibility with Pandora defined AIML.
```xml
<category>
    <pattern>CAN YOU GOOGLE * FOR ME</pattern>
    <template>
        <search><star /></search
    </template>
</category>
```

## select<a name="select"> [2.0]
Allows the user to query RDF triples that have been previously added either at system start up from the triples.txt file or via addtriple tag.

The select, uniq, addtriple and deletetriple tags provide a comprehensive knowledge system. For more information check out [RDF](./RDF) on the wiki.

```xml
<category>
    <pattern>FIND ANIMALS WITH TAILS</pattern>
    <template>
        <search>
             <vars>?name</vars>
             <subj>?name</subj><pred>hasA</pred><obj>tail</obj>
        </search>
    </template>
</category>
```
See Also: [addtriple](#addtriple), [deletetriple](#deletetriple), [search](#search), [uniq](#uniq), [RDF Support](./RDF)

## sentence<a name="sentence"> [1.0]
Capitalises the first work of the sentence and sets all other words to lower case
```xml
<category>
    <pattern>Create a sentence with the word *</pattern>
    <template>
        <sentence>HAVE you Heard ABouT <star/></sentence>
    </template>
</category>
```
An alternative form with no children implies the use of `<star />
```xml
<category>
    <pattern>CORRECT THIS *</pattern>
    <template>
        <sentence />
    </template>
</category>
```

## size<a name="size"> [1.0]
Returns the number of categories currently held with in the brain
```xml
<category>
    <pattern>WHAT DO YOU KNOW</pattern>
    <template>
        I know <size /> things
    </template>
</category>
```

## split<a name="split"> [2.1]
TBD

## sr<a name="sr"> [1.0]
Short hand for `<srai><star/></srai>`
```xml
<category>
    <pattern>ANSWER ME *</pattern>
    <template>
        <sr />
    </template>
</category>
```
Is syntacially equivalent to 
```xml
<category>
    <pattern>ANSWER ME *</pattern>
    <template>
        <srai><star/></srai>
    </template>
</category>
```
See Also: [star](#star), [srai](#srai), [sraix](#sraix)

## srai<a name="srai"> [1.0]
The srai element allows your bot to recursively call categories after transforming the user’s input. So you can define a template that calls another category. The acronym “srai” has no official meaning, but is sometimes defined as symbolic reduction or symbolic recursion.
 ```xml
<category>
    <pattern>HELLO GOOD DAY</pattern>
    <template><srai>HI</srai></template>
</category>

<category>
    <pattern>BONJOUR</pattern>
    <template><srai>HI</srai></template>
</category>

<category>
    <pattern>GUTEN TAG</pattern>
    <template><srai>HI</srai></template>
</category>

<category>
    <pattern>HI</pattern>
    <template>Hello there!</template>
</category>      
```
See Also: [star](#star), [sr](#sr), [sraix](#sraix)

## sraix<a name="sraix"> [2.0]
The original purpose of the sraix tag was to allow a bot to call another bot and to chain the questions together, however in Program-Y this has been extended to provide the capability to call any external REST API.

For more information about calling existing external services and also how to built and interact with your own, see [External Servics](./External_Services)
```xml
<category>
    <pattern>XXX</pattern>
    <template>
        <sraix host="http://somehost.com" botid="testbot" hint="test query" apikey="1234567890" service="ask">
            Ask this question
        </sraix>
    </template>
</category>
```
See Also: [star](#star), [sr](#sr), [srai](#srai)

## star<a name="star"> [1.0]
The star element is used to echo portions of the user’s input that were captured by wildcards. The index attribute provides the ability to access each individual match in the sentence. Wildcards include the one or more characters * and _, the zero or more characters ^ and #, maps, sets, isets and bot tags.
```xml
<category>
    <pattern>MY FAVORITE * IS *</pattern>
    <template>
        Your favorite <star /> is <star index="2" />
    </template>
</category>
```
See Also: [sr](#sr), [srai](#srai), [sraix](#sraix)

## system<a name="system"> [1.0]
The system tag allows you to make underlying system calls. This is obviously a security concern allowing users unfettered access to the underlying system if they know the operating system and can inject shell scripts.

By default this is disabled, but can be turned on by setting the configuration option `allow_system_aiml` to True.

This tag is included in the original AIML 2.0 specification but is removed in Pandora Bot due to the obvious security restrictions. 
```xml
<category>
    <pattern>LIST ALL AIML FILES</pattern>
    <template>
        <system>ls -l *.aiml</system>
    </template>
</category>
```

## that<a name="that"> [2.0]
A child element of `category`, that when defined that `pattern` will only match if the previous response from the bot matches the contents of `that`. However when used in the context of the template node, `that` provides access to responses provided by the bot. The attribute 'index' provides a numbered index for each previous that.
```xml
<category>
    <pattern>HELLO</pattern>
    <template>
         Hi there
    </template>
</category>

<category>
    <pattern>PARDON</pattern>
    <that>Hi There</that>
    <template>
         I said <that/>
    </template>
</category>

```
See Also: [star](#star), [topic](#topic), [thatstar](#thatstar), [topicstar](#topicstar)

## thatstar<a name="thatstar"> [1.0]
The `that` tag can use the full set of wildcard matching that is available in the pattern tag. These matches are accessed in the same way as using `<star/>`, but for that tag, we use `<thatstar/>`
```xml
<category>
    <pattern>YES</pattern>
    <that>DO YOU LIKE *</that>
    <template>
        I like <thatstar /> too.
    </template>
</category>
```
See Also: [star](#star), [topic](#topic), [thatstar](#thatstar), [topicstar](#topicstar) 

## think<a name="think"> [1.0]
The think element allows your bot to set predicates without actually displaying the contents of a set element to the user. This is sometimes referred to as “silently” setting a predicate.
```xml
<category>
    <pattern>MY NAME IS *</pattern>
    <template>
       <think><set name="name"><star /></set></think>
       I will remember your name.
    </template>
</category>
```

## topicstar<a name="topicstar"> [1.0]
The `topic` tag can use the full set of wildcard matching that is available in the pattern tag. These matches are accessed in the same way as using `<star/>`, but for the topic tag, we use `<topicstar/>`
```xml
<topic name=”beverages *”>
<category>
    <pattern>WHAT DO I WANT</pattern>
        <template><topicstar/></template>
    </category>
</topic>
```
See Also: [star](#star), [topic](#topic), [that](#that), [thatstar](#thatstar)

## uniq<a name="uniq"> [2.0]
Uniq is used in conjection with [select](#select) tag. If the select query returns more than one RDF element, then uniq can be used to reduce that to a single element. Consider uniq as an equivalent to 'first' but for RDF elements.

The select, uniq, addtriple and deletetriple tags provide a comprehensive knowledge system. For more information check out [RDF](./RDF) on the wiki.
```xml
<category>
    <pattern>HOW MANY LEGS DOES A MONKEY HAVE</pattern>
    <template>
        <uniq>
            <subj>MONKEY</subj>
            <pred>legs</pred>
            <obj>?legs</obj>
        </uniq>
    </template>
</category>
```
See Also: [addtriple](#addtriple), [deletetriple](#deletetriple), [search](#search), [select](#select), [RDF Support](./RDF)

## uppercase<a name="uppercase"> [1.0]
Converts all words contained in the tag to uppercase.
```xml
<category>
    <pattern>MY SURNAME IS *</pattern>
    <template>
        Hello Mr <uppercase><star /></uppercase>
    </template>
</category>
```
An alternative form with no children implies the use of `<star />
```xml
<category>
    <pattern>MY SURNAME IS *</pattern>
    <template>
        Hello Mr <uppercase />
    </template>
</category>
```
See Also: [lowercase](#lowercase)

## vocabulary<a name="vocabulary"> [1.0]
Returns the number of distinct words known by the Bot.
```xml
<category>
    <pattern>HOW BIG IS YOUR BRAINI</pattern>
    <template>
        I know <vocabulary /> words
    </template>
</category>
```
See Also: [size](#size)

## video<a name="video"> [2.1]
TBD

## word<a name="word"> [1.0]
A `<word>` tag as such does not exist, but each individual text word in a sentence is converted into a word node.
```xml
<category>
    <pattern>HELLO</pattern>
    <template>Hi there!</template>
</category>
```

## xml<a name="xml"> [1.0]
Like a word node, there is not `<xml>` tag as such however given that AIML is an XML dialect, and if the parser comes across an xml element it does not undertand, it stores it as pure XML. 

This is extremely useful when you include HTML in you template responses. It allows template and xml nodes to be mixed, such that the template nodes are evaluated to strings and then combined with the xml nodes.
```xml
<category>
    <pattern>HIGHLIGHT * IN BOLD</pattern>
    <template>
        <bold><star /></bold>
    </template>
</category>
```
