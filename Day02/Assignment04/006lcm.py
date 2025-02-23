#lcm of two numbers
import math
print("Enter two numbers: ")
n1=int(input())
n2=int(input())

print(f"LCM of {n1} and {n2} is {(n1*n2)/math.gcd(n1,n2)}")
