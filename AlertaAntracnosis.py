#tomando como referencia el archivo de la clasificacion
#del nivel de antracnosis, se genera las alertas.
#
import time
from time import gmtime, strftime

lista = []

def iniciarArchivo():
    archivo = open("clasificacionAntrac.csv","a")
    archivo.close()
    
def cargar():
    archivo = open("clasificacionAntrac.csv","r")
    linea = archivo.readline()
    
    if linea:
        while linea:
            if linea[-1]=='\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()

def capturarUltimosValores():
   
    listaA1 = lista[len(lista)-120:len(lista)] #ultimos datos del archivo clasificacionAntrac (HR,TEMP, ANTRAC) consultados para ver si hay alerta
    listaA2 = lista[len(lista)-60:len(lista)]
    listaA3 = lista[len(lista)-30:len(lista)]
    valoresA1 = [] #valores de los ultimos datos de ANTRAC (A0,A1,A2,A3)
    valoresA2 = []
    valoresA3 = []
    print 'tamano lista ',len(lista)
    print listaA1
    print listaA2
    print listaA3
    for elemento in listaA1:
        arreglo = elemento.split(",") # arreglo es una fila del archivo
        valoresA1.append(arreglo[2]) # valoresA1 es una lista con los valores de ANTRAC de listaA1
    for elemento in listaA2:
        arreglo = elemento.split(",") # arreglo es una fila del archivo
        valoresA2.append(arreglo[2]) # valoresA2 es una lista con los valores de ANTRAC de listaA2
    for elemento in listaA3:
        arreglo = elemento.split(",") # arreglo es una fila del archivo
        valoresA3.append(arreglo[2]) # valoresA3 es una lista con los valores de ANTRAC de listaA2
    return valoresA1, valoresA2, valoresA3

def capturarAlerta():
    vA1, vA2, vA3 = capturarUltimosValores()
    print 'lista ul 1',vA1
    n1A0 = vA1.count('A0')
    n1A1 = vA1.count('A1')
    n1A2 = vA1.count('A2')
    n1A3 = vA1.count('A3')
    lAlerta1 = [n1A3,n1A2,n1A1,n1A0]
    print 'lista alerta 1',lAlerta1
    print 'max lista',max(lAlerta1)
    print 'index max lista',lAlerta1.index(max(lAlerta1))
    indAlerta1 = lAlerta1.index(max(lAlerta1))

    print 'lista ul 2',vA2
    n2A0 = vA2.count('A0')
    n2A1 = vA2.count('A1')
    n2A2 = vA2.count('A2')
    n2A3 = vA2.count('A3')
    lAlerta2 = [n2A3,n2A2,n2A1,n2A0]
    print 'lista alerta 2',lAlerta2
    print 'max lista',max(lAlerta2)
    print 'index max lista',lAlerta2.index(max(lAlerta2))
    indAlerta2 = lAlerta2.index(max(lAlerta2))

    print 'lista ul 3',vA3
    n3A0 = vA3.count('A0')
    n3A1 = vA3.count('A1')
    n3A2 = vA3.count('A2')
    n3A3 = vA3.count('A3')
    lAlerta3 = [n3A3,n3A2,n3A1,n3A0]
    print 'lista alerta 3',lAlerta3
    print 'max lista',max(lAlerta3)
    print 'index max lista',lAlerta3.index(max(lAlerta3))
    indAlerta3 = lAlerta3.index(max(lAlerta3))

    lAlertaFinal = [indAlerta3,indAlerta2,indAlerta1]
    indn1A0 = lAlertaFinal.count(3)
    indn1A1 = lAlertaFinal.count(2)
    indn1A2 = lAlertaFinal.count(1)
    indn1A3 = lAlertaFinal.count(0)
    lindexAlertaFinal = [indn1A3,indn1A2,indn1A1,indn1A0]

    print 'lista 3 alertas', lAlertaFinal
    print 'lista F',lindexAlertaFinal
    print 'max lista',max(lindexAlertaFinal)
    print 'index max lista',lindexAlertaFinal.index(max(lindexAlertaFinal))
    indAlertaFinal = lindexAlertaFinal.index(max(lindexAlertaFinal))
    nivelAlertaFinal = ''
    if indAlertaFinal == 0:
        nivelAlertaFinal = 'A3'
    elif indAlertaFinal == 1:
        nivelAlertaFinal = 'A2'
    elif indAlertaFinal == 2:
        nivelAlertaFinal = 'A1'
    elif indAlertaFinal == 3:
        nivelAlertaFinal = 'A0'

    print 'nivel de alerta final',nivelAlertaFinal
    return nivelAlertaFinal

def enviarAlerta():
    alertF = capturarAlerta()
    fechaDato = strftime("%d %b %Y %H:%M:%S", gmtime())
    archivoAlerta = open("alertasAntrac.csv","a")
    line = alertF+','+fechaDato+'\n'

    if alertF == 'A0':
        print 'no hay alerta'
    else:
        archivoAlerta.write(line)
    archivoAlerta.close()    
               

def consultarAlerta():
    valores = []

    for elemento in lista:
        arreglo = elemento.split(",")
        valores.append(arreglo[3])
        print arreglo
       
iniciarArchivo()
cargar()
enviarAlerta()
