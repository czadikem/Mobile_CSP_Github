# Twitter Client

## Overview
The current Twitter client uses a polling mechanism as provided by the Python package tweepy, 
it is envisaged in the future that this will have streaming added to it. 
This is in the backlog and is likely to make it into a 1.x release

## Create a Twitter Chatbot
Once you have created a Twitter account and can sucessfully tweet from it, head over to the 
Twitter Application Management Dashboard at https://developer.twitter.com/en/apps

### Create a Developer Account
Click 'Create an app'. If you have not already applied for a Developer Account, you will be prompted
to apply for one now, with the following popup

[[images/twitter/twitter1.png]]

Click Apply

[[images/twitter/twitter2.png]]

Select the Twitter account you want to associate your developer account with, and then click 'Continue'

[[images/twitter/twitter3.png]]

Select the account type and the name of you Twitter bot, then again click 'Continue'

[[images/twitter/twitter4.png]]

Select the type of bot and also answer the additional questions to help with expiditing your 
application, again click 'Continue'

[[images/twitter/twitter5.png]]

Read the terms and conditions ( as if ) and click 'Accept' to continue and then 'Submit Application'
at the bottom of the screen

[[images/twitter/twitter6.png]]

Final complete email validation

### Create a Twitter App

#### Permissions
These keys and secrets come from registering as a developer on Twitter, creating an app and then following the instructions to create Consumer And Access tokens and secrets. Please note that a Bot needs specific permissions, so please make sure that you set the access to 'Read, Write and Access direct messages'

```
What type of access does your application need?
Read only
Read and Write << default
Read, Write and Access direct messages << needed!
```


## Running the Client
The client is derived from the following Python class
```python
    programy.clients.twitter.TwitterBotClient
```

To run the Facebook client, you can use the shell script in Y-Bot scripts folder
```bash
./y-bot-twitter.sh
```

Or you can use the command line 
```bash
python3 -m programy.clients.polling.twitter.client --config <PATH TO CONFIG> --cformat yaml --logging <PATH TO LOGGING>
```

Eithernway nyou should see the following output on your console
```bash
Loading Twitter client, please wait. See log output for progres...
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 1 errors in your grammars, check your errors store
Found a total of 6 duplicates in your grammars, check your duplicates store
Twitter Bot connected and running...
```

## Configuration Settings
The configuration settings can be found in the wiki page 
[Twitter Configuration](./Config-Client-Twitter).

## License Key Settings
In addition to configuration settings, there are a number of Twitter-specific license keys. These are stored in license.keys in the /config file. However, for security reasons, this file is excluded from Github and you'll need to create your own with the following settings

```ini
    TWITTER_USERNAME = programybot
    TWITTER_CONSUMER_KEY = xxxxxxxxxxxxxxxxxxxxxxxxxxxx
    TWITTER_CONSUMER_SECRET = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    TWITTER_ACCESS_TOKEN = xxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    TWITTER_ACCESS_TOKEN_SECRET = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

