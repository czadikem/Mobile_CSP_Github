# Installation on Windows Using Pip

Before you install Programy on Ubuntu you need to check that you have the pre-requisites installed, 
named Python 3.x and Pip. Installation instructions for Windows can be found in [Windows Prerequisites](Install_Windows_PreReqs)

## Installation via Git
Once Git is installed we can download the latest and greatest code from Github
```bash
cd /opt
mkdir program-y
cd program-y
git init .
git remote add program-y https://github.com/keiffster/program-y
git pull program-y master
```
Next, we need Pip and the Python 3 version of it. Once this is installed we can install all of the necessary Python dependencies.
```bash
sudo apt-get install python3-pip
pip3 install --upgrade pip
pip3 install -r requirements.txt 
```
We can now install and configured all of the clients starting with the REST service.

# Working with your Bot
You are now ready to start working your with bot. To do this, jump to the next page [You and Your Bot](./You_And_Your_Bot)