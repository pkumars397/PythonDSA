#discount
bill=float(input("Enter the bill amount: "))
discount=0
if bill>=5000:
  discount=bill*0.20
  
else:
 discount=bill*0.10
print(f"You get a {discount}% discount! pay {bill-discount}")

