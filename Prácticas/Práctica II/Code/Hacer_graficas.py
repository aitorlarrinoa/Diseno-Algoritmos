# FILE PARA HACER GRÁFICAS EN ALG. ANCHURA


from matplotlib.pyplot import *

def saltos_posibles(S,n): # FUNCIÓN AUXILIAR
    (x,y) = S[-1]
    lista = list()
    
    for (i,j) in [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]:
        a = x + i
        b = y + j
        if 0 <= a < n and 0 <= b < n and not (a,b) in S :
            lista.append((a,b))
        
    return lista

def caballo_anchura(casilla,n): # ALG. EN ANCHURA
    activo = 0
    V = [[casilla]]
    n2 = n*n
    Nlistas = [0,1]
    m = 0
    tamaño = len(V[activo])
    while activo < len(V):
        if len(V[activo]) != tamaño:
            tamaño = len(V[activo])
            Nlistas.append(m)
            m = 0
            
        if len(V[activo]) == n2:
            activo += 1
        else:
            for rama in saltos_posibles(V[activo],n):
                V.append(V[activo] + [rama])
                m = m + 1
            del V[activo]    
    return Nlistas

print('GRÁFICA ALG. EN ANCHURA\n\n')
n = int(input('Introducir valor de "n" : '))
x = int(input('1ª coord casilla inicio: '))
y = int(input('2ª coord casilla inicio: '))
file = input('Nombre de la gráfica: ')

levelmax = (n*n) + 1
plot(list(range(levelmax)),caballo_anchura((x,y),n),'green')
ylabel(' Nº de Nodo ')
xlabel(' Etapa/Nivel')
title(' Seguimineto de exploración ')
savefig(file + '.png')
