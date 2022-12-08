The parser supports a full set of AIML tags which are defined in the system included template_nodes.conf. You can modify this file to change the implementation of the node, or to add you own nodes. NOTE: This should be for advanced users only as changing a node implementation can seriously impact the performance and operation of the parser

```ini
word = programy.parser.template.nodes.word.TemplateWordNode
authorise = programy.parser.template.nodes.authorise.TemplateAuthoriseNode
random = programy.parser.template.nodes.rand.TemplateRandomNode
condition = programy.parser.template.nodes.condition.TemplateConditionNode
srai = programy.parser.template.nodes.srai.TemplateSRAINode
sraix = programy.parser.template.nodes.sraix.TemplateSRAIXNode
get = programy.parser.template.nodes.get.TemplateGetNode
set = programy.parser.template.nodes.set.TemplateSetNode
map = programy.parser.template.nodes.map.TemplateMapNode
bot = programy.parser.template.nodes.bot.TemplateBotNode
think = programy.parser.template.nodes.think.TemplateThinkNode
normalize = programy.parser.template.nodes.normalise.TemplateNormalizeNode
denormalize = programy.parser.template.nodes.denormalise.TemplateDenormalizeNode
person = programy.parser.template.nodes.person.TemplatePersonNode
person2 = programy.parser.template.nodes.person2.TemplatePerson2Node
gender = programy.parser.template.nodes.gender.TemplateGenderNode
sr = programy.parser.template.nodes.sr.TemplateSrNode
id = programy.parser.template.nodes.id.TemplateIdNode
size = programy.parser.template.nodes.size.TemplateSizeNode
vocabulary = programy.parser.template.nodes.vocabulary.TemplateVocabularyNode
eval = programy.parser.template.nodes.eval.TemplateEvalNode
explode = programy.parser.template.nodes.explode.TemplateExplodeNode
implode = programy.parser.template.nodes.implode.TemplateImplodeNode
program = programy.parser.template.nodes.program.TemplateProgramNode
lowercase = programy.parser.template.nodes.lowercase.TemplateLowercaseNode
uppercase = programy.parser.template.nodes.uppercase.TemplateUppercaseNode
sentence = programy.parser.template.nodes.sentence.TemplateSentenceNode
formal = programy.parser.template.nodes.formal.TemplateFormalNode
that = programy.parser.template.nodes.that.TemplateThatNode
thatstar = programy.parser.template.nodes.thatstar.TemplateThatStarNode
topicstar = programy.parser.template.nodes.topicstar.TemplateTopicStarNode
star = programy.parser.template.nodes.star.TemplateStarNode
input = programy.parser.template.nodes.input.TemplateInputNode
request = programy.parser.template.nodes.request.TemplateRequestNode
response = programy.parser.template.nodes.response.TemplateResponseNode
date = programy.parser.template.nodes.date.TemplateDateNode
interval = programy.parser.template.nodes.interval.TemplateIntervalNode
system = programy.parser.template.nodes.system.TemplateSystemNode
extension = programy.parser.template.nodes.extension.TemplateExtensionNode
learn = programy.parser.template.nodes.learn.TemplateLearnNode
learnf = programy.parser.template.nodes.learnf.TemplateLearnfNode
first = programy.parser.template.nodes.first.TemplateFirstNode
rest = programy.parser.template.nodes.rest.TemplateRestNode
log = programy.parser.template.nodes.log.TemplateLogNode
oob = programy.parser.template.nodes.oob.TemplateOOBNode
xml = programy.parser.template.nodes.xml.TemplateXMLNode
addtriple = programy.parser.template.nodes.addtriple.TemplateAddTripleNode
deletetriple = programy.parser.template.nodes.deletetriple.TemplateDeleteTripleNode
select = programy.parser.template.nodes.select.TemplateSelectNode
uniq = programy.parser.template.nodes.uniq.TemplateUniqNode
search = programy.parser.template.nodes.search.TemplateSearchNode

```

Each Template Tag inherits from the base class `programy.parser.template.nodes.base.TemplateNode`. This is quite a large base class and encapsulates both parsing of raw xml into the node attributes, but also the resolving the full node into text as part of the overall template evaluation.

The key methods to override include

* `def parse_expression(self, graph, expression)` - Parses an ET.Element xml structure into the node, throwing appropriate exceptions as needed
* `def resolve_to_string(self, bot, clientid)` - Resolves the node to a string, always called by resolve()
* `def resolve(self, bot, clientid)` - Called by the brain to resolve individual template nodes to a string. Resolutions are chained together to create a response sentence
* `def to_string(self)` - Provides a string version of the node for debugging and writing to brain tree in text mode
* `def to_xml(self, bot, clientid)` - Provides an xml version of the node. This is used for a variety of purposes including writing aiml files as part of learnf and writing XML version of the braintree to file
