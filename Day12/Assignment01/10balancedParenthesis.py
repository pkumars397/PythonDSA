def is_balance(str):
    s=[]
    match={')':'(','}':'{',']':'['}
    for char in str:
        if char in match.values():
            s.append(char)
        elif char in match.keys():
            if len(s)==0 or s.pop()!=match[char]:
                return False 
    return len(s)==0

print(is_balance("{[()]}"))