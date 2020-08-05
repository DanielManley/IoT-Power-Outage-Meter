#Create sensor that uses orange pi zero and relay to sense voltage
#!/usr/bin/env python

import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')

import time
from pyA20.gpio import gpio
from pyA20.gpio import connector
from pyA20.gpio import port

GVEA = port.PA12
#led = connector.gpio0p0     # This is the same as port.PH2
#button = connector.gpio3p40


gpio.init() #initiate GPIO usage


gpio.setcfg(GVEA,gpio.INPUT)
"""Set directions"""
#gpio.setcfg(led, gpio.OUTPUT)
#gpio.setcfg(button, gpio.INPUT)

"""Enable pullup resistor"""
#gpio.pullup(GVEA, gpio.PULLUP)
#gpio.pullup(button, gpio.PULLDOWN)     # Optionally you can use pull-down resistor

try:
    print ("Press CTRL+C to exit")
    while True:
        state = gpio.input(GVEA)      # Read button state
        print (state)
	time.sleep(2)
        """Since we use pull-up the logic will be inverted"""
        #gpio.output(led, not state)

except KeyboardInterrupt:
    print ("Goodbye.")
