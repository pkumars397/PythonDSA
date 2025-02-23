import re
pattern=r"^-?\d+(\.\d+)?$"
text=input("enter ur number in string format: ")
matchObj=re.match(pattern,text)
if matchObj:
    print(f"Valid number")
    exit()
print("Invalid Number")