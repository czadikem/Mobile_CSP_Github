# Running on AWS Lightsail Instance

This example is specific to setting up Program-y as a multi client platform using AWS Lightsail instance. 
It introduces a number concepts for building a scalable Bot platform that supports all available client types

* **REST Service.** The primary bot exposes itself as a REST Service. This bot contains all of the categories that the bot will use to converse.
* **Micro Services.** Each client runs as its own micro service thus distributing load as evenly as possible.
* **SRAIX**. All bots other than the primary REST service use SRAIX to call the REST Service. Each bot has a simple `<pattern>*</pattern` grammar which will capture all input and direct to the REST service.

This example uses very specific configuration to get everything up and running and does not provide a generic solution to
building a Cloud based service. Instead it uses the following

* **AWS Lightsail.** A cheap version of AWS EC2 Server. 
* **Ubuntiu 18.04**. Long Term Support (LTS) Server version of this Linux distribution
* **Nginx.** The web server which handles all initial upfront web and REST calls where required
* **systemctl.** A systemd utility which is responsible for Controlling the systemd system and service manager. To allow you services to run without being logged in they need to run as daemons, and I use systemctl to manageme them

# Amazon Lightsail

So let start by creating a AWS Lightsail instance, head over to https://aws.amazon.com/console/ and either login or register for an AWS account and then login

In the 'Build a solution' selection, click 'Build using virtual servers with Lightsail', alternatively you can go directly via the following link
https://lightsail.aws.amazon.com/ls/webapp/create/instance

* From 'Select a Platform' choose 'Linux/Unix'
* From 'Select a blueprint' choose 'OS only' and then 'Ubuntu 18.04 LTS'
* Select the price point server, for a full Program-y install I recommend the '$20' option which gives, 4GB, 2 vCPUs, 80GB Storage and 4TB Transfer. The biggest 2 impacts are the size of you grammar and the number of questions, but for now lets stick with this as a cood compromise of value vs performance.
* Click 'Create instance' and then wait a few moments for the magic at Amazon to happen.

If you want a static IP address to make configuration with the outside world easier then you will need to following these additional steps

* Click 'Home'
* Click 'Networking'
* Click 'Create static IP'
* Give it a name
* Click 'Create'
* Attach the IP to the Lightsail instance you created above

You now have a basic Ubuntu Linux instance running in the cloud with a static IP address you can use directly in your
code, or configure DNS to map this to a domain name. You can now log in to the instance using SSH and begin configuring the server.

* Click 'Home'
* Either 
  * Click the symbol >_
* Or 
  * Click the name of your instance
  * Click 'Connect using SSH'
   
A console window should show shortly and log you in directly as 'ubuntu' user. You are now ready to use your instance

## Install Nginx
Make sure repo is up to date
```bash
> sudo apt-get update
```

No we install a web server NGinx
```bash
> sudo apt-get install nginx
```

Next we can check it is working by using the the IP address we created above, head to http://IP-ADDRESS and you should 
see the Nginx home page which should look similar to 

[[images/lightsail/lightsail-nginx.png]]

### Install Free SSL Certification
Now lets set up SSL support using certbot. For full documentation of this process see https://certbot.eff.org/. 
However the following steps will get you up and running with full SSL protection.

At this point, you should have decided what you domain name and mapped it to the static ip address in the above process.
For the rest of this demo will will be using 'servus.ai' which is the domain name I use for all cloud testing.

In the steps below we first add the certbot repo to our apt-get repository, then install certbot, run the configuration process to 
generate and install SSL certificates into our website, and then reload nginx to pick up the changes we make.

During setup make sure you select the option to default all HTTP traffic ( Port 80 ) to HTTPS ( Port 43 )

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-nginx

sudo certbot --nginx

