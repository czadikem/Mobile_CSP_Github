[LINE Messenging](https://line.me/en/) is a freeware app for instant communications on electronic devices such as smartphones, tablet computers, and personal computers. Line users exchange texts, images, video and audio, and conduct free VoIP conversations and video conferences. The service is operated by Line Corporation, a Japanese subsidiary of the South Korean internet search giant Naver Corporation.

For a great introduction on how to setup a Line bot, and obtain the neccassary permissions and tokens, head over to the [Line Documentation](https://github.com/line/line-bot-sdk-python)

Line Client operates as a webhook REST server, so the config required reflects this. Like all Program-Y REST clients it requires host, port and debug flags as follows in config.yaml
```yaml
line:
  host: 127.0.0.1
  port: 5000
  debug: false
```

In addition, once you have regsitered your bot with Line, you can create the channel secret and access token and add them to the license.keys file as follows
```ini
LINE_CHANNEL_SECRET = XXXXX
LINE_ACCESS_TOKEN = XXXXX
```

To run the Facebook client, you can use the shell script in Y-Bot scripts folder
```bash
./y-bot-line.sh
```

Or you can use the command line 
```bash
python3 -m programy.clients.rest.flask.line.client --config <PATH TO CONFIG> --cformat yaml --logging <PATH TO LOGGING>
```
