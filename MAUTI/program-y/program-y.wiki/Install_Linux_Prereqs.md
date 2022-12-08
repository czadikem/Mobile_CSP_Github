# Linux Prerequisites

Before you install Programy on Ubuntu you need to check that you have the pre-requisites installed, 
named Python 3.x and Pip. Installation instructions for Ubuntu can be found in [Ubuntu Prerequisites](Install_Linux_PreReqs)

## Python3 and Pip3
Program-Y is written exclusively in Python 3.x so you are going to need this installed. It also uses a large number of external Python 3rd party libraries so you are also going to need Python 3 version of pip

On Ubuntu ( other Linux's exist ), the following should get you sorted

First make sure apt is up to date
```bash
keith@ubuntu:~$ sudo apt-get update
[sudo] password for keith: 
Hit:1 http://security.ubuntu.com/ubuntu bionic-security InRelease
Hit:2 http://us.archive.ubuntu.com/ubuntu bionic InRelease
Hit:3 http://us.archive.ubuntu.com/ubuntu bionic-updates InRelease
Hit:4 http://us.archive.ubuntu.com/ubuntu bionic-backports InRelease
Reading package lists... Done                      
keith@ubuntu:~$ 
```

Then install Python 3.x
```bash
keith@ubuntu:~$ sudo apt-get install python3
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libpython3-stdlib libpython3.6 libpython3.6-minimal libpython3.6-stdlib
  python3-minimal python3.6 python3.6-minimal
Suggested packages:
  python3-doc python3-tk python3-venv python3.6-venv python3.6-doc
  binfmt-support
The following packages will be upgraded:
  libpython3-stdlib libpython3.6 libpython3.6-minimal libpython3.6-stdlib
  python3 python3-minimal python3.6 python3.6-minimal
8 upgraded, 0 newly installed, 0 to remove and 400 not upgraded.
Need to get 0 B/5,536 kB of archives.
After this operation, 35.8 kB disk space will be freed.
Do you want to continue? [Y/n] y
```
Hit 'y' and let the installer finish

If you are to you use Python Virtual Environments, then we need to install that, otherwise skip to 
Pip3 section
```bash
keith@ubuntu:~/mybots$ sudo apt-get install python3-venv
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  python3.6-venv
The following NEW packages will be installed:
  python3-venv python3.6-venv
0 upgraded, 2 newly installed, 0 to remove and 391 not upgraded.
Need to get 7,392 B of archives.
After this operation, 44.0 kB of additional disk space will be used.
Do you want to continue? [Y/n] 
```
Hit 'Y' and let it complete

Now we are ready to install Python3 Pip
```bash
keith@ubuntu:~$ sudo apt-get install python3-pip
Reading package lists... Done
Building dependency tree       
Reading state information... Done
9 upgraded, 39 newly installed, 0 to remove and 391 not upgraded.
Need to get 74.6 MB/82.2 MB of archives.
After this operation, 201 MB of additional disk space will be used.
Do you want to continue? [Y/n] 
```
Again hit 'Y' and let the installer complete

Now it's successfully installed we should just do a final check to make sure its on the command line and
the right versions are available
```bash
keith@ubuntu:~$ python3 --version
Python 3.6.7
keith@ubuntu:~$ pip3 --version
pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
keith@ubuntu:~$ 
```
You now have all the requirements to install Programy

## Git
If you are going to only install programy via pip, then you are finished and don't need to worry about Git. If you are looking at downloading programy as a Git clone or looking to develop on the main code base then you will need to have Git installed.

```bash
keith@ubuntu:~$ sudo apt-get install git
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  git-man liberror-perl
Suggested packages:
  git-daemon-run | git-daemon-sysvinit git-doc git-el git-email git-gui gitk
  gitweb git-cvs git-mediawiki git-svn
The following NEW packages will be installed:
  git git-man liberror-perl
0 upgraded, 3 newly installed, 0 to remove and 391 not upgraded.
Need to get 4,733 kB of archives.
After this operation, 33.9 MB of additional disk space will be used.
Do you want to continue? [Y/n] 
```
As per the usual, hit 'Y' and let the installer complete, you now have git installed and ready to go