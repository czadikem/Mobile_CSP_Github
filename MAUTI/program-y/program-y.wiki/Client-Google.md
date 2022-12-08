# Google DialogFlow

Like the Alexa client, the DialogFlow client uses the ability for your intents to call our to a a REST endpoint in which
all of the logic for calling Program-Y and returning a result is held

## Sign In 
first we need to sign in with a Googel ID. If you have one already then create a new one and use the credentials to login

[[images/google/Step1.png]]

Once you log in you will be presented with the DialogFlow Console. Click Create Agent

## Create An Agent

[[images/google/Step2.png]]

Give you bot a name, and ensure the language and timezone is what you need them to be, and then click Create

## Create Intents
Once the agent is created you will be presented with the following screen

[[images/google/Step3.png]]

First delete the 2 intents Default Fallback and Default Welcome by clicking on the trash can on the right of their name.

Now we are going to create the intents we need for integration with Program-y. We need 4 intents Launch, Query, Help and Quit.

### Launch Intent
Click Create Intent in the top right corner, the following screen will appear

[[images/google/Step4.png]]

Click on the down arrow next to Events and select Google Assistant Welcome

[[images/google/Step5.png]]

Click the down arrow next to Training Phrases, and enter phrases that a user would use to start your skill.
In this instance we have chosen to use
* launch boracle
* start boracle

[[images/google/Step6.png]]

Finally scroll down to the bottom and click the down arrow next to Fulfillment, then click Enable Fulfillment, 
then click Enable Webhook call for this intent

[[images/google/Step7.png]]

We are done with this intent so we can click Save, to save the intent

### Quit Intent
Carry out the same steps as above, this time calling the intent Quit Intent, but this time do not select an Event
and use the following phrases
* stop
* exit
* leave
* quit

### Help Intent
Again carry out the same steps as above, this time calling the intent Help Intent, again do not select an Event
and use the following phrases
* help
* what can I ask you
* help me
* what can you do

### Query Intent
Finally carry out the same processes, but this time call the intent Query Intent, do not select an Event, but this time
we have one training phrase 
* query

This time however we add a parameter as follows
[[images/google/Step8.png]]

## Connect Endpoint
Finally we need to set the endpoint that DialogFlow will call each time it identifies an intent.

On the left hand side menu bar, click Fulfillment link. Click Enabled and then enter the URL that should be called 
which Program-Y is running on as a Google client

[[images/google/Step9.png]]

In the example above I use ngrok to create a temporary URL for development and testing purpose. 
For more details see [Using ngrok](./Using-ngrok). The API endpoint is always '/api/alexa/v1.0/ask' So combine this
with the ngrok URL, gives you 'https://87e27269.ngrok.io/api/alexa/v1.0/ask'. To save this click 'Save Endpoints' and 
you are ready to get your client up and running

Scroll down to the bottom and click Save

## Client Configuration
Like all clients the Programy Google client requires some configuration which is held in the config.yaml file for the client.
The available configuration options are as follows
```yaml
        google:
          host: 127.0.0.1
          port: 5000
          debug: false
          launch_text: Hello and welcome
          launch_srai: GOOGLE_LAUNCH
          quit_text: Good bye matey
          quit_srai: GOOGLE_STOP
          help_text: Ask me anything, I know loads
          help_srai: GOOGLE_HELP
          error_text: Oopsie there has been an error
          error_srai: GOOGLE_ERROR
```

## Client Execution
Y-Bot ships with a unix shell script for running an Google client. It can be found in the scripts/xnix folder 
of your y_bot installation and is called 'y-bot-google.sh'.

Alternatively you can use the following command line to run it

```bash
python3 -m programy.clients.restful.flask.google.client --config ../../config/xnix/config.google.yaml --cformat yaml --logging ../../config/xnix/logging.yaml
```

## Additional Client Integration
By Integration with Google Dialog Flow you can create then use the provided capabilities to create 
clients to a wide range of other services, including 

* Google Assistant
* Web Client
* Facebook Messenger
* Dialogflow Phone Gateway 
* Slack
* Viber
* Twitter
* Twillio
* Skype
* Telegram
* Kik
* LINE
* Cisco Spark
* Amazon Alexa
* Microsoft Cortana

Integration with the clients above, and as an alternative to the native clients provided with Program-Y. 
Not however that Google DialgowFlow has both free and paid for services. 