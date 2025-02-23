import re 
text="Ehllo my email is pkumars397@gmail.com"
matchPattern=r"\w+@\w+\.\w+"
newTxt=re.sub(matchPattern,"Its okay",text)
print(newTxt)