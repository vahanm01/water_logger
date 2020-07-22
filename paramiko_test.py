
import paramiko
import json

    
client =  paramiko.client.SSHClient()
hostname='98.210.69.250'
#hostname='192.168.0.88'
port=22
username='pi'
password='Felicia2020#'


client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
client.load_system_host_keys()
print('loaded client')
client.connect(hostname, port, username, password)
print('connection made')

sftp_client = client.open_sftp()

localFilePath='./detector_output.json'
sftp_client.get('/home/pi/water_logger/detector_output.json', localFilePath)
    
sftp_client.close() 


with open(localFilePath) as detector_output:
  flow_data = json.load(detector_output)
  
flow_eval=str(flow_data['flow'])

print(str(flow_eval))
