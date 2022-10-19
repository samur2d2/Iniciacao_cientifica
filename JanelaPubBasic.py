#Precisa ter o codigo do MQTT_pub salvo e configurado
from tkinter import *
from tkinter import ttk
from MQTT_pub import *


app = Tk()
app.title("App")
app.geometry("680x520")

nb=ttk.Notebook(app)
nb.place(x=0, y=0, width=680, height=520)

abaConectar = Frame(nb)
abaDefinirPortas = Frame(nb)

nb.add(abaConectar, text = "Conectar")
nb.add(abaDefinirPortas, text = "Definir portas")


def Enviar():
    Sent("oi")

botaoSend = Button(abaConectar, text="Enviar", command=Enviar).place(x=50, y=50)


app.mainloop()