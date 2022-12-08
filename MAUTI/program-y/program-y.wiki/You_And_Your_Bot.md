# You and Your Bot

Once you have downloaded your bot, you will see it consists of 3 primary sub folders, each of which contain various files that control your bot. These folders and their content are described below

## scripts
The 'scripts' folder contains scripts which allow you to run your bot using the various clients that Program-y runs with. There are scripts for the core platforms windows which contains batch files, while xnix contains shell scripts to run your bots on Linux and Mac OSX.

For more details of the clients available and associated scripts, see the [Clients](./Clients) page.

## config
The 'config' folder contains config files which allow you to configure your bot using the various clients that Program-y runs with. There are config files for the core platforms; the windows folder which contains config files that work on windows , while xnix folder contains config files that configure your bots on Linux and Mac OSX.

For configuration details, see the [Config](./Config) page.

## storage
The storage folder contains all of the files your bot loads when its running with the storage model set to 'file'
There are a large number of sub folders, each of which hold a specific data file as follows
* categories - All AIML files and sub folder
* conversations - Created at startup if not exists, and stores a log of converations
* licenses - License keys
* lookups - Lookup files, denormal, normal, gender, person and person2
* maps - All map files
* nodes - A list of all nodes the system loads and supports
* processing - List of pre and post processors
* properties - Properties and default variable values 
* rdfs - All RDF files
* regex - List of all regexs to use in regex nodes
* security - Security information
* sets - All set files
* spelling - Spelling corpus, only if using Norvig spelling checker
* triggers - Trigger files
* twitter - Used by the Twitter Client to store messages ids

For more details of the how to configure the various storage models, see the [Storage](./Storage) page.

## Next Steps

Now that you have a bot and know the basics of your file structure of the bot, you are ready to start adding grammars to your bot. If you are new to AIML then start with the [AIML Tutorial](./AIML-Tutorial) or for more information on how to configure your bot and change your behaviour, head over to [Configuring Your Bot](./Config)

