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





results = []
resultDist = []
resultCentroGravedad = []
resultCombinatoria = []
familia = []
solucion = []
individuo=[]



#Abrir csv y volcar contenido a una lista (Formato Json)
with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        results.append(row)



#PASO 1 (Generar aleatoriamente el primer conjunto de soluciones factible)

#Crear la familia de soluciones factibles
cardinalidad = 0
while cardinalidad <= 4:  #Defino en 20 la cardinalidad del conjunto de soluciones
    cardinalidad+=1
    
    familia.append((random.sample(range(5), 4)))
    
print(familia)

#PASO 2 (Seleccionar por Fitness las 2 Mejores Soluciones - "Soluciones Padres")
fit = fitness(familia)

print(fit)

