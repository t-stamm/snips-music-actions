#!/usr/bin/env python2
 
import sys
import paho.mqtt.client as mqtt
from spotify_controller import SpotifyController

def intent_received(_self, hermes, intent_message):
    print('Intent {}'.format(intent_message.intent))
    
    for (slot_value, slot) in intent_message.slots.items():
        print('Slot {} -> \n\tRaw: {} \tValue: {}'.format(slot_value, slot[0].raw_value, slot[0].slot_value.value.value))

    hermes.publish_end_session(intent_message.session_id, None)
    
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("hermes/hotword/default/detected")
    # Subscribe to intent topic
    client.subscribe("hermes/intent/#")
        

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.topic == 'hermes/hotword/default/detected':
        print("Wakeword detected!")
    else:
        try:
            intent = msg.topic[((len(msg.topic) - msg.topic.index(":")) - 1) * -1:]
            print("Intent "+intent+" found.")
            if intent in actions:
                print("Running intent...")
                actions[intent](msg.payload)
        except:
            e = sys.exc_info()[0]
            print("Error while trying to invoke intent from topic '"+msg.topic+"': "+e)


spotify = SpotifyController()

actions = {"pause":  spotify.pause}
#, "restartPlaylist", "volume_down", "shuffleMode", "next", "volume_up", "repeatMode", "play", "addPlaylist", "playResource", "previous"]

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("raspberrypi", 1883, 60)

client.loop_forever()