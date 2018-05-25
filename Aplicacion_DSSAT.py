# -*- coding: cp1252 -*-
from Tkinter import *

from time import gmtime, strftime
print strftime("%d %b %Y %H:%M:%S", gmtime())

lista = []


def iniciarArchivo():
    archivo = open("datasetclasificacion.csv","a")
    archivo.close()
def cargar():
    archivo = open("datasetclasificacion.csv","r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1]=='\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()

def consultarAlerta():
    r = Text(ventana, width=80, height=15)
    lista.sort()
    valores = []
    r.insert(INSERT, "Fecha\tAlerta\t\tRecomendacion\t\tAccion\n")
    for elemento in lista:
        arreglo = elemento.split(",")
        valores.append(arreglo[3])
        r.insert(INSERT, arreglo[0]+"\t"+arreglo[1]+"\t\t"+
        arreglo[2]+"\t\t"+arreglo[3]+"\t\n")
    r.place(x=300, y=80)

    r.config(state=DISABLED)

def consultarDatosClasificados():
    r = Text(ventana, width=80, height=15)
    #lista.sort()
    valores = []
    r.insert(INSERT, "HR\tTEMP\t\tANTRAC\t\tFECHA\n")
    for elemento in lista:
        arreglo = elemento.split(",")
        valores.append(arreglo[3])
        r.insert(INSERT, arreglo[0]+"\t"+arreglo[1]+"\t\t"+
        arreglo[2]+"\t\t"+arreglo[3]+"\t\n")
    r.place(x=300, y=80)

    r.config(state=DISABLED)


def actionButton_ver_temp():
    print ("buton1 pulsado")
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)

    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, 'o-')
    plt.title('A tale of 2 subplots')
    plt.ylabel('Damped oscillation')

    plt.subplot(2, 1, 2)
    plt.plot(x2, y2, '.-')
    plt.xlabel('time (s)')
    plt.ylabel('Undamped')

    plt.show()

def actionButton2():
    print ("buton2 pulsado")

def actionButtonSumar():
    suma = int(txtsum1.get())+int(txtsum2.get())
    print (suma)
    resulsum.set(suma)
    

ventana = Tk()
ventana.title("DSS Antracnosis")
ventana.geometry("1000x600")

etiqueta = Label(ventana, text="DSS Antracnosis",fg="Black", font=("Times New Roman",28))
etiqueta.pack()
label_Temp1 = Label(ventana, text="Temp:",fg="Black",font=("Times New Roman",20)).place(x=30,y=50)
label_Temp1 = Label(ventana, text="20",fg="green",font=("Times New Roman",20)).place(x=100,y=50)
label_Temp1 = Label(ventana, text=" C",fg="Black",font=("Times New Roman",20)).place(x=140,y=50)

label_HR1 = Label(ventana, text="HR:",fg="Black",font=("Times New Roman",20)).place(x=30,y=80)
label_HR1 = Label(ventana, text="80",fg="green",font=("Times New Roman",20)).place(x=100,y=80)
label_HR1 = Label(ventana, text=" %",fg="Black",font=("Times New Roman",20)).place(x=140,y=80)

label_Titulo_Alertas = Label(ventana, text="Alertas de Antracnosis",fg="black",font=("Times New Roman",15)).place(x=500,y=50)

button_ver_temp = Button(ventana, text="ver temp  ",fg="black", command=actionButton_ver_temp).place(x=30,y=150)
button_ver_temp = Button(ventana, text="ver HR     ",fg="black", command=actionButton2).place(x=30,y=180)
button_ver_temp = Button(ventana, text="ver Antrac",fg="black", command=actionButton2).place(x=30,y=210)
txtvar = StringVar()


iniciarArchivo()
cargar()
consultarDatosClasificados()


ventana.mainloop()
