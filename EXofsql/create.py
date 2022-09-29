from sqlite3 import Cursor
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Password@123"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE PRIYANKA")
mydb.close()