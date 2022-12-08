# Installation on Windows Using Pip in a Virtual Environment

Before you install Programy on Ubuntu you need to check that you have the pre-requisites installed, 
named Python 3.x and Pip. Installation instructions for Windows can be found in [Windows Prerequisites](Install_Windows_PreReqs)

## Installation via Pip

First lets create a directory to run our bot in 

```cmd
mkdir mybots
cd mybots
```

Now we are going to using Python Virtual Environment to contain the changes Program-y makes

```cmd
C:\Users\keiff\mybots>python -m venv programy
C:\Users\keiff\mybots>cd programy
C:\Users\keiff\mybots\programy>
```

Activate the virtual environment and then create a directory to hold our programy installations

```cmd
C:\Users\keiff\mybots\programy>Scripts\activate.bat
(programy) C:\Users\keiff\mybots\programy>
mkdir ybot
cd ybot
(programy) C:\Users\keiff\mybots\programy\ybot>
```

Now lets install programy

```cmd
pip install --no-cache-dir programy
```

Installation will now start and you’ll see something like the following
```cmd
Collecting programy
  Downloading https://files.pythonhosted.org/packages/1e/3d/1121464836275c392f87920650150450151606f794593f731cc832b2d70f/programy-3.5.1.tar.gz (457kB)
    100% |████████████████████████████████| 460kB 4.6MB/s
Collecting python-dateutil==2.7.3 (from programy)
  Downloading https://files.pythonhosted.org/packages/cf/f5/af2b09c957ace60dcfac112b669c45c8c97e32f94aa8b56da4c6d1682825/python_dateutil-2.7.3-py2.py3-none-any.whl (211kB)
    100% |████████████████████████████████| 215kB 4.5MB/s
Collecting beautifulsoup4==4.6.3 (from programy)
  Downloading https://files.pythonhosted.org/packages/21/0a/47fdf541c97fd9b6a610cb5fd518175308a7cc60569962e776ac52420387/beautifulsoup4-4.6.3-py3-none-any.whl (90kB)
    100% |████████████████████████████████| 92kB 5.6MB/s
Collecting lxml==4.2.5 (from programy)
  Downloading https://files.pythonhosted.org/packages/9b/33/31b79b7acfdb3fa8cdf4cb34ed282f0dc359f34a150b5abc81b591b27abd/lxml-4.2.5-cp36-cp36m-win32.whl (3.2MB)
    100% |████████████████████████████████| 3.2MB 7.9MB/s
Collecting PyYAML==4.2b4 (from programy)
  Downloading https://files.pythonhosted.org/packages/a8/c6/a8d1555e795dbd0375c3c93b576ca13bbf139db51ea604afa19a2c35fc03/PyYAML-4.2b4.tar.gz (262kB)
    100% |████████████████████████████████| 266kB 7.1MB/s
```

Eventually all the packages used by programy will download and you’ll see the installer running the necessary configuration scripts. You should see something similar to the following

```cmd
Installing collected packages: six, python-dateutil, beautifulsoup4, lxml, PyYAML, idna, chardet, certifi, urllib3, requests, itsdangerous, MarkupSafe, Jinja2, Werkzeug, click, Flask, python-engineio, python-socketio, Flask-SocketIO, PySocks, oauthlib, requests-oauthlib, tweepy, sleekxmpp, future, pycparser, cffi, asn1crypto, cryptography, python-telegram-bot, requests-toolbelt, pymessenger, pytz, PyJWT, twilio, websocket-client, slackclient, viberbot, line-bot-sdk, kik, wikipedia, MetOffer, tzlocal, APScheduler, emoji, autocorrect, redis, pymongo, SQLAlchemy, PyMySQL, wget, singledispatch, nltk, textblob, programy
  Running setup.py install for PyYAML ... done
  Running setup.py install for PySocks ... done
  Running setup.py install for sleekxmpp ... done
  Running setup.py install for future ... done
  Running setup.py install for pycparser ... done
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
Successfully installed APScheduler-3.5.3 Flask-1.0.2 Flask-SocketIO-3.0.2 Jinja2-2.10 MarkupSafe-1.1.0 MetOffer-1.3.2 PyJWT-1.7.1 PyMySQL-0.9.2 PySocks-1.6.8 PyYAML-4.2b4 SQLAlchemy-1.2.12 Werkzeug-0.14.1 asn1crypto-0.24.0 autocorrect-0.3.0 beautifulsoup4-4.6.3 certifi-2018.11.29 cffi-1.11.5 chardet-3.0.4 click-7.0 cryptography-2.5 emoji-0.5.1 future-0.17.1 idna-2.7 itsdangerous-1.1.0 kik-1.5.0 line-bot-sdk-1.8.0 lxml-4.2.5 nltk-3.4 oauthlib-3.0.1 programy-3.5.1 pycparser-2.19 pymessenger-0.0.7.0 pymongo-3.7.1 python-dateutil-2.7.3 python-engineio-3.3.2 python-socketio-3.1.2 python-telegram-bot-11.1.0 pytz-2018.9 redis-2.10.6 requests-2.20.0 requests-oauthlib-1.2.0 requests-toolbelt-0.9.1 singledispatch-3.4.0.3 six-1.12.0 slackclient-1.3.0 sleekxmpp-1.3.3 textblob-0.15.2 tweepy-3.6.0 twilio-6.18.1 tzlocal-1.5.1 urllib3-1.24.1 viberbot-1.0.11 websocket-client-0.54.0 wget-3.2 wikipedia-1.4.0
```

