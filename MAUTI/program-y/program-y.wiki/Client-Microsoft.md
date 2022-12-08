# Microsoft Client

## Creating a Bot on Azure

Log onto your Azure Platform https://portal.azure.com/. If you don't already have an userid/password, then you
will need to create a Microsoft account first. Onc eyou have done this log onto the Azure platform

[[images/microsoft/microsoft1.png]]

We first need to create a Resource Group to pay for our bot user of Azure. Click on the 'Resource Groups'
link on the left hand side menu bar

[[images/microsoft/microsoft2.png]]

Click the '+ Add' link

[[images/microsoft/microsoft3.png]]

Select the Subscription type, in this instance we are going with 'Pay-As-You-Go'. 

Next give your resource group a name, 

Select your region, we choose 'UK West'

Finally click 'Review + Create' button at the bottom of the screen
  
[[images/microsoft/microsoft4.png]]

Review the details, and then click 'Create', it will take a few minutes to create, 
but eventually it will appear in the Resources Group panel

[[images/microsoft/microsoft5.png]]

We can now create out Bot interface, click on 'All Resources'

[[images/microsoft/microsoft6.png]]

Click 'Create resources'

[[images/microsoft/microsoft7.png]]

Then search for 'Bot Channels Registration' in the search field, which will automatically take you to the follow

[[images/microsoft/microsoft8.png]]

Click 'Create' at the bottom to create you bot

[[images/microsoft/microsoft9.png]]

Edit the settings, giving your bot a name, set the subscription, typically based on the resource you create earlier.
Set the 'Location', and the 'Application Insights Location'

Next enter the HTTPS URL that you bot will be exposed on. For testing purposes we use ngrok, but for
production we can edit this later to the URL of your production server

Next click 'Auto create App ID and password'. We will use these values later when we configure our client.

Finally click 'Create', and wait while the bot is created for you

When deployment is complete click 'All resources' in the left hand side menu

[[images/microsoft/microsoft10.png]]

Then click the name of you bot

[[images/microsoft/microsoft11.png]]

Now lets get out APP ID and Password to configure our client. First click on 'Settings'

[[images/microsoft/microsoft12.png]]

Next to Microsoft App ID, click the 'Manage'. You will probably be asked to log into with your credentials again

On the next screen click 'Generate New Password'

A new password will be generated and shown to you, copy this to the clipboard and we'll use it shortly

Open licenses.keys and paste in App ID from the screen and the password we just created

MICROSOFT_APP_ID = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
MICROSOFT_APP_PASSWORD = XXXXXXXXXXXXXXXXXXXXXXXXXX

We are now ready to test our Microsoft Bot Client, you can test you bot via the built in Web Client

Click the 'Test in Web Chat' link which will bring up a web chat client. 


## Client Execution
Y-Bot ships with a unix shell script for running an Microsoft client. It can be found in the scripts/xnix folder 
of your y_bot installation and is called 'y-bot-microsoft.sh'.

Alternatively you can use the following command line to run it

```bash
python3 -m programy.clients.restful.asyncio.microsoft.client --config ../../config/xnix/config.microsoft.yaml --cformat yaml --logging ../../config/xnix/logging.yaml
```

Running either of these and you should see the following output

```bash
No bot root argument set, defaulting to [../../config/xnix]
Found a total of 1 errors in your grammars, check your errors store
Found a total of 6 duplicates in your grammars, check your duplicates store
Microsoft Client loaded
Started http server
```

You can now interact with you bot

[[images/microsoft/microsoft13.png]]

## Client Configuration
Like all clients the Programy Alexa client requires some configuration which is held in the config.yaml file for the client.
The available configuration options are as follows

```yaml
    microsoft:
      description: Program-Y Microsoft Client
      host: 127.0.0.1
      port: 9000
```

