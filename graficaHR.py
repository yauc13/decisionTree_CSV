import numpy as np
import matplotlib.pyplot as plt

x = np.linspace( 0, 2*np.pi, 100) #define el vector de datos
y = np.sin(x) #define un vector con los valores de la funcion sin(x)
z = np.cos(x)




lista = []


def iniciarArchivo():
    archivo = open("datasetclimanoche.csv","a")
    archivo.close()
    
def cargar():
    archivo = open("datasetclimanoche.csv","r")
    linea = archivo.readline()
    
    if linea:
        while linea:
            if linea[-1]=='\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()
    

def capturarValoresHR():
   
    listaA1 = lista #datos del archivo clasificacionAntrac (HR,TEMP, ANTRAC) consultados para ver si hay alerta
    
    valoresTemp = [] #valores de temperatura
    valoresIndice = []
    valoresHrMax = []
    valoresHrMin = []

    for elemento in listaA1:
        arreglo = elemento.split(",") # arreglo es una fila del archivo
        valoresTemp.append(arreglo[1]) # valoresA1 es una lista con los valores de ANTRAC de listaA1
        valoresIndice.append(listaA1.index(elemento))
        valoresHrMax.append(75)
        valoresHrMin.append(65)
    return valoresIndice, valoresTemp, valoresHrMax, valoresHrMin

iniciarArchivo()
cargar()
indice, hr, hrM, hrm= capturarValoresHR()

ejex = len(indice)
ejey = 100

plt.plot(indice,hr, 'b-', label= 'Humedad Relativa',linewidth=2) #grafica de x vs y, con linea de color azul 'b-'
plt.plot(indice,hrM, 'g-', label= 'HR max',linewidth=2)
plt.plot(indice,hrm, 'g-', label= 'HR min',linewidth=2)
plt.legend() #para mostrar las label o etiquetas de las graficas
plt.grid(True) #para mostrar la cuadricula
plt.axis([0,ejex,0,ejey]) #define unos espacios por arriba y debajo de la grafica
plt.title('Grafica Humedad Relativa') #titulo de la grafica
plt.xlabel('tiempo') # etiqueta de los valores en x
plt.ylabel('humedad Relativa')
plt.show() #muestra la grafica
