

import RPi.GPIO as GPIO
import time, sys
import datetime
import csv
#from csv_test import cleaner

FLOW_SENSOR = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING)
global count
count = 0
file_log="/home/pi/Desktop/Water_Sensor/water_log.csv"

global logger
logger=[]

while True:

   if GPIO.event_detected(FLOW_SENSOR):
      count = count + 1
      logger.append(count)
      file_log_append=open(file_log,'a', newline='')
      csv.writer(file_log_append).writerow([datetime.datetime.now(),max(logger)])
      file_log_append.close()
      print(datetime.datetime.now(),max(logger))

   else:

      count=0
      logger=[]

      



