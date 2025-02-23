#filter use to get new list based on conditions
#it will apply condition on each items but only returns items in list which is true
num=[1,2,3,4,5]
evenNum=list(filter(lambda x:x%2==0,num))
print(evenNum)