# REST Based Security

Program-Y provides 2 mechanisms to implement REST based Authentication

## Authorization Header

Each REST service is now enabled to use Basic Authorization as defined by HTTP standards. This is
based on setting the 'Authorization' parameter in the header. Program-y does this automatically for you
when you set the 'authorization' config setting as follows

```yaml
flask:
  description: Program-Y Flask Rest Client
  host: 0.0.0.0
  port: 9999
  debug: false
  authorization: Basic
```

The rest server will now only accept requests when the following header is sent, which is done for
you automatically by Program-y

```text
Authorization: Basic XXXXXXXXXXXXXX
```

For the server the value for the authorization token is stored in the license.keys file in licenses folder of your storage folder you then need to add the Authorisation token

```text
BASIC_AUTH_TOKEN = XXXXXXXXXXXXXX
```

### Services

For a service, you just need to add 'authorization' config item

```yaml
    services:
        PROGRAMY:
            classname: programy.services.programy.ProgramyRESTService
            method: GET
            url: /api/rest/v1.0/ask
            host: 127.0.0.1
            port: 8989
            authorization: Basic
            
```

### Open Chatbots

For Open Chatbot services, you add it to the open chat bot configiration as follows

```yaml
    openchatbots:
      chatbot3:
        url: http://localhost:9999/api/rest/v2.0/ask
        method: GET
        authorization: Basic
```

Again for the calling client, the value for the authorization token is stored in the license.keys file in licenses folder of your storage folder you then need to add the Authorisation token

```text
BASIC_AUTH_TOKEN = XXXXXXXXXXXXXX
```

## API Keys

Either as an alternative to authorization defined above, or as an addition to. Each rest service is able to 
use api keys as a security mechanism. Using this, instead of all clients sending the same authorization token, each client
is supplied with an API Key, unique to them. 

The server maintains a list of valid API keys and rejects any requests that do not have a valid API key

Using API Keys is configured in the server by setting the 'use_api_keys' and 'api_key_file' config items as follows

```yaml
flask:
  description: Program-Y Flask Rest Client
  host: 0.0.0.0
  port: 7777
  debug: false
  use_api_keys: true
  api_key_file: ../../storage/keys/keys.txt
```

The keys.txt file is a text file contains a list of api keys as follows

```text
11111111111111
22222222222222
33333333333333
```

Each client then then sets the 'api_key' config item as follows

### Rest

For REST services, you set the API Key as part of the service definition 

```yaml
    services:
        PROGRAMY:
            classname: programy.services.programy.ProgramyRESTService
            method: GET
            url: /api/rest/v1.0/ask
            host: 127.0.0.1
            port: 8989
            api_key: '11111111111111'

```

### Open Chatbots

For Open Chatbots you set the api key as follows

```yaml
    openchatbots:
      chatbot4:
        url: http://localhost:7777/api/rest/v2.0/ask
        method: GET
        api_key: '11111111111111'
```

NOTE: api keys storage is likely to move into the storage system in a future date, but backward compatibility will be maintained for a number of releases

