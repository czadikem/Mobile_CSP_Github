# Amazon Alexa

First you....

[[images/alexa/Step1.png]]

Then you....

[[images/alexa/Step2.png]]
Then you....

[[images/alexa/Step3.png]]
Then you....

[[images/alexa/Step4.png]]
Then you....

[[images/alexa/Step4.1.png]]
Then you....

[[images/alexa/Step4.2.png]]
Then you....

[[images/alexa/Step4.3.png]]

Finally you....

## Client Execution
Y-Bot ships with a unix shell script for running an Alexa client. It can be found in the scripts/xnix folder 
of your y_bot installation and is called 'y-bot-alexa.sh'.

Alternatively you can use the following command line to run it

```bash
python3 -m programy.clients.restful.flask.aslexa.client --config ../../config/xnix/config.alexa.yaml --cformat yaml --logging ../../config/xnix/logging.yaml
```

Running either of these and you should see the following output

```bash
Initiating Alexa Client...
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 1 errors in your grammars, check your errors store
Found a total of 6 duplicates in your grammars, check your duplicates store
Alexa Client loaded
alexa Client running on 127.0.0.1:5001
alexa Client running in http mode, careful now !
 * Serving Flask app "client" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
```

## Client Configuration
Like all clients the Programy Alexa client requires some configuration which is held in the config.yaml file for the client.
The available configuration options are as follows
```yaml
alexa:
  description: Program-Y Alexa Client
  host: 127.0.0.1
  port: 5001
  debug: False
  api: /api/alexa/v1.0/ask
  launch_text: Hello and welcome
  launch_srai: ALEXA_LAUNCH
  session_end_text:  Good bye matey
  session_end_srai: ALEXA_END
  error_text: Oopsie there has been an error
  error_srai: ALEXA_ERROR
  leave_intent: LeaveIntent
```