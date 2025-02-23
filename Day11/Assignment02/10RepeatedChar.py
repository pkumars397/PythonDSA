import re
pattern=r"(.)\1"
text=input("enter ur string: ")
matchObj=re.findall(pattern,text)
print(matchObj)