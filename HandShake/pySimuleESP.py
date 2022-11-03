import time
import paho.mqtt.client as mqtt

broker = "192.168.0.67"
port = 1883
handShake = "pyCommands" #TOPICO QUE O PYTHON MAIN VAI DAR SUB
personalTopic = "1.0.0.0" #TOPICO QUE O PYTHON MAIN VAI DAR PUB
message = "message"
client_id = "1.0.0.0"
KeepAliveBroker = 60

lerDataLastData = "lastDataSaved.txt"

def on_connect(client, userdata, flags, rc):
    print("[STATUS] Connected to Broker.")
    publish(client, handShake, personalTopic)
    client.subscribe(personalTopic)

def on_message(client, userdata, msg):
    msgRecieved = str(msg.payload)
    print("Message from " + msg.topic + ": " + msgRecieved)

def publish(client, topicToSend, dataToSend):
    result = client.publish(topicToSend, dataToSend)
    status = result[0]
    if status == 0:
        print(f"Sent `{dataToSend}` to topic `{topicToSend}`")
    else:
        print(f"Failed to send message to topic {topicToSend}")

try:
    print("[STATUS] Starting MQTT...")
    client = mqtt.Client(client_id)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port, KeepAliveBroker)
    client.loop_start()
    while True:
        publish(client, message, "oi")
        time.sleep(1)
    
except:
    print("Error")