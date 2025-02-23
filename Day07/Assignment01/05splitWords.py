import re
pat=r"\s+"
text="Python is fun"
result=re.split(pat,text)
print(f"Word list: {result}")