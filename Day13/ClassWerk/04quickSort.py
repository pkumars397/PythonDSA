def quickSort(arr):
    if len(arr)==1:
        return arr
    pivot=arr[len(arr)//2]
    left=[arr[i] for i in range(len(arr)) if arr[i]<pivot]
    right=[arr[i] for i in range(len(arr)) if arr[i]>pivot]
    mid=[arr[i] for i in range(len(arr)) if arr[i]==pivot]

    return quickSort(left)+mid+quickSort(right)

a=[10,7,8,11,15]
print(quickSort(a))