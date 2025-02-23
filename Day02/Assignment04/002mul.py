# first multiple of 7
n=int(input("enter n:"))
r=0
for i in range(1,n+1):
 if i<n:
   continue;
 else:
   r=i%7
print(r)

print(f"First Multiple of 7 after 50 is {n+(7-r)}")

