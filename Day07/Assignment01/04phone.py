import re 
pat=r"(\d{3})-(\d{3})-(\d{4})"
valid_num="123-456-7890"
invalid_num="12345-67890"
m1=re.match(pat,valid_num)
m2=re.match(pat,invalid_num)
if m1:
    print("Valid phone ",m1.group())
else:
    print("Not a valid phone")
if m2:
    print("Valid phone ",m2.group())
else:
    print(invalid_num," Not a valid phone")