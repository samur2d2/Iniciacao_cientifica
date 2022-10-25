from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plotter
from tkinter import *
from tkinter import ttk
from MQTTPub import *
from MQTTSub import *


color1 = "#C6DEFF"

app = Tk()
app.title("App")
app.geometry("960x600")

nb=ttk.Notebook(app)
nb.place(x=0, y=0, width=960, height=600)

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



def Conectar():
    conectar(str(ipNum.get()), str(clientPubName.get()), int(portNum.get()))

botaoConectar = Button(abaConectar, text="Conectar", command=Conectar).place(x=50, y=100)


mensagem=StringVar()
labelSub = Label(abaConectar, text=str(mensagem.get()))
def Receber():
    run()

botaoReceber = Button(abaConectar, text="Receber", command=Receber).place(x=50, y=150)



lerDadosPID = "dadosPID_23102022.txt"
lerDadosSET = "dadosSET_23102022.txt"

def Grafico ():
    fig, ax = plotter.subplots()
    canvas = FigureCanvasTkAgg(fig, master = abaConectar) 
    def animar(i):
        Receber()
        xPID, yPID = [], []
        xSET, ySET = [], []

        with open(lerDadosPID, 'r') as fonte:
            dadosPID = fonte.read()
        for linha in dadosPID.split('\n'):
            if len(linha) == 0:
                continue
            for dadosLinha in linha.split('; '):
                xi, yi = dadosLinha.split(',')
                xPID.append(xi)
                try:
                    yPID.append(float(yi))
                except:
                    yPID.append(0)

        with open(lerDadosSET, 'r') as fonte:
            dadosSET = fonte.read()
        for linha in dadosSET.split('; '):
            if len(linha) == 0:
                continue
            xi, yi = linha.split(',')
            xSET.append(xi)
            try:
                ySET.append(float(yi))
            except:
                ySET.append(0)

        ax.clear()
        ax.plot(xSET,ySET)
        ax.plot(xPID,yPID) 
        
        for tick in ax.get_xticklabels(): 
            tick.set_rotation(90)

        last = open('dadosLAST.txt', 'r')
        lastWrite = last.read()
        last.close()
        limSupMin = lastWrite[0:2]
        limSupSec = lastWrite[3:5]
        limInfMin = ""
        limInfSec = ""

        if int(limSupSec) >= 30:
            limInfMin = limSupMin
            if int(limSupSec) < 40:
                limInfSec = str("0"+str(int(limSupSec)-30))
            else:
                limInfSec = str(int(limSupSec)-30)

        elif int(limSupMin) < 1:
            limInfMin = "00"
            limInfSec = "00"
        else:
            limInfMin = str("0"+str(int(limSupMin) - 1))
            diferenca = 30 - int(limSupSec)
            limInfSec = str(60 - diferenca)
        
        plotter.xlim(limInfMin+":"+limInfSec, limSupMin+":"+limSupSec)
    ani = FuncAnimation(fig, animar, interval = 500)
    canvas.get_tk_widget().place(x=250,y=50)
    canvas.draw()
Grafico()


#===========================================MENU DEFINICOES





#===========================================MENU CONFIGS
ipNum=StringVar()
ipNum.set("192.168.0.68")
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
