class OddNumber:
    def __init__(self,n):
      self.n=n
      self.current=1 
    def __iter__(self):
      return self 
    def __next__(self):
      if self.current>self.n:
        raise StopIteration 
      Value=self.current
      self.current+=2
      return Value
      
oddNum=OddNumber(10)
for num in oddNum:
  print(num)