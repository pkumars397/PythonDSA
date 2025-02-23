#iterators: object that can be iteratized upon
#__iter__(): return iterator object
#__next__(): return the next value from iterator,raises StopIteration at end

nums=[1,2,3,4,5]
iterator=iter(nums) #get an iterator from list
#get elements one by one
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))