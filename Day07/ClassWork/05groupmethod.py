#group() --entire match
#group(1)--first group
#group(2)--second group
import re
pat=r"(\d{3})-(\d{3})-(\d{4})"
text="My Contact is 987-654-3210"
match_obj=re.search(pat,text)

if match_obj:
    print("Full Match:",match_obj.group(0))
    print("First Group ",match_obj.group(1))
    print("Second Group ",match_obj.group(2))
    print("Third Group ",match_obj.group(3))