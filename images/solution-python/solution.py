#!/usr/bin/env python

import pandas
from sqlalchemy import create_engine

db_driver = 'mysql+mysqlconnector'
db_name = 'db'
db_user = 'db_user'
db_pass = 'db_pass'
db_host = 'db_server'
db_port = 3306


# Connect to the database
try:
    db_string = '{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(db_driver, db_user, db_pass, db_host, db_port, db_name)
    db = create_engine(db_string,  echo=False)
except Exception as e:
    print(e)


# Iterate over files and store it in DB
files = ['places', 'people']

for file in files:
    try:
        df = pandas.read_csv('/data/' + file + '.csv', encoding='utf-8')  # encoding='ISO-8859-1'
        df.to_sql(con=db, name=file, if_exists='replace', index=False, method='multi')
        print(f'Data for {file} file inserted.')
    except Exception as e:
        print(f'Error in  {file} file  with exception as', e)