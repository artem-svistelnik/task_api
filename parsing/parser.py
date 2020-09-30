import csv
import psycopg2
from dotenv import load_dotenv, find_dotenv
import  os
from dotenv import dotenv_values
load_dotenv(find_dotenv())
dot_env_values = dotenv_values()


user = dot_env_values['user']
password = dot_env_values['password']
db_name = dot_env_values['db_name']
connection = psycopg2.connect(user=user,
                              password=password,
                              host="127.0.0.1",
                              port="5432",
                              database=db_name)
cursor = connection.cursor()
try:
    drop_table1 = '''DROP TABLE Products cascade ;'''
    drop_table2 = 'DROP TABLE Reviews;'
    cursor.execute(drop_table1)
    cursor.execute(drop_table2)
    connection.commit()
except Exception as e:
    connection.commit()

create_table1 = '''
    CREATE TABLE Products (
        ID SERIAL,
        Title varchar(255) NOT NULL,
        Asin VARCHAR(255) NOT NULL,
        PRIMARY KEY(Asin)
    );'''
create_table2 = '''
    CREATE TABLE Reviews (
        ID SERIAL,
        Products_asin VARCHAR(255) NOT NULL ,
        Title varchar(255) NOT NULL,
        Review TEXT NOT NULL,
        FOREIGN KEY (Products_asin) REFERENCES  Products(Asin),
        PRIMARY KEY(ID)
    );
'''
cursor.execute(create_table1)
connection.commit()
cursor.execute(create_table2)
connection.commit()

with open('Products.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cursor.execute("Insert into Products (Title,Asin) VALUES ('{}', '{}');".format(row[0].replace("'", "`"), row[1]))

with open('Reviews.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cursor.execute("Insert into Reviews (Products_asin, Title,Review) VALUES ('{}','{}','{}');".format(row[0],
                                                                                          row[1].replace("'", "`"),
                                                                                          row[2].replace("'", "`")))
connection.commit()
connection.close()
