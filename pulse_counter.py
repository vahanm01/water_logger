#!/usr/bin/python3

import RPi.GPIO as GPIO
import datetime
import pandas as pd
from datetime import timedelta
import time
import uuid
from helpers import*

FLOW_SENSOR = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING)

pulse_dict={}
pulse = 0
init_time = datetime.datetime.now()

while True:

  if GPIO.event_detected(FLOW_SENSOR)==True:

     pulse = pulse + 1
     time.sleep(.1)  
    
  if GPIO.event_detected(FLOW_SENSOR)==False and init_time < datetime.datetime.now() - timedelta(minutes=15) and pulse > 0:

      pulse_dict={str(datetime.datetime.now()):pulse}
      pulse_dict = pd.DataFrame(list(pulse_dict.items()), columns=['record_date', 'total_pulses'])
      pulse_dict["type"] = "whole_house"
      pulse_dict["id"] = uuid.uuid4()
      
      pgres_engine_uploader(pulse_dict, 'pulse_detection')

      pulse = 0
      init_time = datetime.datetime.now()
      pulse_dict={}
