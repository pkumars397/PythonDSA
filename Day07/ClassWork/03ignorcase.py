import re 
pattern=f"regex" #matches one or more digits
text="Python supports Regex for pattern matching."
match_obj=re.search(pattern,text,re.IGNORECASE)
if match_obj:
    print("Matched Text: ",match_obj.group())
    print("Start Position:",match_obj.start())
    print("End Position: ",match_obj.end())
    print("Span: ",match_obj.span())
else:
    print("No Match Found!")