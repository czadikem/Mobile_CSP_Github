# Triggers

Triggers provide a way in which to generate events that you can hook into while a Program-Y is running, the system
currently supports the following events. (Please note that this list is constantly being added to as new events are
added to the application )

* **SYSTEM_STARTUP** - At system startup before any processing takes place
* **SYSTEM_SHUTDOWN** - The last thing the system does before exiting
* **CONVERSATION_START** - AS each new conversation starts. This is based on the unique Id, the first time it is seen, this event is triggered
* **QUESTION_ASKED** - Provides the question and answer

The trigger system is made up of 2 distinct parts

* **Trigger Manager** - A handle for all triggers
* **Trigger** - An object that handles a specific event

The system ships with 2 different trigger managers

* **Local** - Maps the event to a preloaded Python object, executing the code in the Python trigger object
* **REST** - Calls a REST endpoint with a JSON payload represent the triggered event

## Local Trigger Manager
A local trigger manager is configured using the following data in your 'config.yaml'. It requires a single parameter
'manager' which is the Python path to a trigger manager object implementing the TriggerManager interface.

```yaml
console:
    triggers:
        manager: programy.triggers.local.LocalTriggerManager
```

The local trigger manager has additional configuration as part of the storage system. This is where you define how the
of events and their mapped trigges are loaded. 

A typical storage configuration to load a triggers file is as follows:

```yaml
console:
  storage:
      entities:
          triggers: file

    stores:
      file:
        triggers_storage:
          file: ../../storage/triggers/triggers.txt
  
```

A triggers.txt file is made up of a series of lines which provide a mapping to events and the Python object to execute
when the event is captured by the manager. An event can have any number of objects attached to it, all are fired when the
is captured.

```text
SYSTEM_STARTUP:programy.triggers.null.NullTrigger
SYSTEM_STARTUP:programy.triggers.null.NullTrigger
SYSTEM_SHUTDOWN:programy.triggers.null.NullTrigger
CONVERSATION_START:programy.triggers.null.NullTrigger
```

## REST Trigger Manager
The REST Trigger Manager is a simpler manager, in that it sends a json payload of the event and additional data based on 
the type of event to a REST end point

The configuration for the REST Manager is as follows:

```yaml
console:
    triggers:
        manager: programy.triggers.rest.RestTriggerManager
        url: http://localhost:8989/api/v1.0/trigger
        method: POST
        token: 123BC4F3D
```

* **manager** - 
* **url** - REST endpoint to call
* **method** - Optional REST method to use, defaults to POST if not defined
* **token** - Optional API Token which is passed to the receiver in the Bearer Header parameter

## Test Receiver
Programy ships with test trigger event receive 'programy/triggers/receiver.py'. This is a simple Flask REST server which
exposes a single endpoint '/api/rest/v1.0/trigger'. The code is as follows and is provided as a basis for you building
your own Trigger REST receiver

```python
import sys

from flask import Flask, request, json

if __name__ == '__main__':

    print("Initiating Trigger Receiver...")
    receiver = Flask(__name__)

    @receiver.route('/api/rest/v1.0/trigger', methods=['POST'])
    def trigger():
        print("\nTrigger received...")
        try:
            print(request.json)
        except Exception as e:
            print(e)
        return 'OK'

    receiver.run(port=sys.argv[1])
```

To configure you client to call this REST trigger receiver, use the following configuration elements in your 'conf'g.yaml'
```yaml
console:
  triggers:
    manager: programy.triggers.rest.RestTriggerManager
    url: http://localhost:8989/api/rest/v1.0/trigger
```

To run the REST server, use the following command line, the only parameter is the PORT on which the server is running and
should be the same as the port in the above 'url' configuration item. You should then see the following output when it is running.

```bash
python3 -m programy.triggers.receiver 8989

Initiating Trigger Receiver...
Loading, please wait...
 * Serving Flask app "receiver" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

If you have 'wget' installed on your system, you can test it using the following line. Again making sure that the port number
is the same as the only provided as the parameter to the receiver.

```bash
 wget -S --header='Content-Type: application/json' --post-data '{"event": "SYSTEM_STARTUP"}' http://localhost:8989/api/rest/v1.0/trigger
```

### Building a Trigger Manager
A trigger manager is based of the  abstract class programy.triggers.manager.TriggerManager, and should inherit
this class. It should implement the 'trigger' method as in the example below:

The full Python class path to this object should then be added to the 'manager' configuration item as above.

```python
from programy.triggers.config import TriggerConfiguration
from programy.context import ClientContext


class MyTriggerManager(TriggerManager):

    def __init__(self, config: TriggerConfiguration):
        TriggerManager.__init__(self, config)

    def trigger(self, event: str, client_context: ClientContext = None, additional: {} = None) -> bool:
        # Trigger Logic goes here
```

### Building a Trigger
A trigger is based on the abstract class programy.triggers.trigger.Trigger, and should inherit this class. It should
then implement the 'trigger' method. The local trigger manager calls this method for each object loaded which maps to the 
associated trigger event.

```python
from programy.triggers.trigger import Trigger
from programy.context import ClientContext


class Trigger1(Trigger):

    def __init__(self):
        Trigger.__init__(self)

    def trigger(self, client_context: ClientContext = None, additional = None):
        # Trigger logic goes here
```

## Adding Customer Triggers
If you wish to add custom events to your own code, then its a simple as using the client_context object to get the client
and to use the trigger_mgr attribute as follows. Note always worth checking trigger_mgr is not None is case it didn't load on startup
```python
    if client_context.trigger_mgr is not None:
        client_context.trigger_mgr.trigger(event="MYEVENT")

```

If you are using the local client, then MYEVENT will need to map to a python object in triggers.txt as above

