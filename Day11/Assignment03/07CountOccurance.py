import re
listOfNum=[]
n=int(input("Enter number of strings u want to append in list: "))
for i in range(n):
    listOfNum.append(int(input()))

print(listOfNum.count(2))