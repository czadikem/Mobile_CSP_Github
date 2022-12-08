# Slack Client

[Slack](http://www.slack.com) is a cloud-based set of proprietary team collaboration tools and services, founded by Stewart Butterfield. Slack began as an internal tool used by their company, Tiny Speck, in the development of Glitch, a now-defunct online game. The name is an acronym for "Searchable Log of All Conversation and Knowledge"

For an introduction on how to configure your Slack bot for integration with Program-Y read the [Slack Documentation](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)

##Creating a Slack Bot
Login into slack and then head over to the Slack Apps page at https://api.slack.com/apps which should look something like the following screen

[[images/slack/slack1.png]]

Click ‘Create an App’

The following pop up will appear

[[images/slack/slack2.png]]

Give your app a name and select which workspace to associate it.

[[images/slack/slack3.png]]

Click ‘Create App’ and wait for the app the be created. The web site will then automatically switch you apps Basic Information page, which should look something like this

[[images/slack/slack4.png]]

Next we need to create a Bot User. Click on the ‘Bots’ panel, and the screen will look like this following

[[images/slack/slack5.png]]

Click ‘Add Bot User’ to see the following screen

[[images/slack/slack6.png]]

You can pretty much leave the info as it is, and click ‘Add Bot User’, wait for the user to be created then click ‘Save Changes’

Next, on the left hand side menu click ’Event Subscriptions’ 

[[images/slack/slack7.png]]

Then toggle ‘Enable Events’ on On, The screen should change to the following

[[images/slack/slack8.png]]

Finally click on ‘OAuth & Permissions’ on the left hand side menu

[[images/slack/slack9.png]]

And click ‘Install App into Workspace’

[[images/slack/slack10.png]]

Click ‘Authorize’, and it will return you to the following page with some new tokens for you bot

[[images/slack/slack11.png]]

Click the ‘Copy’ button to copy the token under the title ‘Bot User OAuth Access Token’. You copy this token into your licenses.keys file

You are now ready to talk to your bot

# Running Slack Client

To run the Facebook client, you can use the shell script in Y-Bot scripts folder
```bash
./y-bot-slack.sh
```

Or you can use the command line 
```bash
python3 -m programy.clients.polling.slack.client --config <PATH TO CONFIG> --cformat yaml --logging <PATH TO LOGGING>
``

Either way you should see the following output

```bash
Loading Slack client, please wait. See log output for progress...
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 1 errors in your grammars, check your errors store
Found a total of 6 duplicates in your grammars, check your duplicates store
Slack Bot connected and running...
```

Head over to your favourite client, and you should see you app in the list of apps on the left hand side

[[images/slack/slack12.png]]

You interact my sending a direct message using the @<bot name> and then your question

[[images/slack/slack13.png]]

# Configuration

The client only requires a single setting in config.yaml. The polling interval for which to check for news messages. This is set as follows
```yaml
slack:
  polling_interval: 1
```


