import csv
import psycopg2
from psycopg2 import Error
connection = psycopg2.connect(user = "postgres",
                              password = "1",
                              host = "127.0.0.1",
                              port = "5432",
                              database = "postgres")

cursor = connection.cursor()
drop_table1='''DROP TABLE Products cascade ;'''
drop_table2='DROP TABLE Reviews;'
cursor.execute(drop_table1)
cursor.execute(drop_table2)
connection.commit()
create_table1='''
    CREATE TABLE Products (
        ID SERIAL,
        Title varchar(255) NOT NULL,
        Asin VARCHAR(255) NOT NULL,
        PRIMARY KEY(Asin)
    );'''
create_table2='''
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
        print(len(row))
        cursor.execute("Insert into Products (Title,Asin) VALUES ('{}', '{}');".format(row[0].replace("'","`"), row[1]))

with open('Reviews.csv', 'r') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        cursor.execute("Insert into Reviews (Products_asin, Title,Review) VALUES ('{}','{}','{}');".format(row[0],
                                                                                                  row[1].replace("'","`"),
                                                                                                  row[2].replace("'","`")))
connection.commit()

cursor.execute('''Select * from Products;''')
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.execute('''Select * from Reviews;''')
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()



