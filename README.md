#Upgrading to python 3.8 and making it default
https://installvirtual.com/how-to-install-python-3-8-on-raspberry-pi-raspbian/

#Installing sqlalchemy for python 3

sudo apt-get install python3-pip
sudo apt-get install python3-all-dev
sudo pip3 install SQLAlchemy

#installing psycopg2

sudo apt-get install libpq-dev
pip3 install psycopg2

#Auto lan
```bash
sudo /etc/network/interfaces
```

include following:
auto wlan0
iface wlan0 inet dhcp
wpa-ssid {network name}
wpa-psk {password}
sudo dhclient wlan0


#Detached script run
```bash
nohup python3 -u pulse_counter.py &
```

```bash
tail -f nohup.out
```

Above shows the current output of script. Must be pointing to directory where you run script detached. 

#Disable Wifi power management and check settings
```bash
sudo iwconfig wlan0 power off
sudo iwconfig
```

#SSH into EC2
Attach IAM role (full admin access EC2 role) to EC2 instance. I went into the default EC2 role and allowed full admin access.
Then go to session manager and should appear there.

#Check Python jobs
```bash
ps -aef | grep python
```

#Startup scripts/commands
At root, edit the /etc/rc.local file with below commands. Not the commands to run scripts at PI user, where Python packages are installed.
```bash
iwconfig wlan0 power off
sudo -H -u pi /usr/bin/python3 /home/pi/water_logger/pulse_counter.py > /home/pi/water_logger/pulse_counter_log.log 2>&1 &
sudo -H -u pi /usr/bin/python3 /home/pi/water_logger/detector.py > /home/pi/water_logger/detector_log.log 2>&1 &
```

## Config file
Within the local repo on the RPi side, you will need a config.py file as a credentials manager. Do not push to web. 

pgress_pass=<your password to DB>

#Troubleshooting
Cannot SSH to RPi outside network. Restart routers, check routher NAT forwarding virtual servers. Refresh port 22 by clicking status button or restart the virtual server; or reset.

#Wiring
Reed switch Vdd will have 10k resistor to 3.3v. GPIO white wire to GPIO pin will have 1k resistor. Black to groud on GPIO.  