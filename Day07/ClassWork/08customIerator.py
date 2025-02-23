class CountUp:
 def __init__(self,start,end):
  self.current=start 
  self.end=end 
 def __iter__(self):
  return self 
 def __next__(self):
  if self.current>self.end:
    raise StopIteration 
  Value=self.current 
  self.current+=1 
  return Value

counter=CountUp(1,5)
print(counter)
for num in counter:
 print(num)