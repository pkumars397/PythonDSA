import re 
pat=r"python"
text1,text2="I love Python","PYTHON is powerful"
m1,m2=re.search(pat,text1,re.IGNORECASE),re.search(pat,text2,re.IGNORECASE)

if m1:
     print("matched word: ",m1.group())
else: 
     print("Didn't matched")
if m2:
     print("matched word: ",m2.group())
else: 
     print("Didn't matched")