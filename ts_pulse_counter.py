#!/usr/bin/python3

import RPi.GPIO as GPIO
import datetime
from datetime import timedelta

import httplib
import urllib
import time
from config import* 

FLOW_SENSOR = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING)

pulse_dict={}
pulse = 0
init_time = datetime.datetime.now()
key = ts_api_key 


while True:

  if GPIO.event_detected(FLOW_SENSOR)==True:

     pulse = pulse + 1
     time.sleep(.1)  
    
  if GPIO.event_detected(FLOW_SENSOR)==False and init_time < datetime.datetime.now() - timedelta(minutes=1) and pulse > 0:
      #New pulse detection is 13.33 pulses per gallon. We double because there are two reed switches each at halfway.      
      pulse=pulse/26.7
      
    
      
      params = urllib.urlencode({'Gallons': pulse, 'key':key }) 
      headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
      conn = httplib.HTTPConnection("api.thingspeak.com:80")
      conn.request("POST", "/update", params, headers)
      conn.close()

      pulse = 0
      init_time = datetime.datetime.now()
      pulse_dict={}

