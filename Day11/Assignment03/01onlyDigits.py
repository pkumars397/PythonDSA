import re
listOfStr=[]
n=int(input("Enter number of strings u want to append in list: "))
for i in range(n):
    listOfStr.append(input())

pattern=r"^\d+$"
for string in listOfStr:
    matchObj=re.match(pattern,string)
    if matchObj:
        print(f"{string} have only digits")
    else:
        print(f"{string} doesn't have only digits")