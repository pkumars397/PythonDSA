import sys
argList=sys.argv
if len(argList)!=3:
 print(f"Usage: python3 {" ".join(argList)}")
 sys.exit()
num1=int(argList[1])
num2=int(argList[2])
print(F"Sum of {num1} and {num2} is {num1+num2}")
