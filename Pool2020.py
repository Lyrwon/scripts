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

import os
import os.path
import RPi.GPIO as GPIO
from datetime import datetime, time, timezone
import time
from datetime import datetime as DT
from datetime import date as Date

def write_to_log(msg):
    file_name = "/opt/pool.log"
    output = open(file_name, 'a')
    jetzt = datetime.now().strftime("%H:%M:%S")
    output.write(msg + " " + jetzt + "\n")
    print(msg + " " + jetzt)
    output.close()

def GPIO_14_on():
    GPIO.output(14, GPIO.LOW)

def GPIO_14_off():
    GPIO.output(14, GPIO.HIGH)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, GPIO.HIGH)

feierabend = False
pumpe_an = False

write_to_log("Programm gestartet um: ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:
    #zwischen 9 und 17 Uhr
    if int(datetime.now().strftime("%H")) > 8 and int(datetime.now().strftime("%H")) <= 17:
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Beim Umstellen auf Arbeit wird feierabend auf False gesetzt
        if feierabend == True:
            write_to_log("Pumpe arbeitet seit: ")
            feierabend = False

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #bei 0,10,20,30,40,50 Min und weniger als 21 sec wird die Pumpe angeschaltet
        if int(datetime.now().strftime("%M")) % 10 == 0 and int(datetime.now().strftime("%S")) < 21  and pumpe_an == False:
            write_to_log("Pumpe an um: ")
            pumpe_an = True
            GPIO_14_on()
            time.sleep(20)

        #andernfalls ist die Pumpe aus
        else :
            if pumpe_an == True:
                write_to_log("Pumpe aus um: ")
                pumpe_an = False
                GPIO_14_off()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        if feierabend == False:
            feierabend = True
        GPIO_14_off()
        pause = True
        write_to_log("Feierabend: ")

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #solange in der Schleife bis aktuelle Uhrzeit mindestens 10:00 Uhr
        while pause:
            now = time.localtime()
            if int(datetime.now().strftime("%H")) > 9 and int(datetime.now().strftime("%H")) < 17:
                pause = False
            time.sleep(1)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    time.sleep(1)

