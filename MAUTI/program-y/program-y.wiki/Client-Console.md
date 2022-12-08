The console client is found in the module
```python
programy.clients.console.ConsoleBotClient
```
To run the Console client, you can use the shell script in Y-Bot scripts folder
For OSX & Linux
```bash
cd y-bot/scripts/xnix
./y-bot.sh
```

For Windows
```bash
cd y-bot/scripts/windows
y-bot.cmd
```

Alternatively you can use the command line calling Python directly as follows
```bash
python3 -m programy.clients.events.console.client --config <PATH TO CONFIG> --cformat yaml --logging <PATH TO LOGGING>
```

Any of these methods will display something similar to the following
```console
Loading, please wait...
No bot root argument set, defaulting to [.]
Y-Bot version 0.0.1, initiated March 14, 2017
Hi, how can I help you today?
>>> Hello
Greetings!
>>> 
```
You can now interact with the client by typing in questions at the >>> prompt

The console is configured using the option described in [Console Configuration](./Config-Client-Console)
