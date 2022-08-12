#!/usr/bin/env python
# coding: utf-8
import os 
import pandas as pd
import pyarrow
import argparse
from sqlalchemy import create_engine

taxi = pd.read_parquet('../data/yellow_tripdata_2021-01.parquet')

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    parquet_name = 'output.parquet'

    #download parquet file
    os.system('wget {url} -0 {parquet_name}')
    taxi = pd.read_parquet('{parquet_name}')
    
    engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()
    print(pd.io.sql.get_schema(parquet_name,con=engine))
    taxi.to_sql(name=table_name,con=engine ,if_exists='replace')




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest parquet data to Postgres')

    parser.add_argument('--user',help='user name for postgres')
    parser.add_argument('--password',help='password for postgres')
    parser.add_argument('--host',help='host for postgres')
    parser.add_argument('--port',help='port for postgres')
    parser.add_argument('--db',help='database name for postgres')
    parser.add_argument('--table_name',help='table name for postgres')
    parser.add_argument('--url',help='url of the parquet files')

    args = parser.parse_args()
    
    main(args)

