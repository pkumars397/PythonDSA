#prime or not
n=int(input("Enter a number: "))
if n==2: print("it is a prime")
isprime=True
for i in range(2,n):
  if n%i == 0:
    isprime=False
    break
if isprime:
 print(f"{n} is a prime number")
else:
 print(f"{n} is not a prime number")
