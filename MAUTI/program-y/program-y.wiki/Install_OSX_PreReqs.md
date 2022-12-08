# OSX Prerequisites

## Python3 and Pip3
OSX currently only ships with Python 2.x installed, and Programy was designed fo Python 3.x. Installation of Python 3 requires a little more care than most platforms but if you follow the next steps you should be fine.
This information was taken from [William Vicent's Blog](https://wsvincent.com/install-python3-mac/)

```bash
$ python --version Python 2.7.15.
$ xcode-select --install. 
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
$ brew doctor 
Your system is ready to brew. 
$ brew install python3. 
```

Now its successfully installed we should just do a final check to make sure its on the command line and
the right versions are available
```bash
$ python3 --version 
Python 3.7.0.
$ pip3 --version
pip 19.0.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
```

## Git
You now have all the requirements to install Programy

If you are going to only install programy via pip, then you are finished and don't need to worry about Git. If you are looking at downloading programy as a Git clone or looking to develop on the main code base then you will need to have Git installed.