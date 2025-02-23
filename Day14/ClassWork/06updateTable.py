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

# mycursor.execute(
#     '''
#     update table customer set name="Prashu" where name="Prashant"
# '''
# )
# mysqlDB.commit()

#showing datas
mycursor.execute('''
 select * from customer
                 ''')
rows=mycursor.fetchall()
for row in rows:
    print(row)
mycursor.close()