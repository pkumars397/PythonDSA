try :
 n1=int(input("enter n1: "))
 n2=int(input("enter n2: "))
 result=n1/n2
 print(result)
except ZeroDivisionError:
 print("You cann't divide by zero")
except ValueError:
 print("Please enter valid number")

