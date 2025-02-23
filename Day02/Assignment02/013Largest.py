#largest of three number:
print("Enter four numbers: ")
n1=float(input())
n2=float(input())
n3=float(input())
n4=float(input())

if n1>n2 and n1>n4 and n1>n3:
 print(f"{n1} is largest")
elif n2>n1 and n2>n3 and n2>n4:
 print(f"{n2} is largest")
elif n3>n1 and n3>n2 and n3>n4:
 print(f"{n3} is largest")
else:
 print(f"{n4} is largest")
