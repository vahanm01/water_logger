#!/usr/bin/python3
import json 
import RPi.GPIO as GPIO
import datetime




import httplib
import urllib
import time
from config import* 

key = ts_api_key  # Put your API Key here


FLOW_SENSOR = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING)

while True:
    
  if GPIO.event_detected(FLOW_SENSOR)==True:
     detect=1
     
     params = urllib.urlencode({'field1': detect, 'key':key }) 
     headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
     conn = httplib.HTTPConnection("api.thingspeak.com:80")
     conn.request("POST", "/update", params, headers)
     conn.close()

     time.sleep(5)
         

  if GPIO.event_detected(FLOW_SENSOR)==False:
      
     params = urllib.urlencode({'field1': 0, 'key':key }) 
     headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
     conn = httplib.HTTPConnection("api.thingspeak.com:80")
     conn.request("POST", "/update", params, headers)
     conn.close()    
     time.sleep(5)     
     
     
