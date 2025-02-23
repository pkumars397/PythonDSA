#Iterator is efficient way to loop over data
#object which allow to loop through elements one by one
#each call to next() fetches next item
#if all time is accessed then it will raise stopIteration error

my_list=[1,2,3,4]
iterator=iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) #will throw stopiteration error