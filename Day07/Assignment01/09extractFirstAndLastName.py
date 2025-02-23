import re 
pattern=r"\s+"
text="John Doe"
words=re.split(pattern,text)
print(f"First Name: {words[0]} Last Name: {words[1]}")