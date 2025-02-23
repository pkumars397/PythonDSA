def mergeAlternately( word1: str, word2: str) -> str:
        ans=""
        i,j=0,0 #two pointers to iterate on both strings
        #adding alternate characters ,till both string pointers is range
        # w1=ab w2=pqrs -> ""+w1[0]+w2[0]->ap+w1[1]+w2[1]->apbq,i reached end of w1
        #still w2 chars are left out to add
        while i<len(word1) and j<len(word2):
            ans=ans+word1[i]+word2[j]
            i+=1
            j+=1
        #adding remaining char if anything left in word1
        while i<len(word1):
            ans=ans+word1[i]
            i+=1
        #j=1,will add all remaining chars
        #adding remaining chars if lefted out in word2->apbq+w2[2]->apbqr+w2[3]->apbqrs
        while j<len(word2):
            ans=ans+word2[j]
            j+=1
        return ans

word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1,word2))