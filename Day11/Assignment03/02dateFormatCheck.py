import re
listOfDates=[]
n=int(input("Enter number of dates u want to append in list: "))
for i in range(n):
    listOfDates.append(input())

pattern=r"^\d{2}/\d{2}/\d{4}$"
for d in listOfDates:
    matchObj=re.match(pattern,d)
    if matchObj:
        print(f"{d} is valid date format")
    else:
        print(f"{d} not valid date")