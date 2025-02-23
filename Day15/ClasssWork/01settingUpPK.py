import mysql.connector
print("Hello world!")
mysqlDB=mysql.connector.MySQLConnection(
    host="localhost",
    port="3306",
    user="root",
    password="rps@123",
    database="Prashant"
)

print("Connection establish")
# print(mysqlDB)

mycursor=mysqlDB.cursor()

#Adding Primary key in table

# mycursor.execute('''
#  create table customer(
#     id int auto_increment primary key,
#     name varchar(50),
#     address varchar(100)
#                          )
# ''')

#Adding Column in table
# mycursor.execute('''
# alter table customer add column Data int
# ''')

#inserting something into Table

# mycursor.execute('''
# insert into customer(name,address,Data)
# values("Prashant","Chapra",1000),
# ("Binu","Chapra",2000),
# ("Akash","gorkhpur",3000)
# ''')
# mysqlDB.commit()

#Delete something
mycursor.execute('''
delete from customer where id=8
''')
mysqlDB.commit()
print("end")

