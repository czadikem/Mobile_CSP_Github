# REST Client Configuration

In addition to the [common configuration items](./Config_Client) available to all clients, the additional configuration 
items available to any REST based client are as follows

```yaml
rest:
  host: 127.0.0.1
  port: 5000
  debug: false
  workers: 4
  use_api_keys: false
  api_key_file: apikeys.txt
```
* **host** - The IP or DNS  name of the server hosting your web chat client
* **port** - The port number the server is running on
* **debug** - Whether to run the REST server in debug mode. This enables debug features of the underlying Flask or Sanic framework
* **workers** - The numnber of works to create if using the Sanic framework 
* **use_api_keys** - Use API Keys to secure the API Client. Requires API to be included in the API Call
* **api_keys_file** - The list of API Keys to load