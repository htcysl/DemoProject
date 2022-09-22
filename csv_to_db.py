import os
import pandas as pd
import psycopg2 

# list of csv files in demo directory
csv_files = [] 
for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
      csv_files.append(file)

# csv to pandas dataframe 
df = {}
for file in csv_files:
    df[file] = pd.read_csv(file)

# a dictionary that maps pandas dtypes to sql dtypes
replacements = {
    'object':'varchar',
    'float64':'float',
    'int64' : 'int',
    'datetime64':'timestamp',
    'timedelta64[ns]': 'varchar'
}

for k in csv_files:
    dataframe = df[k]
    
    # create table name same as csv file  without .csv extension
    tbl_name = '{0}'.format(k.split('.')[0])
    # replace [ and ] characters with  _ 
    dataframe.columns = [x.replace("[","_").replace("]","_") for x in dataframe.columns]
    # table schema
    col_str = ", ".join("{} {}".format(n,d) for (n,d) in zip(dataframe.columns,dataframe.dtypes.replace(replacements)))
    
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
    
        # drop table with the same name 
        cursor.execute("drop table if exists %s;" % (tbl_name))
        
        # create table
        cursor.execute("create table %s (%s)" % (tbl_name,col_str)) 
        print('{0} was created successfully'.format(tbl_name))
        
        # insert values to table
        # save df to csv
        dataframe.to_csv(k,header=dataframe.columns, index=False,encoding='utf-8')

        # open the csv file, save it as an object
        my_file = open(k)
        print("file is opened in memory")
    
        # upload to db
        SQL_STATEMENT = """COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ',' """ 
        cursor.copy_expert(sql=SQL_STATEMENT % tbl_name,file=my_file) 
        print("file copied to db")

        conn.commit()
    except Exception as error:
         print(error)   

    finally:
        if cursor is not None:
          cursor.close()
        if conn is not None:
          conn.close()
