def isPrime(n):
    if n<2:
        print("Not a Pirme Number")
        exit()
    isprime=True
    for i in range(2,n):
        if n%i==0:
            isprime=False
            break
    if isprime:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")

n=int(input("enter n"))
isPrime(n)