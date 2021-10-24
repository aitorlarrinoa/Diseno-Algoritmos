import random

#ALGORITMO BUBBLESORT

def BubbleSort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j]>lista[j+1]:
                a=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=a

#ALGORITMO INSERTIONSORT

def InsertionSort(lista):
    for i in range(1,len(lista)):
        a=lista[i]
        j=i-1
        while j>=0 and a<lista[j]:
            lista[j+1]=lista[j]
            j=j-1
            lista[j+1]=a

#ALGORITMO MERGESORT
                
def MergeSort(lista):
    if len(lista)>1:
        mitad=len(lista)//2
        izqlista=lista[:mitad]
        derlista=lista[mitad:]
        MergeSort(izqlista)
        MergeSort(derlista)
        i=0
        j=0
        k=0
        while i<len(izqlista) and j<len(derlista):
            if izqlista[i] < derlista[j]:
                lista[k]=izqlista[i]
                i=i+1
            else:
                lista[k]=derlista[j]
                j=j+1
            k=k+1

        while i<len(izqlista):
            lista[k]=izqlista[i]
            i=i+1
            k=k+1

        while j<len(derlista):
            lista[k]=derlista[j]
            j=j+1
            k=k+1

#ALGORITMO HEAPSORT

def HeapSort(lista):
    def moveDown(lista,primero,ultimo):
        a=2*primero+1
        while a<=ultimo:
            if (a<ultimo) and (lista[a]<lista[a+1]):
                a=a+1
            if lista[a]>lista[primero]:
                vuelta(lista,a,primero)
                primero=a;
                a=2*primero+1
            else:
                return
    def vuelta(lista,x,y):
        a=lista[x]
        lista[x]=lista[y]
        lista[y]=a
        
    long=len(lista)-1
    leastParent=long//2
    for i in range(leastParent,-1,-1):
        moveDown(lista,i,long)
    for i in range(long,0,-1):
        if lista[0]>lista[i]:
            vuelta(lista,0,i)
            moveDown(lista,0,i-1)

#ALGORITMO QUICKSORT

def QuickSort(lista,pivote=None,izq=0,der=None):
    if der==None:
        der=len(lista)-1
    if pivote==None and len(lista)>1:
        pivote=lista[random.randint(izq,der)]  
    elif len(lista)<=1:
        pivote=lista[izq]    
    i=izq
    j=der
    while i<=j:
        while lista[i]<pivote:
            i=i+1
        while lista[j] > pivote:
            j=j-1
        if i<=j:
            a=lista[i]
            lista[i]=lista[j]
            lista[j]=a
            i=i+1
            j=j-1
    if izq<j:
        QuickSort(lista,None,izq,j)
    if i<der:
        QuickSort(lista,None,i,der)
    return lista
