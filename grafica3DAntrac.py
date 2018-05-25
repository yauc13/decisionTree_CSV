from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import random

fig = plt.figure()
ax = fig.gca(projection='3d')

lista = []


def iniciarArchivo():
    archivo = open("COND_ANTRAC_J48 numero.csv","a")
    archivo.close()
    
def cargar():
    archivo = open("COND_ANTRAC_J48 numero.csv","r")
    linea = archivo.readline()
    
    if linea:
        while linea:
            if linea[-1]=='\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()
    
def capturarValoresAntrac():
   
    listaA1 = lista #datos del archivo clasificacionAntrac (HR,TEMP, ANTRAC) consultados para ver si hay alerta
    
    valoresTemp = [] #valores de temperatura
    valoresHR = []
    valoresAntrac = []
    

    for elemento in listaA1:
        arreglo = elemento.split(",") # arreglo es una fila del archivo
        valoresTemp.append(int(arreglo[1])) # valoresTemp es una lista con los valores de ANTRAC de listaA1
        valoresHR.append(int(arreglo[0])) #el int() es para transformar a entero, para posteriormente graficar
        valoresAntrac.append(int(arreglo[2]))
        
    return valoresHR, valoresTemp, valoresAntrac

def capturarValoresAntracA0():
   
    listaA1 = lista #datos del archivo clasificacionAntrac (HR,TEMP, ANTRAC) consultados para ver si hay alerta
    
    valoresTemp = [] #valores de temperatura
    valoresHR = []
    valoresAntrac = []
    

    for elemento in listaA1:
        arreglo = elemento.split(",") # arreglo es una fila del archivo
        if arreglo[2] == '0':               
            valoresTemp.append(int(arreglo[1])) # valoresTemp es una lista con los valores de ANTRAC de listaA1
            valoresHR.append(int(arreglo[0])) #el int() es para transformar a entero, para posteriormente graficar
            valoresAntrac.append(int(arreglo[2]))
        
    return valoresHR, valoresTemp, valoresAntrac

def capturarValoresAntracA1():
   
    listaA1 = lista #datos del archivo clasificacionAntrac (HR,TEMP, ANTRAC) consultados para ver si hay alerta
    
    valoresTemp = [] #valores de temperatura
    valoresHR = []
    valoresAntrac = []
    

    for elemento in listaA1:
        arreglo = elemento.split(",") # arreglo es una fila del archivo
        if arreglo[2] == '1':               
            valoresTemp.append(int(arreglo[1])) # valoresTemp es una lista con los valores de ANTRAC de listaA1
            valoresHR.append(int(arreglo[0])) #el int() es para transformar a entero, para posteriormente graficar
            valoresAntrac.append(int(arreglo[2]))
        
    return valoresHR, valoresTemp, valoresAntrac


def capturarValoresAntracA2():
   
    listaA1 = lista #datos del archivo clasificacionAntrac (HR,TEMP, ANTRAC) consultados para ver si hay alerta
    
    valoresTemp = [] #valores de temperatura
    valoresHR = []
    valoresAntrac = []
    

    for elemento in listaA1:
        arreglo = elemento.split(",") # arreglo es una fila del archivo
        if arreglo[2] == '2':               
            valoresTemp.append(int(arreglo[1])) # valoresTemp es una lista con los valores de ANTRAC de listaA1
            valoresHR.append(int(arreglo[0])) #el int() es para transformar a entero, para posteriormente graficar
            valoresAntrac.append(int(arreglo[2]))
        
    return valoresHR, valoresTemp, valoresAntrac


def capturarValoresAntracA3():
   
    listaA1 = lista #datos del archivo clasificacionAntrac (HR,TEMP, ANTRAC) consultados para ver si hay alerta
    
    valoresTemp = [] #valores de temperatura
    valoresHR = []
    valoresAntrac = []
    

    for elemento in listaA1:
        arreglo = elemento.split(",") # arreglo es una fila del archivo
        if arreglo[2] == '3':               
            valoresTemp.append(int(arreglo[1])) # valoresTemp es una lista con los valores de ANTRAC de listaA1
            valoresHR.append(int(arreglo[0])) #el int() es para transformar a entero, para posteriormente graficar
            valoresAntrac.append(int(arreglo[2]))
        
    return valoresHR, valoresTemp, valoresAntrac


iniciarArchivo()
cargar()

listaHR, listaTEMP, listaANTRAC  = capturarValoresAntracA3() 
x = listaHR
y = listaTEMP
z = listaANTRAC
print x
print y
print z
ax.scatter(x, y, z, zdir='z', c='red', label='A3')

listaHR, listaTEMP, listaANTRAC  = capturarValoresAntracA2() 
x = listaHR
y = listaTEMP
z = listaANTRAC
print x
print y
print z
ax.scatter(x, y, z, zdir='z', c='orange', label='A2')

listaHR, listaTEMP, listaANTRAC  = capturarValoresAntracA1() 
x = listaHR
y = listaTEMP
z = listaANTRAC
print x
print y
print z
ax.scatter(x, y, z, zdir='z', c='yellow', label='A1')

listaHR, listaTEMP, listaANTRAC  = capturarValoresAntracA0() 
x = listaHR
y = listaTEMP
z = listaANTRAC
print x
print y
print z
ax.scatter(x, y, z, zdir='z', c='green', label='A0')

ax.legend()
ax.set_xlim(0, 100) #dibuja los limites max y min
ax.set_ylim(0, 40)
ax.set_zlim(0, 3)
ax.set_xlabel('HR')
ax.set_ylabel('TEMP')
ax.set_zlabel('ANTRAC')
print 'graficar'

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20., azim=-35)

plt.show()
