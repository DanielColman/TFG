#Importaremos los DATOS desde data.csv
import csv, math, random
from operator import itemgetter

def fitness(conjunto): 

    fit=[]
    #fit={"solution":[],"fitness":[]}
    fits=[]
    fitsPadres=[]
   

    for row in conjunto:
        #row.sort()
        
        #Distancia Euclidiana
        eTest1=int(results[row[0]]['Edad'])
        eTest2=int(results[row[1]]['Edad'])
        eControl1=int(results[row[2]]['Edad'])
        eControl2=int(results[row[3]]['Edad']) 

        pTest1=int(results[row[0]]['Peso'])
        pTest2=int(results[row[1]]['Peso'])
        pControl1=int(results[row[2]]['Peso'])
        pControl2=int(results[row[3]]['Peso']) 

        distancia1 = math.sqrt((eTest1-eControl1)**2+(pTest1-pControl1)**2)
        distancia2 = math.sqrt((eTest2-eControl2)**2+(pTest2-pControl2)**2)

        #Distancia Centro de Gravedad
        xPesoT = (int(results[row[0]]['Peso'])+int(results[row[1]]['Peso'])) / 2
        yEdadT = (int(results[row[0]]['Edad'])+int(results[row[1]]['Edad'])) / 2

        xPesoC = (int(results[row[2]]['Peso'])+int(results[row[3]]['Peso'])) / 2
        yEdadC = (int(results[row[2]]['Edad'])+int(results[row[3]]['Edad'])) / 2

        Q1=(distancia1+distancia2)
        Q2=math.sqrt((xPesoT-xPesoC)**2 + (yEdadT-yEdadC)**2)

        Q=500*Q1+Q2 

        fit.append(row)
        fit.append(Q)
        fits.append(fit)
        fit=[]

    fits.sort(key=itemgetter(1))

    fitsPadres.append(fits[0])
    fitsPadres.append(fits[1])

    return fitsPadres

def cruzar(padres):
    c=0
    hijos=[]
    cant=len(padres[0][0])-1
    cross=random.randint(0,cant-1)

    while c<=cross:
        a=padres[0][0][c]
        b=padres[1][0][c]
        
        padres[0][0][c] = b
        padres[1][0][c] = a

        c+=1

    for row in padres:
        hijos.append(row[0])
    
    #print(hijos)
    return(hijos)
    #return (padres[random.randint(0,1)])

        
 
results = []
resultDist = []
resultCentroGravedad = []
resultCombinatoria = []
familia = []
solucion = []
individuo=[]
descendencia=[]
aux=[]




#Abrir csv y volcar contenido a una lista (Formato Json)
with open('codigos/data.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        results.append(row)



#PASO 1 (Generar aleatoriamente el primer conjunto de soluciones factibles)

#Crear la familia de soluciones factibles
cardinalidad = 0
while cardinalidad <= 4:  #Defino en 4 la cardinalidad del Población
    cardinalidad+=1
    
    familia.append((random.sample(range(5), 4)))
    
print(familia)

#PASO 2 (Seleccionar por Fitness las 2 Mejores Soluciones - "Soluciones Padres")
padresFit = fitness(familia)
print(padresFit)


#PASO 3 (Cruzo los padres para generar una nueva Población hijo)
hijos=0

print("-----------")
while hijos <= 1:  #Defino la cantidad de hijos generados, EL CRUZAMIENTO DEVUELVE 2 HIJOS
    hijos+=1
    #Agrego los hijos a la nueva poblacion
    aux = cruzar(padresFit)
    print(aux) 

    for row in aux:
        print(row)
        descendencia.insert(len(descendencia+1),row)
        #descendencia.append(row)
    
    
    #print(padresFit)

print (descendencia)



