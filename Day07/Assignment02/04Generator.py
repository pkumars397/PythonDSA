#generator for fibonacci numbers up to n

def fib(n):
    f1,f2=0,1
    while f1<=n:
        yield f1
        f1,f2=f2,f1+f2
for num in fib(10):
    print(num)