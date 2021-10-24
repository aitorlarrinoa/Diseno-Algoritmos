import time 
from matplotlib.pyplot import *
from numpy import *
import random
from scipy import *
from algoritmos import *

tamaños=[5,50,100,500,1000,2000,4500,7500,9000,12000]

############# LISTA ORDENADA ####################

print('LISTA ORDENADA\n\n')
figure()
tiempo1=0
tiempo2=0


# ALGORITMO MERGESORT
tiempos3=list()
nrep3=600
for n in tamaños:    
    Stimes=0
    for k in range(nrep3):
        lista=list(range(n))
        tiempo1=time.process_time()
        QuickSort(lista)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos3.append(Stimes/nrep3)
plot(tamaños,tiempos3)

# ALGORITMO HEAPSORT
tiempos4=list()
nrep4=500
for n in tamaños:
    Stimes=0
    for k in range(nrep4):
        lista=list(range(n))
        tiempo1=time.process_time()
        HeapSort(lista)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos4.append(Stimes/nrep4)
plot(tamaños,tiempos4)

# ALGORITMO HEAPSORT
tiempos5=list()
nrep5=600
for n in tamaños:
    Stimes=0
    for k in range(nrep5):
        lista=list(range(n))
        tiempo1=time.process_time()
        QuickSort(lista)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos5.append(Stimes/nrep5)
plot(tamaños,tiempos5)
xlabel('Tamaño de la lista')
ylabel('Tiempo empleado por los algoritmos')
legend(('MergeSort','HeapSort','QuickSort'),prop = {'size': 10}, loc='upper right')
title('lista ordenada')
savefig('LISTAORDENADA.png') 


        
print('FIN')
