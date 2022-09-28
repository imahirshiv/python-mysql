import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Password@123",
    database="testdb"
    )
mycursor=mydb.cursor()
sql = "INSERT INTO student (roll, name, marks) VALUES(%s, %s, %s)"
val = [
    (1,'Ahir Shivkumar',95),
    (2,'Yadav Abhishek',53),
    (3,'Shah Ritik',52),
    (4,'Singh Manish',80),
    (5,'Tank Vijay',100),
    (6,'Rajput Abhishek',60),
    (7,'Giri Karan',60),
    (8,'Maurya Dharmendra',85),
    (9,'Patel Yash',52)
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "Record inserted successfully...")
mydb.close()