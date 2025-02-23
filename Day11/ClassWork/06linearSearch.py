def lSearch(l,target):
   for i in range(len(l)):
      if l[i]==target:
         return i
   
   return -1

l=[1,2,3,5,1,10]
target=1
print(lSearch(l,target))