def maxArea(height: list[int]) -> int:
        left,right=0,len(height)-1
        maxArea=0
        while left<=right:
            if height[left]<height[right]:
               tempArea=(right-left)*height[left]
               left+=1
               maxArea=max(maxArea,tempArea)
            else:
                tempArea=(right-left)*height[right]
                right-=1
                maxArea=max(maxArea,tempArea)
        return maxArea
            
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))