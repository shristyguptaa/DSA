# Find Pivot Index
nums = [1,7,3,6,5,6]
totalSum = sum(nums)
leftSum = 0
for i in range(len(nums)):
    rightSum = totalSum - leftSum - nums[i]
    if leftSum == rightSum:
        print(i)
    leftSum += nums[i]
print(-1)
