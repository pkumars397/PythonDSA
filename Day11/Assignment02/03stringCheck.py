import re
pattern=r"^[a-zA-Z]+$"
text=input("enter ur string: ")
matchObj=re.search(pattern,text)
if matchObj:
    print("Its contains only albhabets")
else:
    print("it is no completely alphabets")