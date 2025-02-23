import re 
pat=r"#\w+"
text="Learning #Python is fun #code #100challenge "
matched=re.findall(pat,text)
print(matched)