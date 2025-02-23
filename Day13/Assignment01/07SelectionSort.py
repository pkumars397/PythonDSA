def selectionSort(a):
    for i in range(len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
        if min!=i:
            a[min],a[i]=a[i],a[min]
    return a


n=[1,10,19,3,2,6,22]
print(f"Sorted List: ",selectionSort(n))