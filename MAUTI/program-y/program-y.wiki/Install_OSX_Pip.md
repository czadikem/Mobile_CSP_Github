# Installation on OSX Using Pip

Before you install Programy on OSX you need to check that you have the pre-requisites installed, 
named Python 3.x and Pip. Installation instructions for OSX can be found in [OSX Prerequisites](Install_OSX_PreReqs)

## Installing via Pip

First lets check the version of Python is 3.x and Pip 18.x or above
```bash
(programy) Keiffs-MacBook-Pro-2:programy keith$ python --version
Python 3.7.2
(programy) Keiffs-MacBook-Pro-2:programy keith$ pip3 --version
pip 18.1 from /Users/keith/mybots/programy/lib/python3.7/site-packages/pip (python 3.7)
(programy) Keiffs-MacBook-Pro-2:programy keith$ 
```

Next create the folder that will hold our bots
```bash
Keiffs-MacBook-Pro-2:~ keith$ mkdir mybots
Keiffs-MacBook-Pro-2:~ keith$ cd mybots
```

Then we create a Python virtual environment to run out bot in. This is useful if you are just getting used
to programy and its many dependencies
```bash
Keiffs-MacBook-Pro-2:mybots keith$ python3 -m venv programy
Keiffs-MacBook-Pro-2:mybots keith$ cd programy
```

Once you have created the virtual environment you need to activate it
```bash
Keiffs-MacBook-Pro-2:programy keith$ source ./bin/activate
(programy) Keiffs-MacBook-Pro-2:programy keith$ 
```

Next lets install programy into our virtual environment, the following shows the first 20 lines or so
of the console as Programy is downloaded from pypi and installed
```bash
(programy) Keiffs-MacBook-Pro-2:programy keith$ pip3 install --no-cache-dir programy
Collecting programy
  Downloading https://files.pythonhosted.org/packages/58/9a/faa96bc30515f8ddf8b624ee89bff99b41ff74e6ffa48a84d011360e47d7/programy-3.5.2.tar.gz (229kB)
    100% |████████████████████████████████| 235kB 299kB/s 
Collecting python-dateutil==2.7.3 (from programy)
  Downloading https://files.pythonhosted.org/packages/cf/f5/af2b09c957ace60dcfac112b669c45c8c97e32f94aa8b56da4c6d1682825/python_dateutil-2.7.3-py2.py3-none-any.whl (211kB)
    100% |████████████████████████████████| 215kB 873kB/s 
Collecting beautifulsoup4==4.6.3 (from programy)
  Downloading https://files.pythonhosted.org/packages/21/0a/47fdf541c97fd9b6a610cb5fd518175308a7cc60569962e776ac52420387/beautifulsoup4-4.6.3-py3-none-any.whl (90kB)
    100% |████████████████████████████████| 92kB 1.1MB/s 
Collecting lxml==4.2.5 (from programy)
  Downloading https://files.pythonhosted.org/packages/da/9c/901d13b9d84262082e81d38879600dcec28beb994ae08d1a7cbab4dc3ece/lxml-4.2.5-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (8.6MB)
    100% |████████████████████████████████| 8.6MB 726kB/s 
Collecting PyYAML==4.2b4 (from programy)
  Downloading https://files.pythonhosted.org/packages/a8/c6/a8d1555e795dbd0375c3c93b576ca13bbf139db51ea604afa19a2c35fc03/PyYAML-4.2b4.tar.gz (262kB)
    100% |████████████████████████████████| 266kB 1.4MB/s 
Collecting requests==2.20.0 (from programy)
  Downloading https://files.pythonhosted.org/packages/f1/ca/10332a30cb25b627192b4ea272c351bce3ca1091e541245cccbace6051d8/requests-2.20.0-py2.py3-none-any.whl (60kB)
    100% |████████████████████████████████| 61kB 458kB/s 
Collecting Flask==1.0.2 (from programy)
  Downloading https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl (91kB)
    100% |████████████████████████████████| 92kB 1.1MB/s 
Collecting Flask-SocketIO==3.0.2 (from programy)
  Downloading https://files.pythonhosted.org/packages/f2/c7/2c7dbf4386d87fd3ac3e98ea9ea7f33db9c48ad5e0dcc3ac70718d9034b1/Flask_SocketIO-3.0.2-py2.py3-none-any.whl
Collecting tweepy==3.6.0 (from programy)
  Downloading https://files.pythonhosted.org/packages/05/f1/2e8c7b202dd04117a378ac0c55cc7dafa80280ebd7f692f1fa8f27fd6288/tweepy-3.6.0-py2.py3-none-any.whl
```

