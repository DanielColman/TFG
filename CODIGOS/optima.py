
#Importaremos los DATOS desde data.csv
import csv, math
from operator import itemgetter
results = []
resultDist = []
resultCentroGravedad = []
resultCombinatoria = []


#Abrir csv y volcar contenido a una lista (Formato Json)
with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        results.append(row)


#Obtener de la lista la Distancia Euclidiana para cada par de Pacientes
for row2 in results:
    for row3 in results:
        dist = []
        if row2['id'] != row3['id']:
            #Caculamos la distancia y redondeamos a 2 decimales
            distancia = math.sqrt((int(row2['Edad'])-int(row3['Edad']))**2+(int(row2['Peso'])-int(row3['Peso']))**2)
            dist.append(row2['id'])
            dist.append(row3['id'])
            dist.append(distancia)

            #Almacenamos en una Matriz, donde cada fila corresponde a (PacienteX,PacienteY,Distancia)
            resultDist.append(dist)
            resultDist.sort(key=itemgetter(2))


#Persistimos los resultados en un archivo .CSV (dataDistance)
with open('dataDistance.csv', 'w') as csvfile2:
    fieldnames = ['Paciente1', 'Paciente2', 'Distancia']
    writer = csv.DictWriter(csvfile2, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for row in resultDist:
        writer.writerow( { 'Paciente1': row[0], 'Paciente2': row[1], 'Distancia': row[2] } )

#Poner Condicion para evitar centro consigo mismo (Exito)
#Obtener distancias de Centros de Gravedad
for row2 in results:
    for row3 in results:
        if (row2['id'] != row3['id']):
            centroGravedad = []
            xPeso = (int(row2['Peso'])+int(row3['Peso'])) / 2
            yEdad = (int(row2['Edad'])+int(row3['Edad'])) / 2 
            centroGravedad.append(row2['id'])
            centroGravedad.append(row3['id'])
            centroGravedad.append(xPeso)
            centroGravedad.append(yEdad)

            #Almacenamos en una Matriz, donde cada fila corresponde a (PacienteX, PacienteY, xPeso, yEdad)
            resultCentroGravedad.append(centroGravedad)


#Persistimos los resultados en un archivo .CSV (dataCentroGravedad)
with open('dataCentroGravedad.csv', 'w') as csvfile3:
    fieldnames = ['Paciente1', 'Paciente2', 'xPeso', 'yEdad']
    writer = csv.DictWriter(csvfile3, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for row in resultCentroGravedad:
        writer.writerow( { 'Paciente1': row[0], 'Paciente2': row[1], 'xPeso': row[2], 'yEdad': row[3] } )


#Combinarotorias: para cada conjunto T(t1,t2) se genera sus correspondientes conjuntos C(c1, c2)
#Se calculan los respectivos valores de Q donde Q=500*Q1+Q2


for row1 in results:                        #t1
    for row2 in results:                    #t2
        for row3 in results:                #c1
            for row4 in results:            #c2
                combinatorias = []
                if  (row1['id'] != row2['id'] and row1['id'] != row3['id'] and row1['id'] != row4['id'] and row2['id'] != row3['id'] and row2['id'] != row4['id'] and row3['id'] != row4['id']):
                        
                    #Recuperamos del dataDistance.csv, la distancia Euclidiana previamente calculada
                    for element in resultDist:
                        if element[0] == row1['id'] and element[1] == row3['id']:
                            D1 = float(element[2])    #D(c1,t1)
                        if element[0] == row2['id'] and element[1] == row4['id']:
                            D2 = float(element[2])    #D(c2,t2)

                    #Recuperamos del dataCentroGravedad.csv, las coordenadas de los centros de gravedad
                    for element in resultCentroGravedad:
                        if element[0] == row1['id'] and element[1] == row2['id']:
                            xPesoT=element[2]
                            yEdadT=element[3]
                        if element[0] == row3['id'] and element[1] == row4['id']:
                            xPesoC=element[2]
                            yEdadC=element[3]
                    
                    #Distancia Media, OJO el Profesor no utilizo la division entre 2 en el ejemplo de Excel
                    Q1=(D1+D2)
                    Q2=math.sqrt((xPesoT-xPesoC)**2 + (yEdadT-yEdadC)**2)

                    Q=500*Q1+Q2 

                    t1=row1['id']
                    t2=row2['id']
                    c1=row3['id']
                    c2=row4['id']
                    
                    combinatorias.append(t1)
                    combinatorias.append(t2)
                    combinatorias.append(c1)
                    combinatorias.append(c2)
                    combinatorias.append(Q)

                    #print(combinatorias,'-')
                    #print(D1,'-',D2,'-',xPesoT,'-',yEdadT,'-',xPesoC,'-',yEdadC,'-',500*Q1)
                    
                    resultCombinatoria.append(combinatorias)

#Ordenamos la metricas en funcion a la Calidad de Menor a Mayor
resultCombinatoria.sort(key=itemgetter(4))

#Persistimos los resultados en un archivo .CSV (dataCentroGravedad)
with open('metricasCalidad.csv', 'w') as csvfile4:
    fieldnames = ['PacienteTest1', 'PacienteTest2', 'PacienteControl1', 'PacienteControl2', 'Q (Calidad)']
    writer = csv.DictWriter(csvfile4, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for row in resultCombinatoria:
        writer.writerow( { 'PacienteTest1': row[0], 'PacienteTest2': row[1], 'PacienteControl1': row[2], 'PacienteControl2': row[3], 'Q (Calidad)':row[4] } )



                            
