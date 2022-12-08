As various people ask me questions about the direction and reasons for Program-Y I find myself repeating myself. I therefore think its worth making most of these questions available as an FAQ

### Why AIML

AIML is one of a number of grammar based chat bot systems, along with the likes of ChatScript etc. They all provide a mechanism to define grammars with wildcards that allow a range of questions to be reduced to a smaller number of answers. AIML has been around the longest and is quite mature with lots of support on line. There are other options for creating chatbots, specifically

  * Machine Learning - This takes a huge amount of data, and when first building a client you just don’t have the data. The models for NLP take a lot of processing and the overhead of maintaining the data set becomes quite large. ML is great for the likes of Google, Apple, Facebook etc, but not for us mere mortals with a single Mac Book pro for development

  * NLP - There are a lot of good NLP libraries both for Python and other languages, but again you need to really know the subject matter and then implement quite a lot of the basics that AIML provides because of how it works

  * External Systems - Wit.ai, Facebook Amazon, and now Google all provide capabilities to call their API with some text and get a parsed version back. These mainly provide target, subject and action, but you then need to have a parser for these elements, again something that AIML provides as part of its implementation.

Right now if you are starting out I would recommend either AIML or Chatscript and then refine that choice by the language you prefer. Chatscript is huge Perl system that needs compiling, where as ProgramY is available in quite a few languages. Its also very easy to get start quickly with AIML and prove concepts in front of customers

As you say one of the benefits of an wholly deployed system like Program-Y is that you maintained ALL the data with it hosted where you want. One of the roadmap features is to develop stronger use of databases rather than flat files for storage of data, questions  and answers

### Long term plan for Program-Y

Right now its about getting to 1.0 which I think will be within the next month. A couple of core features and more unit testing will have a fully compliant 2.0 parser with a good core personality and a full suite of documented extensions for various industries ( Banking, Energy, Telecoms etc ).  A large part of getting to 1.0 is the documentation which I am working on at the moment both in terms of how to install and develop against the core platform, but also a full aiml 2.0 tutorial

Longer term there are a number of areas of development I am looking at

1) Clients. I like to add Facebook, Slack, and now Skype !, and also move Twitter and Facebook clients from a poling model to use the newer streaming APIs

2) Personality. I want to be able to add a much richer personality. I have already started on added emotion. A simple system that provides an option to each response based on the previous responses by the user. As the interaction develops the emotion will fluctuate and therefore the answers

3) External Data Sources. At the moment you can query Met Office Weather, Wikipedia, Pandora, Pannous and News Feeds. Longer term I want to add Google and Bing queries, but also more specific data sources.

4) Industry Support. The current industry extensions for YBot are basic Q&A for Energy, Banking and Telecoms ( my own personal work history ). The aim is to extend these further and also look at additional industries. I’ve had a query about a basic medical system and also a legal Q&A bot too, so plenty of scope to develop further

5) Knowledge. A much longer term is to build in an object orientated database of knowledge based on facts and then to provide a query system on top of this. This should allow the storing of all sorts of data with associated attributes and then to have queries against it. As long as you can classify a set of data and the define queries on the attributes you start to build a powerful knowledge base that Y-Bot learns from

### How much of an issue do you think it is that AIML 2.0 is not finalised after four years, and Dr Wallace seems to have gone silent in 2016?

AIML 1.0 took years to finalise and even now 1.0.1 is still referred to as Working Draft ( http://www.alicebot.org/TR/2001/WD-aiml/ ). AIML at is purest is an academic system. Dr Wallace being a research professor whose focus is wider AI. and like much of academic work it has proved itself as an idea and now more commercial applications are the focus. Wallace is pretty  much involved in the joint venture with Fritz Inc which run Pandora Bots.

In terms of AIML 2, I doubt it will ever become a true final version. You can see this by the number of extensions that Pandora have added without referencing them back into the 2.0 spec, again another representation of the commercialisation of this type of work. I try and keep up and ProgramY actually now is fully 2.0 compliance, but also 95% Pandora compliant, but also has 2 or 3 of my own tags that I think the spec is missing. A new version coming soon will allow you to specify the level of ‘strictness’ wither 2.0, Pandora or Mine in terms of tags supported

Wallace keeps an eye on 2.0 usage and responds on chatbots.org to questions on AIML so he is still involved I just think there is little more to add to the grammar

