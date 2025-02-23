import mysql.connector
print("Hello world!")
mysqlDB=mysql.connector.MySQLConnection(
    host="localhost",
    port="3306",
    user="root",
    password="rps@123",
    database="MYTEST"
)

mycursor=mysqlDB.cursor()

mycursor.execute(
    '''
   create table customer(
   name varchar(40),
   age int
   )
'''
)

print("end")