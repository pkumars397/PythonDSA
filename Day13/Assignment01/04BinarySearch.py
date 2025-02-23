def BS(a,target):
    left,right=0,len(a)-1
    while left<=right:
        mid=(left+right)//2
        if a[mid]==target:
            return mid
        elif a[mid]<target:
            left=mid+1 #reduce search space

        else:
            right=mid-1

    return -1

arr=[1,2,2,3,4,5,6,7]
target=6
print(f"{target} found at {BS(arr,target)}th index")