# Best Time to Buy and Sell Stock IV
k = 2
prices = [5,11,3,50,60,90]

# Solution 1
profit = [[0 for p in prices]for t in range(k+1)]
for t in range(1,k+1):
    for d in range(1,len(prices)):
        profit[t][d]=max(profit[t][d-1],max(profit[t-1][x]-prices[x]+prices[d]for x in range(d)))
for p in profit:
    print(p)

# Solution 2
if len(prices)==0:
    print(0)
profit=[[0 for p in prices]for i in range(k+1)]
for t in range(1,k+1):
    maxSoFar = float("-inf")
    for d in range(1,len(prices)):
        maxSoFar=max(maxSoFar,profit[t-1][d-1]-prices[d-1])
        profit[t][d]=max(profit[t][d-1],maxSoFar+prices[d])
print(profit)
