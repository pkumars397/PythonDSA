import re
pattern=r"\.com$"
text=input("enter ur string: ")
matchObj=re.search(pattern,text)
if matchObj:
    print(f"it ends with .com")
else:
    print("Tts didn't end with .com")