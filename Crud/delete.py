import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Password@123",
    database="testdb"
    )
mycursor=mydb.cursor()
sql = "DELETE FROM student WHERE roll=3"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "RecordS deleted...")
mydb.close()