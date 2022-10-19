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
labelIP = Label(abaconfigurarMqtt, text="IP:", font="Calibri", bg=color1).place(x=20, y=10)
entryIP = Entry(abaconfigurarMqtt, width=15, textvariable=ipNum).place(x=20, y=35)

portNum=StringVar()
portNum.set(1883)
labelPorta = Label(abaconfigurarMqtt, text="Porta:", font="Calibri", bg=color1).place(x=150, y=10)
entryPorta = Entry(abaconfigurarMqtt, textvariable=portNum, width=10).place(x=150, y=35)

clientSubName=StringVar()
clientSubName.set("sampepePub")
labelClientPub = Label(abaconfigurarMqtt, text="Client Publisher:", font="Calibri", bg=color1).place(x=20, y=80)
entryClientPub = Entry(abaconfigurarMqtt, width=20, textvariable=clientSubName).place(x=20, y=105)

clientPubName=StringVar()
clientPubName.set("sampepeSub")
labelClientPub = Label(abaconfigurarMqtt, text="Client Subscriber:", font="Calibri", bg=color1).place(x=20, y=130)
entryClientPub = Entry(abaconfigurarMqtt, width=20, textvariable=clientPubName).place(x=20, y=155)

topicName=StringVar()
topicName.set("mensagem")
labelTopic = Label(abaconfigurarMqtt, text="Tópico:", font="Calibri", bg=color1).place(x=20, y=200)
entryTopic = Entry(abaconfigurarMqtt, width=20, textvariable=topicName).place(x=20, y=225)

app.mainloop()