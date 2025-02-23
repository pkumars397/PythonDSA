import math
def gcdOfStrings( str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        return str1[:math.gcd(len(str1),len(str2))] #->str1=ABABAB ->str1[:gcd(6,4)]->str1[:2]->AB
        #ABCABC ->str1[:gcd(6,3)]->str1[:3] ->ABC

str1="ABABAB" 
str2="AB"
print(gcdOfStrings(str1,str2))