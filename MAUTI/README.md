# MAUTI

## Create Docker MAUTI

Make sure you are in this directory.

#### Create the program-y.tar.gz

```tar -czvf Docker/program-y.tar.gz program-y/```

#### Build the Docker Container

```run docker build -t czadikem/mauti-server -f Docker/Dockerfile .```

#### Start the Docker Container

```docker compose -f Docker/docker-compose.yml up -d```

## MIT APPInventor

My code is based off of these programs
Code examples from
https://community.appinventor.mit.edu/t/curl-to-blocks-automatic-generator/47888/2

https://getaix.com/curl-to-blocks

https://community.appinventor.mit.edu/t/disabling-error-notifications/7356/6

http://ai2.appinventor.mit.edu/reference/other/json-web-apis.html 

https://groups.google.com/g/mitappinventortest/c/JaB9odrAu_w?pli=1

http://ai2.appinventor.mit.edu/reference/components/connectivity.html#Web

https://www.bermotech.com/app-inventor-timer/