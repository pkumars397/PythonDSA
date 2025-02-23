#largest digit in number
n=int(input("enter a number: "))
l=0
while n:
 digit=n%10
 n=n//10
 l=max(digit,l)
print(f"Largest digit: {l}")

