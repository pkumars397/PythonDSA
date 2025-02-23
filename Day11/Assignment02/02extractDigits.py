import re
pattern=r"\d+"
text=input("enter ur string: ")
matchList=re.findall(pattern,text)
print(matchList)