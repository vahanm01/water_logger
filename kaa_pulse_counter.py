import RPi.GPIO as GPIO
import datetime
from datetime import timedelta
import json
import random
import string
import time
import paho.mqtt.client as mqtt
from config import* 



KPC_HOST = "mqtt.cloud.kaaiot.com"  # Kaa Cloud plain MQTT host
KPC_PORT = 1883  # Kaa Cloud plain MQTT port

ENDPOINT_TOKEN = ENDPOINT_TOKEN       # Paste endpoint token
APPLICATION_VERSION = APPLICATION_VERSION  # Paste application version
topic=f'kp1/{APPLICATION_VERSION}/dcx/{ENDPOINT_TOKEN}/json'




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
    
  if GPIO.event_detected(FLOW_SENSOR)==False and init_time < datetime.datetime.now() - timedelta(minutes=10) and pulse > 0:
      #New pulse detection is 13.33 pulses per gallon. We double because there are two reed switches each at halfway.      
      pulse=round(pulse/26.7)
      
      client = mqtt.Client(client_id=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))
      client.connect(KPC_HOST, KPC_PORT, 60)
      client.loop_start()
      
      payload=json.dumps([
                {"gallons": pulse}
                
                ])
      
      result = client.publish(topic=topic, payload=payload)
    
      client.loop_stop()
      client.disconnect()

      pulse = 0
      init_time = datetime.datetime.now()
      pulse_dict={}















