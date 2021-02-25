import Adafruit_DHT
import time
import datetime

def temp_hum():
    fecha_hora=str(datetime.datetime.now())[:19]
    sensor=Adafruit_DHT.DHT11
    pin=4
    humedad,temperatura=Adafruit_DHT.read_retry(sensor, pin)
    print('Fecha Hora',fecha_hora)
    print('Humendad={0:0.1f}'.format(humedad))
    print('Temperatura={0:0.1f}'.format(temperatura))

    

    return {'humedad':humedad,'temp':temperatura,'fecha':fecha_hora}
