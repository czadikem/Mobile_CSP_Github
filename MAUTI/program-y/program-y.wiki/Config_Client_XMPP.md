# XMPP Client Configuration

In addition to the [common configuration items](./Config_Client) available to all clients, the additional configuration 
items available to a XMPP client are as follows

```yaml
xmpp:
  server: talk.google.com
  port: 5222
  xep_0030: true
  xep_0004: true
  xep_0060: true
  xep_0199: true
```

* **server** - The IP or DNS  name of the server hosting your XMPP Client
* **port** - The port number the server is running on
* **xep_0030** - Enable XMPP Extension xep_0030 - Service Discovery
* **xep_0004** - Enable XMPP Extension xep_0004 - Data Forms
* **xep_0060** - Enable XMPP Extension xep_0060 - Publish-Subscribe
* **xep_0199** - Enable XMPP Extension xep_0199 - XMPP Ping
