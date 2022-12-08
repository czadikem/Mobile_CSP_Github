#Brain Selection

Each bot has the option to load one or more brains into itself and then the option to decide which brain
to select to answer a question. 

Each brain configuration for a bot is contained within the 'brains' section of the configuration file within
the specific bot the brain belongs to

```yaml
console:
    bots:
      bot1:
        brains:
          brain1:
            # Configuration for brain1 or bot 1
          brain2:
            # Configuration for brain2 or bot 1

      bot2:
        brains:
          brain3:
            # Configuration for brain3 or bot 1

```
