#Tuples
fruits=("Apple","Banana","Cherry")

numbers=(1,2,3,4,5)
mixed=("hello",42,3.14,True)
print(fruits)
print(numbers)
print(mixed)

#accessing the tuples
print(fruits[0])
print(fruits[1])
print(fruits[-1])

#modify tuple
#fruits[1]="Mango"

#slicing tuple
print(numbers[2:])
print(numbers[:4])

#tuple methods
print(fruits.count("Banana"))
print(fruits.index("Cherry"))

if "Apple" in fruits:
 print("Apple in the tuple")
