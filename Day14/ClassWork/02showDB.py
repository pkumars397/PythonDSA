import mysql.connector
print("Hello world!")
mysqlDB=mysql.connector.MySQLConnection(
    host="localhost",
    port="3306",
    user="root",
    password="rps@123"
)
mycursor=mysqlDB.cursor()

mycursor.execute("show databases")
for x in mycursor:
    print(x)