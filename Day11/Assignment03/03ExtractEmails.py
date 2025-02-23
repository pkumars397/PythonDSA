import re
text=input("ente the text text: ")
pat=r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
matchList=re.findall(pat,text)
print(matchList)