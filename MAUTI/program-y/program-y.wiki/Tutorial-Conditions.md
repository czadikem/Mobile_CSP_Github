# Conditions
Within AIML version 2.0 there exist 3 distinct types of conditions an AIMl developer can use to control/alter the flow and create loops within their grammar template processing.
* Block Conditions
* Single Predicate Condition
* Multi-predicate Condition

As is typical with most AIML tags, there are 2 variants of how the name and value pair is presented. These are either
* Attributes of the condition tag 
  * ```<condition name="var1" value="val1"></condition>```
* Child tags of the condition tag 
  * ```<condition><name>var1</name><value>val1</value</condition>```

We will use both options interchangeably during the tutorial pages

## Block Condition
A block condition allows you to wrap AIML template tags with a condition tag, and the children and then only evaluated if the condition is true. Each conditional value is either a global or local variable which has typically either been set previously in the processing by a set tag or has been set at startup using default values.

Each block condition is treated as a separate conditional statement, so that if a template contains multiple statements all of them are evaluated and all if true will contribute content to the template resulting evaluation.

The following examples show all the different variants representing the name/var value pair. In each example, the think tag is used to set the value of either a global ( name ) or local ( var ) variable. The value is then checked by each of the conditional statements and the appropriate text then returned as the template.

```xml
        <!-- Example using global variable with name and value as attributes -->
	<category>
		<pattern>TYPE1 VARIANT1</pattern>
		<template>
		    <think><set name="var1">value2</set></think>
                    You chose 
		    <condition name="var1" value="value1">X</condition>
		    <condition name="var1" value="value2">Y</condition>
		    <condition name="var1" value="value3">Z</condition>
		</template>
	</category>

        <!-- Example using global variable with name as attribute and value as child -->
	<category>
		<pattern>TYPE1 VARIANT2</pattern>
		<template>
		    <think><set name="var1">value1</set></think>
                    You chose 
		    <condition name="var1"><value>value1</value>X</condition>
		    <condition name="var1"><value>value2</value>Y</condition>
		    <condition name="var1"><value>value3</value>Z</condition>
		</template>
	</category>

        <!-- Example using global variable with name as child and value as an attribute -->
	<category>
		<pattern>TYPE1 VARIANT3</pattern>
		<template>
		    <think><set name="var1">value3</set></think>
                    You chose 
		    <condition value="value1"><name>var1</name>X</condition>
		    <condition value="value2"><name>var1</name>Y</condition>
		    <condition value="value3"><name>var1</name>Z</condition>
		</template>
	</category>

        <!-- Example using global variable and value as children -->
	<category>
		<pattern>TYPE1 VARIANT4</pattern>
		<template>
		    <think><set name="var1">value2</set></think>
                    You chose 
		    <condition><name>var1</name><value>value1</value>X</condition>
		    <condition><name>var1</name><value>value2</value>Y</condition>
		    <condition><name>var1</name><value>value3</value>Z</condition>
		</template>
	</category>

        <!-- Example showing what happens if noting is matched, nothing is displayed -->
	<category>
		<pattern>TYPE1 VARIANT1 NO MATCH</pattern>
		<template>
		    <think><set name="var1">XXX</set></think>
                    You chose 
		    <condition name="var1" value="value1">X</condition>
		    <condition name="var1" value="value2">Y</condition>
		    <condition name="var1" value="value3">Z</condition>
		</template>
	</category>

```

