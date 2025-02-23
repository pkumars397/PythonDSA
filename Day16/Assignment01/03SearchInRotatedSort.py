def search(nums: list[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            #checking sorted part
            #left half sorted!
            if nums[left]<=nums[mid] :
                if nums[left]<=target and target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            #right half sorted
            else:
               if target<=nums[right] and target>=nums[mid]:
                  left=mid+1
               else:
                  right=mid-1
        return -1
n=[4,5,6,7,0,1,2]
target=0
print(search(n,target))