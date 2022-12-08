# Brain Configuration Defaults

These options control some of the default values the bot responds with when something is undetermined

```yaml
bot:
  defaults:
    default_get: unknown
    default_property: unknown
    default_map: unknown
```

* **default_get** - if the '<get>' tag failed to find a value, this the value that is returned. If not defined if defaults to 'unknown' 
* **default_property** - if the '<property>' tag failed to find a value, this the value that is returned. If not defined if defaults to 'unknown' 
* **default_map** - if the '<map>' tag failed to find a value, this the value that is returned. If not defined if defaults to 'unknown'
