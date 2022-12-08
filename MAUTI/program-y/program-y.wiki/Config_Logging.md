# Logging Configuration

Program-Y using Python logging for all logging output. 
For a full description of how to specify logging configuration options see 
the [Python Logging Documentation](https://docs.python.org/3/library/logging.config.html#user-defined-objects)

The current logging file is as follows and is a good start which logs all output to /tmp/y-bot.log

```yaml
    version: 1
    disable_existing_loggers: False

    formatters:
      simple:
        format: '%(asctime)s  %(name)-10s %(levelname)-7s %(message)s'

    handlers:
      file:
        class: logging.handlers.RotatingFileHandler
        formatter: simple
        filename: /tmp/y-bot.log

    root:
      level: DEBUG
      handlers:
          - file
```

## Changing Logging Location

If for some reason you want to switch off logging then you have 2 options, either

Log to /dev/null on Linux as follows

```yaml
    version: 1
    disable_existing_loggers: False

    formatters:
      simple:
        format: '%(asctime)s  %(name)-10s %(levelname)-7s %(message)s'

    handlers:
      file:
        class: logging.handlers.RotatingFileHandler
        formatter: simple
        filename: /dev/null

    root:
      level: DEBUG
      handlers:
          - file
```
This is useful if you just want to switch off logging temporarily but switch back the file later

Alternatively use the NullHandler as follows

```yaml
    version: 1
    disable_existing_loggers: False

    formatters:
      simple:
        format: '%(asctime)s  %(name)-10s %(levelname)-7s %(message)s'

    handlers:
      file:
        class: logging.handlers.NullHandler
        formatter: simple

    root:
      level: DEBUG
      handlers:
          - file

```

This being a more permanent solution

## Changing Logging Level

An alternative to changing where the output is written to is to change the logging level. 
In Python logging there are X levels

* CRITICAL
* ERROR
* WARNING
* INFO
* DEBUG

Where DEBUG is the most verbose and produces the most output an CRITICAL will only output the most major issues, 
usually when something catastrophic ( or critical ! ) has gone wrong and the application is about to terminate


