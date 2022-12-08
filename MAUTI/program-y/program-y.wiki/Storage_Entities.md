#Storage Entities

Each storage engine provides the ability to handle a range of different entities. 
Primary storage engines such as File, SQL and Mongo can handle all entity types, where as more specialist
engines such as Redis and Logger only handle specific entities. See their specific documentation for details of 
what is supported and why

The entities support at this time are as follows

* categories - All AIMl files
* errors - A list of errors produced when loading the AIML files during the current load
* duplicates - A list of all duplicates produced when loading the AIML files during the current load
* learnf - A subset of categories used to store AIML categories generated from evaluating learnf nodes
* conversations - A record of all conversations as they happend

* maps - All the maps to be loaded by the bot at start up
* sets - All the sets to be loaded by the bot at start up
* rdf - All the rdf entities to be loaded by the bot at start up

* denormal - List of denormaalisations to be loaded by the bot at start up
* normal - A list of normalisations to be loaded by the bot at start up
* gender - A list of genderisations to be loaded by the bot at start up
* person - A list of personalisations in the first person to be loaded by the bot at start up
* person2 - A list of personalisations in the second person to be loaded by the bot at start up

* regex_templates - A list of all regular expression templates to be loaded by the bot at start up

* properties - A list of properties to be loaded by the bot
* defaults - A list of properties with default values to be added to each new conversaiton

* twitter - Ony required when running the twitter client, and used to cache the latest twitter messages ids

* spelling_corpus - The spelling corpus to be loaded by the spelling checker if in use
* license_keys - List of all license keys to be loaded by the bot

* pattern_nodes - A list of the pattern nodes to support
* template_nodes - A list of the template nodes to support, typically AIML 2.1

* binaries - If you want to cache the brain as a binary file, then this entity holds that content
* braintree - If you want to export the brain as a structured XML file, then this entity holds that configuration

* preprocessors - A list of all preprocessors to load in order and apply to all questions before passing to the bot
* postprocessors - A list of all post processors to load in order and apply to the answer before display

* usergroups - User group information used by the Authentication extensions of programy