Programy is now downloaded and installed. A quick check is if the admin tool is up and running

```cmd
(programy) C:\Users\keiff\mybots\programy\ybot>python -m programy.admin.tool
Available commands are:

        help
        list
        download <bot-name>
        install <component>
```
Now lets install additional components, in this instance only textblob are required. You should see something similar to the following


```cmd
(programy) C:\Users\keiff\mybots\programy\ybot\>python -m programy.admin.tool install textblob
Installing additional components for textblob
[nltk_data] Downloading package punkt to
[nltk_data]     C:\Users\keiff\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping tokenizers\punkt.zip.
[nltk_data] Downloading package brown to
[nltk_data]     C:\Users\keiff\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping corpora\brown.zip.
[nltk_data] Downloading package punkt to
[nltk_data]     C:\Users\keiff\AppData\Roaming\nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\keiff\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping corpora\wordnet.zip.
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     C:\Users\keiff\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping taggers\averaged_perceptron_tagger.zip.
[nltk_data] Downloading package conll2000 to
[nltk_data]     C:\Users\keiff\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping corpora\conll2000.zip.
[nltk_data] Downloading package movie_reviews to
[nltk_data]     C:\Users\keiff\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping corpora\movie_reviews.zip.
```

Now lets download y-bot

```cmd
python -m programy.admin.tool download y-bot
Removing existing file from [C:\Users\keiff\Documents\mybots\programy\ybot]
Downloading [y-bot] from [https://github.com/keiffster/y-bot/archive/master.zip]
[..................................................................................................]
Download complete

To run y-bot bot in console mode, use the following commands

        cd scripts\xnix
        y-bot.cmd```
```

### Console Client
We are not ready to run y-bot in console mode for the first time

Change to scripts/windows folder and run programy from the command file y-bot.cmd

```cmd
cd scripts\windows
(programy) C:\Users\keiff\Documents\mybots\programy\ybot\>y-bot.cmd
Loading, please wait...
C:\Users\keiff\Documents\mybots\programy\ybot\scripts\windows
No bot root argument set, defaulting to [..\..\config\windows]
Found a total of 1 errors in your grammars, check your errors store
Found a total of 6 duplicates in your grammars, check your duplicates store
Y-Bot, App: v3.0.0 Beta 1 Grammar v1.6.0, initiated March 14, 2017
Hey, whats up ?
>>> Hello
Hello!
>>> What are you
I'm artificial intelligent agent.
>>> Who created you
My botmaster's name is Keith Sterling.
>>>
```

### Rest Server
If you want to run the REST Server, use y-bot-flask-rest.cmd
```cmd
(programy) C:\Users\keiff\Documents\mybots\programy\ybot\>y-bot-flask-rest.cmd
Initiating Flask REST Service...
Loading, please wait...
No bot root argument set, defaulting to [..\..\config\windows]
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

The end point is exposed at 'http://localhost:8989/api/rest/v1.0/ask'

To call it from Powershell, use the embedded curl or wget to call the url 'http://localhost:8989/api/rest/v1.0/ask?question=hello+world&userid=1234567890'

### WebChat Server
If you want to run the Webchat Server, use y-bot-webchat.cmd
```cmd
(programy) C:\Users\keiff\Documents\mybots\programy\ybot\>y-bot-webchat.cmd
Initiating WebChat Client...
No bot root argument set, defaulting to [..\..\config\windows]
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



We we are finished we should deactivate our virtual environment. You also return to this again by using the source command as described above

```cmd
deactivate
```

# Working with your Bot
You are now ready to start working your with bot. To do this, jump to the next page [You and Your Bot](./You_And_Your_Bot)