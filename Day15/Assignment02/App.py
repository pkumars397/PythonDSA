import mysql.connector
mysqlDB=mysql.connector.MySQLConnection(
    host="localhost",
    port="3306",
    user="root",
    password="rps@123",
    database="DummyDB"
)

print("Connection establish")

mycursor=mysqlDB.cursor()
mycursor.execute('''
create database IF NOT EXISTS DummyDB
''')

tablequery='''create table if not exists Customer(c_id int primary key,trans int,balance int)'''

mycursor.execute(tablequery)

cid=int(input("Enter Customer ID: "))
transAmnt=int(input("Enter the Transfer Amount: "))
bal=int(input("Enter Your Balance: "))

insertQ='''Insert into Customer values(%d,%d,%d)'''
values=(cid,transAmnt,bal)
mycursor.execute(insertQ,values)

