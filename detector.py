#!/bin/bash

import json 
import RPi.GPIO as GPIO
import datetime
import time

FLOW_SENSOR = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING)




while True:
    
  if GPIO.event_detected(FLOW_SENSOR)==True:
     detect='True' 
     pulse_dict={'timestamp':str(datetime.datetime.now()), 'flow':str('True')}
     
     with open('/home/pi/water_logger/detector_output.json', 'w') as output_file:
         json.dump(pulse_dict, output_file)
    
     output_file.close()     
     time.sleep(5)
         
     
    
    

  if GPIO.event_detected(FLOW_SENSOR)==False:

     pulse_dict={'timestamp':str(datetime.datetime.now()), 'flow':str('False')}
     
     with open('/home/pi/water_logger/detector_output.json', 'w') as output_file:
         json.dump(pulse_dict, output_file)  
     output_file.close()           
     time.sleep(5)     