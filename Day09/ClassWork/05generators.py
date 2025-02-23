#generators: create an iterator without writing a class
#uses yield (instead of return ) : to produce value one at a time
#next()

def countdown(start):
    while start>0:
        yield start #yield current value,suspending func execution 
        start-=1 #decrement the count

#create a generator
gen=countdown(5)

#use next() to get value
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) #StopIteraiton error

'''             iterator                                    generator
creation:  useing a class with __iter__ and __next__    uses a function wiht yield

memoryUse: stores all values in memory               generatre value on demand(efficient)

complexity: more complex ,requires a class          simple ,require only a function
'''