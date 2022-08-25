
import mysql.connector
from mysql.connector import Error
import pymysql
import pandas as pd

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='socker',
                                         user='root',
                                         password='lucinka2004')
    sql_select_Query = "select * from client"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    df = pd.DataFrame(records, columns=['client_id', 'client_name', 'branch_id'])
    print(df)
    print('The data type of df is: ', type(df))

except Error as e:
    print("Error while connecting to MySQL", e)



finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")