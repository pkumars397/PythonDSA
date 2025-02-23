#taking input
name=input("Enter your name : ")
print("hello",name)

age=int(input("enter your age: "))
height=float(input("Enter your height in meters; "))

print("Your age is",age)

print("your height is : ",height,"meters")

#printing multiple items
name="Alice"
age=25
print("Name: ",name,"age",age)

#using sep
print("hello ","world","ji",sep="-")

#using end
print("hello",end="...")
print("world!")

#concat
name="pk"
age=24
print("My name is "+name+"I am "+str(age)+"years old")

#.format
print("my name is {} and i am {} years old".format(name,age))

#fstrings
print(f"my name is {name} and i am {age} years old")
