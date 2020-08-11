This is a power outage meter run on the Orange Pi Zero using the Armbian Buster 5.4 linux-based operating system. The code uses the pyA20 (https://pypi.python.org/pypi/pyA20) python libraries for programming the built in GPIO ports on the board. The code uses the paho mqtt (https://pypi.org/project/paho-mqtt/) python libraties for enabling communication with ThingSpeak. Updates on the power status of the PA11 GPIO port are sent to ThingSpeak in periodic intervals, and whenever the power status of PA11 changes. ThingSpeak process that information, and sends an email via it's "react" function to the email attached to the ThingSpeak account used by the ASF engineering group. 

Installing Hardware: 


Installing Code:
1.) Install Armbian Buster 5.4 onto Orange Pi Zero. 
2.) Connect to Pi via serial using PuTTY. Run hostname -I command. This shows you IP addres of Pi. Reconnect to Pi via SSH on PuTTY using this IP address.
3.) Clone and commit the files from this github onto the Pi. 
4.) Install python 2.7.16
5.) Do command: pip install pyA20.
6.) Do command: pip install paho-mqtt
7.) Do command: sudo su. You are now root user. Do command: crontab -e. At bottom of document, enter "@reboot sleep 90 && python /home/daniel/sensor/program/VoltageSensor.py &" without quatation marks. This starts VoltageSensor.py every time the pi turns on.
8.) Do command: shutdown -h now. This turns off Pi. Unplug Pi, wait a few seconds, then plug it back in. The Pi should turn back on and start running the VoltageSensor program. If that is the case, then ThinkSpeak should show a new entry in Rich Voltage. You are now done with code installation.




























