#to match Python in two strings
import re 
pattern=r"Python"
text1,text2="Python is Awesome!","I love Python"
match1,match2=re.match(pattern,text1),re.match(pattern,text2)
sMatch1,sMatch2=re.search(pattern,text1),re.search(pattern,text2)

if match1:
    print("Matched pattern ",match1.group())
else:
    print("Match not found")
if match2:
    print("Matched pattern ",match2.group())
else:
    print("Match not found")
if sMatch1:
    print("Matched pattern ",sMatch1.group())
else:
    print("not found")
if sMatch2:
    print("Matched pattern ",sMatch2.group())
else:
    print("Not found!")