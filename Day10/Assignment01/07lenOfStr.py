s=input("Enter string: ")
def lenStr(s):
    count=0
    for char in s:
        count+=1
    return count

print(lenStr(s))