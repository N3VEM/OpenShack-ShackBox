##FTDX3000 Serial Ports

A frustration point I noticed with my FDTX3000 was the fact that if I fully powered the rig on and off, it wouldn't always
present it's two serial ports to the PC in the same order. This meant that 50% of the time I powered up, I had to go back into
all the radio software and 're-tell' it what serial ports to use.  

The FTDX3000 actaully uses 2 usb serial devices on one connection - essentially one for data and one for ptt.  The show up in the
system with 2 main differenes in their attributes, one is an "Enhanced Com Port" and one is a "Standard Com Port"

We can use these two attributes to create symlinks, so that instead of referring to our ports by dev/ttyUSB0 and dev/ttyUSB1 (which might change),
we can give them permantent names, using udev rules.

If you want to go all the way down the rabbit hole, here is the [red pill](http://www.reactivated.net/writing_udev_rules.html) that will take you down 
the full path of creating udev rules.

The Blue Pill version is here if you want to just duplicate this for an FTDX3000:

```
sudo touch /etc/udev/rules.d/99-usb-serial.rules

sudo nano /etc/udev/rules.d/99-usb-serial.rules
```

in the file, put these lines:

```
KERNEL=="ttyUSB*", ATTRS{interface}=="Enhanced Com Port", SYMLINK+="ftdx3000data"
KERNEL=="ttyUSB*", ATTRS{interface}=="Standard Com Port",  SYMLINK+="ftdx3000ptt"
```
save and exit.

Plug in the USB cable to the rig if you havn't already, then run this:

```
sudo udevadm control --reload-rules && udevadm trigger
```
now if at the terminal you type
```
ls /dev
```
you should see your newly created symlinks in the list of devices (ftdx3000data and ftdx3000ptt).
This also means that in software like fldigi etc. where it asks for the serial port of your device, you can enter /dev/ftdx3000data and never have to mess with it again.



