# Brain Security Configuration

```yaml
   security:
        authentication:
            classname: programy.utils.security.authenticate.passthrough.BasicPassThroughAuthenticationService
            denied_srai: AUTHENTICATION_FAILED
            denied_text: Access denied
        authorisation:
            classname: programy.utils.security.authorise.usergroupsauthorisor.BasicUserGroupAuthorisationService
            denied_srai: AUTHORISATION_FAILED
            denied_text: You are not authorised to ask that
            usergroups: $BOT_ROOT/config/roles.yaml
```

## Authentication
* **classname** - Defines the full python path of the class to loaded which implements the base class 'Authenticator', defaults to programy.utils.security.authenticate.passthrough.BasicPassThroughAuthenticationService
* **denied_srai** - If authentication fails, then the interpreter excutes the grammar defined in this setting as an SRAI operation. Your aiml files should contain this as a category pattern with appropraite text showing access denied. Default is AUTHENTICATION_FAILED
* **denied_text** - Rather the specify an SRAI element, specifying this instead results in just the actual text being returned without any further processing, default is Access Denied

## Authorisation
* **classname** - Defines the full python path of the class to loaded which implements the base class 'Authorisor'. Default value is programy.utils.security.authorise.usergroupsauthorisor.BasicUserGroupAuthorisationService
* **denied_srai** - If authorisation fails, then the interpreter excutes the grammar defined in this setting as an SRAI operation. Your aiml files should contain this as a category pattern with appropraite text showing access denied. Default is AUTHORISATION_FAILED
* **denied_text** - Rather the specify an SRAI element, specifying this instead results in just the actual text being returned without any further processing. If missing defaults to Access Denied
* **usergroups** - Full path to a Yaml configuration file containing users, groups and roles to use with the authorisation service