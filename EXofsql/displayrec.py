import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Password@123",
    database="PRIYANKA"
    )
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM RESULT")
result=mycursor.fetchall()
for i in result:
    subject=i[0]
    totalmarks=i[1]
    obtainmarks=i[2]
    print(subject,totalmarks,obtainmarks)
mydb.close()