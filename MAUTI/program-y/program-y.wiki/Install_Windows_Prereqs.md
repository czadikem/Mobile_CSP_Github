# Windows Prerequisites

## Python3 and Pip
This information pulled together from [Python Installation on Windows](https://docs.python.org/3/using/windows.html#windows-full). The installer for windows can be found at [Python Releases for Windows](https://www.python.org/downloads/windows/). Choose the latest stable version, which at this time is 3.7.2, and you are looking for the 'Download Windows x86 executable installer' link

Once downloaded, run the installer and you should see the following window

[[./windows/windows-install.png]]

After clicking the 2 checkboxes at the bottom, click 'Install Now' and follow the instructions. 

Python 3 should then be installed and added to your path. You can test this by opening command prompt, and running Python as follows to get the version

```cmd
python --version
Python 3.7.2
```

## Git
If you are going to only install programy via pip, then you are finished and don't need to worry about Git. If you are looking at downloading programy as a Git clone or looking to develop on the main code base then you will need to have Git installed.

Head over to [Git Downloads](https://git-scm.com/download/win), and then select either of the 2 installers
* 32-bit Git for Windows Setup.
* 64-bit Git for Windows Setup.

Run the installer and when its complete you can check Git is installed by typing git at the command line, as follows and you'll see something with the following first view lines.
```cmd
 git
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:
```
