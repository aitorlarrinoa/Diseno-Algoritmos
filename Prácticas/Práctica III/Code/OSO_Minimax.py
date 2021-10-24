
import random

''' FUNCIONES AUXILIARES '''
def haceroso(casilla,Tablero):
    (a,b)=casilla
    n = len(Tablero[0])
    Num_osos = 0
    if Tablero[a][b] == "O":
        X = [-2,-1,-2,-1,-2,-1,0,0,0,0,2,1,2,1,2,1]
        Y = [2,1,0,0,-2,-1,2,1,-2,-1,2,1,0,0,-2,-1]
        for i in range(0,15,2):
            if 0<= a + X[i] < n and 0<= a + X[i+1] < n and 0<= b + Y[i] < n and 0<= b + Y[i+1] and (Tablero[a + X[i]][b + Y[i]],Tablero[a + X[i+1]][ b + Y[i+1]]) == ('O','S'):
                Num_osos += 1
    else:
        X = [-1,1,0,0,-1,1,-1,1]
        Y = [0,0,-1,1,-1,1,1,-1]
        for i in range(0,7,2):
            if 0<= a + X[i] < n and 0<= a + X[i+1] < n and 0<= b + Y[i] < n and 0<= b + Y[i+1] < n and (Tablero[a + X[i]][b + Y[i]],Tablero[a + X[i+1]][ b + Y[i+1]]) == ('O','O'):
                Num_osos += 1
    return Num_osos

def OSO_O(casilla,Tablero,turno):
    X = [-2,-1,-2,-1,-2,-1,0,0,0,0,2,1,2,1,2,1]
    Y = [2,1,0,0,-2,-1,2,1,-2,-1,2,1,0,0,-2,-1]
    (a,b) = casilla
    n = len(Tablero[0])
    Num_osos = 0
    T = not turno
    for i in range(0,15,2):
        if 0<= a + X[i] < n and 0<= a + X[i+1] < n and 0<= b + Y[i] < n and 0<= b + Y[i+1] and (Tablero[a + X[i]][b + Y[i]],Tablero[a + X[i+1]][ b + Y[i+1]]) == ('O','S'):
            Num_osos += 1
            
    if Num_osos > 0:
        T = not T
            
    if turno: 
        Tablero[-1] = (Tablero[-1][0] + Num_osos, Tablero[-1][1])
    else:
        Tablero[-1] = (Tablero[-1][0], Tablero[-1][1] + Num_osos)
    return T

def OSO_S(casilla,Tablero,turno):
    (a,b) = casilla
    X = [-1,1,0,0,-1,1,-1,1]
    Y = [0,0,-1,1,-1,1,1,-1]
    n = len(Tablero[0])
    Num_osos = 0
    T = not turno
    for i in range(0,7,2):
        if 0<= a + X[i] < n and 0<= a + X[i+1] < n and 0<= b + Y[i] < n and 0<= b + Y[i+1] < n and (Tablero[a + X[i]][b + Y[i]],Tablero[a + X[i+1]][ b + Y[i+1]]) == ('O','O'):
            Num_osos += 1
    if Num_osos > 0:
        T = not T
    if turno:
        Tablero[-1] = (Tablero[-1][0] + Num_osos, Tablero[-1][1])
    else:
        Tablero[-1] = (Tablero[-1][0], Tablero[-1][1] + Num_osos)
    return T

''' FUNCIONES DE EVALUACIÓN '''
def eval1(casilla,Tablero,turno): # Dificil
    return Tablero[-1][0] - Tablero[-1][1]

def eval2(casilla,Tablero,turno): # Medio
    if not turno:
        c=1
    else:
        c=-1
    (a,b)=casilla
    
    Num_osos = haceroso(casilla,Tablero)
    if Num_osos > 0:
        return (-c)*(100 + Num_osos)
    o=0
    s=0
    X=[-1,-1,-1,0,0,1,1,1]
    Y=[1,0,-1,1,-1,1,0,-1]
    n = len(Tablero[0])
    for i in range(8):
        if 0<= a + X[i] < n and 0<= b + Y[i] < n:
            if Tablero[a + X[i]][b + Y[i]] == 'O':
                o+=1
            elif Tablero[a + X[i]][b + Y[i]] == 'S':
                s+=1
    if Tablero[a][b] == 'S' and o-s < 0:
        return c*(10 + abs(o-s))
    elif Tablero[a][b] == 'O' and o-s > 0:
        return c*(10 + abs(o-s))
    elif o-s == 0:
        return random.randint(1,5)
    else:
        return 0

def eval3(casilla,Tablero,turno):# Fácil
    if not turno:
        c=1
    else:
        c=-1
    (a,b)=casilla
    X=[2,2,-1,-1,1,1,-2,-2]
    Y=[-1,1,-2,2,-2,2,-1,1]
    Num_osos = haceroso(casilla,Tablero)
    if Num_osos > 0:
        return (-c)*(10 + Num_osos)
    n = len(Tablero[0])
    for i in range(8):
        if 0<= a + X[i] < n and 0<= b + Y[i] < n and Tablero[a + X[i]][b + Y[i]] == 'O' and Tablero[a][b] == 'O':
            return 5*c
    return 0
    


''' ALGORITMO MINIMAX '''
def minimax(casilla,tablero,V,turno,n,f,alpha=-1000,beta=1000):
    letra = ''
    pos = ''
    if n==0 or not V:  
        return (f(casilla,tablero,turno),[letra,pos])
    elif turno:
        for i in range(len(V)):
            (a,b) = V[i]
            marcador = tablero[-1] 
            if i%2 == 0:
                tablero[a][b] = 'S'
                T = OSO_S(V[i],tablero,turno)
                VV = V[:i] + V[i+2:] 
            else:
                tablero[a][b] = 'O'
                T = OSO_O(V[i],tablero,turno)
                VV = V[:i-1] + V[i+1:]
            Eval=minimax(V[i],tablero,VV,T,n-1,f,alpha,beta)[0]
            if alpha < Eval:
                alpha = Eval
                pos = V[i]
                letra = tablero[a][b]
            tablero[a][b] = ' '
            tablero[-1] = marcador 
            if beta<=alpha:
                break
        return (alpha,[letra,pos])
    else:
        for i in range(len(V)):
            (a,b) = V[i]
            marcador = tablero[-1]
            if i%2 == 0:
                tablero[a][b] = 'S'
                T = OSO_S(V[i],tablero,turno)
                VV = V[:i] + V[i+2:]
            else:
                tablero[a][b] = 'O'
                T = OSO_O(V[i],tablero,turno)
                VV = V[:i-1] + V[i+1:]
            Eval=minimax(V[i],tablero,VV,T,n-1,f,alpha,beta)[0]
            if beta > Eval:
                beta = Eval
                pos = V[i]
                letra = tablero[a][b]
            tablero[a][b] = ' '
            tablero[-1]  = marcador
            if beta<=alpha:
                break
        return (beta,[letra,pos])
