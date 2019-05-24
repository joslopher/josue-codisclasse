import cayenne.client
from random import randint
from time import sleep

def lectura():
    temperatura = randint(10,35)
    humitat     = randint(50,100)
    return temperatura,humitat

def tocloud(valors):
    temperatura = valors[0]
    humitat     = valors[1]
    client.virtualWrite(1,temperatura)
    client.virtualWrite(2,humitat)

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME	= "57566e80-7c79-11e9-9636-f9904f7b864b"
MQTT_PASSWORD	= "31f97a16c29f50b41a5e7c863bc763c5b0180686"
MQTT_CLIENT_ID	= "45352210-7c87-11e9-b4eb-6bf2c2412b24"
client		= cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

while True:
    client.loop()
    valors = lectura()
    if valors[0]>30 and valors[1]>80:
        tocloud(valors)
    sleep(0.5)
