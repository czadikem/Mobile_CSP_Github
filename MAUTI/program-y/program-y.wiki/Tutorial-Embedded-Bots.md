# Embedable Bots

## The Most Basic Bot
You can now embed a Programy bot into you own Python application with  2 lines of code, yes 2 lines of code. 
After first installing programy via pip as follows:
```
pip install programy
```
You can then add a bot to you code as using the following code and ask as many questions via the 'ask_question' method. 
Nothing else is required.

(Note it takes a few seconds (~30-50) to load the bot which has ~18,000 statements built into it)
```
from programy.clients.embed.basic import EmbeddedBasicBot

my_bot = EmbeddedBasicBot()

print("Response = %s" % my_bot.ask_question("Hello"))
```
And thats it, it loads a predefined set of grammars as close to Y-bot as possible, 
and you are can ask it as many questions as you like

## Datafile Bot
Once you get the hang of including a bot in your app, you'll want to be able to add your own AIML files and associated 
lookup files. You can do this by using the EmbeddedDataFileBot and passing it a dictionary containing data names and
associated files like this

```
files = {'aiml': ['y-bot/storage/categories'],
         'learnf': ['y-bot/storage/learnf'],
         'properties': 'y-bot/storage/properties/properties.txt',
         'defaults': 'y-bot/storage/properties/defaults.txt',
         'sets': ['y-bot/storage/sets'],
         'maps': ['y-bot/storage/maps'],
         'rdfs': ['y-bot/storage/rdfs'],
         'denormals': 'y-bot/storage/lookups/denormal.txt',
         'normals': 'y-bot/storage/lookups/normal.txt',
         'genders': 'y-bot/storage/lookups/gender.txt',
         'persons': 'y-bot/storage/lookups/person.txt',
         'person2s': 'y-bot/storage/lookups/person2.txt',
         'regexes': 'y-bot/storage/regex/regex-templates.txt',
         'spellings': 'y-bot/storage/spelling/corpus.txt',
         'preprocessors': 'y-bot/storage/processing/preprocessors.conf',
         'postprocessors': 'y-bot/storage/processing/postprocessors.conf',
         'postquestionprocessors': 'y-bot/storage/processing/postquestionprocessors.conf'
         }

my_bot = EmbeddedDataFileBot(files)

print("Response = %s" % my_bot.ask_question("Hello"))
```
Ok, so the big blob of Jason is more than one line, but you can now pass in a series of data files and they will be loaded and you can then just ask it questions

There are a log of data files, but if you just want it to pass AIML and use defaults for all the rest, you can 
use the following code and just pass the directory containing your AIML files
```
files = {'aiml': ['y-bot/storage/categories'] }

my_bot = EmbeddedDataFileBot(files, defaults=True)

print("Response = %s" % my_bot.ask_question("Hello"))
```

## Config File Bot
You can also embed a bot and have full control with a supplied config file as follows

```
from programy.clients.embed.datagile import EmbeddedConfigFileBot

my_bot = EmbeddedConfigFileBot(config_file)
```
or if you have a logging file available you can pass that too
```
from programy.clients.embed.datagile import EmbeddedConfigFileBot

my_bot = EmbeddedConfigFileBot(config_file, logging_file)
```
You can also create a config file with all of the configuration options 
```
from programy.clients.embed.datagile import EmbeddedConfigFileBot

EmbeddedConfigFileBot.generate_default_config_file('yaml)
```

***
[Back - Tutorial](./AIML-Tutorial) | [Next - Bot Template](./Tutorial-Bot-Template)