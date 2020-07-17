import json 
import RPi.GPIO as GPIO
import datetime


FLOW_SENSOR = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING)




while True:
    
  if GPIO.event_detected(FLOW_SENSOR)==True:
     detect='True' 
     pulse_dict={'timestamp':str(datetime.datetime.now()), 'flow':str('True')}
     
     with open('/home/pi/water_logger/detector.json', 'w') as output_file:
         json.dump(pulse_dict, output_file)
         
     
    
    

  if GPIO.event_detected(FLOW_SENSOR)==False:

     pulse_dict={'timestamp':str(datetime.datetime.now()), 'flow':str('False')}
     
     with open('/home/pi/water_logger/detector.json', 'w') as output_file:
         json.dump(pulse_dict, output_file)  
         
     