## Multiple Clients
Program-y now ships with a wide range of client types, including
* Web Chat
* Facebook
* Telegram
* Twitter
* XMPP
* REST
* Socket
* Console

It would be very inefficient to load the same grammar multiples times for each client, so this page describes how to set up a single grammar and then configure a number of bots to use the same grammar. This provides a number of benefits
* Reduced the load on the server as the grammar is only loaded once
* Allows new clients to be added without taking down the core server
* Allows clients to be distributed over multiple servers for performance

For a full description of how we run Program-Y on our Servusai Platform, see [AWS Install](https://github.com/keiffster/program-y/wiki/Install_Linux_AWS)

## Overview
In summary, at the core of this solution is the use of the REST client. This client loads the entire grammar and is used to answer all questions. Through the use of `<sraix>` tag, all other clients have a single grammar which passes ALL questions to the REST service and displayed the returned answer. The only grammar processing each client then has to do is startup, shutdown and error handling if the REST service is unavailable.

## SRAIX Tag
The sraix allows a bot to call another bot using a well defined yet simple REST interface. The REST client is set up as a full client config with all grammar, sets, maps, rdf and other configuration files. All other clients only need to be configured with a single service as defined below
```yaml
brain:
    services:
        PROGRAMY:
            classname: programy.services.programy.ProgramyRESTService
            method: GET
            host: 0.0.0.0
            port: 8989
            url: /api/rest/v1.0/ask
```
The only grammar all other clients apart from the REST service require is the following. Which passes any text received by the individual client to the REST service and displays the result
```xml
<?xml version="1.0" encoding="UTF-8"?>
<aiml>

    <category>
        <pattern>*</pattern>
        <template>
            <sraix service="PROGRAMY"><star /></sraix>
        </template>
    </category>

</aiml>
```
Now no matter what you send to each client, the question is passed to the REST service and the response from the REST service displayed.

## Servusai Example
Programy ships with an example project called `servusai` which demonstrates how to use the core grammar contained in Y-Bot, exposed as a REST service and enabled for all other clients as per the instructions above to expose a multi client bot.

As an aside, Servusai is the domain that hosts the [Program-Y Demonstration](http://www.servus.ai/) on a AWS Lightsail instance.