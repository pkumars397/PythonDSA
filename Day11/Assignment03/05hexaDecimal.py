import re
listOfNum=[]
n=int(input("Enter number of strings u want to append in list: "))
for i in range(n):
    listOfNum.append(input())

pattern=r"^(0x)?[0-9A-Fa-f]+$"
for string in listOfNum:
    matchObj=re.match(pattern,string)
    if matchObj:
        print(f"{string} is hexadecimal")
    else:
        print(f"{string} not a hexadecimal")