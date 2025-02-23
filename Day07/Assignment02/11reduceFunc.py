n=[1,2,3,4,5]
import functools
ans=functools.reduce(lambda x,y:x*y,n)
print(ans)