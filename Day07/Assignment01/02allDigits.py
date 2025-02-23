#findall will return list of all match
import re 
text="My Order numbers are 120,45 and 7890"
pat=r"\d+"
matchObj=re.findall(pat,text)
print("Matched digits list: ",matchObj)