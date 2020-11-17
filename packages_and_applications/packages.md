# OpenShack-ShackBox

In the N3VEM hamshack, the "shackBox" is the primary daily use shack computer.  Below are the packages and any pertinent installation notes. 


From a terminal always begin with
```
sudo apt update

sudo apt upgrage
```
## Ham Radio Specific
stuff goes here

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
I like this broswer.  Blocks add and stupid stuff. Seems to run fast.
Directions for installing and setup [available here](https://brave.com/linux/#linux)

