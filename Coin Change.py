# Coin Change
coins = [1,2,5]
amount = 11
lst = [float("inf") for i in range(amount+1)]
lst[0] = 0
for coin in coins :
    for i in range(coin,len(lst)):
        lst[i]=min(lst[i],lst[i-coin]+1)
if lst[-1]==float("inf"):
    print (-1)
print (lst[-1])
