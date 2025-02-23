import re 
pat=r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,3}"
text="contact me at hello123@gmail.com or support@Company.org"
match_ob=re.findall(pat,text)
print(match_ob)