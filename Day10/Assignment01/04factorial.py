n=int(input("Enter the number: "))
fact=1
for i in range(2,n+1):
    fact*=i
print(f"Factorial of {n} is {fact}")