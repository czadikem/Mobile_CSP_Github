# Overview
This is the most generic of external services but allows you to call any REST service that exposes a GET or POST compliatn RESTful service. 

# Configuration
In terms of configuration, class name does not need to be changed. The user just needs to specify the method type GET or POST, the host and port the endpoint is exposed on and the details of the endpoint url. The GenericRESTService takes care of the rest. Taking the string of words contained as children of the node and returning the result of the call to the service as a string of words.
```yaml
    services:
        myservice:
            classname: programy.services.rest.GenericRESTService
            method: GET
            host: 0.0.0.0
            port:8080
            url:/api/rest/v1.0/ask
```

# Usage
    <category>
        <pattern>ASKOTHERSERVICE *</pattern>
        <template>
            <sraix service="myservice"><star /></sraix>
        </template>
    </category>
