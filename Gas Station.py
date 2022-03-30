# Gas Station
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

# Naive Solution
if sum(gas)<sum(cost):
    return -1
n = len(gas)
tmp = -1
for i in range(len(gas)):
    tank = 0
    if gas[i]<cost[i]:
        continue
    for j in range(i,i+n+1):
        j = j%n
        tank += gas[j]
        if tank>=cost[j]:
            tank -= (cost[j])
            if tank<0:
                break
        else:
            break
        if j==i:
            if tmp == j:
                return j
            else:
                tmp = j
return -1

# Optimised Solution
if sum(gas) < sum(cost):
    return -1

total = 0
res = 0
for i in range(len(gas)):
    total += (gas[i]-cost[i])
    if total < 0:
        total = 0
        res = i+1
return res
