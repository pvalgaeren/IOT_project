#!/usr/bin/env python
# library import
import RPi.GPIO as GPIO
import time
from datetime import datetime
import MySQLdb
import cgitb
import imp ; cgitb.enable() 
import spidev 

#initialiseer variabelen
time_off_measurement = datetime.now
measurements_digitalmeter = 0
measurements_classicalmeter = 0
pulse_meter = 0 

#Verbinden met de database
database = MySQLdb.connect(host="localhost", user="pi", passwd="raspberry",db="mydb")
#database select
cursor = database.cursor()


spi = spidev.SpiDev() # create spi object
spi.open(0,0) # open spi port 0, device CS0 pin 24
spi.max_speed_hz=(1000000) 


# read SPI data 8 possible adc's (0 thru 7) 
def readadc(adcnum): 
 if ((adcnum > 7) or (adcnum < 0)): 
    return -1 
 r 		= spi.xfer2([1,(8+adcnum)<<4,0]) 
 adcout = ((r[1]&3) << 8) + r[2] 
 return adcout 


cursor.execute("INSERT INTO lightandtemp(measurements_digitalmeter, measuerments_classicalmeter, pulse_meter, time_off_measurement) VALUES( %s, %s, %s, %s)",(measurements_digitalmeter, measurements_classicalmeter, pulse_meter, time_off_measurement))
database.commit()
 
    
print(measurements_digitalmeter)
print(measurements_classicalmeter)
print(pulse_meter)
print(time_off_measurement)
time.sleep(1)
    
