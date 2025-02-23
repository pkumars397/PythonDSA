#decorator used to modify the function behaviour
#allow us to modify the behaviour of functions without changing their code

def my_decorator(func):
    def wrapper():
        print("Executing function---")
        func()
        print("Function Execution Finishded---")
    return wrapper
#to use decorator we use @nameofDecorator beffore func name
@my_decorator #applying deco to greet func
def greet():
    print("Hello World!")
greet()