#used to reduce list into one single value
from functools import reduce
num=[1,2,4,5,6]
total=reduce(lambda x,y:x+y ,num)
print(total)