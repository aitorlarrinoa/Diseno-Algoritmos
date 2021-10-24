

def saltos_posibles(S,n): # FUNCIÓN AUXILIAR
    (x,y) = S[-1]
    lista = list()
    
    for (i,j) in [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]:
        a = x + i
        b = y + j
        if 0 <= a < n and 0 <= b < n and not (a,b) in S :
            lista.append((a,b))
        
    return lista

def caballo_profundidad(sol_parcial,n): # ALG. EN PROFUNDIDAD
    sol = list()
    if len(sol_parcial) == n*n:
        sol.append([sol_parcial[:]])
    else:
        for salto in saltos_posibles(sol_parcial,n):
            sol_parcial.append(salto)
            sol = sol + caballo_profundidad(sol_parcial,n)
            del sol_parcial[-1]
    return sol

def caballo_anchura(casilla,n): # ALG. EN ANCHURA
    activo = 0
    V = [[casilla]]
    n2 = n*n
    while activo < len(V):
        if len(V[activo]) == n2:
            activo += 1
        else:
            for rama in saltos_posibles(V[activo],n):
                V.append(V[activo] + [rama])
            del V[activo]      
    return V


###############################################################################
###############################################################################








# CASOS A EJECUTAR
# n = 5 --> (0,0) , (2,2) y (2,4)
# n = 6 --> (0,0) solo profundidad 


# Programa Principal

import time

print('Práctica II - Grupo 11 - Ander Cano, Mikel Lamela y Aitor Larrinoa \n\n')
n = int(input('Introducir valor de "n" : '))
print('\nNOTA: Se considera la casilla (0,0) del tablero aquella de la esquina noroeste')
x = int(input('1ª coord casilla inicio: '))
y = int(input('2ª coord casilla inicio: '))
alg = input(' 1- Alg. Profundidad\n 2- Alg. Anchura\n Introducir nº: ')
file = input('Nombre archivo resultados: ')
tiempo1 = time.process_time()
if alg == '1':
    SOLUCIONES = caballo_profundidad([(x,y)],n)
else:
    SOLUCIONES = caballo_anchura((x,y),n)
tiempo2 = time.process_time() - tiempo1

print('Nº soluciones: ',len(SOLUCIONES))
print('Tiempo aproximado de ejecución: ',tiempo2)
print(SOLUCIONES)
print('Para las soluciones ver ' + file + '.txt')

fp = open(file + '.txt','w')
fp.write('\nSOLUCIONES PROBLEMA CABALLO ALG. PROFUNDIDAD \n\n')
fp.write('Casilla de inicio: '+str((x,y))+'\n\n')
fp.write('Tamaño del tablero: '+ str(n))
fp.write('\n\nTiempo aproximado de ejecución: '+ str(tiempo2)+'s \n')
fp.write('\nNº soluciones: '+ str(len(SOLUCIONES))+'\n')
fp.write('\nSoluciones: \n\n')
for c in SOLUCIONES:
    fp.write(str(c) + '\n')
fp.close()
