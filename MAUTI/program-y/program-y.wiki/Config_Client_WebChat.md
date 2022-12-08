# Web Chat Client Configuration

In addition to the [common configuration items](./Config_Client_Rest) available to all rest based clients, the additional configuration 
items available to a Webchat client are as follows

```yaml
webchat:
    cookie_id: ProgramYSession
    cookie_expires: 90
```

* **cookie_id** - The ID of the cookie to write the users browser to determine session stickiness
* **cookie_expires** - How long in days the cookies lasts for, defaults to 90 days

