#arbol de decision J48 generado por weka
#se prueban valores seudoaleatorios y tambien los
#valores de aprendizaje
#el archivo "COND_ANTRAC_J48.csv" no debe tener el encabezado HR,TEMP,ANTRAC
import csv

def arbolDecisionJ48(HR, T):
    HR = int(HR) #conversion para asegurar que es entero 
    T = int(T)
    #print '-- entra a HR a J48 ---',HR, T
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
    #print '- sale de J48 -', Antrac
    return Antrac

def valoresAprendizaje():
    M = []
    f = open("COND_ANTRAC_J48.csv")
    lns = csv.reader(f,delimiter=',')
    for i in lns:
        M = M+[i]
    #print M

    dataSet = []
    for i in M:
#        i = map(int,i)
        dataSet = dataSet+[i]
    #print dataSet
    
    return dataSet


def valoresPruebaSeudoAleatorio():
    
    HRP = 100 
    MVP = []
    while HRP > 70:
        TP =35
        while TP > 15:
            
            prueba = arbolDecisionJ48(HRP, TP)
            LP = [HRP,TP,prueba]
            MVP = MVP + [LP]
            #print ('prueba: HR='+str(HRP)+' T='+str(TP)+' ANTRAC='+prueba)
            TP -= 13
        HRP -= 12
    return MVP

def valoresPruebaAprendizaje():
    mCl = []
    nTotal=0
    nCorrec=0
    nError=0
    M = []
    f = open("COND_ANTRAC_J48.csv")
    lns = csv.reader(f,delimiter=',')
    for i in lns:
        M = M+[i]
    #print M

    dataSet = []
    for i in M:
#        i = map(int,i)
        HRA = int(i[0])
        TL = int(i[1])
        nTotal +=1
        print ('-valores leidos HR T ANTRAC-', HRA,TL,i[2])
        resp = arbolDecisionJ48(HRA,TL)
        print ('-respuesta algoritmo J48-',resp)
        if resp == i[2]:
            nCorrec +=1
        else:
            mCl = mCl+[HRA,TL,i[2],resp]
            nError +=1
        print ('------------------')
    print ('+-Resultados Finales- total,error,correc',nTotal,nError,nCorrec)
    print ('HR T ESPERADO, CLASIFI',mCl)
         


def comparacionDatos(VA, VP):
    for i in VP:
        print ('filas prueba')
        print (i[0],i[1],i[2])
        for j in VA:
            print ('filas aprendizaje')
            print (j[0],j[1],j[2])
            #if i[0]==j[0] and  i[1]==j[1]:
            if i == j:
                print ('-----filas iguales-----')

#print 'valores para el aprendizaje'
#MApren = valoresAprendizaje()
#print MApren
#print 'valores de prueba'
#MDatos = valoresPrueba()
#print MDatos
print ('comparacion  valores aprendizaje')
valoresPruebaAprendizaje()


