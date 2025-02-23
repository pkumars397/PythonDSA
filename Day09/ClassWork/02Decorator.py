#Decorator adds up some additional functionality for our function.
#for decorator to a func,just use @decoratorName

def my_deco(func):
    def wrapper():
        print("Something before our function call!")
        func()
        print("Something After our function Call!")
    return wrapper

#this will add my_deco decorator to print_Hello function.
@my_deco
def print_Hello():
    print("HEllo ")

print_Hello()
print_Hello()