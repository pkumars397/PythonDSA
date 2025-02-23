l=[]
n=int(input("Enter n: "))
for i in range(n-1):
    l.append(int(input()))

def missingNum(lst):
    sumN=(len(lst)+1)*((len(lst)+1+1))/2
    return sumN-sum(lst)

print(f"Missing Number in list is: {missingNum(l)}")