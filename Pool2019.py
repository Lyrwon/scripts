"""
VIOLET  5V
GRÜN    Ground
Blau    GPIO 14

Modul SRD-05VDC-SL-C
Anschluss

     __     X   Pool
    |
K1   /      X   Außenleiter
    |
    |__     X   Leer
"""

import RPi.GPIO as GPIO
import time
from datetime import datetime as DT
from datetime import date as Date

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, GPIO.HIGH)

feierabend = False
pumpe_an = False
now = time.localtime()
print ("Starttag", now.tm_mday,".",now.tm_mon)
print ("Startzeit", now.tm_hour , now.tm_min , now.tm_sec)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:
    #zwischen 10 und 17 Uhr
    if now.tm_hour > 10 and now.tm_hour <= 16:
        #print("if now.tm_hour > 10 or now.tm_hour <= 16:")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Beim Umstellen auf Arbeit wird feierabend auf False gesetzt    
        if feierabend == True:
            ("Pumpe arbeitet seit ",now.tm_hour , now.tm_min , now.tm_sec)
            feierabend = False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #bei 0,10,20,30,40,50 Min und weniger als 21 sec wird die Pumpe angeschaltet
        if now.tm_min % 10 == 0 and now.tm_sec < 21 and pumpe_an == False:
            print ("Pumpe an um ", now.tm_hour , now.tm_min , now.tm_sec)
            pumpe_an = True
            GPIO.output(14,GPIO.LOW)
            time.sleep(20)
            
        #andernfalls ist die Pumpe aus    
        else :
            if pumpe_an == True:
                print ("Pumpe aus um ", now.tm_hour , now.tm_min , now.tm_sec)
                pumpe_an = False
                GPIO.output(14,GPIO.HIGH)
                
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        if feierabend == False:
            feierabend = True
            print ("Pumpe Feierabend um ", now.tm_hour , now.tm_min , now.tm_sec)
        GPIO.output(14,GPIO.LOW)
        pause = True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #solange in der Schleife bis aktuelle Uhrzeit mindestens 10:00 Uhr
        while pause:
            now = time.localtime()
            if now.tm_hour > 9 and now.tm_hour < 17:
                pause = False
            time.sleep(1)
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    now = time.localtime()
    #print(now.tm_sec)
    time.sleep(1)
