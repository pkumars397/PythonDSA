import re 
pat=r"\d{2}[/]\d{2}[/]\d{4}"
text="Today's Date is 12/05/2023 and yesterday was 11/05/2023"
m=re.findall(pat,text)
print(m)