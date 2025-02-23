import mysql.connector
print("Hello world!")
mysqlDB=mysql.connector.MySQLConnection(
    host="localhost",
    port="3306",
    user="root",
    password="rps@123"
)

print("Connection establish")
print(mysqlDB)

mycursor=mysqlDB.cursor()
mycursor.execute("CREATE DATABASE PRASHANT")
print("Dataabase created!")
