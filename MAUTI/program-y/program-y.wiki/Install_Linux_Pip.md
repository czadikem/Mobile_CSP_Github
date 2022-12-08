# Installation on Ubuntu Using Git

Before you install Programy on Ubuntu you need to check that you have the pre-requisites installed, 
named Python 3.x and Pip. Installation instructions for Ubuntu can be found in [Ubuntu Prerequisites](Install_Linux_PreReqs)

## Installing via Pip

First lets check the version of Python is 3.x and Pip 18.x or above
```bash
keith@ubuntu:~$ python3 --version
Python 3.6.7
keith@ubuntu:~$ pip3 --version
pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
keith@ubuntu:~$ 
```

Next create the folder that will hold our bots
```bash
keith@ubuntu:~$ mkdir mybots
keith@ubuntu:~$ cd mybots
keith@ubuntu:~/mybots$ 
```

Then we create a Python virtual environment to run out bot in. This is useful if you are just getting used
to programy and its many dependencies
```bash
keith@ubuntu:~/mybots$ python3 -m venv programy
keith@ubuntu:~/mybots$ cd programy
keith@ubuntu:~/mybots/programy$ 
```

Once you have created the virtual environment you need to activate it
```bash
keith@ubuntu:~/mybots/programy$ source ./bin/activate
(programy) keith@ubuntu:~/mybots/programy$ 
```

Next lets install programy into our virtual environment, the following shows the first 20 lines or so
of the console as Programy is downloaded from pypi and installed
```bash
(programy) keith@ubuntu:~/mybots/programy$ ^C
(programy) keith@ubuntu:~/mybots/programy$ pip3 install --no-cache-dir programyCollecting programy
  Downloading https://files.pythonhosted.org/packages/b5/67/dd1b8ff1211ac470061b60544b7e3fec9ceb486e46672b3502e1947c2989/programy-3.5.3.tar.gz (229kB)
    100% |████████████████████████████████| 235kB 3.5MB/s 
Collecting APScheduler==3.5.3 (from programy)
  Downloading https://files.pythonhosted.org/packages/97/3a/fa3213cc325091b7729616594611fff31d72c2d4d590418c3efdf7424ae2/APScheduler-3.5.3-py2.py3-none-any.whl (57kB)
    100% |████████████████████████████████| 61kB 24.0MB/s 
Collecting Flask-SocketIO==3.0.2 (from programy)
  Downloading https://files.pythonhosted.org/packages/f2/c7/2c7dbf4386d87fd3ac3e98ea9ea7f33db9c48ad5e0dcc3ac70718d9034b1/Flask_SocketIO-3.0.2-py2.py3-none-any.whl
Collecting Flask==1.0.2 (from programy)
  Downloading https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl (91kB)
    100% |████████████████████████████████| 92kB 10.1MB/s 
Collecting MetOffer==1.3.2 (from programy)
  Downloading https://files.pythonhosted.org/packages/97/d9/6c829f7dded7a3d5a4aeb2ff51abfad154b26dd2bf3e0eedc5e2561f4d1d/MetOffer-1.3.2.tar.gz
Collecting PyMySQL==0.9.2 (from programy)
```

Eventually the installer finished with the last few lines look like
```bash
  Running setup.py install for PyYAML ... done
  Running setup.py install for SQLAlchemy ... done
  Running setup.py install for autocorrect ... done
  Running setup.py install for kik ... done
  Running setup.py install for future ... done
  Running setup.py install for pymessenger ... done
  Running setup.py install for sleekxmpp ... done
  Running setup.py install for nltk ... done
  Running setup.py install for PySocks ... done
  Running setup.py install for viberbot ... done
  Running setup.py install for wget ... done
  Running setup.py install for wikipedia ... done
  Running setup.py install for programy ... done
Successfully installed APScheduler-3.5.3 Flask-1.0.2 Flask-SocketIO-3.0.2 Jinja2-2.10 MarkupSafe-1.1.0 MetOffer-1.3.2 PyJWT-1.7.1 PyMySQL-0.9.2 PySocks-1.6.8 PyYAML-4.2b4 SQLAlchemy-1.2.12 Werkzeug-0.14.1 asn1crypto-0.24.0 autocorrect-0.3.0 beautifulsoup4-4.6.3 certifi-2018.11.29 cffi-1.12.0 chardet-3.0.4 click-7.0 cryptography-2.5 emoji-0.5.1 future-0.17.1 idna-2.7 itsdangerous-1.1.0 kik-1.5.0 line-bot-sdk-1.8.0 lxml-4.2.5 nltk-3.4 oauthlib-3.0.1 programy-3.5.3 pycparser-2.19 pymessenger-0.0.7.0 pymongo-3.7.1 python-dateutil-2.7.3 python-engineio-3.3.2 python-socketio-3.1.2 python-telegram-bot-11.1.0 pytz-2018.9 redis-2.10.6 requests-2.20.0 requests-oauthlib-1.2.0 requests-toolbelt-0.9.1 singledispatch-3.4.0.3 six-1.12.0 slackclient-1.3.0 sleekxmpp-1.3.3 textblob-0.15.2 tweepy-3.6.0 twilio-6.18.1 tzlocal-1.5.1 urllib3-1.24.1 viberbot-1.0.11 websocket-client-0.54.0 wget-3.2 wikipedia-1.4.0
```

Lets check that its installed by running the Admin Tool
```bash
(programy) keith@ubuntu:~/mybots/programy$ python3 -m programy.admin.tool
Available commands are:

	help
	list
	download <bot-name>
	install <component>

(programy) keith@ubuntu:~/mybots/programy$ ```

We can now use the Admin Tool to install additional components, specifically textblob
```bash
(programy) keith@ubuntu:~/mybots/programy$ python3 -m programy.admin.tool install textblob
Installing additional components for textblob
[nltk_data] Downloading package punkt to /home/keith/nltk_data...
[nltk_data]   Unzipping tokenizers/punkt.zip.
[nltk_data] Downloading package brown to /home/keith/nltk_data...
[nltk_data]   Unzipping corpora/brown.zip.
[nltk_data] Downloading package punkt to /home/keith/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package wordnet to /home/keith/nltk_data...
[nltk_data]   Unzipping corpora/wordnet.zip.
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /home/keith/nltk_data...
[nltk_data]   Unzipping taggers/averaged_perceptron_tagger.zip.
[nltk_data] Downloading package conll2000 to /home/keith/nltk_data...
[nltk_data]   Unzipping corpora/conll2000.zip.
[nltk_data] Downloading package movie_reviews to
[nltk_data]     /home/keith/nltk_data...
[nltk_data]   Unzipping corpora/movie_reviews.zip.
(programy) keith@ubuntu:~/mybots/programy$
```

Finally we can download out first bot and install it
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

### Console Client
```bash
(programy) keith@ubuntu:~/mybots/programy$ cd scripts
(programy) keith@ubuntu:~/mybots/programy/scripts$ cd xnix
(programy) keith@ubuntu:~/mybots/programy/scripts/xnix$ ./y-bot.sh

Loading, please wait...
/home/keith/mybots/programy/scripts/xnix
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 1 errors in your grammars, check your errors store
Found a total of 6 duplicates in your grammars, check your duplicates store
Y-Bot, App: v3.0.0 Beta 1 Grammar v1.6.0, initiated March 14, 2017
Hi, how can I help you today?
>>> hello
Good morning.
>>> what are you
I'm a chatbot.
>>> 
```

# Working with your Bot
You are now ready to start working your with bot. To do this, jump to the next page [You and Your Bot](./You_And_Your_Bot)
