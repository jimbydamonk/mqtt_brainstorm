import paho.mqtt.client as mqtt
import argparse
import time
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    if rc != 0:
        print("Unexpected disconnection.")
    client.subscribe("readlist/mutations/1/1", qos=1)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("{topic} {body} @ {time}".format(
        topic=msg.topic,
        body=str(msg.payload), 
        time=time.time()
        ))

def main ():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='the mqtt broker host to connect to.')
    parser.add_argument('--port', help='the mqtt broker port to connect to.')

    args = parser.parse_args()

    client = mqtt.Client()
    client.username_pw_set("admin", "admin")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(args.host, args.port, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()