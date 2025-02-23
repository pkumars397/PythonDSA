#print binary
n=int(input("enter number: "))
bin=""
while n:
  bit=n%2
  bin=bin+str(bit)
  n=n//2
  
print(f"binary rep: {bin}")
  
