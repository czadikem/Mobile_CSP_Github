# XMPP Client

XMPP allows you to run a chat bot via google chat, the config below demonstrates what settings are required to make this happen

You first need a Google account for you bot to run under. You can use an existing account, but for security reasons
I would recomend create a new account. 

Once you have the email address and password, you can add them to the license.keys file as describe below

This is where it gets a bit complex in terms of running your bot on once account but talking to it from another account.

First head over to your Hangout client, or Web site at 'https://hangouts.google.com/'

[[images/hangouts/hangouts1.png]]

Switch accounts to the account you are going to talk to your bot and click the icon near the top left corner that looks like 
2 people and enter the email address of the bot you just created

[[images/hangouts/hangouts2.png]]

When you find it, click on it in the list and the chat window will then open as such

[[images/hangouts/hangouts3.png]]

You can now start chatting with the bot via hangouts

[[images/hangouts/hangouts4.png]]

## Running the Client

To run the Facebook client, you can use the shell script in Y-Bot scripts folder
```bash
./y-bot-xmpp.sh
```

Or you can use the command line 
```bash
python3 -m programy.clients.polling.xmpp.client --config <PATH TO CONFIG> --cformat yaml --logging <PATH TO LOGGING>
```

Either way you should see the following output in the console

```bash
Loading Xmpp client, please wait. See log output for progress...
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 1 errors in your grammars, check your errors store
Found a total of 6 duplicates in your grammars, check your duplicates store
XMPP Bot connected and running...
```

## Configuration Settings

You should not need to change anything if you are using Google, if you are using another XMPP Server then you'll need to change the server and port setting, but should not need to modify the xep_XXXX options. These are really for advanced users only.

Configuration settings are decribed in the Wiki page [XMPP Configuration](./Config-Client-XMPP)

## License Key Settings

You will need a valid Google account, this needs to be set up with userid and password only. Do not use an account that has multi-factor authentication ( MFA ) enabled, otherwise it will not work

    XMPP_USERNAME = xxxxxxx@gmail.com
    XMPP_PASSWORD = XXXXXXXXXXX


    

