class CountDown:
    def __init__(self,start):
        self.current=start #Initialize counter
    
    def __iter__(self):
        return self #return the iterator object itself
    
    def __next__(self):
        #decrease the count and return the cureent number
        #when count reaches zero ,StopIteration is raised
        if self.current<=0:
            raise StopIteration #when it reaches zero
        self.current-=1
        return self.current+1
    
counter=CountDown(5)

print(next(counter))#5
print(next(counter))#4
print(next(counter))#3
print(next(counter))#2
print(next(counter))#1
print(next(counter))#stopiteration error