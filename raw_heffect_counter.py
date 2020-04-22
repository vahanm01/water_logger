

from sqlalchemy import create_engine
import psycopg2

import RPi.GPIO as GPIO
import time, sys
import datetime
import csv
import io
import pandas as pd
#from csv_test import cleaner




FLOW_SENSOR = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING)
global count
count = 0
file_log="/home/pi/Desktop/Water_Sensor/water_log.csv"





test_dict={}
test_dict={str(datetime.datetime.now()):15}
test_dict[str(datetime.datetime.now())]=15
test_dict[str(datetime.datetime.now())]=20


test_dict = pd.DataFrame(list(test_dict.items()), columns=['record_date', 'total_count'])

#global logger
#logger=[]
x=1


while True:

   if GPIO.event_detected(FLOW_SENSOR):
       count = count + 1
      
  engine=create_engine('postgresql://beef:Felicia2020#@water-logger.cmoec5ph6uhr.us-east-1.rds.amazonaws.com:5432/raw_logs')
  conn = engine.raw_connection()
  cur = conn.cursor()
  output=io.StringIO()
  test_dict.to_csv(output, sep='\t', header=False, index=False, doublequote=False, escapechar='\\')
  output.seek(0)
  conents=output.getvalue()
  cur.copy_from(output, 'raw_effect_counts', null="")
  conn.commit()
  count = 0
  test_dict={}

   else:

      count=0
      test_dict={}
      
      
      
      
      
      
      
      



keys = test_dict.keys()
columns = ','.join(keys)
values = ','.join(['%({})s'.format(k) for k in keys])
insert = 'insert into raw_effect_counts ({0} values ({1})'.format(columns, values)
print(cursor.mogrify(insert, test_dict))





