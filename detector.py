import json 
import RPi.GPIO as GPIO
import datetime


FLOW_SENSOR = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING)




while True:
    
  if GPIO.event_detected(FLOW_SENSOR)==True:

     pulse_dict={'timestamp':str(datetime.datetime.now()), 'flow':str('True')}
     
     with open('C:/Users/vahan/water_logger/detector.json', 'w') as fp:
         json.dump(pulse_dict, fp)

  if GPIO.event_detected(FLOW_SENSOR)==False:

     pulse_dict={'timestamp':str(datetime.datetime.now()), 'flow':str('False')}
     
     with open('C:/Users/vahan/water_logger/detector.json', 'w') as fp:
         json.dump(pulse_dict, fp)  
