from tkinter import *
import matplotlib.pyplot as plotter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.animation import FuncAnimation


interface=Tk()
interface.title("Interface Iniciação Científica")
interface['bg']="#C6DEFF"
#interface.resizable(False, False)

lerDadosPID = "dadosPID_23102022.txt"
lerDadosSET = "dadosSET_23102022.txt"

def Grafico ():
    fig, ax = plotter.subplots()
    canvas = FigureCanvasTkAgg(fig, master = interface) 
    def animar(i):
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

        if int(limSupSec) >= 20:
            limInfMin = limSupMin
            if int(limSupSec) < 30:
                limInfSec = str("0"+str(int(limSupSec)-20))
            else:
                limInfSec = str(int(limSupSec)-20)

        else:
            limSupMin = "00"
            limSupSec = "20"
            limInfMin = "00"
            limInfSec = "00"
        
        plotter.xlim(limInfMin+":"+limInfSec, limSupMin+":"+limSupSec)
    ani = FuncAnimation(fig, animar, interval = 500)
    canvas.get_tk_widget().place(x=150,y=80)
    canvas.draw()
Grafico()

def disable_entry():
    if value.get() == True:
        entry.config(state= "disabled")
    else:
        entry.config(state= "normal")

entry=Entry(interface, width= 40, font= ('Helvetica 16'))
entry.pack(pady=20)

value=BooleanVar()
button=Checkbutton(interface, text="Disable Entry", variable=value, command=disable_entry)
button.pack()


def Dimensao_tela():
    largura=800
    altura=600

    largura_tela=interface.winfo_screenwidth()
    altura_tela=interface.winfo_screenheight()

    posx=largura_tela/2 - largura/2
    posy=altura_tela/2 - altura/2

    interface.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
Dimensao_tela()


interface.mainloop()