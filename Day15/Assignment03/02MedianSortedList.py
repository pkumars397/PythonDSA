def median(nums1,nums2):
        mergeList=[]
        i,j=0,0
        #i->[1,2,3,5]   j->[6,7,10,11]
        #[1] -> i=1 ->[1,2] ->i=2->[1,2,3]->i3->[1,2,3,5]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                mergeList.append(nums1[i])
                i+=1
            else:
                mergeList.append(nums2[j])
                j+=1

        while i<len(nums1):
            mergeList.append(nums1[i])
            i+=1
        while j<len(nums2):
            mergeList.append(nums2[j])
            j+=1

        # print(mergeList)
        # [1,2,3] ->mid ->(0+2)//2 or [1,2,3,4] ->mid=(0+3)//2->1
        left,right=0,len(mergeList)-1
        mid=(left+right)//2
        if len(mergeList)%2==0:
            return (mergeList[mid]+mergeList[mid+1])/2
        return mergeList[mid]

n1=[1,2]
n2=[3]
print(median(n1,n2))