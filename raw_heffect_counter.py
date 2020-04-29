
from sqlalchemy import create_engine
import RPi.GPIO as GPIO
import datetime
import io
import pandas as pd
from datetime import timedelta

pgres_user=""
pgres_pass=""

FLOW_SENSOR = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING)

raw_dict={}
count = 0

  
while True:

  if GPIO.event_detected(FLOW_SENSOR)==True:
     init_time = datetime.datetime.now()
     count = count + 1


    
  if GPIO.event_detected(FLOW_SENSOR)==False and count > 15 and init_time < datetime.datetime.now() - timedelta(seconds=60):
      #time.sleep(60)
      print("threshold met. Upload process begin")
      raw_dict={str(datetime.datetime.now()):count}
      raw_dict = pd.DataFrame(list(raw_dict.items()), columns=['record_date', 'total_count'])
      
      
      engine=create_engine('postgresql://{pgres_user}:{pgres_pass}#@water-logger.cmoec5ph6uhr.us-east-1.rds.amazonaws.com:5432/raw_logs')
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
      raw_dict={}
 
    
              
          
          
          
      
      
      
