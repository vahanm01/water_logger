
#!/usr/bin/env python3


from pythonping import ping
import time


while True:
    
    ping('google.com', verbose=True)
    time.sleep(60)
