Please note there are 2 rest clients, one which uses Flask and one use the async library Sanic. Only the Flask version currently works on all platforms. Sanic struggles to install on Windows, so until further notice only use Sanic on Linux of Max

# Overview
The REST client exposes the bot through a REST compliant API, with a GET endpoint `/api/rest/v1.0/ask`. This endpoint takes 2 parameters
* question - which is a urlencoded question to ask. 
* userid - A unique identifier for the user making the call

An example of the URL would therefore be
```
http://localhost:8989/api/rest/v1.0/ask?question=hello+world&userid=1234567890
```

The client returns a response as a JSON package of the format containing a response object and the HTTP status code as follows

```json
[
  {
    "response": {
      "answer": "Hello!", 
      "question": "hello world", 
      "userid": "1234567890"
    }
  }, 
  200
]
```

## Running the Client

To run the client, use a derivative of the following script

```bash
    #! /bin/sh
    clear
    export PYTHONPATH=../../src:.
    python3 -m programy.clients.restful.sanic.client --config ./config.yaml --cformat yaml --logging ./logging.yaml
```

### Using Curl
You can test the client using curl using the following command
```bash
curl 'http://localhost:8989/api/rest/v1.0/ask?question=hello+world&userid=1234567890'
```
This will return the following response against Y-Bot
```json
[
  {
    "response": {
      "answer": "Hello!", 
      "question": "hello world", 
      "userid": "1234567890"
    }
  }, 
  200
]
```
## Configuration Settings

Configuration settings are described in the Wiki page [REST Configuration](./Config-Client-Rest)
