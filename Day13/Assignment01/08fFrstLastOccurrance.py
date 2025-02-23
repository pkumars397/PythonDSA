#First and last occurance of a target

def firstOccurance(l,target):
    left,right=0,len(l)-1
    index=-1
    while left<=right:
        mid=(left+right)//2
        if l[mid]==target:
            index=mid
            right=mid-1
        elif l[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return index

def lastOccurance(l,target):
    left,right=0,len(l)-1
    index=-1
    while left<=right:
        mid=(left+right)//2
        if l[mid]==target:
            index=mid
            left=mid+1
        elif l[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return index


l=[1,2,3,4,5,5,5,6]
target=5

print(f"First Occurance and last Occurance of {target} in {l} : {firstOccurance(l,target)}th index and {lastOccurance(l,target)}th index ")