import mysql.connector
print("Hello world!")
mysqlDB=mysql.connector.MySQLConnection(
    host="localhost",
    port="3306",
    user="root",
    password="rps@123",
    database="APPDB"
)

print("Connection establish")

mycursor=mysqlDB.cursor()
mycursor.execute('''
create table StudentData(
    student_id int primary key,
    name varchar(40),
    roll_no int,
    subject varchar(40),
    result varchar(40)             
                 )
''')