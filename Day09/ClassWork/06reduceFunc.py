#it returns a single value on a iterator
#syntax ,reduce(function,iterator,intialValue)

from functools import reduce
def add(a,b):
    return a+b
num=[1,2,3,4,5]
result=reduce(add,num,0)
print(result)

#aternativly can use lambda function also

result2=reduce(lambda x,y:x+y,num) #if u don't give initial value ,default 0 it assumes

print(result2)


#finding max 
maxi=reduce(lambda x,y:x if x>y else y,num)
print(maxi)

'''
(x,y)->(1,2)->(2,3)->(3,4)->(4,5)->5
'''