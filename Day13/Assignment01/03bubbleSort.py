#bubble sort in python 
def bubbleSort(l):
    for i in range(0,len(l)):
        for j in range(0,len(l)-i-1):
            if l[j]>l[j+1]:
               l[j],l[j+1]=l[j+1],l[j]
    # return l
numList=[10,1,-10,2,5,10]
bubbleSort(numList)
print(numList)