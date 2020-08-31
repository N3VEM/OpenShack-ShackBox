#!/usr/bin/python
import time

#Started but never followed up on.  The intent was to turn on the logging feature in fldigi
#and then have this script that would read what gets logged (i.e. what gets recevied)
#with the idea that, via something like a serial connection and micro controller
#i could create an "external" receive device, like an old school dot matrix or rtty machine
#that would print out received text. Then by making a pseduo-keyboard interface, I could have something similar
#to send the keystrokes to fldigi for input, essentially building a "digital mode terminal" with a vintage feel

fileBytePos = 0
while True:
    inFile = open('../../.fldigi/fldigi20200830.log','r') #this would need updated with your path to the fldigi logs
    inFile.seek(fileBytePos)
    data = inFile.read()
    if (data):
        print (data)
    fileBytePos = inFile.tell()
    #print fileBytePos
    inFile.close()
    time.sleep(1)
