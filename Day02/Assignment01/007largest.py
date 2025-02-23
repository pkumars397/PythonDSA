#largest
print("enter three numbers: ")
n1=float(input())
n2=float(input())
n3=float(input())

if n1>n2 and n1>n3:
 print(f"{n1} is largest")
elif n2>n3 and n2>n1:
 print(f"{n2} is largest")
else:
 print(f"{n3} is largest")

