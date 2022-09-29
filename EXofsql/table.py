from sqlite3 import Cursor
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Password@123",
    database="PRIYANKA",
)
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE RESULT(subject VARCHAR(255),totalmarks INT,obtainmarks INT) ")
mydb.close()