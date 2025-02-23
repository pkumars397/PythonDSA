n=int(input("Enter Your number: "))
n=str(n)
rev=""
for char in n: 
    rev=char+rev
print(f"Reversed Number is: {int(rev)}")