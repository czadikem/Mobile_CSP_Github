# Brain Service Configuration
Programy provides the ability to define a number of services which can then be called from the 'sraix' tag. Each service is expected to be a basic REST API. The original AIML spec required the various configuration parameters to be embedded into the sraix tags, but this made changing them in multiple places difficult and error prone. 

The configuration has therefore been extracted into the config file, and all that is required in the 'sraix' tag is to define the service name.

```yaml
  brain:
    services:
        REST:
            classname: programy.utils.services.rest.GenericRESTService
            method: GET
            host: 0.0.0.0
        Pannous:
            classname: programy.utils.services.pannous.PannousService
            url: http://weannie.pannous.com/api
        Pandora:
            classname: programy.utils.services.pandora.PandoraService
            url: http://www.pandorabots.com/pandora/talk-xml
        Wikipedia:
            classname: programy.utils.services.wikipediaservice.WikipediaService
```

* **classname** - Name of the Python class which will call the service
* **method** - HTTP method, either POST or GET to use when calling
* **host** - IP or DNS name of the port hosting the service
* **port** - Port the service is running on
* **url** - Instead of using Host and Port, you can provide the full URL instead

