# Overview
The survey extension provides an example of how to create a grammar that asks a customer a series of questions as part of a typical survey and then use a Python extension to store the results into a file for later processing

## Core Grammars
The grammars are slightly different and show a good example of how to use a combination of topic and forward chaining to link a series of questions together. A question is posed as the output of a question, the answer is processed in a subsequent grammar given a specific topic.

You start the survey with `START SURVEY` either the customer enters that, or its driven as the result of another question and an `<srai>` tag.

At the end of the question, an Extension is used to write the results to a file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml>
    <!-- File: balance.aiml -->
    <!--  -->
    <!-- This AIML file is part of the Y-Bot knowledge base. -->
    <!--  -->
    <!-- Y-Bot is Copyright &copy; 2017 by Keith Sterling. -->
    <!--
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
    documentation files (the "Software"), to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
    and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
    THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    -->

    <category>
        <pattern>
            START SURVEY
        </pattern>
        <template>
            <think><set name="topic">SURVEY_QUESTION1</set></think>
            Question 1. What do you like about AIML?
        </template>
    </category>

    <topic name="SURVEY_QUESTION1">
        <category>
            <pattern>
                #
            </pattern>
            <template>
                <think>
                    <set name="topic">SURVEY_QUESTION2</set>
                    <set name="answer1"><star /></set>
                </think>
                Thanks, now Question 2. What do you dislike about AIML?
            </template>
        </category>
    </topic>

    <topic name="SURVEY_QUESTION2">
        <category>
            <pattern>
                #
            </pattern>
            <template>
                <think>
                    <set name="answer2"><star /></set>
                    <extension path="programy.extensions.survey.survey.SurveyExtension">
                    <get name="answer1" />|
                    <get name="answer2" />
                </extension>
                </think>
                Thanks, thats the end of the survey
                <think>
                    <set name="topic"></set>
                </think>
            </template>
        </category>
    </topic>

</aiml>
```