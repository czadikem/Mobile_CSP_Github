Once you get the experience of using the provided bots you are likely to want to 
create your own. For this purpose, we have created a template framework that you 
can use called 'Template-Y'. 

This bot keeps your aiml and code separate from program-y so that you do not get 
corrupted from GitHub pulls.

This tutorial takes you through a couple of examples to build 2 types of bot

* Console Bot
* Web Chat Bot

## Download Template-Y
We use the admin tool to download Template-Y. First create a folder and then run the tool
from inside the folder as follows

(In the example below, use 'python3' on Linux and OSX and 'python' on Windows)

```bash
$ python3 -m programy.admin.tool download template-y
Downloading [y-bot] from [https://github.com/keiffster/template-y/archive/master.zip]
[.............................................................................]
Download complete
```

If downloading on Linux or OSX, you should see the follow
```bash
To run y-bot bot in console mode, use the following commands

	cd scripts/xnix
	./template-y.sh 
```

If you have downloaded on Windows, then you should see the following
```bash
To run y-bot bot in console mode, use the following commands

	cd scripts/windows
	./template-y.cmd 
```

Running either of these and you should see something similar to the following

### Running Console Client
```bash
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
Use Ctrl-C to exit the bot

## Modifying Your Bot

Template-y directory structure is designed to allow you to start editing your onw files.

* **config**
  * **windows** - Windows specific configuration files
  * **xnix** - Linux/OSX specific configuration files
* **scripts**
  * **windows** - Windows specific batch files
  * **xnix** - Linux/OSX specific shell scripts
* **src** - Location to add your own code for extensions, services etc
* **storage** - Location for all data files, this is where you aiml files go
* **test** - Unit test files that accompany the source files in the 'src' folder



## Web Chat Client
Program-y uses the Python Flask framework for most of the Web and REST clients it provides.
Idally you should have basic experience of creating a Flask app before using the WebChat client. 
However, if all you want to do is get a WebChat client up and running to just add/modify grammars 
then these instructions should get you up and running

Template-y ships with a shell script for Linux/OSX and a batch file for windows which execute the 
WebChat client.

On Linux & OSX 
```bash
$ cd scripts
$ cd xnix
$ ./template-webchat.sh
Initiating WebChat Client...
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 0 errors in your grammars, check your errors store
Found a total of 0 duplicates in your grammars, check your duplicates store
WebChat Client running on 127.0.0.1:8090
WebChat Client running in http mode, careful now !
 * Serving Flask app "client" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
```
You can now point your browser at http://127.0.0.1:8090

On Windows use the following
```bash
$ cd scripts
$ cd windows
$ template-webchat.cmd
Initiating WebChat Client...
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 0 errors in your grammars, check your errors store
Found a total of 0 duplicates in your grammars, check your duplicates store
WebChat Client running on 127.0.0.1:8090
WebChat Client running in http mode, careful now !
 * Serving Flask app "client" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
```

Again you can now point your browser at http://127.0.0.1:8090

### Modifying the WebChat UI Code
The html, css and javascript files for webchat are location in 
'src/templatey/clients/restful/flask/webchat/static'
Here you will find the webchat.html file that displays the bot windows and the
y-bot.js javascript file, that uses JQuerty to call back to the bot

Unless you are fundamentally change the way the bot operates, you should not have to 
modify the file 'src/templatey/clients/restful/flask/webchat/client.py' Python source file

### Modifying the WebChat Bot Data
If you want to start adding/modifying grammars, maps or sets, then you can modify the files
found in the storage folders as described above.


