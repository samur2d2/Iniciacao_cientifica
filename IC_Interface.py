from cgitb import text
from tkinter import *
from turtle import screensize
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

#inserir Label mostrando os valores dos ganhos. Atentar-se ás posições dos painéis na tela
#INSERIR CHECK BOX PARA SELECIONAR MALHA FECHADA OU MALHA ABERTA
#EM MALHA FECHADA, OS CONTROLADORES ENTRARÃO EM AÇÃO
#INSERIR BOTAO "TROCAR PARAMETROS" --> ABRE OUTRA TELA PERMITINDO O USUÁRIO EDITAR OS GANHOS --> BOTAO APPLY E TROCAR OS NUMEROS
#PESQUISAR COMO INSERIR GRÁFICOS EM TKINTER
#def TrocaParametro():

interface=Tk()
interface.title("Interface Iniciação Científica")
interface['bg']="#C6DEFF"
interface.resizable(False, False)

def CheckBox():
    var1=IntVar()
    var2=IntVar()

    CheckMA = Checkbutton(interface, text='Malha Aberta',variable=var1, onvalue=1, offvalue=0, command=var1).place(x=300,y=10)
    CheckMF = Checkbutton(interface, text='Malha Fechada',variable=var2, onvalue=1, offvalue=0, command="print_selection").place(x=410,y=10)
CheckBox()

def Grafico ():
    fig=Figure(figsize=(4,4),dpi=100)
    
    y=[i**(1/2) for i in range(50)]

    plot1 = fig.add_subplot(111)
    plot1.plot(y)

    canvas = FigureCanvasTkAgg(fig, master = interface)  
    canvas.draw()

    canvas.get_tk_widget().place(x=300,y=80)
    #toolbar = NavigationToolbar2Tk(canvas,interface)
    #toolbar.update()
Grafico()


def Dimensao_tela():
    largura=800
    altura=600

    largura_tela=interface.winfo_screenwidth()
    altura_tela=interface.winfo_screenheight()

    posx=largura_tela/2 - largura/2
    posy=altura_tela/2 - altura/2

    interface.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
Dimensao_tela()

def Descricoes():
    Ganho_P=Label(interface, text="Ganho Proporcional do Controlador", bg="#FFFFCC", fg="#0C090A", font="Calibri").place(x=10,y=10)
    Ganho_I=Label(interface, text="Ganho Integral do Controlador", bg="#FFFFCC", fg="#0C090A", font="Calibri").place(x=10,y=70)
    Ganho_D=Label(interface, text="Ganho Derivativo do Controlador", bg="#FFFFCC", fg="#0C090A", font="Calibri").place(x=10,y=130)
    Setpoint=Label(interface,text="Setpoint", bg="#FFFFCC", fg="#0C090A", font="Calibri").place(x=10,y=190)
    Velocidade=Label(interface, text="Velocidade de Rotação", bg="#FFFFCC", fg="#0C090A", font="Calibri").place(x=10,y=250)
Descricoes()

def Inputs ():
    velocidade=StringVar()
    
    Input_Ganho_P=Entry(interface, font="Calibri", bg="White").place(x=10, y=40)
    Input_Ganho_I=Entry(interface, font="Calibri", bg="White").place(x=10, y=100)
    Input_Ganho_D=Entry(interface, font="Calibri", bg="White").place(x=10, y=160)
    input_Setpoint=Entry(interface, font="Calibri", bg="White").place(x=10, y=220)
    Input_Velocidade=Entry(interface,font="Calibri",bg="White", textvariable=velocidade).place(x=10,y=280)

Inputs()

def Botoes():
    BotaoAplicar=Button(interface, text="Aplicar", font="Calibri", command="refresh").place(x=50,y=320)
    BotaoSair=Button(interface, text="Sair", font="Calibri", command="exit").place(x=10,y=320)
Botoes()


interface.mainloop()