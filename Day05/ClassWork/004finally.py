try :
 n1=int(input("enter n1: "))
 n2=int(input("enter n2: "))
 result=n1/n2
except ZeroDivisionError:
 print("You cann't divide by zero")
except ValueError:
 print("Please enter valid number")
else:
 print(f"Result is : {result}")
finally: 
 print("Finally code execution completed")
