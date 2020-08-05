import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt.thingspeak.com",1883,60)

channelId = "1112212"         # Put your channel ID here,i.e.. the number from the URL, https://thingspeak.com/channels/285697
apiKey = "AZP2G6XY3CKLAYFC"  # Put the API key here (the Write API Key from the API Keys tab in ThingSpeak)

client.publish("channels/%s/publish/%s" % (channelId,apiKey), "field1=26&field2=1013")
client.loop(2)
