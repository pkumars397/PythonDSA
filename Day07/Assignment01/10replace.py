import re 
text="This a bad example"
replaced=re.sub(r"bad","good",text)
print(replaced)