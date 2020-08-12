This is a power outage meter run on the Orange Pi Zero using the Armbian Buster 5.4 linux-based operating system. The code uses the pyA20 (https://pypi.python.org/pypi/pyA20) 
python libraries for programming the built in GPIO ports on the board. The code uses the paho mqtt (https://pypi.org/project/paho-mqtt/) python libraties for enabling 
communication with ThingSpeak (https://thingspeak.com/). Updates on the power status of the PA11 GPIO port are sent to ThingSpeak in periodic intervals and whenever the power 
status of PA11 changes. Your information first goes to your channel on ThingSpeak. This uses the Rich Voltage channel. To send an email there is MatLab code in ThinkSpeak's 
analysis app. This code sends an email from ThinkSpeak. The ThinkSpeak react app is set to call the aforementioned MatLab code when certain criteria are met. In this case, voltage 
goes high or low, depending on the situation.

Installing Hardware: Look at attached GPIO Reference and circuit diagram for reference. The circuit diagram shows right after the power is off. On the Orange Pi Zero, PA11 is 
noramlly high (3.3V). When PA11 is connected to the Pi's ground, PA11 goes low (0V). I connected the Pi's ground to common on the relay, and PA11 to normally closed on the relay. 
This means that PA11 is shorted to ground when power is lost, and thus goes low. Building the circuit should be as simple as looking at the reference images and recreating that. 
Note that you could also make the same circuit with other GPIO ports. If you choose to change the GPIO port, make sure that the port starts high and change the python code to work 
with the new port.

Installing Code: 1.) Install Armbian Buster 5.4 onto Orange Pi Zero. 2.) Connect to Pi via serial using PuTTY. Run hostname -I command. This shows you IP addres of Pi. Reconnect 
to Pi via SSH on PuTTY using this IP address. Note that the Pi receives power via micro usb, so the micro usb must still be plugged in somewhere. 3.) Clone and commit the files 
from this github onto the Pi. 4.) Install python 2.7.16 5.) Do command: pip install pyA20. 6.) Do command: pip install paho-mqtt 7.) Do command: sudo su. You are now root user. Do 
command: crontab -e. At bottom of document, enter "@reboot sleep 90 && python /home/daniel/sensor/program/VoltageSensor.py &" without quatation marks. This starts VoltageSensor.py 
every time the pi turns on. Note that you must enter this reboot command in the sudo crontab. If you don't change to root user before entering crontab, then your command won't 
launch on the pi without you logging into it. That means if the power goes out, it won't be able to reboot itself back to full operation. 8.) Do command: shutdown -h now. This 
turns off Pi. Unplug Pi, wait a few seconds, then plug it back in. The Pi should turn back on and start running the VoltageSensor program. If that is the case, then ThinkSpeak 
should show a new entry in Rich Voltage. You are now done with code installation.    
