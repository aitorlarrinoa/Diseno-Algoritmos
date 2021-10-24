print('\nPRÁCTICA 1 - GRUPO 11 - Ander Cano y Mikel Lamela - Febrero 2021\n')

print('INICIO\n')

# importamos las librerías descargadas
import time 
from matplotlib.pyplot import *
from numpy import *
import random
from scipy import *
from scipy.optimize import curve_fit
from algoritmos import *


algoritmos = [BubbleSort,InsertionSort,MergeSort,HeapSort,QuickSort]
tamaños = [5,500,1000,2000,4500,7500,9000,12000]
nrepeticion = 50
tiempos_ordenada = [None for j in range(len(algoritmos))]
tiempos_inv_ordenada = [None for j in range(len(algoritmos))]
tiempos_par_ordenada = [None for j in range(len(algoritmos))]
tiempos_aleatoria = [None for j in range(len(algoritmos))]


# LISTA ORDENADA
print(' LISTA ORDENADA\n')
figure() # Nueva Gráfica

# Cálculo de tiempos
i = 0
for alg in algoritmos:
    times = list()
    for n in tamaños:
        lista = list(range(n))
        Stimes = 0
        for k in range(nrepeticion):
            time1 = time.process_time()
            alg(lista)
            time2 = time.process_time()
            Stimes += (time2-time1)
        times.append(Stimes/nrepeticion)
    tiempos_ordenada[i] = times
    i+=1

# Gráfica
plot(tamaños,tiempos_ordenada[0],tamaños,tiempos_ordenada[1],tamaños,tiempos_ordenada[2],tamaños,tiempos_ordenada[3])
xlabel('Tamaño del problema ')
ylabel('Tiempo empleado en segundos')
legend(('BubbleSort','InsertionSort','MergeSort','HeapSort','QuickSort'),prop = {'size': 10}, loc='upper right')
title('LISTA ORDENADA')
savefig('lista_ordenada.png')



# LISTA INVERSAMENTE ORDENADA 
print(' LISTA INVERSAMENTE ORDENADA\n')
figure() # Nueva Gráfica

# Cálculo de tiempos
i = 0
for alg in algoritmos:
    times = list()
    for n in tamaños:
        Stimes = 0
        for k in range(nrepeticion):
            lista = list(range(n))
            lista.reverse()
            time1 = time.process_time()
            alg(lista)
            time2 = time.process_time()
            Stimes += (time2-time1)
        times.append(Stimes/nrepeticion)
    tiempos_inv_ordenada[i] = times
    i+=1

# Dibujo de la gráfica
plot(tamaños,tiempos_inv_ordenada[0],tamaños,tiempos_inv_ordenada[1],tamaños,tiempos_inv_ordenada[2],tamaños,tiempos_inv_ordenada[3])
xlabel('Tamaño del problema ')
ylabel('Tiempo empleado en segundos')
legend(('mergeSort','insertionSort','heapSort','quickSort'),prop = {'size': 10}, loc='upper left')
title('LISTA INVERSAMENTE ORDENADA')
savefig('lista_inversa_ordenada.png')



# PARCIALMENTE ORDENADA 
print(' LISTA PARCIALMENTE ORDENADA\n')

figure() # Nueva Gráfica

