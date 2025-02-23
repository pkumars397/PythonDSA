#List ->> datatype to store various datatype data in list

fruits=["Apple","Banana","Cherry"]
number=[1,2,3,4,5]
mixed=["Hello",42,3.14,True]
print(fruits)
print(number)
print(mixed)

#Accessing listt
print(fruits[0])
print(fruits[1])
print(fruits[-2])

#modify list
fruits=["Apple","Banana","Cherry"]
fruits[1]="Blueberry"

print(fruits)

#Add and remove the items
fruits.append("Mango")
fruits.insert(1,"Orange")

print(fruits)

#removing items
fruits.remove("Blueberry")
last_fruit=fruits.pop()

print(fruits)
print("Last fruit removed",last_fruit)

#looping through list
for fruit in fruits:
 print(fruit)

for index,fruit in enumerate(fruits):
 print(index,fruit)
 
#slicing
n=[10,20,30,40,50]
print(n[1:4])
print(n[:3])
print(n[2:])
print(n[-3:])
print(n[::222222])

#checking list
if "Apple" in fruits :
 print("Apple is in the list")
