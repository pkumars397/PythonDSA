def productExceptSelf( nums: list[int]) -> list[int]:
        prefix=[0]*len(nums)
        prefix[0]=1
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        suffix=[0]*len(nums)
        suffix[len(nums)-1]=1
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            nums[i]=prefix[i]*suffix[i]
        return nums


n=[1,2,3,4,5]
print(productExceptSelf(n))