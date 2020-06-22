"""
Vorgabe ist:
Zwischen 10 und 16 Uhr immer zur vollen 10min Pumpe für 20 sec anschalten
"""
import RPi.GPIO as GPIO
import time
from datetime import datetime as DT
from datetime import date as Date
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.HIGH)
status = "Y"
loop = 1
anschalten = [10,20,30,40,50,00] #in minuten
ausschalten = [20] #in sekunden
#Aktuelle Uhrzeit zwischenspeichern
now = time.localtime()
nowh = now.tm_hour
nowm = now.tm_min
nows = now.tm_sec
print ("Starttag", now.tm_mday,".",now.tm_mon)
print ("Startzeit", nowh , nowm, nows)

print("hh mm ss")
while loop == 1:
    #Pumpe ausschalten
    if status != 0:
        #Pumpe ausschalten
        print("Standard Pumpe aus")
        GPIO.output(24, GPIO.HIGH)
        status = 0
    #localtime nehmen
    now = time.localtime()
    nowh = now.tm_hour
    nowm = now.tm_min
    nows = now.tm_sec
    #anzeige verschönern
    if nowh < 10 or nowh >= 16 and nows>=10 and nows<=59:
        print ("XXX Zwischen 16 und 10 Uhr XXX")
        print (nowh , nowm, nows,"Außenloop")
        time.sleep(60)
    elif nowh < 10 or nowh >= 16 and nows>=0 and nows<=9:
        if nows == 0:
            nowss = "00"
        elif nows == 1:
            nowss = "01"
        elif nows == 2:
            nowss = "02"
        elif nows == 3:
            nowss = "03"
        elif nows == 4:
            nowss = "04"
        elif nows == 5:
            nowss = "05"
        elif nows == 6:
            nowss = "06"
        elif nows == 7:
            nowss = "07"
        elif nows == 8:
            nowss = "08"
        elif nows == 9:
            nowss = "09" 
            print ("XXX Zwischen 16 und 10 Uhr XXX")
            print (nowh , nowm, nowss,"Außenloop")
            time.sleep(60)
    else:
        print ("XXX Zwischen 10 und 16 Uhr XXX")
        #zwischen 10 und 16 uhr Steuerung anschalten
        #Aktuelle Uhrzeit zwischenspeichern
        now = time.localtime()                      #gesamte localtime
        nowh = now.tm_hour                          #stunden
        nowm = now.tm_min                           #minuten
        nows = now.tm_sec
        while nowh >= 10 and nowh < 16:
            time.sleep(20)
                                                        #Aktuelle Uhrzeit zwischenspeichern
            now = time.localtime()                      #gesamte localtime
            nowh = now.tm_hour                          #stunden
            nowm = now.tm_min                           #minuten
            nows = now.tm_sec                           #sekunden
            print ("steuerung an",nowh , nowm, nows)    #Anzeige
            for x in anschalten:                        #anschalten array der reihe nach durchsuchen, ob nows einem wert des arrays entspricht 
                if x == nowm and status == 0:           #wenn x gleich minute und pumpe aus 
                    status = 1                          #setze status auf 1
                    GPIO.output(24, GPIO.LOW)           #Raspberry Ausgang HIGH-schalten
                    print("                              ~~ ON ~~",nowh , nowm, nows)                   #anzeige das Pumpe an
                    time.sleep(1)
                    print("1")
                    time.sleep(1)
                    print("2")
                    time.sleep(1)
                    print("3")
                    time.sleep(1)
                    print("4")
                    time.sleep(1)
                    print("5")
                    time.sleep(1)
                    print("6")
                    time.sleep(1)
                    print("7")
                    time.sleep(1)
                    print("8")
                    time.sleep(1)
                    print("9")
                    time.sleep(1)
                    print("10")
                    time.sleep(1)
                    print("11")
                    time.sleep(1)
                    print("12")
                    time.sleep(1)
                    print("13")
                    time.sleep(1)
                    print("14")
                    time.sleep(1)
                    print("15")
                    time.sleep(1)
                    print("16")
                    time.sleep(1)
                    print("17")
                    time.sleep(1)
                    print("18")
                    time.sleep(1)
                    print("19")
                    time.sleep(1)
                    print("20")
                    status = 0                                  #setze status auf 0
                    GPIO.output(24, GPIO.HIGH)                  #Raspberry Ausgang HIGH-schalten
                    now = time.localtime()                      #gesamte localtime
                    nowh = now.tm_hour                          #stunden
                    nowm = now.tm_min                           #minuten
                    nows = now.tm_sec 
                    print (nowh , nowm, nows)                   #Zeitstempel
                    print("                              ~~~OFF~~~",nowh , nowm, nows)                  #anzeige das Pumpe aus
                    time.sleep(50)                              #50sec nichts tun
            
