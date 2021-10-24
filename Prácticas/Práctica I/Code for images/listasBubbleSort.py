import time 
from matplotlib.pyplot import *
from numpy import *
import random
from scipy import *
from algoritmos import *

tamaños=[5,50,100,500,1000,2000,4500,7500,9000,12000]

#Cálculo del tiempo para el algoritmo BubbleSort.
print(' BUBBLESORT\n\n')
figure()
tiempo1=0
tiempo2=0
nrep=5


# Lista Parcialmente Ordenada
tiempos3=list()
for n in tamaños:    
    Stimes=0
    for k in range(nrep):
        lista=list(range(n//2)) + [random.randint(n//2,n) for j in range(n//2)]
        tiempo1=time.process_time()
        BubbleSort(lista)
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
        BubbleSort(lista)
        tiempo2=time.process_time()
        Stimes=Stimes+(tiempo2-tiempo1)
    tiempos4.append(Stimes/nrep)
plot(tamaños,tiempos4)
xlabel('Tamaño de la lista')
ylabel('Tiempo empleado por el algoritmo BubbleSort')
legend(('Lista parcialmente ordenada','Lista aleatoria'),prop = {'size': 10}, loc='upper right')
title('Algoritmo BubbleSort')
savefig('BUBBLESORT.png') 


        
print('FIN')
