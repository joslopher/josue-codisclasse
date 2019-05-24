from random import randrange

def lectura():
    #codi del del sensor dht11 velleman temperatura i humitat
    temperatura = randrange(10,35)
    humitat	= randrange(50,100)
    return temperatura,humitat