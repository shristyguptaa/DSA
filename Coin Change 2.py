# Coin Change 2
amount = 5
coins = [1,2,5]
lst = [0 for i in range(amount+1)]
# lst = [0]*(amount+1)
lst[0]=1
for coin in coins:
    for i in range(coin,len(lst)):
        # if i>= coin:
            lst[i]+=lst[i-coin]
print (lst[-1])
