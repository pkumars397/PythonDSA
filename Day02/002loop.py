#for loop
for i in range(5):
 print("Hello,Python!")
 
#iterating over  a list
fruits=["Apple","banana","cherry"]
for fruit in fruits:
 print(fruit)
 
#while

count=1
while count<=5:
 print(f"Count : {count}")
 count+=1

for num in range(1,6):
 if num==3:
   continue
 print(num)

for num in range(1,6):
  if num==3:
   pass
  print(num)
