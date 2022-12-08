# Overview
This service provides access to the Pannous Bot API which is described in full detail at [Pannous website](http://pannous.com/)

## Configuration
In terms of configuration, all that is required is the following options added to the services section of config.yaml
```yaml
    services:
            classname: programy.services.pannous.PannousService
            url: http://weannie.pannous.com/api
```
In addition the following addition to license.keys is required
```ini
PANNOUS_LOGIN = XXXXXXXXXXX
```
Where XXXXXXXXXXX is the userid you obtained by registering with the Pannous service

## Usage
in terms of using Pannous service, the following AIML will call Pandora bot and display the response given
```xml
<category>
    <pattern>WHAT DO YOU KNOW ABOUT *</pattern>
    <template>
        <sraix service="pannous">WHAT IS <star/></sraix>
    </template>
</category>
```

