def insertion_sort(arr):
    #traverse through 1 to len(arr)
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
         arr[j+1]=arr[j]
         j-=1
         arr[j+1]=key
arr=[12,4,5,19,1,7]
insertion_sort(arr)
print(arr)