Eventually the installer finished with the last few lines look like
```bash
  Downloading https://files.pythonhosted.org/packages/c5/10/369f50bcd4621b263927b0a1519987a04383d4a98fb10438042ad410cf88/singledispatch-3.4.0.3-py2.py3-none-any.whl
Collecting pycparser (from cffi!=1.11.3,>=1.8->cryptography->python-telegram-bot==11.1.0->programy)
  Downloading https://files.pythonhosted.org/packages/68/9e/49196946aee219aead1290e00d1e7fdeab8567783e83e1b9ab5585e6206a/pycparser-2.19.tar.gz (158kB)
    100% |████████████████████████████████| 163kB 2.5MB/s 
kik 1.5.0 has requirement six==1.10.0, but you'll have six 1.12.0 which is incompatible.
Installing collected packages: six, python-dateutil, beautifulsoup4, lxml, PyYAML, idna, certifi, chardet, urllib3, requests, click, Werkzeug, MarkupSafe, Jinja2, itsdangerous, Flask, python-engineio, python-socketio, Flask-SocketIO, oauthlib, requests-oauthlib, PySocks, tweepy, sleekxmpp, asn1crypto, pycparser, cffi, cryptography, future, python-telegram-bot, requests-toolbelt, pymessenger, PyJWT, pytz, twilio, websocket-client, slackclient, viberbot, line-bot-sdk, kik, wikipedia, MetOffer, tzlocal, APScheduler, emoji, autocorrect, redis, pymongo, SQLAlchemy, PyMySQL, wget, singledispatch, nltk, textblob, programy
  Running setup.py install for PyYAML ... done
  Running setup.py install for PySocks ... done
  Running setup.py install for sleekxmpp ... done
  Running setup.py install for pycparser ... done
  Running setup.py install for future ... done
  Running setup.py install for pymessenger ... done
  Running setup.py install for viberbot ... done
  Running setup.py install for kik ... done
  Running setup.py install for wikipedia ... done
  Running setup.py install for MetOffer ... done
  Running setup.py install for tzlocal ... done
  Running setup.py install for autocorrect ... done
  Running setup.py install for SQLAlchemy ... done
  Running setup.py install for wget ... done
  Running setup.py install for nltk ... done
  Running setup.py install for programy ... done
Successfully installed APScheduler-3.5.3 Flask-1.0.2 Flask-SocketIO-3.0.2 Jinja2-2.10 MarkupSafe-1.1.0 MetOffer-1.3.2 PyJWT-1.7.1 PyMySQL-0.9.2 PySocks-1.6.8 PyYAML-4.2b4 SQLAlchemy-1.2.12 Werkzeug-0.14.1 asn1crypto-0.24.0 autocorrect-0.3.0 beautifulsoup4-4.6.3 certifi-2018.11.29 cffi-1.12.0 chardet-3.0.4 click-7.0 cryptography-2.5 emoji-0.5.1 future-0.17.1 idna-2.7 itsdangerous-1.1.0 kik-1.5.0 line-bot-sdk-1.8.0 lxml-4.2.5 nltk-3.4 oauthlib-3.0.1 programy-3.5.2 pycparser-2.19 pymessenger-0.0.7.0 pymongo-3.7.1 python-dateutil-2.7.3 python-engineio-3.3.2 python-socketio-3.1.2 python-telegram-bot-11.1.0 pytz-2018.9 redis-2.10.6 requests-2.20.0 requests-oauthlib-1.2.0 requests-toolbelt-0.9.1 singledispatch-3.4.0.3 six-1.12.0 slackclient-1.3.0 sleekxmpp-1.3.3 textblob-0.15.2 tweepy-3.6.0 twilio-6.18.1 tzlocal-1.5.1 urllib3-1.24.1 viberbot-1.0.11 websocket-client-0.54.0 wget-3.2 wikipedia-1.4.0
```

Lets check that its installed by running the Admin Tool
```bash
(programy) Keiffs-MacBook-Pro-2:programy keith$ python3 -m programy.admin.tool
Available commands are:

	help
	list
	download <bot-name>
	install <component>

(programy) Keiffs-MacBook-Pro-2:programy keith$ 
```

We can now use the Admin Tool to install additional components, specifically textblob

```bash
(programy) Keiffs-MacBook-Pro-2:programy keith$ python3 -m programy.admin.tool install textblob
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

Finally we can download out first bot and install it
```bash
(programy) Keiffs-MacBook-Pro-2:programy keith$ python3 -m programy.admin.tool download y-bot
Removing existing file from [/Users/keith/mybots/programy]
Downloading [y-bot] from [https://github.com/keiffster/y-bot/archive/master.zip]
[..................................................................................................]
Download complete

To run y-bot bot in console mode, use the following commands

	cd scripts/xnix
	./y-bot.sh
(programy) Keiffs-MacBook-Pro-2:programy keith$ 
```

### Console Client
```bash
(programy) Keiffs-MacBook-Pro-2:programy keith$ cd scripts
(programy) Keiffs-MacBook-Pro-2:scripts keith$ cd xnix
(programy) Keiffs-MacBook-Pro-2:scripts keith$ ./y-bot.sh
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

### REST Server
```bash
(programy) Keiffs-MacBook-Pro-2:xnix keith$ ./y-bot-flask-rest.sh 
Initiating Flask REST Service...
Loading, please wait...
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 1 errors in your grammars, check your errors store
Found a total of 6 duplicates in your grammars, check your duplicates store
flask Client running on 0.0.0.0:8989
flask Client running in http mode, careful now !
 * Serving Flask app "client" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
```

### Webchat Server
```bash
(programy) Keiffs-MacBook-Pro-2:xnix keith$  ./y-bot-webchat.sh
Initiating WebChat Client...
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 1 errors in your grammars, check your errors store
Found a total of 6 duplicates in your grammars, check your duplicates store
WebChat Client running on 0.0.0.0:8090
WebChat Client running in http mode, careful now !
 * Serving Flask app "client" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
```

Point your browser at http://localhost:8090

# Working with your Bot
You are now ready to start working your with bot. To do this, jump to the next page [You and Your Bot](./You_And_Your_Bot)






