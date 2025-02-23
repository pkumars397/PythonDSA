def min_coins(coins,amount):
    coins.sort(reverse=True)
    count=0
    for coin in coins:
        while amount>=coin:
            amount-=coin
            count+=1
    return count

coins=[1,5,10,25]
print(min_coins(coins,30)) #output: 2