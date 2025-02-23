#lets crate a decorator which will take function as argumnent and additional behaviour

def my_deco(func):
 def wrapper(*args,**kwargs):
  print("Function Calling Started..")
  res=func(*args,**kwargs)
  return res 
 return wrapper 

#now lest use the above decorator ,
@my_deco
def add(a,b):
 return a+b

#we can use same decorator to any number of functions
def multiply(a,b):
 return a*b 

print(add(3,5))
print(multiply(3,5))
