import re
pattern=r"^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9.]+\.[a-zA-Z0-9]+$"
text=input("enter ur email: ")
matchObj=re.match(pattern,text)
if matchObj:
    print("valid Email")
else:
    print("Invalid Email")