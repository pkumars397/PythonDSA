def linearSearch(num,target):
    for item in num:
        if item==target:
            return num.index(item)
    return -1

n=[1,2,10,12,9,8]
target=10
print(linearSearch(n,target))