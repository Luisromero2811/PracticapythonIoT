import RPi.GPIO as GPIO
import time
import pymongo
import datetime



def distancia():
    
    try:
        fecha_hora=str(datetime.datetime.now())[:19]
        GPIO.setmode(GPIO.BCM)
        
        TRIG = 23
        ECHO = 24
        
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.setwarnings(False)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO) == False:
            start = time.time()
        
        while GPIO.input(ECHO) == True:
            end = time.time()
        
        sig_time = end-start
        
        #CM:
        distance = sig_time / 0.000058
        
        #inches:
        #distance = sig_time / 0.000148


        #print('Distance: {0:0.2f} centimeters'.format(distance))
        

    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        print("Keyboard interrupt")

    except:
        print("some error")
    

    finally:
        print("clean up") 
        GPIO.cleanup() # cleanup all GPIO 

    return {'distancia':distance,'fecha':fecha_hora}
