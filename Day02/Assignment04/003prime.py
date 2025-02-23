#check for prime
n=int(input("enter number:"))
if n==2: 
 print(f"{n} is a prime number")
else:
 isprime=True
 for i in range(2,n):
  if n%i==0:
    isprime=False
    break 
 if isprime==True:
   print(f"{n} is a prime number")
 else:
   print("Not a prime")
