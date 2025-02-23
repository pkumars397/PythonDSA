#sum of digits
n=int(input("Enter a three digit number: "))
digitSum=n%10
n=n//10
digitSum=digitSum+n%10
n=n//10
digitSum=digitSum+n%10
print(f"Sum of digits: {digitSum}")
