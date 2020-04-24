#Upgrading to python 3.8 and making it default
https://installvirtual.com/how-to-install-python-3-8-on-raspberry-pi-raspbian/


#Installing sqlalchemy for python 3

sudo apt-get install python3-pip
sudo apt-get install python3-all-dev
sudo pip3 install SQLAlchemy

#installing psycopg2

sudo apt-get install libpq-dev
pip3 install psycopg2



Elastic bean setup
#Install EB CLI
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-windows.html


#launching app on  beanstalk
Create dir with application.py file. Will always look for that and can be changed in config
Include requirements.txt folder with below:

Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0

eb init -p python-3.6 flask-water-logger --region us-east-1

eb create flask-env-water-logger

eb open
eb terminate

debug should be false when deploying
for connecting to RDS postgres, the defined security (default) for the RDS should have inbound rule of custom TCP, port 5432 and anywhere. 

