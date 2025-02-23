#n armstrng number
import math
n=int(input("enter n:"))
i=100
while n:
 #check for armstrng number
 s=str(i)
 total=sum(math.pow(int(s[i]),len(s)) for i in range(len(s)))
 if total==int(i):
   print(i)
   n-=1
 i+=1
