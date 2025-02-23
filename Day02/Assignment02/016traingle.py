#triangle
s1=int(input("Enter three sides: "))
s2=int(input())
s3=int(input())

if s1==s2  and s2==s3:
  print("It is equilateral triangle")
elif s1==s2 and s2!=s3:
  print("it is isosceles")
else:
  print("it is isolated triangle")
  
