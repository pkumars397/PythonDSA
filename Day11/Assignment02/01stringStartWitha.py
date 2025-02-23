import re
pattern=r"^a"
text=input("enter ur string: ")

matchObj=re.match(pattern,text,re.IGNORECASE)
if matchObj:
    print(f"its starts with a")
else:
    print("Its didn't start with a")