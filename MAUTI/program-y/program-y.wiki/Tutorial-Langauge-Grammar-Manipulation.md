AIML comes with a number of grammar text manipulation tags. These tags are used to convert the input or output stream based on some basic grammar rules

* normalize - Converts input stream into text elements that are more easily parsable by the Bot
* denormalize - Essentially the reverse of normalize in that it converts text into more human readable elements
* person - Transform pronouns between first and third person
* person2 - Transforms pronouns between first and second person
* gender - Converts the gender of the enclosed text

Each of these conversion tags uses a file of substitutions that it uses to match input text and to convert to using output text. The locations of these files are held in the brain configuration section under files. 

## Normalize

Normalize uses the file referenced in normal element of the files section of brain as defined below
```yaml
brain:
    files:
        normal: $BOT_ROOT/config/normal.txt
```        

```xml
<category>
    <pattern>MY EMAIL IS *</pattern>
    <template>
        OK, I'll email you on <normalize><star /></normalize>
    </template>
</category>
```
	
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> My email is keiffster@gmail.com
OK, I'll email you on keiffster at gmail dot com
```

## Denormalize

Denormalize uses the file referenced in denormal element of the files section of brain as defined below
```yaml
brain:
    files:
        denormal: $BOT_ROOT/config/denormal.txt
```        

```xml
<category>
    <pattern>EMAIL ME AT *</pattern>
    <template>
        OK, sending an email to <denormalize><star /></denormalize>
    </template>
</category>
```
	
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> Email me at keiffster at gmail dot com
OK, sending an email to keiffster@gmail.com
```

## Person

Person uses the file referenced in person element of the files section of brain as defined below
```yaml
brain:
    files:
        person: $BOT_ROOT/config/person.txt
```        

```xml
<category>
    <pattern>I AM *</pattern>  
    <template>
        You are <person><star/></person>
    </template>  
</category>```
	
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> I am waiting for you
You are waiting for me
```


## Person2

Person2 uses the file referenced in person2 element of the files section of brain as defined below
```yaml
brain:
    files:
        person2: $BOT_ROOT/config/person2.txt
```        

```xml
<category>  
    <pattern>GIVE THE * TO *</pattern>  
    <template>
        User has asked me to give the <star/> to <person2><star index="2"/></person2>
    </template>  
</category>
```
	
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> Give the password to me
User has asked me to give the password to them
```

## Gender

Gender uses the file referenced in gender element of the files section of brain as defined below
```yaml
brain:
    files:
        gender: $BOT_ROOT/config/gender.txt
```        

```xml
<category>
    <pattern>DOES IT BELONG TO *</pattern>  
    <template>No, it belongs to <gender><star/></gender></template>  
</category>
```
	
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> Does it belong to her
No, it belongs to him
```

***
[Back to Tutorial](./AIML-Tutorial) | [Back - Text Translation](./Tutorial-Text-Translation) | [Next - List Processing](./Tutorial-List-Processing)