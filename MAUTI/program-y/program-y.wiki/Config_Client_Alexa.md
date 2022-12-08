# XMPP Client Configuration

In addition to the [common configuration items](./Config_Client_Rest) available to all rest based clients, the additional configuration 
items available to a Alexa client are as follows

```yaml
alexa:
  host: 127.0.0.1
  port: 5000
  debug: false
  launch_text: Hello and welcome
  launch_srai: ALEXA_LAUNCH
  cancel_text: OK, what else can I do?
  cancel_srai: ALEXA_CANCEL
  stop_text: Good bye matey
  stop_srai: ALEXA_STOP
  help_text: Ask me anything, I know loads
  help_srai: ALEXA_HELP
  error_text: Oopsie there has been an error
  error_srai: ALEXA_ERROR
  leave_intents: AMAZON.CancelIntent, AMAZON.StopIntent
  intent_map_file: intents.map
```

* **host** - [See REST Configuration](./Config_Client_Rest)
* **port** - [See REST Configuration](./Config_Client_Rest)
* **debug** - [See REST Configuration](./Config_Client_Rest)
* **launch_text** - The text to say when the bot is launched
* **launch_srai** - The SRAI to call on launch, if missing, tries to use 'launch_text'
* **cancel_text** - The text to say when the bot is cancelled
* **cancel_srai** - The SRAI to call on cancel, if missing, tries to use 'cancel_text'
* **stop_text** - The text to say when the bot is stopped
* **stop_srai** - The SRAI to call on stop, if missing, tries to use 'stop_text'
* **help_text** - The text to say if user askes for help
* **help_srai** - The SRAI to call if the user asks for help, if missing uses, 'help_text'
* **error_text** - The text to say if there is an error
* **error_srai** - The SRAI to call on error, if missing tries to use 'error_text'
* **leave_intents** - The Amazon intents that mean the bot should leav
* **intent_map_file** - The intent map file

