def second_largest(l):
   sl=0
   largest=l[0]
   for item in l:
      if item>largest:
         sl=largest
         largest=item
      elif item>sl:
            sl=item
   return sl 
n=[-10,5,2,4]
print(second_largest(n))