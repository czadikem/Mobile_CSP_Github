# Brain Configuration Overrides

The configuration sections controls elements of the bot which can leave your bot open to security issues

```yaml
brain:
  overrides:
    allow_system_aiml: true
    allow_learn_aiml: true
    allow_learnf_aiml: true
```

* **allow_system_aiml** - Allow the use of the '<system>' tag
* **allow_learn_aiml** - Allow the '<learn>' tag which allows users to add new knowledge to the running bot
* **allow_learnf_aiml** - Allow the '<learnf>' tag which allows users to add new knowledge to the running bot, and also persist the knowledge to the storage system to be loaded at a later time


