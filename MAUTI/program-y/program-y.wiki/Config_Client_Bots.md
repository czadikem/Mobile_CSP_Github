
#Bot Selection

Each client has the option to load one or more bots into itself and then the option to decide which bot
to select to answer a question. 

Each client bot configuration is contained within a 'bots' section of the configuration file

```yaml
console:
  bots:
    bot: 
      # Configuration for the bot goes here 

```

If you want to load more then one bot then you list each of them as distinctly named bots in the 'bots' 
section of the configuration

In this instance we have chosen to use the Round Robin Selector, but you can write your own, or use
one of the other system defined classes

```yaml
client:
  bot_selector: programy.clients.client.RoundRobinBotSelector
  bots:
    bot1:
      # Bot 1 configuration goes here
    bot2:
      # Bot 2 configuration goes here
  
```

