''' ESTRUCTURA GRÁFICA DEL JUEGO '''
import random

def Reglas():
    print('\n Para leer las instrucciones Pulse CUALQUIER letra. Para jugar ENTER.')
    aa = input()
    if aa != '':
        fp = open('reglas_oso.txt')
        print(fp.read())
        fp.close()
        print(' ¿Jugamos? Click ENTER ')
        bb = input()
        while bb != '':
            print(' ¿Jugamos? Click ENTER ')
            bb = input()

def dibujarTablero(tablero):
   
    print('\n')
    print('\t\t '  + '1' + '   ' + '2' + '   ' + '3' + '   ' + '4' + '   ' + '5' + '   ' + '6'+'\n')
    print('\t\t   |   |   |   |   |   ')
    print('\t     '  + '1' + '   '  + tablero[0][0] + ' | ' + tablero[0][1] + ' | ' + tablero[0][2] + ' | ' + tablero[0][3] + ' | ' + tablero[0][4] + ' | ' + tablero[0][5])
    print('\t\t   |   |   |   |   |   ')
    print('\t\t-----------------------')
    print('\t\t   |   |   |   |   |   ')
    print('\t     '  + '2' + '   '  + tablero[1][0] + ' | ' + tablero[1][1] + ' | ' + tablero[1][2] + ' | ' + tablero[1][3] + ' | ' + tablero[1][4] + ' | ' + tablero[1][5])
    print('\t\t   |   |   |   |   |   ')
    print('\t\t-----------------------')
    print('\t\t   |   |   |   |   |   ')
    print('\t     '  + '3' + '   '  + tablero[2][0] + ' | ' + tablero[2][1] + ' | ' + tablero[2][2] + ' | ' + tablero[2][3] + ' | ' + tablero[2][4] + ' | ' + tablero[2][5])
    print('\t\t   |   |   |   |   |   ')
    print('\t\t-----------------------')
    print('\t\t   |   |   |   |   |   ')
    print('\t     '  + '4' + '   '  + tablero[3][0] + ' | ' + tablero[3][1] + ' | ' + tablero[3][2] + ' | ' + tablero[3][3] + ' | ' + tablero[3][4] + ' | ' + tablero[3][5])
    print('\t\t   |   |   |   |   |   ')
    print('\t\t-----------------------')
    print('\t\t   |   |   |   |   |   ')
    print('\t     '  + '5' + '   '  + tablero[4][0] + ' | ' + tablero[4][1] + ' | ' + tablero[4][2] + ' | ' + tablero[4][3] + ' | ' + tablero[4][4] + ' | ' + tablero[4][5])
    print('\t\t   |   |   |   |   |   ')
    print('\t\t-----------------------')
    print('\t\t   |   |   |   |   |   ')
    print('\t     '  + '6' + '   '  + tablero[5][0] + ' | ' + tablero[5][1] + ' | ' + tablero[5][2] + ' | ' + tablero[5][3] + ' | ' + tablero[5][4] + ' | ' + tablero[5][5])
    print('\t\t   |   |   |   |   |   ')
    print('\n')
    print('CPU: '+ str(tablero[-1][0]))
    print('USUARIO: '+ str(tablero[-1][1]))


def Nivel():
    print('\n Elegir nivel de dificultad: \n')
    print('   1 - Fácil')
    print('   2 - Medio')
    print('   3 - Dificil')
    while True:
        f = input('\n Introducir Nº del nivel de dificultad: ')
        if f in ['1','2','3']:
            f = int(f)
            break
    
    if f == 3:
        n = int(input('\n    Introducir Nº de niveles de exploración: '))
    else:
        n = 1
        
    return f,n
    

def JugadaUsuario(tablero,V):
    pos = (' ',' ')

    while True:
        print('\n ¿Cuál es la posición en la que quiere escribir? fila columna')
        strpos = input()
        if strpos == 'EXIT':
            return 0
        entrada = strpos.split()
        if len(entrada) == 2:
            if entrada[0] in ['1','2','3','4','5','6'] and entrada[1] in ['1','2','3','4','5','6']:
                pos = (int(entrada[0])-1,int(entrada[1])-1)
                if pos  in V:
                    break
                else:
                    print( '\n   ¡AVISO! Casilla ocupada' )
            else:
                print( '\n   ¡AVISO! Coordenadas fuera del tablero' )         
        else:
            print( '\n   ¡AVISO! Formato erroneo' )
        
    letra = ''
    while True:
        print('\n ¿Qué letra desea escribir? S | O')
        letra = input().upper()
        if letra == 'S' or letra == 'O':
            break
        else:
             print( '\n   ¡AVISO! Escriba S,s,O,o' )

    return [letra,pos]

def Escribir(tablero, V, Mov):
    V.remove(Mov[1])
    V.remove(Mov[1])
    (a,b) = Mov[1]
    tablero[a][b] = Mov[0]

def Final(Tablero):
    if Tablero[-1][0] < Tablero[-1][1]:
        print(' \t ¡¡¡ VICTORIA !!!')
    elif Tablero[-1][0] > Tablero[-1][1]:
        print(' \t DERROTA...')
    else:
        print(' Empate')

def revancha():
    Decision = ''
    while Decision not in ['SI','NO']:
        print(' ¿Desea volver a jugar (SI o NO)?')
        Decision = input()
    return Decision == 'SI'


def QuienVaPrimero():
    return random.choice([True,False])


