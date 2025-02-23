def logger(func):
    def wrapper():
        print("Function inside another function")
        func()
    return wrapper


@logger
def hello():
    print("Hello!")
hello()