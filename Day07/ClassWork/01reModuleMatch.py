#Regular Expression pattern matching using re module ,regular expression module
import re
pattern=f"Hello"
text="Hello,welcome to Regex!"
#match ,find the pattern at the beginning of string.
match_obj=re.match(pattern,text)

print(match_obj)
if match_obj:
    print("Match Found: ",match_obj.group())
else:
    print("Match Not found!")