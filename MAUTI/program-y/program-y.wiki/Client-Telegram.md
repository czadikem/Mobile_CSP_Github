#Telegram Bot

The Telegram Client provides a way for a [Telegram Messenger](https://telegram.org/) to interact with a bot client. 

To begin, you'll need an Access Token. Read and follow the [Introduction to the API](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API) on the Telegram Developer website. When you are ready you then need to create an Access Token, which do by talking to the @BotFather via Telegram Messenger and follow a few simple steps.

You create new bots by directly interacting with the Telegram BotFather via your favourite Telegram client.

Login to Telegram Client

[[images/telegram/telegram1.png]]

Start a conversation with BotFather by searching for ‘botfather’ in the search box, click on @BotFather and a new conversation will start

[[images/telegram/telegram2.png]]

We create a new bot with the ‘/newbot’ command

```bash
/newbot
```
Give it a name

Give it a username

Telegram will now create a token to access HTTP API is given

[[images/telegram/telegram4.png]]

Take the token (blacked out for security purposes) and add it to licenses.keys

```text
TELEGRAM_TOKEN = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

You are now ready to run your Telegram client

```bash
Run ./y-bot-telegram.sh
Loading Telegram client, please wait. See log output for progress...
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 1 errors in your grammars, check your errors store
Found a total of 6 duplicates in your grammars, check your duplicates store
Telegram Bot connected and running...
```

Once you can can see its runnings, you can go to Telegram Client and search for the bot name you used above

[[images/telegram/telegram5.png]]

Click on your bot and then on ‘start’ and you can then start talking to you bot

[[images/telegram/telegram6.png]]

## Configuration
Telegram client needs little configuration apart from which message to return if you send it an unknown command. 
This can be configured by adding the following client configuration to config.yaml.

```yaml
telegram:
  unknown_command: Sorry, that is not a command I have been taught yet!
```

## Running Program-y Telegram Client
To run the Telegram client, you can use the shell script in Y-Bot scripts folder
```bash
./y-bot-telegram.sh
```

Or you can use the command line 
```bash
python3 -m programy.clients.polling.telegram.client --config <PATH TO CONFIG> --cformat yaml --logging <PATH TO LOGGING>
```

