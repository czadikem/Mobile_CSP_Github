# AIML Cookbook

On this page, we'll start to publish common ways to achieve things using AIML. This will take the tutorial to the next level and we'll explore easy ways to accomplish what at times may appear complex. AIML is powerful and there is typically more than one way to achieve what you want to do. The cookbook will always try and give you the most efficient way to achieve it and give you the reason why its the most efficient.

# Variables

## Bot variables

## Global variables

## Local Variables

## Saving Variables

# Control Structures

## How do I loop

## If statement

## If then else statement

## Switch Statement

## For loop

## Do loop

## While Loop

# Handling Empty Responses
```xml
<?xml version="1" encoding="UTF-8" ?>
<aiml>

        <category>
                <!-- This is your entry into the conversation -->
                <!-- The * matches everything you ask Wikipedia and gets passed into the topic -->
               <pattern>ASK WIKIPEDIA * </pattern>
               <template>
            <think><set name="topic">ASKWIKIPEDIA</set></think>
            <srai>YASKWIKIPEDIA <star /></srai>
        </template>
        </category>

    <topic name="ASKWIKIPEDIA">
        <category>
            <!-- This is the grammar that calls Wikipedia -->
             <!-- If wikipedia returns a response it will be displayed -->
            <pattern>YASKWIKIPEDIA *</pattern>
            <template>
                <srai>ASKWIKIPEDIA <star /></srai>
            </template>
        </category>

        <category>
            <!-- This is the grammar that will get called if Wikipedia return an empty string -->
            <!-- Y-Bot never returns NULL as content
            <pattern>YEMPTY</pattern>
            <template>
                <think><set name="topic"></set></think>
                <!-- You need to modify this to do whatever you want to if wikipedia returns empty string -->
                Nothing from Wikipedia
            </template>
        </category>
    </topic>

</aiml>
```

