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

id=(input("Enter your id: "))
name=input("Enter your Name: ")
roll=int(input("enter your roll number: "))
subject=input("Enter your subject name: ")
marks=int(input("Enter your marks percentage: "))

query='''insert into StudentData values(%s,%s,%s,%s,%s)'''

res="Pass"
if marks<30:
    res="Fail"

values=(id,name,roll,subject,res)

mycursor.execute(query,values)

# mycursor.execute('''truncate table StudentData''')
mysqlDB.commit()