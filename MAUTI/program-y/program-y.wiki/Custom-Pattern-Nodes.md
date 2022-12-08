# Supported Tags
The parser supports a full set of AIML tags which are defined in the system included pattern_nodes.conf. You can modify this file to change the implementation of the node, or to add you own nodes. NOTE: This should be for advanced users only as changing a node implementation can seriously impact the performance and operation of the parser

```ini
#AIML 1.0
root = programy.parser.pattern.nodes.root.PatternRootNode
word = programy.parser.pattern.nodes.word.PatternWordNode
priority = programy.parser.pattern.nodes.priority.PatternPriorityWordNode
oneormore = programy.parser.pattern.nodes.oneormore.PatternOneOrMoreWildCardNode
topic = programy.parser.pattern.nodes.topic.PatternTopicNode
that = programy.parser.pattern.nodes.that.PatternThatNode
template = programy.parser.pattern.nodes.template.PatternTemplateNode

#AIML 2.0
zeroormore = programy.parser.pattern.nodes.zeroormore.PatternZeroOrMoreWildCardNode
set = programy.parser.pattern.nodes.set.PatternSetNode
bot = programy.parser.pattern.nodes.bot.PatternBotNode

#Program-Y
iset = programy.parser.pattern.nodes.iset.PatternISetNode
regex = programy.parser.pattern.nodes.regex.PatternRegexNode 
```

Each Pattern Tag inherits from the base class `programy.parser.pattern.nodes.base.PatternNode`. This is quite a large base class and encapsulates both parsing of raw xml into the node attributes, but also the matching a word to the type of node during pattern evaluation.

The key methods to override include

* `def equivalent(self, other)` - Tests if the node other is equivalent to the node carrying out the check.
* `def equals(self, bot, client, words, word_no)` - Checks if the word matches the rules of the node.
* `def to_string(self, verbose=True)` - Converts the node to string representation for debugging purposes
* `def to_xml(self, bot, clientid)` - Convers the node to xml format both for saving to xml version of the braintree and for debugging purposes.



