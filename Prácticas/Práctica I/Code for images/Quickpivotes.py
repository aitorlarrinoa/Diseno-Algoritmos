import time 
from matplotlib.pyplot import *
from numpy import *
import random
from scipy import *
from algoritmos import *

tamaños=[5,50,100,500,1000,2000,4500,7500,9000,12000]

#Cálculo del tiempo para el algoritmo QuickSort.
print('QUICKSORT PIVOTES\n\n')
figure()
tiempo1=0
tiempo2=0
nrep=500

# Pivote primera posición
tiempos1=list()
for n in tamaños:
    lista=[random.randint(0,n) for j in range(n)]
    Stimes=0
    for k in range(nrep):
        tiempo1=time.process_time()
        QuickSort(lista,lista[0],0,None)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos1.append(Stimes/nrep)
plot(tamaños,tiempos1)

# Pivote última posición
tiempos2=list()
for n in tamaños:
    Stimes=0
    for k in range(nrep):
        lista=[random.randint(0,n) for j in range(n)]
        lista.reverse()
        tiempo1=time.process_time()
        QuickSort(lista,lista[len(lista)-1],0,None)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos2.append(Stimes/nrep)
plot(tamaños,tiempos2)

# Pivote aleatorio
tiempos3=list()
for n in tamaños:    
    Stimes=0
    for k in range(nrep):
        lista=[random.randint(0,n) for j in range(n)]
        tiempo1=time.process_time()
        QuickSort(lista,lista[random.randint(0,len(lista)-1)],0,None)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos3.append(Stimes/nrep)
plot(tamaños,tiempos3)

# Pivote mitad
tiempos4=list()
for n in tamaños:
    Stimes=0
    for k in range(nrep):
        lista=[random.randint(0,n) for j in range(n)]
        tiempo1=time.process_time()
        QuickSort(lista,lista[len(lista)//2],0,None)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos4.append(Stimes/nrep)
plot(tamaños,tiempos4)
xlabel('Tamaño de la lista')
ylabel('Tiempo empleado por el algoritmo QuickSort')
legend(('Primera posición','última posición','posición aleatoria','posición mitad'),prop = {'size': 10}, loc='upper right')
title('Algoritmo QuickSort')
savefig('QUICKSORTpivotes.png') 


        
print('FIN')
