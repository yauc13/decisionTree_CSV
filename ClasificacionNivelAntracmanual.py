#arbol de decision J48 generado por weka
#clasifica los valores que llegan de los sensores
#en las categorias A3,A2,A1,A0
#y los almacena en un archivo csv
#ademas envia algunas alertas sobre el clima
import csv
import serial
import time
from time import gmtime, strftime

# Abrimos la conexion con Arduino
#arduino = serial.Serial('COM3', baudrate=9600, timeout=1.0)

#arbolDecisionJ48() ingresan los valores de HR y Temp
#retorna la clasificacion Antrac (A3,A2,A1,A0)

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



def arbolDecisionJ48(HR, T):
    HR = int(HR) #conversion para asegurar que es entero 
    T = int(T)
    if HR <= 89:
        if T <= 29:
            if HR <= 80:
                Antrac = 'A0'
            elif HR > 80:
                if T <= 23:
                    if HR <= 85:
                        Antrac = 'A0'
                    elif HR > 85:
                        Antrac = 'A1'
                elif T > 23:
                    Antrac = 'A1'
        elif T > 29:
            if HR <= 75:
                Antrac = 'A1'
            elif HR > 75:
                Antrac = 'A2'
    elif HR > 89:
        if T <= 29:
            if HR <=95 :
                if HR <=90:
                    Antrac = 'A1'
                elif HR >90:
                    Antrac = 'A2'
            elif HR >95:
                Antrac = 'A3'
        elif T > 29 :
            Antrac = 'A3'
    return Antrac


         
def capturarDatosSensor():
    HRA = 0
    TL = 0
    try:
        var = "L"
        arduino.write(var)
        time.sleep(0.1) #tiempo que demora en envia y obtener respuesta de arduino
        while arduino.inWaiting() > 0:
            line = arduino.readline()
            print line
            archivo = open("datoTemporal.csv","w") #la 'w' es para decirle que borre y escriba de nuevo 
            archivo.write(line)
            archivo.close()
        M = []
        f = open("datoTemporal.csv")
        lns = csv.reader(f,delimiter=',')
        for i in lns:
            M = M+[i]
#        print M

        dataSet = []
        for i in M:
            HRA = int(i[0])
            TL = int(i[1])
            print HRA,TL

    except KeyboardInterrupt:
        capturarDatosSensor()
        print "ERROR DESDE ARDUINO"
    except IOError:
        print "ERROR DESDE CARGAR DATO TEMPORAL"
          
    return HRA,TL

def almacenarDatosClasificados():
    listaA1 = lista
    for elemento in listaA1:
        arreglo = elemento.split(",") # arreglo es una fila del archivo
        HRAl = arreglo[1]
        TEMPAl = arreglo[2]
        ANTRACAl = arbolDecisionJ48(HRAl,TEMPAl)
        fechaDato = strftime("%d %b %Y %H:%M:%S", gmtime())
        
        line = str(HRAl)+','+str(TEMPAl)+','+ANTRACAl+','+fechaDato+'\n'
        print line
        archivo = open("clasificacionAntrac.csv","a") #la 'a' es para decirle que agregue y no borre lo que ya esta 
        archivo.write(line)
        archivo.close()
        #time.sleep(2)
        

print 'clasificacion  valores de sensores'

iniciarArchivo()
cargar()
almacenarDatosClasificados()

