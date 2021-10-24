
from Estructura_grafica import *
from OSO_Minimax import *
import random
import time

print( '- JUEGO DEL OSO - DISEÑO DE ALGORITMOS 2021 - GRUPO 11  - \n')
print( ' Activar: Bloq Mayus \n')
print( ' Para detener el juego escribir: EXIT \n')

# Reglamento
Reglas()


while True:
    
    # Nivel de dificultad
    f,n = Nivel()
    Nombres_Funciones = [eval3,eval2,eval1]
    f_eval = Nombres_Funciones[f-1]
    
    # Creamos el tablero vacio
    tablero = [[' 'for i in range(6)]for j in range(6)]
    tablero.append((0,0)) 
    dibujarTablero(tablero)

    tiempos = list()
    tiemp_med = 0
    num = 0

    # Casillas libres minimax
    V = [] 
    for i in range(6):
        for j in range(6):
            V.append((i,j))
            V.append((i,j))
            
    # Turno Inicial
    if QuienVaPrimero():
        turno = True
        print("\n Ups! Comienza jugando la CPU\n")
    else:
        turno = False
        print("\n Enhorabuena!! Te toca empezar!\n")
    
    seEstajugando = True

    while seEstajugando:
        
        if not turno: # Turno jugador

            Mov = JugadaUsuario(tablero,V)

            if Mov == 0: # Detener el juego
                break
            
            Escribir(tablero,V,Mov)
            

            # Análisis del turno tras jugada
            if Mov[0] == 'O':
                turno = OSO_O(Mov[1],tablero,turno)   
            else:
                turno = OSO_S(Mov[1],tablero,turno)

            dibujarTablero(tablero)

            # Estudio de Fin juego    
            if not V:
                seEstajugando = False
                print('\n\nTiempos de ejecución por jugada de CPU: \n')
                print(tiempos)
                print('\n Tiempo medio de jugada: ', tiemp_med/num)
                Final(tablero)               
                

        else: # Turno del ordenador

            t1 = time.time()
            Mov = minimax(' ',tablero,V,True,n,f_eval)[1]
            t2 = time.time()
            tiempos.append(str(t2-t1))
            tiemp_med += (t2-t1)
            num += 1

            Escribir(tablero,V,Mov)

            # Análisis del turno tras jugada
            if Mov[0] == 'O':
                turno = OSO_O(Mov[1],tablero,turno)   
            else:
                turno = OSO_S(Mov[1],tablero,turno)

            dibujarTablero(tablero)

            # Estudio de Fin juego
            if not V:
                seEstajugando = False
                print('\n\nTiempos de ejecución por jugada de CPU: \n')
                print(tiempos)
                print('\n Tiempo medio de jugada: ', tiemp_med/num)
                Final(tablero)
                

            
    if not revancha():
        print( '\n \t FIN DEL JUEGO \n')
        break
