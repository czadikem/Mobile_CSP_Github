So you have followed the instructions on the Home page and now have Program-Y installed on your files system. You should then have a directory structure which looks something like this

    /bots
        /alice2
        /rosie
        /rosie_fixed
        /y-bot
    /docs
        /images
        /stylesheets
    /src
       /programy
       /src

To run program-y navigate into the y-bot folder and you'll see a number of scripts

    y-bot.sh 

This is a good starting point, it loads Program-Y as a console app and you can enter questions and get responses quite easily. If you run the script you should see something like the following

    Loading, please wait...
    No bot root argument set, defaulting to [.]
    Y-Bot version 0.0.1, initiated March 14, 2017
    Hi, how can I help you today?
    >>> 

Y-Bot is not up and running and you can have a basic conversation with him

    Loading, please wait...
    No bot root argument set, defaulting to [.]
    Y-Bot version 0.0.1, initiated March 14, 2017
    Hi, how can I help you today?
    >>> hello 
    Hello!
    >>> what time is it
    The time is 03:00 PM
    >>> what day is it
    Today is THURSDAY
    >>> 

Once you are finished just Ctrl-C and Y-Bot will terminate gracefully

    >>> ^CSo long, and thanks for the fish!

That's it, you have a fully functional ChatBot with a basic grammar. The other scripts run Y-Bot in different configurations but require more advanced set up with credentials and specific URLs which we will come to shortly. For now head over to the [AIML Tutorial](https://github.com/keiffster/program-y/wiki/AIML-Tutorial) to see how to create your own AIML grammars and extend Y-Bot or write you own sets of conversation from scratch

