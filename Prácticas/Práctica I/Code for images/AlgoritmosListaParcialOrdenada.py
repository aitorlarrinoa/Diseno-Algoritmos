import time 
from matplotlib.pyplot import *
from numpy import *
import random
from scipy import *
from algoritmos import *

tamaños=[5,50,100,500,1000,2000,4500,7500,9000,12000]

############# LISTA PARCIALMENTE ORDENADA ####################

print('LISTA PARCIALMENTE ORDENADA\n\n')
figure()
tiempo1=0
tiempo2=0



# ALGORITMO MERGESORT
tiempos3=list()
nrep3=900
for n in tamaños:    
    Stimes=0
    for k in range(nrep3):
        lista=list(range(n//2)) + [random.randint(n//2,n) for j in range(n//2)]
        lista.reverse()
        tiempo1=time.process_time()
        MergeSort(lista)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos3.append(Stimes/nrep3)
plot(tamaños,tiempos3)

# ALGORITMO HEAPSORT
tiempos4=list()
nrep4=700
for n in tamaños:
    Stimes=0
    for k in range(nrep4):
        lista=list(range(n//2)) + [random.randint(n//2,n) for j in range(n//2)]
        lista.reverse()
        tiempo1=time.process_time()
        HeapSort(lista)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos4.append(Stimes/nrep4)
plot(tamaños,tiempos4)

# ALGORITMO HEAPSORT
tiempos5=list()
nrep5=900
for n in tamaños:
    Stimes=0
    for k in range(nrep5):
        lista=list(range(n//2)) + [random.randint(n//2,n) for j in range(n//2)]
        lista.reverse()
        tiempo1=time.process_time()
        QuickSort(lista)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos5.append(Stimes/nrep5)
plot(tamaños,tiempos5)
xlabel('Tamaño de la lista')
ylabel('Tiempo empleado por los algoritmos')
legend(('MergeSort','HeapSort','QuickSort'),prop = {'size': 10}, loc='upper right')
title('lista parcialmente ordenada')
savefig('LISTAPARCIALORDENADA.png') 


        
print('FIN')
