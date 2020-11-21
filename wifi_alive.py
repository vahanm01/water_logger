# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 13:26:41 2020

@author: vahan
"""



from pythonping import ping
import time


while True:
    
    ping('google.com', verbose=True)
    time.sleep(60)
