def maxiNum(l):
    maxi=l[0]
    for item in l:
        if item>maxi:
            maxi=item
    return maxi 

print("Enter the list Items: ")
n=int(input("enter the length of list: "))
numList=[]
for i in range(n):
    numList.append(int(input()))

print(f"Maximum in list: ",maxiNum(numList))