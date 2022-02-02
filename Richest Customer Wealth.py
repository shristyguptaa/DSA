# Richest Customer Wealth
accounts = [[1,2,3],[3,2,1]]

# Solution 1
maxWealth = 0
for account in accounts:
    wealth = 0
    for money in account:
        wealth+=money
    maxWealth = max(maxWealth,wealth)
    """
    if wealth > maxWealth:
        maxWealth = wealth
    """
print (maxWealth)

# Solution 2
maxWealth = 0
for account in accounts:
    wealth = sum(account)
    maxWealth = max(maxWealth,wealth)
    """
    if wealth > maxWealth:
        maxWealth = wealth
    """
print (maxWealth)

# Solution 3
print (max([sum(account) for account in accounts]))
