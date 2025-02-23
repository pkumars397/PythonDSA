def searchRange( nums: list[int], target: int) -> list[int]:
        def first(nums,target):
            index=-1
            l,r=0,len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target: # 1 2 2 2 3 4 ,t=2
                    index=mid
                    r=mid-1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return index

        def last(nums,target):
            index=-1
            l,r=0,len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    index=mid
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return index
        return [first(nums,target),last(nums,target)]

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))