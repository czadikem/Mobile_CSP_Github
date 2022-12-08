# Available Chatbots

The /bots folder contains a number of bots, the AIML grammars for these bots have been sourced from various AIML sites, specifically Pandora who published Alice2 and Rosie. However, all have been set up with the right config and startup scripts to be compatible with Program-Y. As more bots are added to the project, they will be found here

## Alice2
This is the bot that was created to support AIML 2, and is an updated version of Alicebot which was the original bot created for AIML 1. It has a comprehensive set of grammars but is very America in some of its responses. Also I some of the more complex grammars either rely on none AIML 2.0 which are only implemented in the Pandora Bots. Still its a good start for most people

## Professor
The professor is a huge AIML grammar set, close to 500K categories. The original version was very buggy and had lots of errors and duplicates. However, this version has been thoroughly updated and corrected by user gimisa@yahoo.fr. It provides a great foundation for those looking for a general knowledge database. However be careful, it can take several minutes to load

## Rosie
A second bot created by the creators of AIML. Rosie has less grammars but is designed and documented to be the foundation for AIML 2.0 bot development. Easier to work with than Alice2, but still has one or 2 tags which are not AIML 2 compliant and only work with Pandora bots

## Talk-y
An experimental bot which provides Text To Speech and Speech To Text capabilities to allow you to 
talk to your bot via you computer microphone and hear what it says via the speakers. 

## Traintimes-y
A bot that uses the National Rail service APIs to provide train times and help services

## Y-Bot
This is my bot, being developed slowly with a complete set of grammar tests. Y-Bot is designed to both have a  good core knowledge for general chat discussions, a personality and also support a set of industry extensions such for use in Energy, Banking, and Telecoms

## Template-y
This is a foundation bot which provides you with a basic Bot with empty files. Its a starting point, a great way to start with an empty bot but with all the config and files created for you. 

# Installing a Bot

```bash
(programy) keith@ubuntu:~/mybots/programy$ python3 -m programy.admin.tool
Available commands are:

	help
	list
	download <bot-name>
	install <component>

(programy) keith@ubuntu:~/mybots/programy$ 
```

If you use 'python3 -m programy.admin.tool list' it will provide a list of all the bots you can download. In the example below, we have decided to download y-bot

```bash
(programy) keith@ubuntu:~/mybots/programy$ python3 -m programy.admin.tool download y-bot
Downloading [y-bot] from [https://github.com/keiffster/y-bot/archive/master.zip]
[.............................................................................]
Download complete

To run y-bot bot in console mode, use the following commands

	cd scripts/xnix
	./y-bot.sh
(programy) keith@ubuntu:~/mybots/programy$ 
```


