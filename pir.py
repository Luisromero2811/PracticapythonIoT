# Import required Python libraries
import time
import RPi.GPIO as GPIO
import pymongo
import datetime

# Use BCM GPIO references
# instead of physical pin numbers


def movimiento():
  GPIO.setmode(GPIO.BCM)
  GPIO_PIR =18 
  GPIO.setwarnings(False)
  GPIO.setup(GPIO_PIR,GPIO.IN)
  fecha_hora=str(datetime.datetime.now())[:19]
  if GPIO.input(GPIO_PIR):
    print("Se detecta  movimiento")
    valor="Se detecto movimiento"
    time.sleep(1)
  else :
    print("No hay movimiento")
    valor="No hay movimiento..."
    time.sleep(1)
  return {'movimiento':valor,'fecha':fecha_hora}

  # Reset GPIO settings
GPIO.cleanup()
