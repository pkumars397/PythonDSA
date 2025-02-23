def isPalindrome(s):
    return s==s[::-1]

# s="prashant"
# # s[intitialIndex,lastindex,step]
# ns=s[::-1]

s=input("enter the string: ")
if (isPalindrome(s)):
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")