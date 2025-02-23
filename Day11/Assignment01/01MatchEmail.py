import re 
EmailPattern=r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
txt="Hello this is my email my-email123_@sub-domain.uk"
matchedObj=re.search(EmailPattern,txt)
if matchedObj:
    print("Matched Email: ",matchedObj.group())
else:
    print("Email not matched")