def repeat(n):
 def decorator(func):
    def wrapper():
        for i in range(n):
            func()
    return wrapper
 return decorator

@repeat(3)
def hello():
    print("Hello!")
hello()