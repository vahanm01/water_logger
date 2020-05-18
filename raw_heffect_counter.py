
from sqlalchemy import create_engine
import RPi.GPIO as GPIO
import datetime
import io


import pandas as pd
from datetime import timedelta
import os


print("initiating GPIO")
FLOW_SENSOR = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING)

raw_dict={}
count = 0
init_time = datetime.datetime.now()


  
print("begin listening loop")

while True:

  if GPIO.event_detected(FLOW_SENSOR)==True:

     count = count + 1
     print("total pulses..." + str(count))
     
      

    
  if GPIO.event_detected(FLOW_SENSOR)==False and init_time < datetime.datetime.now() - timedelta(seconds=60):
      #time.sleep(60)
      print("threshold met. Upload process begin")
      raw_dict={str(datetime.datetime.now()):count}
      raw_dict = pd.DataFrame(list(raw_dict.items()), columns=['record_date', 'total_count'])
      raw_dict["type"] = "whole_house"
      
      engine=create_engine("postgresql://beef:Felicia2020#@water-logger.cmoec5ph6uhr.us-east-1.rds.amazonaws.com:5432/raw_logs")
      conn = engine.raw_connection()
      cur = conn.cursor()
      output=io.StringIO()
      raw_dict.to_csv(output, sep='\t', header=False, index=False, doublequote=False, escapechar='\\')
      output.seek(0)
      conents=output.getvalue()
      cur.copy_from(output, 'raw_effect_counts', null="")
      conn.commit()
      
      
      print(str(count) + ' uploaded')
      count = 0
      init_time = datetime.datetime.now()
      raw_dict={}
 
    
              
       #with open(os.path.expanduser("~/.bashrc"), "a") as outfile:
         #outfile.write("export water_status=True")
         #outfile.close()        
          
#import os

#del os.environ['pgres_user']
#os.environ.get('pgres_user')   
#os.environ('pgres_user')=""
      
