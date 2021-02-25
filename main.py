import os
from sensor_dht22 import *
from saveJson import *
from pir import *
import time
from ultrasonico import *
from mongo import *
from mysql_ import *



def iniciar():
    valores=temp_hum()
    storeJson(valores,sensor='DHT11')
    storeMongo(valores,sensor='DHT11')
    Insertar(valores,sensor='DHT11')
    valores=movimiento()
    storeJson(valores,sensor='pir')
    storeMongo(valores,sensor='pir')
    Insertar(valores,sensor='pir')
    valores=distancia()
    storeJson(valores,sensor='ultrasonico')
    storeMongo(valores,sensor='ultrasonico')
    Insertar(valores,sensor='ultrasonico')
    os.system("clear")
    


if __name__=='__main__':
    while True:
        iniciar()
        time.sleep(10)
