# OpenShack-ShackBox
Part of the larger OpenShack project, this repository focuses on custom code/scripts written to be used on a stations "daily use" (i.e. logging) machine.

In the N3VEM hamshack, this machine is running Debian 10.

In the N3VEM hamshack, the "shackBox" is the one the rig is connected to.  The server for remote access/control of the shack is a different machine.  Currently, for remote rig control, the rig connected to this machine needs to be accessible across the network, which I am currently doing using hamlib and its utility rigctld.

the manual for rigctld [is available here](http://hamlib.sourceforge.net/manuals/hamlib.html#Introduction-to-rigctld)

If you have programs like fldigi install, you may already have this.  If not, install hamlib and its utilities:
```
sudo apt install libhamlib2 libhamlib-utils
```

I run rigctld as a systemd service so it's always ready, and will reconnect automatically if it crashes, or if I power down the rig and power it back up.

Create a file with your rig paramters:
```
sudo nano /etc/rigctld.conf
```

enter the following into the file for an ftdx3000.  the numbers to use for model ID for different radios [is available here](https://github.com/Hamlib/Hamlib/wiki/Supported-Radios).  the "RIGDEVICEPATH" needs updated to the device that your rig is plugged into.  I created a symlink for my rig so that I could refer to it by name, even if the port changes for some reason.  Google should be able to help you figure out how to do that until I can document it, if you'd like to do the same.
```
MODELFLAG=-m
MODELID=132
RIGFILEFLAG=-r
RIGDEVICEPATH=/dev/ftdx3000data
```

create a systemd service file:
```
sudo nano /lib/systemd/system/rigctld.service
```

enter the following:
```
[Unit]
Description=hamlib rig contol server
After=multi-user.target
StartLimitIntervalSec=0

[Service]
User= #user name that you want the service to run under
Type=simple
Restart=always
RestartSec=1
EnvironmentFile=/etc/rigctld.conf
ExecStart=/usr/bin/rigctld $MODELFLAG $MODELID $RIGFILEFLAG $RIGDEVICEPATH

[Install]
WantedBy=multi-user.target
```

after you service file is created, enable it, and start it.  Afterwards, it should always run on boot.
```
sudo systemctl enable rigctld
sudo systemctl start rigctld
```
