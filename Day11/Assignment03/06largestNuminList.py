import re
listOfNum=[]
n=int(input("Enter number of strings u want to append in list: "))
for i in range(n):
    listOfNum.append(input())
maxi=listOfNum[0]
for item in listOfNum:
    if item>maxi:
        maxi=item

print(f"Maximum in list is ",maxi)