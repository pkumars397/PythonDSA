#sum of digits
n=int(input("enter number:"))
total=0

while n:
 digit=n%10
 n=n//10
 total+=digit
print(f"Sum of digits : {total}")
