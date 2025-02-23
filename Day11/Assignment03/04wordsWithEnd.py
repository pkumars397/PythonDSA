import re
listOfStr=[]
n=int(input("Enter number of strings u want to append in list: "))
for i in range(n):
    listOfStr.append(input())

pattern=r"\b\w+ing\b"
for string in listOfStr:
    matchObj=re.findall(pattern,string)
    if matchObj:
      print(f"{string} has words with end ing :{matchObj}")
    else:
      print(f"{string} has no words with end ing")