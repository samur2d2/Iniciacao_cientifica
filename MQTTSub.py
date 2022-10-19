from paho.mqtt import client as mqtt_client
import time

brokerIp = "192.168.0.67"
portNum = 1883
KeepAliveBroker = 60
topicName = "mensagem" 
clientName = "sub"



def connect_mqtt(brokerIp, clientName, portNum):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    
    client.on_connect = on_connect
    client.connect(brokerIp, portNum)
    return client

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{topicName}` topic")
    
client = mqtt_client.Client(clientName)    
client = connect_mqtt(brokerIp, clientName, portNum)


def run():
    
    client.loop_start()
    client.subscribe("mensagem")
    client.on_message = on_message
    time.sleep(1)
    client.loop_stop()

while True:
    run()
    #time.sleep(1)