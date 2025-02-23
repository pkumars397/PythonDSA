#set 
fruits={"Apple","Banana","Cheery","Apple","Banana"}
print(fruits)

#print(fruits[0]) error

fruits.add("Mango")
print(fruits)
fruits.remove("Banana")
print(fruits)

fruits.discard("Pineapple") #will not give error
print(fruits)

for fruit in fruits:
 print(fruit)
 
#set operations
set1={1,2,3,4}
set2={3,4,5,6}
print(set1 | set2)
print(set1 & set2)
print(set1 -set2)
print(set1 ^ set2)

if "Apple" in fruits:
  print("Apple is in the set")
