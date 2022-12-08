# Creating a Brain Tree
Program-Y provides a way to examine the internal parse tree structure that contains your grammars.
The first stage to create a tree is to use the brain config item 'dump_to_file'. The value for this should be a file that the program will write the entire contents of the tree once loaded. An example is shown below, here th program writes to /tmp/alice2_braintree.txt

    brain:
        allow_system_aiml: true
        allow_learn_aiml: true
        allow_learnf_aiml: true
        dump_to_file: /tmp/alice2_braintree.txt

# Deciphering the Brain Tree
Once you have a brain tree you will want to understand what information is being displayed, below is a segment of a real parse tree

```
ROOT [P(4)^(0)#(1)C(994)_(1)*(1)To(0)Th(0)Te(0)]
        PWORD [P(0)^(0)#(0)C(1)_(0)*(0)To(0)Th(0)Te(0)] word=[WHO]
                WORD [P(0)^(0)#(0)C(1)_(0)*(0)To(0)Th(0)Te(0)] word=[IS]
                        WORD [P(0)^(0)#(0)C(0)_(0)*(0)To(1)Th(0)Te(0)] word=[ALICE]
                                TOPIC [P(0)^(0)#(0)C(0)_(0)*(1)To(0)Th(0)Te(0)]
                                        ONEORMORE [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(1)Te(0)] wildcard=[*]
                                                THAT [P(0)^(0)#(0)C(0)_(0)*(1)To(0)Th(0)Te(0)]
                                                        ONEORMORE [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(0)Te(1)] wildcard=[*]
                                                                PTEMPLATE [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(0)Te(1)] 
                                                                        {[WORD]I}
                                                                        {[WORD]am}
                                                                        {[BOT ([NODE])]}
                                                                        {[WORD].}
        PWORD [P(0)^(0)#(0)C(2)_(0)*(1)To(0)Th(0)Te(0)] word=[EMAIL]
                ONEORMORE [P(0)^(0)#(0)C(6)_(0)*(0)To(1)Th(0)Te(0)] wildcard=[*]
                        TOPIC [P(0)^(0)#(0)C(0)_(0)*(1)To(0)Th(0)Te(0)]
                                ONEORMORE [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(1)Te(0)] wildcard=[*]
                                        THAT [P(0)^(0)#(0)C(0)_(0)*(1)To(0)Th(0)Te(0)]
                                                ONEORMORE [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(0)Te(1)] wildcard=[*]
                                                        PTEMPLATE [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(0)Te(1)] 
                                                                {[SRAI]}
                                                                        {[WORD]CONTACTINIT}
                                                                {THINK}
                                                                        {[SET [Global] - [NODE]]}
                                                                                {STAR Index=1}
                                                                {[SRAI]}
                                                                        {[WORD]EMAILACTION}
```

## Node Definition 
For each node in the tree you get what may look like a cryptic definition, but this is just short hand for the contents of the node, for example the Root node ( which every tree has one and only one of ) looks like this
'''
ROOT [P(4)^(0)#(1)C(994)_(1)*(1)To(0)Th(0)Te(0)]
'''
The breakdown as follows
* ROOT - Name of the node, in this case ROOT
* P(n) - How many priority child nodes it contains, in this instance 4
* ^(n) - 1 if there is a wild card ^ present, otherwise 0
* #(n) - 1 if there is a wild card # present, otherwise 0
* C(n) - How many child nodes 
* _(n) - 1 if there is a wild card _ present, otherwise 0
* *(n) - 1 if there is a wild card * present, otherwise 0
* To(n) - 1 if a Topic node is present, otherwise 0
* Th(n) - 1 if a That node is present, otherwise 0
* Te(n) - 1 if a Template node is present, otherwise 0

So for each node, you can now see in detail the parse tree structure, for example, for a very basic AIML grammar

```
    <category>
        <pattern>SOMEBODY #</pattern>
        <template>Who</template>
    </category>
```

The node tree structure recorded internally in the parse tree would be 

```
             :
             :
                WORD [P(0)^(0)#(1)C(0)_(0)*(0)To(0)Th(0)Te(0)] word=[SOMEBODY]
                        ZEROORMORE [P(0)^(0)#(0)C(0)_(0)*(0)To(1)Th(0)Te(0)] wildcard=[#]
                                TOPIC [P(0)^(0)#(0)C(0)_(0)*(1)To(0)Th(0)Te(0)]
                                        ONEORMORE [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(1)Te(0)] wildcard=[*]
                                                THAT [P(0)^(0)#(0)C(0)_(0)*(1)To(0)Th(0)Te(0)]
                                                        ONEORMORE [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(0)Te(1)] wildcard=[*]
                                                                PTEMPLATE [P(0)^(0)#(0)C(0)_(0)*(0)To(0)Th(0)Te(1)] 
                                                                        {[WORD]Who}
             :
             :
```

Shows the structure of a WORD node. ( A node that contains a single word of text ).
* The word node contains the text 'SOMEBODY'
* It has one child node, a wildcard # node.
* The wildcard has one child, Topic 
* Topic has one child, a wildcard * node.
* The wildcard has one child, That 
* That has one child, a wildcard * node.
* The wildcard has one child, a Template
* The Template has one child, a word node 'Who'