# Cálculo de tiempos
i = 0
for alg in algoritmos:
    times = list()
    for n in tamaños:
        Stimes = 0
        for k in range(nrepeticion):
            lista = list(range(n//2)) + [random.randrange(n//2,n,1) for j in range(n//2)]
            time1 = time.process_time()
            alg(lista)
            time2 = time.process_time()
            Stimes += (time2-time1)
        times.append(Stimes/nrepeticion)
    tiempos_par_ordenada[i] = times
    i+=1

# Dibujo de la gráfica
plot(tamaños,tiempos_par_ordenada[0],tamaños,tiempos_par_ordenada[1],tamaños,tiempos_par_ordenada[2],tamaños,tiempos_par_ordenada[3])
xlabel('Tamaño del problema ')
ylabel('Tiempo empleado en segundos')
legend(('mergeSort','insertionSort','heapSort','quickSort'),prop = {'size': 10}, loc='upper left')
title('LISTA PARCIALMENTE ORDENADA')
savefig('lista_parcial_ordenada.png')



# LISTA ALEATORIA 
print(' LISTA ALEATORIA\n')

figure() # Nueva gráfica

# Cálculo de tiempos    
i = 0
for alg in algoritmos:
    times = list()
    for n in tamaños:
        Stimes = 0
        for k in range(nrepeticion):
            lista = [random.randrange(0,n,1) for j in range(n)]
            time1 = time.process_time()
            alg(lista)
            time2 = time.process_time()
            Stimes += (time2-time1)
        times.append(Stimes/nrepeticion)
    tiempos_aleatoria[i] = times
    i+=1

# Dibujo de la gráfica
plot(tamaños,tiempos_aleatoria[0],tamaños,tiempos_aleatoria[1],tamaños,tiempos_aleatoria[2],tamaños,tiempos_aleatoria[3])
xlabel('Tamaño del problema ')
ylabel('Tiempo empleado en segundos')
legend(('mergeSort','insertionSort','heapSort','quickSort'),prop = {'size': 10}, loc='upper left')
title('LISTA ALEATORIA')
savefig('lista_aleatoria.png')



# GRAFICAS POR ALGORITMO
print(' GRAFICAS POR ALGORITMO\n')
nombre_alg = ['BubbleSort','InsertionSort','MergeSort','HeapSort','QuickSort']
for i in range(len(nombre_alg)):
    figure() 
    plot(tamaños,tiempos_ordenada[i],tamaños,tiempos_inv_ordenada[i],tamaños,tiempos_par_ordenada[i],tamaños,tiempos_aleatoria[i])
    xlabel('Tamaño del problema ')
    ylabel('Tiempo empleado en segundos')
    legend(('LISTA ORDENADA','LISTA INVERSAMENTE ORDENADA','LISTA PARCIALMENTE ORDENADA','LISTA ALEATORIA'),prop = {'size': 10}, loc='upper left')
    title(nombre_alg[i])
    savefig(nombre_alg[i]+'.png')               



# CASOS QUICKSORT
print(' ESTUDIO QUICKSORT\n')
def pivotes(i,n,lista):
    if i==0:
        return lista[0]
    elif i == 1:
        return lista[n//2]
    elif i == 2:
        return lista[n-1]
    elif i == 3:
        return None
    else:
        p1 = lista[random.randint(0,n-1)]
        p2 = lista[random.randint(0,n-1)]
        p3 = lista[random.randint(0,n-1)]
        return (p1+p2+p3)//3

# Cálculo de tiempos
tiempos_pivote = [None for j in range(5)]
for i in range(5):
    times = list()
    for n in tamaños:
        Stimes = 0
        for k in range(nrepeticion):
            lista = [random.randrange(0,n,1) for j in range(n)]
            time1 = time.time()
            quickSort(lista,pivotes(i,n,lista))
            time2 = time.time()
            Stimes += (time2-time1)
        times.append(Stimes/nrepeticion)
    tiempos_pivote[i] = times
    
# Dibujo de la gráfica
figure()
plot(tamaños,tiempos_pivote[0],tamaños,tiempos_pivote[1],tamaños,tiempos_pivote[2],tamaños,tiempos_pivote[3],tamaños,tiempos_pivote[4])
xlabel('Tamaño del problema ')
ylabel('Tiempo empleado en segundos')
legend(('1º elemento','Elemento mitad','Último elemento','Random','A tres bandas'),prop = {'size': 10}, loc='upper left')
title('Estudio_Pivotes_QuickSort')
savefig('Estudio_QuickSort.png')


# BUBBLESORT
print(' BUBBLESORT\n\n')
figure()
time1 = 0
time2 = 0
nrep = 5
times = list()

# Lista Ordenada
for n in tamaños:
    lista = list(range(n))
    Stimes = 0
    for k in range(nrep):
        time1 = time.process_time()
        bubbleSort(lista)
        time2 = time.process_time()
        Stimes += (time2-time1)
    times.append(Stimes/nrep)
plot(tamaños,times)

# Lista Inv Ordenada
times = list()
for n in tamaños:
    Stimes = 0
    for k in range(nrep):
        lista = list(range(n))
        lista.reverse()
        time1 = time.process_time()
        bubbleSort(lista)
        time2 = time.process_time()
        Stimes += (time2-time1)
    times.append(Stimes/nrep)
plot(tamaños,times)

# Lista Par Ordenada
times = list()
for n in tamaños:    
    Stimes = 0
    for k in range(nrep):
        lista = list(range(n//2)) + [random.randrange(n//2,n,1) for j in range(n//2)]
        time1 = time.process_time()
        bubbleSort(lista)
        time2 = time.process_time()
        Stimes += (time2-time1)
    times.append(Stimes/nrep)
plot(tamaños,times)
# Lista Aleatoria
times = list()
for n in tamaños:
    Stimes = 0
    for k in range(nrep):
        lista = [random.randrange(0,n,1) for j in range(n)]
        time1 = time.process_time()
        bubbleSort(lista)
        time2 = time.process_time()
        Stimes += (time2-time1)
    times.append(Stimes/nrep)
plot(tamaños,times)
xlabel('Tamaño del problema ')
ylabel('Tiempo empleado en segundos')
legend(('LISTA ORDENADA','LISTA INVERSAMENTE ORDENADA','LISTA PARCIALMENTE ORDENADA','LISTA ALEATORIA'),prop = {'size': 10}, loc='upper left')
title('BUBBLESORT')
savefig('BUBBLESORT.png') 


        

print('FIN\n')
