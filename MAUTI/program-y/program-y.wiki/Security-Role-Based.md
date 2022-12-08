# Security

Program-Y provides 2 key elements of security

## Authentication

Authentication takes place directly within brain within the core code. Each time a user asks a question, the method ask_question() is called. One of its parameters is 'clientid' which is the id associated with the user asking the question. For clients like console this is always 'console' but for more online clients such as webchat, xmpp or twitter, its up to the developer to decide which id to use and how to make sure clientid is set appropriately ( more on this to follow )
 
```python
    def ask_question(self, bot, clientid, sentence) -> str:

        if self.authentication is not None:
            if self.authentication.authenticate(clientid) is False:
                logging.error("[%s] failed authentication!")
                return self.authentication.configuration.denied_srai

```

The authentication service is defined in a dynamically loaded class, the base class of which is defined as follows 

```python
class Authenticator(object):

    def __init__(self, configuration: BrainSecurityConfiguration):
        self._configuration = configuration

    @property
    def configuration(self):
        return self._configuration

    def get_default_denied_srai(self):
        return self.configuration.denied_srai

    def authenticate(self, clientid: str):
        return False
```

A very simple implementation of this class is a class that only authenticates those client ids that are contained within the 'authorised' array.

More advanced classes would call an external service to check the client id was truly authenticated.

```python
class ClientIdAuthenticationService(Authenticator):

    def __init__(self, configuration: BrainSecurityConfiguration):
        Authenticator.__init__(self, configuration)
        self.authorised = [
            "console"
        ]

    # Its at this point that we would call a user auth service, and if that passes
    # return true, appending the user to the known authorised list of user
    # This is a very naive approach, and does not cater for users that log out, invalidate
    # their credentials, or have a TTL on their credentials
    # #Exercise for the reader......
    def _auth_clientid(self, clientid):
        authorised = False # call user_auth_service()
        if authorised is True:
            self.authorised.append(clientid)
        return authorised

    def authenticate(self, clientid: str):
        try:
            if clientid in self.authorised:
                return True
            else:
                if self._auth_clientid(clientid) is True:
                    return True

                return False
        except Exception as excep:
            logging.error(str(excep))
            return False

```

The configuration to enable this capability is held within brain seection of config.yaml, within the security sub section as follows

```yaml
brain:
    security:
        authentication:
            classname: programy.utils.security.authenticate.clientidauth.ClientIdAuthenticationService
            denied_srai: AUTHENTICATION_FAILED
```

* classname. Defines the full python path of the class to loaded which implements the base class 'Authenticator'
* denied_srai. If authentication fails, then the interpreter excutes the grammar defined in this setting as an SRAI operation. Your aiml files should contain this as a category pattern with appropraite text showing access denied.

## Authorisation

Authorisation is currently implemented via basic User, Group and Role model, defined as 

* User. A user is a single entity. A user can both be assigned specific roles and inherited roles through inclusion in one or more groups
* Group. A collection of users that has one of more associated roles.
* Role. A string definition of an activity that a user of group can perform.

The base class for all authorisation is defined as

```python
class Authoriser(object):

    def __init__(self, configuration: BrainSecurityConfiguration):
        self._configuration = configuration

    @property
    def configuration(self):
        return self._configuration

    def get_default_denied_srai(self):
        return self.configuration.denied_srai

    def authorise(self, userid, role):
        return False
```

A basic implementation of this base class which performs User, Group and ROle based authorisation is as follows

```python
class BasicUserGroupAuthorisationService(Authoriser):

    def __init__(self, config: BrainSecurityConfiguration):
        Authoriser.__init__(self, config)
        self.load_users_and_groups()

    def load_users_and_groups(self):

        self._users = {}
        self._groups = {}

        if self.configuration.usergroups is not None:
            loader = UserGroupLoader()
            self._users, self._groups = loader.load_users_and_groups_from_file(self.configuration.usergroups)
        else:
            logging.warning("No user groups defined, authorisation tag will not work!")

    def authorise(self, clientid, role):
        if clientid not in self._users:
            raise AuthorisationException("User [%s] unknown to system!"%clientid)

        if clientid in self._users:
            user = self._users[clientid]
            return user.has_role(role)
        else:
            return False

```

Configuration is defined as

```yaml
    security:
        authorisation:
            classname: programy.utils.security.authorise.usergroupsauthorisor.BasicUserGroupAuthorisationService
            denied_srai: AUTHORISATION_FAILED
            usergroups: $BOT_ROOT/config/roles.yaml
```

Format of the roles file is as follows

```yaml
users:
  console:
    roles:
      user
    groups:
      sysadmin

groups:
  sysadmin:
    roles:
      root, admin, system
    groups:
      user

  user:
    roles:
      ask
```

To wrap an AIML grammar in authorisation, wrap the template in an 'authorise' tag, an example of which is shown below. Here if 'ALLOW ACCESS' is asked and the user does not have the 'root' role associated with them then grammar defined in denied_srai.

```xml
	<category>
		<pattern>ALLOW ACCESS</pattern>
		<template>
		    <authorise role="root">
				Access Allowed
			</authorise>
		</template>
	</category>
```

