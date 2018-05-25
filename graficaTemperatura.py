import numpy as np
import matplotlib.pyplot as plt

x = np.linspace( 0, 2*np.pi, 100) #define el vector de datos
y = np.sin(x) #define un vector con los valores de la funcion sin(x)
z = np.cos(x)




lista = []


def iniciarArchivo():
    archivo = open("DATALOG_06_12_17_6PM_6AM.csv","a")
    archivo.close()
    
def cargar():
    archivo = open("DATALOG_06_12_17_6PM_6AM.csv","r")
    linea = archivo.readline()
    
    if linea:
        while linea:
            if linea[-1]=='\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()
    

def capturarValoresTemperatura():
   
    listaA1 = lista #datos del archivo clasificacionAntrac (HR,TEMP, ANTRAC) consultados para ver si hay alerta
    
    valoresTemp = [] #valores de temperatura
    valoresIndice = []
    valoresTempMax = []
    valoresTempMin = []

    for elemento in listaA1:
        arreglo = elemento.split(",") # arreglo es una fila del archivo
        valoresTemp.append(arreglo[2]) # valoresA1 es una lista con los valores de ANTRAC de listaA1
        valoresIndice.append(listaA1.index(elemento))
        valoresTempMax.append(26)
        valoresTempMin.append(22)
    return valoresIndice, valoresTemp, valoresTempMax, valoresTempMin

iniciarArchivo()
cargar()
indice, temp, tempM, tempm = capturarValoresTemperatura()

ejex = len(indice)
ejey = 40
plt.plot(indice,temp, 'b-', label= 'Temperatura',linewidth=2) #grafica de x vs y, con linea de color azul 'b-'
plt.plot(indice,tempM, 'g-', label= 'Temperatura max',linewidth=2)
plt.plot(indice,tempm, 'g-', label= 'Temperatura min',linewidth=2)
plt.legend() #para mostrar las label o etiquetas de las graficas
plt.grid(True) #para mostrar la cuadricula
plt.axis([0,ejex,0,ejey]) #define unos espacios por arriba y debajo de la grafica
plt.title('Grafica Temperatura') #titulo de la grafica
plt.xlabel('tiempo') # etiqueta de los valores en x
plt.ylabel('temperatura')
plt.show() #muestra la grafica
