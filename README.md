This is a power outage meter run on the Orange Pi Zero using the Armbian Buster 5.4 linux-based operating system. The code uses the pyA20 (https://pypi.python.org/pypi/pyA20) python libraries for programming the built in GPIO ports on the board. The code uses the paho mqtt (https://pypi.org/project/paho-mqtt/) python libraties for enabling communication with ThingSpeak. Updates on the power status of the PA11 GPIO port are sent to ThingSpeak in periodic intervals, and whenever the power status of PA11 changes. ThingSpeak process that information, and sends an email via it's "react" function to the email attached to the ThingSpeak account used by the ASF engineering group. 

Installing:
1.) Install Armbian Buster 5.4 onto Orange Pi Zero. 
2.) Clone and commit the files from this github onto the Pi. 





























