import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "postgres",password = "Kandra5moneR",host="localhost",port="5432",database = "Recommendations")

    cursor = connection.cursor()
    create_table_query = ''' CREATE TABLE IF NOT EXISTS users
    (ID SERIAL PRIMARY KEY NOT NULL , USERNAME TEXT NOT NULL,PASSWORD TEXT NOT NULL )
    '''
    cursor.execute(create_table_query)
    connection.commit()
    print('Table was created')
except (Exception,psycopg2.DatabaseError) as error:
    print("Occured error while initialising database")
finally:
    #closing database connection
        if (connection):
            cursor.close()
            connection.close()
            print("Connection is closed")
