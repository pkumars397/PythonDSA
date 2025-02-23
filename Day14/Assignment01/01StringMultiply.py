def stringMul(num1,num2):
        num1,num2=num1[::-1],num2[::-1]
        res=[0]*(len(num1)+len(num2))

        if "0" in [num1,num2]:
            return "0"

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit=int(num1[i])*int(num2[j])
                res[i+j]+=digit
                res[i+j+1]+=res[i+j]//10
                res[i+j]%=10

        #10*10 ->>100 ,001 ,remove zero
        res,beg=res[::-1],0
        while beg<len(res) and res[beg]==0:
            beg+=1
        res=map(str,res[beg:])
        return "".join(res)

n1="123" 
n2="456"
print(stringMul(n1,n2))