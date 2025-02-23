import re 
pattern=r"\d+" #it will look for digit match

text="My numbers are 123,456,and 789"

#match function does matching at start for first matching orccurance
#search function does matching in entire str for first occurance of pattern
#findall() -finds all occurance of the pattern
#finditr()-details match objects 

#group() returns the matched text
#groups() returns all matches as tuple
#start() returns the start position of the match
#end() returns the end posttion of the match
#span() returns tuple ,(start,end) 
sObject=re.search(pattern,text)
match_obj=re.findall(pattern,text)

print(sObject.group())
print(match_obj) #returns the list of all match

for match in re.finditer(pattern,text):
    print(f"Match Found: {match.group()} at position {match.start()} to {match.end()}")
