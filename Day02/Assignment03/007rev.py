#reverse a num
n=int(input("enter a number:"))
rev=0
while n:
 digit=n%10
 n=n//10
 rev=rev*10+digit
print(f"Reverse: {rev}")

