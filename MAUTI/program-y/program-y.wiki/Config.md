# Configuring Your Bot

NOTE: Version 4 introduced some breaking changes to the way the configuration file is laid out. This is purely a 
structural change and is designed to align configuration file structure with internal client -> bot -> brain structure.

## Configuration File
Configuration is passed as parameter to the Python script using the --config option

    python3 ../../src/programy/clients/console.py --config ./config.yaml --cformat yaml --logging ./logging.yaml 

You can either specify the format with --cformat option, or the system will try and determine the format from the file extension of the config file you pass in the --config option

Configuration file can be either
* yaml
* json
* xml

## Command Line Options

All the clients have the same set of command line options which ar used to control initial startup

* --bot_root. Root folder for all bot configuration data
* --config [path to configuration file]. Specifies the configuration file to use to run the client. See [Configuration](./Configuration) for more details of configuration settings
* --cformat [yaml|json|xml]. Optionally specifies the format of the config file. If not specified programy will use file extension to work out the format
* --logging [path to logging configuration file]. Path to logging configuration file
* --noloop. Do not enter conversation loop. Only useful when debugging program start up. Program will run through startup, load configuration, and all grammars and then exit.
* ---subs. Allows you to substitute configuration items by keyword. See [Substitutions](./Config_Substitutions)

For this tutorial, we will focus on the Yaml version, but the names of values are the same. An example of a basic configuration file using Yaml file format is below

## Bot Root
In many of the paths defined in the configuration file, you will see a reference to a variable $BOT_ROOT. This allows the configuration file to be separate from many of the data files, or allows you to use partial paths when defining your config options.

Bot Root is set in one of 2 ways, either

* --bot_root. By passing this as a parameter to the client app, the full path given as the value is used in place of $BOT_ROOT
* default. If no parameter is passed to the client, then the current directory is used, and $BOT_ROOT is set to '.' 

When the configuration file is loaded for the first time, the $BOT_ROOT is replaced with the value from one of the 2 options above.

## Configuration Sections

The configuration file is made upon a number of distinct sections. 
These sections creation a hierarchy of configuration which reflects how the client, bot and brain elements work together.
The basic structure is that a client has 1 or more bots, and each bot has one or more brains. Bot and Brain selectors are 
used to select the appropriate brain to ask a question. Default is a basic round robin selector, but you have the option 
of writing your own. The basic is structure is therefore
```yaml
client:
    bots:
      bot1:
        brains:
          brain1:
          brain2:
      bot2:
        brains:
          brain3:
```

If upgrading to version 4, then the change requires adding bots: and brains: sections and moving and then tabbing right 
your bot and brain definition

At the core is a Client. There are a range of clients which offer different interfaces such as simple Console 
REPL interface to more complex social media platforms such as Facebook, Slack, Twitter etc.

  * [Clients](./Config_Client)
    * [Storage](./Storage)
    * [Healthcheck](./Client-Healthcheck)
  * [Bot](./Config_Bot)
    * [Sentence Splitting](./Config_Bot_Sentence)
    * [Spelling](./Config_Bot_Spelling)
    * [Sentiment Analysis](./Config_Bot_Sentiment)
    * [Translation](./Config_Bot_Translation)
  * [Brain](./Config_Brain)
    * [Overrides](./Config_Brain_Overrides)
    * [Defaults](./Config_Brain_Defaults)
    * [Binaries](./Config_Brain_Binaries)
    * [Services](./Config_Brain_Services)
    * [Security](./Config_Brain_Security)
  * [Logging](./Config_Logging)
