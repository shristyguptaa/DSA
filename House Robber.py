# House Robber
nums = [1,2,3,1]
r1 = r2 = 0
for n in nums:
    temp = max(r1+n,r2)
    r1 = r2
    r2 = temp
print (r2)
