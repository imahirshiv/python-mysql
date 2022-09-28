import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Password@123",
    database="testdb"
    )
mycursor=mydb.cursor()
sql = "UPDATE student SET name='Nitin Kumar' WHERE roll=5"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "Record affected...")
mydb.close()