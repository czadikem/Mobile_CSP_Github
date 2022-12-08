# Overview
This service provides access to the Pandora Bot API which is described in full detail at [chatbots.io](https://developer.pandorabots.com/docs)

## Configuration
In terms of configuration, all that is required is the following options added to the services section of config.yaml
```yaml
    services:
        Pandora:
            classname: programy.services.pandora.PandoraService
            url: http://www.pandorabots.com/pandora/talk-xml
```
In addition the following addition to license.keys is required
```ini
PANDORA_BOTID = XXXXXXXXXXX
```
Where XXXXXXXXXXX is the license key you obtained by registering with Pandora

## Usage
in terms of using Pandora service, the following AIML will call Pandora bot and display the response given
```xml
<category>
    <pattern>ASKPANDORA *</pattern>
    <template>
        <sraix service="PANDORA"><star /></sraix>
    </template>
</category>
```

