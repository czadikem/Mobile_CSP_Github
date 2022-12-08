[Kik Messenging](http://www.kik.com/) ommonly called Kik, is a freeware instant messaging mobile app from the Canadian company Kik Interactive, available free of charge on iOS and Android operating systems.[1] It uses a smartphone's data plan or Wi-Fi to transmit and receive messages, photos, videos, sketches, mobile webpages, and other content after users register a username. Kik is known for its features preserving users' anonymity, such as allowing users to register without providing a telephone number

For a great introduction on how to setup a Kik bot, and obtain the neccassary permissions and tokens, head over to the [Kik Documentation](https://kik.readthedocs.io/en/latest/)

Kik Client operates as a webhook REST server, so the config required reflects this. Like all Program-Y REST clients it requires host, port and debug flags as follows in config.yaml. In addition it needs the name of the bot and the webhook to call back when it has messages for the client.
```yaml
kik:
  bot_name: servusai
  webhook: https://4264d3b1.ngrok.io/incoming
  host: 127.0.0.1
  port: 5000
  debug: false
```

In addition, once you have registered your bot with Kik, bot API token and add them to the license.keys file as follows
```ini
KIK_BOT_API_KEY = XXXXXXX
```

To run the Facebook client, you can use the shell script in Y-Bot scripts folder
```bash
./y-bot-kik.sh
```

Or you can use the command line 
```bash
python3 -m programy.clients.rest.flask.facebook.client --config <PATH TO CONFIG> --cformat yaml --logging <PATH TO LOGGING>
```
