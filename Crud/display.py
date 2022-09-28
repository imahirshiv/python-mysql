import imp
from unittest import result

import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='admin',
    password='Password@123',
    database='testdb'
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM student")
result=mycursor.fetchall()
for i in result:
    roll=i[0]
    name=i[1]
    marks=i[2]
    print(roll,name,marks)
mydb.close()