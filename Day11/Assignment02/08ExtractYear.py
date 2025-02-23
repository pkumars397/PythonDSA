import re
pattern=r"\d{4}$"
text=input("enter ur date(dd-mm-yyyy): ")
matchObj=re.search(pattern,text)

print("Year is ",matchObj.group())