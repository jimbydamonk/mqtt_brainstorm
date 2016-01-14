from gevent import monkey
monkey.patch_all()

import argparse
import gevent
import time 
import uuid
import paho.mqtt.client as mqtt
import threading


class MQTTProducer(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.client = mqtt.Client()
        self.client.username_pw_set("admin", "admin")

        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish

        self.host = host
        self.port = port
        self.client.connect(self.host, self.port, 60)
        self.running = True

    def run(self):
        try:
            while self.running:
                self.client.loop_forever()
        except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
            print "\nKilling Thread..."
            self.running = False
        except StopIteration:
            self.client = None

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        if rc != 0:
            print("Unexpected disconnection.")
        self.publish_numbers(client, "readlist/mutations/1/1")

    def on_publish(self, client, userdata, mid):
        print "Published message (" + str(mid)+ ")( published @", time.time()
        self.publish_numbers(client, "readlist/mutations/1/1", mid)


    def publish_number(self, client, topic, counter=0):
        payload = "%s_%s" % (counter, str(uuid.uuid4()))
        rc, mid = client.publish(topic, payload=payload, qos=1)
        print "Sent message with ", payload, " and ", rc, mid

    def publish_numbers(self, client, topic, counter=0):
        gevent.spawn(self.publish_number, client, topic, counter)
        time.sleep(1.05)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='the mqtt broker host to connect to.')
    parser.add_argument('--port', help='the mqtt broker port to connect to.')

    args = parser.parse_args()
    return args

def main(args):

    producer = MQTTProducer(args.host, args.port)
    producer.start()

if __name__ == "__main__":
    main(parse_args())