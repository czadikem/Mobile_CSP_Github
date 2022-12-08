#Redis Storage
The redis storage engine is typically used to cache variables in a redis store and is useful if you are running 
multiple instances of a bot behind a load balancer. Without the use of a cache such as Redis then each bot will 
keep its own instance of the variables in memory and if the load balance swaps between 2 different instances during a 
conversation then there will likely be inconsistencies if variables are being used in the response

To configure Redis as a storage engine, use the following configuration. First we tell the bot that for variables 
we want to use a storage engine called 'redis'. This name can be any text, but must match the name name in the subsequent
'stores' section.

In the 'stores' section we define a new store with the same name as the value for 'variables' and give it a type of 'redis'.
The system will then know to load a Redis storage engine and use the configuration provided.

```yaml
  storage:
      entities:
          variables: redis

      stores:
        redis:
            type:   redis
            config:
                host: localhost
                port: 6379
                password: passwordX
                db: 0
                prefix: programy
                drop_all_first: True            

```

In terms of configuration

* host - Defines the name of the host the redis server is running on
* port - Defines the port on the host the redis server is running on
* password - Is the password to access the redis server
* db - Numeric value of the db to use, defaults to 0
* prefix - A text value to prefix to all bot variables to ensure they remain unique in the cache
* drop_all_first - Setting this to true will clear all variables in the cache on start up. Setting to false will result in variable values being preserved between bot restarts.