Running this grammar through the Bot we can ask the following questions and see the conditions in action

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> TYPE1 VARIANT1
You chose Y
>>> TYPE1 VARIANT2
You chose X
>>> TYPE1 VARIANT3
You chose Z
>>> TYPE1 VARIANT4
You chose Y
>>> TYPE1 VARIANT1 NO MATCH
You chose
```

For more information on this type of condition see [Block](./Template-Tags#type1)

## Single-predicate Condition
A single predicate condition allows you to create a construct which resembles the programming construct if then else or switch. Each li element of the condition is evaluated in turn, and processing stops as soon as the first element evaluates to true, then content of that element then used in the template. All further li elements are ignored.

If no li element evaluates to true the bot checks for a default value which is represented as an li tag without any name of value attributes/children. The content of this tag is then used.

The following examples show the various types of Single predicate condition statement.

```xml
        <!-- Example of a single predicate condition using a global variable defined as                     -->
        <!-- an attribute and the value also an attribute of the li tag. The condition has no default value -->
	<category>
		<pattern>TYPE2 VARIANT1 NO DEFAULT</pattern>
		<template>
		    <think><set name="var1">value2</set></think>
                    You chose 
		    <condition name="var1">
		        <li value="value1">X</li>
		        <li value="value2">Y</li>
		        <li value="value3">Z</li>
		    </condition>
		</template>
	</category>

        <!-- Example of a single predicate condition using a global  variable defined as                   -->
        <!-- an attribute and the value also an attribute of the li tag. The condition has a default value -->
	<category>
		<pattern>TYPE2 VARIANT1 WITH DEFAULT</pattern>
		<template>
		    <think><set name="var1">XXX</set></think>
                    You chose 
		    <condition name="var1">
		        <li value="value1">X</li>
		        <li value="value2">Y</li>
		        <li value="value3">Z</li>
		        <li>DEF</li>
		    </condition>
		</template>
	</category>

        <!-- Example of a single predicate condition using a global variable defined as                      -->
        <!-- an attribute and the value defined as a child of the li tag. The condition has no default value -->
	<category>
		<pattern>TYPE2 VARIANT2 NO DEFAULT</pattern>
		<template>
		    <think><set name="var1">value3</set></think>
                    You chose 
		    <condition name="var1">
		        <li> <value>value1</value>X</li>
		        <li> <value>value2</value>Y</li>
		        <li> <value>value3</value>Z</li>
		    </condition>
		</template>
	</category>

        <!-- In this example we show what happens when this is no match and no default value -->
	<category>
		<pattern>TYPE2 VARIANT2 NO MATCH</pattern>
		<template>
		    <think><set name="var1">XXX</set></think>
                    You chose 
		    <condition name="var1">
		        <li> <value>value1</value>X</li>
		        <li> <value>value2</value>Y</li>
		        <li> <value>value3</value>Z</li>
		    </condition>
		</template>
	</category>
```

Running this grammar through the Bot we can ask the following questions and see the conditions in action

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> TYPE2 VARIANT1 NO DEFAULT
You chose Y
>>> TYPE2 VARIANT1 WITH DEFAULT
You chose DEF
>>> TYPE2 VARIANT2 NO DEFAULT
You chose Z
>>> TYPE2 VARIANT2 NO MATCH
You chose
```

