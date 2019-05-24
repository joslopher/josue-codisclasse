from time import sleep
from graficar import grafic
from leer import lectura

#codi principal

#faig una crida a la funcio distancia

comptador   = 0
temperatura = []
humitat     = []

while True:
    valors =lectura()
    temperatura.append(valors[0])
    humitat.append(valors[1])
    print(valors,temperatura,humitat)
    comptador += 1 			# comptador = comptador +  1
    if comptador == 10:
        grafic(temperatura, humitat) 	# crido la funció grafic (dins de l'arxiu graficar)
        comptador   = 0
        temperatura = []
        humitat     = []
     
    sleep(1)
