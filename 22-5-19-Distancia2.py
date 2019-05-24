from random import randint
from time import sleep

'''
import cayenne
'''

def cayenne(valors):
    temperatura = valors[0]
    humitat     = valors[1]

def lectura():
    #codi del sensor dht11 velleman temperatura i humitat
    temperatura = randint(10,35)
    humitat     = randint(50,100)
    return temperatura,humitat

#codi principal

while True:
    valors = lectura()
    cayenne(valors)
    sleep(0.5)

