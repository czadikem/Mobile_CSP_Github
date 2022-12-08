Y-Bot supports persistence of conversation state by saving the state of all properties between bot sessions. This functionality is based on 2 factors

* Default Variables - Provide a way to seed all variables available to the system with default values
* Variable Persistence - Stores on the filesystem the value of all variables as they change

When bot starts it loads the default values and keeps them cached. As each user connects ( identified by a unique client id ), the default values are used to seed their session variables. As the user then interacts with the not and these variables change then their values are saved. Each time the user returns and is identified by the same client id, their saved state is reloaded.

## Default Variables
New config option properties which will load a set of default property values into each new conversation as it is initiated. New conversations are defined by a unique client id

```yaml
files:
    aiml:
        properties: $BOT_ROOT/config/properties.txt
```

## Saving Variables
Conversation state storage is configured by the conversations configuration element of the bot section of the configuration file.

The first section `conversations` defines the `type` of storage, and then `config_name` points to the type specific configuration section. A 3rd option `empty_on_start` allows the bot to clear down previous conversations, useful during development and debugging.

Currently, only file system storage is supported, but it is envisaged that various other mechanisms will be added such as SQL, NoSQL, Redis etc

```yaml
bot:
    conversations:
      type: file
      config_name: file_storage
      empty_on_start: true

    file_storage:
      dir: $BOT_ROOT/conversations
```

In the example above, we specify the storage type as `file`, which then points to `file_storage`, which only needs 1 config item, that of the folder to store conversations in. The system uses this folder to store a single file for each unique client containing name-value pairs of all variables.