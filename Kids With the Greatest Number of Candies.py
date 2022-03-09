# Kids With the Greatest Number of Candies
candies = [2,3,5,1,3]
extraCandies = 3

# solution 1
maxCandy = max(candies)
ans = []
for i in range(len(candies)):
    if candies[i]+extraCandies>=maxCandy:
        ans.append(True)
    else:
        ans.append(False)
print(ans)

# Solution 2
maxCandy = max(candies)-extraCandies
ans = []
for candy in candies:
    if candy>=maxCandy:
        ans.append(True)
    else:
        ans.append(False)
print(ans)
