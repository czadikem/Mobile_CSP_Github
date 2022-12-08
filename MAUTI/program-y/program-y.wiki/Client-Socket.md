The socket client provides a quick and easy way to call a Program-Y server via raw TCP sockets. The bot client exposes a single TCP socket that you can then send a json payload over and receive a json payload back

To configure the client, use the following configuration items in config.yaml
```yaml
socket:
  host: 127.0.0.1
  port: 9999
  queue: 5
  max_buffer: 1024
  debug: true
```
queue, max_buffer and debug are optional and control the number of socket readers, the size of the socket buffer and whether the client runs in debug mode or not respectively.

To run the Facebook client, you can use the shell script in Y-Bot scripts folder
```bash
./y-bot-socket.sh
```

Or you can use the command line 
```bash
python3 -m programy.clients.events.tcpsocket.client --config <PATH TO CONFIG> --cformat yaml --logging <PATH TO LOGGING>
```

To help with testing, or even developing your own client to the bot client, in programy\src\utils\socket_client there is a python script for calling the socket client, the code is
```python
# client.py
import socket
import sys
import json

host =      sys.argv[1]
port =      int(sys.argv[2])
question =  sys.argv[3]
clientid =  sys.argv[4]
max_size =  1024
if len(sys.argv) == 6:
    max_size = sys.argv[5]

payload = {"question": question, "clientid": clientid}
json_data = json.dumps(payload)

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection to hostname on the port.
s.connect((host, port))

s.send(json_data.encode('utf-8'))

# Receive no more than 1024 bytes
received = s.recv(max_size)

s.close()

json_data = json.loads(received.decode('utf-8'))

print("Answer: %s" % json_data['answer'])
```
You can call it with the following script
```bash
#!/usr/bin/env bash
python3 socket_client.py 127.0.0.1 9999 hello 123456789
```
The parameters to the python script are ip address, port, message and clientid respectively.