import re
listOfNum=[]
n=int(input("Enter number of strings u want to append in list: "))
for i in range(n):
    listOfNum.append(int(input()))
print(f"Reversed list is {listOfNum[::-1]}")# listOfNum.reverse()