import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Password@123",
    database="PRIYANKA"
    )
mycursor=mydb.cursor()
sql = "INSERT INTO RESULT(subject,totalmarks,obtainmarks) VALUES(%s, %s, %s)"
val = [
    ('Gujarati',100,87),
    ('English',100,65),
    ('O.C',100,90),
    ('Econ.',100,95),
    ('Account',100,80),
    ('State',100,85),
    ('Computer',100,65),
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "Record inserted successfully...")
mydb.close()