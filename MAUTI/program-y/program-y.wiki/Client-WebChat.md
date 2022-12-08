# Overview
The WebChat client provides a very basic HTML based chat client. The client uses a combination of the Python Flask library and some basic Javascript/Ajax on the client. It is by no way meant to be a fully features and production ready web client. Instead, it is designed to show how a web client could be integrated.

## Running the Client

TTo run the Facebook client, you can use the shell script in Y-Bot scripts folder
```bash
./y-bot-webchat.sh
```

Or you can use the command line 
```bash
python3 -m programy.clients.rest.flask.webchat.client --config <PATH TO CONFIG> --cformat yaml --logging <PATH TO LOGGING>
```

## Configuration Settings
Configuration settings are described in the Wiki page [Web Chat Configuration](./Config-Client-WebChat)
