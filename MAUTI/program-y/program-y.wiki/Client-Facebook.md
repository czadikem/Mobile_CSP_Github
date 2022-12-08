
## Create Facebook Page
First, This tutorial takes you through setting up a Facebook page that can respond to questions, the answers will be provided by Program-y.
The facebook page is just a usual facebook page, head over to https://www.facebook.com/pages/create. 

[[images/facebook/facebook1.png]]

Choose either “Cause and Community”, or "Buisness or Brand". It does matter for this demo, but worth readinf up about the 
differences before you do type for production

[[images/facebook/facebook2.png]]

Give you page a name and optional Category and then click 'Continue'. 

[[images/facebook/facebook3.png]]

You can add a profile picture, alternatively click 'Skip' a couple of times and move on and you will be taken to the Facebook 
page for your Community or Business depending upon what you chose above.

## Facebook Developer Account
Before creating a facebook app, you need a facebook developer account. With my own facebook account, 
Login to https://developers.facebook.com/ and then click “Get Started”. 
It will turn the facebook account to be a developer account.

## Create a Facebook App
After successful conversion, login to developers.facebook.com, and click “Get Started” to complete the setup. 
Then click “Add a New App” to add our chatbot as an app. 

[[images/facebook/facebook4.png]]

Click on 'My Apps' and then 'Add New App' in the drop down

[[images/facebook/facebook5.png]]

You will then be asked to provide some information about your app

[[images/facebook/facebook6.png]]

Give you app a Display Name and Contact email address and then click 'Create App ID'

[[images/facebook/facebook7.png]]

You can skip this section by clicking 'Skip' in the bottom right corner

[[images/facebook/facebook8.png]]

On the left hand side click the + sign next to Products

[[images/facebook/facebook9.png]]

Find the Messenger Product and click 'Setup', scoll down to Access Tokens and click 'Edit Permissions', at the next 
box select to login as yourself and then at the next box, select the name of the page you just created, click 'Next'
then 'Done' and finally 'OK'

[[images/facebook/facebook10.png]]

Click the Dropdown under the title 'Page' and again select the page you just created. This will generate a Page Access
Token. 

You need to copy this value and paste it into license.keys in your bot until the following value

```ini
FACEBOOK_ACCESS_TOKEN = XXXX
```

Next scroll down to 'Webhooks' and click 'Subscribe to Events'

[[images/facebook/facebook11.png]]

Select to subscribe to all events. 

Then in the 'Verify Token' enter the value you have in the 'FACEBOOK_VERIFY_TOKEN' value in license.keys

```ini
FACEBOOK_VERIFY_TOKEN = YYYY
```

Then in the 'Callback URL' enter the URL that your facebook client is running on. In this example we are using ngrok.

Make sure you client is running using the command below and then click 'Verify and Save'. This will actually call your
client passing the information in 'FACEBOOK_VERIFY_TOKEN'. If you client needs to return 200 HTTP code. This is already 
setup in the Program-y Facebook client for you

You are now ready to chat to your bot

## REST Client
The Facebook client is primarily a REST end point that the Facebook platform calls every time some one sends your Facebook bot a message. Therefore the setup and configuration is almost identical to how your set up a REST client. The following configuration should be added to the config.yaml file of your bot
```yaml
facebook:
  description: Program-Y Facebook Client
  host: 127.0.0.1
  port: 5000
  debug: false
  api: /api/facebook/v1.0.ask
```
This will then expose the bot on port 5000. If your server is public then it will be available on https://<IP OF SERVER>:5000, or if you intend to use ngrok to expose your server, you can use the port number as follows
```bash
ngrok http 5000
```
Remember to cut and paste the ngrok https address back into the Facebook configuration of your bot before you try and use it

In addition the configuration, you need to add to entries to license.keys. These securely provide the Access Token and Verify Token you previously set during the Facebook creation process. These entries are as follows
```ini
FACEBOOK_ACCESS_TOKEN = XXXX
FACEBOOK_VERIFY_TOKEN = YYYY
```

To run the Facebook client, you can use the shell script in Y-Bot scripts folder
```bash
./y-bot-facebook.sh
```

Or you can use the command line 
```bash
python3 -m programy.clients.rest.flask.facebook.client --config <PATH TO CONFIG> --cformat yaml --logging <PATH TO LOGGING>
```

Either way you will see something like this

```bash
Initiating Facebook Client...
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 1 errors in your grammars, check your errors store
Found a total of 6 duplicates in your grammars, check your duplicates store
Facebook Client loaded
facebook Client running on 127.0.0.1:5000
Healthcheck now running as part of REST Service...
facebook Client running in http mode, careful now !
 * Serving Flask app "client" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
```

Head over to your messenger client and start chatting away

## HTTPS
Facebook requires your server to run using HTTPS on a server with a DNS entry.
More info to follow on this in a future release

