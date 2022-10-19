from cgitb import text
from tkinter import *
from tkinter import ttk
from MQTT_pub import *


color1 = "#C6DEFF"


app = Tk()
app.title("App")
app.geometry("680x520")

nb=ttk.Notebook(app)
nb.place(x=0, y=0, width=680, height=520)

abaConectar = Frame(nb, bg=color1)
abaDefinicoes = Frame(nb, bg=color1)
abaconfigurarMqtt = Frame(nb, bg=color1)

nb.add(abaConectar, text = "Conectar")
nb.add(abaDefinicoes, text = "Definicoes")
nb.add(abaconfigurarMqtt, text = "Configs")

#===========================================MENU CONECTAR
def Enviar():
    Sent("oi", str(ipNum.get()), int(portNum.get()), str(topicName.get()), str(clientPubName.get()))

botaoSend = Button(abaConectar, text="Enviar", command=Enviar).place(x=50, y=50)

#===========================================MENU DEFINICOES





#===========================================MENU CONFIGS
ipNum=StringVar()
ipNum.set("192.168.0.67")
objIpPosX, objIpPosY = 20, 10
labelIP = Label(abaconfigurarMqtt, text="IP:", font="Calibri", bg=color1).place(x=objIpPosX, y=objIpPosY)
entryIP = Entry(abaconfigurarMqtt, width=15, textvariable=ipNum).place(x=objIpPosX, y=objIpPosY+25)

portNum=StringVar()
portNum.set(1883)
objPortPosX, objPortPosY = 150, 10
labelPorta = Label(abaconfigurarMqtt, text="Porta:", font="Calibri", bg=color1).place(x=objPortPosX, y=objPortPosY)
entryPorta = Entry(abaconfigurarMqtt, textvariable=portNum, width=10).place(x=objPortPosX, y=objPortPosY+25)

clientSubName=StringVar()
clientSubName.set("sampepePub")
objPubPosX, objPubPosY = 20, 80
labelClientPub = Label(abaconfigurarMqtt, text="Client Publisher:", font="Calibri", bg=color1).place(x=objPubPosX, y=objPubPosY)
entryClientPub = Entry(abaconfigurarMqtt, width=20, textvariable=clientSubName).place(x=objPubPosX, y=objPubPosY+25)

clientPubName=StringVar()
clientPubName.set("sampepeSub")
objSubPosX, objSubPosY = 20, 130
labelClientSub = Label(abaconfigurarMqtt, text="Client Subscriber:", font="Calibri", bg=color1).place(x=objSubPosX, y=objSubPosY)
entryClientSub = Entry(abaconfigurarMqtt, width=20, textvariable=clientPubName).place(x=objSubPosX, y=objSubPosY+25)

topicName=StringVar()
topicName.set("mensagem")
objTopicPosX, objTopicPosY = 20, 200
labelTopic = Label(abaconfigurarMqtt, text="Tópico:", font="Calibri", bg=color1).place(x=objTopicPosX, y=200)
entryTopic = Entry(abaconfigurarMqtt, width=20, textvariable=topicName).place(x=objTopicPosX, y=objTopicPosY+25)

app.mainloop()