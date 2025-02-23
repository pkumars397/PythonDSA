#creatign decorator
def modify(modifier): 
 def uppercase_decorator(func):
    def wrapper(*args,**kwarg):
      res=func(*args,**kwarg)
      return modifier(res)
    return wrapper 
 return uppercase_decorator

@modify(lambda x:x.upper())
def say_something():
    return "hello world"
print(say_something())