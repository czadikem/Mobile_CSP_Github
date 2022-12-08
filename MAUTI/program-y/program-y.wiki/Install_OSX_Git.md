# Installation on OSX Using Git

Before you install Programy on OSX you need to check that you have the pre-requisites installed, 
named Python 3.x and Pip. Installation instructions for OSX can be found in [OSX Prerequisites](Install_OSX_PreReqs)

## Pull Source Code
First off we need to create a directory to hold and initialise it for use with Git
```bash
Keiffs-MacBook-Pro-2:dev keith$ mkdir programy
Keiffs-MacBook-Pro-2:dev keith$ cd programy
Keiffs-MacBook-Pro-2:programy keith$ git init .
Initialized empty Git repository in /Users/keith/dev/programy/.git/
```

Next is to create a git connection to the remote repo and pull the code from that repo as follows
```bash
Keiffs-MacBook-Pro-2:programy keith$ git remote add github https://github.com/keiffster/program-y.git
Keiffs-MacBook-Pro-2:programy keith$ git pull github master
remote: Enumerating objects: 1302, done.
remote: Counting objects: 100% (1302/1302), done.
remote: Compressing objects: 100% (966/966), done.
remote: Total 20827 (delta 730), reused 669 (delta 323), pack-reused 19525
Receiving objects: 100% (20827/20827), 33.54 MiB | 4.13 MiB/s, done.
Resolving deltas: 100% (15379/15379), done.
From https://github.com/keiffster/program-y
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> github/master
Keiffs-MacBook-Pro-2:programy keith$ ls
CODE_OF_CONDUCT.md	README.md		master_checkin.sh	src
CONTRIBUTING.md		coverage.cmd		pylint.cfg		test
COPYRIGHT.txt		coverage.sh		pylint.sh
ISSUE_TEMPLATE.md	docs			requirements.txt
Keiffs-MacBook-Pro-2:programy keith$ 
```

You now have the code in place, the next 2 steps allow us to set the PYTHONPATH and then install the neccasary python requirements.

```bash
Keiffs-MacBook-Pro-2:programy keith$ export PYTHONPATH=/Users/keith/dev/programy/src
Keiffs-MacBook-Pro-2:programy keith$ pip3 install -r requirements.txt
```

This will install all of the neccassary python libraries. 

We can check its all installed by running Admin Tool

```bash
Keiffs-MacBook-Pro-2:programy keith$ python3 -m programy.admin.tool
Available commands are:

	help
	list
	download <bot-name>
	install <component>

Keiffs-MacBook-Pro-2:programy keith$ 
```

We can now install the additional components used by Programy

```bash
Keiffs-MacBook-Pro-2:programy keith$ python3 -m programy.admin.tool install textblob
Installing additional components for textblob
[nltk_data] Downloading package punkt to /Users/keith/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package brown to /Users/keith/nltk_data...
[nltk_data]   Package brown is already up-to-date!
[nltk_data] Downloading package punkt to /Users/keith/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package wordnet to /Users/keith/nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /Users/keith/nltk_data...
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
[nltk_data] Downloading package conll2000 to /Users/keith/nltk_data...
[nltk_data]   Package conll2000 is already up-to-date!
[nltk_data] Downloading package movie_reviews to
[nltk_data]     /Users/keith/nltk_data...
[nltk_data]   Package movie_reviews is already up-to-date!
(programy) Keiffs-MacBook-Pro-2:programy keith$ 
```

Now lets create a new directory to story our choice of first bot

```bash
 cd ..
Keiffs-MacBook-Pro-2:dev keith$ mkdir y-bot
Keiffs-MacBook-Pro-2:dev keith$ cd y-bot
Keiffs-MacBook-Pro-2:y-bot keith$ python3 -m programy.admin.tool download y-bot
Downloading [y-bot] from [https://github.com/keiffster/y-bot/archive/master.zip]
[..................................................................................................]
Download complete

To run y-bot bot in console mode, use the following commands

	cd scripts/xnix
	./y-bot.sh
```

### Console Client
```bash
Keiffs-MacBook-Pro-2:dev keith$cd scripts
Keiffs-MacBook-Pro-2:dev scripts keith$ cd xnix
Keiffs-MacBook-Pro-2:dev scripts ./y-bot.sh
Loading, please wait...
/Users/keith/mybots/programy/scripts/xnix
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 1 errors in your grammars, check your errors store
Found a total of 6 duplicates in your grammars, check your duplicates store
Y-Bot, App: v3.0.0 Beta 1 Grammar v1.6.0, initiated March 14, 2017
Hi, how can I help you today?
>>> hello
Good morning.
>>> who are you
Call me Y-Bot.
>>> 
```

# Working with your Bot
You are now ready to start working your with bot. To do this, jump to the next page [You and Your Bot](./You_And_Your_Bot)