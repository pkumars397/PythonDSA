#functions
def greet():
 print("Hello,Devs")

greet()
greet()

def add(a,b):
 return a+b

add(3,5)

def add_numbers(*numbers):
 return sum(numbers)
add_numbers(1,2,3,4)
#default parameter
def info(name="pk"):
 print(F"your name is {name}")
info("Binu")
info()

def show_details(**info):
  for k,v in info.items():
    print(f"{k}: {v}")

show_details(name="Prashant",age=24,country="india") #takes argument as dic

#lambda function
square=lambda x: x*x

print(square(4))
print(square(3))
