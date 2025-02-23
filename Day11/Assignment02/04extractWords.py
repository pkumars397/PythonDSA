import re
pattern=r"\b\w+\b"
text=input("enter ur string: ")
matchObj=re.findall(pattern,text)
print(matchObj)