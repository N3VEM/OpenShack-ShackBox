# OpenShack-ShackBox

In the N3VEM hamshack, the "shackBox" is the primary daily use shack computer.  Below are the packages and any pertinent installation notes. 


From a terminal always begin with
```
sudo apt update

sudo apt upgrage
```
## Ham Radio Specific

### TrustedQSL
For submitting logs to LOTW
```
sudo apt install trustedqsl
```

### CQRlog
I've used this logging program on Linux for a while now.  It seems to do most of what I want. There seem to be some dependancy things when installing on Linux Mint 20, but luckily PA1SBM has written up a little install script that handles it makes the install a snap.  First get the script from his [github page.](https://github.com/pa1sbm/LM20_CQRlog_Installer) After you've copied the .sh file to your home directory run this:
```
sudo sh ./LM20_CQRlog_Installer.sh
```

### fldigi
*The* program for basically all the digital modes that aren't wsjt or SSTV.
As a note, I use the hamlib option for rig control, NOT the flrig option that it tries to push you towards.
```
sudo apt install fldigi
```

### QSSTV
I don't do much SSTV stuff, but when I do, this is what I've used, mostly because it seems like pretty much the only option for linux.  I have no complaints about it though.
```
sudo apt install qsstv
```

### WSJTX
All the cool kids hang out on the digital modes this software was designed for (FT8, et. al.)
```
sudo apt install wsjtx
```

## Not Ham Radio Specific, but stuff I use on this machine.

### Barrier
I have multiple computers (not all for shack purposes) and use a 'software KVM' so that one mouse and keyboard can be used across all of them, like one large continuous desktop.
I currently use [Barrier](https://github.com/debauchee/barrier) for this purpose. Detailed information provided at the linked github repo for installation and setup.
```
sudo apt install barrier
```

### AWSCLI
I do some dabbling with AWS, so the AWS CLI is a must-have tool for some of the development work I do in AWS.
```
sudo apt install awscli
```

### MySQL Workbench
I like Workbench for working with MySQL databases.  It must be installed from .deb [downloadable here](https://dev.mysql.com/downloads/workbench/)

replace path and file name below with the path to your downloaded file, and its name.
```
sudo apt install ~/path/to/download/mysql-workbench-community_8.0.22-1ubuntu20.04_amd64.deb
```

### Brave Browser
I like this broswer.  Blocks adds and stupid stuff. Seems to run fast.
Directions for installing and setup [available here](https://brave.com/linux/#linux)

### Visual Studio Code
Because code.  Others reccomended installing directly from .deb provided by the vendor vs. using what's in the repo.
You can get the .deb [available here](https://code.visualstudio.com/)

I installed this package using the GUI gdebi package manager.

### Slack
This is becoming pretty common for communication amoung different groups.  We use it in POTA to keep in touch with other admins and participants.
Installed from .deb.  [Download here](https://slack.com/downloads/linux)

Installed with gdebi gui application.
