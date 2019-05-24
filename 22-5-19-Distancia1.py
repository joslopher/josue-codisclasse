from random import randint
from time import sleep

'''
import de les llibreries específiques del sensor de distància
que fem servir com a comptapersones
import dv345
'''

def grafica(llista1,llista2):
    #amb matplotlib.pyplot graficarem les dates
    pass

def lectura():
    #codi del sensor dht11 velleman temperatura i humitat
    temperatura = randint(10,35)
    humitat     = randint(50,100)
    return temperatura,humitat

#codi principal

#faig una crida a la funció distància

comptador   = 0
temperatura = []
humitat     = []

while True:
    valors  = lectura()
    temperatura.append(valors[0])
    humitat.append(valors[1])
    print(valors,temperatura,humitat)
    comptador += 1                      # comptador = comptador + 1
    if comptador == 10:
        grafica(temperatura, humitat)   # ara mateix té 10 valors
        comptador   = 0
        temperatura = []
        humitat     = []
    sleep(0.5)

