dummyStr=input("Enter you Dummy string: ")
def nonRepeatingChar(s):
    dct={}
    for c in s:
        if c not in dct:
            dct[c]=1
        else:
            dct[c]+=1
    for key,val in dct.items():
        if val==1:
            return key

print(f"First nonRepeatingChar in {dummyStr} is: {nonRepeatingChar(dummyStr)}")