# Brain Configuration

Thye brain configuration controls how the brain interprets, processes the questions you ask and presents the answers back.

It is made up a large number of configurable options, all of which have default values, so you don't need to set any when you first start using the bot.

The configuration sections are as follows

 * [Overrides](./Config_Brain_Overrides)
 * [Defaults](./Config_Brain_Defaults)
 * [Binaries](./Config_Brain_Binaries)
 * Braintree
 * [Services](./Config_Brain_Services)
 * [Security](./Config_Brain_Security)
 * Dynamic Maps and Sets
 * Tokenizers
 * Debug Files
 
 ## Exmaple
 
 ```yaml
 brain:

    # Overrides
    overrides:
      allow_system_aiml: true
      allow_learn_aiml: true
      allow_learnf_aiml: true

    # Defaults
    defaults:
      default_get: unknown
      default_property: unknown
      default_map: unknown
      learnf-path: file

    # Binary
    binaries:
      save_binary: true
      load_binary: true
      load_aiml_on_binary_fail: true

    # Braintree
    braintree:
      create: true

    services:
        REST:
            classname: programy.services.rest.GenericRESTService
            method: GET
            host: 0.0.0.0
            port: 8080
        Pannous:
            classname: programy.services.pannous.PannousService
            url: http://weannie.pannous.com/api

    security:
        authentication:
            classname: programy.security.authenticate.passthrough.BasicPassThroughAuthenticationService
            denied_srai: AUTHENTICATION_FAILED
        authorisation:
            classname: programy.security.authorise.usergroupsauthorisor.BasicUserGroupAuthorisationService
            denied_srai: AUTHORISATION_FAILED
            usergroups:
              storage: file

    dynamic:
        variables:
            gettime: programy.dynamic.variables.datetime.GetTime
        sets:
            numeric: programy.dynamic.sets.numeric.IsNumeric
            roman:   programy.dynamic.sets.roman.IsRomanNumeral
        maps:
            romantodec: programy.dynamic.maps.roman.MapRomanToDecimal
            dectoroman: programy.dynamic.maps.roman.MapDecimalToRoman
```   