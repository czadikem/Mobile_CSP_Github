# Health Check  

All clients now ship with an optional Health Check service which runs as an additional REST endpoint on any RESTful 
client, or if not a RESTful client, it spins up a REST server to expose the endpoint

## Configuration
Without the following information the Healhcheck service does not start

```yaml
console:
  responder:
    name: Responder
    host: localhost
    port: 6666
    url: /api/console/v1.0/ping
    shutdown: /api/console/v1.0/shutdown
```

## Healthcheck Data

Querying the Healthcheck endpoint '/api/console/v1.0/ping' with something like Curl will return the following payload
of information about the Client and how it is operating

```json
{  
   "bots":[  
      {  
         "brains":[  
            {  
               "id":"brain",
               "questions":1
            }
         ],
         "id":"bot",
         "questions":0
      }
   ],
   "client":"Console",
   "logging":{  
      "criticals":0,
      "debugs":8334,
      "errors":51,
      "exceptions":0,
      "fatals":0,
      "infos":847,
      "warnings":441
   },
   "questions":0,
   "start_time":"2019-05-01 06:09:54.448213"
}
```

## Healthcheck UI

A future release will ship with a web based client that cna be used to visualise the data returned




