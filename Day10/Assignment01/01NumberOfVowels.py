def count_vowels(s):
    count=0
    for char in s:
        if char in "aeiouAEIOU":
            count+=1
    return count 
txt=input("Enter The String: ")
print(count_vowels(txt))