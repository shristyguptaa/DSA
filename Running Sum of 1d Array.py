# Running Sum of 1d Array
nums = [1,2,3,4]

# Solution 1
out = []
next=0
for num in nums:
    next += num
    out.append(next)
print (out)

# Soluton 2
print ([sum(nums[:i]) for i in range(1,len(nums)+1)])
