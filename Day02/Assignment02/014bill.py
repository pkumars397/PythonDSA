#bill cal
u=float(input("enter the units consumed: "))
bill=0
if u<=100:
  bill=u*5
elif u>100:
  bill=100*5 +(u-100)*8
  
print(f"Your electricity bill is {bill}")
