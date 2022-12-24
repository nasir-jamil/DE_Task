#!/usr/bin/env python
import json
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

connection = db.connect()
try:
    results = connection.execute('''
                    SELECT country, count(*)
                    FROM people pp
                    LEFT JOIN places pl ON pl.city = pp.place_of_birth
                    GROUP BY country
                    ''')
except Exception as e:
    print(e)
finally:
    connection.close()

# output the SQL results to a JSON file
if results:
    try:
        with open('/data/output_python.json', 'w') as json_file:
            rows = {row[0]: row[1] for row in results}
            json.dump(rows, json_file, separators=(',', ':'))
            print('Output file generated.')
    except Exception as e:
        print(e)

else:
    print('No Data')

db.dispose()
