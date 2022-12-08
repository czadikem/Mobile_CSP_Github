# Template

Once you have got the hang of working with the embed-able bots we can start to think about creating our own bots with s full file system implementation. We start with downloading a basic bot template using the Admin Tool

Create a directory for your bot to be stored in and then run Admin Tool using the following commands

```bash
mkdir mybot
cd mybot
python3 -m programy.admin.tool download template-y
```

This will download all the necessary template files from GitHub and set up 
your environment for the tutorial work.

You can run the bot at any time by using the provided script 

```bash
cd scripts/xnix
./template-y.sh
Loading, please wait...
/Users/keith/Documents/Development/Python/Projects/AIML/template-y/scripts/xnix
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 0 errors in your grammars, check your errors store
Found a total of 0 duplicates in your grammars, check your duplicates store
None, App: vNone Grammar vNone, initiated None
Hi, how can I help you today?
>>> 
```
You can stop the bot at any time by using Ctrl-C
````bash
>>> ^CSo long, and thanks for the fish!
````

## A Quick Tour Of Template-Y
We are now ready to start creating out AIML grammars

***
[Back to Tutorial](./AIML-Tutorial) | [Back - Embedded Bots](./Tutorial-Embedded-Bots) | [Next - Getting Started](./Tutorial-Getting-Started)
