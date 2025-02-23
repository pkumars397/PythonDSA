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
insert into customer(name,age)
values
("Ankit",22),
("Abhishek",23),
("Binu",26),
("SOmi",20)
'''
)
mysqlDB.commit()