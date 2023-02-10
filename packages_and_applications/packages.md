# OpenShack-ShackBox

In the N3VEM hamshack, the "shackBox" is the primary daily use shack computer.  Below are the packages and any pertinent installation notes. This isn't a compresensive list of everything installed, but it's the things I find most pertinent to my Ham Radio Hobby.


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
### GQRX
this is SDR software that can be used with dongles and such.  I've actually only fiddled with it a little bit with an RTD-SDR, but it's there.
```
sudo apt install gqrx-sdr
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

### Zoiper
I use this dabbling around with Allstar stuff sometimes.  It's softphone software that you can use to connect to allstar nodes.
I'd [head to their website for the latest.](https://www.zoiper.com/en/voip-softphone/download/current#linux)

## Not Ham Radio Specific, but stuff I use on this machine.
These are things that I use pretty often, that are regulalary ham radio adjacent.

### Arduino
Best bet is to go [their website](https://www.arduino.cc/) to get the latest and greatest.

### AWSCLI
I do some dabbling with AWS, so the AWS CLI is a must-have tool for some of the development work I do in AWS.
```
sudo apt install awscli
```

### git
For all the glory.
```
sudo apt install git-all
```

### MySQL Workbench
I like Workbench for working with MySQL databases.  It must be installed from .deb [downloadable here](https://dev.mysql.com/downloads/workbench/)

replace path and file name below with the path to your downloaded file, and its name.
```
sudo apt install ~/path/to/download/mysql-workbench-community_8.0.22-1ubuntu20.04_amd64.deb
```

### Visual Studio Code
Because code.  Others reccomended installing directly from .deb provided by the vendor vs. using what's in the repo.
You can get the .deb [available here](https://code.visualstudio.com/)

I installed this package using the GUI gdebi package manager.

### Slack
This is becoming pretty common for communication amoung different groups.  I used the most as a volunteer for POTA to keep in touch with other admins and participants.
Installed from .deb.  [Download here](https://slack.com/downloads/linux)

Installed with gdebi gui application.
