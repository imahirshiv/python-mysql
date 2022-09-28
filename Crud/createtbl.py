import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Password@123",
    database="testdb"
    )
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE student(roll INT,name VARCHAR(255),marks INT)")
mydb.close()