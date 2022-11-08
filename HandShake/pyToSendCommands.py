import paho.mqtt.client as mqtt
from datetime import datetime
import returnBrokerIP as IP
import threading
import time

broker = IP.getIP()
port = 1883
commands = "pyCommands" 
client_id = "pyCommandsClient"
KeepAliveBroker = 60

respondeu = [False]

def on_connect(client, userdata, flags, rc):
    print("[STATUS] Connected to Broker.")
    client.subscribe(commands)

def on_message(client, userdata, msg):
    msgRecieved = str(msg.payload)[2:-1]
    IPSender, mensagem = msgRecieved.split("/")
    
    if mensagem == "ping":
        client.publish(IPSender, "reping")
        respondeu[0] = True
    else:
        print("Time elapsed: "+mensagem)

def publish(client, ipToReply, dataToReply):
    client.publish(ipToReply, dataToReply)

def Ping():
    while True:
        text = input()
        if text[0:4] == "ping":
            command, ip = text.split(" ")
            for i in range(4):
                respondeu[0] = False
                result = client.publish(ip, command)[0]
                if result == 0:
                    print("Sending a package to "+ip+"... ", end="")
                else:
                    print("Fail to communicate with the broker")
                time.sleep(2)
                if respondeu[0] == False:
                    print("Timeout.")
                    
            print("Test ended.")
        else:
            now = str(datetime.now())
            day, hour = now.split(" ")
            hourSent=hour[0: 8]
            day=day.replace("-", "_")
            ip, command = text.split(" ")
            parameter, value = command.split("=")
            result = client.publish(ip, parameter+"/"+day+"/"+hourSent+"/"+value)[0]
            if result == 0:
                print("Sent "+command+" to "+ip+".")
            else:
                print("Fail to communicate with the broker")
                

try:
    print("[STATUS] Starting MQTT...")
    client = mqtt.Client(client_id)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port, KeepAliveBroker)
    threading.Thread(target=Ping).start()
    client.loop_forever()
    
except:
    print("Error")