import time 
from matplotlib.pyplot import *
from numpy import *
import random
from scipy import *
from algoritmos import *

tamaños=[5,50,100,500,1000,2000,4500,7500,9000,12000]

#Cálculo del tiempo para el algoritmo BubbleSort.
print('INSERTIONSORT\n\n')
figure()
tiempo1=0
tiempo2=0
nrep=5


# Lista Ordenada
tiempos1=list()
for n in tamaños:
    lista=list(range(n))#generamos la lista ordenada
    Stimes=0
    for k in range(nrep):
        tiempo1=time.process_time()
        InsertionSort(lista)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos1.append(Stimes/nrep)
plot(tamaños,tiempos1)

# Lista Inversamente Ordenada
tiempos2=list()
for n in tamaños:
    Stimes=0
    for k in range(nrep):
        lista=list(range(n))
        lista.reverse()
        tiempo1=time.process_time()
        InsertionSort(lista)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos2.append(Stimes/nrep)
plot(tamaños,tiempos2)

# Lista Parcialmente Ordenada
tiempos3=list()
for n in tamaños:    
    Stimes=0
    for k in range(nrep):
        lista=list(range(n//2)) + [random.randint(n//2,n) for j in range(n//2)]
        tiempo1=time.process_time()
        InsertionSort(lista)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos3.append(Stimes/nrep)
plot(tamaños,tiempos3)

# Lista Aleatoria
tiempos4=list()
for n in tamaños:
    Stimes=0
    for k in range(nrep):
        lista = [random.randint(0,n) for j in range(n)]
        tiempo1=time.process_time()
        InsertionSort(lista)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos4.append(Stimes/nrep)
plot(tamaños,tiempos4)
xlabel('Tamaño de la lista')
ylabel('Tiempo empleado por el algoritmo InsertionSort')
legend(('Lista ordenada','Lista inversamente ordenada','Lista parcialmente ordenada','Lista aleatoria'),prop = {'size': 10}, loc='upper right')
title('Algoritmo InsertionSort')
savefig('INSERTIONSORT.png') 


        
print('FIN')

