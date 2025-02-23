def first(haystack,needle):
    if needle in haystack:
            return haystack.index(needle)
    return -1

s1="leetcode"
s2="leeto"
s3="leet"
print(first(s1,s3))
