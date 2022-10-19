from tkinter import *
from tkinter import ttk
from tkinter import messagebox


app = Tk()
app.title("App")
app.geometry("680x520")

nb=ttk.Notebook(app)
nb.place(x=0, y=0, width=680, height=520)

abaConectar = Frame(nb)
abaDefinirPortas = Frame(nb)

nb.add(abaConectar, text = "Conectar")
nb.add(abaDefinirPortas, text = "Definir portas")


labelKp=Label(abaDefinirPortas,text="Kp")
entryKp=Entry(abaDefinirPortas)


labelKi=Label(abaDefinirPortas,text="Ki")
entryKi=Entry(abaDefinirPortas)

labelKd=Label(abaDefinirPortas,text="Kd")
entryKd=Entry(abaDefinirPortas)


labelKp.place(x=50, y=15)
entryKp.place(x=50, y=30)

labelKi.place(x=150, y=15)
entryKi.place(x=150, y=30)

labelKd.place(x=250, y=15)
entryKd.place(x=250, y=30)



app.mainloop()