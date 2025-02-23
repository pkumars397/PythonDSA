#n odd num

n=int(input("enter n: "))
i=1
while n!=0:
 if (i%2)==0:
  i+=1
  continue
 n-=1
 print(i)
 i+=1
