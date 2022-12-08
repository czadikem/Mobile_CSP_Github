Once you start creating AIML files there are a number of configuration options that will help you when things are not working like you think they should

# Logging
The first step in debugging your AIML is to make sure that Program-Y is logging in DEBUG mode. This is done by setting the logging level in the logging.yaml configuration file as follows
```
root:
    level: DEBUG
```
Depending on where you have set the logger to write to, Program-Y will generate a huge amount of information as it loads and parses you AIML files.

On a Unix environemnt its best to tail this file so that you can watch it as Program_y executes.
```
tail -f /tmp/alice2.log
```

## Statistics
When Program-Y has finished loading in writes a number of statistics to the log file to tell you just what it has loaded and what if any errors and duplicates it may have found. The output will look similar to the following, but may differ based on the error and duplicate settings defined below.
```
2017-06-02 11:32:20,133  root       INFO    Total processing time 202.938356.2 secs
2017-06-02 11:32:20,134  root       INFO    Loaded a total of 204 aiml files with 508932 categories
2017-06-02 11:32:20,134  root       INFO    Thats approx 1.005231 aiml files per sec
2017-06-02 11:32:20,134  root       INFO    Saving aiml errors to file [/tmp/alice2_errors.txt]
2017-06-02 11:32:20,140  root       INFO    Saving aiml duplicates to file [/tmp/alice2_duplicates.txt]
2017-06-02 11:32:20,255  root       INFO    Found a total of 3300 errors in your grammrs, check out [/tmp/alice2_errors.txt] for details
2017-06-02 11:32:20,255  root       INFO    Found a total of 74446 duplicate patterns in your grammrs, check out [/tmp/alice2_duplicates.txt] for details
2017-06-02 11:32:20,255  root       DEBUG   Dumping AIML Graph as tree to [/tmp/alice2_braintree.txt]
2017-06-02 11:32:55,221  root       INFO    Loaded a total of 140 denormalisations
2017-06-02 11:32:55,226  root       INFO    Loaded a total of 458 normalisations
2017-06-02 11:32:55,227  root       INFO    Loaded a total of 15 genderisations
2017-06-02 11:32:55,228  root       INFO    Loaded a total of 56 persons
2017-06-02 11:32:55,230  root       INFO    Loaded a total of 9 person2s
2017-06-02 11:32:55,230  root       INFO    Loaded a total of 78 predicates
2017-06-02 11:32:55,231  root       INFO    Loaded a total of 5 pronouns
2017-06-02 11:32:55,232  root       INFO    Loaded a total of 23 properties
2017-06-02 11:32:55,248  root       INFO    Loaded a total of 5677 triples
```

# Dumping The Parse Tree
The braintree option in the 'brain' section of the configuration option tells the program to output the entire parse tree once it has been loaded. This will write a text or xml version of the tree (depending on the value of the `content` option), showing all the hierarchy and all the nodes as they are stored in memory to the file specified in the `file` option

```
brain:
    braintree:
      file: /tmp/braintree.xml
      content: xml
```
The file is rewritten every time the program executes, so you always have the latest tree.

For more details and explanation see [The Brain Tree](./The-Brain-Tree)

## Viewing the Braintree
A new addition to the bot is the ability to view the entire xml tree. See src/utils/braintree_viewer/viewer.py. This is a simple Tk app that loads the xml specified as the only command line paramater. Over time this app will be developed further, but for now its a useful util to view the braintree.

# Savings Errors
As the program parses you AIML, it may come across invalid xml or invalid AIML definitions. As describe above in logging these are output to the log file, however in Debug mode, Program-Y can generate quite a lot of logging. Therefore by setting the 'errors' option of the 'aiml' section of the 'files' section of 'brain' configuration as shown below, Program-Y will write each AIML error to this file along with the filename and the approx line number on the file where the error occurs
```
brain:
    files:
        aiml:
             errors: /tmp/alice2_errors.txt
             duplicates: /tmp/alice2_duplicates.txt
```
The setting is a full path to the file you want errors written to. The contents of the file will look like the following snapshot
```
Error, unsupported random child tag: search in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/personality.aiml] at [line(1676), column(0)]
Error, invalid get in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/rsvp.aiml] at [line(34), column(69)]
Error, invalid get in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/rsvp.aiml] at [line(48), column(69)]
Error, oob not implemented yet! in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/sraix.aiml] at [line(74), column(134)]
Error, oob not implemented yet! in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/sraix.aiml] at [line(82), column(65)]
Error, unsupported random child tag: eval in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/train.aiml] at [line(286), column(55)]
Error, invalid get in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/triple.aiml] at [line(62), column(71)]
Error, invalid get in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/triple.aiml] at [line(77), column(76)]
```

# Saving Duplicates
One of the most frustrating parts of creating grammars is when you don't get the answer you are expecting. If you are importing grammars from other sources, then it's possible that you can end up with duplicate questions resulting in different answers. Program-Y will create the necessary parse subtree the first time it parses a question, subsequent times the parsing leads to the same end node and a template exists at that node, the new subtree is thrown away and a duplicate warning is raised.  You can capture these duplicates in a single file by setting the 'duplicates' option of the 'aiml' section of the 'files' section of 'brain' configuration as shown below, Program-Y will write each duplicate grammar to this file each time it finds one
```
brain:
    files:
        aiml:
             duplicates: /tmp/alice2_duplicates.txt
```
The setting is a full path to the file you want duplicates written to. The contents of the file will look like the following snapshot
```
Dupicate grammar tree found [None] in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/knowledge.aiml]
Dupicate grammar tree found [None] in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/knowledge.aiml]
Dupicate grammar tree found [SEND TEXT MESSAGE TO *] in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/reductions2.aiml]
Dupicate grammar tree found [JOKE] in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/sraix_combine.aiml]
Dupicate grammar tree found [LIMERICK] in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/sraix_combine.aiml]
Dupicate grammar tree found [I ] in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/train.aiml]
Dupicate grammar tree found [I AM ] in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/train.aiml]
Dupicate grammar tree found [None] in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/train.aiml]
Dupicate grammar tree found [None] in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/alice2/train.aiml]
Dupicate grammar tree found [WATER IS WET] in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/professor/professor.0001.aiml]
Dupicate grammar tree found [WAS JOHN F KENNEDY ASSASINATED] in [/Users/keithsterling/Documents/Development/Python/Projects/AIML/program-y/bots/alice2/aiml/professor/professor.0001.aiml]
```
# Saving Conversations
By adding the `conversation` option to the aiml section of files in the brain settings, the bot will write a line to the file specified for every question answered. 
```
brain:
    files:
        aiml:
            conversation: /tmp/y-bot-conversation.txt
```
It will show the timestamp, clientid, question and answer as follows
```
2017-08-31 15:58:48 - Console - Question[hello] - Response[Hi there!]
2017-08-31 15:58:57 - Console - Question[How are you] - Response[Feeling really joyful today.]
2017-08-31 15:59:35 - Console - Question[location] - Response[I'm currently in Kinghorn.]
```

