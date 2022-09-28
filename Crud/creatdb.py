import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Password@123"
    )
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE testdb")
mydb.close()