sudo nginx -s reload
```

The final step is to use the AWS Console to enable SSL Port 443 in the firewall

* Click 'Home'
* Click 'Instances'
* Click the name of you instance
* Click 'Networking'
* In the 'Firewall' section, click the '+ Add another'
* Select 'HTTPS' in the Application box, the port should default to 443
* Click 'Save'

Again we can now test the configuration by using  both HTTP and HTTPS versions of our URL, 

* http://IP-ADDRESS
* https://IP-ADDRESS

Both should direct to the HTTPS version and again show the Nginx home page as above

## Things to remember

* `/etc/nginx/sites-enabled/default` The path where nginx stores all host configuration files
* `/etc/letsencrypt/live/servus.ai/fullchain.pem` Location of your SSL Certification 
* `/etc/letsencrypt/live/servus.ai/privkey.pem` Location of your SSL Private Key

## Installing Python 3

Now we have a web server up, running and secure we can set about installing the neccassary requirements
to run Program-y. This starts with install Python 3.
```bash
> sudo apt-get install python3
``` 
Check the version of Python is 3.6 or above
```bash
> python3 —version
Python 3.6.7
```

Next we need to install Python 3 Pip

```bash
> sudo apt-get install python3-pip
```

## Install Program-y
Now we have out Python environment up and running, we can set about installing Program-y, download Y-Bot and Servusai-y

```bash
> sudo pip3 install programy

> sudo python3 -m programy.admin.tool install textblob

> sudo cd /opt
> sudo mkdir y-bot
> sudo cd y-bot
> sudo  python3 -m programy.admin.tool download y-bot
```

## Install Servusai-y
Servusai is the Program-y framework for building multi client environments and comes with most things configured
to get your core bot and multiple clients up and running

```bash
> sudo cd /opt
> sudo mkdir servusai-y
> sudo cd servusai-y
> sudo git init .
> sudo git remote add servusai-y https://github.com/keiffster/servusai-y
> sudo git pull servusai-y master

> sudo chown -hR ubuntu servusai-y
```
The last line is because we are doing everything as 'root' under sudo, but all of the apps run as ubuntu user

### Configure REST Service
We can first test the REST Service runs locally
```bash
> cd /opt/servusai-y/rest/scripts/xnix
> sudo ./rest.sh
```

Make sure its up and running on the right port as per config and you see this in the output when it starts up. 
Then Ctrl-C kill the server. We can now install the rest service

```bash 
> sudo ./install.sh
```

Now test its running on the local port with the following 

```bash
> sudo ./test-rest-local.sh
[{"response":{"answer":"Greetings!","question":"hello world","userid":"1234567890"}},200]
```

Next we need to configure nginx to port forward from our external port to out internal port
This means that the server is not exposed directly to the outside world, and nginx can take the load
Of handling multiple requests

```bash 
> cd ../../config/xnix
```

In here you will find rest.site which contains the config to run the rest server on a different port, but to then forward that port to the internal rest port

```bash
> sudo cp rest.site /etc/nginx/sites-enabled
```

Then we restart nginx to pick up the changes

```bash
> sudo service nginx restart
```

Now make sure you expose the port view the Lightsail firewall config

And then we can test it is running on the external port

```bash
> sudo ./test-rest-remote.sh
[{"response":{"answer":"Greetings!","question":"hello world","userid":"1234567890"}},200]
```

All our testing so far has been from the Lightsail instance, from the command line of your computer run the same 
command as in test-rest-remote.sh

```bash
>  curl 'https://servus.ai:9989/api/rest/v1.0/ask?question=hello+world&userid=1234567890'
[{"response":{"answer":"Hi there!","question":"hello world","userid":"1234567890"}},200]
```

### Configure Console Client
Once we have the REST up and running the quickest way to check everything is running is to use the Console Client
which in Servusai-y is configure to REST via SRAI to call the rest client.

```bash
> cd /opt/servusai-y/console
> ./console.sh
Loading, please wait...
/opt/servusai-y/console/scripts/xnix
No bot root argument set, defaulting to [../../config/xnix] hello, trying another path
Found a total of 0 errors in your grammars, check your errors storeonversation for client Console
Found a total of 0 duplicates in your grammars, check your duplicates storen = [*]
None, App: v1.0.0 Grammar v1.0.0, initiated March 14, 2017ern default to [*]
Hi, how can I help you today?matching sentence [], topic=[*], that=[*] 
>>> hello
Hiya!
```

### Configure WebChat Client
Now finally we can a Web Chat client up and running which uses the REST service for all its calls

```bash
> cd /opt/servusai-y/web/scripts/xnix
> sudo ./install.sh
```

Point your browser to http://servus.ai and the following window should be displayed allowing you to interact 
with the bot itself.

## Going Further

Now you have all the core components up and running, with defined clients and scripts to install and run all 
the other clients. Over the coming weeks we'll add instructions for just that. Enjoy

# Working with your Bot
You are now ready to start working your with bot. To do this, jump to the next page [You and Your Bot](./You_And_Your_Bot)


