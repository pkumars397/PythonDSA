#fib num
n=int(input("Enter N: "))

f1=0
f2=1
print(f1)
print(f2)
for i in range(1,n-1):
  nextN=f1+f2
  print(f"{nextN}")
  f1=f2
  f2=nextN

  

  
