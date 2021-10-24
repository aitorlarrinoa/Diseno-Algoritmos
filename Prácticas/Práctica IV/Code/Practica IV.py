# PRÁCTICA IV - ABRIL/MAYO 2021 - GRUPO 11

import random
from matplotlib.pyplot import *
import time

''' FUNCIONES DE SELECCIÓN '''

def ProntoFinal(Peliculas, ListaFechas):
    eleccion = 999999999
    film = ''
    fechas = ''
    i = 0
    for x0,xF in ListaFechas:
        if xF < eleccion:
            eleccion = xF
            film = Peliculas[i]
            fechas = (x0,xF)   
        i += 1
    return film, fechas

def InicioMasTarde(Peliculas, ListaFechas):
    eleccion = -999999999
    film = ''
    fechas = ''
    i = 0
    for x0,xF in ListaFechas:
        if x0 > eleccion:
            eleccion = x0
            film = Peliculas[i]
            fechas = (x0,xF)
        i += 1
    return film, fechas

def DuraciónMenor(Peliculas, ListaFechas):
    eleccion = 999999999
    film = ''
    fechas = ''
    i = 0
    for x0,xF in ListaFechas:
        if xF-x0 < eleccion:
            eleccion = xF-x0
            film = Peliculas[i]
            fechas = (x0,xF)   
        i += 1
    return film, fechas

''' FUNCIONES AUXILIARES '''

def Ampliable(FechasOcupadas, FechaFilm):
    f0, ff = FechaFilm
    for x0,xF in FechasOcupadas:
        if f0 <= x0 <= ff or f0 <= xF <= ff:
            return False
    return True

def HacerGrafica(Pelis,Fechas,nombre):
    figure()
    for j in range(len(Pelis)):
        a,b = Fechas[j]
        xx = list()
        yy = list()
        ind = int(Pelis[j])
        for i in range(a,b+1):
            xx.append(i)
            yy.append(ind+1)
        plot(xx,yy)
    xlabel('Fechas de grabación')
    ylabel('Pelicula')
    title(nombre)
    savefig(nombre + '.png')
    

''' ALGORITMO VORAZ '''

def Voraz_DisneyPixar(Peliculas, ListaFechas, Seleccion):
    S_peliculas = list()
    S_fechas = list()
    while Peliculas:
        x,fecha = Seleccion(Peliculas, ListaFechas)
        Peliculas.remove(x)
        ListaFechas.remove(fecha)
        if Ampliable(S_fechas,fecha):
            S_peliculas.append(x)
            S_fechas.append(fecha)
    return S_peliculas, S_fechas


''' PROGRAMA PRINCIPAL '''

Peliculas = list()
Listafechas = list()

Tiempos1 = list()
Tiempos2 = list()
Tiempos3 = list()

NumSol1 = list()
NumSol2 = list()
NumSol3 = list()

Tamaño = list()
nrep = 50

print('INICIO')

for n in range(0,200,5):
    
    Time1 = 0
    Time2 = 0
    Time3 = 0
    Tamaño.append(n)
    
    for i in range(n):
        f0 = random.randint(1,34)
        f1 = random.randint(f0+1,38)
        Peliculas.append(str(i))
        Listafechas.append((f0,f1))

    for j in range(nrep):
        L1 = Listafechas[:]
        P1 = Peliculas[:]
        L2 = Listafechas[:]
        P2 = Peliculas[:]
        L3 = Listafechas[:]
        P3 = Peliculas[:]
    
        t1 = time.time()
        Sol_Optima1 = Voraz_DisneyPixar(P1, L1, ProntoFinal)
        t2 = time.time()
        Time1 += t2-t1

        t3 = time.time()
        Sol_Optima2 = Voraz_DisneyPixar(P2, L2, InicioMasTarde)
        t4 = time.time()
        Time2 += t4-t3
        
        t5 = time.time()
        Sol_Optima3 = Voraz_DisneyPixar(P3, L3, DuraciónMenor)
        t6 = time.time()
        Time3 += t6-t5


    Tiempos1.append(Time1/nrep)
    Tiempos2.append(Time2/nrep)
    Tiempos3.append(Time3/nrep)

    NumSol1.append(len(Sol_Optima1[0]))
    NumSol2.append(len(Sol_Optima2[0]))
    NumSol3.append(len(Sol_Optima3[0]))

        
figure()
plot(Tamaño,Tiempos1,Tamaño,Tiempos2,Tamaño,Tiempos3)
xlabel('Tamaño del problema')
ylabel('Tiempo de ejecución')
legend(('ProntoFinal','InicioMasTarde','DuraciónMenor'),loc='upper left')
savefig('AnalisisTemporal.png')

figure()
plot(Tamaño,NumSol1,Tamaño,NumSol2,Tamaño,NumSol3)
xlabel('Tamaño del problema')
ylabel('Numero de soluciones')
legend(('ProntoFinal','InicioMasTarde','DuraciónMenor'),loc='upper left')
savefig('NumeroSoluciones.png')


print('FINAL')






