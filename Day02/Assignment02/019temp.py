#convert
temp=int(input("enter 1 for c to f ,enter 2 for f to "))
if temp==1:
 t=float(input("enter celsius"))
 ans=t*9/5+32
 print("temperature in fah",ans,"f")
else:
 t=float(input("enter fah"))
 ans=(t-32)*5/9
 print("temperature in cel",ans,"c")
 


