#!/usr/bin/env python3
 


from sqlalchemy import create_engine
import RPi.GPIO as GPIO
import datetime
import io
import pandas as pd
from datetime import timedelta
import os
import time
import uuid
import subprocess

print("Initiating GPIO")
FLOW_SENSOR = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING)

pulse_dict={}
pulse = 0
init_time = datetime.datetime.now()


print("Pulse detection is now live.")

#test="TRUE"
#subprocess.call('echo "${}" | /home/pi/water_logger/pulse_counter.py --args'.format(test), shell=True)


#subprocess.call('test=123', shell=True)  
 


#bashCommand = "test=123"
#os.system(bashCommand) 
#os.environ["test"] = "1"

#testing="123"  

while True:
    



  if GPIO.event_detected(FLOW_SENSOR)==True:

     pulse = pulse + 1
     print("Total pulses = " + str(pulse) + ' | ' + str(datetime.datetime.now()))
     time.sleep(.1)  

    
  if GPIO.event_detected(FLOW_SENSOR)==False and init_time < datetime.datetime.now() - timedelta(minutes=1):
      #time.sleep(60)
      print("Threshold met. Upload process initiated.")
      pulse_dict={str(datetime.datetime.now()):pulse}
      pulse_dict = pd.DataFrame(list(pulse_dict.items()), columns=['record_date', 'total_pulses'])
      pulse_dict["type"] = "whole_house"
      pulse_dict["id"] = uuid.uuid4()
      
      engine=create_engine("postgresql://beef:Felicia2020#@water-logger.cmoec5ph6uhr.us-east-1.rds.amazonaws.com:5432/raw_logs")
      conn = engine.raw_connection()
      cur = conn.cursor()
      output=io.StringIO()
      pulse_dict.to_csv(output, sep='\t', header=False, index=False, doublequote=False, escapechar='\\')
      output.seek(0)
      conents=output.getvalue()
      cur.copy_from(output, 'pulse_detection', null="")
      conn.commit()
      
      
      print(str(pulse) + ' Uploaded to DB')
      pulse = 0
      init_time = datetime.datetime.now()
      pulse_dict={}
 
    
              
#with open(os.path.expanduser("~/.bashrc"), "a") as outfile:
  #outfile.write("export water_status=True")
  #outfile.close()        
          

#del os.environ['pgres_user']
#os.environ.get('pgres_user')   
#os.environ('pgres_user')=""
      
