# Alliance for Open Chatbot

Program-y is proud to be involved and support the [Alliance for Open Chatbot](https://en.alliance-open-chatbot.org/)

The alliance is a working group whose ambition is to lead the development of open source chatbot interface.
Their goal is to interconnect chatbots to make them more effective and relevant.

The focus of the Alliance is to create an open API standard for bots to communicate with each other.
You can find details of this work on [GitHub](https://github.com/alliance-for-openchatbot/standard).

Program-y currently supports both client and server elements of the API, in that

* Client. Program-y has implemented ability to be able to call any chatbot that has implemented the agreed API
* Server. Program-y has implement the Open Chatbot API, making it available to be called from any chatbot

In addition Program-y has also built the concept of a Metabot which provides a single server configured to talk 
to a wide range of Open ChatBots, thus removing the need for Chatbot developers to integrate with multiple bots themselves.

## Server

#### Config

Operate as a REST Server as per normal REST configuration

```yaml
flask:
  description: Program-Y Flask Rest Client
  host: 0.0.0.0
  port: 8888
  debug: false
```

#### AIML

No specific AIML is required for the server, just the ability to respond to questions as per any other chatbot

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">

    <category>
        <pattern>*</pattern>
        <template>Chatbot1 says hello</template>
    </category>

 </aiml>
```

If you are running a metabot, then the following AIML us useful

```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml version="2.0">

    <category>
        <pattern>AT * *</pattern>
        <template>
            <sraix service="OPENCHAT"><star index="1" /> <star index="2" /></sraix>
        </template>
    </category>

 </aiml>
```

## Client 

#### Config

```yaml
    services:
        OPENCHAT:
            classname: programy.services.openchat.OpenChatRESTService

    openchatbots:
      protocols: http, https
      domains: org, co.uk
      chatbot1:
        url: http://localhost:8989/api/rest/v2.0/ask
        method: GET
      chatbot2:
        url: http://localhost:9898/api/rest/v2.0/ask
        method: GET
      chatbot3:
        url: http://localhost:9999/api/rest/v2.0/ask
        method: GET
        authorization: Basic
      chatbot4:
        url: http://localhost:7777/api/rest/v2.0/ask
        method: GET
        api_key: '11111111111111'
      metabot:
        url: http://localhost:8888/api/rest/v2.0/ask
        method: GET
```

#### AIML

Direct to Open Chatbot

```xml
    <category>
        <pattern>QUERY AT * *</pattern>
        <template>
            <sraix service="OPENCHAT"><star index="1" /> <star index="2" /></sraix>
        </template>
    </category>
```

Connecting to a Meta bot to route to other chatbots
```xml
    <category>
        <pattern>METABOT AT * *</pattern>
        <template>
            <sraix service="OPENCHAT">QUERY @METABOT <star index="1" /> <star index="2" /></sraix>
        </template>
    </category>
```

### Metabot

#### Config

Operate as a REST Server as per normal REST configuration

```yaml
flask:
  description: Program-Y Flask Rest Client
  host: 0.0.0.0
  port: 8888
  debug: false
```

In the brain config, define an OPENCHAT service, and then add the the Open Chatbots you want
to proxy to as follows

```yaml
brain:
    services:
        OPENCHAT:
            classname: programy.services.openchat.OpenChatRESTService

    openchatbots:
      protocols: http, https
      domains: org, co.uk
      chatbot1:
        url: http://localhost:8989/api/rest/v2.0/ask
        method: GET
      chatbot2:
        url: http://localhost:9898/api/rest/v2.0/ask
        method: GET
      chatbot3:
        url: http://localhost:9999/api/rest/v2.0/ask
        method: GET
        authorization: Basic
      chatbot4:
        url: http://localhost:7777/api/rest/v2.0/ask
        method: GET
        api_key: '11111111111111'
```

### AIML
