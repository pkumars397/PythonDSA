def reverseVowels( s: str) -> str:
        s=list(s) #first converted into list ,coz u of mutability
        left,right=0,len(s)-1 #pointers for iterating over our string
        vowelsString="aeiouAEIOU" #vowelstring for checking char is vowel or not
        while left<right:
           #if left char is not vowel,move pointer left by 1
           if left<right and s[left] not in vowelsString:
            left+=1
           #if right char is not vowel,move pointer right by 1
           if left<right and s[right] not in vowelsString:
            right-=1
           #if both left and right chars are vowel then swap them,and move pointers also.
           if s[left] in vowelsString and s[right] in vowelsString:
             s[left],s[right]=s[right],s[left]
             left+=1
             right-=1
        return "".join(s) #finally convert that list into string.

s = "IceCreAm"
print(reverseVowels(s))