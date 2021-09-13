import RPi.GPIO as GPIO
import dht11
import time
import datetime
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
# read data using pin 14
#now = datetime.datetime.now()
instance = dht11.DHT11(pin = 4)
f1=open("temp.txt","w")
result = instance.read()
x=0
for x in range(24):
        GPIO.output(16,True)
        if result.is_valid():
                f1.write(str(datetime.datetime.now())+"\t"+" temp:"+str(result.temperature)+"  humidity:"+str(result.humidity))     
        else:
                print("Error: %d" % result.error_code)

        time.sleep(1)
        GPIO.output(16,False)
        time.sleep(1)
        
        time.sleep(3600)


GPIO.cleanup()
f1.close()


