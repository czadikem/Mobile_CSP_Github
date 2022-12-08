# Client Configuration

Program-Y ships with a number of ways to run the bot. Many of these clients have their own specific configuration settings
to control how they operate. 

However there are some config options which are generic to all clients as follows

The name of the configuration setting is always the name of the client, in this example the client is 'console' and its what
the config loaded looks for when loading the Console Configuration option.

```yaml
console:
  bot:  bot
  bot_selector: programy.clients.client.DefaultBotSelector
  renderer: programy.clients.render.text.TextRenderer
  scheduler:
    name: Scheduler1
    debug_level: 0
    add_listeners: True
    remove_all_jobs: True
```

The config section is make up of the following items

* **[Bots](./Config_Client_Bots)** - How to configure one of more bots to load into the client
* **[Renderer](./Config_Client_Renderer)** - The type of rendered to display the output to the user. For console this is basic text renderer 
* **[Storage](./Config_Client_Storage)** - The configuration for controlling the storage options of the boc
* **[Scheduler](./Config_Client_Scheduler)** - If you are using asynchronous events then you configured the scheduler here
* **[Email](./Config_Client_Email)** - A new addition post v3.6 which provides the abiity to send emails from your client
    
Some clients then have additional configuration items specific to them, these are:

* **[Alexa](./Config_Client_Alexa)**
* **[Console](./Config_Client_Console)**
* **[Google](./Config_Client_Google)**
* **[Kik](./Config_Client_Kik)**
* **[Line](./Config_Client_Line)**
* **[Slack](./Config_Client_Slack)**
* **[Socket](./Config_Client_Socket)**
* **[Telegram](./Config_Client_Telegram)**
* **[Twitter](./Config_Client_Twitter)**
* **[Viber](./Config_Client_Viber)**
* **[Web Chat](./Config_Client_WebChat)**
* **[XMPP](./Config_Client_XMPP)**

