The history of Program-Y is all about learning how to build and operate a ChatBot. When I started this project is was an attempt to see if I could actually write one, and then could I write one that implements all of the AIML 2.0 spec, and then could I write one that other people could use, extend and also learn how chatbots operate. Therefore the core guiding principles are 

## 100% Open Source
Not a single line of code is hidden from anyone wanting to explore how an AIML based chatbot works. The core engine, Utilit and a wide range of extensions are open source and will stay open source for ever.

## 100% AIML 2.0 Support
AIML is a great language for chatbot development, and the 2.0 spec offers some major improvements over 1.0. However there are limited implementations and most of them are hosted solutions such as PandoraBots. To fully show the power of AIML the full 2.0 spec needed to be implemented, which would then also allow users to upload their grammars to commercial sites with little of no change.

## 100% Python
Python is a great language, easy to learn, easy to modify and also easy to read. This makes it a great choice for programmers wanting to see how key parts of a chatbot are implemented. Program-Y will remain current with Python 3.x for ever.

These 3 principles have meant a number of choices had to made which impacted the design. Specifically the choice of programme paradigm meant easy readability over high performance was paramount. I do not use any functional programming other than list comprehensions, I also do not try and optimise the code too much, rather favouring readability over hard to read complex code structures.

Hope you enjoy it....