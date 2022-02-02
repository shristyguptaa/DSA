# Shuffle the Array
nums = [2,5,1,3,4,7]
n = 3

# Solution 1
n1 = nums[:n]
n2 = nums[n:]
out = []
for i in range(n):
    out.append(nums[i])
    out.append(nums[n+i])
print (out)

# Solution 2
out = []
for i in range(n):
    out.append(n1[i])
    out.append(n2[i])
print (out)
