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
    if len(lista)<=1:
        return lista
    else:
        mitad=len(lista)//2
        izqlista=lista[:mitad]
        derlista=lista[mitad:]
        #se ordenan cada una de las listas que acabamos de crear
        MergeSort(izqlista)
        MergeSort(derlista)
        i = 0
        j = 0
        k = 0
        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                lista[k] = izq[i]
                i += 1
            else:
                lista[k] = der[j]
                j += 1
            k += 1

        while i < len(izq):
            lista[k] = izq[i]
            i += 1
            k += 1

        while j < len(der):
            lista[k] = der[j]
            j += 1
            k += 1

#ALGORITMO HEAPSORT

def HeapSort(lista):
    def moveDown( lista, first, last ):
        largest = 2 * first + 1
        while largest <= last:
            if ( largest < last ) and ( lista[largest] < lista[largest + 1] ):
                largest += 1
            if lista[largest] > lista[first]:
                swap( lista, largest, first )
                first = largest;
                largest = 2 * first + 1
            else:
                return
            
    def swap( A, x, y ):
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp

    length = len(lista) - 1
    leastParent = length // 2
    for i in range(leastParent, -1, -1):
        moveDown(lista, i, length)
    for i in range(length, 0, -1):
        if lista[0] > lista[i]:
            swap(lista, 0, i)
            moveDown(lista, 0, i - 1)

#ALGORITMO QUICKSORT

def QuickSort(lista,pivote=None,izq=0,der=None):
    if der == None:
        der = len(lista) - 1

    if pivote == None and len(lista) > 1:
        pivote = lista[random.randint(izq,der)]
        
    elif len(lista)<= 1:
        pivote = lista[izq]
        
    i = izq
    j = der

    while i <= j:
        while lista[i] < pivote:
            i += 1
        while lista[j] > pivote:
            j -= 1
        if i <= j:
            lista[i],lista[j] = lista[j],lista[i]
            i += 1
            j -= 1
    if izq < j:
        quickSort(lista,None,izq,j)
    if i < der:
        quickSort(lista,None,i,der)

