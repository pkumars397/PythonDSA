import re
pattern=r"\s."
text=input("enter ur string: ")
newText=re.sub(pattern,"-",text)

print(newText)