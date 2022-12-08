# Twilio SMS Client

Twilio, among many messaging options provides cost-effective worldwide SMS messaging platform.  For a description on how to register your bot with Twilio and obtain the necessary security tokens read the [Twilio Documentation](https://www.twilio.com/docs/quickstart/python/sms#sign-up-for-twilio-and-get-a-phone-number)

If you dont have a Twilio account head over to https://www.twilio.com and sign up for an Account

The simpliest way to integrate with a Program-y Chatbot is by buying a telephone number and hooking a webhook to the number.
Everytime the number receives an SMS your endpoint is called and you can then return a bot response.

Program-y ships with a Twilio REST server that you can use in this manner

From the console screen, click the icon on the left hand side for 'All Products & Services'

[[images/twilio/twilio1.png]]

From the slide out menu select 'Telephone Numbers'

[[images/twilio/twilio2.png]]

If you have not already bought a telephone number click the red + sign to 'Buy a New Number'

[[images/twilio/twilio3.png]]

Once you have done that, click on the number you have purchased to go to the following screen

[[images/twilio/twilio4.png]]

Scroll down to the bottom of the screen, and in the messaging section enter the URL of the webhook
that you expose via your Twilio Client

[[images/twilio/twilio5.png]]

Click 'Save' and you are ready for testing

## Running the Client

To run the Facebook client, you can use the shell script in Y-Bot scripts folder
```bash
./y-bot-twilio.sh
```

Or you can use the command line 
```bash
python3 -m programy.clients.rest.flask.twilio.client --config <PATH TO CONFIG> --cformat yaml --logging <PATH TO LOGGING>
```

## Configuration

The Twilio client operates as a RESTfl webhook server that Twilio calls whenever it receives a message. We configure these settings as follows in config.yaml
```yaml
twilio:
  host: 127.0.0.1
  port: 5000
  debug: false
```

## License Keys

Twilio developer portal provides the Account SID for your bot and the Authentication token. 
You will also need to purchase a telephone number with SMS rights, and this is also included 
in license.keys as follows

The Account SID and Auth Token are found in the following screen in the Console

[[images/twilio/twilio6.png]]

And go into the following sections along with the number you purchased in license.keys file

```ini
TWILIO_ACCOUNT_SID = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
TWILIO_AUTH_TOKEN = YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
TWILIO_FROM_NUMBER = +441315105590
```

