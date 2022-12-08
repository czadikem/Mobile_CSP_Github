# Overview

This service provides access to the Pandora Bot API which is described in full detail at chatbots.io

## Configuration

In terms of configuration, all that is required is the following options added to the services section of config.yaml
```yaml
    services:
        Wikipedia:
            classname: programy.services.wikipediaservice.WikipediaService
```

## Usage

in terms of using Wikipedia service, the following AIML will call Wikipeia API and display the response given
```xml
<category>
    <pattern>ASKWIKIPEDIA *</pattern>
    <template>
        <sraix service="WIKIPEDIA"><star /></sraix>
    </template>
</category>
```