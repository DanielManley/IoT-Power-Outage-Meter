#Create sensor that uses orange pi zero and relay to sense voltage
#!/usr/bin/env python

import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')

import paho.mqtt.client as mqtt
import time
from pyA20.gpio import gpio
from pyA20.gpio import connector
from pyA20.gpio import port

client = mqtt.Client()
client.connect("mqtt.thingspeak.com",1883,60)
channelId = "1112212"  # Put your channel ID here
apiKey = "AZP2G6XY3CKLAYFC"  # Put the API write key here


GVEA = port.PA12 #set pin 12 to GVEA
gpio.init() #initiate GPIO usage
gpio.setcfg(GVEA,gpio.INPUT) #set GVEA to input

try:
    print ("Press CTRL+C to exit")
    while True:
        state = gpio.input(GVEA)      # Read button state
        print (state)
	time.sleep(2)
	client.publish("channels/%s/publish/%s" % (channelId,apiKey), "field1=/%s" % (state))


except KeyboardInterrupt:
    print ("Goodbye.")
