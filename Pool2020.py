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
import sys
import subprocess
import os
import os.path
import RPi.GPIO as GPIO
from datetime import datetime, time, timezone
from datetime import datetime as DT
from datetime import date as Date

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, GPIO.HIGH)

feierabend = False
pumpe_an = False

def write_to_log(msg):
    file_name = "/opt/pool.log"
    output = open(file_name, 'a')
    jetzt = datetime.now().strftime("%H_%M_%S")
    output.write(jetzt + " " + msg)
    output.close()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:
    #zwischen 10 und 17 Uhr
    if datetime.now().strftime("%H") > 10 and datetime.now().strftime("%H") <= 16:
        #write_to_log("if datetime.now().strftime(\"%H\") > 10 and datetime.now().strftime(\"%H\") <= 16:")
        #print("if datetime.now().strftime("%H") > 10 or datetime.now().strftime("%H") <= 16:")
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Beim Umstellen auf Arbeit wird feierabend auf False gesetzt
        if feierabend == True:
            write_to_log("Pumpe arbeitet seit ",datetime.now().strftime("%H") , datetime.now().strftime("%M") , datetime.now().strftime("%S"))
            feierabend = False

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #bei 0,10,20,30,40,50 Min und weniger als 21 sec wird die Pumpe angeschaltet
        if datetime.now().strftime("%M") % 10 == 0 and datetime.now().strftime("%S") < 21 and pumpe_an == False:
            print ("Pumpe an um ", datetime.now().strftime("%H") , datetime.now().strftime("%M") , datetime.now().strftime("%S"))
            pumpe_an = True
            GPIO.output(14,GPIO.LOW)
            time.sleep(20)

        #andernfalls ist die Pumpe aus
        else :
            if pumpe_an == True:
                print ("Pumpe aus um ", datetime.now().strftime("%H") , datetime.now().strftime("%M") , datetime.now().strftime("%S"))
                pumpe_an = False
                GPIO.output(14,GPIO.HIGH)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        if feierabend == False:
            feierabend = True
            print ("Pumpe Feierabend um ", datetime.now().strftime("%H") , datetime.now().strftime("%M") , datetime.now().strftime("%S"))
        GPIO.output(14,GPIO.HIGH)
        pause = True

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #solange in der Schleife bis aktuelle Uhrzeit mindestens 10:00 Uhr
        while pause:
            now = time.localtime()
            if datetime.now().strftime("%H") > 9 and datetime.now().strftime("%H") < 17:
                pause = False
            time.sleep(1)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    now = time.localtime()
    #print(datetime.now().strftime("%S"))
    time.sleep(1)
