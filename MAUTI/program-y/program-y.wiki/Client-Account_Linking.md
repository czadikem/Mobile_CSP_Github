#Account Linking

If you are running multiple bots on the same grammar and want users to be able to allow conversations
to continue across these different bots in the context of a single conversation then this mechanism provides a way 
to allow a user to link accounts together.

The primary purpose of this is that the entire conversation is stored as a single entity. The user can use
this to retrieve previous questions and response, the bot can use the entire conversation to provide a consistent
sentiment analysis, and the bot can share variable values across all sessions

Account Linking is based on a small number of simple concepts

* Primary Account - The first account that the linking starts from. This contains the base references to all other 
linked accounts. It can be any client type. Removing the primary account link removes all links.

* Secondary Account - Every other account linked is considered a secodnary account and references back to the primary 
account. Removing a secondary account link just removes that association and impacts no other links

* Generated Key - When the process is started, the primary account is used to generate a key which is presented back to the user.
The user then presents this auto generated key back to the bot when linking secondary accounts.

##Link Primary Account
The bot ships with a basic grammar that you can use to link accounts. This grammar is typically called via an SRAI call
in grammar the grammar developer has collected the various pieces of information as part of a conversation.

This grammar requires 3 pieces of informaation

* User ID - User id associated with the primary account 
* Client ID - Name of the client which is the primary account
* Password - A user provided password that will be used as part of the secondary linking process

The core grammar is as follows

    LINK PRIMARY ACCOUNT <USERID> <CLIENTD> <USERPASSWORD>


The grammar will respond with either 

    PRIMARY ACCOUNT LINKED <GENERATEDKEY>

The grammar developer should retain the GENERATEDKEY value and show it back to the user

If an error occurs then the grammar responds with 

    INVALID PRIMARY ACCOUNT COMMAND
    

##Link Secondary Account
The next step in the linking process is from another client to initiate a secondary account linking grammar
as follows
 
    LINK SECONDARY ACCOUNT <PRIMARYUSERID> <SECONDARYUSERID> <SECONDARYCLIENTID> <USERPROVIDEDKEY> <GENERATEDKEY>

This takes the following parameters

* Primary User ID - User id associated with the primary account 
* Primary Client ID - Name of the client which is the primary account
* Secpnday User ID - User id associated with the secondary account 
* Secondary Client ID - Name of the client which is the seconday account
* Password - A user provided password supplied during the primary account linking process
* Generated Key - The provided back during the primary linking process

If the link is successful, the grammar reponds with the following

    SECONDARY ACCOUNT LINKED
    
If the link is unsuccessful then the follow grammar is returned

    INVALID SECONDARY ACCOUNT COMMAND
    
        
##Removing Link
Coming soon...