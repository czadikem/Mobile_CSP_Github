# Out Of Band (OOB)

Out of band ( or OOB ) is a way for the bot to return commands back to the processing client. 
The commands are embedded as specific XML in the text response from the bot. 
An OOB processor strips out the XML and passes it to an OOB processor configured to understand the specific xml

For example you could develop a bot that can control you PC. It would respond to commands such as "VOLUME UP", "VOLUME DOWN",
"PLAY NEXT TRACK", "PAUSE" etc. The OOB processor would know how, for you specific architecture (OSX, Linux, Windows etc)
how to do this. 

Programy ships with a number of Out of Band processors for you to use and/or extend. They are loaded through a configuration file
using the storage engine

In the entities section of the storage config, define a 'oobs' section and specify the storage type. In the example below we 
are using 'file'
```yaml
  storage:
    entities:
        oobs: file
```
   
Then in the stores section, specify the location and file type of the config file as follows
```yaml 
  storage:
    stores:
      file:
        type: file
        config:
          oobs_storage:
            file: ./oob/callmom.conf
            extension: null
            subdirs: false
            format: text
            encoding: utf-8
            delete_on_start: false

```

A typicaly config file looks like the example below, each OOB has a name which corresponds to its xml tag, and the classname of the
python object to use to process the OOB request
```buildoutcfg
default=programy.oob.callmom.DefaultOutOfBandProcessor
alarm=programy.oob.callmom.alarm.AlarmOutOfBandProcessor
camera=programy.oob.callmom.camera.CameraOutOfBandProcessor
clear=programy.oob.callmom.clear.ClearOutOfBandProcessor
dial=programy.oob.callmom.dial.DialOutOfBandProcessor
dialog=programy.oob.callmom.dialog.DialogOutOfBandProcessor
email=programy.oob.callmom.email.EmailOutOfBandProcessor
geomap=programy.oob.callmom.map.MapOutOfBandProcessor
schedule=programy.oob.callmom.schedule.ScheduleOutOfBandProcessor
search=programy.oob.callmom.search.SearchOutOfBandProcessor
sms=programy.oob.callmom.sms.SMSOutOfBandProcessor
url=programy.oob.callmom.url.URLOutOfBandProcessor
wifi=programy.oob.callmom.wifi.WifiOutOfBandProcessor
```

AS an example, dial tag typically looks like
```xml
<category>
    <pattern>DIAL *</pattern>
    <template>
        OK, I'm dialing <star />
		<oob><dial><star /></dial></oob>
	</template>
</category>
```

OOB works through a combination of a dynamically loaded class and associated configuration. For each OOB node that you want to use you need to develop and associated Python class. The base class to subclass and build on is defined as the following

```python
import xml.etree.ElementTree as ET

class OutOfBandProcessor(object):

    def __init__(self):
        return

    # Override this method to extract the data for your command
    # See actual implementations for details of how to do this
    def parse_oob_xml(self, oob: ET.Element):
        return

    # Override this method in your own class to do something
    # useful with the command data
    def execute_oob_command(self, bot, clientid):
        return ""

    def process_out_of_bounds(self, bot, clientid, oob):
        if self.parse_oob_xml(oob) is True:
            return self.execute_oob_command(bot, clientid)
        else:
            return ""

```

As an example, here we have an Out Of Band capability to send an email from your client device, the OOB AIML is as follows

```xml
<oob>
    <email>
        <to>recipient</to>
        <subject>subject text</subject>
        <body>body text</body>
    </email>
</oob>
```

The class that implements this would look similar to the following, the only addition to make this work would be to subclass the class before and implement the execute_oob_command() method to send and email

```python
class EmailOutOfBandProcessor(OutOfBandProcessor):

    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._to = None
        self._subject = None
        self._body = None

    def parse_oob_xml(self, oob: ET.Element):
        for child in oob:
            if child.tag == 'to':
                self._to = child.text
            elif child.tag == 'subject':
                self._subject = child.text
            elif child.tag == 'body':
                self._body = child.text
            else:
                logging.error ("Unknown child element [%s] in email oob"%(child.tag))

            if self._to is not None and \
                self._subject is not None and \
                self.body is not None:
                return True

            logging.error("Invalid email oob command")
            return False

    def execute_oob_command(self, bot, clientid):
        logging.info("EmailOutOfBandProcessor: Emailing=%s", self._to)
        return ""
```
