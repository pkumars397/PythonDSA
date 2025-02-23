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

myCursor=mysqlDB.cursor()
operation=(input("You want to Add something to table or not?(Y/N)"))

if operation=="Y":
   name=input("Enter the user name: ")
   address=(input("Enter Your age: "))
   data=int(input("Enter your data code: "))
   query='''Insert into customer(name,address,Data) value(%s,%s,%s)'''
   values=(name,address,data)

   myCursor.execute(query,values)
   mysqlDB.commit()

print("end")