For more information on this type of condition see [Single Predicate](./Template-Tags#type2)

## Multi-predicate Condition
A multi predicate condition is very much like a multi step if - elseif - elseif - else statement in most programming languages. Each condition is independent and each has their own variable and value. The bot evaluates each condition in term until one resolves to true and then use the value of the li tag as the template value.

If no condition evaluates to true then the bot looks for an li with no name and value and uses that as the default value. Otherwise if none is found no value is returned from the condition.

The following examples show the various types of Single predicate condition statement.

```xml
        <!-- An example which shows multiple conditions some with different variables, others with the -->
        <!-- same variable but different values. No default values is defined                          -->
	<category>
	    <pattern>TYPE3 VARIANT1 NO DEFAULT</pattern>
	    <template>
		<think><set name="var1">value2</set></think>
                You chose
                <condition>
                    <li name='var1' value="value2">A</li>
                    <li value="value2"><name>var2</name>B</li>
                    <li name="var3"><value>value3</value>C</li>
                    <li><name>var4</name><value>value4</value>D</li>
                </condition>
	    </template>
	</category>

        <!-- An example which shows multiple conditions some with different variables, others with the -->
        <!-- same variable but different values. A default value is defined                            -->
	<category>
	    <pattern>TYPE3 VARIANT1 WITH DEFAULT</pattern>
	    <template>
                <think><set name="var1">XXX</set></think>
                You chose
                <condition>
                    <li name='var1' value="value2">A</li>
                    <li value="value2"><name>var2</name>B</li>
                    <li name="var3"><value>value3</value>C</li>
                    <li><name>var4</name><value>value4</value>D</li>
                    <li>DEF</li>
                </condition>
	    </template>
	</category>

        <!-- An example which shows multiple conditions some with different variables, others with the -->
        <!-- same variable but different values. No default value is defined. There is no match in     -->            
        <!-- example, and nothing evaluates so nothing is returned from the condition                  -->
	<category>
	    <pattern>TYPE3 VARIANT1 NO MATCH</pattern>
	    <template>
	        <think><set name="var1">XXX</set></think>
                You chose
                <condition>
                    <li name='var1' value="value2">A</li>
                    <li value="value2"><name>var2</name>B</li>
                    <li name="var3"><value>value3</value>C</li>
                    <li><name>var4</name><value>value4</value>D</li>
                </condition>
	    </template>
	</category>

```

Running this grammar through the Bot we can ask the following questions and see the conditions in action

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> TYPE3 VARIANT1 NO DEFAULT
You chose A
>>> TYPE3 VARIANT1 WITH DEFAULT
You chose DEF
>>> TYPE3 VARIANT1 NO MATCH
You chose 
```

For more information on this type of condition see [Multi Predicate](./Template-Tags#type3)

Default value

## Looping
Looping adds the final element to the condition structures and allows the condition to be re-evaluated repeatedly until one of the values evaluates to true.

In the first example below, the first pass through the condition, var1 = value2, this chooses the second li element, which returns 'Y' and then sets a value var1 = value3. In then also contains a loop tag, which causes the entire condition to be re-evaluated. This time as var1 = value3 the third li tag evaluates to true and the content 'Z' is returned. 

In the second example, the initial value of var2 = value2. Which means the second li statement evaluates to true and B is used as the content. The li statement also contains to tags which set 2 variables, var2 = value 3 and var4 = value 4. The loop tag then forces the entire condition statement to be re-evaluated. This time the var4 = value4 forces the 4th li tag to evaluate to true this time to append D to the output.

```xml
<aiml>
	<category>
		<pattern>TYPE2 LOOP</pattern>
		<template>
		    <think><set name="var1">value2</set></think>
                    You chose 
		    <condition name="var1">
		        <li value="value1">X</li>
		        <li value="value2">Y <think><set name="var1">value3</set></think><loop /></li>
		        <li value="value3">Z</li>
		    </condition>
		</template>
	</category>

	<category>
	    <pattern>TYPE3 LOOP</pattern>
	    <template>
	        <think><set name="var2">value2</set></think>
                You chose 
                <condition>
                    <li name='var1' value="value1">A</li>
                    <li value="value2">
                        <name>var2</name>
                        B
                        <think>
                            <set name="var2">value3</set>
                            <set name="var4">value4</set>
                        </think>
                        <loop />
                    </li>
                    <li name="var3"><value>value3</value>C</li>
                    <li><name>var4</name><value>value4</value>D</li>
                </condition>
	    </template>
	</category>

</aiml>
```

Running this grammar through the Bot we can ask the following questions and see the conditions in action

```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> TYPE2 LOOP
You chose Y Z
>>> TYPE3 LOOP
You chose B D
```
By combining additional AIML elements you can implement complex conditional and looping statements such as counting elements of a list, repeat calling of an external service until it responds without error etc.

For more information on how looping works, see the documentation on [Looping](./Template-Tags#looping)

To see more information on conditional statements, see the wiki page [Conditions](./Template-Tags#condition).


***
[Back to Tutorial](./AIML-Tutorial) | [Back - Variables](./Tutorial-Variables) | [Next - Date And Time](./Tutorial-Date-And-Time)