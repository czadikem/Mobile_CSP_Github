
# REST Service
The first service to get up and running is the REST service, this loads the core Y-Bot Grammar and will also be
called by all other clients in our multi-client configuration.
We can first test it works locally by using the shell script `servusai-rest.cmdd`

```bash
```
Here we can see that it's running in HTTP mode, on port 8989. This is fine as we are not exposing the REST service at this time to the outside world. Instead, it will be called by all other services so HTTP is fine.

Install as a Windows Service....

## Console Console
Now we have a REST service running against a full Y-Bot grammar, lets tests it's working. Servusai ships with a fully configured Console client that connects to the REST Client. 

```bash
$ cd ..\console
$ console.cmd
Loading, please wait...
No bot root argument set, defaulting to [.]
None, App: v1.0.0 Grammar v1.0.0, initiated March 14, 2017
Hi, how can I help you today?
>>> hello
Hiya!
>>> what are you
I'm a full-time virtual assistant.
>>> 
```
This shows that its connected, working and the REST client is responding correctly. Lets configure all of the other clients

# Web Chat Client
First we check its working locally using the script `web.sh`
```bash
$ cd ..\web
$ web.cmd
Loading, please wait...
No bot root argument set, defaulting to [.]
Initiating Webchat Client...
WebChat Client running on 0.0.0.0:8080
Webchat Client running in http mode, careful now !
```
Again, the above output shows that the webchat client is running and waiting for us to connect on https://servus.com

## Telegram Client
Next client is the Telegram client, so head over that folder and lets check its all working by running the local script.
```bash
$ cd ..\telegram
$ telegram.cmd
Loading Telegram client, please wait. See log output for progress...
No bot root argument set, defaulting to [.]
Telegram client running....
```
Install as a Windows Service....

As this point we should see that the server started and is running. Head over to your favourite Telegram client and you can start chatting with Servus AI at @servusai

## Google Talk Client (XMPP Client)
Another good client ot have running is the XMPP client. In this instance, it is configured to run as Google Talk Client.
$ cd ..\xmpp
$ xmpp.cmd
Loading XMPP client, please wait. See log output for progress...
No bot root argument set, defaulting to [.]
XMPP client running [programy@gmail.com]
```
Once we have proved it is all working, we can install it as a service like all the other ones we have done already.

Install as a Windows Service....

Again, the last command tells us if the service is up and running.

## Twitter Client
So the pattern starts to become familiar now

```bash
$ cd ..\twitter
$ twitter.cmd
Loading Twitter client, please wait. See log output for progress...
No bot root argument set, defaulting to [.]
Twitter client running as [programybot]...
```
Now we have confirmed it will run on the server we can install it as a service

Install as a Windows Service....

## Socket Client
Again lets head over to the socket client and test it locally first
```bash
$ cd ..\socket
$ socket.cmd
Loading, please wait...
No bot root argument set, defaulting to [.]
TCP Socket server now listening on 127.0.0.1:9999
```
So that confirms its running, now we can install it as a service

Install as a Windows Service....

And hey presto, we should see that the service is running.

Note that if you keep getting the same tweets responded to, then its likely the storage directory defined in config.yaml is either defined incorrectly or missing. 

## Facebook Client
Facebook is probably one of the more complicated clients to get up and running due to the need to define an SSL url that is a fully defined DNS url

I run nginx as my webserver in front of all the web based clients including the Facebook webhook URL. You will need to configure you server appropriately to expose the port for Facebook client and also ensure its running HTTPS, otherwise Facebook won't like it. So once you have done that lets run the local client first

```bash
$ cd ..\facebook
$ .\facebook.cmd
No bot root argument set, defaulting to [.]
Facebook Client loaded
Facebook Client running on 127.0.0.1:5000
Facebook Client running in http mode, careful now !
```
Again we can see that its running, so we can go ahead and install it as a service

Install as a Windows Service....

## Slack Client
So the pattern starts to become familiar now

```bash
$ cd ..\slack
$ slack.cmd
Loading Slack client, please wait. See log output for progress...
No bot root argument set, defaulting to [.]
Starter Bot connected and running!
```
Now we have confirmed it will run on the server we can install it as a service

Install as a Windows Service....

## Twilio SMS Client
Again the pattern continues to become even more familiar now

```bash
$ cd ..\twilio
$ twilio.sh
No bot root argument set, defaulting to [.]
Twilio Client loaded
Twilio Client running on 127.0.0.1:5000, receiving on +44777777777
Twilio Client running in http mode, careful now !
```
Now we have confirmed it will run on the server we can install it as a service

Install as a Windows Service....

# Working with your Bot
You are now ready to start working your with bot. To do this, jump to the next page [You and Your Bot](./You_And_Your_Bot)