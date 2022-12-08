# Configuration Substitutions

Version 3.6 onwards addresses a couple of issues around the use of configuration files. It introduces 2 new concepts

## License Key Substitutions
1) Ability to autoload values from license.keys into config data. By specifying a config item as LICENSE_KEY:VALUE it will replace the value in license.keys into the config data. This means config such as
```yaml
client:
  email:
    username: LICENSE_KEY:EMAIL_USERNAME
    password:LICENSE_KEY:EMAIL_PASSWORD
```
Can use the username and password values stored in license keys as
```text
EMAIL_USERNAME=fredwest@gmail.com
EMAIL_PASSWORD=pavingslabs
```
This is a clean way of keeping config files free of secure data and keeping license.keys out of GitHub by using .gitignore

## Command Line Subsitutions
Ability to pass a substitutions.txt file as a command line parameter. Values in this file will be automatically replaced in your config file, e.g
```yaml
client:
  email:
    host: $EMAIL_HOST
    port: $EMAIL_PORT
```

You can then have multiple substitutions.txt files with different values
```text
$EMAIL_HOST:prod_server.com
$EMAIL_PORT:9999
```

and 
```text
$EMAIL_HOST:test_server.com
$EMAIL_PORT:888
```
By just passing in the subs file as '-subs substitutions.txt' you can keep one config file and just change environment settings.
