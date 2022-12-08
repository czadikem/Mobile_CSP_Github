# Logger Storage

This storage engine provides the capability to write all conversations to a seperate file using Python logging capabilities

To use this storage option for your conversation storage, use the following configuration

```yaml
console:
  storage:
      entities:
          conversations:   logger

       stores:
         logger:
              type:   logger
              config:
                  conversation_logger: conversation

```

The 'entities' element states that for conversations use the logger store. This must then reference
a store in the 'stores' section called 'logger' and of type 'logger'. 

The only configuration is the name of the Python logger to use to write the conversations. This will tyoically 
reference a logger defined in logging.yaml. An example would be

```yaml
version: 1
disable_existing_loggers: False

formatters:
  conversation:
    format: '%(asctime)s - %(message)s'
  simple:
    format: '%(asctime)s  %(name)-10s %(levelname)-7s - %(message)s'

handlers:
    file:
        class: logging.handlers.RotatingFileHandler
        formatter: simple
        filename: /tmp/y-bot.log
        maxBytes: 20972152
        backupCount: 10
        encoding: utf-8

    conversation:
        class : logging.handlers.RotatingFileHandler
        formatter: conversation
        filename: /tmp/y-bot-conversation.log

loggers:
  conversation:
    level: DEBUG
    handlers:
      - conversation
    propogate: no

root:
    level: DEBUG
    handlers:
        - file

``` 

If the bot is run with this overall configuration, all conversations will be written to the file '/tmp/y-bot-conversation.log'
and formatted as per the formatting instructions in logging.yaml for conversation.