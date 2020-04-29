
from sqlalchemy import create_engine
import psycopg2
import time, sys
import datetime
import csv
import io
import pandas as pd
from datetime import datetime


init_df=pd.read_csv("C://Users//vmouradian//Desktop//historical_water_logs.csv")


def water_query_results(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    query_fetch = cursor.fetchall()
    cols = list(map(lambda x: x[0], cursor.description))
    query_fetch=pd.DataFrame(query_fetch, columns=cols)
    return query_fetch


def water_pgres(user, password):
    connection = psycopg2.connect(user = user,
                                  password = password,
                                  host = "water-logger.cmoec5ph6uhr.us-east-1.rds.amazonaws.com",
                                  port = "5432",
                                  database = "raw_logs")
    return connection



connection = water_pgres("beef", "Felicia2020#")  

init_df=water_query_results(f"select* from raw_effect_counts", connection)


init_df=init_df
init_df["gallons"]=float(0)
init_df.record_date=init_df.record_date.dt.date

#Group by date to combine same month dates
init_df=init_df.groupby(['record_date']).sum()


init_df.gallons=init_df.total_count/1800












#Convert to actual date time if needed
init_df.record_date=pd.to_datetime(init_df.record_date)
init_df.dtypes




sum(init_df.gallons)



engine=create_engine('postgresql://beef:Felicia2020#@water-logger.cmoec5ph6uhr.us-east-1.rds.amazonaws.com:5432/raw_logs')
conn = engine.raw_connection()
cur = conn.cursor()
output=io.StringIO()
init_df.to_csv(output, sep='\t', header=False, index=False, doublequote=False, escapechar='\\')
output.seek(0)
conents=output.getvalue()
cur.copy_from(output, 'raw_effect_counts', null="")
conn.commit()