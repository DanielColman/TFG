#Importaremos los DATOS desde data.csv
import time
inicio = time.time()

import csv, math, random
from operator import itemgetter

def replaceRepetido(solucion,espacio):
    for i in range(1, len(solucion)):
        c=0
        if solucion[i] in solucion[:i]:
            while c!=-1:
                valorReemplazo =random.randint(0,espacio)
                if not (valorReemplazo in solucion):
                    solucion[i]=valorReemplazo
                    c=-1


def fitness(conjunto): 

    fit=[]
    fits=[]
    fitsPadres=[]
   

    for row in conjunto:
        #row.sort()
        
        #Distancia Euclidiana

        cantIndividuos =  len(row)
        individuosPorGrupo = int(cantIndividuos / 2) 
        
        c=0
        sumDistancias=0
        xPesoT=0
        xPesoC=0
        yEdadT=0
        yEdadC=0
        while c<individuosPorGrupo:
            eTest=int(results[row[c]]['Edad'])
            eControl=int(results[row[individuosPorGrupo+c]]['Edad'])
            pTest=int(results[row[c]]['Peso'])
            pControl=int(results[row[individuosPorGrupo+c]]['Peso'])

            distancia = math.sqrt((eTest-eControl)**2+(pTest-pControl)**2)
            sumDistancias += distancia
            #Centro de Gravedad
            xPesoT += int(results[row[c]]['Peso'])
            yEdadT += int(results[row[c]]['Edad'])
            
            xPesoC += int(results[row[individuosPorGrupo+c]]['Peso'])
            yEdadC += int(results[row[individuosPorGrupo+c]]['Edad'])
            
            c+=1

        xPesoT = xPesoT/2
        yEdadT = yEdadT/2
        
        xPesoC = xPesoC/2
        yEdadC = yEdadC/2

        Q1=sumDistancias
        Q2=math.sqrt((xPesoT-xPesoC)**2 + (yEdadT-yEdadC)**2)

        Q=500*Q1+Q2 

        fit.append(row)
        fit.append(Q)
        fits.append(fit)
        fit=[]

    fits.sort(key=itemgetter(1))

    fitsPadres.append(fits[0])
    fitsPadres.append(fits[1])

    #Para no seleccionar padres GEMELOS
    

    return fitsPadres

def cruzar(padres, espacio):

    c=0
    hijos=[]
    cant=len(padres[0][0])-1
    cross=random.randint(0,cant)
    while c<=cross:

        a=padres[0][0][c]
        b=padres[1][0][c]
        
        padres[0][0][c] = b
        padres[1][0][c] = a

        c+=1

    for row in padres:
        hijos.append(row[0][:])
    
    c=0
    while c<=cross:

        a=padres[0][0][c]
        b=padres[1][0][c]
        
        padres[0][0][c] = b
        padres[1][0][c] = a

        c+=1

    for row in hijos:
        replaceRepetido(row,espacio) #OJOOOOOOOOOOOOO EL VALOR CORRESPONDE A LA DE INDIVIDUOS

    #print(hijos[0][:],hijos[1][:])
    return(hijos[0][:],hijos[1][:])

def mutar(hijos, espacio):
    for row in hijos:
        c=0
        cant=len(row)-1
        while c!=-1:
            genMutado=random.randint(0,cant)
            valorMutado =random.randint(0,espacio)
            if not (valorMutado in row):
                row[genMutado]=valorMutado
                c=-1

    
    #print(hijos)
    return hijos[:][:]
        
 
results = []
resultDist = []
resultCentroGravedad = []
resultCombinatoria = []
familia = []
solucion = []
individuo=[]
descendencia=[]


#Abrir csv y volcar contenido a una lista (Formato Json)
with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        results.append(row)


#PASO 1 (Generar aleatoriamente el primer conjunto de soluciones factibles)
#Crear la familia de soluciones factibles

##################################
SolFactibles = 6 #NUMERO PAR
##################################

cardinalidad = 0
while cardinalidad <= SolFactibles-1:  #Defino en 4 la cardinalidad del Poblaci??n
    cardinalidad+=1
    familia.append((random.sample(range(len(results)), 4))) #El valor numerico significa la cantidad de individuos seleccionados para tes y control
#print(familia)

generacion=0
hijosMutados=[]
while (generacion<=100000):
    #PASO 2 (Seleccionar por Fitness las 2 Mejores Soluciones - "Soluciones Padres")
    if generacion==0:
        padresFit = fitness(familia)
    else:
        padresFit=fitness(hijosMutados)
    #print(padresFit)
    print(padresFit[0][1])
   
    #PASO 3 (Cruzo los padres para generar una nueva Poblaci??n Hija)
    hijo=1
    while hijo <= SolFactibles/2:  #Defino la cantidad de hijos generados, EL CRUZAMIENTO DEVUELVE 2 HIJOS
        hijo+=1
        descendencia.extend(cruzar(padresFit,len(results)-1))
    #print (descendencia)

    #Aplicar Mutacion la nueva la Generaci??n
    hijosMutados=mutar(descendencia,len(results)-1) #OJOOOOOOOOOOOOO EL VALOR CORRESPONDE A LA CANTIDAD DE INDIVIDUOS
    descendencia.clear()
    
    #print(hijosMutados)

    #Usar Etilismo y agregar el mejor padre a la probacion hija
    hijosMutados.append(padresFit[0][0])
    #print(hijosMutados)
  
    #print("--------------------------")
    generacion+=1


fin = time.time()
print(fin-inicio)




