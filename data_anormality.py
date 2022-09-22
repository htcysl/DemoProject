import pandas as pd
import psycopg2 
import math

# open database connection
hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'admin' 
port_id = 5432
conn = None
cursor = None
try:
        conn = psycopg2.connect(host=hostname, dbname=database, user= username, password=pwd, port=port_id)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM angular_velocity')
            
        update_str = "UPDATE angular_velocity SET type = %s where time = %s" 

        for record in cursor.fetchall():
               result =  math.sqrt( pow(record[2],2) + pow(record[3],2) )*100 >= 30.0 
               if result:
                  val = ("1",record[5])
                  cursor.execute(update_str,val)
               else :
                  val = ("0",record[5])
                  cursor.execute(update_str,val)
                
        conn.commit()
except Exception as error:
         print(error)   

finally:
        if cursor is not None:
          cursor.close()
        if conn is not None:
          conn.close()
