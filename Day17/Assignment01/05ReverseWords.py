def reverseWords( s: str) -> str:
      words=s.split() #will return list of words
      ans=""
      for i in range(len(words)-1,-1,-1): #iterating from back of word list
        if i>0: #if i!=0 then only space
         ans=ans+words[i]+" "
        else:
         ans=ans+words[i]
      return ans

s="the sky is blue"
print(reverseWords(s))