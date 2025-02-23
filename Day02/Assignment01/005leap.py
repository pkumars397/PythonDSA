#Leap year check
year=int(input("Enter year: "))
if year%100==0:
  if year%400==0:
     pirnt(f"{year} is a leap year")
  else:
     print("Not a leap year")
elif year%4==0:
    print(f"{year} is a leap year")
else:
    print("not a leap year")
    
