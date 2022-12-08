[Viber](http://www.viber.com) is a cross-platform instant messaging and voice over IP (VoIP) application operated by Japanese multinational company Rakuten, provided as freeware for the Microsoft Windows, macOS, Linux, Android and iOS platforms. It requires a telephone computer to operate. In addition to instant messaging, it allows users to exchange media such as images and video records.

For a description on how to register your bot with Viber and access the necessary security tokens, please see the [Viber Documentation](https://developers.viber.com/docs/api/python-bot-api/)

Viber configuration requires 2 settings in config.yaml as follows. This defines the name of your bot and the avatar it will display
```yaml
viber:
  name: Servusai
  avatar: http://viber.com/avatar.jpg
```

In addition to need to make the security token given in the viber developer website as follows
```ini
VIBER_TOKEN = XXXXX
```

To run the Facebook client, you can use the shell script in Y-Bot scripts folder
```bash
./y-bot-viber.sh
```

Or you can use the command line 
```bash
python3 -m programy.clients.rest.flask.viber.client --config <PATH TO CONFIG> --cformat yaml --logging <PATH TO LOGGING>
```
