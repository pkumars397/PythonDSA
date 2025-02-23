#smallest digit in number
n=int(input("enter a number: "))
l=10
while n:
 digit=n%10
 n=n//10
 l=min(digit,l)
print(f"Smallest digit: {l}")
