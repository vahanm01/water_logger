# -*- coding: utf-8 -*-
"""
Functions for pulse_counter and detector

@author: vahan
"""
import psycopg2
from sqlalchemy import create_engine
import io
import pandas as pd
import os
from config import* 

def pgres_engine (user, passwd):
    user=user
    passwd=passwd
    engine = create_engine(f'postgresql://{user}:{passwd}@water-logger.cmoec5ph6uhr.us-east-1.rds.amazonaws.com:5432/raw_logs')
    return engine

def pgres_engine_uploader(data, table): 
    engine = pgres_engine('beef', pgres_pass)
    table=str(table)
    data=data
    conn = engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()
    data.to_csv(output, sep='\t', header=False, index=False, doublequote=False,escapechar='\\')
    output.seek(0)
    contents = output.getvalue()
    cur.copy_from(output, table, null="") # null values become ''
    conn.commit()



