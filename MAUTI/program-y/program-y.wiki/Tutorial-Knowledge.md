There are a number of different ways in which to add knowledge to your Bot. The most simplest way is to add a huge number of questions and associated reductions for all the types of things you want you bot to know
```
Example goes here
```
Alternatively, you can use the `learn` and `learnf` tags described in [Learning](./Tutorial-Learning) section of this tutorial. 

However AIML also supported the use of RDF to add specific knowledge in the form of subject -> predicate -> object patterns that can then be used to extract and reference knowledge about the objects

* addtriples
* deletetriple
* select
* uniq
* get
  * tuple

```xml
<category>
    <pattern>HELLO *</pattern>
    <template>
        <XXX><star /></XXX>
    </template>
</category>
```
	
```bash
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> XXX
YYY
```

***
[Back to Tutorial](./AIML-Tutorial) | [Back - List Processing](./Tutorial-List-Processing) | [Next - Learning](./Tutorial-Learning)