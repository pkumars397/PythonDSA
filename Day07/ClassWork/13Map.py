#map()--applies function to each item in a list
#here lambda is func which we use on each item in list ,we will get new list
num=[1,2,3,4,5]
squaredList=list(map(lambda x:x*x,num))
print(squaredList)