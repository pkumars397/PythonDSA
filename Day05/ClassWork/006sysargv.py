import sys
argList=sys.argv
print(f"Script name: {argList[0]}")
if len(argList)>1:
 print(f"Arguments Passed: {argList[1:]}")
else:
 print(f"Opps there no arguments!")

