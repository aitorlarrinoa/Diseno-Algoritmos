''' EJEMPLO '''

Peliculas = list()
Listafechas = list()
for i in range(10):
    f0 = random.randint(1,34)
    f1 = random.randint(f0+1,38)
    Peliculas.append(str(i))
    Listafechas.append((f0,f1))
HacerGrafica(Peliculas, Listafechas, 'Calendario')  
Sol = Voraz_DisneyPixar(Peliculas, Listafechas, ProntoFinal)
HacerGrafica(Sol[0], Sol[1], 'CalendarioOptimo')

print('ejemplo completado')
