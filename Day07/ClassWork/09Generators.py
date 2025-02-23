#use yeild instead of return 
#doesn't store all values in memery
def count_up(start,end):
    while start<=end:
        yield start 
        start+=1 
for num in count_up(1,5):
    print(num)