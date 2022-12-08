Date and Interval elements of AIML provide a comprehensive mechanism for viewing and manipulating time-based data

## Date
The date tag provides a way to format the current date and time using a variety of ways. The formatting is controlled by the format attribute of the date tag. This is a string which takes a set of formatting options as defined by the Python Programming Language [datetime module](https://docs.python.org/3.6/library/datetime.html)

In this first example, we use the date tag to return the name of the day. As defined by the formatting command "%A". 

```xml
<aiml>
    <category>
        <pattern>DAY</pattern>
        <template>Today is
            <date format="%A"/>
        </template>
    </category>
</aiml>
```

When this is run in the bot, and you ask for the day, it returns the textual representation of the day as follows

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> DAY
Today is Thursday
```

Another way to use the date tag is to set the value of a variable and then act on the value of the variable. In the next example, we use the name of the month to return the name of the season

```xml
<aiml>
    <category>
        <pattern>SEASON</pattern>
        <template>
            <think>
                <set var="month">
                    <date format="%B"/>
                </set>
            </think>
            <condition var="month">
                <li><value>JANUARY</value>Winter
                </li>
                <li><value>FEBRUARY</value>Winter
                </li>
                <li><value>MARCH</value>Winter
                </li>
                <li><value>APRIL</value>Spring
                </li>
                <li><value>MAY</value>Spring
                </li>
                <li><value>JUNE</value>Summer
                </li>
                <li><value>JULY</value>Summer
                </li>
                <li><value>AUGUST</value>Summer
                </li>
                <li><value>SEPTEMBER</value>Fall
                </li>
                <li><value>OCTOBER</value>Fall
                </li>
                <li><value>NOVEMBER</value>Winter
                </li>
                <li><value>DECEMBER</value>Winter
                </li>
                <li>unknown</li>
            </condition>
        </template>
    </category>
</aiml>
```

Running this through the bot we can ask for the name of the season as follows

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> SEASON
Winter
```

Some additional useful uses are as follwos
```xml
<aiml>

    <category>
        <pattern>YEAR</pattern>
        <template>This is
            <date format="%Y" />
        </template>
    </category>

    <category>
        <pattern>MONTH</pattern>
        <template>This is
            <date format="%B" />
        </template>
    </category>

    <category>
        <pattern>TIME</pattern>
        <template>The time is
            <date format="%I:%M %p" />
        </template>
    </category>

    <category>
        <pattern>DATE</pattern>
        <template>Today is
            <date format="%B %d, %Y" />
        </template>
    </category>

    <category>
        <pattern>DAY PHASE</pattern>
        <template>
            <think>
                <set var="hour">
                    <date format="%I" />
                </set>
                <set var="ampm">
                    <date format="%p" />
                </set>
            </think>
            <condition>
                <li value="AM" var="ampm">Morning</li>
                <li>
                    <condition var="hour">
                        <li value="12">Noon</li>
                        <li value="1">Afternoon</li>
                        <li value="2">Afternoon</li>
                        <li value="3">Afternoon</li>
                        <li value="4">Afternoon</li>
                        <li value="5">Afternoon</li>
                        <li value="6">Afternoon</li>
                        <li>Night</li>
                    </condition>
                </li>
            </condition>
        </template>
    </category>

    <category>
        <pattern>DATE AND TIME</pattern>
        <template>The date and time is
            <date/>
        </template>
    </category>

</aiml>
```

## Interval
Interval tag allows you to compute the time difference between 2 periods and then obtain the difference in a variety of formats, in the same way, that the date tag works.

```xml
<aiml>
    <category>
        <pattern>DAYS UNTIL CHRISTMAS</pattern>
        <template>
            <interval format="%B %d" >
                <style>days</style>
                <from>
                    <date format="%B %d" />
                </from>
                <to>December 25</to>
            </interval>
            days until Christmas.
        </template>
    </category>
</aiml>
```

We now have an incredibly useful grammar for asking the number of days until Christmas

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> Days until christmas
46 days until Christmas.
```

Or a more generic one

```xml
<aiml>
    <category>
        <pattern>DAYS UNTIL <set>month</set> <set>number</set> <set>number</set>
        </pattern>
        <template>
            <interval format="%B %d %Y" >
                <style>days</style>
                <from>
                    <date format="%B %d %Y" />
                </from>
                <to>
                    <star/>
                    <star index="2"/>
                    <star index="3"/>
                </to>
            </interval>
            days.
        </template>
    </category>
</aiml>
```

Running this in the bot and we can ask for the number of days between now and a future date

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> Days until December 24 2017
45 days.
```

For a more detailed description of how to use all the various formatting options see the Python Programming Language [datetime module](https://docs.python.org/3.6/library/datetime.html)

***
[Back to Tutorial](./AIML-Tutorial) | [Back - Conditions](./Tutorial-Conditions) | [Next - System Information](./Tutorial-System-Information)